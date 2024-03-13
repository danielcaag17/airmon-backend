from django.apps import AppConfig
from .data_providers.provider_registry import provider_registry
from .data_providers.provider import Provider


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):

        gen_cat = Provider("gen_cat", "https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json")
        provider_registry.add_provider(gen_cat)
