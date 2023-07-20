from flet import * 
from reader import getPull, getPush, getLegs, getFavorite
import pages.home as home

class WorkOuts(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page


    def build(self):
        return Column(
            controls = [
                Container(
                    height=800,width=1600, padding = 30,
                    bgcolor='white', 
                    content =Column(controls = [
                            Text("Your workouts:", size = 40, color = "black"), 
                            Text("Pull:", size = 23, color = "black"),
                            Text(getPull(home.experience_level), size = 20, color = "black"), 
                            Text("Push:", size = 23, color = "black"),
                            Text(getPush(home.experience_level), size = 20, color = "black"), 
                            Text("Legs:", size = 23, color = "black"),
                            Text(getLegs(home.experience_level), size = 20, color = "black"),
                            Text("Extra excercises:", size = 23, color = "black"),
                            Text(getFavorite(home.experience_level, home.fav_muscle_group), size = 20, color = "black")
                        ])
                    )
            ]
        )