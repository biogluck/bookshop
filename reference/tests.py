from django.test import TestCase

from .models import Author


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(name="Василий", short_name="В.")
        Author.objects.create(name="Тургенев", short_name="Т.")

    def test_author_str(self):
        a1 = Author.objects.get(name="Василий")
        self.assertEqual(a1.name, 'Василий')

    def test_author_is_instance(self):
        a1 = Author.objects.get(name="Василий")
        self.assertIsInstance(a1, Author)

    def test_author_is_instance(self):
        a1 = Author.objects.get_or_create(name="Василий"*50)
        self.assertRaises(ValueError)

    def test_author_nums_in_name(self):
        aut = Author.objects.get(name="Василий")
        self.assertRegex(text=aut.name, expected_regex=r'[0-9]')
