import os
import uuid
from typing import Optional
from fastapi import UploadFile
import shutil

def save_upload_file(upload_file: UploadFile, destination_dir: str = "static/images") -> str:
    """Save uploaded file and return the file path."""
    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)
    
    # Generate unique filename
    file_extension = upload_file.filename.split(".")[-1] if upload_file.filename else "jpg"
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(destination_dir, unique_filename)
    
    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    
    return file_path

def format_currency(amount: float) -> str:
    """Format amount as currency."""
    return f"${amount:.2f}"

def calculate_tax(subtotal: float, tax_rate: float = 0.08) -> float:
    """Calculate tax amount."""
    return subtotal * tax_rate

def calculate_total(subtotal: float, tax_rate: float = 0.08, shipping: float = 0.0) -> float:
    """Calculate total amount including tax and shipping."""
    tax = calculate_tax(subtotal, tax_rate)
    return subtotal + tax + shipping