
def calculate_grade(score, extra_credit):
    # Intentional Unused Local Variable to trigger Sonar S1481
    unused_grading_curve = 1.05
    
    if score >= 90:
        print("Grade is A") # Intentional Print S106
        return "A"
    elif score >= 80:
        print("Grade is B")
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
