# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex17_shortV.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jsauron <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/16 17:28:34 by jsauron           #+#    #+#              #
#    Updated: 2019/04/16 17:50:09 by jsauron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from os.path import exists

script, from_file, to_file = argv
open(to_file, 'w').write(open(from_file).read())

