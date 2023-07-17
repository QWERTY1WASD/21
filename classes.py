class Player:
    def __init__(self, name: str, money: int) -> None:
        self.name = name
        self.money = money
        self.wins = 0

    @property
    def get_name(self) -> str:
        return self.name

    @property
    def get_money(self) -> int:
        return self.money

    @property
    def get_wins(self) -> int:
        return self.wins

    def increase_wins(self) -> None:
        self.wins += 1

    def rename(self, new_name: str) -> None:
        self.name = new_name

    def get_money(self, money: int) -> None:
        self.money += money

    def lose_money(self, money: int) -> None:
        self.get_money(-money)

    def get_one_hundred(self) -> None:
        if self.money < 100:
            self.money += 100
