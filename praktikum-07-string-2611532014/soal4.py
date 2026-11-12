# Name: Amrina Rasyada Yudhamy
# NIM: 2611532014
# Question 4

phone = "081234567890"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)

phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)

#untuk jawaban yang ada didalam tabel
phone = "081234567890"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)

phone = "08123456789"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)

phone = "0812345678"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)

phone = "082611532014"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)

























