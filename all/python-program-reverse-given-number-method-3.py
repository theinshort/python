def reverse_number(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_number = number // 10
        reversed_number = reverse_number(remaining_number)
        return int(str(last_digit) + str(reversed_number))
 
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)