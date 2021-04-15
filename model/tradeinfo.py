class TradeInfo:

    def __init__(self, data:str):
        self.data = json.loads(data)
        self.parse(self.data)
    
    def parse(self, data:dict):
        self.__trade_date_utc:str = data['trade_date_utc']
        self.__trade_time_utc:str = data['trade_time_utc']
        self.__timestamp:int = data['timestamp']
        self.__trade_price:int = data['trade_price']
        self.__trade_volume:int = data['trade_volume']
        self.__prev_closing_price:int = data['prev_closing_price']
        self.__change_price:int = data['change_price']
        self.__ask_bid:str = data['ask_bid']
        self.__sequential_id:int = data['sequential_id']

    @property
    def trade_date_utc(self) -> str:
        return self.__trade_date_utc

    @property
    def trade_time_utc(self) -> str:
        return self.__trade_time_utc

    @property
    def timestamp(self) -> int:
        return self.__timestamp

    @property
    def trade_price(self) -> int:
        return self.__trade_price

    @property
    def trade_volume(self) -> int:
        return self.__trade_volume

    @property
    def prev_closing_price(self) -> int:
        return self.__prev_closing_price

    @property
    def change_price(self) -> int:
        return self.__change_price

    @property
    def ask_bid(self) -> str:
        return self.__ask_bid

    @property
    def sequential_id(self) -> int:
        return self.__sequential_id
