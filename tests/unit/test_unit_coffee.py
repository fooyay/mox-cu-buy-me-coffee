from eth_utils import to_wei


def test_price_feed_is_correct(coffee, eth_usd_price_feed):
    assert coffee.PRICE_FEED() == eth_usd_price_feed.address


def test_starting_values(coffee, default_account):
    assert coffee.MINIMUM_USD() == to_wei(5, "ether")
    assert coffee.OWNER() == default_account.address
