# Adidas Shoes Store - Backend API

A professional ecommerce backend API for Adidas shoes built with FastAPI, SQLAlchemy, and modern Python practices.

## Features

- **Authentication & Authorization**: JWT-based auth with user registration/login
- **Product Management**: Full CRUD operations for products with categories
- **Order Management**: Complete order processing with cart functionality
- **User Management**: User profiles and account management
- **Database**: SQLAlchemy ORM with SQLite (easily configurable for PostgreSQL)
- **Security**: Password hashing, JWT tokens, CORS support
- **API Documentation**: Auto-generated OpenAPI/Swagger docs
- **Production Ready**: Docker support, health checks, proper error handling

## Quick Start

### Local Development

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Set Environment Variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Run the Application**
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Docker Deployment

1. **Build and Run**
```bash
docker build -t adidas-store-api .
docker run -p 8000:8000 adidas-store-api
```

### Fly.io Deployment

1. **Install Fly CLI**
```bash
curl -L https://fly.io/install.sh | sh
```

2. **Deploy**
```bash
fly deploy
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### Products
- `GET /api/products/` - Get all products
- `GET /api/products/featured` - Get featured products
- `GET /api/products/{id}` - Get product by ID
- `POST /api/products/` - Create product (admin)
- `PUT /api/products/{id}` - Update product (admin)

### Orders
- `POST /api/orders/` - Create new order
- `GET /api/orders/` - Get user orders
- `GET /api/orders/{id}` - Get specific order

### Users
- `GET /api/users/profile` - Get user profile
- `PUT /api/users/profile` - Update user profile

## API Documentation

Visit `http://localhost:8000/docs` for interactive Swagger documentation.

## Database Schema

### Users
- User authentication and profile information
- Admin role support

### Products
- Product catalog with categories
- Pricing, inventory, and variants (sizes/colors)
- Featured products support

### Orders
- Complete order management
- Order items with product variants
- Order status tracking

### Categories
- Product categorization
- Hierarchical category support

## Configuration

Key environment variables:

```env
DATABASE_URL=sqlite:///./adidas_store.db
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
HOST=0.0.0.0
PORT=8000
```

## Security Features

- **Password Hashing**: bcrypt for secure password storage
- **JWT Authentication**: Stateless token-based auth
- **CORS Support**: Configurable cross-origin requests
- **Input Validation**: Pydantic models for request validation
- **SQL Injection Prevention**: SQLAlchemy ORM protection

## Frontend Integration

This API is designed to work with modern frontend frameworks:

- **CORS enabled** for React/Vue/Angular applications
- **RESTful design** with consistent response formats
- **Comprehensive error handling** with proper HTTP status codes
- **Pagination support** for large datasets

## Sample Data

To populate the database with sample Adidas products, run:

```python
python scripts/seed_data.py
```

## Testing

Run tests with:

```bash
pytest
```

## Production Considerations

- Use PostgreSQL for production database
- Set strong SECRET_KEY in production
- Configure proper CORS origins
- Enable HTTPS
- Set up monitoring and logging
- Use environment-specific configurations

## License

This project is for educational/demonstration purposes.