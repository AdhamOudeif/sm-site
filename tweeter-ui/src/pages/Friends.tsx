import React from 'react';
import FriendsList from '../components/FriendsList';

const MOCK_FRIENDS = [
  {
    UserID: 2,
    Username: "johndoe",
    FirstName: "John",
    LastName: "Doe",
    Email: "john.doe@example.com",
    Birthdate: "1992-05-15",
    Gender: "Male",
    ProfilePicture: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    RegistrationDate: "2023-01-02T00:00:00.000Z",
    friendship: {
      FriendshipID: 1,
      User1ID: 1,
      User2ID: 2,
      Status: "accepted"
    }
  }
];

const MOCK_PENDING_REQUESTS = [
  {
    UserID: 3,
    Username: "sarahsmith",
    FirstName: "Sarah",
    LastName: "Smith",
    Email: "sarah.smith@example.com",
    Birthdate: "1995-08-20",
    Gender: "Female",
    ProfilePicture: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    RegistrationDate: "2023-02-15T00:00:00.000Z",
    friendship: {
      FriendshipID: 2,
      User1ID: 3,
      User2ID: 1,
      Status: "pending"
    }
  }
];

export default function Friends() {
  return (
    <div>
      <FriendsList
        friends={MOCK_FRIENDS}
        pendingRequests={MOCK_PENDING_REQUESTS}
      />
    </div>
  );
}