
login = int(input())

office_Human = {}
work_holic = []
check_out = []
for _ in range(login):
    name, chool = input().split()
    office_Human[name] = chool
    for run_out in office_Human[name]:
        check_out += run_out
        check_login = "".join(check_out)
        if 'enter' == check_login:
            work_holic.append(name)
        print(check_out)
    




