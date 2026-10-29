<!-- yomates-install:readme -->
> **먼저 요메이트(Yomates)가 필요해요.** 이 스킬은 요메이트 앱 안에서 돌아가요. 아직 설치하지 않았다면 [YOMATES-INSTALL.md](YOMATES-INSTALL.md) 순서대로 설치한 뒤 돌아오세요. 공식 다운로드는 https://yomates.ai 하나뿐이에요.
<!-- /yomates-install:readme -->

<!-- yomates-install:skill -->
## 0단계: 요메이트가 있는지 먼저 확인 (이 스킬을 읽은 AI가 맨 먼저)

1. 지금 요메이트 팀원으로 돌고 있으면(요메이트 앱의 팀원 채팅에서 이 스킬을 받았으면) 이 단계를 건너뛰고 아래 원래 순서로 간다. 알아보는 법: 환경값 중 `LEVIOSA_` 로 시작하는 것이 있거나, `yomates`·`canvas_write` 같은 요메이트 도구가 있다.
2. 아니면(Claude Code, 다른 AI 앱, 파일을 그냥 연 경우) 이 컴퓨터에 요메이트가 깔려 있는지 본다.
   - 맥: `/Applications/Yomates.app` 또는 `~/Applications/Yomates.app` 이 있는지.
   - 윈도우: PowerShell `Get-StartApps | Where-Object Name -like '*Yomates*'` 결과가 있는지. 명령을 못 쓰면 사용자에게 시작 메뉴에서 'Yomates'를 찾아 달라고 한다.
3. 깔려 있지 않으면 이 저장소의 `YOMATES-INSTALL.md` 를 사용자에게 그대로 보여 주고 여기서 멈춘다. 설치 파일을 대신 내려받거나 실행하지 않는다. 다운로드 주소는 https://yomates.ai 만 안내한다.
4. 깔려 있는데 지금 요메이트 밖이면, "요메이트를 열고 팀원 채팅에 이 저장소 주소와 'SKILL.md 읽고 스킬로 저장해 줘'를 보내 주세요"라고 안내하고 멈춘다. 요메이트 밖에서 이 스킬의 나머지 단계를 돌리지 않는다.
<!-- /yomates-install:skill -->
