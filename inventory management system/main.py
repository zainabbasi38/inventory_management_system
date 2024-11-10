class Product():
    def __init__(self,product_id,product_name,price,category,stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price 
        self.category = category
        self.stock_quantity = stock_quantity

    def details(self):
        return f"Product details: Product_id: {self.product_id} ,Product name: {self.product_name}, Price: {self.price}$,Category: {self.category} , Stock quantity: {self.stock_quantity}"

# product details:
class InventoryManagementSystem():
    def __init__(self):
        self.products = {}
        
    # Admin can add product
    def add_product(self):
        while True:
            print("When you enter zero it means that you want don't add any product")
            product_id = int(input("Enter product id: "))
            if product_id == 0:
                break
            else:
                product_name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                category = input("Enter category: ")
                stock_quantity = int(input("Enter stock quantity: "))  
                

                product = Product(product_id, product_name, price,category , stock_quantity)
                self.products[product_id] = product
                print(f"Product '{product_name}' added successfully")
        
    # Admin and User both can view product details:
    def view_product(self):
            for product_name in self.products:
                print(self.products[product_name].details())

        
    # Admin can edit/update product:
    def edit_product(self):
        product_id = int(input("Enter product id: "))
        if product_id in self.products:
            name = input("Enter product new name.")
            stock = int(input("Enter new stock quantity."))
            price = int(input(f"Enter new price of {name}."))
            category = input("Enter category of your new product")

            self.products[product_id].price = price
            self.products[product_id].product_name = name
            self.products[product_id].stock_quantity = stock
            self.products[product_id].category = category

            print(f"Your product has new name is '{name}'")
            print(f"Stock for product {self.products[product_id].product_name} updater to '{stock}'.")
            print(f"Your {name} has new price is {price}")
            print(f"Your product has new category is {category}")

        else:
            print("Product not found.")

    # Admin delete product:
    def delete_product(self):
        product_id = int(input("Enter product id: "))
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product '{product_id}' deleted successfully")

        else:
            print("Product not found.")

# Login system:
class User():
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role 

class Authentication():
    def __init__(self):
        self.users = {
            "admin" : User("admin","admin123", "admin"),
            "user1" : User("user1","user123", "user")
        }
        
    def login(self):
        print("Welcome to Inventory Management System.")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.users and self.users[username].password == password:
            print(f"Welcome {username}")
            return self.users[username]
            
        else:
            print("invalid credentials! Please try again ")
            return None
        
def main_menu():
    auth = Authentication()
    ims = InventoryManagementSystem()

    user = auth.login()
    if not user:
        print("")

    if user.role == "admin":
        # admin has full access
        while True:           
            print("\nInventory Management System. ")
            print("1. Add products")
            print("2. View products")
            print("3. Edit products")
            print("4. Delete products")
            print("5. Exit")

            try:
                choice = int(input("Enter a choice: "))
                if choice == 1 :
                    ims.add_product()
                elif choice == 2 :
                    ims.view_product()
                elif choice == 3 :
                    ims.edit_product()
                elif choice == 4 :
                    ims.delete_product()
                elif choice == 5 :
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice.Please try again")

            except ValueError as e:
                print(f"ERROR OCCURRED: {e}")

    else:
        # user access
        while True:
            print("\nInventory Management System. ")
            print("1. View products")
            print("2. Exit")
            try:
                choice = int(input("Enter a choice: "))

                if choice == 1:
                    print(ims.view_product())
                elif choice == 2:
                    print("Exiting...")
                    break
                else:
                    print("Wrong credentials,Please try again")

            except ValueError as e:
                print(f"ERROR OCCURRED: {e}")

if __name__ == "__main__":
    main_menu()