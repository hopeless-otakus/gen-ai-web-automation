import os

MAPPING = {
    "news": {
        "path": "cerai-hugo/content/english/news",
        "fields": [
            "title",
            "date",
            "publisher",
            "draft",
            "image",
            "link",
            "description",
        ],
    },
    "event": {
        "path": "cerai-hugo/content/english/events",
        "fields": ["title", "date", "venue", "image", "link", "draft"],
    },
    "education": {
        "path": "cerai-hugo/content/english/education",
        "fields": ["title", "date", "image", "link", "draft"],
    },
    "collaborators": {
        "path": "cerai-hugo/content/english/collaborators",
        "fields": [
            "title",
            "subtitle",
            "filter",
            "date",
            "image",
            "draft",
            "description",
        ],
    },
    "careers": {
        "path": "cerai-hugo/content/english/careers",
        "fields": [
            "title",
            "image",
            "link",
            "draft",
            "weight",
        ],
    },
    "announcements": {
        "path": "cerai-hugo/content/english/announcements",
        "fields": [
            "title",
            "date",
            "venue",
            "image",
            "link",
            "draft",
        ],
    },
    "advisory": {
        "path": "cerai-hugo/content/english/advisory",
        "fields": [
            "title",
            "subtitle",
            "subsubtitle",
            "date",
            "image",
            "draft",
            "link",
            "weight",
            "caption",
        ],
    },
    "activities": {
        "path": "cerai-hugo/content/english/activities",
        "fields": [
            "image",
            "title",
            "label",
            "link",
            "weight",
            "description",
        ],
    },
}


class Mapping:
    def __init__(self):
        pass

    def get_categories(self):
        return [key for key in MAPPING.keys()]

    def get_category_fields(self, category):
        fields = MAPPING[category]["fields"]
        return fields

    def get_category_path(self, category):
        return MAPPING[category]["path"]

    def get_unique_fields(self):
        unique_fields = set()
        for category in MAPPING:
            for field in MAPPING[category]["fields"]:
                unique_fields.add(field)
        return unique_fields
        
