<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Projects Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .project {
            margin-bottom: 30px;
            padding: 15px;
            border-left: 4px solid #3498db;
            background-color: #f1f7fc;
            border-radius: 4px;
        }
        h2 {
            color: #2980b9;
            margin-top: 0;
        }
        h3 {
            color: #16a085;
            margin-bottom: 5px;
        }
        p {
            font-weight: bold;
            margin-bottom: 5px;
        }
        ul {
            margin-top: 5px;
            padding-left: 20px;
        }
        li {
            margin-bottom: 6px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>My Projects</h1>

    <!-- PROJECT 1 -->
    <div class="project">
        <h2>MY FIRST PROJECT</h2>
        <h3>Personal Finance Account</h3>
        <p>Features</p>
        <ul>
            <li>Different users can log in (Separate login page for each user)</li>
            <li>Create, update, and delete transactions</li>
            <li>Filter and view transactions by specific timeline or date range</li>
            <li>Track income, expenses, and total balance dynamically</li>
        </ul>
    </div>

    <!-- PROJECT 2 -->
    <div class="project">
        <h2>MY SECOND PROJECT</h2>
        <h3>School / College Portal Website</h3>
        <p>Features</p>
        <ul>
            <li><strong>Role Selection:</strong> Continuous login system for Teachers and Students</li>
            <li><strong>Teacher Features:</strong>
                <ul>
                    <li>Schedule lectures with Start and End times (Restricted to working hours: 08:00 - 17:00)</li>
                    <li>Automatic time-conflict detection to prevent overlapping lectures on the same day</li>
                    <li>Post notices and announcements with auto-generated dates</li>
                    <li>Upload homework assignments with due dates</li>
                    <li>Mark student attendance records (Present / Absent)</li>
                </ul>
            </li>
            <li><strong>Student Features:</strong>
                <ul>
                    <li>View school notices and announcements</li>
                    <li>Check daily lecture timetables in real-time</li>
                    <li>View assignment details and submit answers directly</li>
                    <li>Check personal attendance history by date</li>
                </ul>
            </li>
            <li><strong>Data Management:</strong> Integrated with JSON persistent storage (`data.json`)</li>
        </ul>
    </div>

<!--    <!-- PROJECT 3 -->
    <div class="project">
        <h2>MY THIRD PROJECT</h2>
        <h3>E-Commerce / Online Store App</h3>
        <p>Features</p>
        <ul>
            <li>User account creation and profile management</li>
            <li>Product listing with categories, search, and filtering</li>
            <li>Shopping cart management (Add, update quantity, remove items)</li>
            <li>Order summary and checkout processing</li>
        </ul>
    </div>

    <!-- PROJECT 4 -->
    <div class="project">
        <h2>MY FOURTH PROJECT</h2>
        <h3>Task Management & Todo Tracker</h3>
        <p>Features</p>
        <ul>
            <li>Add, edit, and delete daily tasks</li>
            <li>Set priority levels (High, Medium, Low) and due dates</li>
            <li>Mark tasks as completed or pending</li>
            <li>Save tasks locally so data stays intact after closing</li>
        </ul>
    </div> -->

</div>

</body>
</html>
