import threading
class BankAccount():
    def __init__(self,balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Withdrew {amount}, new balance is {self.balance}')


lock = threading.Lock()

def deposit_task(account, amount):
    for _ in range(5):
        with lock:
            account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        lock.acquire()
        account.withdraw(amount)
        lock.release()

account = BankAccount(1000)

#deposit_task(account, 100)
#withdraw_task(account, 150)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()













