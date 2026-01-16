max_value = 50

for i in range(0, max_value + 1):
    three = i % 3
    four = i % 4
    check = three + four
    if check != 0:
        pass
    else:
        print(i)
        print("Wahoo!")