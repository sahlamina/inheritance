# I began this code by creating a parent class of restaurant with a few basic attributes
class Restaurant:

# I used the init method to initialise the restaurant class with two parameters: name and cuisine
    def __init__(self, name, cuisine):
# Every other restaurant I create will INHERIT these attributes
        self.name = name
        self.cuisine = cuisine

    def open(self):
        print(self.name + " is now open")

    def close(self):
        print(self.name + " just closed!")

    def event(self):
        print(self.name + " is doing a promotional event!")

# Take_away is a child class of the parent class which is denoted in the parenthesis
# I named my takeaway Jerk Pit after one of my favourite Caribbean spots
class Take_away(Restaurant):
# I used pass to denote that nothing needs to happen in this class becasue all the attributes are contained within the parent class
    pass
# Here I demonstrated how Jerk Pit inherits the attributes from the restaurant class
jerk_pit = Take_away("Jerk pit", "Caribbean food")
print(jerk_pit.name)
jerk_pit.open()
print(jerk_pit.cuisine)
jerk_pit.close()







