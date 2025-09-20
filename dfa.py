def check_dfa(input_string):

    q0 = 0
    q1 = 1
    q2 = 3
    q3 = 2

    current_state = q0
    final_state = q0


    for char in input_string:
        # Transition from q0
        if current_state == q0:
            if char == '0':
                current_state = q1
            elif char == '1':
                current_state = q3
        # Transition from q1
        elif current_state == q1:
            if char == '1':
                current_state = q2
            elif char == '1':
                current_state = q0
        # Transition from q2
        elif current_state == q2:
            if char == '1':
                current_state = q1
            elif char == '0':
                current_state = q3
        # Transition from q3
        elif current_state == q3:
            if char == '1':
                current_state = q0
            elif char == '0':
                current_state = q2


    return current_state == final_state

test_string = "0010100"
is_accepted = check_dfa(test_string)

if is_accepted:
    print(f"The string '{test_string}' is accept.")
else:
    print(f"The string '{test_string}' is no accept")
