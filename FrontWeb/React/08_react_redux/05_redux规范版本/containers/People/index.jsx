import React, { Component } from "react";
import { connect } from "react-redux";
import { Space, Input, Button, Card } from "antd";
import { UserOutlined, FieldTimeOutlined } from "@ant-design/icons";
import { nanoid } from "nanoid";

import { addPerson } from "../../redux/actions/people";

class People extends Component {
  addPerson = () => {
    const name = this.nameNode.input.value;
    const age = this.ageNode.input.value;
    const personObj = { id: nanoid(), name, age };
    this.props.addPerson(personObj);
  };

  render() {
    return (
      <Space direction="vertical" size="large" style={{ display: "flex" }}>
        <h1>当前求和为: {this.props.count}</h1>
        <Input
          ref={(c) => (this.nameNode = c)}
          placeholder="请输入姓名"
          prefix={<UserOutlined />}
        />
        <Input
          ref={(c) => (this.ageNode = c)}
          placeholder="请输入年龄"
          prefix={<FieldTimeOutlined />}
        />
        <Button
          danger
          type="dashed"
          style={{ width: 300 }}
          onClick={this.addPerson}
        >
          添加
        </Button>
        <Card title="数据展示" style={{ width: 300 }}>
          {this.props.people.map((item) => {
            return (
              <p key={item.id}>
                {item.name} -- {item.age}
              </p>
            );
          })}
        </Card>
      </Space>
    );
  }
}

const mapStateToProps = (state) => ({
  people: state.people,
  count: state.count,
});

const mapDispatchToProps = { addPerson };

export default connect(mapStateToProps, mapDispatchToProps)(People);
