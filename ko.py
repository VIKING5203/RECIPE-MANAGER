import csv

#(ChatGPT, 2025)
filename1 = r"C:\Users\mayank\Downloads\PROCESS.CSV" 
filename2 = r"C:\Users\mayank\Downloads\INGREDIENTS.CSV"
filename3 = r"C:\Users\mayank\Downloads\users.csv"
#(ChatGPT, 2025)

def loadRecipes():
    recipeList = []
    try:
        with open(filename1, newline='') as file1:
            reader1 = csv.DictReader(file1)
            for row in reader1:
                recipe = {
                    'id': row['id'],
                    'name': row['name'],
                    'cuisine': row['cuisine'],
                    'serves': row['serves'],
                    'process': row['process'],
                    'ingredients': [] #so ingredients can be added here 
                }
                recipeList.append(recipe)
    except:
        print("Could not read recipes from file")
    return recipeList

def loadIngredients(recipeList):
    try:
        with open(filename2, "r") as file2:
            reader2 = csv.DictReader(file2)
            for row in reader2:
                recipeId = row['recipeId']
                ingredient = {
                    'name': row['ingredient'],
                    'quantity': row['quantity'],
                    'unit': row['unit']
                }
                # Find the recipe and add ingredient
                for recipe in recipeList:
                    if recipe['id'] == recipeId:
                        recipe['ingredients'].append(ingredient)#GPT
                        break       
    except:
        print("File not found")

def loadUsers():
    users = []
    try:
        with open(filename3, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = {
                    'UserID': row['UserID'],
                    'Password': row['Password'],
                    'MealPlan': {
                        'Monday': row['Monday'],
                        'Tuesday': row['Tuesday'],
                        'Wednesday': row['Wednesday'],
                        'Thursday': row['Thursday'],
                        'Friday': row['Friday'],
                        'Saturday': row['Saturday'],
                        'Sunday': row['Sunday']
                    }
                }
                users.append(user)
    except Exception as e: #Initially had error problem here but now it has been solved
        print("Could not load user data.")
    return users

    
def saveRecipes(recipeList):
    try:
        with open(filename1, 'w', newline='') as file1:
            fieldnames = ['id', 'name', 'cuisine', 'serves', 'process']
            writer = csv.DictWriter(file1, fieldnames=fieldnames)
            writer.writeheader()
            for recipe in recipeList:
                writer.writerow({
                    'id': recipe['id'],
                    'name': recipe['name'],
                    'cuisine': recipe['cuisine'],
                    'serves': recipe['serves'],
                    'process': recipe['process']
                })
    except:
        print("Failed to save recipes.")

# Save ingredients to file
def saveIngredients(recipeList):
    try:
        with open(filename2, 'w', newline='') as file2:
            fieldnames = ['recipeId', 'ingredient', 'quantity', 'unit']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            writer.writeheader()
            for recipe in recipeList:
                for ing in recipe['ingredients']:
                    writer.writerow({
                        'recipeId': recipe['id'],
                        'ingredient': ing['name'],
                        'quantity': ing['quantity'],
                        'unit': ing['unit']
                    })
    except:
        print("Failed to save ingredients.")

def saveUsers(users):
    try:
        with open(filename3, 'w', newline='') as file:
            fieldnames = ['UserID', 'Password', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                row = {
                    'UserID': user['UserID'],
                    'Password': user['Password'],
                    'Monday': user['MealPlan']['Monday'],
                    'Tuesday': user['MealPlan']['Tuesday'],
                    'Wednesday': user['MealPlan']['Wednesday'],
                    'Thursday': user['MealPlan']['Thursday'],
                    'Friday': user['MealPlan']['Friday'],
                    'Saturday': user['MealPlan']['Saturday'],
                    'Sunday': user['MealPlan']['Sunday']
                }
                writer.writerow(row)
    except:
        print("Could not save user data.")
        
#(S.Cambers,2025)
def loginUser(users):
    print("\n=== LOGIN ===")
    username = input("UserID: ").strip()
    password = input("Password: ").strip()
    for user in users:
        if user['UserID'].strip() == username and user['Password'].strip() == password:
            print("Login successful.")
            return user
    print("Invalid credentials.")
    return None  # GeeksforGeeks. (n.d.). Python None Keyword.
#(S.Cambers,2025)

def registerUser(users):
    print("\n=== REGISTER NEW USER ===")
    while True:
        username = input("Choose a UserID: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue

        # Check if username already exists
        exists = False
        for user in users:
            if user['UserID'].strip().lower() == username.lower():
                exists = True
                break

        if exists:
            print("Username already exists. Try a different one.")
        else:
            break

    while True:
        password = input("Choose a Password: ").strip()
        if not password:
            print("Password cannot be empty.")
        else:
            break

    newUser = {
        'UserID': username,
        'Password': password,
        'MealPlan': {
            'Monday': '',
            'Tuesday': '',
            'Wednesday': '',
            'Thursday': '',
            'Friday': '',
            'Saturday': '',
            'Sunday': ''
        }
    }

    users.append(newUser)
    saveUsers(users)
    print("User registered successfully. You can now log in.")

def recipeSummary(recipeList):
    print("\n===CURRENT RECIPES===")
    for row in recipeList:
        print(row['id'] + ".", row['name'])
        print("Cuisine:", row['cuisine'])
        print("Serves:", row['serves'])
        print("-"*30)
        
def recipeDetails(recipe):
    print("\nName:", recipe['name'])
    print("Cuisine:", recipe['cuisine'])
    print("Serves:", recipe['serves'])
    print("Ingredients:")
    #(ChatGPT, 2025). Formatting help to improve recipe display
    for ing in recipe['ingredients']:
        print("-", ing['quantity'], ing['unit'], ing['name'])
    print("\nMethod:", recipe['process'])
    #(ChatGPT, 2025)

# Ask for valid recipe ID and return the matching recipe
def verifyRecipeInput(recipeList):
    if not recipeList:
        print("No recipes available.")
        return None
    while True:
        recipeId = input("Enter recipe ID: ").strip()
        for recipe in recipeList:
            if recipe['id'] == recipeId:
                return recipe
        print("Recipe ID not found. Try again.")

# Add a new recipe
def addRecipe(recipeList):
    print("\n=== ADD NEW RECIPE ===")
    name = input("Enter recipe name: ")
    cuisine = input("Enter cuisine: ")

    while True:
        serves = input("How many servings: ")
        if serves.isdigit() and int(serves) > 0: #W3Schools (no date) Python String isdigit() Method
            break
        else:
            print("Please enter a positive whole number.")

    process = input("Enter preparation steps: ")

    #(ChatGPT, 2025)
    # Assign new unique ID
    newId = str(max([int(r['id']) for r in recipeList] + [0]) + 1)
    #(ChatGPT, 2025)
    
    newRecipe = {
        'id': newId,
        'name': name,
        'cuisine': cuisine,
        'serves': serves,
        'process': process,
        'ingredients': []
    }

    while True:
        try:
            count = int(input("How many ingredients to add: "))
            if count <= 0:
                print("Please enter a positive number.")
            else:
                break
        except:
            print("Invalid input. Please enter a number.")

    for i in range(count):
        print(f"Ingredient {i + 1}:")

        ingName = input("  Name: ").strip()

        # Validate quantity input as a number
        while True:
            ingQty = input("  Quantity (e.g. 200, 1.5): ").strip()
            try:
                float(ingQty)
                break
            except:
                print("  Please enter a number like 200 or 1.5.")

        # Ask for unit and give examples
        while True:
            ingUnit = input("  Unit (e.g. grams, ml, pcs): ").strip()
            if ingUnit:
                break
            else:
                print("  Unit cannot be empty. Please try again.")

        newRecipe['ingredients'].append({
            'name': ingName,
            'quantity': ingQty,
            'unit': ingUnit
        })

    print("\n=== RECIPE PREVIEW ===")
    recipeDetails(newRecipe)

    while True:
        confirm = input("\nSave this recipe? (y/n): ").lower()
        if confirm == 'y':
            recipeList.append(newRecipe)
            saveRecipes(recipeList)
            saveIngredients(recipeList)
            print("Recipe added successfully.")
            break
        elif confirm == 'n':
            print("Recipe discarded.")
            break
        else:
            print("Please enter 'y' or 'n'.")

# Edit an existing recipe
def editRecipe(recipeList):
    recipeSummary(recipeList)
    print("\n==== EDIT RECIPE ====")
    recipe = verifyRecipeInput(recipeList)
    if recipe is None:
        return

    print(f"\nEditing '{recipe['name']}' (leave blank to keep current value.)")
    name = input(f"New name [{recipe['name']}]: ").strip()
    cuisine = input(f"New cuisine [{recipe['cuisine']}]: ").strip()

    # Validate servings input 
    while True:
        servesInput = input(f"New servings [{recipe['serves']}]: ").strip()
        if servesInput == "":
            serves = recipe['serves']
            break
        elif servesInput.isdigit() and int(servesInput) > 0:
            serves = servesInput
            break
        else:
            print("Please enter a positive whole number.")

    process = input(f"New process [{recipe['process']}]: ").strip()

    if name:
        recipe['name'] = name
    if cuisine:
        recipe['cuisine'] = cuisine
    recipe['serves'] = serves
    if process:
        recipe['process'] = process

    # Ask if the user wants to edit ingredients
    while True:
        change = input("Do you want to change ingredients? (y/n): ").lower()
        if change == 'y':
            while True:
                try:
                    count = int(input("How many ingredients to add: "))
                    if count <= 0:
                        print("Please enter a positive number.")
                    else:
                        break
                except:
                    print("Invalid input. Please enter a number.")
            
            recipe['ingredients'] = []
            for i in range(count):
                print(f"Ingredient {i+1}:")
                ingName = input("  Name: ")
                ingQty = input("  Quantity: ")
                ingUnit = input("  Unit: ")
                recipe['ingredients'].append({
                    'name': ingName,
                    'quantity': ingQty,
                    'unit': ingUnit
                })
            break
        elif change == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")

    saveRecipes(recipeList)
    saveIngredients(recipeList)
    print("Recipe updated successfully.")

# Delete a recipe
def deleteRecipe(recipeList):
    recipeSummary(recipeList)
    print("\n=== DELETE RECIPE ===")
    recipe = verifyRecipeInput(recipeList)
    while True:
        confirm = input(f"Are you sure you want to delete '{recipe['name']}'? (y/n): ").lower()
        if confirm == 'y':
            recipeList.remove(recipe) #Reference
            saveRecipes(recipeList)
            saveIngredients(recipeList)
            print("Recipe deleted.")
            break
        elif confirm == 'n':
            print("Deletion cancelled")
            break
        else:
            print("Please enter 'y' or 'n'.")

def planMeals(user, recipeList):
    print("\n=== PLAN MEALS ===")
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    recipeSummary(recipeList)
    for day in days:
        print(f"\n{day}'s meal:")
        recipe = verifyRecipeInput(recipeList)
        if recipe:
            user['MealPlan'][day] = recipe['id']
    print("Meal plan saved.")

def generateShoppingList(user, recipeList):
    print("\n=== Shopping List ===")
    shoppingList = {}

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in days:
        recipeId = user['MealPlan'][day]
        for recipe in recipeList:
            if recipe['id'] == recipeId:
                for item in recipe['ingredients']:
                    name = item['name'].strip().lower()
                    unit = item['unit'].strip().lower()

                    try:
                        quantity = float(item['quantity'])
                    except:
                        print(f"Warning: Invalid quantity for {name}. Skipped.")
                        continue

                    #sum similar items
                    #(CHAT GPT, 2025)
                    key = (name, unit)
                    if key in shoppingList:
                        shoppingList[key] += quantity
                    else:
                        shoppingList[key] = quantity
                    #(CHAT GPT, 2025)

    if not shoppingList:
        print("No ingredients found. Please plan your meals first.")
        return

    print("\nYour Shopping List:\n")
    for (name, unit), quantity in shoppingList.items():
        print(f"- {round(quantity, 2)} {unit} {name}")

def searchRecipes(recipeList):
    print("\n=== FIND A RECIPE ===")
    print("Search by:")
    print("  1. Name")
    print("  2. Ingredient")
    option = input("Choose 1 or 2: ").strip()

    if option == '1':
        searchTerm = input("Enter a word from the recipe name: ").strip().lower()
        results = []
        for recipe in recipeList:
            if searchTerm in recipe['name'].lower():
                results.append(recipe)

        if results:
            print(f"\nFound {len(results)} recipe(s) with '{searchTerm}':")
            for check in results:
                recipeDetails(check)
        else:
            print("Sorry, no recipes match that name.")

    elif option == '2':
        searchIng = input("Enter an ingredient to look for: ").strip().lower()
        matched = []
        for recipe in recipeList:
            for item in recipe['ingredients']:
                if searchIng in item['name'].lower():
                    matched.append(recipe)
                    break

        if matched:
            print(f"\nRecipes containing '{searchIng}':")
            for i in matched:
                recipeDetails(i)
        else:
            print("No recipes found with that ingredient.")
    else:
        print("That wasn't a valid choice. Please try again")
        searchRecipes(recipeList)
        
# Display menu
def menu():
    print("\n=== RECIPE MANAGER MENU ===")
    print("1. View all recipe summaries")
    print("2. View full recipe details")
    print("3. Add a new recipe")
    print("4. Edit an existing recipe")
    print("5. Delete a recipe")
    print("6. Plan meals for the week")
    print("7. Generate shopping list for meal plan")
    print("8. Search recipes")
    print("9. Save and Exit")
    return input("Enter your choice (1–9): ")

# Main program
def main():
    recipeList = loadRecipes()
    loadIngredients(recipeList)
    users = loadUsers()
    user = None
    print("\n=== Welcome to the Weekly Recipe Planner ===")

    while user is None:
        print("\nWhat would you like to do?")
        print("1. Sign in")
        print("2. Create a new account")
        print("3. Exit the program")
        option = input("Select an option (1-3): ").strip()

        if option == '1':
            user = loginUser(users)
            if user is None:
                print("Incorrect login. Please try again.")
        elif option == '2':
            registerUser(users)
        elif option == '3':
            print("Exiting the program. Have a great day!")
            return
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

    select(user, users, recipeList)

            
def select(user, users, recipeList):
    while True:
        choice = menu()
        if choice == '1':
            recipeSummary(recipeList)
        elif choice == '2':
            recipeSummary(recipeList)
            print("\n=== VIEW FULL RECIPE DETAILS ===")
            recipe = verifyRecipeInput(recipeList)
            if recipe:
                recipeDetails(recipe)
        elif choice == '3':
            addRecipe(recipeList)
        elif choice == '4':
            editRecipe(recipeList)
        elif choice == '5':
            deleteRecipe(recipeList)
        elif choice == '6':
            planMeals(user, recipeList)
            saveUsers(users)
        elif choice == '7':
            generateShoppingList(user, recipeList)
        elif choice == '8':
            searchRecipes(recipeList)
        elif choice == '9':
            saveUsers(users)
            print("Goodbye!")
            return
        else:
            print("Invalid option. Please enter a number between 1 and 9.")

# Run the program
main()

