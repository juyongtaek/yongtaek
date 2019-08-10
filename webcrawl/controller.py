from webcrawl.assembly import AssemblyCrawler
from webcrawl.bugsmusic import BugsCrawler

class Controller:
    def __init__(self):
        num1 = int(input('a'))
        num2 = int(input('b'))
        self.calc = ContactsModel(num1, num2)

    def exec(self):
        op = ''
        if op == '+':
        result = self.calc.add()
        print('계산결과 : %d' % result)

    def exec(self):
        op = ''
        if flag == 'a':
            a = AssemblyCrawler(http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_P1J9W0O8I0J1U1X3N0B7N1H9B0Q9P6)
            a.scrap()

        elif flag == 'b':
            b = BugsCrawler(https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11)
            b.scrap()

        elif flag == '*':
            result = self.calc.add()

        elif op == '/':
            result = self.calc.add()

        return result
