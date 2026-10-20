"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
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

class NetworkDevice:
    device_type = "Network Device"

    def __init__(self, hostname, ip_address, status):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status

    def describe(self):
        return (
            f"{self.device_type}: {self.hostname} | "
            f"IP Address: {self.ip_address} | Status: {self.status}"
        )


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

class Router(NetworkDevice):
    device_type = "Router"

    def __init__(self, hostname, ip_address, status, routing_protocol, interfaces):
        super().__init__(hostname, ip_address, status)
        self.routing_protocol = routing_protocol
        self.interfaces = interfaces

    def describe(self):
        return (
            f"{self.device_type}: {self.hostname} | "
            f"IP Address: {self.ip_address} | Status: {self.status} | "
            f"Routing Protocol: {self.routing_protocol} | "
            f"Interfaces: {self.interfaces}"
        )

    def check_connectivity(self):
        if self.status.lower() == "online":
            return f"{self.hostname} is online and available."
        return f"{self.hostname} is offline and may need troubleshooting."


# Student-created extension: a switch uses the shared parent functionality
# but adds VLAN information specific to network switches.
class Switch(NetworkDevice):
    device_type = "Switch"

    def __init__(self, hostname, ip_address, status, vlan_ids):
        super().__init__(hostname, ip_address, status)
        self.vlan_ids = vlan_ids

    def describe(self):
        return (
            f"{self.device_type}: {self.hostname} | "
            f"IP Address: {self.ip_address} | Status: {self.status} | "
            f"VLANs: {self.vlan_ids}"
        )


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

    router1 = Router("R1", "192.168.1.1", "Online", "OSPF", 4)
    router2 = Router("R2", "192.168.1.2", "Offline", "BGP", 6)

    print("Class variable through class:", Router.device_type)
    print("Class variable through object:", router1.device_type)

    # This attribute belongs only to router1; router2 remains unchanged.
    router1.location = "Main Office"

    print("\nRouter 1 instance namespace:")
    print(router1.__dict__)

    print("\nRouter 2 instance namespace:")
    print(router2.__dict__)

    # The class namespace contains attributes and methods defined on Router.
    print("\nRouter class namespace:")
    print(Router.__dict__)


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

    original_config = {
        "hostname": "R1",
        "vlans": [10, 20, 30],
        "interfaces": {
            "GigabitEthernet0/1": "192.168.1.1",
            "GigabitEthernet0/2": "192.168.1.2"
        }
    }

    shallow_config = copy(original_config)
    deep_config = deepcopy(original_config)

    # A shallow copy creates a new outer dictionary but shares references
    # to nested lists and dictionaries with the original configuration.
    #
    # A deep copy recursively copies nested data, so modifications to the
    # original nested objects do not change the deep copy.
    original_config["vlans"].append(40)
    original_config["interfaces"]["GigabitEthernet0/3"] = "192.168.1.3"

    print("Original configuration:", original_config)
    print("Shallow copy:", shallow_config)
    print("Deep copy:", deep_config)


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
    print("=== Network Device Management System ===")

    print("\nParent class object:")
    device = NetworkDevice("CoreDevice", "192.168.1.10", "Online")
    print(device.describe())

    print("\nChild class object:")
    router = Router("R1", "192.168.1.1", "Online", "OSPF", 4)
    print(router.describe())
    print(router.check_connectivity())

    print("\nStudent-Created Extension:")
    switch = Switch("SW1", "192.168.1.20", "Online", [10, 20, 30])

    # Different device classes can provide their own describe() behavior.
    devices = [device, router, switch]
    for network_device in devices:
        print(network_device.describe())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
