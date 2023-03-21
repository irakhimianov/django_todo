from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from todoapp.models import Task

User = get_user_model()


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='test_username',
            email='testemail@email.com',
            password='_Qtest_any$31231asaxz123',
        )
        Task.objects.create(
            title='title_name',
            description='description_text',
            is_completed=False,
            owner=user,
        )

    def test_title_label(self):
        task = list(Task.objects.all())[0]
        field_label = task._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'заголовок')

    def test_description_label(self):
        task = list(Task.objects.all())[0]
        field_label = task._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'описание')

    def test_is_completed_label(self):
        task = list(Task.objects.all())[0]
        field_label = task._meta.get_field('is_completed').verbose_name
        self.assertEquals(field_label, 'выполнен')

    def test_title_max_length(self):
        task = list(Task.objects.all())[0]
        max_length = task._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_task_is_completed(self):
        task = list(Task.objects.all())[0]
        self.assertFalse(task.is_completed)

    def test_task_created_today(self):
        task = list(Task.objects.all())[0]
        today_date = timezone.now().date()
        self.assertEquals(task.created_at.date(), today_date)

    def test_task_updated_today(self):
        task = list(Task.objects.all())[0]
        today_date = timezone.now().date()
        self.assertEquals(task.updated_at.date(), today_date)
