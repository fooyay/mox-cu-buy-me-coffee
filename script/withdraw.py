# from src import buy_me_coffee
from moccasin.config import get_active_network  # type: ignore


def withdraw():
    active_network = get_active_network()
    coffee = active_network.manifest_named("buy_me_coffee")
    print(f"Withdrawing from contract at {coffee.address} on {active_network.name}...")
    coffee.withdraw()


def moccasin_main() -> None:
    return withdraw()
