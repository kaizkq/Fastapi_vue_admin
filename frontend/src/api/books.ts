import axios from './axios'

export interface Book {
  id: number
  title: string
  category: string
  author: string
  publishedDate: string
  createdAt: string
  updatedAt: string
}

export interface PageResult<T> {
  success: boolean
  message: string
  data: T[]
  total: number
}

export interface PageParams {
  pageNumber: number
  pageSize: number
}

export const getBooks = async (params: PageParams) => {
  const response = await axios.get('/Books', { params })
  return response.data as PageResult<Book>
}

export const getBookById = async (id: number) => {
  const response = await axios.get(`/Books/${id}`)
  return response.data.data as Book
}

export const createBook = async (book: Omit<Book, 'id' | 'createdAt' | 'updatedAt'>) => {
  const response = await axios.post('/Books', book)
  return response.data.data as Book
}

export const updateBook = async (id: number, book: Partial<Book>) => {
  const response = await axios.patch(`/Books/${id}`, book)
  return response.data.data as Book
}

export const deleteBook = async (id: number) => {
  const response = await axios.delete(`/Books/${id}`)
  return response.data.data as Book
} 