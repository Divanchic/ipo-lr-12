class Client():
    def __init__(self, name):
        self.name = name
        self.names = []
    def gav(self):
        self.names.append(self.name)
    def asd(self):
        return self.names

a = Client("ivan")
a.gav()
print(a.name)