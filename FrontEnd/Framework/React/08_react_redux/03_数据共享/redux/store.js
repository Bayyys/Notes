import { applyMiddleware, combineReducers, createStore } from "redux";
//引入为 Count 组件服务的 reducer
import count from "./reducers/count";
import people from "./reducers/people";
import thunk from "redux-thunk";

export default createStore(
  combineReducers({ count, people }),
  applyMiddleware(thunk)
); // 创建 store 对象内部会第一次调用 reducer() 得到初始状态值
