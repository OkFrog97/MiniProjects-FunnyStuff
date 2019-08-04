from name_function import get_formated_name


def main():
    print("Enter 'q' for any time to quit\n")
    while True:
        first_name = input("Enter first name: ")
        if first_name == "q":
            break
        last_name = input("Enter last name: ")
        if last_name == "q":
            break
        print(get_formated_name(first_name, last_name))


if __name__ == "__main__":
    main()
    