import { Component } from "react";
import Header from "./Components/Header/Header";
import Footer from "./Components/Footer/Footer";
import List from "./Components/List/List";
import "./App.css";

export default class App extends Component {
  state = {
    todos: [
      { id: "001", name: "吃饭", done: true },
      { id: "002", name: "睡觉", done: true },
      { id: "003", name: "打豆豆", done: false },
    ],
  };

  addTodo = (todoObj) => {
    console.log("App", todoObj);
    const { todos } = this.state;
    const newTodos = [todoObj, ...todos];
    this.setState({ todos: newTodos });
  };

  render() {
    return (
      <div className="todo-container">
        <Header addTodo={this.addTodo} />
        <List todos={this.state.todos} />
        <Footer />
      </div>
    );
  }
}
