from mapping import Mapping
from pprint import pprint
from hug_chat import HugChat
import textdistance
import time
from tqdm import tqdm
from tabulate import tabulate

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
      return min_category, min_distance
    return None, None
  
  def get_help_intent(self, text):
    MAX_DISTANCE = 1
    MIN_DISTANCE = 0
    PERCENTAGE_THRESHOLD = 0.5

    categories = self.mapping.get_categories()
    category_intent_mapping = []
    for category in categories:
      category_intent_mapping.append((category, self.mapping.get_category_help_intent(category)))
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
      return min_category, min_distance
    return None, None
  
  def get_final_intent(self, text):
    intent, distance = self.get_intent(text)
    help_intent, help_distance = self.get_help_intent(text)
    intent_type = "intent" if distance < help_distance else "help_intent"
    if intent_type == "intent":
      return intent, distance, intent_type
    return help_intent, help_distance, intent_type
    
  def extract_field(self, text, extract_query):
    INSTRUCTION = "Just provide the title and no explanation. If not present, print null"
    query = "Query:" + text + "\n\n " + "Extract Query: " + extract_query + "\n\n " + INSTRUCTION
    result = self.hug_chat.chat(query)
    if result == "null":
      return None
    return str(result)
  
  def parse_query(self, query):
    DELAY = 5
    category, distance, intent_type = self.get_final_intent(query)
    if category is None:
      return None
    if intent_type == "intent":
      field_mapping = []
      for field in tqdm(self.mapping.get_category_fields(category)):
        extract_queries = self.mapping.get_field_extract(category, field)
        extract_query = extract_queries[0]
        value = self.extract_field(query, extract_query)
        field_mapping.append((field, value))
        time.sleep(DELAY)
      field_mapping = dict(field_mapping)
      return category, field_mapping, intent_type
    elif intent_type == "help_intent":
      self.print_help(category)
      return category, None, intent_type
  
  def print_help(self, category):
    fields = self.mapping.get_category_fields(category)
    table_data = []
    for field in fields:
        is_required = self.mapping.is_field_required(category, field)
        is_generatable = self.mapping.is_field_generatable(category, field)
        table_data.append([field, is_required, is_generatable])
    
    headers = ["Field", "Required", "Generatable"]
    print(tabulate(table_data, headers, tablefmt="grid"))


    

# query = "Create a event with title 'Test Event', date '2021-09-01', time '12:00:00', image 'test.jpg', tags ['test'], publisher 'test', link 'test'"
query = "help event"

intent_bot = IntentBot()
result = intent_bot.parse_query(query)
# print(intent_bot.print_help("event"))
print(result)