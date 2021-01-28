# https://www.globaletraining.com/
# Simple Inheritance
# ChildClass1 is derived from ParentClass1
# ChildClass2 ( no __init__) is derived from ParentClass1

import random


class ParentClass1:
    def __init__(self, message, message_id):
        print("ParentClass1 __init__")
        self.message = message
        self.message_id = message_id

    def click_happy(self):
        print("Class: ParentClass1, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_01(self):
        print("Class: ParentClass1, Method: click_happy_01, {}:{}".format(self.message_id, self.message))


class ChildClass1(ParentClass1):
    def __init__(self, message):
        print("ChildClass1 __init__")
        self.message = message
        self.message_id = random.randint(100, 200)
        super().__init__(self.message, self.message_id)

    def click_happy(self):
        print("Class: ChildClass1, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_11(self):
        print("Class: ChildClass1, Method: click_happy_11, {}:{}".format(self.message_id, self.message))


class ChildClass2(ParentClass1):
    def click_happy(self):
        print("Class: ChildClass2, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_21(self):
        print("Class: ChildClass2, Method: click_happy_21, {}:{}".format(self.message_id, self.message))


def main():
    print("ChildClass1 object".center(40, "-"))
    obj1 = ChildClass1("Checking")
    # print(ChildClass1.__mro__)
    obj1.click_happy()
    obj1.click_happy_01()
    obj1.click_happy_11()

    print("")

    print("ChildClass2 object".center(40, "-"))
    obj2 = ChildClass2("Checking", 500)
    # print(ChildClass2.__mro__)
    obj2.click_happy()
    obj2.click_happy_01()
    obj2.click_happy_21()


if __name__ == '__main__':
    main()
