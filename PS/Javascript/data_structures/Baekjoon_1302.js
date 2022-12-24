const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(data) {
  const [N, ...titles] = data;

  const sales = {};

  for (const title of titles) {
    if (!sales.hasOwnProperty(title)) {
      sales[title] = 1;
      continue;
    }

    sales[title] = sales[title] + 1;
  }

  const sortedSalesArray = Object.entries(sales).sort((a, b) => {
    if (a[1] > b[1]) {
      return -1;
    } else if (a[1] < b[1]) {
      return 1;
    } else {
      if (a[0] > b[0]) {
        return 1;
      }

      return -1;
    }
  });

  console.log(sortedSalesArray[0][0]);
}

solution(data);
