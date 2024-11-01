#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return dir(obj)

# Test cases
if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    class MyClass3(object):
        def dir(self):
            return ["my_class", "is", "empty"]

    class MyClass4(object):
        one_attribute = 89

    class MyClass5(object):
        def one_meth(self):
            pass

    print(lookup(MyClass1))  # Expected output: list of default attributes and methods
    print(lookup(MyClass2))  # Expected output: list of default attributes, methods + 'my_attr1', 'my_meth'
    print(lookup(int))       # Expected output: list of int attributes and methods
    print(lookup(float))     # Expected output: list of float attributes and methods
    print(lookup(object))    # Expected output: list of object attributes and methods
    print(lookup(list))      # Expected output: list of list attributes and methods
    print(lookup(MyClass3))  # Expected output: ["my_class", "is", "empty"]
    print(lookup(MyClass4))  # Expected output: list of default attributes, methods + 'one_attribute'
    print(lookup(MyClass5))  # Expected output: list of default attributes, methods + 'one_meth'
