import { useState } from "react";

export default function ParentState() {
  const [activeIndex, setActiveIndex] = useState(0);
  return (
    <>
      <h2>哈萨克斯坦，阿拉木图</h2>
      <Panel
        title="关于"
        isActive={activeIndex === 0}
        onShow={() => setActiveIndex(0)}
      >
        阿拉木图人口约200万，是哈萨克斯坦最大的城市。它在 1929 年到 1997
        年间都是首都。
      </Panel>
      <Panel
        title="词源"
        isActive={activeIndex === 1}
        onShow={() => setActiveIndex(1)}
      >
        这个名字来自于 <span lang="kk-KZ">алма</span>
        ，哈萨克语中“苹果”的意思，经常被翻译成“苹果之乡”。事实上，阿拉木图的周边地区被认为是苹果的发源地，
        <i lang="la">Malus sieversii</i> 被认为是现今苹果的祖先。
      </Panel>
      <SyncedInputs />
    </>
  );
}

function Panel({ title, children, isActive, onShow }) {
  return (
    <section className="panel">
      <h3>{title}</h3>
      {isActive ? <p>{children}</p> : <button onClick={onShow}>显示</button>}
    </section>
  );
}

function SyncedInputs() {
  const [text, setText] = useState("测试");
  return (
    <>
      <Input text={text} setText={setText} label="第一个输入框" />
      <Input text={text} setText={setText} label="第二个输入框" />
    </>
  );
}

function Input({ text, setText, label }) {
  function handleChange(e) {
    setText(e.target.value);
  }

  return (
    <label>
      {label} <input value={text} onChange={handleChange} />
    </label>
  );
}
