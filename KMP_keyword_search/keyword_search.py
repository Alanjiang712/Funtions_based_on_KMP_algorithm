from evaluateDict import evaluateDict
from symptomDict import symptomDict


def keyword_search(s, target_list):
    evaluateList = evaluateDict.keys()
    symptomList = symptomDict.keys()

    def KMP(s, keywords_list):
        next = []

        match = []

        location_words_keys = []

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

        def search():
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
                    location_words_keys.append(
                        [p, (tar - pos), Dict[p]])
                    match.append(p)
                    pos = next[pos-1]

        for p in keywords_list:
            buildNext()
            search()

        keywords = sorted(set(match), key=match.index)

        return location_words_keys, keywords

    if target_list == "EVALUATE":
        Dict = evaluateDict
        output = KMP(s, evaluateList)
        return output
    elif target_list == "SYMPTOM":
        Dict = symptomDict
        output = KMP(s, symptomList)
        return output
    else:
        return "Target list is not found, please check your spelling"
