import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    needed_knots = [int(x) for x in input_data[1:n+1]]
    learned_knots = [int(x) for x in input_data[n+1:]]
    
    missing_knot = sum(needed_knots) - sum(learned_knots)
    print(missing_knot)

if __name__ == '__main__':
    main()
 