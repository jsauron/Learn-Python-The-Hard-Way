# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex23.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jsauron <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/17 15:19:23 by jsauron           #+#    #+#              #
#    Updated: 2019/04/19 12:59:46 by jsauron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

def print_chr(argv*):
    while argv:
        print(chr(argv))
    """docstring for """
    
    
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
print(ord('Z'))
print(0b1011010)
print(chr(90))
print(chr(90, 101, 100, 32, 65, 46, 32, 83, 104, 97, 119))

