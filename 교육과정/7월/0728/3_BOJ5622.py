import string

name = input().upper()
a = string.ascii_uppercase
# 내장함수를 불러와서 A ~ Z 까지 대문자를 a 에 정의한다
daaear = {}
sum_number = []
# a에 있는 문자(A ~ Z)를 순회 하면서
# i 가 각각의 번호판에 있는 문자와 같으면 소요되는 시간을
# 딕셔너리 daaear(다이얼)에 키값을 통해 value 값을 수정
for i in a:
    if i == "A" or i == "B" or i == "C":
        daaear[i] = 3
    elif i == "D" or i == "E" or i == "F":
        daaear[i] = 4
    elif i == "G" or i == "H" or i == "I":
        daaear[i] = 5
    elif i == "J" or i == "K" or i == "L":
        daaear[i] = 6
    elif i == "M" or i == "N" or i == "O":
        daaear[i] = 7
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        daaear[i] = 8
    elif i == "T" or i == "U" or i == "V":
        daaear[i] = 9
    elif i == "W" or i == "X" or i == "Y" or i == "Z":
        daaear[i] = 10
for X in name:
    sum_number.append(daaear[X])
# 노가다를 한 후 name 인풋값을 X로 순회 하면서
# 딕셔너리의 value 값을 뽑아 sum_number 리스트에 넣은후
# 리스트의 값을 더하여 출력 한다
print(sum(sum_number))