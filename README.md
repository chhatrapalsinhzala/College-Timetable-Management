# College-Timetable-Management

simple college classes management app using Django. This app doesn't contain any templates it has all basic apis only.

 

Setup Guide



1) Create your virtual env first in Python3.

      virtualenv -p python3 env

  

2) activate env clone the repository and install required packages. 

      source env/bin/activate

      pip install -r requirements.txt

  

3) For a completely new database change DATABASE variable in the settings.py and perform migrations. Then start server.

      python manage.py makemigrations

      python manage.py migrate

      python manage.py runserver

  

In this project I have created 3 apps

    - classapp : stores all class related details. (models like subject, class etc.)

    - staff : stores the class teacher related information (staff model)

    - student : store details related to student (models like student and student_in_class etc.)

    

To Implement this I have created 3 permission levels:

    - student : students can only see the data like class details, their class timings,etc. They can not create or edit any information of the table. 

    - staff : Staff can create classes and can add the student in the class.

    - admin : All permissions with the access of Django admin.


Project APIs
    
    - Rigister as a student or staff.
    - Create class, Delete Class, Get class list.
    - Add student in class, get all student class list and remove student form classs.
    (I have shared the postman collection to test all apis.)
 


















