# ERIC MANUEL MANZANERO
# BSCPE 2A
# SINGLY LINK LIST
# PROBLEM: 
#     CREATE A PROGRAM THAT READS STUDENTS TEST SCORES IN THE RANGE OF 0-100. IT SHOULD THEN DETERMINE THE NUMBER OF STUDENTS HAVING SCORES IN EACH OF THE FOLLOWING RANGES: 0-25, 26-50, 51-75, 76-100. OUTPUT THE SCORE RANGES AND THE NUMBER OF STUDENTS.
# CHALLENGE:
#     CREATE A LINK LIST TO STORE THE SCORES THEN CONVERT THE LINK LIST INTO LIST 

# CLASS THAT CREATES NODE OBJECT
class Node:
    def __init__(self, data, nexNode = None):
        self.data = data
        self.nextNode = nexNode

#CLASS THAT CREATE THE WHOLE LINK LIST
class linkedList:
    def __init__(self, head = None):
        self.head = head
    
    #FUNCTION FOR INSERTING DATA INTO THE LINK LIST
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node        
            return
        
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
    
    # FUNCTION THAT CONVERTS THE LINK LIST INTO A LIST    
    def linkListToList(self):
        elements = []
        currentNode = self.head
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
            elements.append(currentNode.data)
        return elements
        
        
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
    scores = linkedList() # LINK LIST THAT STORES STUDENT SCORES
     # LOOP THAT INPUTS STUDENT'S SCORE
    while True:
        try:
            score = input("INPUT Student's Score ranging from 0-100 or \"s\" to stop: ").strip()
            if score.lower() == "s":
                break
            
            score = int(score)
            if 0 <= score <= 100: # CHECK IF THE SCORE IS VALID
                scores.insert(score) # ADD THE SCORE TO THE LINK LIST
            else:
                print("Invalid Input")   
        except ValueError:
            print("Invalid input. Please enter a valid number between 0-100 or \"s\" to stop")
    
    scores = scores.linkListToList()
    
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
main()