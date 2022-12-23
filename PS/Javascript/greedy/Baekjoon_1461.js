const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [NMString, bookString] = data;
const [N, M] = NMString.split(" ").map(Number);
const books = bookString.split(" ").map(Number);

function solution(N, M, books) {
  books.sort((a, b) => a - b);

  let answer = 0;

  const pivot = books.findIndex((pos) => pos > 0);

  if (pivot === -1) {
    for (let i = 0; i < N; i += M) {
      answer += Math.abs(books[i]) * 2;
    }
  } else if (pivot === 0) {
    for (let i = N - 1; i > -1; i -= M) {
      answer += books[i] * 2;
    }
  } else {
    for (let i = 0; i < pivot; i += M) {
      answer += Math.abs(books[i]) * 2;
    }

    for (let i = N - 1; i >= pivot; i -= M) {
      answer += books[i] * 2;
    }
  }

  answer -= Math.max(Math.abs(books[0]), Math.abs(books[N - 1]));

  console.log(answer);
}

solution(N, M, books);
