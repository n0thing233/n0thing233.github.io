#https://aonecode.com/amazon-online-assessment-winning-sequence
#time:O(1)
#space:O(1)
def get_max_array(n,lower,upper):
    if (upper-lower)*2+1 < n:
        return None
    if n < 3:
        return None
    if n >= (upper-lower+2):
        return ([i for i in range((upper-(n-(upper-lower+1))),upper)]+[i for i in range(lower,(upper+1))][::-1])
    return ([upper-1,upper] + [i for i in range(upper-(n-2),upper)][::-1])

#test case
print(get_max_array(4,10,12)) #[11, 12, 11, 10]
print(get_max_array(6,1,3)) #None
print(get_max_array(5,1,4)) #[3,4,3,2,]
print(get_max_array(5, 3, 10)) #[9, 10, 9, 8, 7]
print(get_max_array(7, 3, 10)) #[9, 10, 9, 8, 7, 6 ,5]
print(get_max_array(10, 3, 10)) #[8, 9, 10, 9, 8, 7, 6, 5, 4, 3]
print(get_max_array(15, 3, 10)) #[3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3]
print(get_max_array(16, 3, 10)) #null
print(get_max_array(5, 1, 3)) #[1, 2, 3, 2, 1]
print(get_max_array(3, 1, 3)) #[2, 3, 2]
print(get_max_array(5, 9, 10)) #null
print(get_max_array(5, 10, 10)) #null
