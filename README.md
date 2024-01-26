**User’s Guide **

1.1 Getting Started

1.1.1 Account Creation
Once you open the main page, you will see a page where you can either go to the login page or the register page. If you don’t have an account yet, you should first register. Register using your Bilkent ID, username, email address and password with specifying your user type.

1.1.2 Logging In
Once registered, log in using your credentials. If you forget your password, use the "Forgot Password" option to reset it. Once logged in, each user has a homepage where they see posts by other users creating posts, and a search where the user can search for posts or other users. The user can access their profile page here as well.

1.1.3 User Types
Bilkonect has four user types: Student, Admin, Staff, and Instructor. Each user type has specific permissions and features tailored to their roles.

1.2 Main Features

1.2.1 Posting
The most important feature of the application is the posting feature. Users can create posts to connect with others on campus. Once logged in, you can post a post using the “create post” button on the left sidebar.
 
1.2.2 Post Categories
Bilkonect offers ten post categories:
Donation Post
Found Item Post
Lost Item Post
Second-Hand Sale Post
Need Post
Roommate Search Post
Study Buddy Search Post
Gym Buddy Search Post
Trip Buddy Search Post
Course Material Search Post

Different post types include different fields that the user should fill in. For example second-hand sale posts have a price field where roommate search posts don’t. Some post types also have an image related to the post. Another thing that differentiates posts is that Lost Item Posts and Found Item Posts have a feature called mark. Users can mark these posts as found and mine, respectively.
Users can see a small version of a post on their feed and homepage, and when they click on it, they can see the big version of the post with more details and can chat with the post owner.

1.2.3 Visibility Settings
The application offers different and specialized visibility settings depending on user type. To make the post feature more efficient, only Student-type users can create and see study buddy and course-related posts. Also, on a user's feed, their own posts are not shown.

1.2.4 Chat Functionality
Another one of the most important features is chatting functionalityEngage with other users by chatting through posts. Discuss details, coordinate plans, or simply connect with someone who shares your interests.
 
1.3 User Types and Permissions
1.3.1 Student
Students can create and view all types of posts. They have access to study buddy and course-related posts exclusively.

1.3.2 Admin Staff
Admin staff have elevated privileges, allowing them to monitor and moderate posts. They can also send campus-wide announcements. There will be one hard-coded admin in the system.

1.3.3 Instructor
Instructors have features similar to students but can also create course-related posts for better communication with their students.

1.4. Additional Features

1.4.1 Notifications
Stay updated with notifications for new posts, replies, and announcements. Customize your notification preferences in the settings.

1.4.2 Profile Management
Keep your profile information up-to-date. Add a profile picture and a brief bio to enhance your Bilkonect experience.

1.4.3 Reporting and Moderation
Users can report inappropriate content. Admin staff can review and take appropriate action, ensuring a safe and respectful community.

1.4.4 Search Bar
Users can search for other users by their username, where they can see all the users that include the search text in their username. The user can follow other users through here. Users can also search for posts by their title, which works similarly to user search.

**Build Instructions
**
1- If the system does not have python and node.js, they need to be installed. For that, the official documentation can be useful. (python, node.js)

2- The project’s repository from Github (https://github.com/ozgur2dag/Bilkonect-full-app) must be cloned to your system using “git clone”.

3- Using your operating system’s shell (Bash on GNU/Linux, terminal on MacOS, or cmd for Windows, for example), navigate to the directory where you cloned the repository, for example, “cd C:\Users\%USERPROFILE%\Desktop\bilkonect\Source_Code” on Windows.

4- Execute the following command in the system’s shell:
	python -m venv venv
	if it does not create a directory called venv try:
	python3 -m venv venv

5- Execute the following command based on your operating system:
	a)If you are running on MacOS and GNU/Linux:
		source venv/bin/activate
	b)If you are running on Windows:
		venv/Scripts/activate

6- Execute the following commands based on their order: 
pip install -r requirements.txt
pip install flask_cors
pip install flask_socketio
python app.py
This should run the backend. If it does not work, try:
python3 app.py

7- Now open a new system shell and navigate to the frontend directory, for e.g., “cd C:\Users\%USERPROFILE%\Desktop\bilkonect\sample”

8- Execute the following commands based on their order:
	npm install
	npm start
Once the terminal indicates that it is working, you can use Bilkonect from http://localhost:3000/

9- You can close the app by CTRL+C on Windows or CTRL+C on MacOS on both system shells.
