# input_processing.py
# Tejpreet Bal, ENSF 592 P23
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 git repository.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self, traffic_light="green", pedestrian_status="no", vehicle_status="no"):
        self.traffic_light = traffic_light
        self.pedestrian_status = pedestrian_status
        self.vehicle_status = vehicle_status

    def reset_variables(self):
        self.traffic_light = "green"
        self.pedestrian_status = "no"
        self.vehicle_status = "no"

    # updates the status 
    def update_status(self,input1,input2): # input1 is the selection of light, pedestrian...and input2 is the status
        # Nested if loops that return the updated status based on the two strings the user entered
        if input1 == "1":            
            if input2 == "red":
                self.traffic_light = input2 
                return (self.traffic_light, self.pedestrian_status, self.vehicle_status)
            elif input2 == "green":
                self.traffic_light = input2
                return (self.traffic_light, self.pedestrian_status, self.vehicle_status)               
            elif input2 == "yellow":
                self.traffic_light = input2
                return (self.traffic_light, self.pedestrian_status, self.vehicle_status)
            else: print("Invalid vision change")

        elif input1 == "2":            
            if input2 == "yes":
                self.pedestrian_status = input2
                return (self.traffic_light, self.pedestrian_status, self.vehicle_status)
            elif input2 == "no":
                self.pedestrian_status = input2
                return (self.traffic_light, self.pedestrian_status, self.vehicle_status)
            else: print("Invalid vision change")

        elif input1 == "3":            
            if input2 == "yes":
                self.vehicle_status = input2
                return (self.traffic_light, self.pedestrian_status, self.vehicle_status)
            elif input2 == "no":
                self.vehicle_status = input2
                return (self.traffic_light, self.pedestrian_status, self.vehicle_status)
            else: print("Invalid vision change")


        


        



# The sensor object should be passed to this function to print the action message and current status
# Inquires about the change, then calls update_status() to update status and prints current status
def print_message(sensor):
    while True:
        try:
            input1 = input("Are changes detected in the vision input?"+'\n'
                        + "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            if input1 == "0":
                break

            if input1 not in ["1", "2" , "3"]:
                print()
                raise ValueError 

            input2 = input("What change has been identified?: ")
            print()                  

            if input1 == "1": # Change in light         
                if input2 == "red":        # If it is red         
                    print("STOP"+'\n')      # Prints course of action message          
                    current_status=sensor.update_status(input1,input2) # updates the instance variables and returns the current status
                    print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2]+'\n')                
                    sensor.reset_variables() # Resets instance variables to initial values after current status is printed               
                elif input2 == "green":                
                    print("Proceed" + '\n')                
                    current_status=sensor.update_status(input1,input2) # updates the instance variables and returns the current status
                    print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')                  
                    sensor.reset_variables()
                elif input2 == "yellow":            
                    print("Caution" + '\n')                
                    current_status=sensor.update_status(input1,input2) # updates the instance variables and returns the current status
                    print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')                
                    sensor.reset_variables()  # Resets instance variables to initial values after current status is printed 
                else: raise ValueError                

            elif input1 == "2": # Pedestrian
                if input2 == "yes":                
                    print("STOP" + '\n')                
                    current_status=sensor.update_status(input1,input2) # updates the instance variables and returns the current status
                    print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')                   
                    sensor.reset_variables()  # Resets instance variables to initial values after current status is printed  
                elif input2 == "no":                
                    print("Proceed" + '\n')                
                    current_status=sensor.update_status(input1,input2) # updates the instance variables and returns the current status
                    print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')                 
                    sensor.reset_variables()  # Resets instance variables to initial values after current status is printed  
                else: raise ValueError  

            elif input1 == "3": # Vehicle
                if input2 == "yes":                
                    print("STOP" + '\n')                
                    current_status=sensor.update_status(input1,input2) # updates the instance variables and returns the current status
                    print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')                 
                    sensor.reset_variables()  # Resets instance variables to initial values after current status is printed  
                elif input2 == "no":                    
                    print("Proceed" + '\n')                
                    current_status=sensor.update_status(input1,input2) # updates the instance variables and returns the current status
                    print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')                
                    sensor.reset_variables()
                else: raise ValueError   

        except ValueError:
            print("Invalid vision change"+'\n')


# Complete the main function below
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")
    sensor1 = Sensor()
    print_message(sensor1)



# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

