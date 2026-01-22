import pytest
from script.deploy import deploy_coffee
from script.deploy_mocks import deploy_price_feed
from moccasin.config import get_active_network  # type: ignore
from eth_utils import to_wei
import boa  # type: ignore

SEND_VALUE = to_wei(1, "ether")


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


@pytest.fixture(scope="function")
def coffee_funded(coffee, default_account):
    boa.env.set_balance(default_account.address, SEND_VALUE)
    with boa.env.prank(default_account.address):
        coffee.fund(value=SEND_VALUE)
    return coffee
