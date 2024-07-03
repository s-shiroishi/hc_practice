from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Type, List, Dict

class NegativeValueError(ValueError):
    pass

class InsufficientBalanceError(ValueError):
    pass

class InvalidChargeAmountError(Exception):
    pass

class StockError(ValueError):
    pass

class Suica:
    def __init__(self):
        self._balance = 500

    def __str__(self):
        return f'Suica残高: {self._balance}'

    @property
    def deposit(self):
        return self._balance
    
    def deduct(self, amount: int):
        if amount < 0:
            raise NegativeValueError('不正な値です。')
        if self._balance < amount:
            raise InsufficientBalanceError(f'{amount - self._balance}円足りません。')
        self._balance -= amount

    def charge(self, amount: int):
        if amount < 100:
            raise InvalidChargeAmountError('100 円未満はチャージできません')
        self._balance += amount

class AbstractJuice(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> int:
        pass

class Pepsi(AbstractJuice):
    @property
    def name(self) -> str:
        return 'ペプシ'
    
    @property
    def price(self) -> int:
        return 150

class Irohasu(AbstractJuice):
    @property
    def name(self) -> str:
        return 'いろはす'
    
    @property
    def price(self) -> int:
        return 120

class Monster(AbstractJuice):
    @property
    def name(self) -> str:
        return 'モンスター'
    
    @property
    def price(self) -> int:
        return 230

class VendingMachine:
    def __init__(self, refilled_juices: Dict[Type[AbstractJuice], int]):
        self._earnings = 0
        self._stocks = defaultdict(list)
        self.refill(refilled_juices)

    def __str__(self) -> str:
        stocks_str = '自動販売機在庫: '
        for name, stock in self._stocks.items():
            stocks_str += f'{name}{len(stock)}本、'
        return stocks_str.rstrip('、')

    @property
    def stocks(self) -> List[str]:
        stocks = []
        for name, stock in self._stocks.items():
            if len(stock) > 0:
                stocks.append(name)
        return stocks
    
    @property
    def earnings(self) -> int:
        return self._earnings
    
    def refill(self, refilled_juices: Dict[Type[AbstractJuice], int]):
        for juice, cnt in refilled_juices.items():
            if cnt < 0:
                raise NegativeValueError('補充数は0以上の数値を入力してください。')
            for _ in range(cnt):
                _juice = juice()
                self._stocks[_juice.name].append(_juice)

    def _add_earnings(self, amount: int):
        if amount < 0:
            raise NegativeValueError('不正な値です。')
        self._earnings += amount

    def _remove_juice(self, juice_name: str):
        if juice_name not in self.stocks:
            raise StockError(f'{juice_name}の在庫がありません。')
        return self._stocks[juice_name].pop()

    def sell(self, suica: Suica, juice: Type[AbstractJuice]):
        juice_name = juice().name
        try:
            removed_juice = self._remove_juice(juice_name)
        except StockError as e:
            raise StockError(f"在庫エラー: {e}")
        try:
            suica.deduct(removed_juice.price)
        except NegativeValueError as e:
            self._stocks[juice_name].append(removed_juice)
            raise NegativeValueError(f"不正値エラー: {e}")
        except InsufficientBalanceError as e:
            self._stocks[juice_name].append(removed_juice)
            raise InsufficientBalanceError(f"残高エラー: {e}")
        self._add_earnings(removed_juice.price)

def view_condition(suica: Suica, vending_machine: VendingMachine):
    print(suica)
    print(vending_machine)
    print(f'自動販売機収益: {vending_machine.earnings}円')


if __name__ == '__main__':
    suica = Suica()
    vending_machine = VendingMachine({
        Pepsi: 5,
        Monster: 5,
        Irohasu: 5,
    })

    print('初期状態'.center(70, '='))
    view_condition(suica, vending_machine)

    print('ペプシ購入(150円)'.center(70, '='))
    vending_machine.sell(suica, Pepsi)
    view_condition(suica, vending_machine)

    print('モンスター購入(230円)'.center(70, '='))
    vending_machine.sell(suica, Monster)
    view_condition(suica, vending_machine)

    print('いろはす購入(120円)'.center(70, '='))
    vending_machine.sell(suica, Irohasu)
    view_condition(suica, vending_machine)

    print('Suica300円チャージ'.center(70, '='))
    suica.charge(300)
    view_condition(suica, vending_machine)

    print('在庫6本補充'.center(70, '='))
    vending_machine.refill({
        Pepsi: 6,
        Monster: 6,
        Irohasu: 6,
    })
    
    view_condition(suica, vending_machine)