from django.test import TestCase


class CollectionTest(TestCase):
    def test_contact(self):
        r = self.client.get('/contact/')
        self.assertEqual(r.status_code, 200)
