#!/usr/bin/env python

import re
import sys
import argparse


class ASNConverter(object):
    def __init__(self):
        self.max4byte_asn = 4294967295
        self.max2byte_asn = 65535
        self.asplain_pattern = re.compile("^(\d+)$")
        self.asdot_pattern = re.compile("^(\d+)\.(\d+)$")

    def _check_value(self):
        for _value in (self.part1, self.part2):
            if int(_value) > self._max_asn:
                raise ValueError("{} exceeds {}".format(_value, self._max_asn))
            else:
                return True

    def _is_asdot(self):
        if re.match(self.asdot_pattern, self.my_asn):
            return True
        else:
            return False

    def _is_asplain(self):
        if re.match(self.asplain_pattern, self.my_asn):
            return True
        else:
            return False

    def _to_asplain(self):
        try:
            self._check_value()
        except Exception as err:
            print err
            sys.exit(1)
        converted_asn = int(self.part1)*(self.max2byte_asn+1)+int(self.part2)
        return converted_asn

    def _to_asdot(self):
        try:
            self._check_value()
        except Exception as err:
            print err
            sys.exit(1)
        (byte34, byte12) = divmod(int(self.part1), self.max2byte_asn+1)
        converted_asn = str(byte34)+"."+str(byte12)
        return converted_asn

    def convert(self, my_asn):
        self.my_asn = my_asn
        if self._is_asdot():
            (self.part1, self.part2) = self.my_asn.split(".")
            self._max_asn = self.max2byte_asn
            result_asn = self._to_asplain()
            return result_asn
        elif self._is_asplain():
            (self.part1, self.part2) = (self.my_asn, 0)
            self._max_asn = self.max4byte_asn
            result_asn = self._to_asdot()
            return result_asn
        else:
            raise ValueError("I do not recognize this format"
                             .format(self.my_asn))


def main():
    parser = argparse.ArgumentParser(description="Convert 4-byte Autonomous \
              System Number in asplain notation to asdot or asdot to asplain")
    parser.add_argument("asn", help="Autonomous System Number",
                        metavar="<AS Number>")
    args = parser.parse_args()
    converter = ASNConverter()
    try:
        output = converter.convert(args.asn)
    except Exception as err:
        print err
        sys.exit(1)
    print "Converted value is {}".format(output)


if __name__ == '__main__':
    main()
