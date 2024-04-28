import PropsTrans from "./practice/01.PropsTrans";
import StateInsert from "./practice/02.StateInsert";
import ParentState from "./practice/03.ParentState";
import PreserveState from "./practice/04.PreserveState";
import EffectDemo from "./practice/05.EffectDemo";

function App() {
  return (
    <>
      <div className="container">
        {false && <PropsTrans />}
        {false && <StateInsert />}
        {false && <ParentState />}
        {false && <PreserveState />}
        {true && <EffectDemo />}
      </div>
    </>
  );
}

export default App;
