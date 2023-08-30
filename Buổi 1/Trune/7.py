if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Convert the map object to a list and remove duplicates
    unique_scores = list(set(arr))

    # Sort the unique scores in descending order
    unique_scores.sort(reverse=True)

    # The runner-up score will be the second element in the sorted list
    runner_up_score = unique_scores[1]

    print(runner_up_score)
