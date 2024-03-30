import { createSlice } from "@reduxjs/toolkit";

export const configurationSlice = createSlice({
  name: "setUp",
  initialState: {
    initConnectedUser: {},
    initUsersData: {},
    initOriginsData: {},
  },
  reducers: {
    initConnectedUser: (state, action) => {
      state.initConnectedUser = {
        connectedUserData: action.payload,
      };
    },
    getUsers: (state, action) => {
      state.initUsersData = {
        usersData: action.payload,
      };
    },
    getOriginsData: (state, action) => {
      state.initOriginsData = {
        originsData: action.payload,
      };
    },
  },
});
