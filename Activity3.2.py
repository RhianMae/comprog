while True:
    input_password = input(
"Enter the password: ")
    has_letter = False
    has_digit = False

    for c in input_password:
        if c.isalpha():
            has_letter = True
        if c.isdigit():
            has_digit = True

    if has_letter and has_digit:
        print("Password accepted.")
        break
    else:
        print("Invalid password.")
