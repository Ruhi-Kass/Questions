def mutate_string(string, position, character):
    # Convert string to list (strings are immutable)
    s_list = list(string)
    
    # Change the character at the given position
    s_list[position] = character
    
    # Join back into a string
    return ''.join(s_list)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    i = int(i)  # convert position to integer
    
    result = mutate_string(s, i, c)
    print(result)
