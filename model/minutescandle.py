class MinutesCandle:

    def __init__(self, data):
        self.data = json.loads(data) if type(data) == str else data
        self.parse(self.data)
        
    def parse(self, data:dict):
        self.__market = data['market']
        self.__candle_date_time_utc = data['candle_date_time_utc']
        self.__candle_date_time_kst = data['candle_date_time_kst']
        self.__opening_price = data['opening_price']
        self.__high_price = data['high_price']
        self.__low_price = data['low_price']
        self.__trade_price = data['trade_price']
        self.__timestamp = data['timestamp']
        self.__candle_acc_trade_price = data['candle_acc_trade_price']
        self.__candle_acc_trade_volume = data['candle_acc_trade_volume']
        self.__unit = data['unit']

    @property
    def market(self):
        return self.__market

    @property
    def candle_date_time_utc(self):
        return self.__candle_date_time_utc

    @property
    def candle_date_time_kst(self):
        return self.__candle_date_time_kst

    @property
    def opening_price(self):
        return self.__opening_price

    @property
    def high_price(self):
        return self.__high_price

    @property
    def low_price(self):
        return self.__low_price
    
    @property
    def trade_price(self):
        return self.__trade_price
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @property
    def candle_acc_trade_price(self):
        return self.__candle_acc_trade_price
    
    @property
    def candle_acc_trade_volume(self):
        return self.__candle_acc_trade_volume
    
    @property
    def unit(self):
        return self.__unit
    
    def __str__(self):
        ret = ""
        ret += f'market : {self.market}, '
        ret += f'candle_date_time_utc : {self.candle_date_time_utc}, '
        ret += f'candle_date_time_kst : {self.candle_date_time_kst}, '
        ret += f'opening_price : {self.opening_price}, '
        ret += f'high_price : {self.high_price}, '
        ret += f'low_price : {self.low_price}, '
        ret += f'trade_price : {self.trade_price}, '
        ret += f'timestamp : {self.timestamp}, '
        ret += f'candle_acc_trade_price : {self.candle_acc_trade_price}, '
        ret += f'candle_acc_trade_volume : {self.candle_acc_trade_volume}, '
        ret += f'unit : {self.unit}'
        return ret