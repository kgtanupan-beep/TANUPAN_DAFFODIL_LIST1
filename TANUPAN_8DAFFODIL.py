
items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

print("Original List:", ", ".join(items))

index = int(input("Input Index to Update: "))
new_value = input("Input New Value: ")

print("Index to Update:", index)
print("New Value:", new_value)

start = int(input("Enter Slice Range 1: "))
end = int(input("Enter Slice Range 2: "))

sliced_list = items[start:end]
print(f"Sliced List ({start}:{end}):", ", ".join(sliced_list))

search_item = input("Enter Search Item: ")

found = False
for item in sliced_list:
    if item.lower() == search_item.lower():
        found = True
        break

print("Search Result (from sliced array):")
if found:
    print(search_item, "is found in the sliced array.")
else:
    print(search_item, "is not found in the sliced array.")

if 0 <= index < len(items):
    items[index] = new_value

print("Updated List:", ", ".join(items))
