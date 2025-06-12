import json
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import database as db_models
from models.schemas import ProductCreate, ProductUpdate, OrderCreate, UserCreate
from core.security import get_password_hash
from core.utils import calculate_tax, calculate_total

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> db_models.User:
        # Check if user already exists
        db_user = db.query(db_models.User).filter(db_models.User.email == user.email).first()
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Create new user
        hashed_password = get_password_hash(user.password)
        db_user = db_models.User(
            email=user.email,
            hashed_password=hashed_password,
            first_name=user.first_name,
            last_name=user.last_name
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[db_models.User]:
        return db.query(db_models.User).filter(db_models.User.email == email).first()

class ProductService:
    @staticmethod
    def get_products(db: Session, skip: int = 0, limit: int = 100, category_id: Optional[int] = None) -> List[db_models.Product]:
        query = db.query(db_models.Product).filter(db_models.Product.is_active == True)
        if category_id:
            query = query.filter(db_models.Product.category_id == category_id)
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def get_product(db: Session, product_id: int) -> Optional[db_models.Product]:
        return db.query(db_models.Product).filter(
            db_models.Product.id == product_id,
            db_models.Product.is_active == True
        ).first()
    
    @staticmethod
    def create_product(db: Session, product: ProductCreate) -> db_models.Product:
        db_product = db_models.Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    
    @staticmethod
    def update_product(db: Session, product_id: int, product_update: ProductUpdate) -> Optional[db_models.Product]:
        db_product = db.query(db_models.Product).filter(db_models.Product.id == product_id).first()
        if not db_product:
            return None
        
        update_data = product_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_product, field, value)
        
        db.commit()
        db.refresh(db_product)
        return db_product
    
    @staticmethod
    def get_featured_products(db: Session, limit: int = 6) -> List[db_models.Product]:
        return db.query(db_models.Product).filter(
            db_models.Product.is_featured == True,
            db_models.Product.is_active == True
        ).limit(limit).all()

class OrderService:
    @staticmethod
    def create_order(db: Session, order: OrderCreate, user_id: int) -> db_models.Order:
        # Calculate order totals
        subtotal = 0.0
        order_items = []
        
        for item in order.items:
            product = db.query(db_models.Product).filter(db_models.Product.id == item.product_id).first()
            if not product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Product with id {item.product_id} not found"
                )
            
            if product.stock_quantity < item.quantity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Insufficient stock for product {product.name}"
                )
            
            item_total = product.price * item.quantity
            subtotal += item_total
            
            order_items.append({
                "product_id": item.product_id,
                "quantity": item.quantity,
                "size": item.size,
                "color": item.color,
                "unit_price": product.price,
                "total_price": item_total
            })
        
        tax_amount = calculate_tax(subtotal)
        shipping_amount = 10.0 if subtotal < 100 else 0.0  # Free shipping over $100
        total_amount = calculate_total(subtotal, shipping=shipping_amount)
        
        # Create order
        db_order = db_models.Order(
            user_id=user_id,
            subtotal=subtotal,
            tax_amount=tax_amount,
            shipping_amount=shipping_amount,
            total_amount=total_amount,
            shipping_address=order.shipping_address,
            billing_address=order.billing_address
        )
        db.add(db_order)
        db.flush()  # Get order ID
        
        # Create order items
        for item_data in order_items:
            db_order_item = db_models.OrderItem(
                order_id=db_order.id,
                **item_data
            )
            db.add(db_order_item)
            
            # Update product stock
            product = db.query(db_models.Product).filter(
                db_models.Product.id == item_data["product_id"]
            ).first()
            product.stock_quantity -= item_data["quantity"]
        
        db.commit()
        db.refresh(db_order)
        return db_order
    
    @staticmethod
    def get_user_orders(db: Session, user_id: int) -> List[db_models.Order]:
        return db.query(db_models.Order).filter(db_models.Order.user_id == user_id).all()
    
    @staticmethod
    def get_order(db: Session, order_id: int, user_id: Optional[int] = None) -> Optional[db_models.Order]:
        query = db.query(db_models.Order).filter(db_models.Order.id == order_id)
        if user_id:
            query = query.filter(db_models.Order.user_id == user_id)
        return query.first()

class CategoryService:
    @staticmethod
    def get_categories(db: Session) -> List[db_models.Category]:
        return db.query(db_models.Category).all()
    
    @staticmethod
    def create_category(db: Session, name: str, description: Optional[str] = None) -> db_models.Category:
        db_category = db_models.Category(name=name, description=description)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category