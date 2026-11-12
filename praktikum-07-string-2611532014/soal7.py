# Name: Amrina Rasyada Yudhamy
# NIM: 2611532014
# Question 7

full_name = "Siti Aisyah"
nim = "2610511023"
name = full_name.strip().lower().title()

clean_name = full_name.strip()
space = clean_name.find(" ")
if space == -1:
  first_name = clean_name
else:
  first_name = clean_name[:space]
username = first_name.lower() + nim[-3:]

intake = "20" + nim[:2]
border = "=" * 30
title_card = "STUDENT CARD".center(30)

card_output = f"""{border}
{title_card}
{border}
Name      : {name}
NIM       : {nim}
Username  : {username}
Intake    : {intake}
{border}"""
print(card_output)






























