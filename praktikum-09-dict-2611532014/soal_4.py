students = input("masukkan nomor absen seluruh kelas: ").split()
submitted = input("nomor mahasiswa yang mengumpulkan: ").split()

submitted_set = set(submitted)
not_submitted = set(students) - set(submitted)

print("submitted", len(submitted_set), "students")
print("not submitted:", len(not_submitted), "students")

for not_submit in not_submitted:
    print(not_submit)
























