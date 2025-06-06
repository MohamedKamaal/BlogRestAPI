import pytest
from users.factories import UserFactory  
from django.contrib.auth import get_user_model
from django.db import IntegrityError
import logging 
logger = logging.getLogger(__name__)
User = get_user_model()

pytestmark = pytest.mark.django_db  # global DB marker


def test_create_user():  
    user = UserFactory()

    assert User.objects.count() == 1

    user = User.objects.first()

    assert user.is_active is True
    assert user.is_superuser is False
    assert user.is_staff is False  # was `user.staff` — typo!


from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_user_duplicate_emails_fail():
    # Create the first user
    user1 = User.objects.create_user(
        email="testuser@yahoo.com",
        password = "testuserpass112",
        first_name = "testuser1",
        last_name = "lastname1"
        
       
    )
    
    with pytest.raises(IntegrityError):
        user2 = User.objects.create_user(
        email="testuser@yahoo.com",
        password = "testuserpass112",
        first_name = "testuser1",
        last_name = "lastname1"
       
    )


@pytest.mark.django_db
def test_user_invalid_email_fail():
    # Create the first user
    with pytest.raises(ValidationError):
        user = User.objects.create_user(
            email="testuseryahoo.com",
            password = "testuserpass112",
            first_name = "testuser1",
            last_name = "lastname1"
        )
        
@pytest.mark.django_db
def test_user_normalize_email_pass():
    # Create the first user
    user = User.objects.create_user(
        email="TestUser@YAHOO.com",
        password = "testuserpass112",
        first_name = "testuser1",
        last_name = "lastname1"
    )
    assert user.email == "TestUser@yahoo.com"
        
@pytest.mark.django_db
def test_user_without_email_fail():
    # Create the first user
    with pytest.raises(ValueError):
        user = User.objects.create_user(
            email="",
            password = "testuserpass112",
            first_name = "testuser1",
            last_name = "lastname1"
        )
        
@pytest.mark.django_db
def test_superuser_valid_data_pass():
    # Create the first user
    user = User.objects.create_superuser(
        email="admin@yahoo.com",
        password = "testuserpass112",
        first_name = "testuser1",
        last_name = "lastname1"
        
    )
    assert user.is_active is True
    assert user.is_superuser is True
    assert user.is_staff is True  
