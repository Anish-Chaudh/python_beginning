def sum_avg(list):
    total=sum(list)
    avg=total/len(list)
    return total,avg
lst=(2,3,4,8,6,7,0,19,10)
total,avg=sum_avg(lst)
print("the lst is ",lst)
print("the sum of the list is ",total)
print("the average of the list is ",avg)