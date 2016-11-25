import unittest
from unittest.mock import patch
from core.downloader import HTTPDownloader

CHUNK = ["1"] * 10


class TestHTTP(unittest.TestCase):

    def setUp(self):
        self.size = 500
        self.downloader = HTTPDownloader("http://localhost", self.size)

    def test_init(self):
        self.assertEqual(self.downloader.url, "http://localhost")
        self.assertEqual(self.downloader.size, self.size)

    def test_range(self):
        self.assertEqual(self.downloader._range[0], 0)
        self.assertEqual(self.downloader._range[1], self.size - 1)

    def test_request(self):
        self.assertEqual(self.downloader.build_request().headers[0], 1)

    @patch('core.downloader.HTTPDownloader.get_response', return_value=CHUNK)
    def test_new_range(self, read):
        self.downloader.download_chunk()
        self.assertEqual(self.downloader._range[0], len(CHUNK))
        self.assertEqual(
            self.downloader._range[1], len(CHUNK) + self.size - 1)


if __name__ == '__main__':
    unittest.main()
