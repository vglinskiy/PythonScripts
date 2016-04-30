#!/usr/bin/env python

import re
import sys
max4byte_asn="4294967295"
max2byte_asn="65536"
reserved_asn="23456"
asplain_pattern=re.compile("^(\d+)$")
asdot_pattern=re.compile("^(\d+)\.(\d+)$")

try:
  asn=sys.argv[1]
except:
  asn=raw_input("Enter AS number: ")

if re.match(asdot_pattern, asn):
  split_pattern=re.compile("\.")
  (byte12, byte34)=re.split(split_pattern,asn)
  if int(byte12) > int(max2byte_asn) or int(byte34) > int(max2byte_asn):
    print "In asdot notation neither 2 bytes can exceed {0}".format(max2byte_asn)
    sys.exit(2)
  asplain=int(byte12)*int(max2byte_asn)+int(byte34)
  print "asplain notation: {0}".format(asplain)
elif re.match(asplain_pattern, asn):
  if int(asn) > int(max4byte_asn):
    print "4-byte AS number can not exceed {0}".format(max4byte_asn)
    sys.exit(2)
  elif int(asn) == int(reserved_asn):
    print "{0} is reserved AS number".format(reserved_asn)
    sys.exit(2)
  (part1, part2)=divmod(int(asn), int(max2byte_asn))
  asdot=str(part1)+"."+str(part2)
  print "asdot notation: {0}".format(asdot)
else:
  print "I do not recognize this type of ASN\n"
