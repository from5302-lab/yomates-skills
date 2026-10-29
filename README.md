# yomates-skills

<!-- yomates-install:readme -->
> **먼저 요메이트(Yomates)가 필요해요.** 이 스킬은 요메이트 앱 안에서 돌아가요. 아직 설치하지 않았다면 [YOMATES-INSTALL.md](YOMATES-INSTALL.md) 순서대로 설치한 뒤 돌아오세요. 공식 다운로드는 https://yomates.ai 하나뿐이에요.
<!-- /yomates-install:readme -->

학원 쌤들을 위한 요메이트(Yomates) 스킬 묶음이에요. 주소 하나로 목록을 보고, 필요한 것만 골라 설치해요.

## 설치

요메이트 팀원에게 이렇게 보내요.
> https://github.com/from5302-lab/yomates-skills 의 SKILL.md 읽고 '쌤-스킬-설치' 스킬로 저장해 줘. 그다음 목록 보여 주고 내가 고른 것만 설치해 줘.

팀원이 체크 칸으로 목록을 보여 주고, 고른 것만 저장한 뒤 바로 연결할지 물어봐요. 나중에 "스킬 업데이트해 줘"라고 하면 최신으로 바꿔요.

## 들어 있는 스킬

| 스킬 | 할 수 있게 되는 것 | 쌤이 하실 일 |
|---|---|---|
| [스레드 연결](https://github.com/from5302-lab/yomates-threads-skill) | 말로 부탁하면 내 스레드에 글 올리기·답글·조회수·댓글 확인 | 페이스북·스레드 로그인 |
| [Firebase 세팅](https://github.com/from5302-lab/yomates-firebase-skill) | 내 사이트 주소와 데이터베이스 만들기, 첫 화면 배포 | 구글 로그인 (필요할 때만 Blaze 카드 등록) |
| [학원 AI 팀 12명](https://github.com/from5302-lab/yomates-academy-team) | 상담·데스크·수납·리포트·채점·시험지·홈페이지 등 팀원 12명을 한 번에 들이기 | 학원 이름·과목·학년 답하기 |
| [솔라피 문자 연결](https://github.com/from5302-lab/yomates-solapi-skill) | 학부모·학생 문자 보내기, 내 사이트에서 자동 문자 | 솔라피 로그인, 발신번호 인증, 충전 |

로그인과 결제를 뺀 복잡한 설정은 요메이트 팀원이 해요. 키와 토큰은 쌤 컴퓨터(맥은 키체인)에만 저장되고, 채팅이나 AI 화면에 나오지 않아요.

## 새 스킬 더하기 (관리자용)

1. 스킬 저장소를 만들고 SKILL.md 맨 위에 `name`과 `description`을 넣어요.
2. 이 저장소의 `skills.json`에 한 줄을 더해요(id, name, title, what, you_do, repo, skill_url).
