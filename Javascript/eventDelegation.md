## 📌 이벤트 위임

### 💡 사전 지식
1. 이벤트 전파는 총 세 가지 단계가 순차적으로 진행된다.
    - 캡쳐링 단계: 부모 엘리먼트에서 자식 엘리먼트로 이벤트가 전달되는 과정
    - 타깃 단계: 이벤트가 타깃에 도창한 시점
    - 버블링 단계: 이벤트 타깃에서 부모 엘리먼트로 이벤트가 전달되는 과정

<br>

### 이벤트 위임이란?
- 자식 엘리먼트에서 발생된 이벤트를 부모 엘리먼트에서 처리하는 방식이다.
- 부모 엘리먼트에서 이벤트를 처리하기 위해 부모 엘리먼트에 이벤트 핸들러를 바인딩한다.

<br>

### 특징
- 주로 동적으로 생성되는 자식 엘리먼트들의 이벤트를 처리하기 위해 사용된다.
- 원하는 자식 엘리먼트의 이벤트를 처리하기 위해 발생된 이벤트 타킷을 확인할 필요가 있다.

<br>

### 예시
```html
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>이벤트 위임 연습</title>
</head>
<body>
    <div>
        <ul id="fruits">
            <li class="fruit">사과</li>
            <li class="fruit">바나나</li>
            <li class="fruit">체리</li>
        </ul>
    </div>
    <script>
        const $fruits = document.querySelector('#fruits');

        $fruits.addEventListener('click', (event) => {
            if (!event.target.classList.contains('fruit')) { // 이벤트 타깃의 class를 확인
                return;
            }

            console.log(`현재 클릭된 과일 이름은 ${event.target.textContent}입니다.`)
        });
    </script>
</body>
```

