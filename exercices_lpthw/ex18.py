# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex18.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jsauron <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/16 17:39:54 by jsauron           #+#    #+#              #
#    Updated: 2019/04/16 17:50:07 by jsauron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#this one is like your scipts wth argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 = {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1 : {arg1}, arg2:{arg2}")

#This just takes one argument
def print_one(arg1):
    print(f"arg1 : {arg1}")

#This one takes no arguments
def print_none():
    print("I got nothin'..")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First !")
print_none()
