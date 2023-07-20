from flet import *
from reader import getPull, getPush, getLegs, getFavorite
import flet as ft
from views import views_handler

def main(page : Page):
    pass
    # page.horizontal_alignment = "center"
    # page.vertical_alignment = "center"
    # page.padding = 35
    # newPull = []
    # newPush = []
    # newLegs = []
    # newFav = []

    # BB = '#E7F2F8' #Baby blue
    # NB = '#1C3F60' #Navy blue
    # EB = '#353643' #Ebony
    # OR = "#FD7F20" #orange
    # AM = "#F3DAC0" #Tan basically

    # page.bgcolor = "white"

    def route_change(route):
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )


    page.on_route_change = route_change
    page.go('/login')

app(target=main, view= WEB_BROWSER)


    # def handle_experience_input(self):
    #     global experience_level
    #     experience_level = tf.value  

    # def handle_muscle_group_input(self):
    #     global fav_muscle_group
    #     fav_muscle_group = tf2.value
    #     newFav = getFavorite(experience_level, fav_muscle_group)
    #     page.go(page.route) #Goes to next view.

    #Page to show actual workouts.
    # def route_change(route):
    #     page.views.clear()
    #     view = View(
    #             "/",
    #             [
    #                 AppBar(title=Text("Gymio"), bgcolor= "#D3BBDD", color = "black"),
    #                 Container(
    #                     #set container attributes right here.
    #                 Column(
    #                     controls = [
    #                         Text("Your workouts:", 
    #                           size = 40, color = "black"), 
    #                         Text("Pull:", size = 23, color = "black"),
    #                         Text(getPull(experience_level), size = 20, color = "black"), 
    #                         Text("Push:", size = 23, color = "black"),
    #                         Text(getPush(experience_level), size = 20, color = "black"), 
    #                         Text("Legs:", size = 23, color = "black"),
    #                         Text(getLegs(experience_level), size = 20, color = "black"),
    #                         Text("Extra excercises:", size = 23, color = "black"),
    #                         Text(getFavorite(experience_level, fav_muscle_group), size = 20, color = "black")])
    #                 )
    #             ], horizontal_alignment="CENTER", vertical_alignment="CENTER", bgcolor="white"
    #         )
    #     page.views.append(
    #         view
    #     )
    #     page.update()
    
    
    
    


    # tf = TextField(label = "Beginner, Intermediate", color = "#303437", border_color=EB, width = 450, cursor_color="white")
    # tf2 = TextField(label = "Enter a muscle group", color = "#303437", border_color = EB, width = 450, cursor_color="white")
    # page.add(AppBar(title=Text("Gymio"), bgcolor= "#D3BBDD", color = "#303437"),
    #          Column(controls = [
    #             Text(value = "Welcome!", color = "#303437", size = 40),
    #             Text(value="What is your level of experience in the gym?", color= "#303437", size=20), 
    #             tf,
    #             ElevatedButton("Submit", color = "white", on_click = handle_experience_input),
                
    #             Text(value = "What muscle group would you like to grow the most?", color = "#303437", size = 20),
    #             tf2,    
    #             ElevatedButton("Submit", color = "white", on_click = handle_muscle_group_input)  
    #         ]
    #     )
    # )
    # page.on_route_change = route_change
    
