## 📌 클로저(Closure)

### 💻 클로저란?
- 클로저는 함수와 주변 상태(lexical environment)의 조합이다.
- 클러저는 내부에 있는 함수로, 외부 함수의 스코프에 접근 가능하게 하는 함수이다.

<br>

### ✔️ 사용 예시
- 익명 함수와 함께 사용한 예시
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <title>클로저 연습</title>
  </head>
  <body>
    <div id="count-value">0</div>
    <button id="button-increase">+</button>
    <script>
      const $countValue = document.querySelector('#count-value');
      const $buttonIncrease = document.querySelector('#button-increase');

      // 여기서 익명 함수가 외부 함수이고, 이 함수는 호출 후 바로 소멸이 된다.
      // 익명 함수는 함수를 반환하며, 반환된 함수는 increaser 식별자로 접근 가능하다.
      // increaser 식별자로 접근하는 함수 내부에는 count 변수가 정의되어 있지 않다.
      // 하지만 이 함수가 선언된 곳 외부에 count가 정의됐고, 이 함수가 실행되면 외부에 정의됐던 count에 접근하게 된다.
      // 따라서, increaser 식별자로 접근하는 이 함수는 클로저이다.
      const increaser = (function() {
        let count = 0;

        return function() {
          count += 1;
          return count;
        }
      })();

      $buttonIncrease.addEventListener('click', () => {
        $countValue.innerHTML = increaser();
      });
    </script>
  </body>
</html>
```

- 생성자 함수와 함께 사용한 예시
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <title>클로저 연습</title>
  </head>
  <body>
    <div id="count-value">0</div>
    <button id="button-increase">+</button>
    <button id="button-decrease">-</button>
    <script>
      const $countValue = document.querySelector('#count-value');
      const $buttonIncrease = document.querySelector('#button-increase');
      const $buttonDecrease = document.querySelector('#button-decrease');

      // count 변수는 this로 바인딩 되지 않았기 때문에, 생성한 인스턴스로 접근이 불가능하다.
      // 여기서 increase와 decrease 메서드는 외부에 선언된 count에 접근 가능하게 해주는 클로저이다.
      const Counter = function() {
        let count = 0;

        this.increase = function() {
          count += 1;

          return count;
        }
        
        this.decrease = function() {
          count -= 1;

          return count;
        }
      }

      const counter = new Counter();

      $buttonIncrease.addEventListener('click', () => {
        $countValue.innerHTML = counter.increase();
      });

      $buttonDecrease.addEventListener('click', () => {
        $countValue.innerHTML = counter.decrease();
      });
    </script>
  </body>
</html>
```

<br>

### ❗️ 특징
- 클로저를 사용하면 전역 변수를 사용하지 않고 상태 값을 유지할 수 있다.
- 객체를 생성할 때, 정보 은닉을 구현할 수 있다.

<br>

### 📚 출처
- [MDN Web Docㄴ - Closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [poiemaweb.com - 5.19 Closure](https://poiemaweb.com/js-closure)
