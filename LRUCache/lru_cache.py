
from collections import OrderedDict

class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            # Move the accessed item to the end
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            # Update the value and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item (first item in the OrderedDict)
                self.cache.popitem(last=False)
            self.cache[key] = value

    def __str__(self):
        return str(self.cache)
    
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))    # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(4))
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Test case 1: Basic operations
cache = LRU_Cache(3)
cache.set(1, 10)
cache.set(2, 20)
cache.set(3, 30)
print(cache.get(2))  # Output: 20
cache.set(4, 40)
print(cache.get(1))  # Output: -1 (not found)
print(cache.get(3))  # Output: 30
print(cache.get(4))  # Output: 40

# Test case 2: Cache with capacity 1
cache = LRU_Cache(1)
cache.set(1, 10)
print(cache.get(1))  # Output: 10
cache.set(2, 20)
print(cache.get(1))  # Output: -1 (not found)
print(cache.get(2))  # Output: 20

# Test case 3: Empty cache
cache = LRU_Cache(2)
print(cache.get(1))  # Output: -1 (not found)
cache.set(1, 10)
print(cache.get(1))  # Output: 10
print(cache.get(2))  # Output: -1 (not found)

# Test case 4: Large capacity
cache = LRU_Cache(1000)
for i in range(1000):
    cache.set(i, i * 10)
print(cache.get(500))  # Output: 5000
print(cache.get(1001))  # Output: -1 (not found)

# Test case 5: Very large values
large_cache = LRU_Cache(10**6)
for i in range(10**6):
    large_cache.set(i, i)
print(large_cache.get(0))  # Output: 0
print(large_cache.get(10**6))  # Output: -1