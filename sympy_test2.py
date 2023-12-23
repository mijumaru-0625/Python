"""
globals() という関数に何が入っているかを確認
locals() という関数に何が入っているかを確認
"""


class GlobalsTest:

    def __init__(self) -> None:
        self.aaa_dict = {}

    def test(self):
        a = 1
        print(globals())
        print("-------------------------")
        print(locals())


def test():
    a = 1
    print(globals())
    print("-------------------------")
    print(locals())

print("def test():")
test()

print()
print("Class GlobalsTest().test()")
GlobalsTest().test()