import os

def getPath(field):
  BASE_PATH = os.path.join('crai-hugo', 'content', 'english')
  if field == 'news':
    return os.path.join(BASE_PATH, 'news')

  return False


class ContentManager():
  def __init__ (self, field, data):
    self.field = field
    self.data = data
    self.BASE_PATH = getPath(field)

  def generate_md_content(self):
    title = self.data.get('title', '')
    date = self.data.get('date', '')
    time = self.data.get('time', '')
    image = self.data.get('image', '')
    tags = self.data.get('tags', [])
    publisher = self.data.get('publisher', '')
    link = self.data.get('link', '')

    md_content = f"""---
      title: "{title}"
      date: {date}
      time: {time}
      image: "{image}"
      tags: {tags}
      publisher: "{publisher}"
      link: "{link}"
      draft: false
      ---
      """
    return md_content
  
  def create_md_file(self):
    title = self.data.get('title')
    if not title:
      title = "test"
    
    filename = f"{title.replace(' ', '-').lower()}.md"
    file_path = os.path.join(self.BASE_PATH, filename)
    content = self.generate_md_content()

    with open(file_path, 'w', encoding='utf-8') as file:
      file.write(content)

    return file_path
