# factories.py
import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating test User instances.
    
    Generates User objects with realistic fake data for testing purposes.
    """
    class Meta:
        model = User

    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall('set_password', 'defaultpass123')