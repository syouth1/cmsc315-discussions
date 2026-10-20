# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

Overview

In this project, the object-oriented programming concepts using Python were implemented in a network device management application. The concepts studied were classes, objects, inheritance, method overriding, namespaces, and shallow and deep copying.

Implementation

1. Classes and Inheritance

The parent class NetworkDevice was created having attributes such as hostname and IP address, and status and a method describe. The child class Router inherited the functionalities of the parent class and provided with additional methods and attributes such as routing protocol and interface information. The functionality of super() was used to invoke the parent class constructor and the method describe is overridden to use router features.

2. Namespaces

Two objects of routers were created and the class variable device_type was accessed using both the class and the object. Another attribute location was added to just one of the routers. The __dict__ method was used to see the variables of both the instance and the class.

3. Shallow and Deep Copying

I made a nested dictionary that shows how a router is set up, including VLANs and network interfaces. I used the functions copy() and deepcopy() to check the copying process and found that shallow copies were affected by changes in the nested data of the original configuration, but not deep copies.

4. Newly Implemented Feature

I added the Switch class which is a subclass of NetworkDevice and provides VLAN details. I created different objects of devices and put them into the list and used the describe() method with an aim to show polymorphism.
Steps to Run the Code
1. Make sure that Python3 is installed on your computer.
2. Open the terminal in the working folder, which contains the file unit1_discussion.py.
3. Execute the command from your terminal:
python3 unit1_discussion.py

Result

I executed the program and made sure that the parent, router, and switch worked in compliance with the requirements. I have checked the instance variabilities in details and made sure that router methods are performing their functions correctly and results of shallow and deep copies are meeting expectations.

Conclusion

The project showed the way in which inheritance and polymorphism enabled code reuse, the way in which namespaces helped to structure data, and the impact of copying on nested configuration data. The networking example illustrated how OOP can help coordinate network devices while maintaining their specific abilities.
