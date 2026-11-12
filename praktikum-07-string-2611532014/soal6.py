# Name: Amrina Rasyada Yudhamy
# NIM: 2611532014
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())




full_name = "Amrina Rasyada Yudhamy"
nim = "2611532014"

clean_name = full_name.strip()
space = clean_name.find(" ")

if space == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space]
last_3_nim = nim[-3:]

username = first_name.lower() + last_3_nim
print(username)










































