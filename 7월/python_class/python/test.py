'''
import numbers


print('Hello woled')

lunch =['짜장면', '햄버거', '순대국밥', '김밥', '라면']
print(lunch[0])


numbers = input().split()
print(numbers)
'''

num = int(input())

if num > 151 :
    print('매우나쁨')
elif num > 80:
    print('나쁨')
elif num > 30:
    print('보통')
else :
    print('매우좋음')
 
print(num)

