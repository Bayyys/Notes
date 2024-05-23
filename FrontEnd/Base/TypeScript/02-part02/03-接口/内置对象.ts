// ECMAScript 内置对象
let num: Number = new Number(123);
let data: Date = new Date();
let reg: RegExp = new RegExp("\\d+");
let error: Error = new Error("出错了");
let xhr: XMLHttpRequest = new XMLHttpRequest();

// BOM 和 DOM 对象
let body: HTMLElement = document.body;
let allDiv: NodeList = document.querySelectorAll("div");
let allDivs: HTMLCollection = document.getElementsByTagName("div");
let fragment: DocumentFragment = document.createDocumentFragment();
let div_footer: NodeListOf<HTMLDivElement | HTMLElement> =
  document.querySelectorAll("div footer");

let local: Storage = window.localStorage;
let lo: Location = window.location;
let promise: Promise<number> = new Promise((resolve) => resolve(123));
let cookie: string = document.cookie;
