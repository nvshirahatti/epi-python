# O(1) time,  O(1) space
def change_making(cents) -> int:
    COINS = [100, 50, 25, 10, 5, 1]
    res = 0

    for coin in COINS:
        res += cents // coin
        cents %= coin

    return res


if __name__ == "__main__":
    cents = 156
    assert change_making(cents) == 4
    print("All tests passed!")
