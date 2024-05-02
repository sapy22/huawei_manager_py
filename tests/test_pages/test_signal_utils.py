import unittest
from src.pages.signal.tabs.monitor.utils import split_tx, split_k, split_d
from src.pages.signal.tabs.statistics.utils import convert_bytes, convert_to_mb




class TestSignalMonitorUtils(unittest.TestCase):
    def test_split_tx_valid(self):
        self.assertEqual(split_tx("PPusch:0dBm PPucch:0dBm PSrs:0dBm PPrach:0dBm"), "0dBm/0dBm")
        self.assertEqual(split_tx("PPusch:0dBm PPucch:0dBm PSrs:0dBm"), "0dBm/0dBm")
        self.assertEqual(split_tx("PPusch:0dBm PPucch:0dBm"), "0dBm/0dBm")
    
    def test_split_tx_invalid(self):
        self.assertEqual(split_tx("PPusch 0dBm PPucch 0dBm PSrs 0dBm PPrach 0dBm"), "")
        self.assertEqual(split_tx("PPusch 0dBm PPucch 0dBm PSrs 0dBm"), "")
        self.assertEqual(split_tx("PPusch 0dBm PPucch 0dBm"), "")
        self.assertEqual(split_tx("abc"), "")
        self.assertEqual(split_tx(""), "")
        self.assertEqual(split_tx(" "), "")
        self.assertEqual(split_tx(1), "")
        self.assertEqual(split_tx(None), "")
    

    def test_split_k_valid(self):
        self.assertEqual(split_k("1850000kHz"), 1850)
        self.assertEqual(split_k("1850000"), 1850)
        self.assertEqual(split_k("1850"), 2)
    
    def test_split_k_invalid(self):
        self.assertEqual(split_k("1850000Hz"), 0)
        self.assertEqual(split_k("abc"), 0)
        self.assertEqual(split_k(""), 0)
        self.assertEqual(split_k(" "), 0)
        self.assertEqual(split_k(1), 0)
        self.assertEqual(split_k(None), 0)
    

    def test_split_d_valid(self):
        self.assertEqual(split_d("18.0dbm"), 18)
        self.assertEqual(split_d("-18.0dbm"), -18)
        self.assertEqual(split_d("18db"), 18)
        self.assertEqual(split_d("-18db"), -18)
        self.assertEqual(split_d("18.0000"), 18)
        self.assertEqual(split_d("-18.0000"), -18)
        self.assertEqual(split_d("18,000"), 18000)
    
    def test_split_d_invalid(self):
        self.assertEqual(split_d("abc"), 0)
        self.assertEqual(split_d(""), 0)
        self.assertEqual(split_d(" "), 0)
        self.assertEqual(split_d(1), 0)
        self.assertEqual(split_d(None), 0)


class TestSignalStatisticsUtils(unittest.TestCase):
    def test_convert_bytes(self):
        self.assertEqual(convert_bytes("111111111"), "106.0 MB")

    def test_convert_bytes_int(self):
        self.assertEqual(convert_bytes(111111111), "106.0 MB")
    
    def test_convert_bytes_none(self):
        self.assertEqual(convert_bytes(None), "")
    

    def test_convert_to_mb(self):
        self.assertEqual(convert_to_mb("1111111"), 8.48)

    def test_convert_to_mb_int(self):
        self.assertEqual(convert_to_mb(1111111), 8.48)
    
    def test_convert_to_mb_none(self):
        self.assertEqual(convert_to_mb(None), 0.0)




if __name__ == '__main__':
    unittest.main()