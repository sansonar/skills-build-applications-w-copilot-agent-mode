from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', ASCENDING)], unique=True)

        # Sample data
        marvel_team = {'name': 'Team Marvel', 'members': ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow']}
        dc_team = {'name': 'Team DC', 'members': ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman']}
        teams = [marvel_team, dc_team]
        db.teams.insert_many(teams)

        users = [
            {'name': 'Tony Stark', 'email': 'tony@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Steve Rogers', 'email': 'steve@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Bruce Wayne', 'email': 'bruce@dc.com', 'team': 'Team DC'},
            {'name': 'Clark Kent', 'email': 'clark@dc.com', 'team': 'Team DC'},
        ]
        db.users.insert_many(users)

        activities = [
            {'user': 'Tony Stark', 'activity': 'Running', 'duration': 30},
            {'user': 'Steve Rogers', 'activity': 'Cycling', 'duration': 45},
            {'user': 'Bruce Wayne', 'activity': 'Swimming', 'duration': 60},
            {'user': 'Clark Kent', 'activity': 'Yoga', 'duration': 20},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {'team': 'Team Marvel', 'points': 150},
            {'team': 'Team DC', 'points': 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {'name': 'Full Body Blast', 'suggested_for': 'Team Marvel'},
            {'name': 'Speed & Agility', 'suggested_for': 'Team DC'},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
