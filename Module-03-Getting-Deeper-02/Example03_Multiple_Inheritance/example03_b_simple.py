# https://www.globaletraining.com/
# Simple Multiple Inheritance
# ParentClass1 <--- ChildClassLevel1 <--- ChildClassLevel2


class ParentClass1:
    def __init__(self, message, message_id):
        print("ParentClass1 __init__")
        self.message = message
        self.message_id = message_id

    def click_happy(self):
        print("Class: ParentClass1, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_pc1_1(self):
        print("Class: ParentClass1, Method: click_happy_pc1_1, {}:{}".format(self.message_id, self.message))


class ChildClassLevel1(ParentClass1):
    def __init__(self, message, message_id):
        print("ChildClassLevel1 __init__")
        self.message = message
        self.message_id = message_id
        super().__init__(self.message, self.message_id)

    def click_happy(self):
        print("Class: ChildClassLevel1, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_cc1_1(self):
        print("Class: ChildClassLevel1, Method: click_happy_cc1_1, {}:{}".format(self.message_id, self.message))


class ChildClassLevel2(ChildClassLevel1):
    def __init__(self, message, message_id):
        print("ChildClassLevel2 __init__")
        self.message = message
        self.message_id = message_id
        super().__init__(self.message, self.message_id)

    def click_happy(self):
        print("Class: ChildClassLevel2, Method: click_happy, {}:{}".format(self.message_id, self.message))

    def click_happy_cc2_1(self):
        print("Class: ChildClassLevel2, Method: click_happy_cc2_1, {}:{}".format(self.message_id, self.message))


def main():
    # ChildClassLevel2 Object
    print("ChildClassLevel2 object".center(40, "-"))
    obj1 = ChildClassLevel2("Checking", 501)
    obj1.click_happy()
    obj1.click_happy_cc2_1()
    obj1.click_happy_cc1_1()
    obj1.click_happy_pc1_1()

    print("")

    # ChildClassLevel1 Object
    print("ChildClassLevel1 object".center(40, "-"))
    obj2 = ChildClassLevel1("Checking", 502)
    obj2.click_happy()
    # obj2.click_happy_cc2_1() # ChildClassLevel2 methods are nor accessible to ChildClassLevel1
    obj2.click_happy_cc1_1()
    obj2.click_happy_pc1_1()

    print("")

    # ParentClass1 Object
    print("ParentClass1 object".center(40, "-"))
    obj3 = ParentClass1("Checking", 503)
    # print(ParentClass1.__mro__)
    obj3.click_happy()
    # obj3.click_happy_cc2_1() # ChildClassLevel2 methods are nor accessible to ParentClass1
    # obj3.click_happy_cc1_1() # ChildClassLevel1 methods are nor accessible to ParentClass1
    obj3.click_happy_pc1_1()


if __name__ == '__main__':
    main()
