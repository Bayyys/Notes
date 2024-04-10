import { combineReducers } from "redux";

// 引入 reducer
import count from "./count";
import people from "./people";

export default combineReducers({ count, people });
