<<<<<<< HEAD
blocked_seat = 3 

for row in range(1, 4):
    print(f"Row {row}:", end=" ")
    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")
        
=======
blocked_seat = 3 

for row in range(1, 4):
    print(f"Row {row}:", end=" ")
    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")
        
>>>>>>> 15a643f990a229fb10923e5a4a73c7ce8adbbb2d
    print()  