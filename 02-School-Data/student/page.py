import json
import os

def load_school_data():
    path = "teacher/data.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"notices": [], "assignments": [], "attendance_records": {}, "lectures": []}
    return {"notices": [], "assignments": [], "attendance_records": {}, "lectures": []}

def student_dashboard():
    print("\n" + "=" * 35)
    print("      Welcome to Student Portal      ")
    print("=" * 35)
    
    while True:
        print("\nChoose an action:")
        print("1. View Notices")
        print("2. View Lecture Schedule")
        print("3. View Assignments & Submit Answer")
        print("4. View Attendance Records")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        data = load_school_data()
        
        if choice == "1":
            print("\n--- School Notices ---")
            notices = data.get("notices", [])
            if notices:
                for i, n in enumerate(notices, 1):
                    print(f"  {i}. Title: {n.get('title')} (Date: {n.get('date')})")
                    print(f"     Content: {n.get('content')}")
                    print("-" * 30)
            else:
                print("  No notices available.")
                
        elif choice == "2":
            print("\n--- Lecture Schedule ---")
            lectures = data.get("lectures", [])
            if lectures:
                for i, lec in enumerate(lectures, 1):
                    print(f"  {i}. {lec.get('title')} | Day: {lec.get('day')} | Time: {lec.get('time')}")
            else:
                print("  No lectures scheduled.")
                
        elif choice == "3":
            print("\n--- Assignments ---")
            assignments = data.get("assignments", [])
            if assignments:
                for asm in assignments:
                    print(f"  ID: {asm.get('id')} | Title: {asm.get('title')} | Due: {asm.get('due')}")
                
                sub_choice = input("\nWould you like to submit homework? (y/n): ").strip().lower()
                if sub_choice == 'y':
                    try:
                        asm_id = int(input("Enter Assignment ID to submit: ").strip())
                        student_name = input("Enter your Name: ").strip()
                        answer_text = input("Enter your submission text/answer: ").strip()
                        
                        found = False
                        for asm in assignments:
                            if asm.get("id") == asm_id:
                                found = True
                                if "submissions" not in asm:
                                    asm["submissions"] = []
                                asm["submissions"].append({"student": student_name, "answer": answer_text})
                                break
                        
                        if found:
                            # Save back to JSON file
                            path = "teacher/data.json"
                            with open(path, "w") as f:
                                json.dump(data, f, indent=4)
                            print(" Homework submitted successfully!")
                        else:
                            print(" Assignment ID not found.")
                    except ValueError:
                        print(" Invalid ID format.")
            else:
                print("  No assignments posted.")
                
        elif choice == "4":
            print("\n--- Attendance Records ---")
            records = data.get("attendance_records", {})
            if records:
                for date, students in records.items():
                    print(f"  Date: {date}")
                    for student, status in students.items():
                        print(f"    - {student}: {status}")
            else:
                print("  No attendance records found.")
                
        elif choice == "5":
            print("\nReturning to Main Menu...\n")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")