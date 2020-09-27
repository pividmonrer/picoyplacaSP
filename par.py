import datetime 
import re
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #just the weekdays
carlicplate = input("Enter your car license plate(Ex.: PQR-1234): ") #The user's input for the license plate (Current Ecuadorain format)
print("---PICO Y PLACA---\n")

y = re.match("[A-Z]{3}-[0-9]{4}$", carlicplate) #A regular expression is used to only accept inputs in a valid format according to the Ecuadorian current car license plate format 
if(y is not None):
    var = input("Enter a date (Format: YYYY-MM-DD): ") #The user's input for the date (Using the YYYY-MM-DD format)
    var = var.split("-") #to split the date in three different items: year, month and day
    year = int(var[0])
    month = int(var[1])
    day = int(var[2])

    time = input('Enter a time in the format HH:MM = ') #The user's input for the time (Using HH:MM format)
    time = time.split(":") #to split the time in two different items: hour and minutes
    hour= int(time[0])
    minutes= int(time[1])
    if(hour>0 and hour<24 and minutes>0 and minutes<60):          #checking if the values of hour and minutes are logical
        if(month>0 and month<13 and day>0 and day<32):            #checking if the values of month and day are logical
            trueDay = datetime.date(year, month, day)

            var2 = trueDay.weekday()

            theDay = days[var2]   #we use the array created at the beginning to determine the weekday
            print("The date entered is the day: ", theDay)  #just to show the day entered by the user
            print("The last number of your car license plate is: ", carlicplate[-1]) #just to show the last number of the license plate entered by the user
            print("The time you entered is: ",hour,":",minutes) #just to show the time entered by the user
            if(theDay =="Saturday" or theDay=="Sunday"):   #Saturdays and Sundays are not important because of the Pico y Placa rule (Everyone's allowed to use cars on weekends)
                print("YOU ARE ALLOWED TO USE YOUR CAR")
            elif((theDay == "Monday") and (carlicplate[-1] == "1" or carlicplate[-1]== "2") and (hour>4 and hour<19)):   #Mondays = 1 and 2 [from 5 AM to 20 PM]
                print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Tuesday") and (carlicplate[-1] == "3" or carlicplate[-1]== "4") and (hour>4 and hour<19)): #Tuesdays = 3 and 4 [from 5 AM to 20 PM]
                print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Wednesday") and (carlicplate[-1] == "5" or carlicplate[-1]== "6") and (hour>4 and hour<19)): #Wednesdays = 5 and 6 [from 5 AM to 20 PM]
                print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Thursday") and (carlicplate[-1] == "7" or carlicplate[-1]== "8") and (hour>4 and hour<19)): #Thursdays = 7 and 8 [from 5 AM to 20 PM]
             print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Friday") and (carlicplate[-1] == "9" or carlicplate[-1]== "0") and (hour>4 and hour<19)): #Fridays = 9 and 0 [from 5 AM to 20 PM]
                print("BE CAREFUL! You should not drive your car")
            else:
                print("YOU ARE ALLOWED TO USE YOUR CAR")         
        else:
            print("Error!!! Not a valid date format.")
    else:
        print("Error!!! Not a valid time format.")
else:
    print("Error!!! Not a valid car license plate format")
