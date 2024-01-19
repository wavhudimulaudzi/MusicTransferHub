from .models import User


def create_user(email, password, provider, role, verified, full_name=None):
    """
    Create a new user and add it to the database.
    """
    user = User(email=email, full_name=full_name, provider=provider, role=role, verified=verified)
    user.set_password(password)
    user.save()
    return user


def get_user_by_email(email):
    """
    Retrieve a user by email.
    """
    try:
        user = User.objects.get(email=email)
        return user
    except User.DoesNotExist:
        return None


def get_all_users():
    """
    Retrieve all users from the database.
    """
    return User.objects.all()

# def update_user_by_email(email):
#
#     user = get_user_by_email(email)
#
#     if user !== None:
