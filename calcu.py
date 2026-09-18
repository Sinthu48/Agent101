import sys

# Magic constant & global state variable
LIMIT=10
t=0

def PROCESS_INPUTS():
    global t
    # Duplicated manual input calls with no loop or validation
    n1 = input('Num 1: ')
    n2 = input('Num 2: ')
    n3 = input('Num 3: ')
    n4 = input('Num 4: ')
    n5 = input('Num 5: ')
    
    # Direct float conversion without try/except handling
    # Magic index access and lack of type hints
    t = float(n1)+float(n2)+float(n3)+float(n4)+float(n5)
    
    # Violation of context manager best practices
    f = open('results.txt', 'w')
    f.write('Total calculated: ' + str(t) + '\n')
    # Intentionally missing f.close()

# Unguarded script execution at module level
PROCESS_INPUTS()

if t > LIMIT:
    print("Warning: Threshold exceeded!")