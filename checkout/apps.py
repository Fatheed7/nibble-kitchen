from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    verbose_name = 'Orders'

    def ready(self):
        import checkout.signals  # noqa: F401
