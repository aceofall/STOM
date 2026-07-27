
from backtest.future.backengine_future import BackEngineFuture
from utility.static_method.static_numba import get_profit_future_os_long, get_profit_future_os_short


class BackEngineFutureOversea(BackEngineFuture):
    """해외 선물 백테스트 엔진 클래스입니다.
    BackEngineFuture를 상속받아 해외 선물 시장 특화 로직을 구현합니다."""
    def _get_hogaunit(self, 주문가격):
        """호가 단위를 반환합니다."""
        return self.dict_info[self.code]['호가단위']

    def _set_buy_count(self, 계약수, 현재가, 매수가, 분할비율):
        """매수 수량을 설정합니다."""
        return int(계약수)

    def _get_order_price(self, 거래금액, 주문수량):
        """주문 가격을 계산합니다."""
        return round(거래금액 / 주문수량, self.dict_info[self.code]['소숫점자리수'])

    def _get_profit_info(self, 현재가, 매수가, 보유수량):
        """수익 정보를 계산합니다."""
        code_dict_info = self.dict_info[self.code]
        틱가치 = code_dict_info['틱가치']
        마이크로 = self.code.startswith('M') or self.code.startswith('SIL')
        매입금액 = 보유수량 * 매수가 * 틱가치
        보유금액 = 보유수량 * 현재가 * 틱가치
        위탁증거금 = 보유수량 * code_dict_info['위탁증거금']
        if self.curr_trade_info['보유중'] == 1:
            포지션 = 'LONG'
            평가금액, 수익금, 수익률 = get_profit_future_os_long(마이크로, 매입금액, 보유금액, 위탁증거금)
        else:
            포지션 = 'SHORT'
            평가금액, 수익금, 수익률 = get_profit_future_os_short(마이크로, 매입금액, 보유금액, 위탁증거금)
        return 포지션, 평가금액, 수익금, 수익률
