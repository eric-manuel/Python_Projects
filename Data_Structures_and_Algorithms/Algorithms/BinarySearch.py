# ERIC MANUEL MANZANERO
# BSCPE 2A
# BINARY SEARCH
# PROBLEM: 
#     CREATE A PROGRAM THAT READS STUDENTS TEST SCORES IN THE RANGE OF 0-100. IT SHOULD THEN DETERMINE THE NUMBER OF STUDENTS HAVING SCORES IN EACH OF THE FOLLOWING RANGES: 0-25, 26-50, 51-75, 76-100. OUTPUT THE SCORE RANGES AND THE NUMBER OF STUDENTS.
# CHALLENGE:
#     SORT THE RANGES FROM HIGHEST FREQUENCY TO LOWEST FREQUENCY AND APPLY BINARY SEARCH TO FIND THE FREQUENCY GIVEN THE RANGE

# FUNCTION THAT SEARCH THE FREQUENCY GIVEN THE RANGE
pos = -1
def binarySearch(scores, inputScore):
    beginIndex = 0
    endIndex = len(scores) - 1
    
    while beginIndex <= endIndex:
        midPoint = (beginIndex + endIndex) // 2
        if scores[midPoint] == inputScore:
            globals() ['pos'] = midPoint
            return globals() ['pos']
        elif scores[midPoint] < inputScore:
            beginIndex = midPoint
        else:
            endIndex = midPoint
    
# FUNCTION THAT FIND THE RANGE OF THE GIVEN SCORE    
def scoreClassification(inputScore):
    if 0 <= inputScore <= 25: 
        return "0-25"
    elif 26 <= inputScore <= 50: 
        return "26-50"
    elif 51 <= inputScore <= 75: 
        return "51-75"
    elif 75 <= inputScore <= 100: 
        return "76-100"
        
# FUNCTION THAT SORTS THE SCORES FROM LARGEST TO SMALLEST USING INSERTION SORT
def insertionSort(unsortedScores):
    unsortedScores = list(unsortedScores)# CONVERT THE DICTIONARY INTO LIST
    indexingLength = range(1, len(unsortedScores))
    for i in indexingLength: # ITERATE FOR EVERY VALUE BETWEEN 1 AND THE LENGHT OF UNSORTED RANGES
        valueToSort = unsortedScores[i] # FIRST VALUE IN THE UNSORTED REGION 
        while unsortedScores[i-1] > valueToSort and i>0: # COMPARE THE VALUES BETWEEN THE FIRST VALUE AND THE VALUE IN ITS IMMEDIATE LEFT
            unsortedScores[i], unsortedScores[i-1] = unsortedScores[i-1], unsortedScores[i] # CHANGE THE POSITION OF THE VALUES
            i = i-1 
    return unsortedScores   
        
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
    
    # SORT THE SCORES FORM HIGHEST TO LOWEST VALUE
    sortedScores = insertionSort(scores)
    
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
    
    # FINDING THE POSITION OF THE SCORE 
    scoreInput = int(input("\nEnter the score you want to find: "))
    position = binarySearch(sortedScores, scoreInput)
    
    # FINDING THE RANGE IN WHICH THE SCORE BELONG
    rangeOfScore = scoreClassification(scoreInput)
  
    # PRINT THE POSTION AND THE RANGE IN WHICH THE SCORE BELONG
    print(f"\nThe position of {scoreInput} is {position+1}")
    print(f"The score {scoreInput} is within the range {rangeOfScore}")
main()