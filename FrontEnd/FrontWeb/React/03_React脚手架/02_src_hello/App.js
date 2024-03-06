import { Component } from "react";
import Hello from "./Components/Hello/Hello";
import Welcome from "./Components/Welcome/Welcome";

export default class App extends Component {
  render() {
    return (
      <div className="App">
        <Hello />
        <Welcome />
      </div>
    );
  }
}
