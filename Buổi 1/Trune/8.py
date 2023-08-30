if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort students based on their scores
    students.sort(key=lambda x: x[1])

    # Find the second lowest score
    second_lowest_score = None
    for i in range(1, len(students)):
        if students[i][1] > students[0][1]:
            second_lowest_score = students[i][1]
            break

    # Collect names of students with the second lowest score
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]

    # Print names in alphabetical order
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)
