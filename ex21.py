# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex21.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jsauron <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/17 14:48:29 by jsauron           #+#    #+#              #
#    Updated: 2019/04/17 15:02:13 by jsauron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
def what(age, height, weight, iq):
    print("WTFFF")
    return add(age, substract(height, multiply(weight, divide(iq, 2))))

print("Let's do some math with just functions !")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, weight: {weight}, IQ: {iq}")

# A puzzzle for the extra credit, type it in anyway.
print("here is a puzzle")

wat = add(age, substract(height, multiply(weight, divide(iq, 2))))
wtf = what(age, height, weight, iq)
print("That become : ", wat, "Can you do it by hand?")
print(f"wtf = {wtf}")
