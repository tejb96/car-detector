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

    # updates the instance variables based on the user input
    def update_status(self,change_type,change_occured): # change_type is the selection of light, pedestrian...and change_occured is the status
        # Nested if loops that return the updated status based on the two strings the user entered
        if change_type == "1":  # The outer if-else loop runs based on the type of change (lights, vehicle...) that was selected by the user          
            if change_occured == "red": # The inner loop has conditions based on what the change is (light turned red or other)
                self.traffic_light = change_occured 
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status] # The updated status is then returned
            elif change_occured == "green":
                self.traffic_light = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]               
            elif change_occured == "yellow":
                self.traffic_light = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]

        elif change_type == "2":            
            if change_occured == "yes":
                self.pedestrian_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
            elif change_occured == "no":
                self.pedestrian_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]

        elif change_type == "3":            
            if change_occured == "yes":
                self.vehicle_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
            elif change_occured == "no":
                self.vehicle_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
            
        else: return [self.traffic_light, self.pedestrian_status, self.vehicle_status]


# The sensor object should be passed to this function to print the action message and current status
# After inquiring about the change, the status is updated, printed and then reset to default
def print_message(sensor):
    current_status = [sensor.traffic_light, sensor.pedestrian_status, sensor.vehicle_status]
    while True:
        try:
            change_type = input("Are changes detected in the vision input?"+'\n'
                        + "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            if change_type == "0":
                break

            if change_type not in ["1" , "2" , "3"]: # Ensures only a value from the options given is entered                
                raise ValueError("You must select either 1, 2, 3, 0")  # Raises the value error

            change_occured = input("What change has been identified?: ") # Asks what the change is 
            if change_occured not in ["red" , "yellow" , "green" , "yes" , "no"]: # Checks if the input is valid                
                print("Invalid vision change.")
            else: current_status=sensor.update_status(change_type,change_occured) # updates the instance variables and returns the current status
                                                
            if current_status[0] == "red" or current_status[1] == "yes" or current_status[2] == "yes": # If lights are red or there is a passenger or vehicle       
                print('\n'+"STOP"+'\n')      # Prints course of action message          
                print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n') # Prints the current status                                
            elif current_status[0] == "yellow":     # If yellow       
                print('\n'+"Caution" + '\n')                
                print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')
            elif current_status[0] == "green" or current_status[1] == "no" or current_status[2] == "no": # If green or no pedestrian or no vehicle           
                print('\n'+"Proceed" + '\n')                
                print("Light = "+current_status[0]+", Pedestrian = " + current_status[1] + ", Vehicle = " + current_status[2] + '\n')                                                

        except ValueError as value_error:
            if str(value_error) == "Invalid vision change.":
                print()
            elif str(value_error) == "You must select either 1, 2, 3, 0":
                print("You must select either 1, 2, 3, 0"+'\n')


# Complete the main function below
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")
    sensor1 = Sensor() # Object of class Sensor initialized
    print_message(sensor1) # object passed to print_message function



# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

