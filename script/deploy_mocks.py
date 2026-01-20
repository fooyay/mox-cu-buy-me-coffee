# deploy script for the price feed

from src.mocks import mock_v3_aggregator  # type: ignore
from moccasin.boa_tools import VyperContract  # type: ignore

STARTING_DECIMALS = 8
STARTING_PRICE = int(2000e8)  # $2000 per ETH


def deploy_price_feed() -> VyperContract:
    mock_price_feed = mock_v3_aggregator.deploy(STARTING_DECIMALS, STARTING_PRICE)
    print(f"Deployed mock price feed to {mock_price_feed.address}")
    return mock_price_feed


def moccasin_main() -> VyperContract:
    return deploy_price_feed()
