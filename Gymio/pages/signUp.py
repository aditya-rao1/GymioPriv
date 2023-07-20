from flet import * 

email = TextField(label = "Email", color = "#303437", border_color = "black", width = 450, cursor_color = "white")
userName = TextField(label = "Username", color = "#303437", border_color="black", width = 450, cursor_color="white")
password = TextField(label = "Password", color = "#303437", border_color = "black", width = 450, cursor_color="white", password = True)
passwordCon = TextField(label = "Confirm Password", color = "#303437", border_color = "black", width = 450, cursor_color="white", password = True)


#Main page to register and log people in.
class signUp(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page


  def build(self):
    return Column(
      controls=[
        Container(
          height=800,width=1600, padding = 30,
          bgcolor='white',
          content=Column(
            controls=[
              Text('Sign Up:', color = "black", size = 30), email, userName, password, passwordCon,
              Row(controls = [ElevatedButton(
                on_click= lambda _: self.page.go('/'), 
                content=Text('Submit', color='white')
              )])
            ]
          )
          )
        ]
    )
    