n = int(input())
students = list(map(int, input().split()))
students.sort()
problems_solved = 0

i = 0
while i < n:
    diff = abs(students[i] - students[i+1])
    problems_solved += diff
    i += 2

print(problems_solved)
