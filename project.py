import string
from string import digits, punctuation


class Client:
    def __init__(self,name,surname,number_passport,name_amount):
        self.__check(name)
        self.__check(surname)
        self.name = 'Client: ' + name
        self.surname  = 'Client surname: ' + surname
        self._number_passport = self.__check_digits(number_passport)
        self._amount = {name_amount: 0}




    def __make_amount(self,name_amount):
        return {f'{name_amount}': 0}

    @staticmethod
    def __check(arq):
        not_aloud: str = digits + punctuation
        if not isinstance(arq,str):
            raise TypeError('argument have to be string')
        if arq.strip(not_aloud) != arq:
            raise ValueError('check')

    @staticmethod
    def __check_digits(arq):
        if arq.isdigit():
            ''.join(str(arq))
            return "number of passport is: " + arq

        if not arq.isdigit():
            raise ValueError('check digits')



class BankAccount(Client):
    def __init__(self,name,surname,number_passport,name_amount):
        super().__init__(name,surname,number_passport,name_amount)


    def deposit(self, name_amount, amount):
        if str(name_amount) in {str(x) for x in self._amount}:
            try:
                amount = int(amount)
            except(ValueError, TypeError) as erorr:
                raise (f'deposit failed as {erorr}')

            self._amount[name_amount] += amount
            return self._amount
        return self._amount.keys()

    def withdraw(self,name_amount,amount):
        if name_amount in {x for x in self._amount}:
            try:
                amount = int(amount)
            except(TypeError,ValueError,AssertionError) as erorr:
                raise(f'withdraw failed as {erorr}')

            if not self._amount[name_amount] <= 0:
                self._amount[name_amount] -= amount
            else:
                return f'You\'r account: {name_amount} has no money'
        else:
            return 'You need creat new account of bank'

    def get_balance(self,name_amount):
        return self._amount.get(name_amount,'Not defind account')


    def __repr__(self):
        return (f"Class is {BankAccount}:BankAccount, ParentClass is {Client}: Client,")

    def __str__(self):
        return (f'{self.__dict__}')















c1 = BankAccount('Artem','Rokhmakov','0983','my_first_account')
# print(c1.withdraw('my_first_account',20))
print(c1.get_balance('my_first_account'))

