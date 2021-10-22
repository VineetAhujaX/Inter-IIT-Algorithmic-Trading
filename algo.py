from zipline.api import order, symbol,order_target
from zipline.finance import commission, slippage
from functools import partial
from blueshift.api import (symbol, order_target, get_datetime, terminate,
                           on_data, on_trade, off_data, off_trade)

#rom blueshift.api import symbol, order_target, get_datetime, terminate, on_data, on_trade, off_data, off_trade
import talib
import numpy as np


def initialize(context):
    context.traded = False
    context.entry_price = {}
    context.order_monitors = {}
    context.order_data = {}
    context.data_monitors = {}
    context.stoploss_price = {}
    #context.stock = [symbol('FB'), symbol('ETSY'), symbol('AMD'), symbol(
     #   'AAPL'), symbol('AMZN'), symbol('MSFT'), symbol('TSLA')]
    context.stock = [symbol('ETSY'), symbol('AMD'), symbol
        ('TSLA'),symbol('TWLO'), symbol('ZIOP'),symbol('ROKU'),symbol('NKE'),symbol('DIS')]
            
    context.numberoforders = {}

    context.i = 0
    context.invested = False
    context.candle_rankings = {'CDL3LINESTRIKEBull': 1,
        'CDL3LINESTRIKEBear': 2, 'CDLEVENINGSTARBull': 4,
        'CDLEVENINGSTARBear': 4, 'CDLTASUKIGAPBull': 5, 'CDLTASUKIGAPBear':
        5, 'CDLINVERTEDHAMMERBull': 6, 'CDLINVERTEDHAMMERBear': 6,
        'CDLMATCHINGLOWBull': 7, 'CDLMATCHINGLOWBear': 7,
        'CDLABANDONEDBABYBull': 8, 'CDLABANDONEDBABYBear': 8,
        'CDLBREAKAWAYBull': 10, 'CDLBREAKAWAYBear': 10,
        'CDLMORNINGSTARBull': 12, 'CDLMORNINGSTARBear': 12,
        'CDLPIERCINGBull': 13, 'CDLPIERCINGBear': 13,
        'CDLSTICKSANDWICHBull': 14, 'CDLSTICKSANDWICHBear': 14,
        'CDLTHRUSTINGBull': 15, 'CDLTHRUSTINGBear': 15, 'CDLINNECKBull': 17,
        'CDLINNECKBear': 17, 'CDLENGULFINGBear': 18, 'CDLENGULFINGBull': 18}
    context.candle_names = ['CDL3LINESTRIKE', 'CDLEVENINGSTAR',
        'CDLTASUKIGAP', 'CDLINVERTEDHAMMER', 'CDLMATCHINGLOW',
        'CDLABANDONEDBABY', 'CDLBREAKAWAY', 'CDLMORNINGSTAR', 'CDLPIERCING',
        'CDLSTICKSANDWICH', 'CDLTHRUSTING', 'CDLINNECK', 'CDLENGULFING']
    context.candle_days = {'CDL3LINESTRIKEBull': 4, 'CDL3LINESTRIKEBear': 4,
        'CDLEVENINGSTARBull': 3, 'CDLEVENINGSTARBear': 3,
        'CDLTASUKIGAPBull': 3, 'CDLTASUKIGAPBear': 3,
        'CDLINVERTEDHAMMERBull': 2, 'CDLINVERTEDHAMMERBear': 2,
        'CDLMATCHINGLOWBull': 2, 'CDLMATCHINGLOWBear': 2,
        'CDLABANDONEDBABYBull': 3, 'CDLABANDONEDBABYBear': 3,
        'CDLBREAKAWAYBull': 5, 'CDLBREAKAWAYBear': 5, 'CDLMORNINGSTARBull':
        3, 'CDLMORNINGSTARBear': 3, 'CDLPIERCINGBull': 2, 'CDLPIERCINGBear':
        2, 'CDLSTICKSANDWICHBull': 3, 'CDLSTICKSANDWICHBear': 3,
        'CDLTHRUSTINGBull': 2, 'CDLTHRUSTINGBear': 2, 'CDLINNECKBull': 2,
        'CDLINNECKBear': 2, 'CDLENGULFINGBear': 2, 'CDLENGULFINGBull': 2}
