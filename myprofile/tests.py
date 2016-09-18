from django.test import TestCase


class CollectionTest(TestCase):
    def test_settings(self):
        r = self.client.get('/settings/')
        self.assertEqual(r.status_code, 200)

