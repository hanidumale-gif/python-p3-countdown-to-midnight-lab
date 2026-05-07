import time

def countdown(number):

    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1

    print("HAPPY NEW YEAR!")


def countdown_with_sleep(number):

    while number > 0:
        print(f"{number} SECOND(S)!")
        time.sleep(1)
        number -= 1

    print("HAPPY NEW YEAR!")


# Test the functions
countdown(5)

countdown_with_sleep(5)