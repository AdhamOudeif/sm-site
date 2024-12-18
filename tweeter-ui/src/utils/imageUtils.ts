export const getDefaultProfilePicture = (name: string) => {
  return `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}&background=random`;
};

export const validateImageUrl = (url: string) => {
  if (!url) return false;
  return url.match(/\.(jpeg|jpg|gif|png)$/) != null;
};