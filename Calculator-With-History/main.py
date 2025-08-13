history_file = "history.txt"

def show_history():
    with open(history_file, 'r') as f:
        lines = f.readlines()

    if len(lines) == 0:
        print("No History Found!")
    else:
        for line in reversed(lines):
            print(line.strip())

def clear_history():
    file = open(history_file, 'w')
    file.close()
    print("History Cleared!")

def saved_to_history(equation, result):
    file = open(history_file, 'a')
    file.write(f"{equation} = {str(result)}\n")
    file.close()

def calculate(user_input):
    allowed = "0123456789+-/*%.() **"

    if not all(char in allowed for char in user_input):
        print("Invalid characters in input!")
        return
    
    try:
        result = eval(user_input)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        print("Result: ", result)
        saved_to_history(user_input, result)

    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception:
        print("Invalid calculation!")

def main():
    print("----- SIMPLE CALCULATOR -----")

    while True:
        user_input = input("Enter calculation (+, -, *, /, %, **) or command (history, clear or exit): ").capitalize()
        if user_input == "Exit":
            print("Goodbye!")
            break
        elif user_input == "History":
            show_history()
        elif user_input == "Clear":
            clear_history()
        else:
            calculate(user_input)

main()