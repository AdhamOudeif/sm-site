export interface User {
  UserID: number;
  Username: string;
  Email: string;
  FirstName: string;
  LastName: string;
  Birthdate: string;
  Gender: string;
  ProfilePicture: string;
  RegistrationDate: string;
}

export interface Post {
  PostID: number;
  UserID: number;
  Content: string;
  Photo?: string;
  Timestamp: string;
  LikesCount: number;
  CommentsCount: number;
  SharesCount: number;
  user?: User;
}

export interface Comment {
  CommentId: number;
  PostID: number;
  UserID: number;
  Content: string;
  Timestamp: string;
  LikesCount: number;
  user?: User;
}

export interface Friendship {
  FriendshipID: number;
  User1ID: number;
  User2ID: number;
  Status: 'pending' | 'accepted' | 'rejected';
}