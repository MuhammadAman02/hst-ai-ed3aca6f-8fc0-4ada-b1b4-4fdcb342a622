import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from sqlalchemy.orm import Session
from core.database import SessionLocal, engine
from models.database import Base, Category, Product, User
from core.security import get_password_hash

# Create tables
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    
    try:
        # Create categories
        categories_data = [
            {"name": "Running", "description": "High-performance running shoes"},
            {"name": "Lifestyle", "description": "Casual and street-style footwear"},
            {"name": "Basketball", "description": "Professional basketball shoes"},
            {"name": "Football", "description": "Soccer and football cleats"},
            {"name": "Training", "description": "Cross-training and gym shoes"}
        ]
        
        categories = {}
        for cat_data in categories_data:
            existing_cat = db.query(Category).filter(Category.name == cat_data["name"]).first()
            if not existing_cat:
                category = Category(**cat_data)
                db.add(category)
                db.flush()
                categories[cat_data["name"]] = category.id
            else:
                categories[cat_data["name"]] = existing_cat.id
        
        # Create products
        products_data = [
            {
                "name": "Ultraboost 22",
                "description": "Experience incredible energy return with every step in the Ultraboost 22. Featuring responsive Boost midsole and Primeknit upper.",
                "price": 190.0,
                "original_price": 220.0,
                "image_url": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=500&h=500&fit=crop",
                "category_id": categories["Running"],
                "sizes": json.dumps(["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]),
                "colors": json.dumps(["Black", "White", "Blue"]),
                "stock_quantity": 50,
                "is_featured": True
            },
            {
                "name": "Stan Smith",
                "description": "The iconic tennis shoe that never goes out of style. Clean, classic design with premium leather construction.",
                "price": 80.0,
                "image_url": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?w=500&h=500&fit=crop",
                "category_id": categories["Lifestyle"],
                "sizes": json.dumps(["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]),
                "colors": json.dumps(["White/Green", "White/Navy", "All White"]),
                "stock_quantity": 75,
                "is_featured": True
            },
            {
                "name": "NMD_R1",
                "description": "Street-ready style meets modern comfort technology. Features Boost midsole and distinctive design elements.",
                "price": 140.0,
                "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop",
                "category_id": categories["Lifestyle"],
                "sizes": json.dumps(["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]),
                "colors": json.dumps(["Black", "White", "Red", "Blue"]),
                "stock_quantity": 40,
                "is_featured": True
            },
            {
                "name": "Gazelle",
                "description": "Retro-inspired sneaker with premium suede construction. A timeless classic with modern comfort.",
                "price": 90.0,
                "image_url": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500&h=500&fit=crop",
                "category_id": categories["Lifestyle"],
                "sizes": json.dumps(["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]),
                "colors": json.dumps(["Navy", "Black", "Gray", "Red"]),
                "stock_quantity": 60,
                "is_featured": False
            },
            {
                "name": "Superstar",
                "description": "The shell-toe legend that started it all. Iconic design with premium leather and rubber shell toe.",
                "price": 85.0,
                "image_url": "https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=500&h=500&fit=crop",
                "category_id": categories["Lifestyle"],
                "sizes": json.dumps(["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]),
                "colors": json.dumps(["White/Black", "All Black", "White/Gold"]),
                "stock_quantity": 80,
                "is_featured": True
            },
            {
                "name": "Alphaboost V1",
                "description": "Versatile running shoe for everyday training. Features Bounce midsole for responsive cushioning.",
                "price": 120.0,
                "original_price": 150.0,
                "image_url": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500&h=500&fit=crop",
                "category_id": categories["Running"],
                "sizes": json.dumps(["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]),
                "colors": json.dumps(["Black", "White", "Gray"]),
                "stock_quantity": 35,
                "is_featured": False
            },
            {
                "name": "Dame 8",
                "description": "Damian Lillard's signature basketball shoe. Built for explosive performance on the court.",
                "price": 110.0,
                "image_url": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500&h=500&fit=crop",
                "category_id": categories["Basketball"],
                "sizes": json.dumps(["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12", "13", "14"]),
                "colors": json.dumps(["Black/Red", "White/Blue", "All Black"]),
                "stock_quantity": 25,
                "is_featured": True
            },
            {
                "name": "Copa Mundial",
                "description": "The legendary football boot trusted by professionals worldwide. Premium kangaroo leather construction.",
                "price": 150.0,
                "image_url": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500&h=500&fit=crop",
                "category_id": categories["Football"],
                "sizes": json.dumps(["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]),
                "colors": json.dumps(["Black/White"]),
                "stock_quantity": 30,
                "is_featured": False
            }
        ]
        
        for product_data in products_data:
            existing_product = db.query(Product).filter(Product.name == product_data["name"]).first()
            if not existing_product:
                product = Product(**product_data)
                db.add(product)
        
        # Create admin user
        admin_email = "admin@adidas.com"
        existing_admin = db.query(User).filter(User.email == admin_email).first()
        if not existing_admin:
            admin_user = User(
                email=admin_email,
                hashed_password=get_password_hash("admin123"),
                first_name="Admin",
                last_name="User",
                is_admin=True
            )
            db.add(admin_user)
        
        # Create test user
        test_email = "test@example.com"
        existing_test = db.query(User).filter(User.email == test_email).first()
        if not existing_test:
            test_user = User(
                email=test_email,
                hashed_password=get_password_hash("test123"),
                first_name="Test",
                last_name="User",
                is_admin=False
            )
            db.add(test_user)
        
        db.commit()
        print("Database seeded successfully!")
        print("Admin user: admin@adidas.com / admin123")
        print("Test user: test@example.com / test123")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()