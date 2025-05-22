# main.py

from calculator import Calculator

def display_menu():
    print("\nSimple OOP Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    calc = Calculator()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting...")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            calc.set_values(a, b)

            if choice == '1':
                print("Result:", calc.add())
            elif choice == '2':
                print("Result:", calc.subtract())
            elif choice == '3':
                print("Result:", calc.multiply())
            elif choice == '4':
                print("Result:", calc.divide())
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()
