def multiplication_table(n):
    for i in range(1,21):
        print(f"{n} * {i} = {n * i}")

number = (int(input("enter the table to generate multiplication table: ")))

multiplication_table(number)