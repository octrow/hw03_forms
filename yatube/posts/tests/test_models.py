from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание'
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост'
        )


    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        # Напишите проверку тут
        self.assertEqual(str(PostModelTest.post), 'Тестовый пост... ')
        self.assertEqual(str(PostModelTest.group), 'Тестовая группа')
        self.assertEqual(str(PostModelTest.user), 'auth')

    
    def test_models_have_correct_verbose_names(self):
        """Проверяем, что модель Post имеет верное поле verbose_names."""
        # Напишите проверку тут
        self.assertEquals(Post._meta.get_field('text').verbose_name, 'Текст поста')
        self.assertEquals(Group._meta.get_field('title').verbose_name, 'Имя группы')
        self.assertEquals(User._meta.get_field('username').verbose_name, 'имя пользователя')

    
    def test_models_have_correct_help_texts(self):
        """Проверяем, что модель Post имеет верное поле help_text."""
        # Напишите проверку тут
        self.assertEquals(Post._meta.get_field('text').help_text, 'Введите текст поста')
        self.assertEquals(Group._meta.get_field('title').help_text, '')
        

    def test_post_creation(self):
        """Проверяем, что модель Post создается правильно."""
        # Напишите проверку тут
        self.assertEqual(PostModelTest.post.text, 'Тестовый пост')
        self.assertEqual(PostModelTest.post.author, PostModelTest.user)
        self.assertEqual(PostModelTest.group.title, 'Тестовая группа')
        self.assertEqual(PostModelTest.group.slug, 'Тестовый слаг')
        self.assertEqual(PostModelTest.group.description, 'Тестовое описание')
        self.assertEqual(PostModelTest.user.username, 'auth')
    

    def test_group_creation(self):
        """Проверяем, что модель Group создается правильно."""
        # Напишите проверку тут
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(Group.objects.get(title='Тестовая группа').title, 'Тестовая группа')
        self.assertEqual(Group.objects.get(title='Тестовая группа').slug, 'Тестовый слаг')
        self.assertEqual(Group.objects.get(title='Тестовая группа').description, 'Тестовое описание')
    





    

    
