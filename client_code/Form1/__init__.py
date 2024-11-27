from ._anvil_designer import Form1Template
from anvil import *
from PopupForm import PopupForm

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    popup = PopupForm()
    result = alert(popup, title="My Pop-Up", large=True)
    if result:
      print(popup.text_box_1.text)
    pass

  def outlined_button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass
