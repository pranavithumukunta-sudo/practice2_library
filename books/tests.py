from django.test import TestCase, Client
from django.urls import reverse
from .models import Book
from .forms import BookForm

class BookModelTest(TestCase):
    def test_book_creation_and_str(self):
        book = Book.objects.create(
            title="Clean Code",
            author="Robert C. Martin",
            year_published=2008,
            is_available=True
        )
        self.assertEqual(str(book), "Clean Code")
        self.assertEqual(book.author, "Robert C. Martin")
        self.assertEqual(book.year_published, 2008)
        self.assertTrue(book.is_available)

class BookViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = Book.objects.create(
            title="Wings of Fire",
            author="A. P. J. Abdul Kalam",
            year_published=1999,
            is_available=True
        )
        self.book2 = Book.objects.create(
            title="Malgudi Days",
            author="R. K. Narayan",
            year_published=1943,
            is_available=False
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, "My Book Library")
        self.assertContains(response, "Wings of Fire")
        self.assertContains(response, "Malgudi Days")
        self.assertContains(response, "Available")
        self.assertContains(response, "Issued")
        self.assertEqual(len(response.context['books']), 2)

    def test_add_book_get_view(self):
        response = self.client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/add_book.html')
        self.assertIsInstance(response.context['form'], BookForm)
        self.assertContains(response, "Add a New Book")
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_add_book_post_valid(self):
        data = {
            'title': 'Automate the Boring Stuff',
            'author': 'Al Sweigart',
            'year_published': 2015,
            'is_available': True
        }
        response = self.client.post(reverse('add_book'), data)
        self.assertRedirects(response, reverse('book_list'))
        self.assertTrue(Book.objects.filter(title='Automate the Boring Stuff').exists())

        # Verify it appears on the listing page
        list_response = self.client.get(reverse('book_list'))
        self.assertContains(list_response, 'Automate the Boring Stuff')
        self.assertContains(list_response, 'Al Sweigart')

    def test_add_book_post_invalid(self):
        data = {
            'title': '', # Title is required
            'author': 'Unknown',
            'year_published': 'not-a-year',
            'is_available': True
        }
        response = self.client.post(reverse('add_book'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertFormError(response.context['form'], 'title', 'This field is required.')
