## 📌 싱글톤 패턴

### 💻 싱글톤 패턴이란?
- 시스템에서 한 클래스에 대해서 하나의 인스턴스만 존재하도록 보장하는 디자인 패턴
- 싱글톤 패턴으로 설계된 클래스는 하나의 인스턴스만을 가진다.
    - 생성자 함수를 여러 번 호출해도, 동일한 인스턴스가 반환된다.

<br>

### 🤔 싱글톤 패턴을 공부하는 이유
- 요즘 많이 사용되는 React와 Vue와 같은 프레임워크는 상태를 기반으로 DOM 렌더링 한다.
- 이 프레임워크들은 중앙에서 상태를 관리하기 위해 `상태 관리 라이브러리`를 이용한다.
    - React는 주로 [Redux](https://ko.redux.js.org/introduction/getting-started/)를 사용하고, Vue는 [Vuex](https://vuex.vuejs.org/kr/)를 주로 사용한다.
- 이런 `상태 관리 라이브러리`들은 `싱글톤 패턴`을 기반으로 생성된 저장소(Store)에서 상태값을 관리한다.
- 따라서, `상태 관리 라이브러리`를 이해하기 위해서 `싱글톤 패턴`에 대해서 공부하는 것이 필요!

<br>

### 사용 예시
- 객체 리터럴
```javascript
const test1 = {
  a: 123,
  b: 100,
};

const test2 = {
  a: 123,
  b: 100,
};

console.log(test1 === test2); // true
```

<br>

- 클로저(closure)을 이용한 방식
```javascript
const Test = (function () {
  let instance = null;

  function init() {
    return {
      p1: 100,
      p2: 200,
    };
  }
  return {
    getInstance() {
      if (instance === null) {
        instance = init();
      }

      return instance;
    },
  };
})();

const test1 = Test.getInstance();
const test2 = Test.getInstance();
console.log(test1 === test2); // true

test1.p1 = 1;

console.log(test1.p1); // 1
console.log(test2.p1); // 1
```

<br>

- ES6 이후 Class 키워드를 이용한 방식
```javascript
let instance = null;

class Test {
  constructor() {
    if (instance !== null) {
      return instance;
    }

    instance = this;
  }
}

const test1 = new Test();
const test2 = new Test();

console.log(test1 === test2); // true
```

<br>

### 📚 참고 자료
- [Vuex가 무엇인가요?](https://vuex.vuejs.org/kr/)
- [Vanilla Javascript로 상태관리 시스템 만들기](https://junilhwang.github.io/TIL/Javascript/Design/Vanilla-JS-Store/#_1-중앙-집중식-상태관리)
