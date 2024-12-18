import api from './api';
import { API_CONFIG } from '../config/api.config';
import type { User } from '../types';

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  password: string;
  email: string;
  firstName: string;
  lastName: string;
  birthdate: string;
  gender: string;
  profilePicture?: string;
}

export const authService = {
  async login(credentials: LoginCredentials) {
    const response = await api.post(API_CONFIG.ENDPOINTS.AUTH.LOGIN, credentials);
    return response.data;
  },

  async register(data: RegisterData) {
    const response = await api.post(API_CONFIG.ENDPOINTS.AUTH.REGISTER, data);
    return response.data;
  },

  async getCurrentUser() {
    const response = await api.get(API_CONFIG.ENDPOINTS.AUTH.CURRENT_USER);
    return response.data;
  },
};