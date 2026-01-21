import pytest
from script.deploy import deploy_coffee
from script.deploy_mocks import deploy_price_feed


@pytest.fixture(scope="session")
def eth_usd_price_feed():
    return deploy_price_feed()


@pytest.fixture(scope="function")
def coffee(eth_usd_price_feed):
    return deploy_coffee(eth_usd_price_feed)
