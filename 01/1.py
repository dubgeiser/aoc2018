#!/usr/bin/env python3


with open("input") as data:
    frequency_changes = [int(l.strip()) for l in data]

f = 0
for c in frequency_changes:
    f += c

print()
print(f)
