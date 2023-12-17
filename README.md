1ST-Open Terminal in the "Source Code" folder and run: "python app.py" to initalize backend and database.

2ND-Open a new terminal and run "npm start" to run React.js frontend of the application.

Make sure to follow the instructions file in the "Source Code" folder.
Also make sure you have installed npm (npm -install) in your "React" folder.

READ!!!: If the venv does not work on your local you can delete the "venv" folder and follow the instructions below to rebuild your virtual environment.

HERE  ARE SOME INFO THAT COULD HELP BUILDING AND INITALIZING THE PROJECT:

Try: python app.py
If the built in virtual environment does not work, follow these steps:

1) python -m venv venv
2) source venv/bin/activate
Inside the correct directory
3) pip install -r requirements.txt
4) pip install flask-cors
5) pip install flask-socketio
6) python3 app.py

In Postman:
1) open workspace
2) add request 
3) POST ile http://127.0.0.1:5000/register
4) Body'den raw seçip JSON seçip info girin
5) JSON register için:
{
  "bilkent_id": 22103044,
  "username": "zeynepsuucan",
  "password": "Su29112911!",
  "usertype": "Student",
  "email": "zeynepsuucan@gmail.com"
}
Errors:
{
    "message": "Bilkent ID already exists"
}
,
{
    "message": "Username is already taken"
}
,
{
    "message": "Email address is already registered"
}


11) to login: POST http://127.0.0.1:5000/login
    
12) JSON login:
{
  "username": "zeynepsuucan",
  "password": "Su29112911"
}
Correct Login: 
{
    "bilkent_id": 22103044,
    "username": "zeynepsuucan",
    "usertype": "Student",
    "email": "su.ucan@ug.bilkent.edu.tr",
    "score": 0
}
Incorrect Login:
{
    "message": "Invalid credentials"
}

Correct JSON's for all post types:

1. Donation Post: donation.json
{
  "title": "Sample Donation Post",
  "description": "This is a sample donation post.",
  "post_type": "DonationPost",
  "owner": "zeynepsuucan",
  "criteria": "The person to get the donation needs to be a student.",
  "share_date": "2023-12-31T12:00:00",
  "image": "https://example.com/donation_image.jpg",
  "isDonated": false,
  "isNegotiated": false
}

2. Found Item Post: founditem.json
{
  "title": "Sample Found Item Post",
  "description": "This is a sample found item post.",
  "post_type": "FoundPost",
  "owner": "ozgurikidag",
  "share_date": "2023-12-31T12:00:00",
  "ownerFound": false,
  "image": "https://example.com/found_item_image.jpg"
}

3. Lost Item Post: lostitem.json
{
  "title": "Sample Lost Item Post",
  "description": "This is a sample lost item post.",
  "post_type": "LostPost",
  "owner": "osmanberkay",
  "share_date": "2023-12-31T12:00:00",
  "isFound": false,
  "image": "https://example.com/lost_item_image.jpg"
}

4. Second Hand Sale Post: secondhandsale.json
{
  "title": "Sample Second Hand Sale Post",
  "description": "This is a sample second-hand sale post.",
  "post_type": "SecondHandSalePost",
  "owner": "bartummc",
  "share_date": "2023-12-31T12:00:00",
  "price": 50.0,
  "image": "https://example.com/sale_item_image.jpg",
  "isNegotiated": false,
  "isSold": true
}

5. Need Post: need.json
{
  "title": "Sample Need Post",
  "description": "This is a sample need post.",
  "post_type": "NeedPost",
  "owner": "zeynepsuucan",
  "share_date": "2023-12-31T12:00:00",
  "foundNeed": true,
  "isBorrowed": false
}

6. Course Material Post: coursematerial.json
{
  "title": "Sample Course Material Post",
  "description": "This is a sample course material post.",
  "post_type": "CourseMaterialPost",
  "owner": "ozgurikidag",
  "criteria": "Textbooks for sale",
  "share_date": "2023-12-31T12:00:00",
}

7. Study Buddy Post: studybuddy.json
{
  "title": "Sample Study Buddy Post",
  "description": "This is a sample study buddy post.",
  "post_type": "StudyBuddyPost",
  "owner": "osmanberkay",
  "criteria": "Mathematics study group",
  "share_date": "2023-12-31T12:00:00",
  "course": "Mathematics"
}

8. Gym Buddy Post: gymbuddy.json
{
  "title": "Sample Gym Buddy Post",
  "description": "This is a sample gym buddy post.",
  "post_type": "GymBuddyPost",
  "owner": "bartummc",
  "criteria": "Fitness partner",
  "share_date": "2023-12-31T12:00:00"
}

9. Trip Post: trip.json
{
  "title": "Sample Trip Post",
  "description": "This is a sample trip post.",
  "post_type": "TripPost",
  "owner": "zeynepsuucan",
  "criteria": "Travel companion",
  "share_date": "2023-12-31T12:00:00",
  "tripDate": "2024-01-15T08:00:00",
  "destination": "Beach Resort",
  "departure": "City Center"
}

10. Roommate Post: roommate.json
{
  "title": "Sample Roommate Post",
  "description": "This is a sample roommate post.",
  "post_type": "RoommatePost",
  "owner": "zeynepsuucan",
  "criteria": "Looking for a roommate",
  "share_date": "2023-12-31T12:00:00"
}
 
report json:
{
    "reporterId": 22103044,
    "reporteeId": 22103805,
    "reason": "don't like post",
    "date": "2023-12-31T12:00:00"
}
