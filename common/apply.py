"""충쌤 스킬 저장소 하나에 요메이트 설치 안내를 넣거나 원본과 똑같이 맞춘다(여러 번 돌려도 같은 결과).
쓰는 법: python3 apply.py <원본 common 폴더> <저장소 폴더>
- YOMATES-INSTALL.md 를 원본 그대로 복사
- README.md 맨 위(첫 제목 바로 아래)에 readme 블록
- SKILL.md 앞머리(frontmatter)와 첫 제목 바로 아래에 '0단계' 블록
블록은 <!-- yomates-install:... --> 표시 사이를 통째로 바꾼다.
"""
import sys, re, os, shutil

src, repo = sys.argv[1], sys.argv[2]
blocks = open(os.path.join(src, "blocks.md"), encoding="utf-8").read()

def block(name):
    m = re.search(rf"(<!-- yomates-install:{name} -->.*?<!-- /yomates-install:{name} -->)", blocks, re.S)
    return m.group(1)

def put(path, name):
    if not os.path.exists(path):
        return f"{os.path.basename(path)} 없음"
    t = open(path, encoding="utf-8").read()
    b = block(name)
    pat = re.compile(rf"<!-- yomates-install:{name} -->.*?<!-- /yomates-install:{name} -->", re.S)
    if pat.search(t):
        new = pat.sub(lambda _: b, t)
    else:
        pos = 0
        fm = re.match(r"---\n.*?\n---\n", t, re.S)
        if fm:
            pos = fm.end()
        h1 = re.compile(r"^# .*\n", re.M).search(t, pos)
        if h1 and t[pos:h1.start()].strip() == "":
            pos = h1.end()
        new = t[:pos] + ("\n" if pos and not t[:pos].endswith("\n\n") else "") + b + "\n\n" + t[pos:].lstrip("\n")
    if new != t:
        open(path, "w", encoding="utf-8").write(new)
        return f"{os.path.basename(path)} 바꿈"
    return f"{os.path.basename(path)} 그대로"

shutil.copyfile(os.path.join(src, "YOMATES-INSTALL.md"), os.path.join(repo, "YOMATES-INSTALL.md"))
print(put(os.path.join(repo, "README.md"), "readme"), "·", put(os.path.join(repo, "SKILL.md"), "skill"))
