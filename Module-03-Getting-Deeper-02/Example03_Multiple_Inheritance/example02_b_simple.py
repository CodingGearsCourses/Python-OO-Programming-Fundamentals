# https://www.globaletraining.com/
# Simple Multiple Inheritance
# ChildClass1 is derived from ParentClass1 and ParentClass2
# ChildClass1 is derived from ParentClass2 and ParentClass1

import random


class ParentClass1:
    def __init__(self, message, message_id):
        print("ParentClass1 __init__")
        self.message = message
        self.message_id = message_id

    def click_happy(self):
        print("Class: ParentClass1, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_pc1_1(self):
        print("Class: ParentClass1, Method: click_happy_pc1_1, {}:{}".format(self.message_id, self.message))


class ParentClass2:
    def __init__(self, message, message_id=500):
        print("ParentClass2 __init__")
        self.message = message
        self.message_id = message_id

    def click_happy(self):
        print("Class: ParentClass2, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_pc2_1(self):
        print("Class: ParentClass2, Method: click_happy_pc2_1, {}:{}".format(self.message_id, self.message))


class ChildClass1(ParentClass1, ParentClass2):
    def __init__(self, message):
        print("ChildClass1 __init__")
        self.message = message
        self.message_id = random.randint(100, 200)
        super().__init__(self.message, self.message_id)

    def click_happy(self):
        print("Class: ChildClass1, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_cc1_1(self):
        print("Class: ChildClass1, Method: click_happy_cc1_1, {}:{}".format(self.message_id, self.message))


class ChildClass2(ParentClass2, ParentClass1):
    def __init__(self, message):
        print("ChildClass1 __init__")
        self.message = message
        self.message_id = random.randint(100, 200)
        super().__init__(self.message, self.message_id)

    def click_happy(self):
        print("Class: ChildClass2, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_cc2_1(self):
        print("Class: ChildClass2, Method: click_happy_cc2_1, {}:{}".format(self.message_id, self.message))


def main():
    print("ChildClass1 object".center(40, "-"))
    obj1 = ChildClass1("Checking")
    # print(ChildClass1.__mro__)
    obj1.click_happy()
    obj1.click_happy_pc1_1()
    obj1.click_happy_pc2_1()
    obj1.click_happy_cc1_1()

    print("")

    print("ChildClass2 object".center(40, "-"))
    obj2 = ChildClass2("Checking")
    # print(ChildClass2.__mro__)
    obj2.click_happy()
    obj2.click_happy_pc1_1()
    obj2.click_happy_pc2_1()
    obj2.click_happy_cc2_1()


if __name__ == '__main__':
    main()
