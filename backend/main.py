from content_manager import ContentManager

manager = ContentManager()

data = {
    'title': 'Test',
    'date': '2021-08-19',
    'time': '12:00:00',
    'image': 'test.jpg',
    'tags': ['test'],
    'publisher': 'test',
    'link': 'test',
    'draft': False,
    'description': 'test'
}

result = manager.create_article('news', 'test', data)
print(result)