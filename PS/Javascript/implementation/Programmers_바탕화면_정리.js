function solution(wallpaper) {
  var answer = [];

  let lux = Infinity;
  let luy = Infinity;

  let rdx = -Infinity;
  let rdy = -Infinity;

  wallpaper.forEach((row, rowIndex) => {
    row.split("").forEach((space, columnIndex) => {
      if (space === "#") {
        if (luy > columnIndex) {
          luy = columnIndex;
        }

        if (lux > rowIndex) {
          lux = rowIndex;
        }

        if (rdy < columnIndex + 1) {
          rdy = columnIndex + 1;
        }

        if (rdx < rowIndex + 1) {
          rdx = rowIndex + 1;
        }
      }
    });
  });

  answer = [lux, luy, rdx, rdy];

  return answer;
}
