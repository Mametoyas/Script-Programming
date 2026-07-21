# Week 5 Snapshot – Data Structures: Dictionaries & Sets
**663380518-4 | นายจักรพรรดิ์ มั่งกูล**

---

## 1. Dictionaries (`dict`)

### Creating
```python
my_dict = {}                          # empty
my_dict = dict()                      # empty (alternative)
student = {"name": "Alice", "age": 20, "major": "CS"}
student = dict(name="Alice", age=20)  # keyword arguments
student = dict([("name", "Alice"), ("age", 20)])  # list of tuples
```

### Accessing Values
```python
student["name"]                       # KeyError if not found
student.get("name")                   # None if not found
student.get("city", "Not Available")  # default value if not found
```

### Adding & Modifying
```python
student["email"] = "alice@mail.com"   # add new key
student["age"] = 21                   # modify existing value
```

### Removing
```python
del student["age"]                    # delete by key
student.pop("age")                    # remove & return value
student.popitem()                     # remove & return last inserted pair
student.clear()                       # empty the dictionary
```

### Iterating
```python
for key in student:                   # keys (default)
for value in student.values():        # values
for key, value in student.items():    # key-value pairs
```

### Other Methods
```python
student.keys()     # view of all keys
student.values()   # view of all values
student.items()    # view of all key-value pairs
len(student)       # number of items
"name" in student  # check key existence
```

### Nested Dictionary
```python
students = {
    "S001": {"name": "Alice", "grade": "A"},
    "S002": {"name": "Bob",   "grade": "B"}
}
print(students["S001"]["name"])  # Alice
```

---

## 2. Sets (`set`)

### Creating
```python
my_set = set([1, 2, 2, 3])  # {1, 2, 3} — duplicates removed
unique_nums = {1, 2, 3}
empty_set = set()            # NOT {} — that creates an empty dict
```

### Adding & Removing
```python
my_set.add(4)        # add single element
my_set.remove(2)     # KeyError if not found
my_set.discard(2)    # no error if not found
my_set.pop()         # remove & return arbitrary element
my_set.clear()       # empty the set
```

### Set Operations
```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b   # union()               → {1, 2, 3, 4}
a & b   # intersection()        → {2, 3}
a - b   # difference()          → {1}
a ^ b   # symmetric_difference() → {1, 4}

a.issubset(b)    # True if a ⊆ b
a.issuperset(b)  # True if a ⊇ b
a.isdisjoint(b)  # True if a ∩ b = ∅
```

### Common Use Cases
```python
# Remove duplicates from list
unique = list(set([1, 2, 2, 3, 3]))

# Fast membership testing
blocked_ips = {"192.168.1.1", "10.0.0.1"}
if user_ip in blocked_ips:
    print("Blocked")
```

---

## 3. Choosing the Right Data Structure

| Structure | Ordered | Mutable | Duplicates | Best For |
|-----------|---------|---------|------------|----------|
| `list`    | ✅ | ✅ | ✅ | Sequences where order & change matter |
| `tuple`   | ✅ | ❌ | ✅ | Fixed collections (e.g. coordinates) |
| `dict`    | ✅* | ✅ | Keys: ❌ | Key-value lookups, structured records |
| `set`     | ❌ | ✅ | ❌ | Unique elements, membership testing, set math |

*Insertion-ordered since Python 3.7
