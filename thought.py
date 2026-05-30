solutions = {}

def evaluate_and_store(op1, op2, op3):
    expression = "4 " + op1 + " 4 " + op2 + " 4 " + op3 + " 4"
    value = eval(expression)
    
    if op1 == "//":
        print_op1 = "/"
    else:
        print_op1 = op1
        
    if op2 == "//":
        print_op2 = "/"
    else:
        print_op2 = op2
        
    if op3 == "//":
        print_op3 = "/"
    else:
        print_op3 = op3
        
    display_str = "4 " + print_op1 + " 4 " + print_op2 + " 4 " + print_op3 + " 4 = " + str(value)
    solutions[value] = display_str

evaluate_and_store("+", "+", "+")
evaluate_and_store("+", "+", "-")
evaluate_and_store("+", "+", "*")
evaluate_and_store("+", "+", "//")

evaluate_and_store("+", "-", "+")
evaluate_and_store("+", "-", "-")
evaluate_and_store("+", "-", "*")
evaluate_and_store("+", "-", "//")

evaluate_and_store("+", "*", "+")
evaluate_and_store("+", "*", "-")
evaluate_and_store("+", "*", "*")
evaluate_and_store("+", "*", "//")

evaluate_and_store("+", "//", "+")
evaluate_and_store("+", "//", "-")
evaluate_and_store("+", "//", "*")
evaluate_and_store("+", "//", "//")

evaluate_and_store("-", "+", "+")
evaluate_and_store("-", "+", "-")
evaluate_and_store("-", "+", "*")
evaluate_and_store("-", "+", "//")

evaluate_and_store("-", "-", "+")
evaluate_and_store("-", "-", "-")
evaluate_and_store("-", "-", "*")
evaluate_and_store("-", "-", "//")

evaluate_and_store("-", "*", "+")
evaluate_and_store("-", "*", "-")
evaluate_and_store("-", "*", "*")
evaluate_and_store("-", "*", "//")

evaluate_and_store("-", "//", "+")
evaluate_and_store("-", "//", "-")
evaluate_and_store("-", "//", "*")
evaluate_and_store("-", "//", "//")

evaluate_and_store("*", "+", "+")
evaluate_and_store("*", "+", "-")
evaluate_and_store("*", "+", "*")
evaluate_and_store("*", "+", "//")

evaluate_and_store("*", "-", "+")
evaluate_and_store("*", "-", "-")
evaluate_and_store("*", "-", "*")
evaluate_and_store("*", "-", "//")

evaluate_and_store("*", "*", "+")
evaluate_and_store("*", "*", "-")
evaluate_and_store("*", "*", "*")
evaluate_and_store("*", "*", "//")

evaluate_and_store("*", "//", "+")
evaluate_and_store("*", "//", "-")
evaluate_and_store("*", "//", "*")
evaluate_and_store("*", "//", "//")

evaluate_and_store("//", "+", "+")
evaluate_and_store("//", "+", "-")
evaluate_and_store("//", "+", "*")
evaluate_and_store("//", "+", "//")

evaluate_and_store("//", "-", "+")
evaluate_and_store("//", "-", "-")
evaluate_and_store("//", "-", "*")
evaluate_and_store("//", "-", "//")

evaluate_and_store("//", "*", "+")
evaluate_and_store("//", "*", "-")
evaluate_and_store("//", "*", "*")
evaluate_and_store("//", "*", "//")

evaluate_and_store("//", "//", "+")
evaluate_and_store("//", "//", "-")
evaluate_and_store("//", "//", "*")
evaluate_and_store("//", "//", "//")

input_string = input()
num_test_cases = int(input_string)

current_case = 0
while current_case < num_test_cases:
    case_input = input()
    n = int(case_input)
    
    if n in solutions:
        answer = solutions[n]
        print(answer)
    else:
        print("no solution")
        
    current_case = current_case + 1
