import React from 'react';
import CreatePost from '../components/CreatePost';
import Post from '../components/Post';

const MOCK_POSTS = [
  {
    PostID: 1,
    UserID: 1,
    Content: "Just finished a great workout! 💪 Feeling energized and ready to tackle the day. #fitness #motivation",
    Photo: "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
    Timestamp: new Date().toISOString(),
    LikesCount: 42,
    CommentsCount: 7,
    SharesCount: 2,
    user: {
      UserID: 1,
      Username: "janedoe",
      FirstName: "Jane",
      LastName: "Doe",
      ProfilePicture: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
    }
  },
  {
    PostID: 2,
    UserID: 2,
    Content: "Beautiful sunset at the beach today! 🌅 Nature never fails to amaze me.",
    Photo: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
    Timestamp: new Date(Date.now() - 3600000).toISOString(),
    LikesCount: 128,
    CommentsCount: 12,
    SharesCount: 5,
    user: {
      UserID: 2,
      Username: "johndoe",
      FirstName: "John",
      LastName: "Doe",
      ProfilePicture: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
    }
  }
];

export default function Home() {
  return (
    <div>
      <CreatePost />
      <div className="space-y-6">
        {MOCK_POSTS.map(post => (
          <Post key={post.PostID} post={post} />
        ))}
      </div>
    </div>
  );
}