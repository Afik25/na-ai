import axios from "axios";

// const BASE_URL = `${process.env.REACT_APP_API_SERVER_URL}:${process.env.REACT_APP_API_SERVER_PORT}/api/v1`;
const BASE_URL = `http://127.0.0.1:8000/api/v1`;

export default axios.create({ baseURL: BASE_URL });
export const axiosPrivate = axios.create({
  baseURL: BASE_URL,
  headers: { "Content-Type": "application/json" },
  withCredentials: true,
});
