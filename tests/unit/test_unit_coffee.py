from eth_utils import to_wei
import boa  # type: ignore
from tests.conftest import SEND_VALUE

RANDOM_USER = boa.env.generate_address("non-owner")


def test_price_feed_is_correct(coffee, eth_usd_price_feed):
    assert coffee.PRICE_FEED() == eth_usd_price_feed.address


def test_starting_values(coffee, default_account):
    assert coffee.MINIMUM_USD() == to_wei(5, "ether")
    assert coffee.OWNER() == default_account.address


def test_fund_fails_with_no_eth(coffee):
    with boa.reverts("You must spend more ETH!"):
        coffee.fund()


def test_fund_fails_with_insufficient_eth(coffee):
    with boa.reverts("You must spend more ETH!"):
        coffee.fund(value=to_wei(0.001, "ether"))


def test_fund_with_money(coffee, default_account):
    boa.env.set_balance(default_account.address, SEND_VALUE * 2)
    coffee.fund(value=SEND_VALUE)
    funder = coffee.funders(0)
    assert funder == default_account.address
    assert coffee.funder_to_amount_funded(funder) == SEND_VALUE


def test_non_owner_cannot_withdraw(coffee_funded, default_account):
    with boa.env.prank(RANDOM_USER):
        with boa.reverts("Not the contract owner!"):
            coffee_funded.withdraw()


def test_owner_can_withdraw(coffee_funded):
    with boa.env.prank(coffee_funded.OWNER()):
        coffee_funded.withdraw()

    assert boa.env.get_balance(coffee_funded.address) == 0


def test_multiple_funders_and_withdraw(coffee):
    starting_balance = boa.env.get_balance(coffee.OWNER())
    # fund the contract with 10 different accounts
    for i in range(10):
        funder = boa.env.generate_address(f"funder-{i}")
        boa.env.set_balance(funder, SEND_VALUE * 2)
        with boa.env.prank(funder):
            coffee.fund(value=SEND_VALUE)

    # withdraw the funds using the owner account
    with boa.env.prank(coffee.OWNER()):
        coffee.withdraw()

    # assert ending balance is 0
    assert boa.env.get_balance(coffee.address) == 0

    # assert the balance of the owner is the sum of all the funded amounts
    expected_balance = starting_balance + (SEND_VALUE * 10)
    assert boa.env.get_balance(coffee.OWNER()) == expected_balance


def test_get_eth_to_usd_rate(coffee):
    eth_amount = to_wei(1, "ether")
    usd_rate = coffee.get_eth_to_usd_rate(eth_amount)
    # Since the mock price feed is set to $2000 per ETH with 8 decimals
    expected_usd_rate = 2000 * (10**18)
    assert usd_rate == expected_usd_rate
