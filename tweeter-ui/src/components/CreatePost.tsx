import React, { useState } from 'react';
import { Image, Send } from 'lucide-react';

export default function CreatePost() {
  const [content, setContent] = useState('');
  const [image, setImage] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Implement post creation
    setContent('');
    setImage('');
  };

  return (
    <div className="bg-white rounded-lg shadow p-4 mb-6">
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full p-3 border border-gray-200 rounded-lg resize-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          placeholder="What's on your mind?"
          rows={3}
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        
        {image && (
          <div className="mt-2 relative">
            <img src={image} alt="Preview" className="rounded-lg max-h-60 w-auto" />
            <button
              type="button"
              className="absolute top-2 right-2 p-1 bg-gray-800 rounded-full text-white"
              onClick={() => setImage('')}
            >
              ×
            </button>
          </div>
        )}

        <div className="flex justify-between items-center mt-4">
          <button
            type="button"
            className="flex items-center space-x-2 text-gray-600 hover:text-blue-500"
            onClick={() => document.getElementById('image-input')?.click()}
          >
            <Image className="h-5 w-5" />
            <span>Add Photo</span>
          </button>
          <input
            id="image-input"
            type="file"
            accept="image/*"
            className="hidden"
            onChange={(e) => {
              const file = e.target.files?.[0];
              if (file) {
                // TODO: Handle image upload
                setImage(URL.createObjectURL(file));
              }
            }}
          />
          
          <button
            type="submit"
            className="px-4 py-2 bg-blue-500 text-white rounded-lg flex items-center space-x-2 hover:bg-blue-600 transition-colors"
            disabled={!content && !image}
          >
            <Send className="h-4 w-4" />
            <span>Post</span>
          </button>
        </div>
      </form>
    </div>
  );
}