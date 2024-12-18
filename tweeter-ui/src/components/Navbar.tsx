import React from 'react';
import { Link } from 'react-router-dom';
import { Home, Users, Bell, MessageSquare, User, LogOut } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="fixed top-0 w-full bg-white border-b border-gray-200 z-50">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex items-center space-x-2">
              <Users className="h-8 w-8 text-blue-600" />
              <span className="text-xl font-bold text-gray-900">SocialHub</span>
            </Link>
          </div>

          <div className="flex items-center space-x-4">
            <Link to="/" className="nav-icon">
              <Home className="h-6 w-6" />
            </Link>
            <Link to="/friends" className="nav-icon">
              <Users className="h-6 w-6" />
            </Link>
            <button className="nav-icon">
              <Bell className="h-6 w-6" />
            </button>
            <button className="nav-icon">
              <MessageSquare className="h-6 w-6" />
            </button>
            <Link to="/profile" className="nav-icon">
              <User className="h-6 w-6" />
            </Link>
            <button className="nav-icon text-red-500">
              <LogOut className="h-6 w-6" />
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}