number_of_rows = 4
seats_per_row = 5

# Write your code below
seating = []
for r in range(number_of_rows):
    row_list = []
    for c in range(seats_per_row):
        row_list.append(".")
    seating.append(row_list)

taken_count = 0

while True:
    for r in range(number_of_rows):
        line = f"Row {r + 1}: "
        for c in range(seats_per_row):
            line += seating[r][c] + " "
        print(line)

    row_choice = int(input("Row (0 to stop): "))
    if row_choice == 0:
        break

    seat_choice = int(input("Seat: "))

    if row_choice < 1 or row_choice > number_of_rows or seat_choice < 1 or seat_choice > seats_per_row:
        print("Invalid seat.")
    elif seating[row_choice - 1][seat_choice - 1] == "X":
        print("Seat already taken.")
    else:
        seating[row_choice - 1][seat_choice - 1] = "X"
        taken_count += 1
        print("Seat booked.")

print("Seats taken: ", taken_count)