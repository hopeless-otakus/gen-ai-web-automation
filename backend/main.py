from content_manager import ContentManager
from intent_bot import IntentBot
from pprint import pprint

manager = ContentManager()
bot = IntentBot()

# data = {
#     'title': 'Test',
#     'date': '2021-08-19',
#     'time': '12:00:00',
#     'image': 'test.jpg',
#     'tags': ['test'],
#     'publisher': 'test',
#     'link': 'test',
#     'draft': False,
#     'description': 'test'
# }

# result = manager.create_article('news', 'test', data)
# print(result)

while True:
    query = input("Enter a query: ")
    result = bot.parse_query(query)
    category = result[0]
    data = result[1]
    intent_type = result[2]
    if intent_type == "intent":
        pprint(data)
        confirm = input("Do you want to create the article? (y/n): ")
        if confirm == "y":
            file_name = data['title'].replace(" ", "-").lower()
            result = manager.create_article(category, file_name, data)
            print(result)