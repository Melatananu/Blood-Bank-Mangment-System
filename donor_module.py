file = open("donors.txt", "w")
file.write("DonorID, Name, BloodType, Age\n")
file.write("1, John Doe, A+, 30\n")
file.write("2, Jane Smith, B-, 25\n")
file.close()

print("Donor data file created successfully!")
