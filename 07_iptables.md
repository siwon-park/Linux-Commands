# 00_iptables

리눅스의 패킷 필터링(Packet Filtering) 도구로서 방화벽 구성이나 NAT(Network Address Translation)에 사용한다.

특정 조건을 가지고 있는 패킷에 대해 허용(ACCEPT)과 차단(DROP) 등을 설정할 수 있으며, 특정 조건 등을 통해 다양한 방식의 패킷 필터링과 처리 방식을 지원한다.

※ 만약 모든 입출력 패킷에 대해 거부(DENY)하는 설정이 테이블 상에서 먼저 등록되면 그 이후에 포트를 허락해주는 설정을 해도 효과는 없음.

설정 파일 위치: `/etc/sysconfig/iptables`

- vi, vim 명령어로도 테이블 정책을 설정할 수 있음

## 1. 제어 명령어

### 1) 설치

```bash
yum install -y iptables-services
```

### 2) 실행

```bash
# 실행
systemctl start iptables
service iptables start

# 서버 재부팅 시에도 자동 실행
systemctl enable iptables
```

### 3) 중지

```bash
systemctl stop iptables
service iptables stop
```

### 4) 재시작

```bash
systemctl restart iptables
service iptables restart
```

### 5) 상태 확인

```bash
systemctl status iptables
service iptables status
```

### 6) 정책 저장

정책을 설정하고 나면 반드시 저장해줘야 한다.

```bash
service iptables save
```

## 2. iptables 기본 명령어

```bash
iptables [-t table] [action] [chain] [matches] [-j target]
```

### 1) 테이블(table)

적용할 테이블을 선택하는 옵션
filter(`-f`), nat(`-n`), mangel(`-m`), raw(`-r`)가 있으며, 생략할 경우 자동적으로 filter가 적용됨

### 2) 액션(action)

조치할 행동에 대해 정의하는 옵션

- `-A`: 새로운 정책을 추가 (APPEND)
  - `--append`
- `-I`: 위치를 지정하여 정책을 삽 (INSERT)
  - `--insert`
- `-D`: 정책을 삭제함 (DELETE)
  - `--delete`
- `-R`: 정책을 교체함 (REPLACE)
  - `--replace`
- `-F`: 모든 정책을 삭제함 (FLUSH)
  - `--flush`
- `-P`: 기본 정책을 설정함 (POLICY)
  - `--policy`
- `-L`: 정책 목록을 확인함 (LIST)
  - `--list`

### 3) 체인(chain)

패킷의 방향성에 대해 설정함

- `-INPUT`: 호스트로 들어오는 모든 패킷
- `-OUTPUT`: 호스트에서 나가는 모든 패킷
- `-FORWARD`: 라우터로 사용되는 모슨 컴퓨터를 통과하는 패킷

### 4) 매치(matches)

- `-s`: 출발지 매칭. 도메인, IP 주소, 넷마스크 값을 이용하여 패키지 송신지를 제어 (`--source`, `--src`)
- `-d`: 목적지 매칭. 도메인, IP 주소, 넷마스크 값을 이용하여 패키지 수신지를 제어 (`--destination`, `--dst`)
- `-p`: 어떤 프로토콜(tcp, udp, icmp 등)과 매칭할지 설정
- `-i`: 입력 인터페이스와 매칭 (`--in-interface`)
- `-o`: 출력 인터페이스와 매칭 (`--out-interface`)
- `-j`: 매치되는 패킷을 방화벽을 지난 다음에 어떻게 처리할지 지정(`--jump`, `타겟(target)`과 연관)
- `-f`: 분절된 패킷과 매칭 (`--fragment`)
- `--sport`: 송신지 포트와 매치
- `--dport`: 수신지 포트와 매치

### 5) 타겟(target)

패킷이 규칙과 일치할 때 취하는 동작을 지정함.

- `ACCEPT`: 해당 패킷을 허용함
- `DROP`: 해당 패킷을 버림 (패킷이 전송된 적 없던 것으로 간주)
- `REJECT`: 해당 패킷을 버림 (응답을 반환)
- `LOG`: 패킷을 syslog에 기록함
- `RETURN`: 호출 체인 내에서 패킷 처리를 계속함

## 3. 사용

### 1) 예시

- iptable 정책 상태 확인

```bash
iptables -nL
```

- SMTP 25번 포트 허용

```bash
# 25번 수신 포트에 대해 tcp 연결로 들어오는 패킷을 허용함
iptables -A INPUT -p tcp --dport 25 -j ACCEPT
```

- 1번 리스트에 127.0.0.1 루프백 허용

```bash
iptables -I INPUT 1 -s 127.0.0.1 -j ACCEPT
```

- 8161번 포트를 차단

```bash
# 8161번 포트로 tcp 연결로 들어오는 패킷을 차단함
iptables -A INPUT -p tcp --dport 8161 -j DROP
```