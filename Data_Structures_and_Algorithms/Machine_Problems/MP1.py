# ERIC MANUEL MANZANERO
# BSCPE 2A
# MP #1
# PROGRAM USING ARRAY
# PROBLEM: 
#     CREATE A PROGRAM THAT READS STUDENTS TEST SCORES IN THE RANGE OF 0-100. IT SHOULD THEN DETERMINE THE NUMBER OF STUDENTS HAVING SCORES IN EACH OF THE FOLLOWING RANGES: 0-25, 26-50, 51-75, 76-100. OUTPUT THE SCORE RANGES AND THE NUMBER OF STUDENTS.

# FUNCTION THAT STORES AND CLASSIFY SCORES IN DIFFERENT RANGES
def rangeClassification(scores):
    
    ranges = [0,0,0,0] # AN ARRAY THAT STORES THE SCORES IN DIFFERNT RANGES
    
    # CATEGORIZE EACH SCORE IN THEIR RANGE
    for score in scores:
        if 0 <= score <= 25: 
            ranges[0] += 1
        elif 26 <= score <= 50:
            ranges[1] += 1
        elif 51 <= score <= 75:
            ranges[2] += 1
        else:
            ranges[3] += 1 
            
    return ranges

# MAIN FUNCTION
def main():
    scores = [] # AN ARRAY THAT STORES STUDENT'S SCORES
    # LOOP THAT INPUTS STUDENT'S SCORE
    while True:
        try:
            score = input("INPUT Student's Score ranging from 0-100 or \"s\" to stop: ").strip()
            if score.lower() == "s":
                break
            
            score = int(score)
            if 0 <= score <= 100: # CHECK IF THE SCORE IS VALID
                scores.append(score) # ADD THE SCORE TO THE ARRAY
            else:
                print("Invalid Input")   
        except ValueError:
            print("Invalid input. Please enter a valid number between 0-100 or \"s\" to stop")
            
    # CATEGORE THE SCORES AND PRINT THE OUTPUT
    range = rangeClassification(scores)
    print("\nRanges and Number of Students") 
    print(f"0-25:{range[0]}")
    print(f"26-50:{range[1]}")
    print(f"51-75:{range[2]}")
    print(f"76-100:{range[3]}")
    
main()