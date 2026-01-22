# Deploy script for Buy Me Coffee contract

from moccasin.config import get_active_network  # type: ignore
from src import buy_me_coffee  # type: ignore
from script.deploy_mocks import deploy_price_feed
from moccasin.boa_tools import VyperContract  # type: ignore


def deploy_coffee(price_feed: str) -> VyperContract:
    print("Deploying Buy Me Coffee contract...")
    coffee: VyperContract = buy_me_coffee.deploy(price_feed)

    active_network = get_active_network()
    if active_network.has_explorer() and not active_network.is_local_or_forked_network():
        print("Verifying on explorer...")
        result = active_network.moccasin_verify(coffee)
        result.wait_for_verification()
        print(f"Verification result: {result}")
    return coffee


def moccasin_main() -> VyperContract:
    active_network = get_active_network()
    price_feed: VyperContract = active_network.manifest_named("price_feed")
    print(f"Using price feed at {price_feed.address} on {active_network.name}")
    return deploy_coffee(price_feed)
