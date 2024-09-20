from hugchat import hugchat
from hugchat.login import Login
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

class HugChat:
  def __init__(self):
    self.cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
    self.sign = Login(EMAIL, PASSWORD)
    self.cookies = self.sign.login(cookie_dir_path=self.cookie_path_dir, save_cookies=True)
    self.chatbot = hugchat.ChatBot(cookies=self.cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

  def chat(self, query):
    result = self.chatbot.chat(query)
    return result