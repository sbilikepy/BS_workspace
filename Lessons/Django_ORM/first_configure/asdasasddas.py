def shortest_word(sentence: str) -> int:

    min_len = 99999999999
    for i in sentence.split():
        print(i)
        if len(i) < min_len:
            min_len = len(i)

    print(min_len)
shortest_word("call 911 asd ertwerfs")