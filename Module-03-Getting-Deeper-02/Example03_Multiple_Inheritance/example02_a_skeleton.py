# https://www.globaletraining.com/
# Simple Multiple Inheritance


class ParentClass1:
    pass


class ParentClass2:
    pass


# Child class with P1 & P2
class ChildClass1(ParentClass1, ParentClass2):
    pass


# Child class with P2 & P1
class ChildClass2(ParentClass2, ParentClass1):
    pass


def main():
    print("ChildClass1 object".center(40, "-"))
    obj1 = ChildClass1()

    print(isinstance(obj1, ParentClass2))

    # Method Resolution Order (MRO)
    print("Method Resolution Order ".center(40, "-"))
    list1 = ChildClass1.mro()
    for i in list1:
        print(i)

    print("")

    print("ChildClass2 object".center(40, "-"))
    obj2 = ChildClass2()

    print(isinstance(obj2, ParentClass2))

    # Method Resolution Order (MRO)
    print("Method Resolution Order ".center(40, "-"))
    list1 = ChildClass2.mro()
    for i in list1:
        print(i)


if __name__ == '__main__':
    main()
