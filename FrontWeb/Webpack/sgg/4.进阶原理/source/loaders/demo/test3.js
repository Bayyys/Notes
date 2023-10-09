// raw loader接受到content是Buffer数据
// module.exports = function (content) {
//   console.log(content);
//   return content;
// };

// module.exports.raw = true;

function test3Loader(content) {
  return content;
}

test3Loader.raw = true;

module.exports = test3Loader;
