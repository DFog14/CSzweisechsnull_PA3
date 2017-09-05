from __future__ import division

class deleted: pass
class empty: pass

class HashTable:
    def __init__(self, b):
        self.buckets = [empty for _ in range(b)]
        self.num_items = 0
        self.probes = 0

    def makenull(self):
        for i in range(len(self.buckets)):
            self.buckets[i] = empty

    def locate(self, x):
        initial = hash(x) % len(self.buckets)
        i = 0
        while True:
            self.probes += 1
            bucket = (initial + i) % len(self.buckets)
            value = self.buckets[bucket]
            if i >= len(self.buckets) or value == x or value == empty or value == deleted:
                return bucket
            i += 1

    def locate1(self, x):
        initial = hash(x) % len(self.buckets)
        i = 0
        while True:
            self.probes += 1
            bucket = (initial + i) % len(self.buckets)
            value = self.buckets[bucket]
            if i >= len(self.buckets) or value == x or value == empty or value == deleted:
                return bucket
            i += 1
    
    def member(self, x):
        return self.buckets[self.locate(x)] == x

    def insert(self, x):
        if self.buckets[self.locate(x)] == x:
            return

        bucket = self.locate1(x)
        if self.buckets[bucket] == empty or self.buckets[bucket] == deleted:
            self.buckets[bucket] = x
            self.num_items += 1
        else:
            raise Exception('table is full (%d/%d values)' % (self.num_items, len(self.buckets)))

    def delete(self, x):
        bucket = self.locate(x)
        if self.buckets[bucket] == x:
            self.buckets[bucket] = deleted
            self.num_items -= 1

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

for i in range(100):
    t = HashTable(100)
    for j in range(2000):
        if t.num_items == 100:
            break
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

with open('closed-insert.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(('load factor (a)', 'actual probes', 'expected probes'))
    for a in sorted(insert_data):
        w.writerow((a, mean(insert_data[a]), 1 + a))

with open('closed-delete.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(('load factor (a)', 'actual probes', 'expected probes'))
    for a in sorted(delete_data):
        w.writerow((a, mean(delete_data[a]), 1 + a))
