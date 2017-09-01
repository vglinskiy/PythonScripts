#!/usr/bin/env python
import unittest
import asnconverter


class TestAsnConverter(unittest.TestCase):
    def test_check_max_4byte_value(self):
        self.assertRaises(Exception, asnconverter.check_value,
                          4294967300, 4294967295)

    def test_check_max_2byte_value(self):
        result = asnconverter.check_value(10, 65536)
        self.assertIs(result, True)

    def test_to_asplain(self):
        result = asnconverter.to_asplain(0, 1, 65536)
        self.assertIs(result, 1)

    def test_to_asdot(self):
        result = asnconverter.to_asdot(1, 65536)
        self.assertEqual(result, '0.1')

suite = unittest.TestLoader().loadTestsFromTestCase(TestAsnConverter)
unittest.TextTestRunner(verbosity=2).run(suite)
