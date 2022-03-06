from unittest import TestCase

from CountDeliveryOrders import countOrders


class Test(TestCase):
    def test_count_orders(self):
        self.assertEqual(6, countOrders(2))
        self.assertEqual(90, countOrders(3))
