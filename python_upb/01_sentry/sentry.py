import sentry_sdk

sentry_sdk.init(
    dsn="https://3f05934c49e0a8f851715c05a7c34b31@o4505677157695488.ingest.sentry.io/4505681394073600",
    traces_sample_rate=1.0
)

def zero_division():
    try:
        zerocheck= int(input("Enter the number: "))
        zerocheck = 1 / zerocheck
        print(zerocheck)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        sentry_sdk.capture_message("Zero Division is Impossible")

zero_division()
