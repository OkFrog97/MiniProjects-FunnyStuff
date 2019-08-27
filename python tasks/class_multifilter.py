class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return True if pos>=neg else False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return True if pos>=1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return True if neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = interable
        self.funcs = funcs
        self.judge = judge
        self.answer = []

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in interable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(self.iterable) == True:
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg) == True:
                self.answer.append(i)
