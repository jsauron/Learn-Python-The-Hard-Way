# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex17.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jsauron <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/16 16:35:05 by jsauron           #+#    #+#              #
#    Updated: 2019/04/16 17:39:47 by jsauron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how ?

in_file = open(from_file)
indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")
#print(f"Does the output file exist? {exists(to_file)}")
print(f"The input file is {len(indata)} bytes long and it exist {exists(to_file)}")
#print("Read, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
