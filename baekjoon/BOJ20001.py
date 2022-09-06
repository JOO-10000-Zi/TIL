
cnt = 0

while True:
    gomoo = input()
    if gomoo == "고무오리 디버깅 끝":
        break
    else:
        if gomoo == "고무오리":
            if cnt == 0:
                cnt += 2
            else:
                if cnt != 0:
                    cnt -= 1
        if gomoo == "문제":
            cnt += 1
if cnt == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")