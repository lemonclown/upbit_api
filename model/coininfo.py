class CoinInfo:
    
    def __init__(self, data:dict):
        self.data = data
        self.parse(data)
        
    def parse(self, data:dict):
        self.__market:str = data['market']
        self.__korean_name:str = data['korean_name']
        self.__english_name:str = data['english_name']
        self.__market_warning:str = data['market_warning'] if 'market_warning' in data else ""

    @property
    def market(self) -> str:
        return self.__market

    @property
    def korean_name(self) -> str:
        return self.__korean_name

    @property
    def english_name(self) -> str:
        return self.__english_name

    @property
    def market_warning(self) -> str:
        return self.__market_warning

    def __str__(self):
        ret = f"Market: {self.market}, "
        ret += f"korean_name: {self.korean_name}, "
        ret += f"english_name: {self.english_name}, "
        ret += f"market_warning: {self.market_warning}"
        return ret 