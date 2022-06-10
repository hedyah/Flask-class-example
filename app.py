#Function needs to find the second highest number in the array

num_list = [5,15,27,39,54,99]

max_= max(num_list[0],num_list[1])
secondmax = min(num_list[0],num_list[1])

for i in range (2,len(num_list)):
        if num_list[i] > max_:
            secondmax=max_
            max_= num_list[i]
        else:
            if num_list[i]>secondmax:
                secondmax = num_list[i]

print("the second highest number in the array is: ", str(secondmax))

#class solution

def find_second(scores: list):
    scores.sort()
    scores.reverse()
    first = scores[0]
    for num in scores:
        if num != first:
            return num
        
def solution2(scores: list):
    first = -101
    second = -101
    for num in scores:
        if num> first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
        return second


list1 = [5,3,8,15,20]
list2 = [-2,-5,0,25,30]
list3 = [1,3,7,9,14]

print(find_second(list1))
print(find_second(list2))
print(find_second(list3))