import React, { Component } from "react";
import "./App.css";
import Search from "./components/Search";
import List from "./components/List";

export default class App extends Component {
  state = {
    users: [],
    isFirst: true,
    isLoading: false,
    isError: false,
    err: "",
  };

  updateAppState = (newState) => {
    this.setState({ ...newState });
  };

  render() {
    const { users, isFirst, isLoading, isError, err } = this.state;
    return (
      <div className="container">
        <Search updateAppState={this.updateAppState} />
        {isFirst ? (
          <h1>输入关键词搜索 GitHub 用户</h1>
        ) : isLoading ? (
          <h1>Loading...</h1>
        ) : isError ? (
          <h1 style={{ color: "red" }}>{err}</h1>
        ) : (
          <List users={users} />
        )}
      </div>
    );
  }
}
