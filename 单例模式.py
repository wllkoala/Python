class Mysingleton:

    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if Mysingleton.__init_flag:
            print("init...")
            self.name = name
            Mysingleton.__init_flag = False


a = Mysingleton("aa")
print(a)
