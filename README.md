# Purpose
Web app created that gives user a weight lifting routine to target the whole body following the push, pull, legs workout format. 

# Technologies
Gymio is a web app that uses Flet(Python framework powered by flutter), Pandas, and Python.

# How it works?
Using the megaGymDataset.csv file that contains a pletora of gym excercises based on what body part they target, the program filters the excercises and randomly chooses one from the criteria. For example, in the function getPull(): we filter based on excercises targetting the back, biceps, and forearms and return a list format of those excercises. Once the lists with the workouts have been made, Flet is used to start the web app and show the user the workouts based on the answers to the questions they fill out. 

# Using the app
Register as a user, or login. Fill out the two questions listed in the main page, and submit your answers. You will then be prompted to a page with the workouts for push, pull, and legs.

# Status
As of July 26, 2023, user login functionality is being implemented.


