import json

class Database:

    def insert(self, username,email,password):
        # Open the JSON file in read mode 
        with open ('projects/user.json', 'r') as file:
            # Load the existing data from the JSON file
            data = json.load(file)
            # lets first check if the user already exists 
            if email in data:
                return 0
            else:
                # Add the new user data to the existing data
                data[email] = {
                    'username': username,
                    'password': password
                }
                # Open the JSON file in write mode to save the updated data
                with open('projects/user.json', 'w') as file:
                    # Write the updated data back to the JSON file
                    json.dump(data, file, indent=4)
                    return 1
        
    def search(self, email, password):

        with open ('projects/user.json' , 'r') as file:
            data = json.load(file)
            if email not in data :
                return 0
            else:
                if data[email]['password'] == password:
                    return 1
                else: 
                    return 0