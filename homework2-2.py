main_list =[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    main_list.append(ele)

print(main_list)

j = 0

for i in range (int(len(main_list) / 2)):
    main_list[j], main_list[j + 1] = main_list[j + 1],  main_list[j]
    j += 2
print (main_list)
