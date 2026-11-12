# Name: Amrina Rasyada Yudhamy
# NIM: 2611532014
# Question bonus

def check_palindrome(kalimat):
  clean_str = "".join(kalimat.lower().split())
  if clean_str == clean_str[::-1]:
    return "Palindrome"
  else:
    return "Not a palindrome"



print(check_palindrome("Kasur ini rusak"))
print(check_palindrome("Algoritma"))
print(check_palindrome("Novalite"))











