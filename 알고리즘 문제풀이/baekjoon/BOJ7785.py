import sys
sys.stdin = open("7785.txt")

N = int(input())

login = {}
for _ in range(N):
    k, v = input().split()
    login[k] = v

work_hollic = []
for k, v in login.items():
    if v != "leave":
        work_hollic.append(k)
work_hollic.sort(reverse=True)
print(*work_hollic, sep="\n")













# login = int(input())


# # logs = dict()
# # logs["Baha"] = 'enter'
# # logs["Askar"] = 'enter'
# # logs["Baha"] = 'leave'
# # logs["Artem"] = 'enter'
# for _ in range(login):
#     key, value = input().split()
#     logs = {}
#     logs[key] = value
#     list_ = []
#     print(logs)
# for key in logs:
#     if logs[key] == 'enter':
#         list_.append(key)
#     print(list_)
#     list_.sort(reverse=True)
#     for name in list_:
#         print(name)



# # office_Human = {}
# # work_holic = []
# # check_out = []
# # for _ in range(login):
# #     name, chool = input().split()
# #     office_Human[name] = chool
# #     for run_out in office_Human[name]:
# #         check_out += run_out
# #         check_login = "".join(check_out)
# #         if 'enter' == check_login:
# #             work_holic.append(name)
# # print(work_holic)
    




