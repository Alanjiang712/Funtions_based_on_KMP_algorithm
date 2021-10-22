import re

astr = "abcccba"

adict = {
    "a": "d",
    "b": "e",
    "c": "f",
}


def keyword_replace(s, replace_dict):

    next = []
    next_str = s

    def buildNext():
        next.append(0)
        x = 1
        now = 0
        while x < len(p):
            if p[now] == p[x]:
                now += 1
                x += 1
                next.append(now)
            elif now:
                now = next[now-1]
            else:
                next.append(0)
                x += 1

    def search(new_str):
        tar = 0
        pos = 0
        while tar < len(s):
            if s[tar] == p[pos]:
                tar += 1
                pos += 1
            elif pos:
                pos = next[pos-1]
            else:
                tar += 1
            if pos == len(p):   # 匹配成功
                next_str = re.sub(p, replace_dict[p], new_str)
                pos = next[pos-1]
                return next_str

    for p in replace_dict:
        buildNext()
        next_str = search(next_str)

    return next_str


print(keyword_replace(astr, adict))
