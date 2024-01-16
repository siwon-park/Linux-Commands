# 15_find 명령어

> 파일 시스템에서 파일 및 디렉토리를 찾기 위한 명령어

find 명령어에는 옵션과 표현식이 많이 존재한다. 그 이유는 리눅스 파일 시스템 구조에 있다.

리눅스 파일 시스템은 구조가 복잡하고, 많은 수의 파일과 디렉토리가 해당 파일 시스템에 저장되어 있다. 이 중에서는 비슷한 이름의 파일과 동일한 확장자를 가진 파일 등 종류가 다양한 파일들이 존재한다.

이에 복잡한 구조에서도 원하는 파일 및 디렉토리를 정확히 찾을 수 있도록 find 명령어에는 다양한 옵션과 표현식이 존재하는 것이다.

## 1. find

> 더 자세한 내용은 find --help를 통해 검색하자.

```bash
find [options] [path] [expression]
```

- 옵션(말 그대로 옵션이기 때문에 생략 가능)
  - `-P`: 심볼릭 링크 자체 정보 사용(심볼릭 링크를 따라가지 않음)
  - `-L`: 심볼릭 링크에 연결된 파일 정보 사용
  - `-H`: 심볼릭 링크를 따라가지 않으나, Command Line Argument를 처리할 땐 예외 적용.
  - `-D`: 디버그 메세지 출력
- 표현식
  - `-name`: 지정된 문자열 패턴에 해당하는 파일 검색
  - `-empty`: 빈 디렉토리 혹은 크기가 0인 파일 검색
  - `-delete`: 검색된 파일 또는 디렉토리 삭제
  - `-exec`: 검색된 파일에 대해 지정된 명령어 실행
  - `-path`: 지정된 문자열 패턴에 해당하는 경로에서 검색
  - `-print`: 검색 결과 출력. 검색 항목은 newline으로 구분(default)
  - `-print0`: 검색 결과 출력. 검색 항목은 null로 구분.
  - `-size`: 파일 크기를 사용하여 파일을 검색
  - `-type`: 지정된 파일 타입에 해당하는 파일 검색
  - `-mindepth`: 검색을 시작할 하위 디렉토리 최소 깊이 지정
  - `-maxdepth`: 검색을 시작할 하위 디렉토리 최대 깊이 지정
  - `-atime`: 파일 접근(access) 시각을 기준으로 파일 검색
  - `-ctime`: 파일의 내용 및 속성의 변경(change) 시간을 기준으로 파일 검색
  - `-mtime`: 파일의 데이터 수정(modify) 시간을 기준으로 파일 검색

<br>

### 1) 표현식과 연산자

find 명령어에서는 두 개 이상의 표현식 조합이 가능하며, 표현식에 연산자를 사용하여 조합을 만들어 낼 수 있다.

- 괄호; (expression) : expression에 대한 우선순위 지정
- `-not`; expression 결과에 대해 NOT 연산
  - !expression
  - -not expression
- `-a`, `-and`; expression 간 AND 연산
  - expression -a expression
  - expression -and expression
  - expression expression
- `-o`, `-or`; expression 간 OR 연산
  - expression -o expression
  - expression -or expression

기본적으로는 AND 연산이 적용된다.

<br>

### 2) 예시

#### (1) 대상 디렉토리에 있는 파일 표시

```bash
$ find DIR_1
DIR_1
DIR_1/FILE_1
DIR_1/FILE_2
DIR_1/FILE_3
```

#### (2) 다양한 패턴의 파일 검색

```bash
# 현재 디렉토리 아래의 모든 파일과 디렉토리를 검색해서 "FILE_1"이라는 파일을 찾음
$ find . -name "FILE_1"

# 루트 디렉토리에서 파일 검색
$ find / -name "FILE_2"

# 특정 문자열로 시작하는 파일 검색 -> 와일드 카드(*) 사용
$ find . -name "B*"

# 특정 문자열이 포함된 파일 검색
$ find . -name "*IS*"

# 특정 파일 확장자의 파일 검색
$ find . -name "*.java"

# 현재 디렉토리에서 크기가 0인 디렉토리나 파일 검색
$ find . -empty

# 특정 확장자를 가진 모든 파일 검색 후 삭제
$ find . -name "*.csv" -delete
```

#### (3) 타입 표현식 사용

`-type` 표현식을 사용하여, 특정 파일 종류를 지정하여 검색 가능

- `b`: block special
- `c`: character special
- `d`: directory
- `f`: regular file
- `l`: symbolic link
- `p`: FIFO
- `s`: socket

```bash
# 끝이 list라는 문자열로 끝나는 파일만 검색
$ find . -name "*list" -type f

# 끝이 list라는 문자열로 끝나는 디렉토리만 검색
$ find . -name "*list" -type d
```

#### (4) 파일 크기를 사용하여 검색

`-size` 표현식을 사용. 특정 알파벳으로 파일 크기의 단위 지정 가능

- `b`: block(블록)
- `c`: byte(바이트)
- `w`: 2byte
- `k`: kbyte(킬로바이트)
- `M`: mbyte(메가바이트)
- `G`: gbyte(기가바이트)

또한 +, -로 초과, 미만을 표현할 수 있다. 이를 활용해서 범위도 지정 가능

```bash
# 크기가 1024 바이트인 파일 검색
$ find . -size 1024c

# 크기가 1024 바이트 초과하는 파일 검색
$ find . -size +1024c

# 크기가 1024 바이트 미만인 파일 검색
$ find . -size -1024c

# 크기가 1024 초과, 2048 미만인 파일 검색
$ find . -size +1024c -size -2048c
```

#### (5) 검색된 파일의 라인 수 출력

```bash
# 확장자가 java인 파일의 라인 수 출력
$ find . -name "*.java" -exec wc -l {} \;
```

#### (6) 검색된 파일에서 특정 내용 검색

```bash
# .java 확장자 파일을 찾고 파일 안에 main이라는 문자열이 있는지 확인
$ find . -name "*.java" -exec grep -n "main" {} \;
```

#### (7) 하위 디렉토리는 검색하지 않기

```bash
# -maxdepth를 1로 설정하여 현재 디렉토리 내에서만 검색
# 단, maxdepth는 다른 표현식보다 앞에 작성해야 한다 
$ find / -maxdepth 1 -name "*.js"
```

#### (8) 파일 검색 후 복사

```bash
# .tar.gz로 끝나는 압축 파일을 찾은 다음 특정 디렉토리로 복사
$ find . -name "*.tar.gz" -exec cp {} /home/zow777/ \;
```

