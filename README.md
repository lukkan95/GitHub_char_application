# GitHub_char_application


This application provides graphic interpretation based on amount of sings in GitHub users repositories.
All data is presented by bar charts and additionally, at one time, u can request for many GitHub users.

## **---- Usage guide ----**

1) When application window will pop up, firstly, in down left corner insert Your username and authorization token 
   from GitHub. It will enable multi-requesting (without authorization limit of requests is set to 60 per hour, 
   but with authorization it's rising to 5000 requests per hour). After successfully insertion, click "Save 
   button". The green text will pop up, and confirm that the transferred values have been saved.


2) In next step, insert the username of single user or many users, who You want to search in entry field under 
   inscription "Search GitHub user/-s". In case of multi-searching for many users, separate nicknames of individual 
   users using common separators (".", ",", ":", ";"). By that, application will try to automatically separate inserted 
   usernames. Remember to not using "-" as separator cause this sing belongs as available to use in usernames on GitHub. 
   After all click "Show" button.


3) Searched user/-s will be transferred and located in Option Menu in top left corner. Additionally, first user's graph 
   containing sums of every unique characters (signs) in all user's repositories will be shown automatically. 
   To display graph of other user, choose from Option Menu and type "Show".


4) In case of next searching, insert new user/-s same as in point 2 and repeat step 2 and 3.


5) In the end, exit application by typing "X" button in top right corner. Program will be terminated  immediately.


## **---- About tests ----**

   In addition to the application some test cases are attached. In "test_GUI_API_multisearching" there are unit
   tests which checks if application works properly. To provide correct working of test, it's need to complete 
   username and token in 'git_acc_data.py' - both taken from GitHub. In 'conftest.py' (tests configuration file 
   placed in test directory) there is a pytest fixture created, used in unit tests.