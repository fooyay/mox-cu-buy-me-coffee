# Deploy script for Buy Me Coffee contract

from moccasin.config import get_active_network  # type: ignore
from src import buy_me_coffee  # type: ignore
from script.deploy_mocks import deploy_price_feed
from moccasin.boa_tools import VyperContract  # type: ignore


def deploy_coffee(price_feed: str):
    print("Deploying Buy Me Coffee contract...")
    buy_me_coffee.deploy(price_feed)


def moccasin_main():
    active_network = get_active_network()
    price_feed: VyperContract = active_network.manifest_named("price_feed")
    print(f"Using price feed at {price_feed.address} on {active_network.name}")
    # price_feed: VyperContract = deploy_price_feed()
    # coffee = buy_me_coffee.deploy(price_feed)
    # print(f"Deployed Buy Me Coffee contract to {coffee.address} on {active_network.name}")

    # pick the correct price feed based on network

    # test on pyevm network

    # deploy_coffee(price_feed)
