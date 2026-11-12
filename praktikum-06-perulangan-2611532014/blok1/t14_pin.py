<<<<<<< HEAD
correct_pin = "1234"
MAX_ATTEMPTS = 3
attempt = 1

pin = input("Enter PIN: ")
while pin != correct_pin and attempt < MAX_ATTEMPTS:
  print("Incorrect PIN.")
  attempt += 1
  pin = input("Enter PIN: ")
if pin == correct_pin:
  print("Access granted")
else:
  print("Account locked")

=======
correct_pin = "1234"
MAX_ATTEMPTS = 3
attempt = 1

pin = input("Enter PIN: ")
while pin != correct_pin and attempt < MAX_ATTEMPTS:
  print("Incorrect PIN.")
  attempt += 1
  pin = input("Enter PIN: ")
if pin == correct_pin:
  print("Access granted")
else:
  print("Account locked")

>>>>>>> 15a643f990a229fb10923e5a4a73c7ce8adbbb2d
