from django.apps import AppConfig


class HypAppConfig(AppConfig):
    name = 'hyp_app'

    def ready(self):
        from . import scheduler
        scheduler.start()