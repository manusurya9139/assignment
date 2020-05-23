# Assingment 3: Get the max length substring without repeating characters
def max_length_substr(string):
    n = len(string)
    max_len = 0
    substr=""
    i = 0
    while n >= i:
        for j in range(i+1, n):
            print substr
            if string[j] not in substr:
                substr= substr + string[j]
            	max_len = max(max_len, len(substr))
            else:
               substr=""
               i=j-1
        i += 1
    return max_len

if __name__ == "__main__":
    string = raw_input("Type a string: ")
    max_len = max_length_substr(string)
    print "Output: {}".format(max_len)

