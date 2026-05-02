# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}


# Display original dictionary
print(f"Original Dictionary: {student}")

# Insertion
key_insert = int(input().strip())
value_insert = input().strip()
student[key_insert] = value_insert
print(f"After Insertion: {student}")

# Update
key_update = int(input().strip())
value_update = input().strip()
if key_update in student:
    student[key_update] = value_update
print(f"After Update: {student}")

# Deletion
key_delete = int(input().strip())
if key_delete in student:
    del student[key_delete]
print(f"After Deletion: {student}")

# Traversal
print("Traversing Dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")

