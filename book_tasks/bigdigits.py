import sys

Zero  = [" *** ",
         "*   *",
         "*   *",
         "*   *",
         "*   *",
         "*   *",
         " *** "]

One   = [" * ",
         "** ",
         " * ",
         " * ",
         " * ",
         " * ",
         "***"]

Two   = [" *** ",
         "*   *",
         "*  * ",
         "  *  ",
         " *   ",
         "*    ",
         "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four  = ["    * ",
         "   ** ",
         "  * * ",
         " *  * ",
         "******",
         "    * ",
         "    * "]
Five  = ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
Six   = [" *** ",
         "*   *",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine  = [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         " *** "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
		 
numbers = sys.argv[1]

try:
    for row in range(7):
        one_string = str()
        for num in numbers:
            one_string += Digits[int(num)][row] + ' git  ' #.replace("*", num) + " "
        print(one_string)

except ValueError as incorrect_arg:
    print(incorrect_arg)

