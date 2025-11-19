#
time=17
is_hungry=False
match time:
    case 8:
        print("Breakfast")
    case 13 | 14:
        print("Lanch")
    case 17 if is_hungry:
        print("Snacks")
    case 20:
        print("Dinner")
    case _:
        print("Study")

