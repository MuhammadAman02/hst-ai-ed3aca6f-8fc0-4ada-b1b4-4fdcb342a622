import React, { createContext, useContext, useState, useEffect } from 'react';
import toast from 'react-hot-toast';

const CartContext = createContext();

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
};

export const CartProvider = ({ children }) => {
  const [cartItems, setCartItems] = useState([]);

  // Load cart from localStorage on mount
  useEffect(() => {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
      try {
        setCartItems(JSON.parse(savedCart));
      } catch (error) {
        console.error('Error loading cart from localStorage:', error);
      }
    }
  }, []);

  // Save cart to localStorage whenever it changes
  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(cartItems));
  }, [cartItems]);

  const addToCart = (product, quantity = 1, size = null, color = null) => {
    setCartItems(prevItems => {
      const existingItem = prevItems.find(
        item => 
          item.id === product.id && 
          item.size === size && 
          item.color === color
      );

      if (existingItem) {
        toast.success(`Updated ${product.name} quantity in cart!`);
        return prevItems.map(item =>
          item.id === product.id && item.size === size && item.color === color
            ? { ...item, quantity: item.quantity + quantity }
            : item
        );
      } else {
        toast.success(`Added ${product.name} to cart!`);
        return [...prevItems, {
          ...product,
          quantity,
          size,
          color,
          cartId: `${product.id}-${size}-${color}` // Unique identifier for cart item
        }];
      }
    });
  };

  const removeFromCart = (cartId) => {
    setCartItems(prevItems => {
      const item = prevItems.find(item => item.cartId === cartId);
      if (item) {
        toast.success(`Removed ${item.name} from cart!`);
      }
      return prevItems.filter(item => item.cartId !== cartId);
    });
  };

  const updateQuantity = (cartId, quantity) => {
    if (quantity <= 0) {
      removeFromCart(cartId);
      return;
    }

    setCartItems(prevItems =>
      prevItems.map(item =>
        item.cartId === cartId ? { ...item, quantity } : item
      )
    );
  };

  const clearCart = () => {
    setCartItems([]);
    toast.success('Cart cleared!');
  };

  const getCartTotal = () => {
    return cartItems.reduce((total, item) => total + (item.price * item.quantity), 0);
  };

  const getCartItemsCount = () => {
    return cartItems.reduce((total, item) => total + item.quantity, 0);
  };

  const getTaxAmount = (subtotal) => {
    return subtotal * 0.08; // 8% tax
  };

  const getShippingAmount = (subtotal) => {
    return subtotal >= 100 ? 0 : 10; // Free shipping over $100
  };

  const getOrderTotal = () => {
    const subtotal = getCartTotal();
    const tax = getTaxAmount(subtotal);
    const shipping = getShippingAmount(subtotal);
    return subtotal + tax + shipping;
  };

  const value = {
    cartItems,
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
    getCartTotal,
    getCartItemsCount,
    getTaxAmount,
    getShippingAmount,
    getOrderTotal,
  };

  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
};