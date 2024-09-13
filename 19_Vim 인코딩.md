# 19_Vim 인코딩

> vi, vim으로 파일을 열었을 때 한글이 깨져있다면?

### 1) 인코딩 방식 변경

```bash
:set enc=[인코딩 방식]

# utf-8로 인코딩 변경
:set enc=utf-8

# euc-kr로 인코딩 변경
:set enc=euc-kr
```

<br>

### 2) 인코딩 방식 재로딩

인코딩 방식만 변경했다고 해서 바로 원하는 타입으로 확인이 불가능한 경우도 있다.

```bash
:e ++enc=[인코딩 방식]

# utf-8로 인코딩 변경
:e ++enc=utf-8

# euc-kr로 인코딩 변경
:e ++enc=euc-kr
```

