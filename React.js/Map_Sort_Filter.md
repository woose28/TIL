# Map_Sort_Filter
### Map

주어진 배열의 요소들에 동일한 함수를 적용 시킨 후 결과를 배열로 반환한다.

syntax

```jsx
arr.map(callback(currentValue[, index[, array]])[, thisArg])
```

예시

```jsx
[1,2,3,5].map((v)=>{return v+1;})
//반환 값 : [2, 3, 4, 6]
```

- Doc for

    [https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

### Sort

주어진 배열의 값을 정렬하는 메서드로 정렬된 결과가 원래 배열에 적용이 된다.

syntax

```bash
arr.sort([compareFunction])
```

[compareFunction]이 주어지지 않으면 기본으로 유니코드 기반으로 비교를 한다.

문자열 정렬 예시

```jsx
var fruits = ["Apple", "Cherry", "Banana"];
fruits.sort();

console.log(fruits);
//출력 값 : ["Apple", "Banana", "Cherry"]
```

숫자 정렬 예시

```jsx
function compareNumbers(a, b){
	return a - b;
}

function compareNumbersReverse(a, b){
    return (a-b) * -1;
}

var numbers = [1, 100, 6554, 8, 5];

numbres.sort(compareNumbers);
console.log(numbers);
//출력 값 : [1, 5, 8, 100, 6554]

numbres.sort(compareNumbersReverse);
console.log(numbers);
//출력 값 : [6554, 100, 8, 5, 1]
```

- Doc for sort

    [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

**Filter**

주어진 배열에서 특정 조건을 만족하는 원소들만 모아 새로운 배열로 반환

*기존 배열에는 영향을 주지 않는다.

syntax

```jsx
arr.filter(callback(element[, index[, array]])[, thisArg])
```

예시

```jsx
function isBigEnough(value){
    return value >= 10;
}

var filtered = [12, 5, 8, 130, 44];
filtered.filter(isBigEnough);
//반환 된 배열은 [12, 130, 44]

console.log(filtered);
//출력 값 : [12, 5, 8, 130, 44]
```

- Doc for Filter

    [https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
