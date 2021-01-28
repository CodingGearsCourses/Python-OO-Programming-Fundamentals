# https://www.globaletraining.com/
# Inheritance - Little Complex One
# A
# B1 --> A
# B2 --> A
# B3 --> A,
# C1 --> B1, B2
# C2 --> B2, B3
# D1 --> C1, C2


class A:
    pass


class B1(A):
    pass


class B2(A):
    pass


class B3(A):
    pass


class C1(B1, B2):
    pass


class C2(B2, B3):
    pass


class D1(C1, C2):
    pass


# Method Resolution Order (MRO)print(" D1:Method Resolution Order ".center(40, "-"))
order = D1.mro()
for x in order:
    print(x)

