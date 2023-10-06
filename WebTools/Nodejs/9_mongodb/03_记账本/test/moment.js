const moment = require("moment");

console.log(moment('2023-10-06'));  // Moment<2023-10-06T00:00:00+08:00>
console.log(moment('2023-10-06').toDate()); // 2023-10-05T16:00:00.000Z