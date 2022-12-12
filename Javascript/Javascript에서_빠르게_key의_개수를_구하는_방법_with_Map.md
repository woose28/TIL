# 들어가며
Javascript에서 Map 자료구조가 있다. 이 자료구조는 Object와 유사하지만 시간 복잡도 측면에서 더 뛰어난 측면이 존재한다.

<br/>

# Key의 개수를 구하는 방법
두 자료구조는 저장된 key의 개수를 구할 때 차이가 발생한다.

<br/>

Map 자료 구조의 경우 내부적으로 `size`프로퍼티를 가지고 있다. 해당 프로퍼티를 사용하면 자료구조 내부에 저장된 key의 개수를 반환받을 수 있다.
해당 프로퍼티의 시간 복잡도는 O(1)이다.

<br/>

```javascript
  const test = new Map();

  test.set('a', 1);
  test.set('b', 2);

  test.size // 2
```

<br/>

반면 일반 Object의 key의 개수를 구할 때는 직접 코드를 구현해야 한다.
일반적으로 Object에서 key의 개수를 구하는 코드는 다음과 같다.

<br/>

```javascript
  const test = {
    'a': 1,
    'b': 2,
  }

  Object.keys(test).length; // 2
```

<br/>

간단한 코드이지만 `Object.keys()`의 시간복잡도가 O(N)이다.
때문에 Object의 key의 개수를 계산하는 시간이 Map 자료구조를 이용할 때보다 더 오래 걸린다.

<br/>

# 끝으로
데이터의 개수가 많아질 때 위 차이점으로 인한 성능이 차가 더욱 체감될 것이다.

<br/>

또한 위 차이점 이외에 Object와 Map 자료구조의 차이점은 몇 가지 더 있다.
이에 대해서는 [여기에](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#objects_vs._maps) 정리가 되어있다.

💡 실제 상황은 아니지만 [이 문제](https://school.programmers.co.kr/learn/courses/30/lessons/67258)를 풀어본다면 간접적으로 차이점을 느낄 수 있다.

<br/>

# 참고 자료
[MDN - Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)  
[Stackoverflow - es6 Map and Set complexity, v8 implementation](https://stackoverflow.com/questions/33611509/es6-map-and-set-complexity-v8-implementation)  
[Stackoverflow - Object.keys() complexity?](https://stackoverflow.com/questions/7716812/object-keys-complexity)  

<br/>

# TODO
1. v8 엔지에서 Map 구현체 살펴보기
2. hash table 자료구조에 관해 공부하기
