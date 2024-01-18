# 16_curl 명령어

> curl; client URL

클라이언트에서 프로토콜을 통해 url로 서버와 데이터를 송수신하는 명령어

Linux, MacOS, Window 등 다양한 환경에서 HTTP, HTTPS, SMTP 등 다양한 프로토콜을 지원하여 통신환경에서 자주 쓰인다.

<br>

## 1. 사용법

자세한 사용법 및 내용은 `cur --help` 또는 `curl --manual`을 통해 확인 가능하다.

```bash
curl [options] [url]

# curl 버전 확인
curl -V
```

- 옵션
  - `-k`: https url 접속 시 SSL 인증서 검사 없이 연결 (`--insecure`)
  - `-i`: http 응답 헤더를 표시(`--head`)
  - `-d`: POST 요청을 통해 JSON 타입으로 Request Body에 데이터를 담을 때 사용 (`--data`)
  - `-o`: [파일명]과 함께 사용하여 출력 결과를 해당 파일명으로 저장(`--output`)
  - `-O`: 파일 저장 시 remote의 파일명으로 저장(`--remote-name`)
    - 단, remote에 파일이 없다면 404
  - `-s`: 진행 내역이나 메세지 등을 출력하지 않음(`--silent`)
  - `-X`: 요청(Request)에 사용할 메서드(GET, POST, PUT, DELTE 등)을 지정(`--request`)
  - `-v`: 동작하는 과정을 출력(`--verbose`)
  - `-A`: 특정 브라우저인 것처럼 동작(`--user-agent`)
  - `-H`: 요청 헤더 설정(`--header`)
  - `-L`: 서버에서 온 응답을 redirect url을 따라감(`--location`)
    - `--max-redirs`로 횟수 지정 가능
  - `-D`: 파일에 응답 헤더를 기록함(`--dump-header`)
  - `-u`: 사용자 아이디 및 비밀번호 입력(`--user`)
  - `-f`: 오류 발생 시 출력 없이 실패(`--fail`)
  - `-T`: 로컬 파일을 서버로 전송(`--upload-file`)
  - `-C`: 중지된 다운로드를 재시작(`--continue-at`)
    - `-C -`는 자동적으로 어디서부터 전송을 다시 시작할 것인지 지정 가능
  - `-J`: 응답 헤더에 있는 파일 이름으로 파일 저장(`--remote-header-name`)
  - `-I`: 응답 헤더만 출력(`--head`)

<br>

### 1) 사용 예시

```bash
# 지정한 파일명으로 저장(vue-v2.6.10.js로 저장)
curl -o vue-v2.6.10.js https://cdn.jsdelivr.net/npm/vue/dist/vue.js

# 원래 서버에 존재하는 파일명으로 저장
curl -O https://cdn.jsdelivr.net/npm/vue/dist/vue.js

# 중지된 다운로드를 재시작
curl -C - -O http://releases.ubuntu.com/18.04/ubuntu-18.04-live-server-amd64.iso
```

