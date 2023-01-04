function solution(want, number, discount) {
  var answer = 0;

  const wantObj = new Map();
  const discountObj = new Map();

  function checkSignUpDate() {
    return want.every(
      (wantItem) => wantObj.get(wantItem) <= discountObj.get(wantItem)
    );
  }

  function addItemToObj(obj, item, count = 1) {
    if (obj.has(item)) {
      obj.set(item, obj.get(item) + count);
      return;
    }

    obj.set(item, count);
  }

  want.forEach((wantItem, index) => {
    const count = number[index];

    addItemToObj(wantObj, wantItem, count);
  });

  for (let i = 0; i < 10; i++) {
    const curItem = discount[i];

    addItemToObj(discountObj, curItem);
  }

  if (checkSignUpDate()) {
    answer += 1;
  }

  for (let i = 10; i < discount.length; i++) {
    const curItem = discount[i];
    const removedItem = discount[i - 10];

    addItemToObj(discountObj, curItem);

    discountObj.set(removedItem, discountObj.get(removedItem) - 1);

    if (checkSignUpDate()) {
      answer += 1;
    }
  }

  return answer;
}
