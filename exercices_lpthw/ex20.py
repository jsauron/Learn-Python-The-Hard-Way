# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex20.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jsauron <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/17 12:42:25 by jsauron           #+#    #+#              #
#    Updated: 2019/04/17 13:15:04 by jsauron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv #importe lib pour use argv

script, input_file = argv # set av[0] et av[1]

def print_all(f): #def a fonction avec av[1] named "f"
    print(f.read())  #print la lecture de  av[1] 

def rewind(f): # def a function pour revenir au debut du file
    f.seek(0) #seek  pour chercher , 0 le premier octet

def print_a_line(line_count, f): 
    print(line_count, f.readline(),  end = ' ') #le numero de ligne a print a la lecture du fichier

current_file = open(input_file) # ouvrire av[1] et l'assigner a une variable

print("First lets print the whole file")

print_all(current_file) #print tout le file

print("Now lets rewind, kinf of like a tape")

rewind(current_file) # revenir au debut du file

print("Lets print three line: ")

current_line = 1 

print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)

