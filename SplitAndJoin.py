def split_and_join(line):
    # write your code here
    words = line.split(" ")
    result = "-".join(words)
    
    return result

print(split_and_join("I am Samuel"))
#10