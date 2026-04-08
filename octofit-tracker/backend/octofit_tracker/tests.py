from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

    def test_user_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='test123', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', description='desc')
        self.assertEqual(workout.name, 'TestWorkout')

    def test_activity_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='test123', team=team)
        workout = Workout.objects.create(name='TestWorkout', description='desc')
        activity = Activity.objects.create(user=user, workout=workout, duration=30)
        self.assertEqual(activity.duration, 30)

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='test123', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
