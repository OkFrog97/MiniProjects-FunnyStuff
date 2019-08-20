class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop()+self.pop())

    def sub(self):
        # операция вычитания
        self.append(self.pop()-self.pop())

    def mul(self):
        # операция умножения
        self.append(self.pop()*self.pop())

    def div(self):
        # операция целочисленного деления
        self.append(self.pop()//self.pop())
