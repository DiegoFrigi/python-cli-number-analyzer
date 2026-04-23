def get_values():
    values = []

    while True:
        user_input = input("Enter a value(q to quit): ").strip()

        if user_input.lower() == "q":
            break

        if not user_input:
            print("Enter a valid value")
            continue

        values.append(user_input)

    return values

def get_average(valid_values):

    if not valid_values:
        return None

    return sum(valid_values) / len(valid_values)

def separate_values(values):
    valids = []
    invalids = []

    for value in values:
        try:
            valids.append(float(value))
        except ValueError:
            invalids.append(value)

    return valids, invalids

def min_max(valid_values):
 
    if not valid_values:
        return None, None
    
    return min(valid_values), max(valid_values)

def sorted_values(valid_values):

    return sorted(valid_values)
            
def main():
        new_values = []

        while True:
            print("=====MENU=====")
            print("1. Enter values")
            print("2. Get average")
            print("3. Largest value")
            print("4. Smallest value")
            print("5. Valid values")
            print("6. Invalid values")
            print("7. Sum of values")
            print("8. Show sorted values")
            print("===============")

            option = input("Enter an option(1-8 or q to quit): ").strip()

            if option.lower() == "q":
                break

            if option not in ("1","2","3","4","5","6","7","8"):
                print("Enter a valid option")
                continue

            valids, invalids = separate_values(new_values)

            if option == "1":
                new_values.extend(get_values())

            elif option == "2":
                avg = get_average(valids)
                print("Enter a valid number" if avg is None else f"The average is: {avg:.2f}")

            elif option == "3":
                _, max_value = min_max(valids)
                print("Enter a valid number" if max_value is None else f"The largest number is: {max_value}")

            elif option == "4":
                min_value, _ = min_max(valids)
                print("Enter a valid number" if min_value is None else f"The smallest number is: {min_value}")
            
            elif option == "5":
                print(f"Valid values: {valids}")

            elif option == "6":
                print(f"Invalid values: {invalids}")

            elif option == "7":
                print(f"Sum of values: {sum(valids):.2f}")

            elif option == "8":
                sorted_vals = sorted_values(valids)
                print(f"Sorted values: {sorted_vals}")

if __name__=="__main__":
    main()


