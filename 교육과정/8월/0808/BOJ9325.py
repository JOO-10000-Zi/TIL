T = int(input())
for _ in range(T):
    car_pay = int(input())
    n = int(input())
    full_car = [car_pay]
    for _ in range(n):
        cnt, pay = map(int, input().split())
        full_car.append(cnt * pay)
    print(sum((full_car)))