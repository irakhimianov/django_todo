from django.test import TestCase
from django.contrib.auth import get_user_model

from todoapp.models import Task

User = get_user_model()


class TaskListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_tasks = 13
        user = User.objects.create_user(
            username='test_username',
            email='testemail@email.com',
            password='_Qtest_any$31231asaxz123',
        )
        for task in range(number_of_tasks):
            Task.objects.create(
                title='title_name',
                description='description_text',
                is_completed=False,
                owner=user,
            )
