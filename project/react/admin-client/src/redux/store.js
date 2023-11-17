import { configureStore } from "@reduxjs/toolkit";
import userReducer from "./user";
import headTitleReducer from "./headTitle";

export default configureStore({
  reducer: {
    user: userReducer,
    headTitle: headTitleReducer,
  },
});
