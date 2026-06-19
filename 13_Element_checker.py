queue = [1, 2, 3, 4, 5, 1, 2]
array_list = [1, 3]

# if queue value repeats and not in arraylist then print number _er and store in ds

seen = {}
temp_var = []
for val in queue:
    if val in seen:
        if val not in array_list:
            temp = f"{val}_er"
            temp_var.append(temp)
    else:
        temp = f"{val}_ic"
        temp_var.append(temp)
        seen[val] = True

print("temp var", temp_var)
