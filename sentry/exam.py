import sentry_sdk
from sentry_sdk import capture_exception
from sentry_sdk import capture_message

def zero_division():
    try:
        zerocheck= int(input("Enter the number: "))
        zerocheck = 1 / zerocheck
        print(zerocheck)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        sentry_sdk.capture_message("Zero Division Error")
zero_division()    