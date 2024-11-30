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

    def get_category_intent(self, category):
        return MAPPING[category]["intents"]

    def get_category_help_intent(self, category):
        return MAPPING[category]["help_intent"]

    def get_category_fields(self, category):
        fields = MAPPING[category]["fields"]
        field_names = [field["name"] for field in fields]
        return field_names

    def get_field_specs(self, category, field_name):
        category_map = MAPPING[category]
        field = [
            field for field in category_map["fields"] if field["name"] == field_name
        ]
        return field[0]["specs"]

    def get_field_extract(self, category, field_name):
        field = [
            field
            for field in MAPPING[category]["fields"]
            if field["name"] == field_name
        ]
        return field[0]["extract"]

    def get_category_path(self, category):
        return MAPPING[category]["path"]

    def is_field_required(self, category, field_name):
        field = [
            field
            for field in MAPPING[category]["fields"]
            if field["name"] == field_name
        ]
        return field[0]["specs"]["required"]

    def is_field_generatable(self, category, field_name):
        field = [
            field
            for field in MAPPING[category]["fields"]
            if field["name"] == field_name
        ]
        return field[0]["specs"]["generate"]
