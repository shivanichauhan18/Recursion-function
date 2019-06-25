count_occures=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
big_list=[]
while i<len(count_occures):
    j=1
    new_list=[]
    count=0
    while j<len(count_occures):
        if count_occures[i]==count_occures[j]:
            count=count+1
            count_occures.remove(count_occures[j])
                continue
        j=j+1
    new_list.append([count_occures[i],count])
    big_list.append(new_list)
    i=i+1
print big_list