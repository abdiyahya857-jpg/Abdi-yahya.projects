import sys

if not sys.stdin.isatty():
    text = sys.stdin.read().strip()
    abbreviation = ""
    
    for index in range(len(text)):
        if index == 0:
            abbreviation = abbreviation + text[index]
        elif text[index - 1] == "-":
            abbreviation = abbreviation + text[index]
            
    print(abbreviation)
    sys.exit()

print("=== SAMPLES ===")
sample1 = "Knuth-Morris-Pratt"
sample2 = "Mirko-Slavko"
sample3 = "Pasko-Patak"

for text in [sample1, sample2, sample3]:
    abbreviation = ""
    for index in range(len(text)):
        if index == 0:
            abbreviation = abbreviation + text[index]
        elif text[index - 1] == "-":
            abbreviation = abbreviation + text[index]
    print(text + " -> " + abbreviation)

print("\n=== YOUR TURN ===")
print("Type a name or type exit")

while True:
    user_input = input("Enter text: ")
    
    if user_input == "exit":
        break
        
    if user_input == "":
        continue
        
    abbreviation = ""
    for index in range(len(user_input)):
        if index == 0:
            abbreviation = abbreviation + user_input[index]
        elif user_input[index - 1] == "-":
            abbreviation = abbreviation + user_input[index]
            
    print("Result: " + abbreviation)
