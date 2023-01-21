function solution(nums) {
  var answer = 0;

  const numKind = new Set(nums);

  answer = Math.min(numKind.size, nums.length / 2);

  return answer;
}
