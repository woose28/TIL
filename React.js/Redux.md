
# Redux
### Redux 설치

```bash
npm install --save redux react-redux
```

atom을 사용한다면 linter-eslint 모듈을 추가 설치하는 것을 권유한다.

### Action

Action = 작업에 대한 정보를 가지고 있는 객체

Action의 이름(Action의 타입)은 대문자와 언더바를 이용해서 작성한다.

⇒ 상수 이름을 짓는다고 생각하면 된다.

Action 객체를 반환하는 함수의 이름은 보통 camelCase를 따라서 짓는다.

```jsx
//Action 객체
{
	type : "타입"
	추가 필요한  자료 ...
}
```

Action 객체에는 반드시 type이 명시돼야 한다.

### Reducer

Reducer = 변화를 일으키는 함수이며 reducer 함수는 3가지 조건이 있다.

즉 이전 상태와 액션을 받아서 다음 상태를 반환한다.

⇒ 전달 받은 기존 상태를 복사하여 액션에 따라 변경 후 복사한 상태를 반환한다.

Reducer 함수 조건

- 비동기 작업 X
- 인수 변경 X
- 동일한 인수 = 동일한 결과

Reducer에는 초기 상태를 정의한 객체가 필요하다.

Action 함수는 dispatch에 의해 Reducer에 전달되고 Reducer는 수신받은 Action의 Type에 따라 State에 변화를 준 후 변경된 State 객체를 반환한다.

Reducer가 2개 이상이라면 Reducer를 합쳐주는 작업이 필요하다.

```jsx
import {combineReducers} from 'redux';
//redux의 combineReducers 이용

const reducers = combineReducers({
	reducer 이름, reducer 이름, ...
});

export default reducers
```

### Store

Store = 어플리케이션의 현재 상태를 지니고 있음

Redux에는 하나의 Store만 존재해야한다.

redux에서 createStore를 불러오고 reducer를 전달해서 만든다.

```jsx
import {createStore} import 'redux';

const store = createStore(reducers);

```

Store가 하는 일

- dispatch(action)

    action을 reducer로 보낸다. store는 reducer 함수에 현재 상태와 방금 받은 action을 전달한다. reducer 함수가 실행 된 후 반환 받은 상태를 저장한다.

- getState()

    현재 상태를 반환한다.

- subscribe(listener)

    상태가 바뀔 떄마다 실행할 함수를 등록하는 함수이다.

    listener은 상태가 바뀔 때 실행되는 함수이다.

    subscribe(listener)의 반환 값은 unsubscribe 함수로 반환 받은 함수를 실행 시키면

    상태 변화가 발생해도 listener 함수가 실행되지 않는다.

- replaceReducer(nextReducer)

    hot reloading과 코드 분할을 이용할 때 구현하는 것으로 거의 사용이 안된다.

### react-redux

view layer binding 도구

react component에서 redux를 사용할 떄 복잡한 작업을 처리해준다.

react-redux 핵심 기능

- Provider

    react component에서 redux 기능을 쉽게 이용 가능하도록 한다.

    Provider 역시 Component 이다.

- connect

    component에 redux를 연결한다.

    주로 Smart Component에서 수행하는 것 같다.

    사용법은 아래와 같다.

    ```jsx
    import {connect} from 'react-redux';

    ...

    connect([options])(컴포넌트 이름);

    ```

    connect 함수에서 자주 사용되는 option

    mapStatetoProps : store에 state가 매개 변수로 전달 되며  state를 component의 props로 매핑한 객체를 전달한다.

    mapDispatchtoProps : dispatch가 매개 변수로 전달 되며 dispatch에 action 생성자를 연결하여 component의 props로 매핑한 객체를 전달한다.

---

### 참고자료

- **React & Express 를 이용한 웹 어플리케이션 개발하기**

    [https://www.inflearn.com/course/react-강좌-velopert/dashboard](https://www.inflearn.com/course/react-%EA%B0%95%EC%A2%8C-velopert/dashboard)

- **Redux 카툰 안내서**

    [http://bestalign.github.io/2015/10/26/cartoon-intro-to-redux/](http://bestalign.github.io/2015/10/26/cartoon-intro-to-redux/)
