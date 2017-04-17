# -*- coding: UTF-8 -*-

from nose.tools import *
from sessionid import stockdog_session_id, stockdog_chrome_version
from pystocktw.crawl import util, setting
from pystocktw.parse import helper

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_stockdog_equity_distribution():
    req_config = setting.stockdog_equity_distribution_atype(stockdog_session_id, stockdog_chrome_version)
    response = util.get(**req_config)
    atype = helper.stockdog_equity_distribution_atype(response)

    for _type in [1, 2, 3]:
        req_config = setting.stockdog_equity_distribution(stockdog_session_id, atype, 2330, _type)
        response = util.get(**req_config)
        headers, data = helper.stockdog_equity_distribution(response)

# csv
def test_twse_code():
    for typek in ['sii', 'otc']:
        req_config = setting.twse_stock_code_hidden_inputs(typek)
        response = util.post(**req_config)
        payload = helper.twse_stock_code_hidden_inputs(response)

        req_config = setting.twse_stock_code(payload)
        response = util.post(**req_config)

def test_tdcc_equity_distribution():
    req_config = setting.tdcc_equity_distribution_for_cache()
    response = util.get(**req_config)

    for date in ['20160411', '20170331']:
        req_config = setting.tdcc_equity_distribution(date, 2330)
        response = util.post(**req_config)
        helper.tdcc_equity_distribution(response)

# csv
def test_twse_warrant_info():
    for r in [1, 2]:
        req_config = setting.twse_warrant_info_hidden_inputs(r)
        response = util.post(**req_config)
        payload = helper.twse_warrant_info_hidden_inputs(response)

        req_config = setting.twse_warrant_info(payload)
        response = util.post(**req_config)


    for date in ['8903', '10604']:
        req_config = setting.twse_warrant_info_expired_hidden_inputs(1, date, date)
        response = util.post(**req_config)
        payload = helper.twse_warrant_info_hidden_inputs(response)

        req_config = setting.twse_warrant_info(payload)
        response = util.post(**req_config)

    for date in ['9301', '10604']:
        req_config = setting.twse_warrant_info_expired_hidden_inputs(2, '9301', '9301')
        response = util.post(**req_config)
        payload = helper.twse_warrant_info_hidden_inputs(response)

        req_config = setting.twse_warrant_info(payload)
        response = util.post(**req_config)

def test_twse_warrant_cancel():
    req_config = setting.twse_warrant_cancel()
    response = util.get(**req_config)
    headers, data = helper.twse_warrant_cancel(response)

# csv
def test_twse_warrant_listed_institution():
    for select2 in ['0999','0999P', '0999C', '0999B', '0999X', '0999Y']:
        for date in ['101/05/02', '106/04/05']:
            req_config = setting.twse_warrant_listed_institution(date, select2)
            response = util.post(**req_config)

# csv
def test_tpex_warrant_counter_institution():
    for se in ['EW', 'BC']:
        for date in ['96/04/23', '103/11/31', '103/12/01', '106/04/05']:
            req_config = setting.tpex_warrant_counter_institution(se, date)
            response = util.post(**req_config)
