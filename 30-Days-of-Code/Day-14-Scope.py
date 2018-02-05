class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        max_num = max(self.__element)
        min_num = min(self.__element)
        self.maximumDifference = max_num - min_num

        if self.maximumDifference < 0:
            self.maximumDifference *= -1

        return self.maximumDifference

a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
