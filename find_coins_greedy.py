def find_coins_greedy(amount: int, coins: list) -> dict:
    """
    Find coins with greedy algorithm

    Args:
        amount (int): amount to be changed
        coins (list): list of coins

    Returns:
        dict: coins to change
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
            if amount == 0:
                break
    return result
