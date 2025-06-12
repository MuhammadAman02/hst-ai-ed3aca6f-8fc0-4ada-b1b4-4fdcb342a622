import React from 'react';
import { Link } from 'react-router-dom';
import { useQuery } from 'react-query';
import axios from 'axios';
import ProductCard from '../components/ProductCard';

const fetchFeaturedProducts = async () => {
  const response = await axios.get('/api/products/featured');
  return response.data;
};

const Home = () => {
  const { data: featuredProducts, isLoading, error } = useQuery(
    'featuredProducts',
    fetchFeaturedProducts
  );

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative hero-gradient text-white overflow-hidden">
        <div className="absolute inset-0 adidas-stripes opacity-10"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-32">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="animate-fade-in">
              <h1 className="text-5xl lg:text-7xl font-black mb-6 leading-tight">
                IMPOSSIBLE
                <br />
                IS NOTHING
              </h1>
              <p className="text-xl lg:text-2xl mb-8 text-gray-300 max-w-lg">
                Discover the latest collection of Adidas shoes. Performance meets style in every step.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link 
                  to="/products"
                  className="bg-white text-adidas-black hover:bg-gray-100 font-semibold px-8 py-4 text-lg rounded transition-colors text-center"
                >
                  Shop Now
                </Link>
                <Link 
                  to="/products?featured=true"
                  className="border-2 border-white text-white hover:bg-white hover:text-adidas-black font-semibold px-8 py-4 text-lg rounded transition-colors text-center"
                >
                  Explore Collection
                </Link>
              </div>
            </div>
            <div className="relative animate-fade-in">
              <div className="relative z-10">
                <img 
                  src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&h=600&fit=crop" 
                  alt="Featured Adidas Shoe"
                  className="w-full max-w-md mx-auto transform rotate-12 hover:rotate-6 transition-transform duration-500"
                />
              </div>
              <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-gradient-to-r from-adidas-red to-transparent rounded-full opacity-20 blur-3xl"></div>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16 bg-adidas-light-gray">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-black text-adidas-black mb-4">
              FEATURED PRODUCTS
            </h2>
            <p className="text-xl text-adidas-gray max-w-2xl mx-auto">
              Discover our latest collection of premium Adidas footwear
            </p>
          </div>

          {isLoading && (
            <div className="flex justify-center items-center py-12">
              <div className="spinner"></div>
              <span className="ml-2 text-adidas-gray">Loading products...</span>
            </div>
          )}

          {error && (
            <div className="text-center py-12">
              <p className="text-red-600">Error loading products. Please try again later.</p>
            </div>
          )}

          {featuredProducts && (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
              {featuredProducts.map((product) => (
                <ProductCard key={product.id} product={product} />
              ))}
            </div>
          )}

          <div className="text-center mt-12">
            <Link 
              to="/products"
              className="btn-primary px-8 py-3 rounded font-semibold text-lg inline-block"
            >
              View All Products
            </Link>
          </div>
        </div>
      </section>

      {/* Brand Story */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-4xl font-black text-adidas-black mb-6">
                THE BRAND WITH THE THREE STRIPES
              </h2>
              <p className="text-lg text-adidas-gray mb-6">
                Since 1949, adidas has been at the forefront of athletic innovation. 
                From the track to the street, our shoes are designed to help you 
                perform at your best while looking your best.
              </p>
              <p className="text-lg text-adidas-gray mb-8">
                Every pair tells a story of craftsmanship, technology, and the 
                relentless pursuit of excellence. Join millions of athletes and 
                style enthusiasts who trust adidas.
              </p>
              <Link 
                to="/products"
                className="btn-secondary px-6 py-3 rounded font-semibold inline-block"
              >
                Discover Our Heritage
              </Link>
            </div>
            <div className="relative">
              <img 
                src="https://images.unsplash.com/photo-1556906781-9a412961c28c?w=600&h=400&fit=crop" 
                alt="Adidas Heritage"
                className="w-full rounded-lg shadow-lg"
              />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;