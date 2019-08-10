from calculator.model import ContactsModel

class CalculatorController:
    def __init__(self):
        num1 = int(input('첫번째 수'))
        num2 = int(input('두번째 수'))
        self.calc = ContactsModel(num1, num2)

    def exec(self):
        op = ''
        if op == '+':
        result = self.calc.add()
        print('계산결과 : %d' % result)

    def exec(self):
        op = ''
        if op == '+':
            result = self.calc.add()

        elif op == '-':
            result = self.calc.add()

        elif op == '*':
            result = self.calc.add()

        elif op == '/':
            result = self.calc.add()

        return result
