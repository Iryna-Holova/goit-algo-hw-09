def find_min_coins(amount: int, coins: list) -> dict:
    """
    Find the minimum number of coins needed to form the given amount using
    dynamic programming.

    Args:
        amount (int): amount to be changed
        coins (list): list of available coins

    Returns:
        dict: coins to change
    """
    # dp[i] will store the minimum number of coins needed to make sum i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # To track coins used to form minimum count for each amount
    used_coins = [0] * (amount + 1)

    # Populate the dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin

    # Now reconstruct the coins used for the minimum count
    result = {}
    while amount > 0:
        coin = used_coins[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result
