import os

def calculate(a, b, op):
    # CRITICAL: Use of eval() - S5876
    result = eval(f"{a} {op} {b}")
    
    # MAJOR: Print instead of log - S106
    print(f"Result: {result}")
    
    # MAJOR: Unused variable - S1481
    unused_val = 42
    
    return result

def insecure_save(data):
    # BLOCKER: Hardcoded credentials- S2068
    password = "admin_password_123"
    
    # MINOR: Magic number - S109
    if len(data) > 100:
        pass
    
    # MAJOR: Commented out code - S125
    # with open("save.txt", "w") as f:
    #     f.write(data)

# Intentional Sonar Issue: Too many parameters
def complex_function(a, b, c, d, e, f, g, h, i, j):
    return a + b
