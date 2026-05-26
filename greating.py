greeting = input()

e_count = 0
for character in greeting:
    if character == "e":
        e_count = e_count + 1

double_e = ""
for i in range(e_count * 2):
    double_e = double_e + "e"

print("h" + double_e + "y")
