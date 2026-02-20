from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name, is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name, is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name, is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name, is_superhero=True)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=steve, type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=bruce, type='swim', duration=60, date='2024-01-03')
        Activity.objects.create(user=clark, type='fly', duration=120, date='2024-01-04')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=200)
        Leaderboard.objects.create(user=steve, score=180)
        Leaderboard.objects.create(user=bruce, score=220)
        Leaderboard.objects.create(user=clark, score=250)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Situps', description='Do situps', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='medium')
        Workout.objects.create(name='Deadlift', description='Heavy deadlift', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
