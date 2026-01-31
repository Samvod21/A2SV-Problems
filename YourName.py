def print_full_name(first, last):
    charin = ["Hello", first, last]
    name = " ".join(charin) + "!"

    return name


first_name = input()
last_name = input()
print(print_full_name(first_name, last_name))
#15 3