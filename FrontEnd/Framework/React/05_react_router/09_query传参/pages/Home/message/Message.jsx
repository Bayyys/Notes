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
                {/* <Link to={`/home/message/detail/${m.id}/${m.title}`}> */}
                <Link to={`/home/message/detail/?id=${m.id}&title=${m.title}`}>
                  {m.title}
                </Link>
              </li>
            );
          })}
        </ul>
        <hr />
        {/* <Route path="/home/message/detail/:id/:title" component={Detail} /> */}
        <Route path="/home/message/detail" component={Detail} />
      </div>
    );
  }
}
