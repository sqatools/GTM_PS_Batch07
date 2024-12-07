# If else program to assign grades as per total marks.

marks = int(input("Enter the total marks: "))
if marks > 100:
    print("Invalid marks")
elif marks > 90:
    print("Grade: Excellent")
elif marks > 80:
    print("Grade: A++")
elif marks > 70:
    print("Grade: A+")
elif marks > 60:
    print("Grade: B")
elif marks > 50:
    print("Grade: C")
else:
    print("Grade: Fail")