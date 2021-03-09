from jesse.strategies import Strategy
from jesse import utils


class TestInverseFuturesLongTrade(Strategy):
    def should_long(self) -> bool:
        if self.index == 0:
            assert self.position.exchange.contract_size == 100

        return self.price == 10

    def should_short(self) -> bool:
        return False

    def go_long(self):
        entry = 10
        # assuming contract size is 100, buy with all capital
        qty = self.capital * self.price / 100
        self.buy = qty, entry
        self.take_profit = qty, 20

    def go_short(self):
        pass

    def should_cancel(self):
        return False

    def update_position(self):
        if 20 > self.price > 10:
            print(self.position.qty)
            assert self.position.qty == 10
