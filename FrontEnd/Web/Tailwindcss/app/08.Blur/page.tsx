import Image from "next/image";

export default function Blur() {
  return (
    <div className="container flex flex-col items-center space-y-2">
      <div className="flex flex-row space-x-4">
        <Image
          className="blur-sm rounded-lg hover:filter-none"
          src="/cool.jpg"
          width={200}
          height={200}
          alt="cool"
        />
        <Image
          className="blur-sm rounded-lg hover:brightness-125"
          src="/cool.jpg"
          width={200}
          height={200}
          alt="cool"
        />
        <Image
          className="rounded-lg drop-shadow-lg hover:drop-shadow-xl"
          src="/cool.jpg"
          width={200}
          height={200}
          alt="cool"
        />
        <Image
          className="rounded-lg grayscale hover:grayscale-0"
          src="/cool.jpg"
          width={200}
          height={200}
          alt="cool"
        />
      </div>
      <div className="flex flex-col space-y-2 text-white">
        <h1 className=" bg-blue-300/50 rounded-xl px-8 py-3">Title</h1>
        <button className="bg-blue-600/75 hover:bg-blue-700 rounded-xl py-3 text-2xl shadow-sm shadow-indigo-300/75">
          Button
        </button>
      </div>
    </div>
  );
}
