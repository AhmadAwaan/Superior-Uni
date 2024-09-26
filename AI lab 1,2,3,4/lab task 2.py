def fizz_buzz(a):
    for i in range(1, a + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
a = int(input("enter a no"))
fizz_buzz(a)