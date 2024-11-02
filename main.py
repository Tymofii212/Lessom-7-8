# from copyreg import constructor
#
#
# class Worker:
#     def __init__(self, name, age):
#         self.Name=name
#         self.Age=age
#
#
# worker_list=[Worker("Olexander",22),
#              Worker("Maxim",14),
#              Worker("Oleh", 54)]
#
#
# print(worker_list)
#
# worker_iter=iter(worker_list)
#
# for elem in worker_iter:
#     print(elem.Name, elem.Age)


class Counter:
    def __init__(self, max_value):
        self.value = 0
        self.max_value=max_value

    def __iter__(self):
        self.value=0
        return self

    def __next__(self):
        self.value += 1
        if self.value > self.max_value:
            raise StopIteration
        return self.value

timer = Counter(10)

print(next(timer))
print(next(timer))
print(next(timer))
print(next(timer))
print(next(timer))
print(next(timer))
print(next(timer))
