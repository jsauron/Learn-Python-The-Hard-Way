from sys import argv
    #importation de la lib sys pour use argv
script, filename = argv
    #av[0] av[1]
print(f"We are going to erase {filename}")
print("If you don't want tgat, hit CTR:-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file ..")
target = open(filename, 'w') # open avec 'w' pour write et ecrase l'ancien fichier
print("Truncatig the file. Goodbye !")
#target.truncate() #write truncate deja

target.write("\n")

print("Now im going to ask you fr three lines.")

line1 = input("line 1: ")
line2 = input("line 2; ")
line3 = input("line 3: ")

print("I'm goig to write these to the file")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)

target.write(line1 + "\n" + line2 + "\n" + line3)
#print(f"{line1}\n{line2}\n{line3}\n") #print sans passer par l'objet
print("And finnaly, we close it.")
target.close() # save et close le file

#print(open(input("filename ?"), 'r').read()) #  r pas necessaire car par defaut
#print(open(input("filename ? ")).read())
#print avec run ex16_bis.py
