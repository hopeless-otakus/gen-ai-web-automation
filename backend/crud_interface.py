import argparse
import os
from datetime import datetime

TAG_MAPPING = {
    "news": ["title", "date", "publisher", "draft", "description"],
    "event": ["title", "date", "venue", "image", "link", "draft"],
    "education": ["title", "date", "image", "link", "draft"],
    "collaborators": ["title", "subtitle", "filter", "date", "image", "draft", "description"],
    "careers": ["title", "image", "link", "draft", "weight"]
}

def create_markdown_file(tag, field_values):
    os.makedirs(f"content/{tag}", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"content/{tag}/{timestamp}.md"
    
    content = f"# {tag.capitalize()}\n\n"
    for field, value in field_values.items():
        content += f"## {field.capitalize()}\n{value}\n\n"
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Created markdown file: {filename}")

def main():
    parser = argparse.ArgumentParser(description='Create markdown file for specific tag')
    parser.add_argument('tag', choices=TAG_MAPPING.keys(), help='Tag name for the content')
    
    args = parser.parse_args()
    field_values = {field: input(f"Enter {field}: ") for field in TAG_MAPPING[args.tag]}
    create_markdown_file(args.tag, field_values)

if __name__ == "__main__":
    main()