module.exports = function (content) {
  console.log('normal loader 1');
  return content;
};

module.exports.pitch = function () {
  console.log("pitch loader 1");
};
