# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex19.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jsauron <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/17 11:24:47 by jsauron           #+#    #+#              #
#    Updated: 2019/04/17 11:39:04 by jsauron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def cheese_and_crackers(cheese_count, boxe_of_crackers):
    print(f"You have {cheese_count} cheeses !")
    print(f"You have {boxe_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a Blanket.\n")

print("We can just give a fonction numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too.")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
