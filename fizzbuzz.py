def fizzbuzz(n):
    # n=int(input("Enter the number"))
    for i in range(1,15):
        if i%3==0:
            print("Fizz")

        elif i%5==0:
            print("Buzz")

        elif i%15==0:
            print("FizzBuzz")

            return n