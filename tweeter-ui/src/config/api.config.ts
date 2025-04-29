// API Configuration
export const API_CONFIG = {
  // Base URL for all API requests
  BASE_URL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
  
  // API endpoints
  ENDPOINTS: {
    // Auth endpoints
    AUTH: {
      LOGIN: '/login/',
      REGISTER: '/users/create/',
      CURRENT_USER: '/users/me/',
    },
    
    // Post endpoints
    POSTS: {
      LIST: '/posts/',
      CREATE: '/posts/create/',
      LIKE: (postId: number) => `/posts/${postId}/like/`,
      COMMENTS: {
        LIST: (postId: number) => `/comments/${postId}/`,
        CREATE: (postId: number) => `/posts/${postId}/comments/create/`,
        LIKE: (commentId: number) => `/comments/${commentId}/like/`,
      },
    },
    
    // Friend endpoints
    FRIENDS: {
      POSTS: (userId: number) => `/friends/posts/${userId}/`,
      SEND_REQUEST: '/friend-request/send/',
      ACCEPT_REQUEST: '/friend-request/accept/',
      REJECT_REQUEST: '/friend-request/reject/',
      PENDING_REQUESTS: (userId: number) => `/friend-request/get-all-pending/${userId}/`,
      REMOVE_FRIEND: '/friend-request/remove/',
    },
    
    // User endpoints
    USERS: {
      LIST: '/users/',
    },
  },
  
  // Default headers
  HEADERS: {
    'Content-Type': 'application/json',
  },
}