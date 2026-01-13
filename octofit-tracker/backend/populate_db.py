django.setup()
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
# from myapp.models import Workout  # Replace 'myapp' and 'Workout' with your actual app/model names

def populate():
    # Create a test user
    user, _ = User.objects.get_or_create(username='testuser', email='test@example.com')

    # Create some test workouts
    workouts = [
        {'name': 'Cardio Blast', 'duration': 30, 'user': user},
        {'name': 'Strength Training', 'duration': 45, 'user': user},
        {'name': 'Yoga Session', 'duration': 60, 'user': user},
    ]

    for w in workouts:
        # Workout.objects.get_or_create(**w)
        pass  # Uncomment and update the above line after defining the Workout model

    print("Database populated with test data!")

if __name__ == '__main__':
    populate()
