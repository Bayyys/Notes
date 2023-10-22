import React, { Component } from "react";
import PubSub from "pubsub-js";
import "./index.css";

export default class List extends Component {
  state = {
    users: [],
    isFirst: true,
    isLoading: false,
    err: "",
  };

  componentDidMount() {
    this.token = PubSub.subscribe("updateListState", (_, stateObj) => {
      this.setState(stateObj);
    });
  }

  componentWillUnmount() {
    PubSub.unsubscribe(this.token);
  }

  render() {
    const { users, isFirst, isLoading, err } = this.state;
    return (
      <div className="row">
        {isFirst ? (
          <h1> 输入关键词搜索 GitHub 用户</h1>
        ) : isLoading ? (
          <h1>Loading...</h1>
        ) : err ? (
          <h1 style={{ color: "red" }}>{err}</h1>
        ) : (
          users.map((user) => {
            return (
              <div className="card" key={user.id}>
                <a rel="noreferrer" href={user.html_url} target="_blank">
                  <img
                    alt=""
                    src={user.avatar_url}
                    style={{ width: "100px" }}
                  />
                </a>
                <p className="card-text">{user.login}</p>
              </div>
            );
          })
        )}
      </div>
    );
  }
}
