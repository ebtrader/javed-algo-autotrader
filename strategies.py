from collections import deque
import pandas as pd
from finta import TA

class WMA:
    def __init__(self, periods: int, ticks: int):
        self.periods = periods
        self.ticks = ticks
        self.period_sum = periods
        self.n = 0
        self.dq = deque()
        self.wma = 0
        self.signal = "NONE"
        self.high = 0
        self.max_value = 0
        self.dq1 = deque()
        self.i = 0

    def calc_wma(self):
        weight = 1
        wma_total = 0
        # for price in self.dq:
        #    wma_total += price * weight
        #    weight = 1
        # self.wma = wma_total / self.period_sum
        data = list(self.dq)
        df = pd.DataFrame(data, columns=['close'])
        # df['sma'] = df['price'].rolling(window=self.periods).mean()
        df['sma'] = TA.SMA(df, self.periods)
        self.wma = df['sma'].iloc[-1]
        self.dq.popleft()

    def update_signal(self, price: float):
        self.dq.append(price)
        self.n += 1
        if self.n < self.periods:
            return
        prev_wma = self.wma
        self.calc_wma()
        if prev_wma != 0:
            if self.wma > prev_wma:
                self.signal = "LONG"
            elif self.wma < prev_wma:
                self.signal = "SHRT"

    def find_high(self, price: float):
        self.dq1.append(price)
        self.max_value = max(self.dq1)
        self.i += 1
        if self.i > self.ticks:
            self.dq1.popleft()


