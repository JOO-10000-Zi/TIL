mail = input()

check_word = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']


for i in check_word:
    if i in mail:
        mail = mail.replace(i,"")
print(mail)


