import api from './api';
import { API_CONFIG } from '../config/api.config';
import type { User, Friendship } from '../types';

export const friendService = {
  async getPendingRequests(userId: number) {
    const response = await api.get(API_CONFIG.ENDPOINTS.FRIENDS.PENDING_REQUESTS(userId));
    return response.data;
  },

  async sendFriendRequest(userId: number) {
    const response = await api.post(API_CONFIG.ENDPOINTS.FRIENDS.SEND_REQUEST, { userId });
    return response.data;
  },

  async acceptFriendRequest(friendshipId: number) {
    const response = await api.post(API_CONFIG.ENDPOINTS.FRIENDS.ACCEPT_REQUEST, { friendshipId });
    return response.data;
  },

  async rejectFriendRequest(friendshipId: number) {
    const response = await api.post(API_CONFIG.ENDPOINTS.FRIENDS.REJECT_REQUEST, { friendshipId });
    return response.data;
  },

  async removeFriend(friendshipId: number) {
    const response = await api.post(API_CONFIG.ENDPOINTS.FRIENDS.REMOVE_FRIEND, { friendshipId });
    return response.data;
  },
};