import datetime 
import re
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #just the weekdays
carlicplate = input("Enter your car license plate(Ex.: PQR-1234): ") #The user's input for the license plate (Current Ecuadorain format)


y = re.match("[A-Z]{3}-[0-9]{4}$", carlicplate) #A regular expression is used to only accept inputs in a valid format according to the Ecuadorian current car license plate format 
if(y is not None):
    var = input("Enter a date (Format: YYYY-MM-DD): ") #The user's input for the date (Using the YYYY-MM-DD format)
    var = var.split("-") 
    year = int(var[0])
    month = int(var[1])
    day = int(var[2])

    time = input('Enter a time in the format HH:MM = ')
    time = time.split(":")
    hour= int(time[0])
    minutes= int(time[1])
    if(hour>0 and hour<24 and minutes>0 and minutes<60):
        if(month>0 and month<13 and day>0 and day<32):
            trueDay = datetime.date(year, month, day)

            var2 = trueDay.weekday()

            theDay = days[var2]
            print("The date entered is the day: ", theDay)
            print("The last number of your car license plate is: ", carlicplate[-1])
            print("The time you entered is: ",hour,":",minutes)
            if(theDay =="Saturday" or theDay=="Sunday"):
                print("YOU ARE ALLOWED TO USE YOUR CAR")
            elif((theDay == "Monday") and (carlicplate[-1] == "1" or carlicplate[-1]== "2") and (hour>4 and hour<19)):
                print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Tuesday") and (carlicplate[-1] == "3" or carlicplate[-1]== "4") and (hour>4 and hour<19)):
                print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Wednesday") and (carlicplate[-1] == "5" or carlicplate[-1]== "6") and (hour>4 and hour<19)):
                print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Thursday") and (carlicplate[-1] == "7" or carlicplate[-1]== "8") and (hour>4 and hour<19)):
             print("BE CAREFUL! You should not drive your car")
            elif((theDay == "Friday") and (carlicplate[-1] == "9" or carlicplate[-1]== "0") and (hour>4 and hour<19)):
                print("BE CAREFUL! You should not drive your car")
            else:
                print("YOU ARE ALLOWED TO USE YOUR CAR")         
        else:
            print("Error!!! Not a valid date format.")
    else:
        print("Error!!! Not a valid time format.")
else:
    print("Error!!! Not a valid car license plate format")
