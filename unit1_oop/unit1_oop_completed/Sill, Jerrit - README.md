# Unit 1 Discussion: Python OOP, Namespaces, and Copying

\---

## 📌 Overview

For this assignment, I implemented a smart-home device hierarchy modeled after home automation platforms like [Home Assistant](https://www.home-assistant.io/). The goal was to explore core Python OOP concepts, including class inheritance, class vs. instance namespaces, standard library object copying (`copy`), and defensive error handling.

\---

## 🎯 Learning Objectives

* \[x] Design parent and child class structures (`SmartDevice` $\\rightarrow$ `Thermostat`)
* \[x] Use `super()` to extend base functionality without repeating code
* \[x] Inspect class and instance namespaces (`\\\_\\\_dict\\\_\\\_`)
* \[x] Demonstrate reference sharing vs. value duplication in `copy.copy()` vs. `copy.deepcopy()`
* \[x] Apply OOP design principles (encapsulation, abstraction, code reusability)

\---

## 🏗️ Implementation Summary

### Class Diagram / Hierarchy

```
               ┌────────────────────────┐
               │      SmartDevice       │
               ├────────────────────────┤
               │ - device\\\_count (class) │
               │ - name                 │
               │ - location             │
               │ - status               │
               ├────────────────────────┤
               │ + turn\\\_on()            │
               │ + turn\\\_off()           │
               │ + get\\\_info()           │
               └───────────┬────────────┘
                           │
                           │  inherits
                           ▼
               ┌────────────────────────┐
               │       Thermostat       │
               ├────────────────────────┤
               │ - supported\\\_modes (cl) │
               │ - target\\\_temp          │
               │ - mode                 │
               │ - schedule (dict)      │
               ├────────────────────────┤
               │ + set\\\_mode()           │
               │ + set\\\_temperature()    │
               │ + get\\\_info() (overridden)│
               └────────────────────────┘
```

### Key Modules Implemented

#### 1\. Base Class: `SmartDevice`

* Acts as the parent class for all network-attached hardware.
* **Class Variable:** `device\\\_count` tracks global instantiation across the entire runtime.
* **Instance Attributes:** `name`, `location`, `status` (`'on'` / `'off'`).
* **Methods:** `turn\\\_on()`, `turn\\\_off()`, and `get\\\_info()` returning summary telemetrics.

#### 2\. Subclass: `Thermostat`

* Inherits directly from `SmartDevice`.
* **Class Variable:** `supported\\\_modes = \\\['heat', 'cool', 'eco', 'off']`.
* **Instance Attributes:** Adds `target\\\_temp`, `mode`, and a nested `schedule` dict containing daily profile lists.
* **Method Overriding:** Overrides `get\\\_info()` using `super().get\\\_info()` to concatenate base device details with thermostat-specific settings.

#### 3\. Namespace Resolution \& Inspection

To inspect how Python resolves scoping:

```python
# Modifying instance dict vs class dict
t1 = Thermostat("Living Room", "Main Floor")
t2 = Thermostat("Bedroom", "Upstairs")

# Shared class attribute
print(Thermostat.supported\\\_modes) # Shared across all instances

# Instance attribute dynamic binding
t1.custom\\\_offset = 1.5 
# t1.\\\_\\\_dict\\\_\\\_ now contains 'custom\\\_offset'
# t2.\\\_\\\_dict\\\_\\\_ remains untouched
```

#### 4\. Object Copying (`copy.copy` vs `copy.deepcopy`)

Tested standard library behavior on complex nested structures (`schedule = {"weekday": \\\[68, 72]}`):

|Copy Type|Method|Nested Object Memory Address (`id()`)|Mutating Original Nested List Affects Copy?|
|-|-|-|-|
|**Shallow Copy**|`copy.copy(obj)`|**Same reference** (shared)|**Yes** ⚠️|
|**Deep Copy**|`copy.deepcopy(obj)`|**New reference** (independent)|**No** ✅|

#### 5\. Extension: Exception Handling

Wrapped input-sensitive setters in `try / except` blocks inside `main()`:

```python
try:
    thermostat.set\\\_mode("hyperdrive") # Invalid mode
except ValueError as e:
    print(f"\\\[ERROR] Invalid operation: {e}")
```

\---

## 💬 Discussion \& Reflection

### Key Learnings

1. **Attribute Lookup Chain:** Python checks the instance `\\\_\\\_dict\\\_\\\_` first. If missing, it traverses up to the class `\\\_\\\_dict\\\_\\\_`, and finally up the MRO (Method Resolution Order) parent classes.
2. **The Shallow Copy Pitfall:** I initially assumed `copy.copy()` cloned the full object graph. Seeing a mutation in `orig.schedule\\\['weekday']` reflect directly inside the shallow copy was a lightbulb moment. Tracing memory addresses with `id()` made references clear.

### Procedural vs. OOP Paradigm Shift

In a procedural approach, device state and functionality are decoupled (e.g., passing raw dictionaries into utility functions). OOP encapsulates data and behavior together, making complex systems much easier to reason about.

```python
# Procedural (Data \\\& logic separated)
update\\\_thermostat\\\_temp(thermostat\\\_dict, 72)

# Object-Oriented (Encapsulated state \\\& behavior)
thermostat.set\\\_temperature(72)
```

**Maintainability:** If I need to add a `SmartLight` or `SmartLock` tomorrow, I simply extend `SmartDevice` and implement only the deltas, thereby reducing redundant boilerplate and long-term tech debt.

