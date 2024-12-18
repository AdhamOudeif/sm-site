import { format, formatDistanceToNow } from 'date-fns';

export const formatDate = (date: string | Date) => {
  const d = new Date(date);
  return format(d, 'PP');
};

export const formatRelativeTime = (date: string | Date) => {
  return formatDistanceToNow(new Date(date), { addSuffix: true });
};

export const formatDateTime = (date: string | Date) => {
  const d = new Date(date);
  return format(d, 'PPp');
};