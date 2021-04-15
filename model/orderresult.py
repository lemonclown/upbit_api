class OrderResult:
    
    def __init__(self, data:str):
        self.data = json.loads(data)
        self.parse(self.data)
    
    def parse(self, data:dict):
        self.__uuid = data.get('uuid','')
        self.__side = data.get('side','')
        self.__ord_type = data.get('ord_type','')
        self.__price = data.get('price','')
        self.__avg_price = data.get('avg_price','')
        self.__state = data.get('state','')
        self.__market = data.get('market','')
        self.__created_at = data.get('created_at','')
        self.__volume = data.get('volume','')
        self.__remaining_volume = data.get('remaining_volume','')
        self.__reserved_fee = data.get('reserved_fee','')
        self.__remaining_fee = data.get('remaining_fee','')
        self.__paid_fee = data.get('paid_fee','')
        self.__locked = data.get('locked','')
        self.__executed_volume = data.get('executed_volume','')
        self.__trade_count = data.get('trade_count','')
    
    @property
    def uuid(self):
        return self.__uuid

    @property
    def side(self):
        return self.__side

    @property
    def ord_type(self):
        return self.__ord_type

    @property
    def price(self):
        return self.__price

    @property
    def avg_price(self):
        return self.__avg_price

    @property
    def state(self):
        return self.__state

    @property
    def market(self):
        return self.__market

    @property
    def created_at(self):
        return self.__created_at

    @property
    def volume(self):
        return self.__volume

    @property
    def remaining_volume(self):
        return self.__remaining_volume

    @property
    def reserved_fee(self):
        return self.__reserved_fee

    @property
    def remaining_fee(self):
        return self.__remaining_fee

    @property
    def paid_fee(self):
        return self.__paid_fee

    @property
    def locked(self):
        return self.__locked

    @property
    def executed_volume(self):
        return self.__executed_volume

    @property
    def trade_count(self):
        return self.__trade_count
    
    def __str__(self):
        ret = ""
        ret += f"uuid : {self.uuid}, "
        ret += f"side : {self.side}, "
        ret += f"ord_type : {self.ord_type}, "
        ret += f"price : {self.price}, "
        ret += f"avg_price : {self.avg_price}, "
        ret += f"state : {self.state}, "
        ret += f"market : {self.market}, "
        ret += f"created_at : {self.created_at}, "
        ret += f"volume : {self.volume}, "
        ret += f"remaining_volume : {self.remaining_volume}, "
        ret += f"reserved_fee : {self.reserved_fee}, "
        ret += f"remaining_fee : {self.remaining_fee}, "
        ret += f"paid_fee : {self.paid_fee}, "
        ret += f"locked : {self.locked}, "
        ret += f"executed_volume : {self.executed_volume}, "
        ret += f"trade_count : {self.trade_count}"
        return ret