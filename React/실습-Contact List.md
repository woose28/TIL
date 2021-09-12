# 실습-Contact List
### 실습 개요

전화번호부를 만드는 실습이다.

이번 실습은 인프런 'React & Express 를 이용한 웹 어플리케이션 개발하기**'** 강의를 수강한 후 강의 내의 실습 내용을 변형을 하여 진행하였다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d254c74a-2106-4290-99d9-80c2eaed2086/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d254c74a-2106-4290-99d9-80c2eaed2086/Untitled.png)

<실습 UI>

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/383d7079-8cfa-45ab-8007-4b479b0f1743/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/383d7079-8cfa-45ab-8007-4b479b0f1743/Untitled.png)

<컴포넌트 구조>

주요 기능은 번호  조회,  추가, 수정, 삭제 네 가지로 나뉜다.

### State

```jsx
//Contact.js

constructor(props){
    super(props);
    this.state = {
			//조회 중인 번호 중 선택한 번호의 인덱스를 저장하는 state
			//아무것도 선택되지 않았을 때는 기본값이 -1이다.
      isSelectedKey:-1,

			//번호 검색 입력창에 입력된 값을 저장하는 state
      keyword:"",

			//저장된 전화번호 원본 데이터
      contactData:[
        {name:"woose", phone:"010-0000-1234"},
        {name:"mike", phone:"010-0000-4568"},
        {name:"henry", phone:"010-0000-1598"},
        {name:"tree", phone:"010-0000-7432"}
      ],
			//검색된 전화번호를 저장하는 state
			//keyword와 일치하는 번호 목록을 렌더링 할때 사용된다.
      searchedData:[
        {name:"woose", phone:"010-0000-1234"},
        {name:"mike", phone:"010-0000-4568"},
        {name:"henry", phone:"010-0000-1598"},
        {name:"tree", phone:"010-0000-7432"}
      ],
    };
	....
}
```

### 조회 기능

입력창에 입력된 값과 일치하는 번호를 보여주는 기능이다.

아무것도 입력하지 않으면 현재 저장된 모든 목록을 보여준다.

```jsx
//Contact.js
render(){
		//검색된 목록을 렌더링하는 함수
		//검색된 번호 데이터가 전달되면 map 함수를 이용하여 원소를 하나씩 <ComtactItem> 컴포넌트를 생성에 이용한다.
    const show_list = (data) => {
      data.sort();

      return data.map((contact, i) => {
        return (<ContactItem contact={contact} key={i} onClick={()=>this.handleSelected(i)}/>);
      });
    };

    return(
      <div>
        <h2>Contact List</h2>
				//검색을 할 수 있는 입력창
				//입력된 값은 keyword state에 저장된다.
        <input
          name="keyword"
          placeholder="Search..."
          value={this.state.keyword}
          onChange={this.handleChange}
          />
        {show_list(this.state.searchedData)}
        <ContactDetail selectedKey={this.state.isSelectedKey} contact={this.state.searchedData[this.state.isSelectedKey]} onRemove={this.handleRemoveButton} onEdit={this.handleEditButton}/>
        <ContactCreate onClick={this.handleCreateButton}/>
      </div>
    );
  }
```

```jsx
//Contact.js

//번호 목록의 요소를 렌더링하는 컴포넌트로 클릭 시 Contact 컴포넌트의 handleSelected 가 호출된다.
class ContactItem extends React.Component{
  render(){
    return(
      <div onClick={this.props.onClick}>{this.props.contact.name}</div>
    );
  }
}
```

```jsx
//Contact.js

//ContactItem이 클릭되면 실행되는 메서드
//목록에서 선택된 아이템 인덱스를 isSelectedKey state에 저장한다.
handleSelected(key){
    this.setState({
      isSelectedKey:key
    });

    console.log(key);
  }
```

```jsx
//Contact.js
handleChange(e){
    let searching_name = e.target.value;

		//ContactData 중 입력된 키워드와 일치하는 요소를 searched_list에 저장한다.
		let searched_list = this.state.contactData.filter((value)=>{
      let keyword_length = searching_name.length;
      return value.name.toLowerCase().slice(0, keyword_length) == searching_name;
    })


		//searchedList를 searchedData state에 저장한다.
		//searchedData는 show_list함수의 매개변수로 전달된다.
    this.setState({
      keyword:e.target.value,
      searchedData:searched_list,
      isSelectedKey:-1
    });

  }
```

### 추가 기능

입력 창을 통해 데이터를 입력하고 버튼을 누르면 데이터가 추가된다.

```jsx
//ContactCreate.js

render(){
    return(<div>
        <h2>Contact Create</h2>
				//이름을 입력받는 입력창
				//입력 받은 이름을 name state에 저장
        <input
          name="name"
          placeholder="name..."
          value={this.state.name}
          onChange={this.handleChange}
          ref = {(ref) => {this.input_name = ref;}}
          />

				//번호를 입력받는 입력창
				//입력 받은 번호를 phone state에 저장
        <input
          name="phone"
          placeholder="phone"
          value={this.state.phone}
          onChange={this.handleChange}
          onKeyPress={this.handleKeyPress}/>
          <p>
				//버튼이 눌리면 name과 phone state 한 쌍이 번호 목록에 추가된다.
            <button onClick={this.handleClick}>Create</button>
          </p>
      </div>);
  }
```

```jsx
//ContactCraete
handleClick(){
    const new_contacdt = {
      name : this.state.name,
      phone : this.state.phone
    };

		//Contact Component의 handleCreateButton가 실행된다.
    this.props.onClick(new_contact);

		//번호가 저장이 되었다면 입력창을 공백으로 초기화 한다.
    this.setState({
      name : "",
      phone: ""
    });
```

```jsx
//Contact.js
handleCreateButton(newContact){
		//새로운 전화번호 정보를 업데이트 하는 함수
    if(this.state.keyword == ""){
      this.setState({
        contactData : update(this.state.contactData,{
          $push:[newContact]
        }),
        searchedData : update(this.state.contactData,{
          $push:[newContact]
        })
      });
    }
    else{
      this.setState({
        contactData : update(this.state.contactData,{
          $push:[newContact]
        })
      });
    }
  }
```

### 수정 & 삭제 기능

```jsx
//ContactDetails.js
constructor(props){
    super(props);
		//isEditMode는 수정 모드의 on/off toggle 기능을 구현할때 사용된다.
    this.state={
      name : "",
      phone : "",
      isEditMode : false,
    };
    this.handleChange = this.handleChange.bind(this);
    this.editToggle = this.editToggle.bind(this);
    this.handleKeyPress = this.handleKeyPress.bind(this);
  }
	...
//isEditMode == true 일때 입력 창에 있는 정보를 이용하여 선택된 번호 정보를 업데이트 한다.
//onEdit props는 Contact.js의 handleEditButton 함수이다.
editToggle(){
    if(this.props.selectedKey == -1){
      return;
    }
    if(this.state.isEditMode){
      const editItem = {
        name: this.state.name,
        phone: this.state.phone,
        prev_name: this.input_name.placeholder,
        prev_phone: this.input_phone.placeholder
      };

      this.props.onEdit(editItem);
      this.setState({
        isEditMode : !this.state.isEditMode,
        name : "",
        phone : ""
      });
    }
    else{
      this.setState({
        isEditMode : !this.state.isEditMode
      });
    }
  }
	...
render(){
    const details_info = (<div>
      <p>{this.props.contact.name}</p>
      <p>{this.props.contact.phone}</p>
      </div>);

    const edit_info = (<div>
      <p><input name="name" placeholder={this.props.contact.name} value={this.state.name} onChange={this.handleChange} ref={(ref) => {this.input_name = ref}}/></p>
      <p><input name="phone" placeholder={this.props.contact.phone} value={this.state.phone} onChange={this.handleChange} ref={(ref) => {this.input_phone = ref}} onKeyPress={this.handleKeyPress}/></p>
    </div>);

		//toggle 모드가 on이면 edit_info를 off면 details_info를 보여준다.
    const view = this.state.isEditMode ? edit_info : details_info;
    const blank = (<div>Not Selected</div>);

		//ContactDetails component를 생성할 때 isSelectedKey를 props로 전달하며
		//props가 -1이면 blank에 정의된 태그를 아니면 view에 정의된 태그를 보여준다.
    return(
      <div>
        <h2>Contact Detail</h2>
        {this.props.selectedKey==-1? blank: view}
        <button onClick={this.editToggle}>{this.state.isEditMode ? "Ok" : "Edit"}</button>
        <button onClick={this.props.onRemove}>Remove</button>
      </div>
    );
  }
```

```jsx
//ContactDetails.js에서 전달된 정보를 이용하여 전화번호를 업데이트 하는 부분으로
//전화 번호 검색창에 keywrod 입력 여부에 따라 수정 방법을 다르게 진행한다.
handleEditButton(editItem){
    if(this.state.keyword == ""){
      this.setState({
        contactData:update(this.state.contactData,{[this.state.isSelectedKey]:{name:{$set:editItem.name},phone:{$set:editItem.phone}}}),
        searchedData:update(this.state.searchedData,{[this.state.isSelectedKey]:{name:{$set:editItem.name},phone:{$set:editItem.phone}}}),
        isSelectedKey:-1
      })
    }
    else{
      let idx = -1;
      const origin_data = this.state.contactData ;
      for(let i = 0; i < origin_data.length; i++){
        if(origin_data[i].name == editItem.prev_name && origin_data[i].phone == editItem.prev_phone){
          idx = i;
          break;
        }
      }

      this.setState({
          contactData: update(this.state.contactData, {[idx]:{name:{$set:editItem.name}, phone:{$set:editItem.phone}}}),
          searchedData:update(this.state.searchedData,{[this.state.isSelectedKey]:{name:{$set:editItem.name},phone:{$set:editItem.phone}}}),
          isSelectedKey:-1
      });
    }
  }

//ContatDetails.js에서 삭제 버튼을 누르면 실행되는 함수이다.
//handleEditButton의 처리 방식 처럼 keword 입력 여부에 따라 삭제 방법이 나뉘어서 진행된다.
handleRemoveButton(){
    if(this.state.isSelectedKey == -1){
      return;
    }

    else if(this.state.keyword == ""){
      this.setState({
        contactData : update(this.state.contactData, {
          $splice:[[this.state.isSelectedKey,1]]
        }),
        searchedData : update(this.state.searchedData, { $splice:[[this.state.isSelectedKey, 1]]}),
        isSelectedKey : -1
      })
    }
    else{
      const remove_item = this.state.searchedData[this.state.isSelectedKey];

      this.setState({
        contactData : this.state.contactData.filter((item) => {
          return (item.name != remove_item.name && item.phone != remove_item.phone)
        }),
        searchedData : update(this.state.searchedData, { $splice:[[this.state.selectedKey, 1]]}),
        isSelectedKey : -1
      })
    }
  }
```

### 추가 기능

위의 4가지 기본 기능 이외에 추가적으로 새로고침을 해도 데이터가 웹 브라우저에 저장되는 기능이 구현되어 있다.

```jsx
//component가 Mount 될 때 로컬 저장소에 미리 저장해 놓은 정보가 있다면 불러온다.
componentWillMount(){
    const contactData = localStorage.contactData;
    if(contactData){
      this.setState({
        contactData:JSON.parse(contactData),
        searchedData : JSON.parse(contactData)
      });
    }
  }

//contactData state에 변화가 있을 때 변화된 정보를 로컬 저장소에 저장을 한다.
  componentDidUpdate(prevProps, prevState){
    if(this.state.contactData != prevState.contactData){
      localStorage.contactData = JSON.stringify(this.state.contactData);
    }
  }
```

---

### 참고자료

- **React & Express 를 이용한 웹 어플리케이션 개발하기**

    [https://www.inflearn.com/course/react-강좌-velopert/dashboard](https://www.inflearn.com/course/react-%EA%B0%95%EC%A2%8C-velopert/dashboard)
