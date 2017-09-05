from __future__ import division

class Item:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class HashTable:
    def __init__(self, b):
        self.buckets = [None for _ in range(b)]
        self.num_items = 0
        self.probes = 0

    def makenull(self):
        for i in range(len(self.buckets)):
            self.buckets[i] = None

    def member(self, x):
        current = self.buckets[hash(x) % len(self.buckets)]
        while current is not None:
            self.probes += 1
            if current.head == x:
                return True
            else:
                current = current.tail
        return False

    def insert(self, x):
        if not self.member(x):
            bucket = hash(x) % len(self.buckets)
            self.buckets[bucket] = Item(x, self.buckets[bucket])
            self.num_items += 1

    def delete(self, x):
        bucket = hash(x) % len(self.buckets)
        if self.buckets[bucket] is not None:
            self.probes += 1
            if self.buckets[bucket].head == x:
                self.buckets[bucket] = self.buckets[bucket].tail
            else:
                current = self.buckets[bucket]
                while current.tail != None:
                    self.probes += 1
                    if current.tail.head == x:
                        current.tail = current.tail.tail
                        self.num_items -= 1
                        return
                    else:
                        current = current.tail

    def load_factor(self):
        return self.num_items/len(self.buckets)

import collections
import csv
import math
import random

def mean(xs):
    return math.fsum(xs) / len(xs)

insert_data = collections.defaultdict(list)
delete_data = collections.defaultdict(list)

for i in range(2000):
    t = HashTable(100)
    for j in range(2000):
        value = random.randint(0, 1000000)

        load_factor = t.load_factor()
        t.probes = 0
        t.insert(value)
        insert_data[t.load_factor()].append(t.probes)

    for j in range(2000):
        value = random.randint(0, 1000000)

        load_factor = t.load_factor()
        t.probes = 0
        t.delete(value)
        delete_data[t.load_factor()].append(t.probes)

with open('open-insert.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(('load factor (a)', 'actual probes', 'expected probes'))
    for a in sorted(insert_data):
        w.writerow((a, mean(insert_data[a]), 1 + a))

with open('open-delete.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(('load factor (a)', 'actual probes', 'expected probes'))
    for a in sorted(delete_data):
        w.writerow((a, mean(delete_data[a]), 1 + a))
