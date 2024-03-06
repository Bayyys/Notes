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

    // params 方式
    // const { id, title } = this.props.location.search;

    // query 方式
    const { search } = this.props.location;
    const { id, title } = qs.parse(search.slice(1));

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
