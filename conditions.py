# has_high_income = True
# is_eligible = False
#
#
# if has_high_income and is_eligible:
#     print("Hello world")
# if has_high_income or is_eligible:
#     print("hello world".upper())



magic_number = 7
guess_count = 3

while guess_count !=0:
    guess = int(input("Enter a number: "))
    guess_count-=1
    if guess == magic_number:
        print("You guessed the number")
        break
else:
    print("Sorry you failed.")