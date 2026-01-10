students = {"Yash":"Sonipat",
            "Palak":"Rohini",
            "Medha":"Vikaspuri",
            "Aditya":"Najafgarh"
            }


# print(students["Yash"])
# print(students["Aditya"])

for student in students:
  # print(student)       #iterates over all the keys not values 
  print(student , students[student] , sep=":")       #iterates over all the keys not values 
