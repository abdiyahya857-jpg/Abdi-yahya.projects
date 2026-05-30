

  solutions = {}

def evaluate_and_store(op1, op2, op3):
    expression = "4 " + op1 + " 4 " + op2 + " 4 " + op3 + " 4"
    value = eval(expression)

    print_op1 = "/" if op1 == "//" else op1
    print_op2 = "/" if op2 == "//" else op2
    print_op3 = "/" if op3 == "//" else op3

    display_str = (
        "4 " + print_op1 +
        " 4 " + print_op2 +
        " 4 " + print_op3 +
        " 4 = " + str(value)
    )

    solutions[value] = display_str

operators = ["+", "-", "*", "//"]

for op1 in operators:
    for op2 in operators:
        for op3 in operators:
            evaluate_and_store(op1, op2, op3)

num_test_cases = int(input())

for _ in range(num_test_cases):
    n = int(input())

    if n in solutions:
        print(solutions[n])
    else:
        print("no solution")