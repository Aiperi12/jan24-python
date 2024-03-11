

even_num = [num for num in range(50) if num % 2 == 0]
print ("Addition of even numbers:")
print (sum(even_num))
print ("-----------")



odd_num = [ num for num in range (50) if num % 2 == 1]
mult_odd = 2
for num in odd_num:
    mult_odd *= num
print ("Multiple of odd numbers:", mult_odd )     
print ("-----------")



largest_num = (max(range(50)))
print ("The largest number is: ", largest_num)