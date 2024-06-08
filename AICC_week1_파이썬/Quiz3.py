# 문제 1) 가로가 4이고 세로가 2인 삼각형의 넓이 출력
width = 4
height = 2
area = (width * height) / 2
print("넓이는 = %d 입니다" % area)

# 문제 2) 월급이 100원이다. 세금 10%를 제외한 연봉 출력
monthly_salary = 100
tax_rate = 0.1
annual_salary = monthly_salary * 12 * (1 - tax_rate)
print(annual_salary)
print("연봉은 %d 원입니다" % annual_salary)

# 문제 3) 100초를 1분 40초로 출력
seconds = 100
divider = 100 / 60
minutes = seconds // 60
remaining_seconds = seconds % 60
print(divider, minutes, remaining_seconds)
print("100초는", minutes, "분", remaining_seconds, "초 입니다")
print("100초는 %d 분 %d 초 입니다" % (minutes, remaining_seconds))


# 문제 4) 800원에서 500원을 제외한 100원의 개수 출력
total_money = 800
removed_500 = 500
remaining = total_money - removed_500
count_100 = remaining // 100
print("100원의 개수 =", count_100)
print("100원의 개수는 %d 개 입니다." % count_100)