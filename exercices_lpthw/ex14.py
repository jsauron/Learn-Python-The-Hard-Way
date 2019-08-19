from sys import argv

script, user_name, p = argv

print(f"hi {user_name}, i'm the script {script} !")
print("I'd like to ask you a few question")
print(f"Do you like me {user_name}?")
likes = input(p)

print(f"Where do you live {user_name}?")
lives = input(p)

print("What kind of computer do you have?")
computer = input(p)

print(f"""
Alright , so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice !
""")
