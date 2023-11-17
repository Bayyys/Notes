import { createSlice } from "@reduxjs/toolkit";
import storageUtils from "../utils/storageUtils";
import { reqLogin } from "../api/api";

const userSlice = createSlice({
  name: "user",
  initialState: { user: storageUtils.getUser(), msg: "" },
  reducers: {
    setUsername: (state, action) => {
      state.user = action.payload;
      state.msg = "";
    },
    setMsg: (state, action) => {
      state.msg = action.payload;
    },
  },
});

export const { setUsername, setMsg } = userSlice.actions;

export const login = (username, password) => {
  return async (dispatch) => {
    const result = await reqLogin(username, password);
    if (result.status === 0) {
      const user = result.data;
      storageUtils.saveUser(user);
      dispatch(setUsername(user));
    } else {
      const msg = result.msg;
      dispatch(setMsg(msg));
    }
  };
};

export const logout = () => {
  return (dispatch) => {
    storageUtils.removeUser();
    dispatch(setUsername({}));
  };
};

export default userSlice.reducer;
