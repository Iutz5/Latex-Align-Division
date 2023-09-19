def latex(divider, divisor):
    res = "\\begin{allign}\n"
    quotient = 0
    remainder = 0
    if divider < 0:
        while divider < 0:
            res += "\t{} - {} &= {} \\tag{{{}}} \\\\\n".format(divider, divisor, divider-divisor, quotient-1)
            divider += divisor
            quotient -= 1
        remainder = divider
    else:
        while divider >= divisor:
            res += "\t{} - {} &= {} \\tag{{{}}} \\\\\n".format(divider, divisor, divider-divisor, quotient+1)
            divider -= divisor
            quotient += 1
        remainder = divider

    res += "\\end{allign}"
    return res

while True:
    try:
        divider = int(input("Please put in a dividend: "))
        divisor = int(input("Please put in a divisor: "))
        print(latex(divider, divisor))
    except ValueError:
        print("Invalid input. Please enter valid integers for the dividend and divisor.")
    else:
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != "yes":
            break