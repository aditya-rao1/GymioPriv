from flet import * 

userName = TextField(label = "Username", color = "#303437", border_color="black", width = 450, cursor_color="white")
password = TextField(label = "Password", color = "#303437", border_color = "black", width = 450, cursor_color="white", password = True)

#Main page to register and log people in.
class Login(UserControl):
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
              Text('Login:', color = "black", size = 30), userName, password,
              Row(controls = [ElevatedButton(
                on_click= lambda _: self.page.go('/'), 
                content=Text('Submit', color='white')
              ), TextButton(on_click= lambda _: self.page.go('/signup'), content = Text("Sign up?"))])
            ]
          )
          )
        ]
    )
    