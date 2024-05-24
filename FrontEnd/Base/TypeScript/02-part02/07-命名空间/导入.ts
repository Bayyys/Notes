namespace Utils {
  export function mul(a: number, b: number): number {
    return a * b;
  }
}

namespace Other {
  import mul = Utils.mul;
}
