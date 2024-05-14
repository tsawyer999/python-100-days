import unittest
from Day008.Utils.EncryptionUtils import EncryptionUtils


class DecryptTests(unittest.TestCase):
    def test_decrypt_a(self):
        result = EncryptionUtils.decrypt("a", 1)
        self.assertEqual("z", result)


if __name__ == '__main__':
    unittest.main()
