export default function TransitionAnimation() {
  return (
    <div className="flex flex-col space-y-2">
      <button className="hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" duration-1000 hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" ease-in-out duration-300 hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" animate-pulse hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" mt-10 animate-bounce hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" hover:scale-x-150 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" hover:rotate-45 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" hover:skew-y-6 hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
      <button className=" hover:rotate-45 origin-top-right hover:scale-110 hover:bg-indigo-500 transition delay-75">
        Button
      </button>
    </div>
  );
}
