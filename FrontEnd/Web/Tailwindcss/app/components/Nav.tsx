"use client";
import React from "react";

export default function Nav() {
  const navList = [
    { name: "01.DarkMode", href: "/01.DarkMode" },
    { name: "02.Color", href: "/02.Color" },
    { name: "03.Typography", href: "/03.Typography" },
    { name: "04.Flex_Grid", href: "/04.Flex_Grid" },
    { name: "05.Layout", href: "/05.Layout" },
    { name: "06.Border", href: "/06.Border" },
    { name: "07.Effect", href: "/07.Effect" },
    { name: "08", href: "/08" },
  ];

  const toggleDarkMode = () => {
    document.documentElement.classList.toggle("dark");
  };
  return (
    <nav className="flex items-start justify-between w-full">
      <div className="grid space-x-4 grid-cols-4">
        {navList.map((navItem) => (
          <a
            key={navItem.name}
            href={navItem.href}
            className="rounded-lg px-3 py-2 text-slate-700 font-medium hover:bg-slate-100 hover:text-slate-900"
          >
            {navItem.name}
          </a>
        ))}
      </div>
      <div className="flex items-center space-x-4">
        <button
          className="bg-blue-500 dark:bg-slate-500 text-white px-6 py-2 rounded-full"
          onClick={toggleDarkMode}
        >
          <svg
            // 后面留出一定的空格
            className="inline-block h-5 w-5 mr-2"
            stroke="currentColor"
            fill="currentColor"
            stroke-width="0"
            viewBox="0 0 24 24"
            height="1em"
            width="1em"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              // 根据不同主题切换图标
              className="hidden dark:inline-block"
              d="M6.993 12c0 2.761 2.246 5.007 5.007 5.007s5.007-2.246 5.007-5.007S14.761 6.993 12 6.993 6.993 9.239 6.993 12zM12 8.993c1.658 0 3.007 1.349 3.007 3.007S13.658 15.007 12 15.007 8.993 13.658 8.993 12 10.342 8.993 12 8.993zM10.998 19h2v3h-2zm0-17h2v3h-2zm-9 9h3v2h-3zm17 0h3v2h-3zM4.219 18.363l2.12-2.122 1.415 1.414-2.12 2.122zM16.24 6.344l2.122-2.122 1.414 1.414-2.122 2.122zM6.342 7.759 4.22 5.637l1.415-1.414 2.12 2.122zm13.434 10.605-1.414 1.414-2.122-2.122 1.414-1.414z"
            ></path>
            <path
              className="dark:hidden"
              d="M20.742 13.045a8.088 8.088 0 0 1-2.077.271c-2.135 0-4.14-.83-5.646-2.336a8.025 8.025 0 0 1-2.064-7.723A1 1 0 0 0 9.73 2.034a10.014 10.014 0 0 0-4.489 2.582c-3.898 3.898-3.898 10.243 0 14.143a9.937 9.937 0 0 0 7.072 2.93 9.93 9.93 0 0 0 7.07-2.929 10.007 10.007 0 0 0 2.583-4.491 1.001 1.001 0 0 0-1.224-1.224zm-2.772 4.301a7.947 7.947 0 0 1-5.656 2.343 7.953 7.953 0 0 1-5.658-2.344c-3.118-3.119-3.118-8.195 0-11.314a7.923 7.923 0 0 1 2.06-1.483 10.027 10.027 0 0 0 2.89 7.848 9.972 9.972 0 0 0 7.848 2.891 8.036 8.036 0 0 1-1.484 2.059z"
            ></path>
          </svg>
          Theme
        </button>
      </div>
    </nav>
  );
}
