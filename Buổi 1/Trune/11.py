if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_list = tuple(integer_list)  # Convert to a tuple
    
    result = hash(tuple_list)  # Compute the hash value of the tuple
    print(result)
