def count(str1, str2):
    set_string1 = set(str1)
    set_string2 = set(str2)
    matched_characters = set_string1 & set_string2
    print(matched_characters)
    #str convert to string
    #len return intergervalue
    #problem string + int
    #print("No. of matching characters are : " + len(matched_characters))
    #the solutions are :
    #1-print("No. of matching characters are : " , len(matched_characters))
    #2-print("len(matached_characters)

    print("No. of matching characters are : " + str(len(matched_characters)) )
    print("No. of matching characters are : " , len(matched_characters))


while 1:
    str1 = input("first string:")
    str2 = input("second string:")
    count(str1, str2)
