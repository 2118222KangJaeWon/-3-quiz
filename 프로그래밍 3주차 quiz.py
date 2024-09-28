# Quiz 1
user_input = input("인사말을 입력하세요: ")

if user_input == '안녕하세요':
    print('반갑습니다')
else:
    print('인사를 먼저하세요.')

# Quiz 2
user_input = input("숫자를 입력하세요: ")
value = int(user_input) + 100

if value >= 150:
    print(value)
else:
    print('값이 부족합니다.')

# Quiz 3
numbers = [100, 200, 300]
result = []

for price in numbers:
    result.append(price * 1.1)  # 10% 부가세 추가

print(result)

# Quiz 4
numbers = [3, 100, 23, 33, 72, 94]
multiples_of_three = []

for number in numbers:
    if number % 3 == 0:
        multiples_of_three.append(number)

print(multiples_of_three)

# Quiz 5
waiting_number = 1

while waiting_number <= 1000:
    print(f'대기번호: {waiting_number}')
    waiting_number += 1

# Quiz 6
sum_of_odds = 0
number = 1

while number <= 100:
    if number % 2 != 0:  # 홀수인지 확인
        sum_of_odds += number
    number += 1

print(f'1부터 100까지의 홀수의 합: {sum_of_odds}')

