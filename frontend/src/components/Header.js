import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ShoppingCart, Search, Menu, X, User, LogOut } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { useCart } from '../contexts/CartContext';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isUserMenuOpen, setIsUserMenuOpen] = useState(false);
  const { user, logout, isAuthenticated } = useAuth();
  const { getCartItemsCount } = useCart();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    setIsUserMenuOpen(false);
    navigate('/');
  };

  const cartItemsCount = getCartItemsCount();

  return (
    <header className="bg-white shadow-sm border-b sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center">
            <Link to="/" className="text-2xl font-bold text-adidas-black">
              adidas
            </Link>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            <Link to="/products" className="text-gray-700 hover:text-adidas-black font-medium transition-colors">
              All Products
            </Link>
            <Link to="/products?category=Running" className="text-gray-700 hover:text-adidas-black font-medium transition-colors">
              Running
            </Link>
            <Link to="/products?category=Lifestyle" className="text-gray-700 hover:text-adidas-black font-medium transition-colors">
              Lifestyle
            </Link>
            <Link to="/products?category=Basketball" className="text-gray-700 hover:text-adidas-black font-medium transition-colors">
              Basketball
            </Link>
          </nav>

          {/* Right side icons */}
          <div className="flex items-center space-x-4">
            <button className="hidden sm:flex p-2 text-gray-700 hover:text-adidas-black transition-colors">
              <Search className="h-5 w-5" />
            </button>
            
            {/* User Menu */}
            {isAuthenticated ? (
              <div className="relative">
                <button 
                  onClick={() => setIsUserMenuOpen(!isUserMenuOpen)}
                  className="flex items-center space-x-2 p-2 text-gray-700 hover:text-adidas-black transition-colors"
                >
                  <User className="h-5 w-5" />
                  <span className="hidden sm:block text-sm font-medium">
                    {user?.first_name}
                  </span>
                </button>
                
                {isUserMenuOpen && (
                  <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50">
                    <Link 
                      to="/profile" 
                      className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      onClick={() => setIsUserMenuOpen(false)}
                    >
                      Profile
                    </Link>
                    <Link 
                      to="/orders" 
                      className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      onClick={() => setIsUserMenuOpen(false)}
                    >
                      Orders
                    </Link>
                    <button 
                      onClick={handleLogout}
                      className="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                    >
                      <LogOut className="h-4 w-4 inline mr-2" />
                      Logout
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <Link 
                to="/login" 
                className="hidden sm:flex p-2 text-gray-700 hover:text-adidas-black transition-colors"
              >
                <User className="h-5 w-5" />
              </Link>
            )}
            
            {/* Cart */}
            <Link 
              to="/cart" 
              className="relative p-2 text-gray-700 hover:text-adidas-black transition-colors"
            >
              <ShoppingCart className="h-5 w-5" />
              {cartItemsCount > 0 && (
                <span className="absolute -top-1 -right-1 bg-adidas-red text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                  {cartItemsCount}
                </span>
              )}
            </Link>
            
            {/* Mobile menu button */}
            <button 
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="md:hidden p-2 text-gray-700 hover:text-adidas-black transition-colors"
            >
              {isMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden border-t bg-white">
            <div className="px-2 pt-2 pb-3 space-y-1">
              <Link 
                to="/products" 
                className="block px-3 py-2 text-gray-700 hover:text-adidas-black font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                All Products
              </Link>
              <Link 
                to="/products?category=Running" 
                className="block px-3 py-2 text-gray-700 hover:text-adidas-black font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                Running
              </Link>
              <Link 
                to="/products?category=Lifestyle" 
                className="block px-3 py-2 text-gray-700 hover:text-adidas-black font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                Lifestyle
              </Link>
              <Link 
                to="/products?category=Basketball" 
                className="block px-3 py-2 text-gray-700 hover:text-adidas-black font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                Basketball
              </Link>
              
              {!isAuthenticated && (
                <Link 
                  to="/login" 
                  className="block px-3 py-2 text-gray-700 hover:text-adidas-black font-medium"
                  onClick={() => setIsMenuOpen(false)}
                >
                  Login
                </Link>
              )}
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;