#!/bin/bash
# 요메이트 설치 안내 원본(common/)을 충쌤 스킬 저장소 전부에 똑같이 퍼뜨린다. 공개/비공개 설정은 건드리지 않는다.
# 쓰는 법: bash common/sync.sh   (gh 로그인 필요)
# 저장소를 새로 만들면 아래 REPOS 에 넣고 다시 돌린다.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REPOS=(
  yomates-skills
  yomates-academy-team
  yomates-academy-homepage
  yomates-solapi-skill
  yomates-threads-skill
  yomates-firebase-skill
  yomates-home-tutor-academy
  yomates-home-tutor-parent
)
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
for r in "${REPOS[@]}"; do
  if ! gh repo view "from5302-lab/$r" >/dev/null 2>&1; then echo "$r: 저장소 없음, 건너뜀"; continue; fi
  gh repo clone "from5302-lab/$r" "$WORK/$r" -- --depth 1 -q
  if [ "$r" = "yomates-skills" ]; then mkdir -p "$WORK/$r/common"; cp "$HERE"/YOMATES-INSTALL.md "$HERE"/blocks.md "$HERE"/apply.py "$HERE"/sync.sh "$WORK/$r/common/"; fi
  echo -n "$r: "; python3 "$HERE/apply.py" "$HERE" "$WORK/$r"
  cd "$WORK/$r"
  if [ -n "$(git status --porcelain)" ]; then
    git add -A && git commit -qm "요메이트 설치 안내 공통 적용 (common/YOMATES-INSTALL.md)" && git push -q && echo "  → 올림 $(git rev-parse --short HEAD)"
  else
    echo "  → 바뀐 것 없음"
  fi
  cd - >/dev/null
done
