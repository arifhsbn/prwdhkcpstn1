from tabulate import tabulate
import re

UserData1 = [
    {
        'user': 'iwan3190',
    'password': '7190'
    },
    {
        'user':'cecep4540',
    'password': '3252'
    },
    {
        'user': 'helen2340',
    'password': '2304'
    },
]

Admin = [{'user': 'admin', 
         'password' : '0000'}]

student_score = [
    {
        'ID': 100,
        'Name': 'Jekjon',
        'Chemistry': '85',
        'Math' : '90',
        'English' : '70'
    },
    {
        'ID': 101,
        'Name': 'Nana',
        'Chemistry': '80',
        'Math' : '65',
        'English' : '80'
    },
    {
        'ID': 102,
        'Name': 'Kayla',
        'Chemistry': '90',
        'Math' : '90',
        'English' : '90'
    }
]

#Read

def user_login(username, password):
    filtered_users = filter(lambda user: user['user'] == username, UserData1)
    filtered_users = list(filtered_users)

    if filtered_users:
        if filtered_users[0]['password'] == password:
            print("User logged in successfully!")
            return 'user'
        else:
            print("Invalid password.")
    else:
        print("Invalid username.")
    return None

def admin_login(username, password):
    for admin_user in Admin:
        if admin_user['user'] == username and admin_user['password'] == password:
            print("Admin logged in successfully!")
            return 'admin'
    print("Invalid admin username or password.")
    return None

def show_registered_accounts():
    if UserData1:
        print("Registered Accounts:")
        print(tabulate(UserData1, headers='keys', tablefmt='fancy_grid'))
    else:
        print("No registered accounts.")

def read_data():
    print(tabulate(student_score, headers='keys', tablefmt='fancy_grid'))

def read_data2():
    low_scores = []
    for student in student_score:
        for subject, score in student.items():
            if subject != 'ID' and subject != 'Name':
                try:
                    if int(score) < 75:
                        low_scores.append([student['Name'], subject, score])
                except ValueError:
                    print(f"Invalid score for {student['Name']} in {subject}: {score}")
    if low_scores:
        print ('Remedial Table')
        print (tabulate(low_scores, headers=["Name", "Subject", "Score"], tablefmt="fancy_grid"))
    else:
        print("No scores below 75.")

#create 

def add_data(student_score):
    if student_score:
        next_id = max(student['ID'] for student in student_score) + 1
    else:
        next_id = 100 

    name = input("Enter student name (alphabetic characters only, maximum 10 characters): ")
    if not (name.isalpha() and len(name) <= 10):
        print("Error: Student name must contain only alphabetic characters and be maximum 10 characters long.")
        return

    score_pattern = re.compile(r'^\d{1,3}$')

    while True:
        chemistry = input("Enter Chemistry score (1 to 3 characters): ")
        if not score_pattern.match(chemistry):
            print("Error: Chemistry score must be numeric and between 1 and 3 characters long.")
            continue
        chemistry = int(chemistry)

        math = input("Enter Math score (1 to 3 characters): ")
        if not score_pattern.match(math):
            print("Error: Math score must be numeric and between 1 and 3 characters long.")
            continue
        math = int(math)

        english = input("Enter English score (1 to 3 characters): ")
        if not score_pattern.match(english):
            print("Error: English score must be numeric and between 1 and 3 characters long.")
            continue
        english = int(english)
        
        break

    new_student_data = {'ID': next_id, 'Name': name, 'Chemistry': chemistry, 'Math': math, 'English': english}
    student_score.append(new_student_data)
    print("Data added successfully!")

def add_user_data():
     while True:
        username = input("Enter username (first name and 4 numbers, e.g., john1234): ")
        if not re.match(r"^[a-zA-Z]+[0-9]{4}$", username):
            print("Error: Username must start with a letter, followed by 4 digits.")
            continue

        while True:
            password = input("Enter password (4 digits): ")
            if not re.match(r"^[0-9]{4}$", password):
                print("Error: Password must be 4 digits.")
                continue
            break

        new_user_data = {'user': username, 'password': password}
        UserData1.append(new_user_data)
        print("User data added successfully!")
        break

#update

def change_user_credentials():
    while True:
        username = input("Enter the username of the user whose credentials you want to change: ")

        if not re.match(r"^[a-zA-Z]+[0-9]{4}$", username):
            print("Error: Username must start with a letter followed by 4 digits.")
            continue

        found = False
        for user in UserData1:
            if user['user'] == username:
                found = True
                new_username = input("Enter the new username (leave blank to keep current): ")

                if new_username and not re.match(r"^[a-zA-Z]+[0-9]{4}$", new_username):
                    print("Error: New username must start with a letter followed by 4 digits.")
                    continue

                new_password = input("Enter the new password (leave blank to keep current): ")

                if new_password and not re.match(r"^[0-9]{4}$", new_password):
                    print("Error: New password must be 4 digits.")
                    continue

                if new_username:
                    user['user'] = new_username
                    print(f"Updated username for {username} to {new_username}")

                if new_password:
                    user['password'] = new_password
                    print(f"Updated password for {username}")

                break

        if found:
            break
        else:
            print(f"User with username {username} not found.")


def update_student_id():
    while True:
        current_id = input("Enter the current ID of the student you want to update: ")
        new_id = input("Enter the new ID: ")

        if len(current_id) > 3 or len(new_id) > 3:
            print("Error: ID must be up to 3 characters long.")
        else:
            try:
                current_id = int(current_id)
                new_id = int(new_id)
                break
            except ValueError:
                print("Error: IDs must be Numbers.")

    found = False
    for student in student_score:
        if student['ID'] == current_id:
            student['ID'] = new_id
            found = True
            print(f"Updated ID for {student['Name']} to {new_id}")
            break

    if not found:
        print(f"Student with ID {current_id} not found.")

def update_student_name():
    current_name = input("Enter the current name of the student you want to update (max 10 characters): ")
    new_name = input("Enter the new name (max 10 characters): ")

    if not (1 <= len(current_name) <= 10) or not (1 <= len(new_name) <= 10):
        print("Error: Names must be between 1 and 10 characters.")
        return

    if not current_name.isalpha() or not new_name.isalpha():
        print("Error: Names must contain only alphabetic characters.")
        return

    found = False
    for student in student_score:
        if student['Name'] == current_name:
            student['Name'] = new_name
            found = True
            print(f"Updated name for student with ID {student['ID']} to {new_name}")
            break

    if not found:
        print(f"Student with name {current_name} not found.")


def update_student_score():
    print("\nUpdate Student Data:")
    print("1. ID")
    print("2. Name")
    print("3. Score")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        update_student_id()
    elif choice == "2":
        update_student_name()
    elif choice == "3":
        update_student_subject_score()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

def update_student_subject_score():
    print("\nUpdate Student Subject Score:")
    print("1. Chemistry")
    print("2. Math")
    print("3. English")
    
    choice = input("Enter the subject you want to update: ")
    
    if choice == "1":
        update_student_score_by_subject('Chemistry')
    elif choice == "2":
        update_student_score_by_subject('Math')
    elif choice == "3":
        update_student_score_by_subject('English')
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

def update_student_score_by_subject(subject):
    student_id = input("Enter the ID of the student you want to update (max 3 characters): ")
    new_score = input(f"Enter the new {subject} score (max 2 characters): ")

    if not (1 <= len(student_id) <= 3):
        print("Error: ID must be between 1 and 3 characters.")
        return

    if not (1 <= len(new_score) <= 3):
        print("Error: Score must be between 1 and 3 characters.")
        return

    if not student_id.isdigit():
        print("Error: ID must be a number.")
        return

    if not new_score.isdigit():
        print("Error: Score must be a number.")
        return

    found = False
    for student in student_score:
        if str(student['ID']) == student_id:
            found = True
            if subject in student:
                try:
                    student[subject] = int(new_score)
                    print(f"Updated {subject} score for {student['Name']} to {new_score}")
                except ValueError:
                    print("Error: Score must be numeric.")
            else:
                print(f"Subject {subject} not found for student {student['Name']}")
            break

    if not found:
        print(f"Student with ID {student_id} not found.")


#Delete

def delete_subject_score():
    print("Available students:")
    for student in student_score:
        print(f"- {student['Name']} (ID: {student['ID']})")

    student_id = input("Enter the ID of the student you want to update: ")
    found = False
    for student in student_score:
        if str(student['ID']) == student_id:
            found = True
            print(f"Selected student: {student['Name']}")

        
            subjects = [key for key in student.keys() if key != 'ID' and key != 'Name']
            print("Available subjects:")
            for i, subject in enumerate(subjects, 1):
                print(f"{i}. {subject}")

        
            subject_index = input("Enter the number of the subject you want to delete: ")
            try:
                subject_index = int(subject_index)
                if 1 <= subject_index <= len(subjects):
                    subject = subjects[subject_index - 1]
                    del student[subject]
                    print(f"Deleted {subject} score for {student['Name']}")
                else:
                    print("Invalid subject number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            break

    if not found:
        print("Student not found.")

def delete_registered_account():
    username = input("Enter the username of the registered account you want to delete: ")
    found = False
    for i, data in enumerate(UserData1):
        if data['user'] == username:
            del UserData1[i]
            found = True
            print(f"Deleted registered account with username {username}")
            break

    if not found:
        print(f"Registered account with username {username} not found.")

def delete_student_score():
    data_id = input("Enter the ID of the student whose score you want to delete: ")
    found = False
    for i, data in enumerate(student_score):
        if str(data.get('ID')) == data_id:
            del student_score[i]
            found = True
            print(f"Deleted student score with ID {data_id}")
            break

    if not found:
        print(f"Student with ID {data_id} not found.")

def sort_data():
    while True:
        print("\nSort Data By:")
        print("1. ID")
        print("2. Name")
        print("3. Subject Score")
        print("4. Back to User Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            sorted_data = sorted(student_score, key=lambda x: x['ID'])
            print(tabulate(sorted_data, headers='keys', tablefmt='fancy_grid'))
        elif choice == "2":
            sorted_data = sorted(student_score, key=lambda x: x['Name'])
            print(tabulate(sorted_data, headers='keys', tablefmt='fancy_grid'))
        elif choice == "3":
            subject = input("Enter the subject you want to sort by (Chemistry/Math/English): ")
            if subject not in ['Chemistry', 'Math', 'English']:
                print("Invalid subject.")
                continue
            sorted_data = sorted(student_score, key=lambda x: x[subject])
            print(tabulate(sorted_data, headers='keys', tablefmt='fancy_grid'))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def main():
    print("\nWelcome to the Student Score System!")
    
    user_type = None
    
    while user_type not in ['user', 'admin']:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if user_login(username, password):
            user_type = 'user'
            print("User logged in successfully!")
        elif admin_login(username, password):
            user_type = 'admin'
            print("Admin logged in successfully!")
        else:
            print("Invalid username or password.")
    
    if user_type == 'user':
        user_menu()
    elif user_type == 'admin':
        admin_menu()

def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Show Scores")
        print("2. Add Score")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            read_data()  
            option = input("Select an option:\n1. Sort by\n2. Show Remedial Table\n3. Back to Main Menu\nEnter your choice: ")
            if option == "1":
                sort_data()
            elif option == "2":
                read_data2()
            elif option == "3":
                print("Returning to User Menu.")
            else:
                print("Invalid option.")
        elif choice == "2":
            add_data()
        elif choice == "3":
            update_student_score()  
        elif choice == "4":
            delete_student_score()  
            continue
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Show Registered Accounts")
        print("2. Add Account")
        print("3. Change User Credentials")
        print("4. Delete Registered Account")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_registered_accounts()
        elif choice == "2":
            add_user_data()
        elif choice == "3":
            change_user_credentials()
        elif choice == "4":
            delete_registered_account()
            continue
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
main()