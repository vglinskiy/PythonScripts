#!/usr/bin/env python

import unittest
from ASNConverter import ASNConverter


class TestASNConverter(unittest.TestCase):
    def setUp(self):
        self.asnconverter = ASNConverter()

    def test_is_asdot(self):
        self.asnconverter.my_asn = "1.0"
        result = self.asnconverter._is_asdot()
        self.assertIs(result, True)

    def test_is_plain(self):
        self.asnconverter.my_asn = "10"
        result = self.asnconverter._is_asplain()
        self.assertIs(True, result)

    def test_check_value_Exception(self):
        self.asnconverter.part1 = 70000
        self.asnconverter.part2 = 0
        self.asnconverter._max_asn = self.asnconverter.max2byte_asn
        self.assertRaises(Exception, self.asnconverter._check_value)

    def test_check_value_True(self):
        self.asnconverter.part1 = 65536
        self.asnconverter.part2 = 0
        self.asnconverter._max_asn = self.asnconverter.max4byte_asn
        result = self.asnconverter._check_value()
        self.assertEqual(result, True)

    def test_to_asdot(self):
        self.asnconverter.part1 = 65536
        self.asnconverter.part2 = 0
        self.asnconverter._max_asn = self.asnconverter.max4byte_asn
        result = self.asnconverter._to_asdot()
        self.assertEqual(result, "1.0")

    def test_to_asplain(self):
        self.asnconverter.part1 = "1"
        self.asnconverter.part2 = "0"
        self.asnconverter._max_asn = self.asnconverter.max2byte_asn
        result = self.asnconverter._to_asplain()
        self.assertEqual(result, 65536)

    def test_convert_Exception(self):
        self.assertRaises(Exception, self.asnconverter.convert, "123.456.789")
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestASNConverter)
unittest.TextTestRunner(verbosity=2).run(suite)
