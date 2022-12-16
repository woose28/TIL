function solution(sticker) {
  var answer = 0;
  const stickerCount = sticker.length;

  if (stickerCount <= 2) {
    return Math.max(...sticker);
  }

  const dp1 = new Array(stickerCount).fill(0);
  const dp2 = new Array(stickerCount).fill(0);

  dp1[0] = sticker[0];
  dp1[1] = sticker[0];

  dp2[1] = sticker[1];

  for (let i = 2; i < stickerCount; i++) {
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + sticker[i]);
    dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + sticker[i]);
  }

  answer = Math.max(dp1[stickerCount - 2], dp2[stickerCount - 1]);

  return answer;
}
