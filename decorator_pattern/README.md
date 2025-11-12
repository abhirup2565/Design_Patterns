## 🧩 1. Definition — *Decorator Pattern*

The **Decorator Pattern** lets you **dynamically add new behavior** to an object **without modifying its structure or class**.

In simpler terms:

> Instead of changing the original class code, we “wrap” it inside another class (a *decorator*) that adds new functionality before or after calling the original one.

---

## ⚙️ 2. Problem It Solves

Imagine you have a class like `Coffee`.
Now, your system wants to support **adding milk**, **adding sugar**, **adding whipped cream**, etc.

You could:

* Keep modifying the `Coffee` class to add new features (bad idea – breaks Open/Closed Principle)
* OR use **inheritance** (`MilkCoffee`, `SugarCoffee`, `MilkSugarCoffee`...) — but that explodes combinatorially 😩

**Decorator pattern fixes that** by letting you “wrap” your base object with decorators that add functionality dynamically at runtime.

---

## 💡 3. Intuition Behind It

It’s like **wrapping gifts** 🎁 —
You start with a plain box (base object), then you wrap it with layers of paper, ribbons, etc. (decorators) that *enhance its presentation* — but the **original gift** is still the same inside.

Or in coding terms:
A decorator class **“wraps”** another class, adding behavior *before/after delegating* the main call.

---

## ⚡ 4. Real-Life Analogy

* A **base pizza** costs ₹200.
* Add **extra cheese** → +₹50
* Add **olives** → +₹30

You don’t create new pizza subclasses every time; you just **decorate** the base pizza with new layers of toppings dynamically.

---

## 🧱 5. Pythonic Angle

In Python, **functions themselves can be decorated** — thanks to the built-in `@decorator` syntax.

So, this pattern is **natively supported in Python** both at function and class level.

### Example (Functional version)

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(2, 3)
```

Output:

```
Calling add
add returned 5
```

This is literally the **Decorator Pattern** at function level.

---

