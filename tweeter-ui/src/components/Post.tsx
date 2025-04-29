import React, { useState } from 'react';
import { Heart, MessageCircle, Share2, MoreVertical } from 'lucide-react';
import { formatDistanceToNow } from 'date-fns';
import type { Post as PostType, Comment as CommentType } from '../types';

interface PostProps {
  post: PostType;
}

export default function Post({ post }: PostProps) {
  const [showComments, setShowComments] = useState(false);
  const [newComment, setNewComment] = useState('');

  const handleLike = () => {
    // TODO: Implement like functionality
  };

  const handleComment = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Implement comment submission
    setNewComment('');
  };

  const handleShare = () => {
    // TODO: Implement share functionality
  };

  return (
    <div className="bg-white rounded-lg shadow mb-6">
      <div className="p-4">
        <div className="flex justify-between items-start mb-4">
          <div className="flex items-center space-x-3">
            <img
              src={post.user?.ProfilePicture || 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80'}
              alt={post.user?.Username}
              className="w-10 h-10 rounded-full object-cover"
            />
            <div>
              <h3 className="font-semibold text-gray-900">
                {post.user?.FirstName} {post.user?.LastName}
              </h3>
              <p className="text-sm text-gray-500">
                {formatDistanceToNow(new Date(post.Timestamp), { addSuffix: true })}
              </p>
            </div>
          </div>
          <button className="text-gray-400 hover:text-gray-600">
            <MoreVertical className="h-5 w-5" />
          </button>
        </div>

        <p className="text-gray-800 mb-4">{post.Content}</p>
        
        {post.Photo && (
          <img
            src={post.Photo}
            alt="Post content"
            className="rounded-lg w-full object-cover max-h-96 mb-4"
          />
        )}

        <div className="flex items-center justify-between text-gray-500 border-t border-gray-100 pt-4">
          <button
            onClick={handleLike}
            className="flex items-center space-x-2 hover:text-red-500"
          >
            <Heart className="h-5 w-5" />
            <span>{post.LikesCount}</span>
          </button>
          
          <button
            onClick={() => setShowComments(!showComments)}
            className="flex items-center space-x-2 hover:text-blue-500"
          >
            <MessageCircle className="h-5 w-5" />
            <span>{post.CommentsCount}</span>
          </button>
          
          <button
            onClick={handleShare}
            className="flex items-center space-x-2 hover:text-green-500"
          >
            <Share2 className="h-5 w-5" />
            <span>{post.SharesCount}</span>
          </button>
        </div>
      </div>

      {showComments && (
        <div className="border-t border-gray-100 p-4">
          <form onSubmit={handleComment} className="mb-4">
            <div className="flex space-x-2">
              <input
                type="text"
                placeholder="Write a comment..."
                className="flex-1 border border-gray-200 rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                value={newComment}
                onChange={(e) => setNewComment(e.target.value)}
              />
              <button
                type="submit"
                className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
                disabled={!newComment.trim()}
              >
                Post
              </button>
            </div>
          </form>

          {/* TODO: Implement comments list */}
        </div>
      )}
    </div>
  );
}