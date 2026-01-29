# Read number of entries
n = int(input())

# Create the phone book (dictionary)
phone_book = {}

# Read n lines of name + phone number
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Now read queries until EOF (end of file/input)
while True:
    try:
        query = input().strip()
        
        # Check if name exists in phone book
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
            
    except EOFError:
        # This happens when there's no more input (end of queries)
        break
