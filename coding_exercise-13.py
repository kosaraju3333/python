

# dimension=input("Enter the 3/3 array dimension like 32 or 33 12 23 etc.. we will replace that place with X: ")
# list_index=int(dimension[0])
# sub_list_index=int(dimension[1])
#
# list_index=list_index-1
# sub_list_index=sub_list_index-1
#
# list=[[1,1,1],[1,1,1],[1,1,1]]
# length_list=len(list)
#
# list[list_index][sub_list_index]='x'
#
# print(f"{list[0]}\n{list[1]}\n{list[2]}")


###########################################################

#### This is proper  way to write program

row1=['😀','😀','😀']
row2=['😀','😀','😀']
row3=['😀','😀','😀']
metrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Enter the Position where you want to hide money: ")
row_number=int(position[0])
column_number=int(position[1])

row_selected=metrix[row_number-1]
row_selected[column_number-1]='x'

print(f"{row1}\n{row2}\n{row3}")



