# Simple Grade Calculator

# Get student details
name = input("Enter student name: ")
subject = input("Enter subject: ")

# Get three grades and ensure input validation
try:
    grade1 = float(input("Enter first grade: "))
    grade2 = float(input("Enter second grade: "))
    grade3 = float(input("Enter third grade: "))

    # Compute average grade
    average = (grade1 + grade2 + grade3) / 3

    # Display results
    print("\nStudent Report Card")
    print(f"Student: {name}")
    print(f"Subject: {subject}")
    print(f"Average Grade: {average:.2f}")

    # Determine pass or fail status
    if average >= 75:
        print("✅ Status: Passed")
    else:
        print("❌ Status: Failed")

except ValueError:
    print("Error: Please enter valid numeric grades.")



