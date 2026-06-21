# List Uniqueness checker
# Problem: Check if all elements in a list are unique. If duplicate is found, exit the loop and print the duplicate.

items =["apple", "banana", "orange", "orange", "mango"]

# MY METHOD
# n=len(items)

# for i in range(0,n):
#     curr=items[i]
#     for k in range(0,n):
#         if(i!=k):
#             if(curr==items[k]):
#                 print(curr)
#                 break

# Method-2
unique_item=set()

for item in items:
    if (item in unique_item):
        print("Duplicate: ", item)
        break
    else:
        unique_item.add(item)    
