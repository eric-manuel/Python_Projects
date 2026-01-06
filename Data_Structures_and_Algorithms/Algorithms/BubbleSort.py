# ERIC MANUEL MANZANERO
# BSCPE 2A
# BUBBLE SORT
# PROBLEM: 
#     CREATE A PROGRAM THAT READS STUDENTS TEST SCORES IN THE RANGE OF 0-100. IT SHOULD THEN DETERMINE THE NUMBER OF STUDENTS HAVING SCORES IN EACH OF THE FOLLOWING RANGES: 0-25, 26-50, 51-75, 76-100. OUTPUT THE SCORE RANGES AND THE NUMBER OF STUDENTS.
# CHALLENGE:
#     IMPLEMENT BUBBLE SORT IN THIS PROGRAM


# FUNCTION THAT SORTS THE RANGES FROM LARGEST TO SMALLEST USING BUBBLE SORT
def bubbleSort(unsortedRanges):
    unsortedRanges = list(unsortedRanges)# CONVERT THE DICTIONARY INTO LIST
    indexingLength = len(unsortedRanges)-1
    Sorted = False
    while not Sorted: # ITERATE WHILE Sorted = FALSE   
        Sorted = True # BREAK THE LOOP IF THE LIST IS IN ORDER      
        for i in range(0, indexingLength):
            if unsortedRanges[i][1] > unsortedRanges[i+1][1]:
                Sorted = False # THE VALUES ARE UNSORTED
                unsortedRanges[i], unsortedRanges[i+1] = unsortedRanges[i+1], unsortedRanges[i] # CHANGE THE POSITION OF THE TWO VALUES
    return unsortedRanges   
        
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
            
    # CLASSIFY EACH SCORES IN THEIR RESPECTIVE RANGES
    classifiedScores = rangeClassification(scores)
    
    # DICTIONARY FOR RANGES AND ITS FREQUENCY 
    range_numberOfStudent = {
        "0-25":classifiedScores[0],
        "26-50":classifiedScores[1],
        "51-75":classifiedScores[2],
        "76-100":classifiedScores[3]
        }
    
    # PRINT THE RANGES AND ITS FREQUENCY
    print("\nOUTPUT:\nRanges and Number of Students") 
    print(f"0-25:{classifiedScores[0]}")
    print(f"26-50:{classifiedScores[1]}")
    print(f"51-75:{classifiedScores[2]}")
    print(f"76-100:{classifiedScores[3]}")
    
    # SORT THE RANGES AND PRINT THE OUTPUT
    sortedRanges = bubbleSort(range_numberOfStudent.items())
    print("\nRanges that are sorted from largest to smallest")
    print(f"{sortedRanges[3][0]}:{sortedRanges[3][1]}")
    print(f"{sortedRanges[2][0]}:{sortedRanges[2][1]}")
    print(f"{sortedRanges[1][0]}:{sortedRanges[1][1]}")
    print(f"{sortedRanges[0][0]}:{sortedRanges[0][1]}")
  
main()