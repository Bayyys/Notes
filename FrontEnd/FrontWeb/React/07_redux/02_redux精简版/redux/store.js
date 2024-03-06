import { createStore } from "redux";
//引入为 Count 组件服务的 reducer
import countReducer from "./count_reducer";

export default createStore(countReducer);
