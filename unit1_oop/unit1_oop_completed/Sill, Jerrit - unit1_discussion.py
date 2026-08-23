"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

This program demonstrates object-oriented programming concepts using a
smart-home theme: a base SmartDevice class and a Thermostat subclass that
inherits from it. It also demonstrates class/instance namespaces and the
difference between shallow and deep copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class SmartDevice:
    """Base class representing any device on the smart-home network."""

    # Class variable shared by every SmartDevice (and subclass) instance.
    device_count = 0

    def __init__(self, name, location):
        # Instance variables — unique to each object.
        self.name = name
        self.location = location
        self.status = "off"

        # Track how many devices have been created across the whole system.
        SmartDevice.device_count += 1

    def turn_on(self):
        self.status = "on"

    def turn_off(self):
        self.status = "off"

    def get_info(self):
        """Return a human-readable summary of the device."""
        return f"{self.name} ({self.location}): status={self.status}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Thermostat(SmartDevice):
    """A thermostat is a SmartDevice that also manages temperature."""

    # New class variable specific to thermostats.
    supported_modes = ["heat", "cool", "auto"]

    def __init__(self, name, location, target_temp, mode="auto"):
        # Reuse the parent constructor for shared setup (name, location, status).
        super().__init__(name, location)

        # New instance variables specific to Thermostat.
        self.target_temp = target_temp
        self.mode = mode
        self.schedule = {"weekday": target_temp, "weekend": target_temp}

    def set_mode(self, mode):
        """New method: change the operating mode, with basic error handling."""
        if mode not in Thermostat.supported_modes:
            raise ValueError(
                f"'{mode}' is not a supported mode. Choose from {Thermostat.supported_modes}."
            )
        self.mode = mode

    def set_temperature(self, temp):
        """New method: update the target temperature with input validation."""
        if not isinstance(temp, (int, float)):
            raise TypeError("Temperature must be a number.")
        self.target_temp = temp

    def get_info(self):
        """Override the parent method to include thermostat-specific details."""
        base_info = super().get_info()
        return f"{base_info}, target_temp={self.target_temp}\u00b0F, mode={self.mode}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    t1 = Thermostat("Living Room Thermostat", "Living Room", 70)
    t2 = Thermostat("Office Thermostat", "Office", 68)

    # Access a class variable through the class itself.
    print(f"Access via class:    Thermostat.supported_modes = {Thermostat.supported_modes}")

    # Access the same class variable through an instance.
    print(f"Access via instance: t1.supported_modes = {t1.supported_modes}")

    # Add a new attribute to only ONE object after creation.
    t1.firmware_version = "2.1.0"

    # Show each object's instance namespace.
    print(f"\nt1.__dict__ (has extra 'firmware_version'): {t1.__dict__}")
    print(f"t2.__dict__ (unaffected by t1's new attribute): {t2.__dict__}")

    # Show that the class namespace is shared and unaffected by instance attributes.
    print(f"\n'firmware_version' in Thermostat.__dict__? "
          f"{'firmware_version' in Thermostat.__dict__}")
    print(f"Thermostat.__dict__ contains class-level items like 'supported_modes': "
          f"{'supported_modes' in Thermostat.__dict__}")
    print(f"Total SmartDevice instances created so far: {SmartDevice.device_count}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = Thermostat("Bedroom Thermostat", "Bedroom", 65)
    original.schedule = {"weekday": [65, 68, 70], "weekend": [70, 72]}

    # Shallow copy: copies the Thermostat object itself, but the nested
    # 'schedule' dictionary (and the lists inside it) are still the SAME
    # objects in memory as the original's.
    shallow = copy(original)

    # Deep copy: recursively copies the object AND every nested mutable
    # object inside it, so the schedule dict/lists are independent copies.
    deep = deepcopy(original)

    # Modify the original's nested mutable data.
    original.schedule["weekday"].append(72)
    original.target_temp = 60  # top-level attribute change, does not affect copies

    print(f"Original : target_temp={original.target_temp}, schedule={original.schedule}")
    print(f"Shallow  : target_temp={shallow.target_temp}, schedule={shallow.schedule}")
    print(f"Deep     : target_temp={deep.target_temp}, schedule={deep.schedule}")

    print(
        "\nExplanation: The shallow copy's top-level attribute (target_temp) did NOT "
        "change because copy() gives it its own top-level namespace, but its nested "
        "'schedule' dict is the SAME object as the original's, so the appended value "
        "'72' shows up in both. The deep copy's schedule is a fully independent copy, "
        "so it was unaffected by the change to the original."
    )


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Parent class object.
    generic_device = SmartDevice("Front Door Camera", "Front Porch")
    generic_device.turn_on()
    print("\nParent object:")
    print(generic_device.get_info())

    # Child class object.
    living_room_thermostat = Thermostat("Living Room Thermostat", "Living Room", 72, "cool")
    living_room_thermostat.turn_on()
    print("\nChild object:")
    print(living_room_thermostat.get_info())

    # Demonstrate inheritance: Thermostat reuses SmartDevice's turn_on/turn_off,
    # but overrides get_info() to add its own details.
    print("\nDemonstrating inheritance (shared turn_off, overridden get_info):")
    living_room_thermostat.turn_off()
    print(living_room_thermostat.get_info())

    # Student-created extension: basic error handling around an invalid operation.
    print("\nDemonstrating error handling (student extension):")
    try:
        living_room_thermostat.set_mode("turbo")  # not a supported mode
    except ValueError as error:
        print(f"Caught expected error: {error}")

    try:
        living_room_thermostat.set_temperature("warm")  # invalid type
    except TypeError as error:
        print(f"Caught expected error: {error}")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
