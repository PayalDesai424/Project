

#Program of Reversing first and last name

def reverse():
    firstName=input("Enter your first name: ")
    lastName=input("Enter your last name: ")
    print(f'Hello {firstName} {lastName}')
    print(f'Your reversed name is: {lastName} {firstName}')

def main():
    reverse()

main()