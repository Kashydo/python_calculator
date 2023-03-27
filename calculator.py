
import os
import sys
OPERETORS = '+-*/'


def key_pressed():
    try:
        import tty
        import termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def is_running(key, is_running=True):
    if key == 'q':
        is_running = False
    return is_running


def is_number(str):
    try:
        float(str)
    except ValueError:
        return False
    return True


def convert_number(str):
    if is_number(str):
        return float(str)


def is_valid_operator(operator):
    if operator in list(OPERETORS):
        return True


def ask_for_a_number(force_valid_input=True):
    while force_valid_input:
        number = input('Please provide a number!: ')

        if is_number(number):
            force_valid_input = False
        else:
            print("This didn't look like a number, try again")
    return convert_number(number)


def ask_for_an_operator(force_valid_input=True):
    while force_valid_input:

        operator = input('Please provide an operator (one of +, -, *, /)!: ')
        if is_valid_operator(operator):
            force_valid_input = False
        else:
            print("Unknown operator")
    return operator


def calc(operator, a, b):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b != 0:
                return a / b
            else:
                print('Error: Division by zero')
                return None


def simple_calculator():
    print("Kalkulator")
    print('Press enter to continue')
    is_running = True
    while is_running:

        key = key_pressed()
        if key == 'q':
            is_running = False
        else:
            a = ask_for_a_number()
            operator = ask_for_an_operator()
            b = ask_for_a_number()
            print(f'The result is {calc(operator,a,b)}')
            print('Press enter to continue or q to exit')


if __name__ == '__main__':
    simple_calculator()
