triangle = []

for _ in range(3):
    num = int(input())
    triangle.append(num)

if 60 == triangle[0] and 60 == triangle[1] and 60 ==triangle[2]:  
    print("Equilateral")
elif 180 == sum(triangle) and (triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[2] == triangle[0]):
    print("Isosceles")
elif 180 == sum(triangle) and (triangle[0] != triangle[1] or triangle[0] != triangle[2] or triangle[1] != triangle[2]):
    print("Scalene")
elif 180 != sum(triangle):
    print("Error")
