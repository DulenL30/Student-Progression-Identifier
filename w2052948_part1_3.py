# I declare that my work contains no example of misconduct, such as plagiarism or collusion
# Any code taken from other sources is referenced within my code solution
# Student ID: w2052948
# Date : 13.12.2023 

# Import classes from graphics library.
from graphics import GraphWin, Point, Rectangle, Text, GraphicsError



# These are list of valid input credits.
input_credits = [0,20,40,60,80,100,120]



# This function created for get user inputs from the user.
def get_user_inputs():
    while True:
        user= input("To enter another set of data enter 'y' for quit and view results enter 'q': ").lower()
        if user =='q':
            break
        try:
            # Get inputs for pass,deffer and fail credits.
            pass_credit = int(input("Enter your credit at pass: "))
            defer_credit= int(input("Enter your defer credit at defer: "))
            fail_credit= int(input("Enter your fail credit at fail: "))

            # Check if the credits in valid credits or not.
            if pass_credit not in input_credits or defer_credit not in input_credits or fail_credit not in input_credits:
                print("Out of Range.")
                continue

            # Check total credits equal to 120 or not.
            total_credits = pass_credit + defer_credit + fail_credit
            
            if total_credits != 120:
                print("Total Incorrect.")
                continue


            # Determine and print the got results.
            if pass_credit == 120:
                print("Progress")
            elif pass_credit == 100:
                print("Progress (module trailer)")
            elif fail_credit >= 80:
                print("Exclude")
            else:
                print("Do not progress - module retriever")

            result = calculate_all_results(pass_credit,fail_credit)
            save_inputed_data(f"Pass: {pass_credit}, Defer: {defer_credit}, Fail: {fail_credit}, Result: {result}")

        #If user input not an integer display "Integer Required".
        except ValueError:
            print("Integer Required.")




# Create a function to calculate results.
def calculate_all_results(pass_credit,fail_credit):
    if pass_credit == 120:
        return "Progress"
    elif pass_credit == 100:
        return "Trailer"
    elif fail_credit >= 80:
        return "Exclude"
    else:
        return "Retriever"




# Create a text file for inputted data.
def save_inputed_data(data):
    with open("Inputted_progression_data.txt","a") as file:
        file.write(data+ "\n")

# Print all valid results inside this created file.
def display_inputed_data():
    try:
        with open("Inputted_progression_data.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No data available.")


# Use histogram for displaying results.
def display_histogram(data):
    categories = ["Progress","Trailer","Retriever","Exclude"]
    category_colors = {"Progress":"green", "Trailer":"yellow", "Retriever":"orange", "Exclude":"red"}
    category_counts = {category: 0 for category in categories}

    for data_entry in data:
        result = data_entry.split(":")[-1].strip()
        category_counts[result] += 1

    win = GraphWin("Histogram", 500,450)
    win.setBackground("white")

    total_students = len(data)

    topic = Text(Point(120,30), "Histogram Results")
    topic.setSize(20)
    topic.setStyle("bold")
    topic.draw(win)

    horizontal_axis = 50
    bar_width = 80


    # Draw bars for each category in the histogram.
    for category, count in category_counts.items():
        bar_height = count / total_students * 200
        rect = Rectangle(Point(horizontal_axis ,350), Point(horizontal_axis +bar_width, 350 -bar_height))
        rect.setFill(category_colors.get(category,"white"))
        rect.draw(win)

        tag = Text(Point(horizontal_axis + bar_width / 2,370), f"{category}\n{count} students.")
        tag.draw(win)

        horizontal_axis += bar_width + 20


    # Display the total number of outcomes.
    total_tag = Text(Point(120,400), f"{total_students} Outcomes in total.")
    total_tag.setStyle("bold")
    total_tag.setSize(14)
    total_tag.draw(win)

    try:
        win.getMouse()
    except GraphicsError:
        pass
    win.close()



# Get all functions into the function called "main".
def main():
    while True:
        get_user_inputs()
        display_inputed_data()
        data = open("Inputted_progression_data.txt").readlines()
        display_histogram(data)



# Execute the main function for run this programme.
if __name__ == "__main__":
    main()
