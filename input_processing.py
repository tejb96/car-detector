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
    def __init__(
        self, traffic_light="green", pedestrian_status="no", vehicle_status="no"
    ):
        # Assign default values to instance variables
        self.traffic_light = traffic_light
        self.pedestrian_status = pedestrian_status
        self.vehicle_status = vehicle_status

    # updates the instance variables based on the user input
    # change_menu_input is the menu input, and change_occured is the change such as red for light
    def update_status(self, change_menu_input, change_occured):
        # Nested if loops that return the updated status based on the two strings the user entered
        # The outer if-else loop runs based on the menu selection (lights, vehicle...)
        if change_menu_input == "1":
            # The inner loop has conditions based on what the change is (light turned red or other)
            if change_occured == "red":
                # The respective instance variable is pointed to the new value
                self.traffic_light = change_occured
                # The updated status is then returned
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
            elif change_occured == "green":
                self.traffic_light = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
            elif change_occured == "yellow":
                self.traffic_light = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
        # If pedestrian is selected
        elif change_menu_input == "2":
            if change_occured == "yes":
                self.pedestrian_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
            elif change_occured == "no":
                self.pedestrian_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
        # If vehicle is selected
        elif change_menu_input == "3":
            if change_occured == "yes":
                self.vehicle_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]
            elif change_occured == "no":
                self.vehicle_status = change_occured
                return [self.traffic_light, self.pedestrian_status, self.vehicle_status]


# The sensor object should be passed to this function to print the action message and current status
# After inquiring about the change, the status is updated, printed and then reset to default
def print_message(sensor):
    # If the input is invalid, the code will run without updating current_status
    current_status = [
        sensor.traffic_light,
        sensor.pedestrian_status,
        sensor.vehicle_status,
    ]
    # Infinite loop only broken when user enters 0
    while True:
        # try block
        try:
            # Asks user to select from the menu and assigns input to change_menu_input as a string
            change_menu_input = input(
                "Are changes detected in the vision input?"
                + "\n"
                + "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "
            )
            # If the user enteres 0, the program is terminated using break
            if change_menu_input == "0":
                break

            # Ensures only a value from the options given is entered
            if change_menu_input not in ["1", "2", "3"]:
                # Raises the value error
                raise ValueError("You must select either 1, 2, 3, 0")

            # Asks what the change is, and change_occured is assigned the input
            change_occured = input("What change has been identified?: ")
            # If the input is invalid, the message is displayed and the status is not updated
            if change_menu_input == "1" and change_occured not in [
                "red",
                "yellow",
                "green",
            ]:
                print("Invalid vision change.")
            elif (
                change_menu_input == "2"
                or change_menu_input == "3"
                and change_occured not in ["yes", "no"]
            ):
                print("Invalid vision change.")
            else:
                # updates the instance variables and returns the current status
                current_status = sensor.update_status(change_menu_input, change_occured)

            # If lights are red or there is a pedestrian or vehicle
            if (
                current_status[0] == "red"
                or current_status[1] == "yes"
                or current_status[2] == "yes"
            ):
                print("\n" + "STOP" + "\n")  # Prints course of action message
                print(
                    "Light = "
                    + current_status[0]
                    + " , Pedestrian = "
                    + current_status[1]  # Prints the current status
                    + " , Vehicle = "
                    + current_status[2]
                    + " ."
                    + "\n"
                )
            # If light is yellow
            elif current_status[0] == "yellow":
                print("\n" + "Caution" + "\n")  # Prints action message
                print(
                    "Light = "
                    + current_status[0]
                    + " , Pedestrian = "  # Prints current status
                    + current_status[1]
                    + " , Vehicle = "
                    + current_status[2]
                    + " ."
                    + "\n"
                )
            # If light is green and no pedestrian and no vehicle
            elif (
                current_status[0] == "green"
                and current_status[1] == "no"
                and current_status[2] == "no"
            ):
                print("\n" + "Proceed" + "\n")  # Prints action message
                print(
                    "Light = "
                    + current_status[0]
                    + " , Pedestrian = "  # Prints current status
                    + current_status[1]
                    + " , Vehicle = "
                    + current_status[2]
                    + " ."
                    + "\n"
                )
        # Except block with if-elif for invalid menu selection and invalid change input
        except ValueError as value_error:
            if str(value_error) == "Invalid vision change.":
                print()
            elif str(value_error) == "You must select either 1, 2, 3, 0":
                print("You must select either 1, 2, 3, 0" + "\n")


# Complete the main function below
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")
    sensor1 = Sensor()  # Object of class Sensor initialized
    print_message(sensor1)  # object passed to print_message function


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == "__main__":
    main()
