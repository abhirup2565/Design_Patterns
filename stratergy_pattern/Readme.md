# 🧠 Strategy Pattern

## 🏷️ Definition

> The **Strategy Pattern** is a behavioral design pattern that defines a family of algorithms (or behaviors), encapsulates each one, and makes them interchangeable.
> It allows an object’s behavior to be changed at runtime without modifying its class.

In simpler terms —
instead of hardcoding how an object behaves, you **delegate** that behavior to another object (called a *strategy*) that can be swapped dynamically.

---

## 🧩 Problem It Solves

Without the Strategy Pattern, you often end up with:

* Long **if-else or switch** statements deciding behavior.
* **Duplicate logic** across subclasses.
* Violation of the **Open/Closed Principle** (every time a new behavior is added, you modify existing code).

Example problem:

```bash
if duck_type == "mallard":
    fly_with_wings()
elif duck_type == "model":
    no_fly()
```

This code is rigid — adding a new behavior means editing existing classes.
The Strategy Pattern fixes this by **separating behaviors into their own classes** and plugging them in when needed.

---

## 💡 Intuition Behind It

Think of Strategy Pattern as **"Behavior injection"**.

Instead of saying:

> “A duck *knows* how to fly and quack.”

we say:

> “A duck *has a* fly behavior and a quack behavior.”

So each duck delegates its behavior to those strategy objects.
That means we can easily **change how it behaves at runtime**:

```bash
model_duck.fly_behavior = FlyRocketPowered()
```

Now, the model duck can fly like a rocket — without changing the `Duck` class itself.

---

## 🚴 Real-Life Analogy

Imagine **a driver and a vehicle**:

* The **Driver** represents your main object.
* The **Vehicle** represents the strategy.

A driver can choose **how to travel** — by car, bike, or airplane.

```bash
Driver (context)
 ├── Car (strategy)
 ├── Bike (strategy)
 └── Airplane (strategy)
```

If the driver switches from a car to a bike, the **driving behavior changes**,
but the **driver remains the same** — that’s exactly how the Strategy Pattern works.

---

## 🧠 Summary Table

| Concept               | Description                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| **Pattern Type**      | Behavioral                                                                                      |
| **Purpose**           | To define a family of algorithms/behaviors and make them interchangeable                        |
| **Solves**            | Rigid code with conditional logic for behavior                                                  |
| **Principle**         | Favor *composition* over *inheritance*                                                          |
| **Example Use Cases** | Payment methods, sorting algorithms, game AI, compression techniques, authentication strategies |
---

---

## 🔑 Key Takeaways

* Use Strategy when:

  * You have multiple interchangeable algorithms.
  * You want to avoid conditional logic.
  * You need to change behavior at runtime.
* Promotes **flexibility**, **reusability**, and **clean design**.
* Implements **composition over inheritance**.


