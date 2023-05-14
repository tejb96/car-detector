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

    # Replace these comments with your function commenting
    def update_status(): # You may decide how to implement the arguments for this function

        looper = None
        while looper != "0":
            input1 = input("Are changes detected in the vision input?"+'\n'+ "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            if input1 == "1":
                input2 = input("What change has been identified?: ")
                if input2 == "red":
                    print("STOP")
                elif input2 == "green":
                    print("Proceed")
                elif input2 == "yellow":
                    print("Caution")
                else: print("Invalid vision change")

            elif input1 == "2":
                input3 = input("What change has been identified?: ")
                if input3 == "yes":
                    print("STOP")
                elif input3 == "no":
                    print("Proceed")
                else: print("Invalid vision change")

            elif input1 == "3":
                input4 = input("What change has been identified?: ")
                if input4 == "yes":
                    print("STOP")
                elif input4 == "no":
                    print("Proceed")
                else: print("Invalid vision change")

            elif input1 == "0":
                looper = 0
                break

            else: print("Invalid vision change") 


        



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    pass



# Complete the main function below
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

