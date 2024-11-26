def studentScore(marks):
    if(marks<=50):return 'D'
    elif(marks>50 and marks<60): return 'C'
    elif(marks>=60 and marks<=75): return 'B'
    else: return "A"
marks=45
print(studentScore(marks))   