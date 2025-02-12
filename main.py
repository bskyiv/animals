# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

from myClasses import Cat, ColorCat, Dog

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




cat1 = Cat("Kitty", 2.5)
cat2 = ColorCat("Marsik",8,"red")


dog1 = Dog("Fluffy", 4)

for animal in (cat1, cat2, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()