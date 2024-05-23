enum Day {
  SUNDAY,
  MONDAY,
  TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
}

enum Status {
  Success = 200,
  NotFound = 404,
  Error = 500,
}
console.log(Status["Success"]); // 200
console.log(Status[200]); // Success
console.log(Status[Status["Success"]]); // Success

enum Result {
  Success = "Success",
  Error = 500,
}
console.log(Result["Success"]); // Success
console.log(Result["Error"]); // 500
