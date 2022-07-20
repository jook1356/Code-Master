# 0720 Study



--------------------

-----



# 반복문, 조건문

## 조건 표현식 (Conditional Expression)

- **삼항 연산자(Ternary Operator)**로 부르기도 함

- 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용

- true인 경우 값 if 조건 else false인 경우 값

- ```python
  value = num if num >= 0 else -num
  여기서 순서는
  value = (num if num >= 0 else -num)
  이렇게 결과가 value 에 맨 마지막에 대입된다.
  고로 else, 즉 false 에 value가 생략된 이유이다.
  ```



#### 복수 조건문

- 다중 분기라고 한다.
- elif, else 를 사용하는 것

#### 중첩 조건문

- 조건문 속에 다시 조건문을 넣어서 쓸 수 있음.

#### While문

- While 문에 들어가는 것을 '초기식', 초기식에 대응되는 식이 '증감식' 이다.

#### 복합 연산자

- 변수 += 1  과 같은 형식의 연산자를 복합 연산자라고 한다.



## for문

- for문은 **시퀀스(string, tuple, list, range)**를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회 
- lterable
  - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등) - **시퀸스 유형과는 별개**
  - 순회형 함수(range, enumerate) 



## 딕셔너리

- keys() : key로 구성된 결과

- values() : value로 구성된 결과

- **items() : (key, value)의 튜플로 구성된 결과**
  
  - ```python
    #아래와 같이 활용이 가능하다.
    grades = {'john' : 80, 'eric' : 90}
    for student, grade in grades.items():
        print(student, grade)
    ```

- 딕셔너리[키] 는 키값이 없으면 에러

  - 딕셔너리.get(키) 로 키값이 없으면 None을 반환해주는 명령어 사용 가능

  

## Dictionary Comprehension

```python
 # 1 ~ 3의 세제곱 딕셔너리 만들기 
    
cubic_dict = {} 
for number in range(1, 4): 
	cubic_dict[number] = number ** 3
print(cubic-dict) 

 # {1: 1, 2: 8, 3: 27} 

```

를 아래와 같이 줄여서 쓸 수 있다.

```python
cubic_dict = {number: number ** 3 for number in range(1, 4)} 
print(cubic_dict) 
 # {1: 1, 2: 8, 3: 27}
    
 # Dictionary = {키: 밸류(혹은 밸류에 들어갈 식) for 변수 in 리스트나 변수}
```



## List Comprehension

```python
# 1~3의 세제곱 리스트 만들기 
cubic_list = [] 
for number in range(1, 4): 
	cubic_list.append(number ** 3) 
print(cubic-list) 

 # [1, 8, 27]
```

를 아래와 같이 줄여서 쓸 수 있다.

```python
cubic_list = [number ** 3 for number in range(1, 4)] 
 print(cubic_list) 
 # [1, 8, 27]

# 분리해서 보자면
cubic_list =
[number ** 3
 for number in range (1,4)]
```

-  {key: value for 변수 in iterable if 조건식} 이렇게 if 조건식도 넣을 수 있다.



## enumerate 순회

- enumerate()
  
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    
    - (index, value) 형태의 tuple로 구성된 열거 객체를 반환
    
    - ```python
      members = ['민수', '영희', '철수']
      
      for idx, number in enumerate(members):
          print(idx, number)
      
      # 출력
      
      0 민수
      1 영희
      2 철수
      ```



## 반복문 제어

- break
  - 해당하는 반복문을 즉각적으로 완전히 빠져나감 (반복문 하나만 빠져나감)
- continue
  - 반복문의 해당 회차만 생략하고 같은 반복문의 다음 회차로 넘어감
- pass
  - 아무 일 없음. 문법상 틀리지 않게 빈공간 채워넣는 명령어
- else
  - 반복문의 조건이 더이상 맞지 않아서 반복문이 끝날때 사용 가능
- return
  - break와 같이 반복문이 종료되며, 결과물을 반환



---------

---------------------



# 함수

## 함수의 정의

- 특정한 기능을 하는 코드의 조각(묶음) 
- 특정 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 간편히 사용 



#### Decomposition(분해)

- 함축된 함수를 구성하는 식으로 분해하는 것.



#### Abstraction

- 복잡한 내용을 모르더라도 사용할 수 있도록 재사용성과 가독성, 생산성0



#### 함수의 종류

- 내장함수 
  - 파이썬에 기본적으로 포함된 함수 
- 외장함수
  - import 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수 
- 사용자 정의 함수
  - 직접 사용자가 만드는 함수



## 함수의 결과값(Output)

#### 값에 따른 함수의 종류

- Void function
  - 명시적인 return 값이 없는 경우, None을 반환하고 종료
  - print와 같은 함수가 대표적인 예 (출력만 하고 return과 같이 반환은 하지 않음)
- Value returning function
  - 함수 실행 후, return문을 통해 값 반환
  - return을 하게 되면, 값 반환 후 함수가 바로 종료
  - return은 항상 하나의 값만을 반환
    - 이를 해결하기 위해 tuple을 사용한다. (ex : return x - y, x* y)
    - 혹은 리스트와 같은 컨테이너 활용

---------

#### REPL(Read-Eval-Print Loop)

- 주피터 노트북과 같은 환경을 REPL이라고 함
- REPL 환경에서는 프린트, 리턴 함수를 쓰지 않아도 결과를 보여주기 때문에 혼동을 주의할 것

---------

---------------------------



## 함수의 입력

## Parameter와 Argument



#### Parameter

- 함수를 정의할 때, 선언할 때, 함수 내부에서 사용되는 변수



#### Argument

- 함수를 호출 할 때, 넣어주는 값

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720134910515.png" alt="image-20220720134910515" style="zoom: 33%;" />

- 함수 호출 시 함수의 Parameter에 대입

- Argument는 소괄호 안에 할당 : funk_name(argument)

  - 필수 Argument : 반드시 전달되어야 하는 argument - 없으면 에러
  - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달

- Positional Arguments

  - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨
    - Argument가 (1, 2)이면 Parameter (x, y)에 순서대로 대입되어 (x = 1, y = 2)가 된다.

- Keyword Argument

  - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
  - Keyword Argument 다음에 Positional Argument를 활용할 수 없음
    - add(x = 2, y = 5)와 add(2, y = 5)는 가능, add(x = 2, 5)는 에러 발생!

- Default Arguments Values

  - 기본값을 지정하여 함수 호출 시 Argument 값을 설정하지 않도록 함

    - Parameter에서 def add(x, **y = 0**)의 y = 0처럼 미리 지정해두면 기본값이 되어 Argument에서 지정하지 않아도 됨
    - 정의된 것 보다 더 적은 개수의 Argument로 호출 가능




#### 가변 인자(*args)

- 여러 개의 Positional Argument를 하나의 필수 Parameter로 받아서 사용

- 몇개의 Argument를 받을지 모르는 함수를 정의할 때 유용

- Asterisk 혹은 언패킹 연산자 *
  - print와 같은 함수가 예시
    - print(*****objects,sep=' ' ~blabla~)
  - 시퀸스 언패킹 연산자라고도 불리며, 말 그대로 시퀸스를 풀어 헤치는 연산자
  - *를 활용하여 가변 인자를 만들 수 있음
  - 함수의 Parameter에 사용하면 Parameter는 튜플 형식이 되고, 일반적으로 쓰면 리스트가 된다.
  
- 패킹 / 언패킹
  - 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것.
    - 리스트를 한 변수에 넣는 것이 예
  - 언패킹 : 시퀸스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
    - 쉽게 말해 리스트 변수의 인덱스 하나하나를 여러 변수로 분할 대입
    - 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야 함
    - 하지만 언패킹시 왼쪽의 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음
    - <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720140533624.png" alt="image-20220720140533624" style="zoom:25%;" />
    - <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720140601530.png" alt="image-20220720140601530" style="zoom:25%;" />
    - 두개중 아래의 사진은 파이썬 고유 문법인데, Argument에 원하는 만큼의 개수로 대입 가능하다.
  
- 가변 인자 예시

  - <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720141334025.png" alt="image-20220720141334025" style="zoom:25%;" />

  - *Parameter에는 하나도 넣지 않아도 상관은 없다

    

#### 가변 키워드 인자(**kwargs)

- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
- **kwargs는 딕셔너리로 묶여 처리되며, parameter에 ****를 붙여 표현
- <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720141608883.png" alt="image-20220720141608883" style="zoom:25%;" />
- <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720141812498.png" alt="image-20220720141812498" style="zoom:25%;" />
- 위 사진에서 주의해야 할 점은 family Argument에서 father, mother 등등은 문자열이 아닌 변수처럼 적어야 한다!
-  if pets: 에서 pets에 내용물이 없으면 0으로 되기 때문에 if false:가 되어서 조건문 실행을 하지 않게 되는 원리이다.



--------------------

- 가변 인자(*args)와 가변 키워드 인자(**args)를 동시에 사용할 수 있는가?
  - 함께 사용 가능하다.
  - <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720143135072.png" alt="image-20220720143135072" style="zoom:25%;" />

-------------------

---------



## Scope

#### Python의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든, 누구나 참조, 사용할 수 있는 공간
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720143617073.png" alt="image-20220720143617073" style="zoom: 33%;" />



#### 변수 수명주기(lifecycle)

- 변수는 각자의 수명주기(lifecycle)가 존재

  - built-in scope

    - 파이썬이 실행된 이후부터 영원히 유지
    - len()과 같은 함수가 예시

  - global scope

    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

  - local scope

    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    - <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720144126980.png" alt="image-20220720144126980" style="zoom:25%;" />

    

#### 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
  - Local scope : 지역 범위 (현재 작업 중인 범위)
  - Enclosed scope : 지역 범위 한 단계 위 범위
  - Global scope : 최상단에 위치한 범위
  - Built-in scope : 모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것)
    - ex) print()
  - 가장 낮은 서열의 공간에서부터 순서대로 변수를 찾으러 가는 여정
    - 변수를 찾으면 더 높은 서열의 공간은 탐색하지 않음
    - 이것이 내장 함수의 이름을 변수로 활용하게 되면 내장 함수의 기능을 잃어버리는 것과 같은 원리
- **함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음**
- <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720145319251.png" alt="image-20220720145319251" style="zoom: 33%;" />



<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720150141072.png" alt="image-20220720150141072" style="zoom:25%;" />



#### global

- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄
  - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
  - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함!



#### nonlocal

- global을 제외하고 가장 가까운 (둘러싸고 있는) scope의 변수를 연결하도록 함
  - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
  - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함!
- global과는 달리 이미 존재하는 이름과의 연결만 가능함
- 한단계 상위 서열의 scope와 변수를 공유하게 됨
  - ex) 중첩 for문에서 안쪽 for문의 변수를 바깥쪽 for문에서 쓸 수 있게 됨
- 중첩 논로컬= 전부 연결됨
- 글로벌 바로 아래에 있는 함수에선 논로컬 사용 못함



#### 함수의 범위 주의

- 함수에서 선언된 변수는 local scope, 함수 종료 시 사라짐
- global, nonlocal 남용 금지
- 왠만하면 argument로 리턴하여 리턴 값을 사용하는 것을 추천



------------

------------

# 함수 응용 (내장 함수)



#### map

- map(function,iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 map object로 반환
- <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720151550178.png" alt="image-20220720151550178" style="zoom:25%;" />

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720151713265.png" alt="image-20220720151713265" style="zoom:25%;" />



#### filter

![image-20220720151800243](C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720151800243.png)

#### zip

- 여러개의 리스트를 세로로 묶어줌
  - 알고리즘 중에 빙고 문제를 풀 때 필요한것!
- 1차원의 리스트들을 2차원으로 묶어주는 것?

![image-20220720151856390](C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720151856390.png)



#### lambda

- 익명 함수라고도 불림
- return문을 가질 수 없음
- 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
- def를 사용할 수 없는 곳에서도 사용 가능
- <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720153147770.png" alt="image-20220720153147770" style="zoom:25%;" />
- 구조는 아래와 같음
  - 함수명 = lambda 변수, 변수2... : 식



#### 재귀 함수(recursive function)

- 자기 자신을 호출하는 함수
- 무한한 호출이 목표가 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
  - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음(예 - 점화식)
  - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
- 예시
  - Factorial
    - <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720153655246.png" alt="image-20220720153655246" style="zoom:25%;" />
    - <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720153803277.png" alt="image-20220720153803277" style="zoom:25%;" />
    - 함수를 한번 쓰면 같은 함수가 여러번 반복된다.
- 재귀 함수 주의 사항
  - 재귀 함수는 base case에 도달할 때까지 함수를 호출함
  - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
  - 파이썬에서는 최대 재구 깊이(maximum recursion depth)가 1000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion error 발생
- 이론적으로는 **재귀 <-> 반복문 으로 서로 변환이 가능**하다!
- 반복문을 재귀 함수로 짜보는 것 연습



-------

-----------

# 모듈



## 모듈과 패키지

- 다양한 기능을 하나의 파일로 묶은 것을 모듈이라 함
- 여러개의 모듈을 하나의 폴더로 묶은 것을 패키지라 함
- 다양한 패키지를 하나의 묶음으로 묶은 것을 라이브러리라 함
- 모듈 -> 패키지 -> 라이브러리



- 모듈

  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것

- 패키지

  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에는 또 다른 서브 패키지를 포함

  <img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720154919170.png" alt="image-20220720154919170" style="zoom:25%;" />



-----

------------------

# 알고만 있으면 될 것들!

#### 라이브러리와 프레임워크의 차이?

- 버즈워드 - 정의가 확실하지 않음
- 라이브러리는 도구와 같은 느낌? (ex: 삽)
  - 원한다면 삽으로 밥을 먹을 수 있는 것처럼 주도권이 나에게 있음
- 프레임워크는 기계? (ex: 포크레인)
  - 기계의 조작법이 따로 있어서 마음대로 하지는 못함

#### pip (파이썬 패키지 관리자)

- 라이브러리를 관리하는 것

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720155217121.png" alt="image-20220720155217121" style="zoom:25%;" />

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720154919170.png" alt="image-20220720154919170" style="zoom:25%;" />

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720155346772.png" alt="image-20220720155346772" style="zoom:25%;" />

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720155403558.png" alt="image-20220720155403558" style="zoom:25%;" />

<img src="C:\Users\Dongju\AppData\Roaming\Typora\typora-user-images\image-20220720155537853.png" alt="image-20220720155537853" style="zoom:25%;" />



#### 가상환경

- 패키지의 활용 공간
- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
  - 과거 외주 프로젝트 - django 버전 2.x
  - 신규 회사 프로젝트 - django 버전 3.x
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음
- 쉽게 말해 여러가지 버전의 패키지를 한 PC에 쓸수 있게 하는 가상 머신
- Python 3.5 부터 모듈로 지원하고 있음
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경이(패키지 집합 폴더 등) 있고 실행 환경(ex: bash)에서 가상환경을 활성화 시켜 해당 폴더에 있는 패키지를 관리/사용함
- 가상환경 명령어
  - venv



-----

-----



# 사용자 모듈과 패키지



## 패키지

#### 패키지 만들기

- 같은 폴더에 __init\_\_.py 가 필요하다



#### 패키지 불러오기

- 불러오는 명령어
  - from 폴더명(패키지명) import 파일명(모듈명)
- 쓰는 명령어
  - 파일명(모듈명).함수(?)

