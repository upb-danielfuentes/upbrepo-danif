import sentry_sdk

sentry_sdk.init(
  dsn="https://3f05934c49e0a8f851715c05a7c34b31@o4505677157695488.ingest.sentry.io/4505681394073600",

  # Set traces_sample_rate to 1.0 to capture 100%
  # of transactions for performance monitoring.
  # We recommend adjusting this value in production.
  traces_sample_rate=1.0
)