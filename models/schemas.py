from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Category schemas
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Product schemas
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    original_price: Optional[float] = None
    image_url: Optional[str] = None
    category_id: int
    sizes: Optional[str] = None  # JSON string
    colors: Optional[str] = None  # JSON string
    stock_quantity: int = 0
    is_featured: bool = False
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    original_price: Optional[float] = None
    image_url: Optional[str] = None
    category_id: Optional[int] = None
    sizes: Optional[str] = None
    colors: Optional[str] = None
    stock_quantity: Optional[int] = None
    is_featured: Optional[bool] = None
    is_active: Optional[bool] = None

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    category: Optional[Category] = None
    
    class Config:
        from_attributes = True

# Order schemas
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    size: Optional[str] = None
    color: Optional[str] = None

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    unit_price: float
    total_price: float
    product: Optional[Product] = None
    
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    shipping_address: Optional[str] = None
    billing_address: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class Order(OrderBase):
    id: int
    user_id: int
    status: str
    subtotal: float
    tax_amount: float
    shipping_amount: float
    total_amount: float
    created_at: datetime
    updated_at: Optional[datetime] = None
    order_items: List[OrderItem] = []
    
    class Config:
        from_attributes = True

# Cart schemas
class CartItem(BaseModel):
    product_id: int
    quantity: int
    size: Optional[str] = None
    color: Optional[str] = None

class Cart(BaseModel):
    items: List[CartItem]
    subtotal: float
    tax_amount: float
    shipping_amount: float
    total_amount: float