list = ["V1_abcd","V2_cejn","V300_dnmewx","V300_cenjc","V301_ceiknce"]
list2=[]
list3=[]

def slipt_list():
    if len(list)!="null":
        for i in list:
            k=i.split("_")
            list2.append(k[0])
            list3.append(k[1])
    else:
        print("list is empty")

slipt_list()

for i in range(len(list2)):
    for j in range(i+1,len(list2)):
        if(list2[i]==list2[j]):
            print("SAME")
        else:
            print("Not SAME")

