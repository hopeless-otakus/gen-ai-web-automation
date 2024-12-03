from mapping import Mapping

class ContentManager:

  def __init__(self):
    self.mapping = Mapping()

  def create_article(self, category, file_name, data):
    fields = self.mapping.get_category_fields(category)
    category_path = self.mapping.get_category_path(category) + "/" + file_name + ".md"
    for field in fields:
      if field not in data:
        return False
    content = "---\n"
    for field in fields:
      if field == "description":
        continue
      content += f"{field}: {data[field]}\n"
    content += "---\n"
    if "description" in data:
      content += data["description"]
    with open(category_path, 'a') as file:
      file.write(content)
    return True

  # def check_article(self, category, file_name):
      
    

