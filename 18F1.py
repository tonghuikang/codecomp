# Python program to check whether two strings are 
# Python program to check if two strings are anagrams of 
# each other 
NO_OF_CHARS = 256
  
# Function to check whether two strings are anagram of 
# each other 
def areAnagram(str1, str2): 
  
    # Create two count arrays and initialize all values as 0 
    count1 = [0] * NO_OF_CHARS 
    count2 = [0] * NO_OF_CHARS 
  
    # For each character in input strings, increment count 
    # in the corresponding count array 
    for i in str1: 
        count1[ord(i)]+=1
  
    for i in str2: 
        count2[ord(i)]+=1
  
    # If both strings are of different length. Removing this 
    # condition will make the program fail for strings like 
    # "aaca" and "aca" 
    if len(str1) != len(str2): 
        return 0
  
    # Compare count arrays 
    for i in range(NO_OF_CHARS): 
        if count1[i] != count2[i]: 
            return 0
  
    return 1


def q1_function(L,a,b):
    result = 0
    for length_sub in range(1,L+1):
#         print("length_sub : " , length_sub)
        for position_a in range(L-length_sub+1):
#             print("pos_a : " , position_a)
            ref = a[position_a:position_a+length_sub]
            for position_b in range(L-length_sub+1):
                check = b[position_b:position_b+length_sub]
#                 print(ref,check)
                if areAnagram(ref, check):
                    result += 1
#                     print("x")
                    break
    return result


# INPUT SNIPPET FOR 18F1

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    L = int(input())
    str_a = input()
    str_b = input()
    
    result = q1_function(L, str_a, str_b)
    print("Case #{}: {}".format(i, result))