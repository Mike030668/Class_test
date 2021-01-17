import random
class Dice:
    def __init__(self, N):
        self.trrow_num = N
        self.current_throw = 0

    def set_hidden_numbers(self):
        self._hidden_num_1 = random.randint(1,6)
        self._hidden_num_2 = random.randint(1,6)

    def throw_dices(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        self.current_throw += 1
        if self.current_throw > self.trrow_num:
            raise Exception('Вы превысили к-во попыток')

        if (dice_1, dice_2) == {self._hidden_num_1, self._hidden_num_2}:
            return True
        else:
            return False

if __name__ == '__main__':
    dice_game = Dice(4)
    dice_game.set_hidden_numbers()
    print(dice_game._hidden_num_1,dice_game._hidden_num_2)
    for i in range(6):
        try:
            print(dice_game.throw_dices())
        except:
            print('game over')