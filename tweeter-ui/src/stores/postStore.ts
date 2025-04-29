import create from 'zustand';
import { postService } from '../services/posts';
import type { Post, Comment } from '../types';

interface PostState {
  posts: Post[];
  isLoading: boolean;
  error: string | null;
  fetchPosts: () => Promise<void>;
  createPost: (content: string, photo?: string) => Promise<void>;
  likePost: (postId: number) => Promise<void>;
  createComment: (postId: number, content: string) => Promise<Comment>;
}

export const usePostStore = create<PostState>((set, get) => ({
  posts: [],
  isLoading: false,
  error: null,

  fetchPosts: async () => {
    set({ isLoading: true });
    try {
      const posts = await postService.getPosts();
      set({ posts, isLoading: false });
    } catch {
      set({ error: 'Failed to fetch posts', isLoading: false });
    }
  },

  createPost: async (content: string, photo?: string) => {
    try {
      const newPost = await postService.createPost({ content, photo });
      set({ posts: [newPost, ...get().posts], error: null });
    } catch {
      set({ error: 'Failed to create post' });
    }
  },

  likePost: async (postId: number) => {
    try {
      await postService.likePost(postId);
      set({
        posts: get().posts.map(post =>
          post.PostID === postId
            ? { ...post, LikesCount: post.LikesCount + 1 }
            : post
        ),
        error: null
      });
    } catch (error) {
      set({ error: 'Failed to like post' });
    }
  },

  createComment: async (postId: number, content: string): Promise<Comment> => {
    try {
      const newComment: Comment = await postService.createComment(postId, content);
      set({
        posts: get().posts.map(post =>
          post.PostID === postId
            ? { ...post, CommentsCount: post.CommentsCount + 1 }
            : post
        ),
      });
      return newComment;
    } catch (error) {
      set({ error: 'Failed to create comment' });
      throw error;
    }
  },
}));