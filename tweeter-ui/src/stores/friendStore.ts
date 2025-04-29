import create from 'zustand';
import { friendService } from '../services/friends';
import type { User, Friendship } from '../types';

interface FriendState {
  friends: (User & { friendship: Friendship })[];
  pendingRequests: (User & { friendship: Friendship })[];
  isLoading: boolean;
  error: string | null;
  fetchPendingRequests: (userId: number) => Promise<void>;
  acceptRequest: (friendshipId: number) => Promise<void>;
  rejectRequest: (friendshipId: number) => Promise<void>;
  removeFriend: (friendshipId: number) => Promise<void>;
}

export const useFriendStore = create<FriendState>((set, get) => ({
  friends: [],
  pendingRequests: [],
  isLoading: false,
  error: null,

  fetchPendingRequests: async (userId: number) => {
    set({ isLoading: true });
    try {
      const requests = await friendService.getPendingRequests(userId);
      set({ pendingRequests: requests, isLoading: false });
    } catch (error) {
      set({ error: 'Failed to fetch requests', isLoading: false });
    }
  },

  acceptRequest: async (friendshipId: number) => {
    try {
      await friendService.acceptFriendRequest(friendshipId);
      const request = get().pendingRequests.find(r => r.friendship.FriendshipID === friendshipId);
      if (request) {
        set({
          friends: [...get().friends, { ...request, friendship: { ...request.friendship, Status: 'accepted' } }],
          pendingRequests: get().pendingRequests.filter(r => r.friendship.FriendshipID !== friendshipId),
        });
      }
    } catch (error) {
      set({ error: 'Failed to accept request' });
    }
  },

  rejectRequest: async (friendshipId: number) => {
    try {
      await friendService.rejectFriendRequest(friendshipId);
      set({
        pendingRequests: get().pendingRequests.filter(r => r.friendship.FriendshipID !== friendshipId),
      });
    } catch (error) {
      set({ error: 'Failed to reject request' });
    }
  },

  removeFriend: async (friendshipId: number) => {
    try {
      await friendService.removeFriend(friendshipId);
      set({
        friends: get().friends.filter(f => f.friendship.FriendshipID !== friendshipId),
      });
    } catch (error) {
      set({ error: 'Failed to remove friend' });
    }
  },
}));