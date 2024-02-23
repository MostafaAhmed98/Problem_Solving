num = int(input("Enter Your Number: \n"))

years_count = num // 360  # 13
num_after_years = num - (years_count * 360)  # 320
months_count = num_after_years // 30  # 10, number_after_years = 320
days_count = num_after_years - (months_count * 30)  # 20

print(years_count, months_count, days_count)
