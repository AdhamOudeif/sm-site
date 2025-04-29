import React, { useState } from 'react';
import { Search } from 'lucide-react';
import { useAuthStore } from '../stores/authStore';
import api from '../services/api';
import { API_CONFIG } from '../config/api.config';
import type { User } from '../types';

export default function UserSearch() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState<User[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const { user: currentUser } = useAuthStore();

  const handleSearch = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setSearchTerm(value);
    
    if (value.length < 2) {
      setSearchResults([]);
      return;
    }

    setIsLoading(true);
    try {
      const response = await api.get(`${API_CONFIG.ENDPOINTS.USERS.LIST}?search=${value}`);
      setSearchResults(response.data.filter((user: User) => user.UserID !== currentUser?.UserID));
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="relative">
      <div className="relative">
        <input
          type="text"
          value={searchTerm}
          onChange={handleSearch}
          placeholder="Search users..."
          className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        />
        <Search className="absolute left-3 top-2.5 h-5 w-5 text-gray-400" />
      </div>
      
      {searchTerm.length >= 2 && (
        <div className="absolute w-full mt-2 bg-white rounded-lg shadow-lg z-50 max-h-96 overflow-y-auto">
          {isLoading ? (
            <div className="p-4 text-center text-gray-500">Searching...</div>
          ) : searchResults.length > 0 ? (
            <div className="py-2">
              {searchResults.map((user) => (
                <div
                  key={user.UserID}
                  className="px-4 py-2 hover:bg-gray-50 flex items-center space-x-3"
                >
                  <img
                    src={user.ProfilePicture || `https://ui-avatars.com/api/?name=${user.FirstName}+${user.LastName}`}
                    alt={user.Username}
                    className="w-10 h-10 rounded-full object-cover"
                  />
                  <div>
                    <p className="font-medium">{user.FirstName} {user.LastName}</p>
                    <p className="text-sm text-gray-500">@{user.Username}</p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="p-4 text-center text-gray-500">No users found</div>
          )}
        </div>
      )}
    </div>
  );
}