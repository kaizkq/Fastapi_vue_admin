import axios from './axios'

interface SignInData {
  username: string
  password: string
}

interface SignUpData extends SignInData {
  nickname?: string
}

interface UpdateUserData {
  username?: string
  password?: string
  nickname?: string
}

export const signIn = async (data: SignInData) => {
  const response = await axios.post('/User/login', data)
  return response.data.data
}

export const signUp = async (data: SignUpData) => {
  const response = await axios.post('/User/register', data)
  return response.data.data
}

export const getCurrentUser = async (userId: number) => {
  const response = await axios.get(`/User/${userId}`)
  return response.data.data
}

export const updateUser = async (id: number, data: UpdateUserData) => {
  const response = await axios.patch(`/User/${id}`, data)
  return response.data.data
} 