# ASSUMPTIONS::
# Anyone can buy or search for cars
#
#



#=======================================================================================
#                       CLASSES & Variables
#=======================================================================================
#to store the details of each variable
class Vehicle:
    def __init__(self, model,city,year, seller,price, details, company ):
        self.seller = seller
        self.company = company
        self.city = city
        self.year = year
        self.model = model
        self.price = price
        self.details = details
        self.comments = []
        self.status = 'available'

    def printVehicle(self):
        print(self.company + " | " + self.model + " | " + self.year + " \nprice: " + str(self.price) + "\n" + self.details + "\n" + self.city + "\n" + self.seller)
        print("COMMENTS:")
        if self.comments:
            for each in self.comments:
                print(each)
        else:
            print("THERE ARE NO COMMENTS FOR THIS VEHICLE YET")

    def addComments(self,name, comments):
        temp = []
        temp.append(name)
        temp.append(comments)
        self.comments.append(temp)
    
    def searchVehicle(self, srch):
        if srch == "-":
            return 0
        if srch in self.seller or srch in self.company or srch in self.city or srch in self.model or srch in self.year or srch == str(self.price):
            return 1
        else:
            return 0

class Seller:
    def __init__(self,name):
        self.name = name
        self.itemsListed = []

    def addVehicle(self, vehicle):
        self.itemsListed.append(vehicle)

    def printSeller(self):
        print(self.name)
        print(self.itemsListed)

#a list of all the vehicles
ListofVehicles = []
ListofSellers = []

#=======================================================================================
#                                   FUNCTIONS
#=======================================================================================

def addVehicle():
    print("FILL IN THE FOLLOWING TO ADD A VEHICLE FOR SELLING:")
    seller = input("Seller Name: ")
    company = input("Vehicle Manufacturing Company: ")
    model = input("Model of the Vehicle: ")
    year = input("Year of model: ")
    price = input("Selling price of the vehicle (Rs): ")
    city = input("City: ")
    details = input("Details: ")
    tempVehicle = Vehicle(model,city,year,seller,price,details,company)
    tempSeller = Seller(seller)
    ListofVehicles.append(tempVehicle)
    ind = ListofVehicles.index(tempVehicle)
    if seller not in ListofSellers:
        tempSeller.addVehicle(ind)
        ListofSellers.append(tempSeller)
    else:
        ListofSellers.index(tempSeller)
        tempSeller.addVehicle(ind)

def internal_search_vehicles(model = "-",city = "-",year = "-", seller = "-",price = 9999999, company = "-"):
    if model == "-" and city == "-" and year == "-" and seller == "-" and str(price) == str(9999999) and company == "-":
        for each in ListofVehicles:
            each.printVehicle()
    else:
        for each in ListofVehicles:
            if each.searchVehicle(model) or each.searchVehicle(city) or each.searchVehicle(year) or each.searchVehicle(seller) or each.searchVehicle(str(price)) or each.searchVehicle(company):
                each.printVehicle()

def search_vehicles():
    print("Please write the filters you wish to search using, if you dont want to filter using that category write - in the input field")
    model = input("MODEL: ")
    city = input("CITY: ")
    year = input("YEAR: ")
    seller = input("SELLER: ")
    price = input("PRICE: ")
    company = input("COMPANY: ")
    internal_search_vehicles(model,city,year,seller,price,company)

def add_comments():
    print("FILL THE FOLLOWING TO ADD COMMENTS: ")
    name = input("YOUR NAME: ")
    seller = input("SELLER: ")
    model = input("MODEL: ")
    year = input("YEAR: ")
    company = input("COMPANY: ")
    if name == seller:
        print("ERROR :: Seller can not leave comments for their own vehicles")
        return 
    for each in ListofVehicles:
        if each.model == model and each.company == company and each.year == year and each.seller == seller:
            each.addComments(name)
    
def vehicle_details():
    print("PLEASE ENTER THE FOLLOWING TO GET THE DETAILS OF THE VEHICLE")
    model = input("MODEL: ")
    year = input("YEAR: ")
    company = input("COMPANY: ")
    for each in ListofVehicles:
        if each.model == model and each.company == company and each.year == year:
            each.printVehicle()
            
def buy_car():
    print("FILL THE FOLLOWING TO MARK THE CAR AS BOUGHT: ")
    seller = input("SELLER: ")
    model = input("MODEL: ")
    year = input("YEAR: ")
    company = input("COMPANY: ")
    for each in ListofVehicles:
        if each.model == model and each.company == company and each.year == year and each.seller == seller:
            each.status = 'sold'

#=======================================================================================
#                           RUNNING THE CODE TO SEE OUTPUT
#=======================================================================================
addVehicle()
addVehicle()
addVehicle()

print("\n\n LIST OF VEHICLES \n\n")
for each in ListofVehicles:
    each.printVehicle()

print("\n\n VEHICLES HAVE BEEN ADDED LETS TEST SOME SCENARIOS\n\n")

add_comments()
print("----------------SEARCH FOR A SPECIFIC VEHICLE'S DETAILS-------------------")
search_vehicles()
print("----------------BUY A VEHICLE-------------------")
buy_car()



