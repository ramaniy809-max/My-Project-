import json
import os
from datetime import datetime

def load_teacher_data():
    """Loads teacher data from JSON file, returning a default structure if it doesn't exist."""
    path = "teacher/data.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"announcements": [], "assignments": [], "lectures": []}
    return {"announcements": [], "assignments": [], "lectures": []}

def save_teacher_data(data):
    """Saves updated teacher data back into the JSON file."""
    os.makedirs("teacher", exist_ok=True)
    path = "teacher/data.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def is_valid_working_hours(time_str):
    """
    Validates if the entered time (HH:MM in 24-hr format) falls between 08:00 and 17:00 (8 AM - 5 PM).
    """
    try:
        lecture_time = datetime.strptime(time_str, "%H:%M").time()
        start_work_time = datetime.strptime("08:00", "%H:%M").time()
        end_work_time = datetime.strptime("17:00", "%H:%M").time()
        
        return start_work_time <= lecture_time <= end_work_time
    except ValueError:
        return False

def teacher_dashboard():
    print("\n" + "=" * 35)
    print("      Welcome to Teacher Portal      ")
    print("=" * 35)
    
    while True:
        print("\nChoose an action:")
        print("1. Schedule a Lecture")
        print("2. Post an Announcement")
        print("3. Post a Homework/Assignment")
        print("4. View All Uploaded Data")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        data = load_teacher_data()
        
        # Ensure 'lectures' list exists in data
        if "lectures" not in data:
            data["lectures"] = []
        
        if choice == "1":
            print("\n--- Schedule a Lecture ---")
            title = input("Enter Lecture/Subject Title: ").strip()
            day = input("Enter Day (e.g., Monday, Tuesday): ").strip()
            print("Note: School working hours are between 08:00 and 17:00 (24-hour format).")
            start_time = input("Enter Lecture Start Time (HH:MM, e.g., 09:00): ").strip()
            end_time = input("Enter Lecture End Time (HH:MM, e.g., 10:00): ").strip()
            
            if not title or not day:
                print(" Title and Day cannot be empty.")
            elif not is_valid_working_hours(start_time) or not is_valid_working_hours(end_time):
                print("\n Invalid Time! Lectures must be strictly within working hours (08:00 to 17:00).")
            else:
                try:
                    s_time = datetime.strptime(start_time, "%H:%M").time()
                    e_time = datetime.strptime(end_time, "%H:%M").time()
                    
                    if s_time >= e_time:
                        print("\n Error: Start time must be earlier than the end time!")
                    else:
                        # Check for lecture time conflicts/overlaps on the same day
                        conflict = False
                        conflicting_title = ""
                        
                        for lec in data.get("lectures", []):
                            if lec.get("day", "").lower() == day.lower():
                                ex_start = datetime.strptime(lec["start_time"], "%H:%M").time()
                                ex_end = datetime.strptime(lec["end_time"], "%H:%M").time()
                                
                                # Overlap condition: (StartA < EndB) and (EndA > StartB)
                                if s_time < ex_end and e_time > ex_start:
                                    conflict = True
                                    conflicting_title = lec.get("title")
                                    break
                        
                        if conflict:
                            print(f"\n Error: Time conflict! Another lecture ('{conflicting_title}') is already scheduled on {day} during this time slot.")
                        else:
                            new_lecture = {
                                "title": title,
                                "day": day,
                                "start_time": start_time,
                                "end_time": end_time
                            }
                            data["lectures"].append(new_lecture)
                            save_teacher_data(data)
                            print(f" Lecture '{title}' scheduled successfully for {day} from {start_time} to {end_time}!")
                            
                except ValueError:
                    print("\n Invalid time format! Please use HH:MM (24-hour format).")
                
        elif choice == "2":
            print("\n--- Post Announcement ---")
            announcement = input("Enter announcement text: ").strip()
            if announcement:
                data["announcements"].append(announcement)
                save_teacher_data(data)
                print(" Announcement posted successfully!")
            else:
                print("Announcement cannot be empty.")
                
        elif choice == "3":
            print("\n--- Post Assignment ---")
            title = input("Enter assignment title: ").strip()
            description = input("Enter assignment description: ").strip()
            
            if title and description:
                new_assignment = {"title": title, "description": description}
                data["assignments"].append(new_assignment)
                save_teacher_data(data)
                print(" Assignment uploaded successfully!")
            else:
                print("Title and description cannot be empty.")
                
        elif choice == "4":
            print("\n--- Current Uploaded Data ---")
            
            print("\n[Lectures Schedule]")
            if data.get("lectures"):
                for i, lec in enumerate(data["lectures"], 1):
                    print(f"  {i}. {lec['title']} | Day: {lec['day']} | Time: {lec['start_time']} - {lec['end_time']}")
            else:
                print("  No lectures scheduled yet.")
                
            print("\n[Announcements]")
            if data.get("announcements"):
                for i, ann in enumerate(data["announcements"], 1):
                    print(f"  {i}. {ann}")
            else:
                print("  No announcements posted yet.")
                
            print("\n[Assignments]")
            if data.get("assignments"):
                for i, asm in enumerate(data["assignments"], 1):
                    print(f"  {i}. Title: {asm['title']} | Details: {asm['description']}")
            else:
                print("  No assignments uploaded yet.")
                
        elif choice == "5":
            print("\nReturning to Main Menu...\n")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")