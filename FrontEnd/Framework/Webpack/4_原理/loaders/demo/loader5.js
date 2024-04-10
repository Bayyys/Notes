module.exports = function (content) {
  console.log("loader5");
  return content;
};
module.exports.pitch = function (remainingRequest, precedingRequest, data) {
  console.log("pitch5");
};
