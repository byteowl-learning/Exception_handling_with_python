try:
    num1 = input("Please enter a number: ")
    num2 = input("Please enter another number: ")
    result = int(num1)/int(num2)
    print(num1, "divided by", num2, "=", str(result))

except ZeroDivisionError as e:
    print("Sorry. you cannot divide a number by 0")

finally:
    print("Thank you for using this program.")
