import os

def getPath(field):
    # Get the absolute path to the directory containing this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to crai-hugo/content/english
    crai_hugo_path = os.path.join(current_dir, '..', 'crai-hugo', 'content', 'english')
    crai_hugo_path = os.path.abspath(crai_hugo_path)
    print(f"crai_hugo_path: {crai_hugo_path}")
    
    if field == 'news':
        news_path = os.path.join(crai_hugo_path, 'news')
        print(f"news_path: {news_path}")
        return news_path

    return False

class ContentManager():
    def __init__(self, field, data):
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