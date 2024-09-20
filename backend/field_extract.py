from hugchat import hugchat
from hugchat.login import Login

EMAIL = "r.rahul.developer@gmail.com"
PASSWD = "Zumbido123@toss"
cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# message_result = chatbot.chat("Hi!")

query = "Can you create a post with the title 'Test Post asdkfhgasdf'?"
extract_query = "What is the title of the query?"
instructions = "Just provide the title."

final_query = "Query:" + query + "\n\n " + "Extract Query: " + extract_query + "\n\n " + instructions
result = chatbot.chat(final_query)
print(result)