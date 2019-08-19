name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'
conv_h = 2.54
conv_w = 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pound heavy.")
print("Actually that's not too heavy!")
print(f"He's got {eyes} eyes ans {hair} hair.")
print(f"His teeth are usually {teeth} depending on the cofee.")

#this line is tricky, try to get it exactly right

total = age + height + weight
cm = height * conv_h
kilo = weight * conv_w
print(f"if i add {age}, {height}, and {weight} I get {total}.")
print("my height  in cm is ", round(cm), ".")
print ("my weight  in kilograms is ", round(kilo), ".")
