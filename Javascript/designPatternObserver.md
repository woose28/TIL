### 📌 옵저버 패턴

### 💻 옵저버 패턴이란?
- 객체의 상태변화를 관찰하는 관찰자(옵저버)를 객체에 등록하고, 상태 변화가 있을 때마다 메서드를 통해 객체가 등록된 옵저버에 통지하는 디자인 패턴
- 관찰 대상인 객체를 `Subject`라고 표현하기도 한다.
- `Subject`에 변화가 있을 때마다 등록된 모든 `Observer`에 변화를 알려주는 것이 옵저버 패턴이다.

<br>

### 🔎 옵저버 패턴 사용된 사례
- Javascript에서 `addEventListener` 메서드를 이용해서 이벤트 핸들러를 등록시키는 패턴이 Javascript에서 대표적으로 옵저버 패턴이 사용된 예시
- `상태 관리 라이브러리`에서 상태 값이 변했을 때, `Store`를 구독하고 있는 `Component`를 다시 렌더링 하는 과정도 옵저버 패턴의 예시이다.

<br>

### 사용 예시
- 생성자 함수를 이용하는 경우
```javascript
function Subject() {
  this.state = {};
  this.observers = new Set();
}

Subject.prototype = {
  addObserver(observer) {
    this.observers.add(observer);
  },
  removeObserver(targetObserver) {
    this.observers = new Set([...this.observers].filter((observer) => observer !== targetObserver));
  },
  notifyObservers() {
    this.observers.forEach((observer) => {
      observer.notify(this.state);
    });
  },
  setState(newState) {
    this.state = { ...this.state, ...newState };
    this.notifyObservers();
  },
};

const subject = new Subject();

const observer1 = {
  notify: (state) => {
    console.log('observer1로 전달받은 state: ', state);
  },
};

const observer2 = {
  notify: (state) => {
    console.log('observer2로 전달받은 state: ', state);
  },
};

subject.addObserver(observer1);
subject.addObserver(observer2);
subject.setState({ a: 100 });
subject.setState({ b: 200 });

subject.removeObserver(observer1);
subject.setState({ c: 300 });
```

<br>

- class를 이용하는 경우
```javascript
class Subject {
  constructor() {
    this.state = {};
    this.observers = new Set();
  }

  addObserver(observer) {
    this.observers.add(observer);
  }

  removeObserver(targetObserver) {
    this.observers = new Set([...this.observers].filter((observer) => observer !== targetObserver));
  }

  notifyObservers() {
    this.observers.forEach((observer) => {
      observer.notify(this.state);
    });
  }

  setState(newState) {
    this.state = { ...this.state, ...newState };
    this.notifyObservers();
  }
}

const subject = new Subject();

const observer1 = {
  notify: (state) => {
    console.log('observer1로 전달받은 state: ', state);
  },
};

const observer2 = {
  notify: (state) => {
    console.log('observer2로 전달받은 state: ', state);
  },
};

subject.addObserver(observer1);
subject.addObserver(observer2);
subject.setState({ a: 100 });
subject.setState({ b: 200 });

subject.removeObserver(observer1);
subject.setState({ c: 300 });
```

<br>

두 예시 모두 아래와 같은 동일한 출력 결과를 가집니다.
```bash
observer1로 전달받은 state:  { a: 100 }
observer2로 전달받은 state:  { a: 100 }
observer1로 전달받은 state:  { a: 100, b: 200 }
observer2로 전달받은 state:  { a: 100, b: 200 }
observer2로 전달받은 state:  { a: 100, b: 200, c: 300 }
```

<br>

### 📚 참고 자료
- [위키백과 - 옵저버 패턴](https://ko.wikipedia.org/wiki/옵서버_패턴)
- [Clpa Yeon - (Design Pattern) Observer Pattern 이란?](https://medium.com/@su_bak/design-pattern-observer-pattern-이란-ef4b74303359)
- [Vanilla Javascript로 상태관리 시스템 만들기](https://junilhwang.github.io/TIL/Javascript/Design/Vanilla-JS-Store/#_1-중앙-집중식-상태관리)

