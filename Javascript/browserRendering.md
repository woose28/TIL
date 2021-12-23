## 📌 브라우저의 렌더링 과정

### 💡 사전 지식
1. 브라우저의 핵심 기능은 서버로 리소스(html, css, 이미지, 폰트 등)를 요청하고, 응답으로 받은 리소스를 화면에 시각적으로 표시하는 것
2. 렌더링은 HTML, CSS, Javascript 등의 리소스를 파싱하여 화면에 출력하는 일이다.

<br>

### 🤔 브라우저의 렌더링 과정을 공부해야 하는 이유
- HTML 요소의 크기와 위치를 계산하는 작업인 `레이아웃`과 렌더링 트리를 픽셀로 변환시키는 작업인 `페인트`는 비용이 많이 드는 작업이다.
- 성능을 최적화하기 위해서는 위 두 작업이 실행되는 `리렌더링(Rerendering)`을 최소화해야 한다.
- 따라서, 렌더링 과정을 알고 있어야 성능 최적화 방법에 대해서 이해할 수 있다!

<br>

### ✔️ 렌더링 과정
1. DOM Tree 생성
    - `DOM(Document Object Model)`은 렌더링 엔진이 HTML 문서를 파싱해서 생성한다.
    - 렌더링 엔진은 HTML을 한 줄씩 파싱하면서 `DOM`을 생성한다.
    - HTML 문서를 파싱해서 `DOM` 트리를 생성하는 과정은 다음과 같다.
        1. 서버로부터 `byte(바이트)` 형태로 전달받은 문서를 인코딩 방식에 맞게 문자열로 변환한다.
        2. 문자열로 변환한 문서 데이터를 해석하여 의미를 갖는 최소 단위인 `token(토큰)`으로 해석한다.
        3. `token`을 기반으로 `node(노드)` 객체를 생성한다. 이 `node`는 `DOM`을 구성하는 기본 요소이다.
        4. `node`를 중첩하여 트리형 자료구조인 `DOM`을 생성한다.

    - HTML 문서를 토큰화하고 트리를 구축하는 과정은 [이곳의](https://d2.naver.com/helloworld/59361) `토큰화 알고리즘`과 `트리 구축 알고리즘` 파트에 자세히 설명되어 있다.

2. CSSOM Tree 생성
    - 렌더링 엔진이 HTML을 파싱하면서 CSS를 불러오는 `link` 태그나 `style` 태그를 만나면 `DOM`을 생성하는 과정을 잠시 중단하고, CSS의 파싱을 시작한다.
    - CSS를 파싱하면 결과물로 `CSSOM(CSS Object Model)`을 생성한다.
    - CSS 파싱이 끝나면 다시 HTML을 파싱하여 `DOM`을 재개한다.

3. Render Tree 생성
    - `DOM`과 `CSSOM`은 `Render(렌더)` 트리로 결합된다.
    - `Render` 트리는 화면에 보이는 `node`만 포함한다.
        - 따라서, script 태그나 CSS에 의해 display:none 스타일이 적용된 노드는 포함되지 않는다.

4. 레이아웃
    - HTML 요소의 위치와 크기를 계산하는 과정

5. 페인트
    - 브라우저 화면에 렌더링 트리를 픽셀로 보여주는 과정
    

### Reflow(리플로우)와 Repaint(리페인트)
`DOM`과 `CSSOM`은 javascript에 의해 수정이 될 수 있다.
수정된 `DOM`과 `CSSOM`은 다시 렌더 트리에 결합이 되고 `레이아웃` 과정과 `페인트` 과정이 다시 실행된다.
`레이아웃` 과정을 다시 거치는 경우를 `Reflow`라고 하며, `페인트` 과정을 다시 거치는 경우를 `Repaint`라고 한다.

* 만약 `DOM`과 `CSSOM`의 수정이 레이아웃에 영향을 주는 작업이 아니라면, `Repaint`만 실행된다.

<br>

### Javascript의 실행과 권장되는 위치
렌더링 엔진이 HTML을 파싱하다가 `script` 태그를 만나면 `DOM` 생성을 잠시 중단하고,
Javascript 엔진이 Javascript를 파싱하고 실행한다.

즉, HTML을 파싱하는 과정과 Javascript를 파싱하는 과정이 동기적으로 수행되기 된다.

따라서 DOM 생성을 빠르게 완료하고 Javascript에서 DOM 조작 시 에러를 피하기 위해서 body 요소 가장 아래에 Javascript를 배치하는 것이 권장된다.

<br>

### 📚 참고 자료
- [Naver D2 - 브라우저는 어떻게 동작하는가?](https://d2.naver.com/helloworld/59361)
- [Vanilla Javascript로 상태관리 시스템 만들기](https://junilhwang.github.io/TIL/Javascript/Design/Vanilla-JS-Store/#_1-중앙-집중식-상태관리)
- 모던 자바스크립트 Deep Dive - Ch38 브라우저의 렌더링 과정
