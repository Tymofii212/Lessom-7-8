from copyreg import constructor


class Worker:
    def __init__(self, name, age):
        self.Name=name
        self.Age=age


worker_list=[Worker("Olexander",22),
             Worker("Maxim",14),
             Worker("Oleh", 54)]


print(worker_list)

worker_iter=iter(worker_list)

for elem in worker_iter:
    print(elem.Name, elem.Age)



