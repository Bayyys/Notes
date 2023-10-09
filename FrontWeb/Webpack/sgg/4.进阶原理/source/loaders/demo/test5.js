module.exports = function (content) {
  console.log("normal loader 2");
  return content;
};

module.exports.pitch = function () {
  console.log("pitch loader 2");
  return "result";
};
