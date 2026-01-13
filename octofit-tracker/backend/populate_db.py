django.setup()
django.setup()
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
# from myapp.models import Workout  # Replace 'myapp' and 'Workout' with your actual app/model names


def populate():
    # Create a primary test user
    User.objects.get_or_create(username='testuser', defaults={'email': 'test@example.com'})

    # Create a few more test users (visible "test data")
    for i in range(3):
        User.objects.get_or_create(username=f'testuser{i}',
                                   defaults={'email': f'test{i}@example.com'})

    print("Database populated with test data!")

if __name__ == '__main__':
    populate()
