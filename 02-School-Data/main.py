from student.page import student_dashboard
from teacher.page import teacher_dashboard

def main():
    while True:
        print("=" * 40)
        print("------- Welcome to School Portal -------")
        print("=" * 40)
        print("\n\nSelect Role")
        print("1. Student")
        print("2. Teacher")
        print("3. Exit Portal") # Added an option to cleanly exit the app
        
        while True:
            try:
                role = int(input("Enter the choice (1, 2, or 3): "))
                
                # Check if the number is outside the valid options (1, 2, or 3)
                if role < 1 or role > 3:
                    raise ValueError("invalid input enter correct input")
                
                # If input is valid, route to the correct dashboard or exit
                if role == 1:
                    print("\nOpening Student Portal...\n")
                    student_dashboard()
                elif role == 2:
                    print("\nOpening Teacher Portal...\n")
                    teacher_dashboard()
                elif role == 3:
                    print("\nExiting School Portal. Goodbye!\n")
                    return # Exits the main function entirely, stopping the app
                    
                break # Break out of inner loop to re-display the main menu when dashboards finish
                
            except ValueError as e:
                # Catches both non-integer inputs (like letters) and our custom raised ValueError
                if str(e):
                    print(e)
                else:
                    print("invalid input enter correct input")
        
        print("\n" + "-" * 40 + "\n") # Visual separator before looping back to main menu

if __name__ == "__main__":
    main()