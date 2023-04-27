function solution(maps) {
  var answer = [];
  maps = maps.map((m) => m.split(""));
  //   console.log(maps);

  function dfs(r, c) {
    if (
      r < 0 ||
      c < 0 ||
      r >= maps.length ||
      c >= maps[0].length ||
      maps[r][c] === "X"
    ) {
      return 0;
    } else {
      var num = parseInt(maps[r][c]);
      maps[r][c] = "X";
      return (
        num + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
      );
    }
  }

  for (let row = 0; row < maps.length; row++) {
    for (let col = 0; col < maps[0].length; col++) {
      if (maps[row][col] !== "X") {
        answer.push(dfs(row, col));
      }
    }
  }

  if (answer.length === 0) {
    return [-1];
  } else {
    console.log(answer.sort((a, b) => a - b));
    return answer.sort((a, b) => a - b);
  }
}

solution(["X591X", "X1X5X", "X231X", "1XXX1"]);
