## 📌 데이터 속성

### 💻 데이터 속성이란?
- HTML 엘리먼트에 추가적인 정보를 저장할 수 있는 표준적인 방법
- HTML5에서 추가된 개념

<br>

### ✔️ 사용 법

**HTML**
- `data-데이터 이름` 형식으로 데이터 속성을 저장

```html
<div
    id="apple"
    data-id="1"
    data-name="사과"
    data-price="100"
    data-country-origin="korea"
>
    사과
</div>
```

<br>

**Javascript**
- DOM 엘리먼트에 저장된 데이터 속성은  dataset 프로퍼티를 통해 접근할 수 있다.
- `data-word1-word2` 형식으로 저장된 속성은 `$target.dataset.word1Workd2` 형식으로 접근이 가능하다.
    - 즉, 데이터 속성에 접근할 때는 camelCase로 접근을 한다.
- 동적으로 DOM 엘리먼트에 데이터 속성을 추가할 때는 `setArrtibute` 메서드를 이용하면 된다.

```html
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>데이터 속성 연습</title>
</head>
<body>
    <div
        id="apple"
        data-id="1"
        data-name="사과"
        data-price="100"
        data-country-origin="korea"
    >
        사과
    </div>
    <script>
        $apple = document.querySelector('#apple');

        console.log('data-name: ', $apple.dataset.name);
        console.log('data-country-origin: ', $apple.dataset.countryOrigin);

        $apple.setAttribute('data-quality', 'best');

        console.log('data-quality: ', $apple.dataset.quality);
    </script>
</body>

```

<br>

### ❗️단점
- 웹 크롤러에서 데이터 속성은 인덱싱 하지 않는다.
    - 따라서 검색 엔진을 통한 노출이 필요한 정보는 데이터 속성으로 사용하면 안된다.
- IE 11 이전 버전에서는 dataset 기능을 제공하지 않는다.

