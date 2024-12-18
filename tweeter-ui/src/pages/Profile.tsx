import React from 'react';
import { Calendar, Mail, MapPin } from 'lucide-react';
import Post from '../components/Post';

const MOCK_USER = {
  UserID: 1,
  Username: "janedoe",
  Email: "jane.doe@example.com",
  FirstName: "Jane",
  LastName: "Doe",
  Birthdate: "1990-01-01",
  Gender: "Female",
  ProfilePicture: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
  RegistrationDate: "2023-01-01T00:00:00.000Z"
};

const MOCK_USER_POSTS = [
  {
    PostID: 1,
    UserID: 1,
    Content: "Exploring new places! 🌎 #travel #adventure",
    Photo: "https://images.unsplash.com/photo-1469474968028-56623f02e42e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
    Timestamp: new Date().toISOString(),
    LikesCount: 89,
    CommentsCount: 15,
    SharesCount: 4,
    user: MOCK_USER
  }
];

export default function Profile() {
  return (
    <div>
      <div className="bg-white rounded-lg shadow mb-6">
        <div className="h-48 bg-gradient-to-r from-blue-500 to-purple-500 rounded-t-lg"></div>
        <div className="px-6 pb-6">
          <div className="relative flex items-end -mt-16 mb-4">
            <img
              src={MOCK_USER.ProfilePicture}
              alt={MOCK_USER.Username}
              className="w-32 h-32 rounded-full border-4 border-white object-cover"
            />
            <div className="ml-4 mb-2">
              <h1 className="text-2xl font-bold">{MOCK_USER.FirstName} {MOCK_USER.LastName}</h1>
              <p className="text-gray-500">@{MOCK_USER.Username}</p>
            </div>
          </div>
          
          <div className="flex flex-wrap gap-4 text-gray-600">
            <div className="flex items-center space-x-2">
              <Mail className="h-5 w-5" />
              <span>{MOCK_USER.Email}</span>
            </div>
            <div className="flex items-center space-x-2">
              <Calendar className="h-5 w-5" />
              <span>Joined {new Date(MOCK_USER.RegistrationDate).toLocaleDateString()}</span>
            </div>
            <div className="flex items-center space-x-2">
              <MapPin className="h-5 w-5" />
              <span>New York, USA</span>
            </div>
          </div>
        </div>
      </div>

      <div className="space-y-6">
        {MOCK_USER_POSTS.map(post => (
          <Post key={post.PostID} post={post} />
        ))}
      </div>
    </div>
  );
}