import numpy as np

# ✅ Step-by-step Tasks:
# Create a NumPy array for marks.

# Calculate total and average marks for each student.

# Find the highest and lowest total scorer.

# Find the topper in each subject.

# Print students who passed (average ≥ 50).

marks = np.array([
    [87, 90, 78, 85],
    [92, 88, 95, 91],
    [56, 60, 70, 65],
    [45, 55, 48, 50],
    [75, 80, 85, 90]
])

sum = 0
total = []
average = []
for i in range (0, 5):
    sum = 0
    for item in np.nditer(marks[i]):
        sum += item
    total.append(sum)
    average.append(sum/4)

for i in range(0, 5):
    print(f"The total of roll no. {i+1} is {total[i]} and the average is {average[i]} ")

highest_total = total[0]
lowest_total = total[0]

for i in range(1,5):
    if total[i] > highest_total:
        highest_total = total[i]
    if total[i] < lowest_total:
        lowest_total = total[i]

print(f"The highest total score is {highest_total} and the lowest total score is {lowest_total}")

subjects = ['Maths', 'Physics', 'English', 'Chemistry' ]
for i in range(0,4):
    highest_in_subject = marks[0,i]
    for j, k in np.ndindex(marks.shape):
        if k == i:
            if marks[j, k] > highest_in_subject:
                highest_in_subject = marks[j, k]
    print(f"Highest marks scored in {subjects[i]} are {highest_in_subject}")

for no,i in enumerate(average):
    if i >= 50:
        print(f"Roll No. {no + 1} : Passed")
    else:
        print(f"Roll No. {no + 1} : Failed")



# Optimized NumPy Version

marks = np.array([
    [87, 90, 78, 85],
    [92, 88, 95, 91],
    [56, 60, 70, 65],
    [45, 55, 48, 50],
    [75, 80, 85, 90]
])

# calculate total and average for each student

total = np.sum(marks, axis = 1)
average = np.mean(marks, axis = 1)
print(total)
# Print Total and average

for i in range(len(marks)):
    print(f"Roll No. {i+1} -> Total : {total[i]}, Average : {average[i]:.2}")

# Find the highest and the lowest total score

highest_total = np.max(total)
lowers_total = np.min(total)

print(f"\n Highest total score : {highest_total}")
print(f"Lowest total score : {lowest_total}")

# Subject Names
subjects = ['Maths', 'Physics', 'English', 'Chemistry']

# Highest mars in each subject 
print("\nHighest marks in each subject :")
for i , subject in enumerate(subjects):
    print(f"{subject} : {np.max(marks[:,i])}")

# Pass/Fail based on average

print("\nResult Summary:")
for i, avg in enumerate(average):
    status = "Passed" if avg >= 50 else "Failed"
    print(f"Roll No. {i+1} : {status}")