import unittest
from Day008.Utils.EncryptionUtils import EncryptionUtils


class EncryptTests(unittest.TestCase):
    def test_encrypt_a(self):
        result = EncryptionUtils.encrypt("z", 1)
        self.assertEqual("a", result)


if __name__ == '__main__':
    unittest.main()
