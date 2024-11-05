from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins
from tabulate import tabulate


def main():
    """
    Main function
    """
    while True:
        try:
            amount = int(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()

    # Different coin sets to test
    coins = [[50, 25, 10, 5, 2, 1], [10, 6, 1]]

    # Preparing data for the table
    table_data = []
    for coins_list in coins:
        result_greedy = find_coins_greedy(amount, coins_list)
        result_dynamic = find_min_coins(amount, coins_list)

        # Calculate total number of coins
        total_greedy = sum(result_greedy.values())
        total_dynamic = sum(result_dynamic.values())

        # Add rows for each algorithm and coin set
        table_data.append([
            str(coins_list),
            "Greedy",
            result_greedy,
            total_greedy
        ])
        table_data.append([
            str(coins_list),
            "Dynamic",
            result_dynamic,
            total_dynamic
        ])

    # Display results in a formatted table
    headers = ["Coin Set", "Algorithm", "Coins Used", "Total Coins"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
