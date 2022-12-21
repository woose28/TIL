const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [C, ...playerList] = data;

function solution(players) {
  let answer = 0;
  const position = Array(11).fill(false);

  function recursion(curPlayer, curScore) {
    if (curPlayer === 11) {
      answer = Math.max(answer, curScore);
      return;
    }

    const abilities = players[curPlayer];

    abilities.forEach((ability, index) => {
      if (ability > 0 && !position[index]) {
        position[index] = true;
        recursion(curPlayer + 1, curScore + ability);
        position[index] = false;
      }
    });
  }

  recursion(0, 0);

  console.log(answer);
}

for (let i = 0; i < Number(C); i++) {
  const player = playerList.slice(11 * i, 11 * (i + 1));

  const playerArray = player.map((player) => player.split(" ").map(Number));

  solution(playerArray);
}
