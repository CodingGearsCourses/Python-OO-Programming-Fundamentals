# https://www.globaletraining.com/
# Simple Multiple Inheritance
# ParentClass1 <--- ChildClassLevel1 <--- ChildClassLevel2


class ParentClass1:
    pass


class ChildClassLevel1(ParentClass1):
    pass


class ChildClassLevel2(ChildClassLevel1):
    pass


def main():
    # ChildClassLevel2
    print("ChildClassLevel2 object".center(40, "-"))
    obj_l2 = ChildClassLevel2()
    print(isinstance(obj_l2, ParentClass1))

    # Method Resolution Order (MRO)
    print("Method Resolution Order ".center(40, "-"))
    list1 = ChildClassLevel2.mro()
    for i in list1:
        print(i)

    print("")

    # ChildClassLevel1
    print("ChildClassLevel1 object".center(40, "-"))
    obj_l1 = ChildClassLevel1()
    print(isinstance(obj_l1, ParentClass1))

    # Method Resolution Order (MRO)
    print("Method Resolution Order ".center(40, "-"))
    list1 = ChildClassLevel1.mro()
    for i in list1:
        print(i)

    print("")

    # ParentClass1
    print("ParentClass1 object".center(40, "-"))
    obj_p1 = ParentClass1()
    print(isinstance(obj_p1, ParentClass1))

    # Method Resolution Order (MRO)
    print("Method Resolution Order ".center(40, "-"))
    list1 = ParentClass1.mro()
    for i in list1:
        print(i)

if __name__ == '__main__':
    main()
