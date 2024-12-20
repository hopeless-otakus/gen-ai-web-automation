from mapping import Mapping
import argparse
import json
from content_manager import ContentManager

map = Mapping()
manager = ContentManager()

fields = map.get_unique_fields()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate a JSON file with the unique fields in the mapping.")
    
    parser.add_argument("category", type=str, help="The category to get unique fields for")
    for field in fields:
        parser.add_argument(f"--{field}", type=str, help=f"Value for {field}")    
    
    args = parser.parse_args()
    category = args.category
    fields = map.get_category_fields(category)
    
    if "draft" in fields:
        fields.remove("draft")

    data = {}
    for field in fields:
        data[field] = getattr(args, field)

    data["draft"] = False
    
    file_name = data["title"].lower().replace(" ", "-")
    manager.create_article(category, file_name, data)
