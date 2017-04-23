## Concept
### 기본 규칙
- 이 parser rule은 오직 lxml(xml)을 파싱하는 것만 목적으로 한다.
- Json Obj 하나는 하나의 Task로 이루어 진다.
- Json Array 는 Task Array로서 Task의 실행 순서를 의미한다. 항상 먼저 정의된 Task가 먼저 실행된다.
- 단, 특별히 용도가 명시된 Json Obj와 Json Arr에 한해 다를 목적으로 사용될 수 있다.
- 하나의 Task는 항상 1개의 결과를 출력한다. 그 결과는 list, bool, dict, None, Tag등 python object로 나타낼 수 있는 모든 것이다.
- Task Array의 제일 마지막 Task의 return값이 Task Array의 return값이 된다.
- Result는 거대한 Dict이며, 1크롤링 = 1Result 이다.

## Command
### common command
* **`$use`**
	* Task에 input을 정의한다. 기본값은 이전 task에서 리턴된 값이다.
	* `$$<result_name>` 을 이용하여 이전에 저장한 값을 불러 올 수 있다.
	* 최고 우선순위를 가진다.
* **`$use_list`**
	* 기본적으로 $use와 같다. 하지만, 항상 input은 list이다. 
	* input이 list가 아니라면, list로 감싸서 사용한다 (* 예 `True` => `[True]` )
	*  최고 우선순위를 가진다.
* **`$as`**
	* return값을 해당 이름을 key로 사용하여 Result에 저장한다. 
	* 단, $ 로 시작하는 이름은 reserved 이므로 사용할 수 없다.
	* 최하우선순위를 가진다.
* **`$command`** :  축약된 Task 에서 사용되는 커멘드이다. 우선순위에 영향을 받지 않는다.

### Beautiful Soup task command
#### find command
아래의 커맨드 들은 beautiful soup의 해당 메서드를 실행시키는 command이다.
* **`$find`**
* **`$find_all`**
* **`$find_parent`**
* **`$find_parents`**
* **`$find_next_siblings`**
* **`$find_next_sibling`**
* **`$find_previous_siblings`**
* **`$find_previous_sibling`**
* **`$find_all_next`**
* **`$find_next`**
* **`$find_all_preivous`**
* **`$find_previous`**
* **`$select`** : option는 String
* **`$select_one`** : option는 String

#### `find_xxxx`에서 사용되는 attribute

find_xxxx는 암묵적 literail_rec dict option으로 받는다.
option은 아래와 같은 key를 포함해야한다.
해당 key에 대한 value들은 각각 tag attribue recusive에 해당한다.

* **`tag`**
* **`attr`**
* **`rec`**

### Collection Command
list와 관련된 커멘드이다.

* **`$filter`**
	* 일반적은 Task/Task Array를 입력받지만, Task는 list input의 각각의 element에 대해서 element하나씩 input을 받아 T/F를 리턴한다.
	* 여기서 True를 리턴받은 element만 재취합 하여 list로 만든다.
* **`$filter_not`** : 함수에서 False를 리턴한 것만 재취합 한다.
* **`$get`**
	* input이 number(int)일경우 해당 index의 element를 리턴한다.
	* int list 라면 해당 element들만 선택하여 list로 만들어 리턴한다.
	* dict라면, `from`,`until`,`step`을 key로하여 값을 입력받아, 그것으로 list[f:u:s] 연산을 한다.
	* input이 Task라면 filter와 동일한 input을 받아 True를 리턴번는 첫 element만 리턴한다.
		* 참고 : ```"$or":{"$command": "filter", ~~~~}```와 동일한 결과를 리턴한다.
* **`$map`** : list 의 element마다 한번식 수행후 결과값들을 취합하여 list로 만든다.
* **`$flat_map`** : list의 elemnt마다 한번씩 수행하여 결과값(list)의 모든 element들을 모아 하나의 list로 만든다
* **`$union`**
	* 입력은 암묵적 literal list이다.
	* Array안에 있는 모든 Task/Value는 리스트(단일 value로 리턴하면 해당 value만 포함하고 있는 list로 변환된다.)의 value를 합쳐 하나의 리스트로 만든다
	* `$union`은 `$flat_map`과 동일한 동작을 하지만, input방법에 차이가 있다.
	* 	예)
	 
		```json
		{"$use": ["$literal_rec",[1,2,3],[4,5,6]], "$flat_map": {"$use": "$self"}}
		```
		 as result :  value `[1, 2, 3, 4, 5, 6]`
			
		same with:
		
		```json
		["$union",["$literal",1,2,3], ["$literal", 4, 5, 6]] 
		```
		as result : value `[1, 2, 3, 4, 5, 6]`
	
* **`$drop`**
	* int 혹은 int list를 입력받는다 여기서 int array는 암묵적으로 literal이다.
	* int list는 drop을 동시에 여러개 하는것과 같은 결과를 보인다.
		* 주의) `[1,2,3,4]`에서 `1,2,3` 을 빼고 싶을땐 `"$drop":[0,0,0]` 이 아니라 `"$drop":[0,1,2]`이다.

### boolean task command

* **`$or`**
    * 입력은 암묵적 list이다.
    * list안에 있는 모든 Task/Value에 대해서 or를 순차적으로 비교한다.
	* short circuit으로 처리된다. 순차적으로 비교하다 True인 값이 있으면 그 즉시 해당 값을 리턴한다.
	* Array에 있는 모든 값이 False라면 False를 리턴한다.

* **`$and`**
	* 입력은 암묵적 list이다.
    * list안에 있는 모든 Task/Value에 대해서 and를 순차적으로 비교한다.
	* short circuit으로 처리된다. 순차적으로 비교하다 False 값이 있으면 그 즉시 False를 리턴한다.
	* Array에 있는 모든 값이 True라면, 값들의 리스트를 리턴한다.
    
* 예)
	* `["$or", False, None, "Some_Value", None]` => `"Some_Value"`
	* `["$or", False, None, False, None]` => `False`
	* `["$and", "Some_Value1", "Some_Value2", "Some_Value3", "Some_Value4"]` => `["Some_Value1", "Some_Value2", "Some_Value3", "Some_Value4"]`
	* `["$and", "Some_Value1", "Some_Value2", "Some_Value3", None]` => `False`



### operator command
다음음 python에서 사용되는 operator를 그대로 표현한것이다.
결과값을 `input` <operator> `option` 으로 계산된다.
* **`$+`**
* **`$/`**
* **`$-`**
* **`$*`**
* **`$%`**
* **`$is`**
* **`$in`**
* **`$is_not`**
* **`$==`**
* **`$!=`**
* **`$>`**
* **`$>=`**
* **`$<`**
* **`$<=`**

### string command
* **`$concat`**
	* 암묵적 list를 option으로 받는다.
	* 입력받은 string list를 합쳐 하나의 스트링으로 만든다.
	* input을 포함해서 합치고 싶다면 반드시 $self를 사용하라.
* **`$mk_string`**
	* input은 String list 이고, Option은 String이다.
	* String list를 합치는데, 이때 Option으로 받은 String 을 구분자로 넣는다.
* **`$replace`**
	* input은 String이고 Option은 replace Option으로, 암묵적인 dict이다.
	* option에 사용되는 key는 "$find", "$find_regex", "$to" find에는 찾을 string, to에는 바꿀 string, 을 넣으면 되고, find 대신에 find_regex를 넣어 변경할 수 있다.
* **`$replace_once`** : replace 는 다 바꾸는거 이건 최초 매칭만 바꾸는거
* **`$format`**
	* format은 String을 generagte할 때 새용한다.
	* input은 $self를 이용해 사용 할 수 있다.
	* Option에는 $format 과 $args 가 있는데 format은 String으로, printf의 그 포맷으로 맞추면 된다. args는 암묵적 list인데, value로서 list를 넘겨도 된다.
