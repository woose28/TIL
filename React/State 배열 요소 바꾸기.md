# State 배열 요소 바꾸기
### Concat

기존 배열을 그대로 두고 요소를 추가하여 새로운 배열을 생성하는 함수

```jsx
this.setState({
	list: this.state.list.concat(newObj)
});
```

### Immutability Helper

객체나 배열의 수정을 편하게 도와주는 라이브러리

기존 데이터를 복사 한후 사용자 요청에 따라 처리를 수행한다. 그 후 새로운 데이터를 반환한다.

추가 라이브러리 설치가 필요

```bash
npm install --save react-addons-update
```

위 라이브러리가 임포트가 안된다면 아래의 방법으로 설치 후 라이브러리를 사용하라

```bash
npm install --save immutability-helper
```

```jsx
import update from 'immutability-helper';

```

데이터 추가

```jsx
import update from 'react-addons-update';
this.setStae({
	list:update(this.state.list,
			{
				$push:[newObj]
			}
	)
});
```

데이터 삭제

```jsx
import update from 'react-addon-update';

this.setState({
	list:update(this.state.list,{
			$splice:[[index,1]]
	});
});
```

데이터를 여러개 삭제할 때는 한 번 삭제 할 때 마다 인덱스 번호가 초기화 되는 점을 유의하자

데이터 수정

```jsx
import update from "react-addon-update";

this.setState({
	list:update(this.state.list,
			{
				[index]:{
					field_01:{$set:"value_01"},
					field_02:{$set:"value_02"}
				}		
		});
});
```

### Spread

```bash
npm install --save babel-preset-stage-0
```

추가적인 webpack.config.js 수정이 필요

---

### 출처

- React & Express를 이용한 웹 어플리케이션 개발하기

    [https://www.inflearn.com/course/react-강좌-velopert/lecture/4152?tab=note&mm=close](https://www.inflearn.com/course/react-%EA%B0%95%EC%A2%8C-velopert/lecture/4152?tab=note&mm=close)
