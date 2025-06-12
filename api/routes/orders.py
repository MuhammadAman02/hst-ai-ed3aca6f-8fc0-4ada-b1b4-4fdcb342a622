from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_active_user
from models.schemas import Order, OrderCreate, User
from services.business import OrderService

router = APIRouter()

@router.post("/", response_model=Order)
async def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new order."""
    try:
        db_order = OrderService.create_order(db, order, current_user.id)
        return db_order
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create order"
        )

@router.get("/", response_model=List[Order])
async def get_user_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all orders for the current user."""
    orders = OrderService.get_user_orders(db, current_user.id)
    return orders

@router.get("/{order_id}", response_model=Order)
async def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific order."""
    order = OrderService.get_order(db, order_id, current_user.id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order