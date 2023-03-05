def calc_average(scores):
    return sum(scores) / len(scores)

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def repeat():
    return input("Do you want to do another calculation?")

scores = []
for i in range(5):
    score = float(input("Enter test score: "))
    scores.append(score)
    print(f"Grade for test {i+1}: {determine_grade(score)}")

average_score = calc_average(scores)
print(f"Average test score: {average_score}")
while repeat ():
    scores = []
    for i in range(5):
        score - float(input("Enter test score: "))
        scores.append(score)
        print(f"Grade for test{i+1}: {determine_grade(score)}")
    average_score = calc_average(scores)
    print(f"Average test score: {average_score}")
    
