import unittest

from core.downloader import HTTPDownloader


class TestHTTP(unittest.TestCase):

    def test_init(self):
        downloader = HTTPDownloader("localhost", 500)
        self.assertEqual(downloader.url, "localhost")
        self.assertEqual(downloader.size, 500)

    def test_get_chunk(self):
        downloader = HTTPDownloader("localhost", 500)
        self.assertEqual(downloader.url, "localhost")
        self.assertEqual(downloader.size, 500)


if __name__ == '__main__':
    unittest.main()
