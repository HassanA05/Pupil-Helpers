# program to take in 5 pupil helper names and ages and store in a list, teacher choses a number and name and age displayed

def get_pupils_info():

  
 PupilInfo = open("Pupil Helpers.csv", "r")


 pupil_helpers= []
 ages = []

 for line in PupilInfo:

  row_data_temp_list = line.split(',')
  
  pupil_helpers.append(row_data_temp_list [0])

  ages.append(int(row_data_temp_list [1]))

 PupilInfo.close()


 return ages, pupil_helpers

def get_number_helpers(pupil_helpers):
  NumberOfHelpers = len(pupil_helpers)
  return pupil_helpers, NumberOfHelpers
 
helperslist = open("HelpersContact.txt", "w")

def linear_search(NumberOfHelpers, ages):
 
 Positions = []
 position = 1
  
 for x in range(NumberOfHelpers):
    if ages[x] == 17:
      Positions.append(position)
      position = position + 1
    else: position = position + 1

 print("The position of pupils who are 17 is: ", *Positions)

 print()

 return NumberOfHelpers, ages

def get_pupil_choice(pupil_helpers, ages, NumberOfHelpers, helperslist ):

 cont = "Y"
 
 while cont != "N":
   pupil_choice = int(input("Choose a pupil number....  "))
   while not (pupil_choice>=1 and pupil_choice<=NumberOfHelpers):
          pupil_choice = int(input("Sorry! Pupil number must be between 1 and 40. Please re-enter....  "))
        
   helperslist.write(" Helper: " + pupil_helpers[pupil_choice - 1] +  "\n\n" + " Age: "  +  str(ages[pupil_choice - 1]) +  "\n\n")       
   
   if ages[pupil_choice - 1] < 14:
    helperslist.write(" Pupil too young to help at Evening Events.\n\n")
   cont = input("Do you need another pupil? Enter Y or N: ")
 print()
 print("Details have been written to file named HelpersContact.txt")

 helperslist.close()
 return


ages, pupil_helpers = get_pupils_info()
pupil_helpers, NumberOfHelpers = get_number_helpers(pupil_helpers)
NumberOfHelpers, ages = linear_search(NumberOfHelpers, ages) 
get_pupil_choice(pupil_helpers, ages, NumberOfHelpers, helperslist)


  
