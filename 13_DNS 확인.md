# 13_DNS 확인

DNS, IP 정보 등 도메인과 관련된 내용을 확인할 수 있는 명령어들

※ 도메인은 `OOO.com`, `OOO.co.kr`과 같은 형태이다. 일반적으로 앞에 많이 붙는 `www`는 도메인이 아님을 유의.

<br>

## 1. nslookup

> NameServer lookup

```bash
nslookup [도메인]

# 예시
nslookup naver.com
```

<br>

## 2. dig

> dig

```bash
dig [옵션] [도메인]

# 예시
dig a naver.com
dig ns naver.com
```

- 옵션
  - `a`: A레코드 확인
  - `ns`: 도메인 네임 서버 확인
  - `mx`: MX레코드 확인