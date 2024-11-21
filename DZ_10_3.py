import threading
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            summa = randint(50, 500)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()

            self.balance += summa
            print(f'Пополнение счета на {summa}. Баланс {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            summa = randint(50, 500)
            print(f'Запрос на снятие {summa}')
            if self.balance >= summa:
                #self.lock.acquire()
                self.balance -= summa
                print(f'Снятие: {summa}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


if __name__ == '__main__':
    bk = Bank()
    t1 = threading.Thread(target=Bank.deposit, args=(bk,))
    t2 = threading.Thread(target=Bank.take, args=(bk,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f'Итоговый баланс: {bk.balance}')
