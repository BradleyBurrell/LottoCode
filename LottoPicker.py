import random
import datetime


def lotto_number_picker():
    will_win = False
    main_numbers = []
    star_numbers = []

    while will_win is False:
        will_win = bool(random.Random(int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))).getrandbits(1))
        if will_win is True:
            while len(main_numbers) <= 4:
                main_number = random.Random(int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))).randrange(1, 51)
                if main_number in main_numbers:
                    pass
                else:
                    main_numbers.append(main_number)
            while len(star_numbers) <= 1:
                star_number = random.Random(int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))).randrange(1, 13)
                if star_number in star_numbers:
                    pass
                else:
                    star_numbers.append(star_number)

    print("Lotto Numbers:")
    for main_number_p in sorted(main_numbers):
        print('\t{}'.format(main_number_p))
    print("Lucky Star Numbers:")
    for star_number_p in sorted(star_numbers):
        print('\t{}'.format(star_number_p))


lotto_number_picker()
