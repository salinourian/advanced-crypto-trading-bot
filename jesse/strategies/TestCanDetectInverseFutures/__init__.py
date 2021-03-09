from jesse.strategies import Strategy
from jesse import utils


class TestCanDetectInverseFutures(Strategy):
    def should_long(self) -> bool:
        if self.index == 0:
            # current capital should be 1 BTC
            assert self.capital == 100
            assert self.position.exchange.type == 'inverse futures'
            assert self.symbol == 'BTC-PERP'
            assert self.leverage == 2
            assert self.contract_size == 1

        return False

    def should_short(self) -> bool:
        return False

    def go_long(self):
        pass

    def go_short(self):
        pass

    def should_cancel(self):
        return False
