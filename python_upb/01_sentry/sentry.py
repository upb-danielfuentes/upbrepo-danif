import sentry_sdk

sentry_sdk.init(
    dsn="https://3f05934c49e0a8f851715c05a7c34b31@o4505677157695488.ingest.sentry.io/4505681394073600",
    traces_sample_rate=1.0
)

# Función para capturar excepciones y mensajes
def capture_exception(e):
    sentry_sdk.capture_exception(e)

def capture_message(message):
    sentry_sdk.capture_message(message)

# Manejar excepciones generales
try:
    import main_script
except Exception as e:
    capture_exception(e)
    capture_message("Error en el script principal")
