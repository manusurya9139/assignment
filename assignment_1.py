# Assingment 1: get the pair of numbers such that a+b = c+d
def pair_of_numbers(arr):
    # Dictionary to store sum of pairs
    sum_dict = {}
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            sum_pair = arr[i] + arr[j]
            # Check if the sum_pair is present in dictionary
            if sum_dict.has_key(sum_pair):
                print("Output: {0} and {1}".format(sum_dict[sum_pair], (arr[i], arr[j])))
                return True
            # If sum_pair doesn't exists in dictionary
            # then add it to dictionary
            else:
                sum_dict[sum_pair] = (arr[i], arr[j])
    print("Output : No Pairs Found")
    return False
    

#driver code
if __name__ == "__main__":
    arr = [3, 4, 7, 1, 2, 9, 8]
    #arr = [65, 30, 7, 90, 1, 9, 8]
    pair_of_numbers(arr)




