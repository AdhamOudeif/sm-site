import api from './api';
import { API_CONFIG } from '../config/api.config';
import type { Post } from '../types';

export const postService = {
  async getPosts() {
    const response = await api.get(API_CONFIG.ENDPOINTS.POSTS.LIST);
    return response.data;
  },

  async getFriendsPosts(userId: number) {
    const response = await api.get(API_CONFIG.ENDPOINTS.FRIENDS.POSTS(userId));
    return response.data;
  },

  async createPost(data: { content: string; photo?: string }) {
    const response = await api.post(API_CONFIG.ENDPOINTS.POSTS.CREATE, data);
    return response.data;
  },

  async likePost(postId: number) {
    const response = await api.post(API_CONFIG.ENDPOINTS.POSTS.LIKE(postId));
    return response.data;
  },

  async createComment(postId: number, content: string) {
    const response = await api.post(
      API_CONFIG.ENDPOINTS.POSTS.COMMENTS.CREATE(postId),
      { content }
    );
    return response.data;
  },

  async getComments(postId: number) {
    const response = await api.get(API_CONFIG.ENDPOINTS.POSTS.COMMENTS.LIST(postId));
    return response.data;
  },
};