from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC'),
            User.objects.create(email='superman@dc.com', name='Superman', team='DC'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now().date())

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Upper body exercise', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Lower body exercise', difficulty='Medium')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
