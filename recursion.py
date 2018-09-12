def hold_input():
    print("Enter two number to compute number1 to the power number2")
    number1 = input("Enter number1: ")
    number2 = input("Enter number2: ")
    print(Power(number1,number2))


def Power(a,b):
    if b == 1:
        return a;
    else:
        return (a * Power(a,b-1));

    
hold_input()