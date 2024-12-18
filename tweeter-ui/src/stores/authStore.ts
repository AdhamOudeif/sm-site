import create from 'zustand';
import { authService } from '../services/auth';
import type { User } from '../types';

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  initialize: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  isLoading: true,

  login: async (username: string, password: string) => {
    const { token, user } = await authService.login({ username, password });
    localStorage.setItem('token', token);
    set({ user, isAuthenticated: true });
  },

  logout: () => {
    localStorage.removeItem('token');
    set({ user: null, isAuthenticated: false });
  },

  initialize: async () => {
    try {
      const token = localStorage.getItem('token');
      if (token) {
        const user = await authService.getCurrentUser();
        set({ user, isAuthenticated: true, isLoading: false });
      } else {
        set({ isLoading: false });
      }
    } catch (error) {
      localStorage.removeItem('token');
      set({ isLoading: false });
    }
  },
}));