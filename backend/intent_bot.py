# intents = {
#     "greet": ["hello", "hi", "hey", "howdy", "hola", "greetings", "good morning", "good afternoon", "good evening"],
#     "goodbye": ["goodbye", "bye", "see you", "see you later", "adios", "cya"],
#     "thanks": ["thanks", "thank you", "thx"],
#     "search": ["search", "find", "look up", "search for"],
# }

# def get_intent(text):
#     for intent, keywords in intents.items():
#         for keyword in keywords:
#             if keyword in text:
#                 return intent
#     return None

# question = "i go now"
# intent = get_intent(question)
# print(intent)  

from mapping import Mapping
from pprint import pprint
from hug_chat import HugChat
import textdistance

class IntentBot():

  def __init__(self):
    self.mapping = Mapping()
    self.hug_chat = HugChat()

  def get_intent(self, text):
    MAX_DISTANCE = 1
    MIN_DISTANCE = 0
    PERCENTAGE_THRESHOLD = 0.5

    categories = self.mapping.get_categories()
    category_intent_mapping = []
    for category in categories:
      category_intent_mapping.append((category, self.mapping.get_category_intent(category)))
    category_intent_mapping = dict(category_intent_mapping)
    category_distance_mapping = []
    for category, intents in category_intent_mapping.items():
      average_distance = 0
      for intent in intents:
        distance = textdistance.levenshtein.normalized_distance(text, intent)
        average_distance += distance
      average_distance /= len(intents)
      category_distance_mapping.append((category, average_distance))
    category_distance_mapping = dict(category_distance_mapping)
    min_category = None
    min_distance = None
    for category, distance in category_distance_mapping.items():
      if min_distance is None:
        min_category = category
        min_distance = distance
        continue
      if distance <= min_distance or min_distance is None:
        min_category = category
        min_distance = distance
    distance_percentage = (min_distance - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE)
    if distance_percentage >= PERCENTAGE_THRESHOLD:
      return min_category
    return None
  
  def extract_field(self, text, extract_query):
    INSTRUCTION = "Just provide the title. If not present, print null"
    query = "Query:" + text + "\n\n " + "Extract Query: " + extract_query + "\n\n " + INSTRUCTION
    result = self.hug_chat.chat(query)
    if result == "null":
      return None
    return result


    

query = "Create a post with the title 'Test Post asdkfhgasdf'"
extract_query = "What is the title of the query?"

intent_bot = IntentBot()
result = intent_bot.extract_field(query, extract_query)
print(result)