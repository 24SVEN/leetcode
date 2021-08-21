#Write a function solution that, given an integer N, returns the maximum possible value obtained by inserting one '5' digit inside the decimal representation of integer N.
#Examples:
#1. Given N=268, the function should return 5268
#2. Given N=670, the function should return 6750
#3. Given N=0, the function should return 50
#4. Given N=-999, the function should return -5999

#Assume that:
#N is an integer within the range [-8, 000.. 8,000].

#In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment


# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")


def max_int(test_int):
    #
    #
    
    str_int = str(test_int)
    
    if str_int[0] == '-':

        str_int = str_int[1:len(str_int)]

        temp_str = '5' + str_int
        max_int = int(temp_str)

        for i in range(len(str_int)):
            #5 + 268
            comp_str = str_int[0:(i+1)] + '5'+ str_int[i+1:len(str_int)]
            #print(comp_str)
            comp_int = int(comp_str)
            if comp_int < max_int:
                max_int = comp_int
        
        hold_max = '-' + str(max_int)
        max_int = int(hold_max)

    else:

        temp_str = '5' + str_int
        max_int = int(temp_str)

        for i in range(len(str_int)):
            #5 + 268
            comp_str = str_int[0:(i+1)] + '5'+ str_int[i+1:len(str_int)]
            #print(comp_str)
            comp_int = int(comp_str)
            if comp_int > max_int:
                max_int = comp_int

    
    return max_int

print('answer is ' + str(max_int(268)))
print('answer is ' + str(max_int(670)))
print('answer is ' + str(max_int(0)))
print('answer is ' + str(max_int(-999)))
