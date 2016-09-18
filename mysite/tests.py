from django.test import TestCase


class CollectionTest(TestCase):
    def test_rfund(self):
        r = self.client.get('/refund/')
        self.assertEqual(r.status_code, 200)

    def test_tandc(self):
        r = self.client.get('/tandc/')
        self.assertEqual(r.status_code, 200)
