import matplotlib.pyplot as plt # importing the pyplot module from the matplotlib library and assigning it to plt


def weight_loss_kg(targeted_weight, current_weight, deficit): # defining a function for weight loss in kg with parameters of targeted weight, current weight, and deficit amount
    calories_per_kg = 7700 # this is the total amount of calories in one kilogram (one pound of calories is 3500. one kg is 2.20462lbs. 2.20462 x 3500 = 7700 rounded to the nearest hundred)
    kg_to_lose = current_weight - targeted_weight # to find the amount of kilograms to lose, subtract targeted weight from current weight
    calories_to_lose = calories_per_kg * kg_to_lose # to find total calories to lose, multiply calories per kg (7700) by amount of kg to lose
    days_goal = round(calories_to_lose / deficit) # to find the amount of days it will take to reach goal, we are dividing calories to lose by the deficit amount. Using round so that we have days as integer and not float
    return days_goal # returning the amount of days to reach goal


def weight_gain_kg(targeted_weight, current_weight, surplus): # defining a function for weight gain in kg with parameters of targeted weight, current weight, and surplus amount
    calories_per_kg = 7700
    kg_to_gain = targeted_weight - current_weight # here we are doing the opposite for weight gain. To find the weight gain in kilograms, we are subtracting the current weight from targeted weight
    calories_to_gain = calories_per_kg * kg_to_gain
    days_goal = round(calories_to_gain / surplus) # to find the amount of days it will take to reach goal, we are dividing calories to gain by the surplus amount
    return days_goal


def weight_loss_lbs(targeted_weight, current_weight, deficit): # defining a function for weight loss in pounds (lbs) with parameters of targeted weight, current weight, and deficit amount
    calories_per_pound = 3500 # calories in one pound
    pounds_to_lose = current_weight - targeted_weight
    calories_to_lose = calories_per_pound * pounds_to_lose
    days_goal = round(calories_to_lose / deficit)
    return days_goal


def weight_gain_lbs(targeted_weight, current_weight, surplus): # defining a function for weight gain in pounds (lbs) with parameters of targeted weight, current weight, and surplus amount
    calories_per_pound = 3500
    pounds_to_gain = targeted_weight - current_weight
    calories_to_gain = calories_per_pound * pounds_to_gain
    days_goal = round(calories_to_gain / surplus)
    return days_goal


def plot_weight_progress(weeks, weekly_weight, weight_type, plan_num): # defining a function that will plot the weekly weight progression by using the matplotlib library. This function takes amount of weeks, the weekly updated weight, weight type (kg or lbs), and plan number as parameters
    plt.plot(weeks, weekly_weight, 'o-') # using plot() function to create a graph with x-axis(weeks), y-axis(weekly_weight) and o- is to create a line graph with circled points to identify each plot
    plt.grid() # using the grid() function to ensure that the graph contains a grid
    plt.xlabel('Weeks') # using the xlabel() function to name the x-axis as Weeks
    with open('weight_progress.txt', 'a') as file: # using with open to create a txt file called 'weight....' and assigning it to file (if text file does not exist, with open will create the file). Using append so that each of the following iterations (plan # 1, plan # 2, and plan # 3) are added to the list. We did not use write mode because that will overwrite the previous iterations (plan #1 and plan #2)
        title_border = '==================================================' # this string will be used as a border for the title in the file, it will help with readability
        file.write(f'\n{title_border}\nPlan #{plan_num}\n{title_border}\n') # This is written to the file as a title for plans surrounded by borders
        for i in range(len(weeks)): # using a for loop to iterate through the range of the length of weeks (weeks is a list). Working with indices.
            if weeks[i] == 0: # when at the first element of the weeks list (week 0) then we are inserting an empty line before week 0 to separate each plan (plan #1, plan #2, and plan #3). This will help with readability
                file.write('\n')
            file.write(f'Week {weeks[i]} ---> {weekly_weight[i]}\n') # using formatted string to write a line to the file showcasing the current week along with the user's weight of that week, per iteration of the for loop. A new line is created per iteration to write the formatted string in a new line (helps with readability)

    if weight_type == "lbs": # using an if statement in a case where the user chose lbs as the weight_type
        plt.ylabel('Pounds') # in that case, the y-axis is named Pounds (used ylabel() function)
        plt.title(f'Plan #{plan_num}: Weekly Progression of Weight in Pounds\n') # within the if statement of lbs, we are using a title() function to name the title of the graph. A newline character is utilized for better readability
        plt.show() # using the show() function to display the graph
    elif weight_type == 'kg': # else in a case where the user chose kg as the weight_type
        plt.ylabel('Kilograms') # in that case, the y-axis is named Kilograms with the ylabel() function
        plt.title(f'Plan #{plan_num}: Weekly Progression of Weight in Kilograms\n') # also in that case, the title is named accordingly ('Weekly Progression of Weight in Kilograms'). A newline character is utilized for better readability
        plt.show() # using the show() function to display the graph


def macro_bar_graph(protein_ratio, carbs_ratio, fats_ratio, plan_num): # defining a function that will create a bar graph showcasing the amount of protein, carbs, and fats needed for the user to reach their goal (according to each plan)
    ratio = [] # initializing the ratio list which will be used below
    if weight_goal == 'L' or weight_goal == 'G': # if statement checks whether the weight_goal input is 'L' or 'G'. If so, the ratio variable (list which was initialized) holds the values of protein, carbs, and fats in a list
        ratio = [protein_ratio, carbs_ratio, fats_ratio]

    plt.bar(['Protein', 'Carbohydrates', 'Fats'], ratio, color=['r', 'b', 'g']) # using the bar() function to create a bar graph for each macronutrient in the x-axis. The height of each bar will match the ratio amount corresponding to the y-axis. Arguments of colors are being passed (r represents red, b represents blue, and g represents green)
    plt.title(f'Plan #{plan_num}: Macronutrient Ratio\n') # using the title() function to name the title of the bar graph. A new line is created for better readability
    plt.xlabel('Macronutrient Name') # using the xlabel() function to name the x-axis to Macronutrient Name
    plt.ylabel('Amount of Calories') # using the ylabel() function to name the y-axis to Amount of Calories
    plt.show() # using the show() function to display the bar graph



if __name__ == "__main__": # The following blocks of code is a part of this conditional line that checks if the script is being run as the main program. If it isn't imported as a module and is run directly, only then will the if statement be executed.
    welcome_border = '============================================================'
    print(f'''{welcome_border}\nWelcome to the CalPal calorie calculator!
This calculator will help you achieve your weight goal!
What are you waiting for? Let's begin this journey!\n{welcome_border}''') # Welcome message. Created a multiline string along with borders for better readability

    # Initializing the following variables to False, as they will be used in the while loops below for looking after user input errors
    correct_entry_begin = False
    correct_entry_weight = False
    correct_entry_goal = False
    correct_weight_type = False
    correct_calorie_input = False
    correct_targeted_weight = False
    correct_weight_inputs = False

    # Initializing the following variables as default values as they will be used within the while loops below
    weight_goal = ""
    user_calories = ""
    targeted_weight = ""
    current_weight = ""
    weight_type = ""

    # while loop used for a case where the user does not enter 'start' correctly
    while correct_entry_begin is False:
        begin = input("Enter 'start' to begin: ").lower() # used lower() method to convert user input to lowercase
        if begin == "start":
            correct_entry_begin = True # boolean value of this variable changes to True if user enters 'start' correctly, breaks out of loop
        else:
            print("Whoops! It looks like you did not enter 'start'. Please try again!")

    # user is given the option to enter either of the two metrics. While loop is used in case the user enters their choice incorrectly
    while correct_weight_type is False:
        weight_type = input("Enter 'kg' for kilograms or 'lbs' for pounds: ").lower()
        if weight_type != 'kg' and weight_type != 'lbs':
            print('Oops! Looks like you entered an invalid option. Please try again!')
        else:
            correct_weight_type = True

    # user is given the option to enter whether they want to (l)ose or (g)ain weight. While loop is used in case the user enters something other than 'l' or 'g'
    while correct_entry_goal is False:
        weight_goal = input("Enter 'L' to lose weight or enter 'G' to gain weight: ").upper()
        if weight_goal != 'L' and weight_goal != 'G':
            print("Oh no! It looks like you did not enter a valid choice. Please try again!")
        else:
            correct_entry_goal = True

    #  while loop with a try & except block within it, used for checking logical errors that the user may have made, as well as whether numeric values were inputted. Explained below
    while correct_weight_inputs is False:
        try:
            current_weight = float(input("Enter your current weight: "))
            targeted_weight = float(input("Enter your target weight: "))
            if current_weight <= 0 or targeted_weight <= 0: # if user enters a negative number or 0 for current_weight or targeted_weight, ask them to try again until a valid value is inputted
                print('Error! Weight inputs must be greater than 0. Please try again!')
            elif weight_goal == 'L' and targeted_weight >= current_weight: # if user is trying to lose weight but enters a targeted weight that is greater than their current weight then ask them to re-enter values until targeted weight is less than current weight
                print("Error! Your target weight must be less than your current weight for weight loss. Please try again!")
            elif weight_goal == 'G' and targeted_weight <= current_weight: # if user is trying to gain weight but enters a targeted weight that is less than their current weight then ask user to re-enter values until the targeted weight is greater than current weight
                print("Error! Your target weight must be greater than your current weight for weight gain. Please try again!")
            else:
                correct_weight_inputs = True # else if there are no logical errors in the user's inputs then set the correct_weight_inputs variable to True and break out of loop
        except ValueError: # except when a user does not enter a numeric value then raise a ValueError and ask user to input values again
            print("Oops! It looks like you did not enter numeric values. Please try again.")

    # while loop with try & except block. Used for if the user enters a calorie consumption amount less than or equal to 0. A ValueError is raised when the user does not enter a numeric value.
    while correct_calorie_input is False:
        try:
            user_calories = int(input('How many calories do you consume in a day: '))
            if user_calories <= 0:
                print('Error! You must enter a calorie intake over 0. Please try again!')
            else:
                correct_calorie_input = True
        except ValueError:
            print("Uh oh! It looks like you did not enter a numeric value. Please try again")

    if weight_goal == "L": # if the user inputted 'L' (lose weight) for weight_goal
        deficit_list = [200, 350, 500] # the values in the list represent the 3 plans (200-caloric deficit, 350-caloric deficit, 500-caloric deficit)
        print("\nCustomized Weight Loss Plans")
        if weight_type == 'lbs': # if user enters 'lbs' for weight_type. In other words, if user is trying to lose weight and wants to use pounds as the mass unit
            plan_num = 1 # initializing plan number to 1 as this will be incremented by one per iteration of the for loop below
            for deficit in deficit_list: # iterating through the deficit_list
                days_for_goal = weight_loss_lbs(targeted_weight, current_weight, deficit) # the returned value of the weight_lost_lbs function is stored in days_for_goal variable
                weeks_for_goal = days_for_goal / 7 # dividing the value of days it will take to reach goal by 7 to determine the amount weeks it will take
                days_message = f'Plan #{deficit_list.index(deficit) + 1}: With a daily caloric deficit of {deficit} calories, it will take you {days_for_goal} days to reach {int(targeted_weight)}lbs'
                # plan number in the formatted string above does the following: 0 + 1 = 1, 1 + 1 = 2, 2 + 1 = 3. This represents the plan number, and it uses the index of the deficit_list. deficit, days_for_goal and targeted weight change per iteration and shown accordingly
                calorie_intake = user_calories - deficit # amount of calories needed is found by subtracting deficit from the user_calories. This is used below to calculate how many calories should come from protein, carbs, and fats. General rule is 40%/30%/30% while losing weight
                protein_ratio = calorie_intake * 0.40
                carbs_ratio = calorie_intake * 0.30
                fats_ratio = calorie_intake * 0.30
                print(days_message)
                # converting protein_ratio, carbs_ratio, and fats_ratio to integer values and printing messages accordingly
                print(f"""40% of your calorie intake should come from protein ---> {int(protein_ratio)} calories of protein
30% of your calorie intake should come from carbohydrates ---> {int(carbs_ratio)} calories of carbohydrates
30% of your calorie intake should come from fats ---> {int(fats_ratio)} calories of fat
""")
                total_weeks = int(weeks_for_goal) # converting weeks_for_goals to an integer value and storing it in total_weeks as it will be used in the for loop below
                weeks = [] # initializing a list for weeks as we will iterate through this when calling the graph functions
                for week in range(total_weeks + 1): # for loop for the total amount of weeks (total_weeks + 1 since we want to use the last week as well)
                    weeks.append(week) # appending each week to the weeks list
                weekly_weight = [] # initializing a list for weekly_weight as this will hold each weight progression value per week
                for week in weeks: # using a for loop to iterate through the weeks list
                    amt_lost = (deficit * week) / 500 # finding the amount of weight lost corresponding to the iterated week of the for loop
                    weekly_weight.append(current_weight - amt_lost) # the updated weight for iterated week is appended to the weekly_weight list (found by subtracting amount lost from current weight)
                plot_weight_progress(weeks, weekly_weight, 'lbs', plan_num) # calling the plot graph function with arguments of weeks list, weekly_weight list, weight_type as 'lbs', and the plan_num
                macro_bar_graph(protein_ratio, carbs_ratio, fats_ratio, plan_num) # calling the bar graph with arguments of protein_ratio, carbs_ratio, and fats_ratio, and plan_num
                plan_num += 1 # incrementing the plan number by 1 (as we want plan #1, plan #2, and plan #3)
        elif weight_type == 'kg': # if user enters 'kg' for weight_type. In other words, if user is trying to lose weight and wants to use kilograms
            plan_num = 1
            for deficit in deficit_list:
                days_for_goal = weight_loss_kg(targeted_weight, current_weight, deficit) # the returned value of the weight_lost_kg function is stored in days_for_goal variable
                weeks_for_goal = days_for_goal / 7
                days_message = f'Plan #{deficit_list.index(deficit) + 1}: With a daily caloric deficit of {deficit} calories, it will take you {days_for_goal} days to reach {int(targeted_weight)}kgs'
                calorie_intake = user_calories - deficit
                protein_ratio = calorie_intake * 0.40
                carbs_ratio = calorie_intake * 0.30
                fats_ratio = calorie_intake * 0.30
                print(days_message)
                print(f"""40% of your calorie intake should come from protein ---> {int(protein_ratio)} calories of protein
30% of your calorie intake should come from carbohydrates ---> {int(carbs_ratio)} calories of carbohydrates
30% of your calorie intake should come from fats ---> {int(fats_ratio)} calories of fat
""")
                total_weeks = int(weeks_for_goal)
                weeks = []
                for week in range(total_weeks + 1):
                    weeks.append(week)
                weekly_weight = []
                for week in weeks:
                    amt_lost = (deficit * week) / 500
                    weekly_weight.append(current_weight - amt_lost)
                plot_weight_progress(weeks, weekly_weight, 'kg', plan_num)
                macro_bar_graph(protein_ratio, carbs_ratio, fats_ratio, plan_num)
                plan_num += 1
    elif weight_goal == "G": # if the user inputted 'G' (gain weight) for weight_goal
        surplus_list = [200, 350, 500] # the values in the list represent the 3 plans (200-caloric surplus, 350-caloric surplus, 500-caloric surplus)
        print("\nCustomized Weight Gain Plans")
        if weight_type == 'lbs': # if user enters 'lbs' for weight_type. In other words, if user is trying to gain weight and wants to use pounds as the mass unit
            plan_num = 1
            for surplus in surplus_list: # iterating through the surplus_list
                days_for_goal = weight_gain_lbs(targeted_weight, current_weight, surplus) # the returned value of the weight_gain_lbs function is stored in days_for_goal variable
                weeks_for_goal = days_for_goal / 7
                days_message = f'Plan #{surplus_list.index(surplus) + 1}: With a daily caloric surplus of {surplus} calories, it will take you {days_for_goal} days to reach {int(targeted_weight)}lbs'
                # plan number in the formatted string above does the following: 0 + 1 = 1, 1 + 1 = 2, 2 + 1 = 3. This represents the plan number, and it uses the index of the surplus_list. surplus, days_for_goal and targeted weight values change per iteration and shown accordingly
                calorie_intake = user_calories + surplus # amount of calories needed in this case is found by adding surplus to the user_calories. This is used below to calculate how many calories should come from protein, carbs, and fats. General rule is 30%/40%/30% while gaining weight
                protein_ratio = calorie_intake * 0.30
                carbs_ratio = calorie_intake * 0.40
                fats_ratio = calorie_intake * 0.30
                print(days_message)
                print(f"""40% of your calorie intake should come from protein ---> {int(protein_ratio)} calories of protein
30% of your calorie intake should come from carbohydrates ---> {int(carbs_ratio)} calories of carbohydrates
30% of your calorie intake should come from fats ---> {int(fats_ratio)} calories of fat
""")
                total_weeks = int(weeks_for_goal)
                weeks = []
                for week in range(total_weeks + 1):
                    weeks.append(week)
                weekly_weight = []
                for week in weeks:
                    amt_gained = (surplus * week) / 500 # finding the amount of weight gained corresponding to the iterated week of the for loop
                    weekly_weight.append(current_weight + amt_gained) # the updated weight for iterated week is appended to the weekly_weight list (found by adding current weight to amount gained
                plot_weight_progress(weeks, weekly_weight, 'lbs', plan_num)
                macro_bar_graph(protein_ratio, carbs_ratio, fats_ratio, plan_num)
                plan_num += 1
        elif weight_type == 'kg': # if user enters 'kg' for weight_type. In other words, if user is trying to gain weight and wants to use kilograms as the mass unit
            plan_num = 1
            for surplus in surplus_list:
                days_for_goal = weight_gain_kg(targeted_weight, current_weight, surplus) # the returned value of the weight_gain_kg function is stored in days_for_goal variable
                weeks_for_goal = days_for_goal / 7
                days_message = f'Plan #{surplus_list.index(surplus) + 1}: With a daily caloric surplus of {surplus} calories, it will take you {days_for_goal} days to reach {int(targeted_weight)}kgs'
                calorie_intake = user_calories + surplus
                protein_ratio = calorie_intake * 0.30
                carbs_ratio = calorie_intake * 0.40
                fats_ratio = calorie_intake * 0.30
                print(days_message)
                print(f"""40% of your calorie intake should be from protein ---> {int(protein_ratio)} calories of protein
30% of your calorie intake should be from carbohydrates ---> {int(carbs_ratio)} calories of carbohydrates
30% of your calorie intake should be from fats ---> {int(fats_ratio)} calories of fat
""")
                total_weeks = int(weeks_for_goal)
                weeks = []
                for week in range(total_weeks + 1):
                    weeks.append(week)
                weekly_weight = []
                for week in weeks:
                    amt_gained = (surplus * week) / 500
                    weekly_weight.append(current_weight + amt_gained)
                plot_weight_progress(weeks, weekly_weight, 'kg', plan_num)
                macro_bar_graph(protein_ratio, carbs_ratio, fats_ratio, plan_num)
                plan_num += 1
print("""Choose a plan above and get ready to see some amazing results! Best of luck on your journey to a healthier you!
© 2023 CalPal. All Rights Reserved.""") # closing message
