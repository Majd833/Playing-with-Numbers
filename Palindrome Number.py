digit=int(input("Enter the number that you want to test:"))
original_number=digit
reversed_number=0
while digit>0:
    number=digit%10
    reversed_number=reversed_number*10+number
    digit//=10
if original_number==reversed_number:
    print(original_number, "is a palindrome")
else:
    print(original_number,"isn't a palindrome")