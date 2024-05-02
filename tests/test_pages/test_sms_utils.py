import unittest
from src.pages.sms.utils import content_preview




class TestSMSUtils(unittest.TestCase):
    def test_content_preview_none(self):
        self.assertEqual(content_preview(None), "")
    
    def test_content_preview_int(self):
        self.assertEqual(content_preview(1), "")

    def test_content_preview_space(self):
        self.assertEqual(content_preview(" "), " ")
    
    def test_content_preview_length(self):
        self.assertEqual(
            len(content_preview("asdfghjklqwertohuihdfghghjkvbnm,mnbvdfghjjjnbbnuuibniubnuinibyubyubjkxcvbnm,wertyuifghjklvbnmdfvbhnjmvbnu")), 40)
    
    
    




if __name__ == '__main__':
    unittest.main()