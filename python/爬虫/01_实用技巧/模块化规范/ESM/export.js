let num = 1;
function add() {
  num++;
}
class People {
  constructor(name) {
    this.name = name;
  }
}

export { num as n, add as plus, People as P };
