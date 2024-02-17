#!/usr/bin/python3
import sys
import re

if len(sys.argv) < 2:
	print("Usage: python h_dump.py <filename>")
	sys.exit(1)

with open(sys.argv[1]) as f:
	array = [row.strip() for row in f]

number = 0  # Initialize the number variable outside the loop

for line in array:
	if re.match("Packet", line):
		print(format((number * 16), '04x') + "\t" + line)  # Add format() function call
	if re.match("^[a-f0-9]", line):
		print(format((number * 16), '04x') + "\t" + line)  # Add format() function call
		number += 1  # Increment the number variable

