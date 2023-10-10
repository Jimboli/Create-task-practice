class BulgarianSolitaire:
    def __init__(self, card_group):
        self.card_group = card_group

    def play(self):
        new_list = [len(self.card_group)]
        for item in self.card_group:
            if item > 1:
                new_list.append(item - 1)
        return BulgarianSolitaire(sorted(new_list))

    def __eq__(self, other):
        return self.card_group == other.card_group

    def __str__(self):
        return ' '.join(map(str, self.card_group))

def main():
    print("Please enter your numbers separated by spaces:")
    numbers = input().split()
    numbers = [int(num) for num in numbers if int(num) > 0]

    b1 = BulgarianSolitaire(numbers)
    
    loop = True

    while loop:
        print(b1)
        b2 = b1.play()
        if b2 == b1:
            loop = False
        else:
            b1 = b2

if __name__ == "__main__":
    main()
