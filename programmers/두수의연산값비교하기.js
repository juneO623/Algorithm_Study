function solution(a, b) {
  var strSum = Number(String(a) + String(b));
  var mul = 2 * a * b;

  return strSum >= mul ? strSum : mul;
}

solution(2, 91);

// toString, a+""+b+""
