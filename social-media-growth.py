# Sherif Mansour
# CPS 3320 Python Programming
# Project 3
# Social Media Growth Calculator

# Library Import
from colored import stylize, fg

# Output Styling
print(stylize("\n|Sherif Mansour| Social Media Growth Calculator |Kean University|\n", fg("yellow")))

# Classes and Methods
class GrowthRate:
    def __init__(self, amount, new_amount):
        self.amount = amount
        self.new_amount = new_amount

    # Output Method
    def __repr__(self):
        rate = stylize(self.calculate_rate(self.amount, self.new_amount), fg("yellow"))
        period = input("Growth Period in # of Weeks: ")
        return f"\nGrowth Rate of {period} Week/s: {rate}%\n"

    # Calculation Method
    def calculate_rate(self, amount, new_amount):
        difference = new_amount - amount

        return round(100 / amount * difference, 2)

# Main Output
if __name__ == "__main__":

    # User Input
    follower_count = int(input("Previous Follower Count: "))
    new_follower_count = int(input("New Follower Count: "))

    # Final Output
    print(GrowthRate(follower_count, new_follower_count))
