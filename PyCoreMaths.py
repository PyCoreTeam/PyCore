from typing import overload


class Sign:

    def __init__(self, sign):
        self.sign = sign

    def getStr(self):
        return self.sign


class Positive(Sign):

    def __init__(self):
        super().__init__("+")

    def getStr(self):
        return '+'


class Negative(Sign):

    def __init__(self):
        super().__init__("-")

    def getStr(self):
        return '-'


class Fraction:
    def __init__(self, sign: Negative or Positive, num: int, deno: int):

        self.sign = sign
        self.num = num
        if deno == 0:
            raise ValueError("Denominator cannot be 0")
        self.deno = deno

    def getFloat(self) -> float:

        if self.sign.getStr() == '-':
            return -((self.num / self.deno))
        else:
            return (self.num / self.deno)

    def getStr(self) -> str:

        if self.sign.getStr() == '-':
            return f"-{self.num}/{self.deno}"

        else:
            return f"{self.num}/{self.deno}"
# 高斯求和 1+2+3+4+.......+100 (SIMPLE)


def GaussSum(n : int):
    return n * (n+1) / 2
def _GaussSum(n, a, d):
    """n表示项数，a表示第一个项，d表示公差"""
    return (n / 2) * (2*a + (n - 1) * d)

print(_GaussSum(10, 1, 1))
