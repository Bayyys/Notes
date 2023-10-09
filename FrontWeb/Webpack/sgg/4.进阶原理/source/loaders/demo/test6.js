module.exports = function (content) {
  console.log('normal loader 3');
  return content;
};

module.exports.pitch = function () {
  console.log("pitch loader 3");
};
