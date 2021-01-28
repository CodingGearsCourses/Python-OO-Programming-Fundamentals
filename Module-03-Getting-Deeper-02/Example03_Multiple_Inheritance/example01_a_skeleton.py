# https://www.globaletraining.com/
# Simple Inheritance


class ParentClass1:
    pass


class ChildClass1(ParentClass1):
    pass


def main():
    obj1 = ChildClass1()
    print(isinstance(obj1, ChildClass1))
    print(isinstance(obj1, ParentClass1))

    # Method Resolution Order (MRO)
    print("Method Resolution Order ".center(40, "-"))
    list1 = ChildClass1.mro()
    for i in list1:
        print(i)



if __name__ == '__main__':
    main()