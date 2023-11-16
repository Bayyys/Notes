import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
  name: "user",
  initialState: {
    username: "",
    password: "",
  },
  reducers: {
    /**
     * 设置用户名
     */
    setUsername: (state, action) => {
      state.username = action.payload;
    },
    /**
     * 设置密码
     */
    setPassword: (state, action) => {
      state.password = action.payload;
    },
  },
});

export const { setUsername, setPassword } = userSlice.actions;
export default userSlice.reducer;
