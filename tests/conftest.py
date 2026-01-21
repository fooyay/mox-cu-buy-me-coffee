import pytest
from script.deploy import deploy_coffee
from script.deploy_mocks import deploy_price_feed
from moccasin.config import get_active_network  # type: ignore


@pytest.fixture(scope="session")
def default_account():
    active_network = get_active_network()
    return active_network.get_default_account()


@pytest.fixture(scope="session")
def eth_usd_price_feed():
    return deploy_price_feed()


@pytest.fixture(scope="function")
def coffee(eth_usd_price_feed):
    return deploy_coffee(eth_usd_price_feed)
