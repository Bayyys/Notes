import React from "react";

export default function Color() {
  return (
    // 内部元素间隔10px
    <div className="flex flex-col items-center justify-center h-screen space-y-5">
      <h1 className="text-3xl font-bold underline text-red-600">
        Hello World!
      </h1>
      <h1 className="text-3xl font-bold underline bg-green-500 text-white">
        Hello World!
      </h1>
      <h1 className="text-3xl border-4 border-blue-500">Hello World!</h1>
      <h1 className="text-3xl text-mycolor-999">Hello World!</h1>
    </div>
  );
}
