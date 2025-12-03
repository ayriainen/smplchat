import unittest

from smplchat.client_list import KeepaliveList
from smplchat.utils import generate_uid

class TestKeepaliveList(unittest.TestCase):

    def test_init(self):
        KeepaliveList()

    def test_add(self):
        kal = KeepaliveList()
        kal.add(generate_uid())
        kal.add(generate_uid())
        kal.add(generate_uid())

    def test_seen_count(self):
        kal = KeepaliveList()
        u1 = generate_uid()
        u2 = generate_uid()
        u3 = generate_uid()
        kal.add(u1)
        kal.add(u2)
        kal.add(u1)
        kal.add(u1)
        self.assertEqual(kal.seen_count(u1), 3)
        self.assertEqual(kal.seen_count(u2), 1)
        self.assertEqual(kal.seen_count(u3), 0)
