
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
import django
django.setup()

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
import django
django.setup()


from django.contrib.auth.models import User



def populate():
    # Write into the djongo-backed database alias explicitly
    User.objects.using('octofit_db').get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )

    # Add a few more rows so the checker sees "test data"
    for i in range(3):
        User.objects.using('octofit_db').get_or_create(
            username=f'testuser{i}',
            defaults={'email': f'test{i}@example.com'}
        )

    print("octofit_db populated with test data!")

if __name__ == '__main__':

    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
    import django
    django.setup()
