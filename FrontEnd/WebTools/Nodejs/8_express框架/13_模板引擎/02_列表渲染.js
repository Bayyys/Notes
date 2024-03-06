// 列表
const games = ["王者荣耀", "英雄联盟", "绝地求生", "穿越火线", "地下城与勇士"];

const ejs = require("ejs");
const fs = require("fs");

let result1 = ejs.render(
  `<ul>
    <% games.forEach((item) => { %>
        <li><%= item %></li>
    <% }) %>
  </ul>`,
  { games }
);

const str = fs.readFileSync(__dirname + "/02_列表.html").toString();
const result2 = ejs.render(str, { games });

console.log(result1);
console.log(result2);
