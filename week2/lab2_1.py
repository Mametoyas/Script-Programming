while True:
    numb = input("Input the Number ('x' to exit): ")

    if numb.lower() == 'x':
        break

    def odd_or_even(number):
        if number % 2 == 0:
            return "even"
        else:
            return "odd"

    def is_num(number):
        try:
            number_f = int(number)

            if number_f > 0:
                sign = "positive"
            elif number_f < 0:
                sign = "negative"
            else:
                sign = "zero"

            parity = odd_or_even(number_f)

            print(f"The number is {sign} and {parity}.")

        except ValueError:
            print("PLEASE input a NUMBER!")

    is_num(numb)