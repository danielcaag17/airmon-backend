from .provider import Provider


class ProviderRegistry:
    def __init__(self):
        self.providers = {}

    def add_provider(self, provider: Provider):
        self.providers[provider.get_name()] = provider

    def get_provider(self, name):
        return self.providers.get(name)

    def get_provider_url(self, name):
        provider = self.get_provider(name)
        if provider is None:
            return ""
        return provider.get_url()

    def get_providers(self):
        return self.providers


provider_registry = ProviderRegistry()
