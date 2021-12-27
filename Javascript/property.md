### 📌 프로퍼티(Property)

### 프로퍼티 종류
- 데이터 프로퍼티(data property)
    - 데이터를 갖는 프로퍼티, 일반적으로 사용하는 프로퍼티가 여기에 속한다.
- 접근자 프로퍼티(accesor property)
    - 다른 데이터 프로퍼티에 접근하기 위해 사용하는 프로퍼티
    - `getter` 또는 `setter` 등의 접근자 함수로 구성된다.

### 프로퍼티 어트리뷰트(Attribute)
- 프로퍼티의 상태를 나타낸다.
    - 프로퍼티 어트리뷰트는 [Object.getOwnPropertyDescriptors()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptors) 메서드를 통해 확인 가능하다.

- 데이터 프로퍼티의 어트리뷰트
    - value
        - 프로퍼티에 연관된 값으로, key로 접근하는 value에 해당된 값
        - 예시
        ```javascript
            const test = {};
            Object.defineProperty(test, 'a', { value: 10 });

            console.log(test.a); // 출력 결과: 10
        ```

    - writable
        - 프로퍼티의 수정 여부를 표현하는 값
        - `writable` 값이 `true`이면 해당 프로퍼티는 수정할 수 있다.

    - enumerable
        - 프로퍼티의 열거 가능 여부를 표현하는 값
        - `enumerable` 값이 `true`이면 해당 프로퍼티는 열거할 수 있다.
            - `enumerable` 값이 `true`이면 [Object.keys()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) 메서드의 반환 값에 포함되고, `false`이면 포함되지 않는다.

    - configurable
        - 프로퍼티의 재구성 여부를 표현하는 값
        - `configurable` 값이 `false`이면 프로퍼티의 삭제와 어트리뷰트 수정이 불가능하다.
            - 단, `configurable` 값이 `false`이고 `writable` 값이 `true`인 경우 예외적으로 `value`와 `writable` 어트리뷰트를 수정할수 있다.

- 접근자 프로퍼티의 어트리뷰트
    - get
        - 접근자 프로퍼티로 값을 읽을 때 호출되는 함수
        - 함수 내부에서 다른 데이터 프로퍼티의 값을 반환하도록 구현된다.
    - set
        - 접근자 프로퍼티로 값을 저장할 때 호출되는 함수
        - 함수 내부에서 다른 데이터 프로퍼티에 값을 저장하도록 구현된다.

    - enumerable
        - 데이터 프로퍼티의 `enumerable` 어트리뷰트와 같다.
    - configurable
        - 데이터 프로퍼티의 `configurable` 어트리뷰트와 같다.

### 프로퍼티 등록
- 객체에 프로퍼티와 프로퍼티 어트리뷰트를 등록할 때 [Object.defineProperty()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty) 메서드를 활용할 수 있다.
    - `Object.defineProperty()` 메서드의 `descriptor` 객체를 통해 데이터 프로퍼티 또는 접근자 프로퍼티의 어트리뷰트를 기술할 수 있다.

### 예시
- `Object.defineProperty()`를 활용하지 않는 예시
```javascript
const testObj = {
  _a: 10,
  get a() {
    console.log('getter 호출됨');
    return this._a;
  },
  set a(newValue) {
    console.log('setter 호출됨');
    this._a = newValue;
  },
};

console.log(testObj.a);

testObj.a = 100;

console.log(testObj.a);

/**
 * 출력 결과
 * getter 호출됨
 * 10
 * setter 호출됨
 * getter 호출됨
 * 100
 */
```

- `Object.defineProperty()`를 활용하는 예시
```javascript
const testObj = {};

Object.defineProperty(testObj, '_a', { value: 10, writable: true });
Object.defineProperty(testObj, 'a', {
  get() {
    console.log('getter 호출됨');
    return this._a;
  },
  set(newValue) {
    console.log('setter 호출됨');
    this._a = newValue;
  },
});

console.log(testObj.a);

testObj.a = 100;

console.log(testObj.a);

/**
 * 출력 결과
 * getter 호출됨
 * 10
 * setter 호출됨
 * getter 호출됨
 * 100
 */
```


### 📚 참고 자료
- 모던 자바스크립트 Deep Dive - Ch.16 프로퍼티 어트리뷰트
- [MDN Web Docs - Object.defineProperty](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
- [Vanilla Javascript로 상태관리 시스템 만들기](https://junilhwang.github.io/TIL/Javascript/Design/Vanilla-JS-Store/#_1-중앙-집중식-상태관리)
