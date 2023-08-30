if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Get the marks of the queried student from the dictionary
    queried_marks = student_marks[query_name]

    # Calculate the average of the marks
    average = sum(queried_marks) / len(queried_marks)
    
    # Print the average with 2 decimal places
    print("{:.2f}".format(average))
