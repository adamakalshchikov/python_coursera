import sys
import xml.sax.saxutils as sax
import argparse


def main():
    maxwidth = params.maxwidth
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()


def process_option():
    parser = argparse.ArgumentParser()

    parser.add_argument('-mw', '--maxwidth', type=int, default=100,
                        help="""maxwidth is an optional integer; if specofied, it sets the maximum number of characters
            that can be output for string fields.
            otherwise a default of 100 is used.""")

    parser.add_argument('-f', '--format', type=str, default=".0f",
                        help="""format is the format to use for numbers. if not specified
            it defaults ot '.0f' """)
    args = parser.parse_args()
    return args




def print_start():
    print("<table border = '1'>")


def print_end():
    print("</table>")


def print_line(line, color, maxwidth):
    print(f"<tr bgcolor='{color}'>")
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x), params.format))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                #field = sax.escape(field)
                if len(field) <= maxwidth:
                    print(f"<td>{field}</td>")
                else:
                    print(f"<td>{field:..{maxwidth}}...</td>")
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields

params = process_option()
main()
