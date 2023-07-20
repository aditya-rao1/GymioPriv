from flet import * 
from pages.login import Login
from pages.home import Home
from pages.signUp import signUp
from pages.workouts import WorkOuts

def views_handler(page):
    return {
        '/':View(route = '/'
                 , controls = [
                     Home(page)
                 ]
        ),
        '/login': View(route = '/login'
                 , controls = [
                     Login(
                        page
                     )
                 ], horizontal_alignment="CENTER", vertical_alignment="CENTER"), 

        '/signup': View(route = '/signup', 
                        controls = [
                            signUp(page)
                        ]),

        '/workouts': View(route = '/workouts', controls = [
                        WorkOuts(page)
        ])
    }



