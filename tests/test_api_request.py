from coinzo.api import coinzo
from coinzo.exceptions import HTTPBadRequest, BadResponse
import pytest
import requests_mock

coinzo = coinzo("api_key", "api_secret")


def test_invalid_json():
    """Test Invalid response Exception"""

    with pytest.raises(BadResponse):
        with requests_mock.mock() as m:
            m.get("https://api.coinzo.com/tickers", text="<head></html>")
            coinzo.get_all_tickers()


def test_api_exception():
    """Test API response Exception"""

    with pytest.raises(HTTPBadRequest):
        with requests_mock.mock() as m:
            json_obj = {"code": 1002, "msg": "Invalid API call"}
            m.get(
                "https://api.coinzo.com/ticker?pair=BTC-TRY",
                json=json_obj,
                status_code=400,
            )
            coinzo.get_ticker("BTC-TRY")


def test_api_exception_invalid_json():
    """Test API response Exception"""

    with pytest.raises(HTTPBadRequest):
        with requests_mock.mock() as m:
            not_json_str = "<html><body>Error</body></html>"
            m.get(
                "https://api.coinzo.com/ticker?pair=BTC-TRY",
                text=not_json_str,
                status_code=400,
            )
            coinzo.get_ticker("BTC-TRY")


# def test_withdraw_api_exception():
#     """Test Withdraw API response Exception"""

#     with pytest.raises(BinanceWithdrawException):

#         with requests_mock.mock() as m:
#             json_obj = {"success": False, "msg": "Insufficient funds"}
#             m.register_uri("POST", requests_mock.ANY, json=json_obj, status_code=200)
#             client.withdraw(asset="BTC", address="BTCADDRESS", amount=100)

