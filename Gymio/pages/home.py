from flet import * 
from reader import getPull, getPush, getLegs, getFavorite

newPull = []
newPush = []
newLegs = []
newFav = []

tf = TextField(label = "Beginner, Intermediate", color = "#303437", border_color="black", width = 450, cursor_color="white")
tf2 = TextField(label = "Enter a muscle group", color = "#303437", border_color = "black", width = 450, cursor_color="white")

def handle_experience_input(self):
    global experience_level
    experience_level = tf.value  


#BECAUSE YOU MADE IT GLOBAL YOU CAN CALL IT FROM ANYWHERE INCLUDING THE NEW CLASS for the.
def handle_muscle_group_input(self):
    global fav_muscle_group
    fav_muscle_group = tf2.value
    self.page.go('/workouts')


class Home(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page


  def build(self):
    return Column(
      controls = [
         Container(
          height=800,width=1600, padding = 30,
          bgcolor='white', 
          content = Column(controls = [
                Text(value = "Welcome!", color = "#303437", size = 40),
                Text(value="What is your level of experience in the gym?", color= "#303437", size=20), 
                tf,
                ElevatedButton("Submit", color = "white", on_click = handle_experience_input),
                
                Text(value = "What muscle group would you like to grow the most?", color = "#303437", size = 20),
                tf2,    
                ElevatedButton("Submit", color = "white", on_click = handle_muscle_group_input)  
         ]))
      ]
    )

