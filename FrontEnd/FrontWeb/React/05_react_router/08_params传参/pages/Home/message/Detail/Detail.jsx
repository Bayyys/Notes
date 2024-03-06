import React, { Component } from "react";

export default class Detail extends Component {
  state = {
    newsDetail: [
      { id: "001", content: "news001 content" },
      { id: "002", content: "news002 content" },
      { id: "003", content: "news003 content" },
    ],
  };
  render() {
    const { newsDetail } = this.state;

    const { id, title } = this.props.location.search;

    const { content } = newsDetail.find((nd) => {
      return nd.id === id;
    });

    return (
      <ul>
        <li>ID: {id}</li>
        <li>TITLE: {title}</li>
        <li>CONTENT: {content}</li>
      </ul>
    );
  }
}
