import React from 'react';
import { UserPlus, UserMinus, Check, X } from 'lucide-react';
import type { User, Friendship } from '../types';

interface FriendsListProps {
  friends: (User & { friendship: Friendship })[];
  pendingRequests: (User & { friendship: Friendship })[];
}

export default function FriendsList({ friends, pendingRequests }: FriendsListProps) {
  const handleAcceptRequest = (friendshipId: number) => {
    // TODO: Implement accept request
  };

  const handleRejectRequest = (friendshipId: number) => {
    // TODO: Implement reject request
  };

  const handleRemoveFriend = (friendshipId: number) => {
    // TODO: Implement remove friend
  };

  return (
    <div className="space-y-6">
      {pendingRequests.length > 0 && (
        <div>
          <h2 className="text-xl font-semibold mb-4">Pending Requests</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {pendingRequests.map((user) => (
              <div key={user.UserID} className="bg-white rounded-lg shadow p-4">
                <div className="flex items-center space-x-4">
                  <img
                    src={user.ProfilePicture || 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80'}
                    alt={user.Username}
                    className="w-12 h-12 rounded-full object-cover"
                  />
                  <div>
                    <h3 className="font-semibold">{user.FirstName} {user.LastName}</h3>
                    <p className="text-sm text-gray-500">@{user.Username}</p>
                  </div>
                </div>
                <div className="flex justify-end space-x-2 mt-4">
                  <button
                    onClick={() => handleAcceptRequest(user.friendship.FriendshipID)}
                    className="p-2 bg-green-500 text-white rounded-full hover:bg-green-600"
                  >
                    <Check className="h-4 w-4" />
                  </button>
                  <button
                    onClick={() => handleRejectRequest(user.friendship.FriendshipID)}
                    className="p-2 bg-red-500 text-white rounded-full hover:bg-red-600"
                  >
                    <X className="h-4 w-4" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div>
        <h2 className="text-xl font-semibold mb-4">Friends</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {friends.map((friend) => (
            <div key={friend.UserID} className="bg-white rounded-lg shadow p-4">
              <div className="flex items-center space-x-4">
                <img
                  src={friend.ProfilePicture || 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80'}
                  alt={friend.Username}
                  className="w-12 h-12 rounded-full object-cover"
                />
                <div>
                  <h3 className="font-semibold">{friend.FirstName} {friend.LastName}</h3>
                  <p className="text-sm text-gray-500">@{friend.Username}</p>
                </div>
              </div>
              <button
                onClick={() => handleRemoveFriend(friend.friendship.FriendshipID)}
                className="mt-4 w-full flex items-center justify-center space-x-2 px-4 py-2 border border-red-500 text-red-500 rounded-lg hover:bg-red-50"
              >
                <UserMinus className="h-4 w-4" />
                <span>Remove Friend</span>
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}