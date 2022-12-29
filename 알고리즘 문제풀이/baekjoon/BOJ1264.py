mo_list = ["a", "e", "i" ,"o" , "u", "A", "E", "I", "O", "U" ]

while True:
    cnt = 0
    word_ = list(map(str, input()))
    for i in str(word_):
        if i == "#":
            break
        if i in mo_list:
            cnt +=1
    if word_[0] == "#":
        break
    print(cnt)
    

