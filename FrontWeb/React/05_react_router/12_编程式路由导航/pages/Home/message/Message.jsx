import React, { Component } from "react";
import { Link, Route } from "react-router-dom";
import Detail from "./Detail/Detail";

export default class Message extends Component {
  state = {
    message: [
      { id: "001", title: "message001" },
      { id: "002", title: "message002" },
      { id: "003", title: "message003" },
    ],
  };
  render() {
    const { message } = this.state;
    return (
      <div>
        <ul>
          {message.map((m) => {
            return (
              <li key={m.id}>
                <Link
                  to={{
                    pathname: "/home/message/detail",
                    state: {
                      id: m.id,
                      title: m.title,
                    },
                  }}
                >
                  {m.title}
                </Link>{" "}
                &nbsp;
                <button
                  onClick={() => {
                    this.props.history.push("/home/message/detail", {
                      id: m.id,
                      title: m.title,
                    });
                  }}
                >
                  push查看
                </button>{" "}
                &nbsp;
                <button
                  onClick={() => {
                    this.props.history.replace("/home/message/detail", {
                      id: m.id,
                      title: m.title,
                    });
                  }}
                >
                  replace查看
                </button>
              </li>
            );
          })}
        </ul>
        <hr />
        <Route path="/home/message/detail" component={Detail} />
      </div>
    );
  }
}
