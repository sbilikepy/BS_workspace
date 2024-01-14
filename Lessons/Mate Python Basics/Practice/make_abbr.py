def make_abbr(words: str) -> str:
    if words == "":
        return ""
    else:
        result = ""
        result += words[0]
        for i in range(len(words)):
            if words[i] == " ":
                result += words[(i) + 1]
    return result.upper()
