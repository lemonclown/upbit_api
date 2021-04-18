import requests, json
import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

from .model.coininfo import CoinInfo
from .model.minutescandle import MinutesCandle
from .model.orderresult import OrderResult
from .model.tradeinfo import TradeInfo

class UpbitApi:

    def __init__(self, access_token=None, secret_token=None):
        self.access_token = access_token
        self.secret_token = secret_token


    def set_credential(self, access_token, secret_token):
        self.access_token = access_token
        self.secret_token = secret_token


    def request_coin_info(self, isDetails:str = "false") -> list:
        '''
        거래소에 상장되어있는 코인 리스트를 가져오는 함수
        params
            - isDetails : 유의종목 필드와 같은 상세 정보 노출
        return list
            - market: 시장정보
            - korean_name: 거래대상 암호화폐 한글명
            - english_name: 거래대상 암호화폐 영문명
            - market_warning: 유의 종목 여부 (NONE, CAUTION)
        '''
        url = "https://api.upbit.com/v1/market/all"
        querystring = {"isDetails":isDetails}
        response = requests.request("GET", url, params=querystring)
        coins = [CoinInfo(coin) for coin in json.loads(response.text)]
        return coins
    
    
    def request_candle_info_by_minutes(self, market:str, minutes:int = 30, count:int = 30, to:str = None) -> list:
        '''
        분단위 캔들을 가져오는 함수
        params
            - market: 시장정보
            - minutes: 분단위
            - count: candle 수 (max:200)
            - to: yyyy-MM-dd'T'HH:mm:ss'Z' / yyyy-MM-dd HH:mm:ss
        return list
            - market: 마켓명
            - candle_date_time_utc: 캔들 기준 시각 (UTC)
            - candle_date_time_kst: 캔들 기준 시각 (KST)
            - opening_price: 시가
            - high_price: 고가
            - low_price: 저가
            - trade_price: 종가
            - timestamp: 해당 캔들에서 마지막 틱이 저장된 시각
            - candle_acc_trade_price: 누적 거래 금액
            - candle_acc_trade_volume: 누적 거래량
            - unit: 분 단위(유닛)
        '''
        url = f"https://api.upbit.com/v1/candles/minutes/{minutes}"
        querystring = {"market":market,"count":str(count)}
        if to is not None:
            querystring['to'] = to
        response = requests.request("GET", url, params=querystring)
#         candles = [MinutesCandle(candle) for candle in json.loads(response.text)]
        return json.loads(response.text)
    
    
    def request_recent_trade_info(self, market:str, to:str = None, count:int = None, cursor:str = None, daysAgo:int = None) -> list:
        '''
        return
            - trade_date_utc: 체결 일자(UTC 기준) String
            - trade_time_utc: 체결 시각(UTC 기준) String
            - timestamp: 체결 타임스탬프 Long
            - trade_price: 체결 가격 Double
            - trade_volume: 체결량 Double
            - prev_closing_price: 전일 종가 Double
            - change_price: 변화량 Double
            - ask_bid: 매도/매수 String
            - sequential_id: 체결 번호(Unique) Long
        '''
        url = "https://api.upbit.com/v1/trades/ticks"
        querystring = {}
        querystring['market'] = market
        if to is not None:
            querystring['to'] = to
        if count is not None:
            querystring['count'] = count
        if cursor is not None:
            querystring['cursor'] = cursor
        if daysAgo is not None:
            querystring['daysAgo'] = daysAgo
        response = requests.request("GET", url, params=querystring)
        trades = json.loads(response.text)
        return trades


    def request_order(self, market:str, side:str, volume:str, price:str, ord_type:str, identifier:str = None) -> dict:
        '''
        주문요청함수
        params
            - market: 시장정보
            - side: 주문타입 (bid:매수, ask:매도)
            - volume: 주문량 (지정가, 시장가 매도 시 필수)
            - price: 주문가격
            - ord_type: 주문타입(limit:지정가, price:시장가 매수, market:시장가 매도)
            - identifier(option): 조회용 사용자 지정값
        return
            - uuid: 주문 고유 아이디
            - side: 주문 종류
            - ord_type: 주문 방식
            - price: 주문당시화폐가격
            - avg_price: 체결 가격의 평균가
            - state: 주문 상태
            - market: 마켓의 유일키
            - created_at: 주문 생성 시간
            - volume: 사용자가 입력한 주문 양
            - remaining_volume: 체결 후 남은 주문 양
            - reserved_fee: 수수료로 예약된 비용
            - remaining_fee: 남은 수수료
            - paid_fee: 사용된 수수료
            - locked: 거래에 사용중인 비용
            - executed_volume: 체결된 양
            - trade_count: 해당 주문에 걸린 체결 수
        '''
        if self.access_token is None or self.secret_token is None:
            print('Error no token')
            return

        bidtype = ['bid','ask']
        if side not in bidtype:
            print(f"Invalid side type(bid/ask) : {side}")
            return False
        query = {
            'market':market,
            'side':side,
            'volume':volume,
            'price':price,
            'ord_type':ord_type
        }
        if identifier is not None:
            query['identifier'] = identifier

        access_token = self.access_token
        secret_token = self.secret_token
        jwt_token = self._generate_jwt_token(query, access_token, secret_token)
        authorize_token = f'Bearer {jwt_token}'
        headers = {"Authorization": authorize_token}

        res = requests.post("https://api.upbit.com/v1/orders", params=query, headers=headers)
        if 'error' in json.loads(res.text):
            print(res.text)
        else:
            print(res.text)
            return OrderResult(res.text)


    def request_current_snapshot(self, codes:list) -> dict:
        url = "https://api.upbit.com/v1/ticker"
        querystring = {}
        querystring['markets'] = ','.join(codes)
        response = requests.request("GET", url, params=querystring)
        return json.loads(response.text)


    def _generate_jwt_token(self, query:dict, access_key:str, secret_key:str):
        query_string = urlencode(query).encode()
        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key':access_key,
            'nonce':str(uuid.uuid4()),
            'query_hash':query_hash,
            'query_hash_alg':'SHA512'
        }

        jwt_token = jwt.encode(payload, secret_key)
        return jwt_token