# Node.js, npm 기본
### 프로젝트 생성


```bash
npm init
```

현재 디렉토리에 node js 프로젝트를 만들어 주는 명령어 프로젝트 정보에 대한 간단한 질문 몇개를 입력 하면 프로젝트가 생성이 되며 해당 정보들은

현재 폴더 package.json에 기록된다.

```bash
npm init -y
```

-y 옵션은 질문을 생략하고 바로 package.json을 생성해준다.

```json
#npm init -y를 통해 생성한 package.json
{
  "name": "practice_project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

package.json에는 프로젝트에 대한 기본 정보가 담겨져 있다.

또한 'scripts ' 에는 프로젝트에서 실행할 수 있는 명령어를 지정할 수 있다.

```json
{
  "name": "practice_project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
		"build" : "빌드 명령어"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

위 처럼 scripts에 build라는 사용자 명령어를 추가할 수 있으며

```bash
npm run build
```

위의 명령어로  실행 할 수 있다.

### 패키지 다운로드

```bash
npm install --svae 패키지 이름
```

```bash
npm install --save-dev 패키지 이름
#--save-dev는 -D로도 사용이 된다.
#npm install -D 패키지 이름
#이 명령어도 같은 기능을 수행한다.
```

—save-dev를 사용하면 package.json에 개발용 모듈이 따로 그룹화 된다.

패키지의 버전은 유의적 버전 체계를 따른다.

예를 들어 14.5.2 가 있을 때

14는 주버전(Major version), 5는 부버전(Minor version), 2는 수버전(Patch version)을 의미한다.

또한 버전 앞에는 ~(틸드)와 ^(캐럿)가 붙는데 이는 허용가능한 버전의 범위를 나타낸다.

- 틸드 범위와 캐럿 범위

    [https://velog.io/@slaslaya/npm-semver-틸트-범위와-캐럿-범위](https://velog.io/@slaslaya/npm-semver-%ED%8B%B8%ED%8A%B8-%EB%B2%94%EC%9C%84%EC%99%80-%EC%BA%90%EB%9F%BF-%EB%B2%94%EC%9C%84)

---

### 참고 자료

- 프론트엔드 개발환경의 이해: NPM

    [https://jeonghwan-kim.github.io/series/2019/12/09/frontend-dev-env-npm.html](https://jeonghwan-kim.github.io/series/2019/12/09/frontend-dev-env-npm.html)
