N = int(input())

# solve it without any methods and with while loops only
while N > 0:
    string = str(input())
    if string == "NO" or string == "nO" or string == "No" or string == "no" \
            or string == "ON" or string == "On" or string == "oN" or string == "on":
        print(f"Match: {string}")
    N -= 1
