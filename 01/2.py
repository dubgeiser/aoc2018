#!/usr/bin/env python3


with open("input") as data:
    frequency_changes = [int(l.strip()) for l in data]

recorded = set()
f = 0
recorded.add(f)
found = False
while not found:
    for c in frequency_changes:
        f += c
        if f in recorded:
            found = True
            break
        recorded.add(f)


print()
print(f)
