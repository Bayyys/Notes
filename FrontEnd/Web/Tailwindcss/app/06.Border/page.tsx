import React from "react";
export default function Border() {
  return (
    <div className="h-screen text-slate-900 space-y-2">
      <h1 className="w-full border-red-600 border-8 rounded-md">Header</h1>
      <h1 className="w-full border-green-600 hover:border-blue-500/50 border-b-2">
        Header
      </h1>
      <div className="grid grid-cols-3 divide-x-2 divide-blue-600/50 text-center">
        <div>01</div>
        <div>02</div>
        <div>03</div>
      </div>
      <div className="grid grid-rows-3 divide-y-4 divide-pink-600/50 text-center divide-dotted">
        <div>01</div>
        <div>02</div>
        <div>03</div>
      </div>
      <h1 className=" outline-4 outline-dashed outline-orange-600 border-4 border-blue-600">
        Header
      </h1>
      <h1 className="ring-2 ring-offset-2 ring-pink-500 hover:ring-4">
        Header
      </h1>
    </div>
  );
}
