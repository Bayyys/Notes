export default function FlexGrid() {
  return (
    <div className="container mx-auto">
      <div className="basis-1">Header</div>
      <div className="flex flex-col md:flex-row">
        <div className=" w-32 bg-sky-300 px-3 mx-3">Sidebar</div>
        <div className="w-full  bg-red-300 px-3 mx-3">Main Content</div>
      </div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <div className=" p-6 rounded-lg bg-sky-500"></div>
        <div className=" p-6 col-span-2 rounded-lg bg-pink-500"></div>
        <div className=" p-6 rounded-lg bg-sky-500"></div>
        <div className=" p-6 col-span-3 rounded-lg bg-pink-500"></div>
        <div className=" p-6 rounded-lg bg-sky-500"></div>
        <div className=" p-6 col-start-2 col-end-4 rounded-lg bg-sky-500"></div>
        <div className=" p-6 rounded-lg bg-pink-500"></div>
      </div>
    </div>
  );
}
