from jar import Jar

# Created a main function to run the Jar program
def main():
    jar = Jar(12)

    while True:
        command = input("Deposit, withdraw, or quit? ").lower()

        if command == 'deposit':
            num = int(input("How many cookies to deposit? "))
            jar.deposit(num)

        elif command == 'withdraw':
            num = int(input("How many cookies to withdraw? "))
            jar.withdraw(num)

        elif command == 'quit':
            break

        print(f"Jar now has {jar.size} cookies")

    print("Goodbye!")

if __name__ == '__main__':
    main()
