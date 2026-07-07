# 📸 Week 3 Snapshot — Control Flow: Loops & Generators

## สัปดาห์ที่ 3: การควบคุมการทำงานด้วยลูป (Loops)

---

## 1. ความจำเป็นของลูป (The Need for Loops)

ลูปช่วยให้เราทำงานซ้ำ ๆ โดยอัตโนมัติ แทนที่จะเขียนโค้ดซ้ำหลายบรรทัด

** without loop (ไม่มีลูป — ยุ่งยาก):**
```python
print(1)
print(2)
print(3)
print(4)
print(5)
# ... ต้องพิมพ์ถึง 100 !
```

** with loop (ใช้ลูป — สะอาดและยืดหยุ่น):**
```python
for i in range(1, 101):
    print(i)
```

---

## 2. `for` Loop

### ไวยากรณ์พื้นฐาน
```python
for item in sequence:
    # ทำอะไรกับ item
```

### 2.1 ฟังก์ชัน `range()`

```python
# range(stop) — เริ่มจาก 0 ถึง stop-1
for i in range(5):
    print(i)          # 0, 1, 2, 3, 4

# range(start, stop) — เริ่มจาก start ถึง stop-1
for i in range(1, 11):
    print(i)          # 1, 2, 3, ..., 10

# range(start, stop, step) — เพิ่มทีละ step
for i in range(0, 11, 2):
    print(i)          # 0, 2, 4, 6, 8, 10

# นับถอยหลัง
for i in range(10, 0, -1):
    print(i)          # 10, 9, 8, ..., 1
```

### 2.2 การวนลูปผ่าน String

```python
my_string = "Python"
for char in my_string:
    print(f"Character: {char}")
# Output: P, y, t, h, o, n
```

### 2.3 การคำนวณสะสม

```python
total_sum = 0
for i in range(1, 6):   # 1 + 2 + 3 + 4 + 5
    total_sum += i
print(f"Sum: {total_sum}")   # 15
```

---

## 3. `while` Loop

### ไวยากรณ์พื้นฐาน — ทำงานซ้ำตราบใดที่เงื่อนไขเป็น True

```python
# ตัวอย่าง: นับถอยหลัง
count = 5
while count > 0:
    print(f"Count: {count}")
    count -= 1          # สำคัญ! ต้องอัปเดตค่าเพื่อไม่ให้เป็น infinite loop
print("Countdown finished!")
```

### การตรวจสอบอินพุตจากผู้ใช้

```python
user_input = ""
while not (user_input == "yes" or user_input == "no"):
    user_input = input("Please enter 'yes' or 'no': ").lower()
print(f"You entered: {user_input}")
```

### ⚠️ Infinite Loop — ข้อควรระวัง!
```python
# ❌ อันตราย! ลูปนี้จะทำงานตลอดไป因为没有อัปเดต counter
# counter = 0
# while counter < 5:
#     print(counter)
#     # ลืม counter += 1 → infinite loop!
```

---

## 4. Loop Control Statements

### `break` — ออกจากลูปทันที

```python
# เกมทายตัวเลข — ออกจากลูปเมื่อทายถูก
secret_number = 7
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input(f"Guess (1-10) [{attempts+1}/{max_attempts}]: "))
    attempts += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break                     # ← ออกจากลูปทันที
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    # else จะทำงานเมื่อลูปจบโดยไม่เจอ break
    print(f"Out of attempts. The number was {secret_number}.")
```

### `continue` — ข้าม iteration ปัจจุบัน ไป iteration ถัดไป

```python
# พิมพ์เฉพาะเลขคู่ (ข้ามเลขคี่)
for i in range(1, 11):
    if i % 2 != 0:    # ถ้าเป็นเลขคี่
        continue      # ← ข้ามไป iteration ถัดไป
    print(f"Even number: {i}")
# Output: 2, 4, 6, 8, 10
```

---

## 5. Nested Loops (ลูปซ้อนลูป)

ลูปชั้นในจะทำงานจนครบ **ทุกรอบ** สำหรับลูปชั้นนอก **แต่ละรอบ**

### สร้างสี่เหลี่ยม
```python
size = 5
for row in range(size):          # ลูปนอก: แถว
    for col in range(size):      # ลูปใน: คอลัมน์
        print("* ", end="")      # ไม่ขึ้นบรรทัดใหม่
    print()                      # ขึ้นบรรทัดใหม่เมื่อจบแถว
```

Output:
```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### สามเหลี่ยมมุมฉาก
```python
height = 5
for row in range(1, height + 1):
    for col in range(row):       # พิมพ์ดาวจำนวนเท่ากับ row
        print("* ", end="")
    print()
```

Output:
```
*
* *
* * *
* * * *
* * * * *
```

### สามเหลี่ยมกลับหัว
```python
for row in range(height, 0, -1):
    for col in range(row):
        print("* ", end="")
    print()
```

Output:
```
* * * * *
* * * *
* * *
* *
*
```

### 🧪 ตารางสูตรคูณ 12×12 (ประยุกต์ใช้ nested loops)

```python
print("12x12 Multiplication Table:")
for i in range(1, 13):           # ลูปนอก: แถว
    for j in range(1, 13):       # ลูปใน: คอลัมน์
        print(f"{i*j:4d}", end="")
    print()                      # ขึ้นบรรทัดใหม่
```

---

## 6. Advanced Topic: Generators (ตัวสร้างมูลค่า)

### Generator Function — ใช้ `yield` แทน `return`

```python
def function():
    for x in range(10):
        yield x ** 2             # ให้ค่าทีละตัว ไม่เก็บทั้งหมดในหน่วยความจำ

g = function()
for val in g:
    print(f"Received {val}")     # 0, 1, 4, 9, ..., 81
```

### Generator Expression — คล้าย list comprehension แต่ใช้วงเล็บ

```python
squares = (x**2 for x in range(10))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### คุณสมบัติสำคัญของ Generator

```python
# 1. ใช้หน่วยความจำน้อย — ไม่ต้องเก็บค่าทั้งหมดไว้ใน list
sum_squares = sum(x**2 for x in range(1000000))  # ทำงานได้ ไม่มีปัญหาเรื่อง memory

# 2. สร้าง infinite sequence ได้
def integers_starting_from(n):
    while True:
        yield n
        n += 1

natural_numbers = integers_starting_from(1)

# 3. Generator จะถูก consume ได้ครั้งเดียว
g = (x**2 for x in range(5))
print(list(g))  # [0, 1, 4, 9, 16]
print(list(g))  # [] — ว่าง เพราะถูก consume ไปแล้ว! ต้องสร้างใหม่
```

### Fibonacci ด้วย Generator

```python
import itertools

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

first_10 = list(itertools.islice(fibonacci(), 10))
print(first_10)  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# หา Fibonacci ตัวที่ 99
def nth_fib(n):
    return next(itertools.islice(fibonacci(), n - 1, n))
print(nth_fib(99))  # 354224848179261915075
```

### `yield from` — ยืมค่าจาก iterable อื่น

```python
def foob(x):
    yield from range(x * 2)
    yield from range(2)

print(list(foob(5)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
```

---

## 📋 สรุป Loop Control Statements

| คำสั่ง | การทำงาน |
|--------|----------|
| `break` | ออกจากลูปทันที (ใช้ใน `for` และ `while`) |
| `continue` | ข้าม iteration ปัจจุบัน ไป iteration ถัดไป |
| `else` (กับลูป) | ทำงานเมื่อลูปจบโดยไม่เจอ `break` |

---

## 🔗 เนื้อหาที่เกี่ยวข้อง

- 📄 [Week 3: Control Flow: Loops (PDF)](./papers/Week%203_%20Control%20Flow_%20Loops.pdf)
- 📄 [Advanced: Generators (PDF)](./papers/p3.%20Generators.pdf)
- 📓 [Lab3.ipynb](./Lab3.ipynb)
- 📝 [Recap Week 2](./Recap_Week2_663380518_4.md)

---

*จัดทำขึ้นเพื่อการทบทวนเนื้อหา Week 3 — Control Flow: Loops & Generators*
