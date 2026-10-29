# (a) Profile card output
name = "Sok Dara"
age = 25
major = "Data Science"
GPA = 3.9

print("====================================================")
print("Name  :", name)
print("Age   :", age)
print("Major :", major)
print(f"GPA   : {GPA:.2f}")

# (b) Printing values with their type names using type(value).__name__
print("====================================================")
print(f"{name} -> {type(name).__name__}")
print(f"{age} -> {type(age).__name__}")
print(f"{major} -> {type(major).__name__}")
print(f"{GPA:.2f} -> {type(GPA).__name__}")

# (c) Dynamic typing demonstration by re-assigning age
print("====================================================")
age = "20"
print(f"Re-assigned age: {age} -> {type(age).__name__}")

"""
What this tells us about dynamic typing in Python:
Variables in Python are just names/labels attached to objects. The type belongs to the value itself, 
not the variable name. Therefore, a variable can refer to an integer (`int`) at one point and be re-assigned 
to a string (`str`) later without explicit type declarations or compilation errors.
"""