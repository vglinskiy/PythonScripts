#!/usr/bin/env python

import re
import sys
import argparse
max4byte_asn = 4294967295
max2byte_asn = 65535
asplain_pattern = re.compile("^(\d+)$")
asdot_pattern = re.compile("^(\d+)\.(\d+)$")


def check_value(my_asn, max_asn):
    """
    Checking if ASN number is within RFC limits
    """
    if int(my_asn) > max_asn:
        raise ValueError("{} exceeds {}".format(my_asn, max_asn))
    else:
        return True


def to_asplain(byte12, byte34, max2byte_asn):
    return int(byte12)*int(max2byte_asn)+int(byte34)


def to_asdot(asn, max2byte_asn):
    (part1, part2) = divmod(int(asn), int(max2byte_asn))
    return str(part1)+"."+str(part2)


def main():
    parser = argparse.ArgumentParser(description="Convert 4-byte Autonomous System \
                  Number in asplain notation to asdot or asdot to asplain")
    parser.add_argument("asn", help="Autonomous System Number",
                        metavar="<AS Number>")
    args = parser.parse_args()
    if re.match(asdot_pattern, args.asn):
        (byte12, byte34) = args.asn.split(".")
        for my_asn in (byte12, byte34):
            try:
                check_value(my_asn, max2byte_asn)
            except Exception as err:
                print err
                sys.exit(1)
        asplain = to_asplain(byte12, byte34, max2byte_asn+1)
        print "asplain notation: {0}".format(asplain)
    elif re.match(asplain_pattern, args.asn):
        try:
            check_value(args.asn, max4byte_asn)
        except Exception as err:
            print err
            sys.exit(1)
        asdot = to_asdot(args.asn, max2byte_asn)
        print "asdot notation: {0}".format(asdot)
    else:
        print "I do not recognize this type of ASN\n"

if __name__ == "main":
    main()
