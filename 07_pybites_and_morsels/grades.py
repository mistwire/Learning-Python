# This week I'd like you to write a percent_to_grade function which will take a 
# percentage and convert it to a grade by using a specific flavor of the A-F 
# grading system used in the US.
# The rules:
# Below 60 is F
# From 60 to below 70 is D
# From 70 to below 80 is C
# From 80 to below 90 is B
# 90 and above is A

def percent_to_grade(num_grade):
    if num_grade < 60:
        return 'F'
    elif num_grade < 70:
        return "D"
    elif num_grade < 80:
        return "C"
    elif num_grade < 90:
        return "B"
    else:
        return "A"

