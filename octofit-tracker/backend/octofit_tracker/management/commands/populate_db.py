from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Verwijder bestaande data
        get_user_model().objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Gebruikers
        User = get_user_model()
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test123', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='test123', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='test123', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='test123', team=dc)

        # Workouts
        w1 = Workout.objects.create(name='Pushups', description='Pushups workout')
        w2 = Workout.objects.create(name='Running', description='Running workout')

        # Activities
        Activity.objects.create(user=ironman, workout=w1, duration=30)
        Activity.objects.create(user=batman, workout=w2, duration=45)

        # Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db succesvol gevuld met testdata.'))
