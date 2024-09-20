import os

MAPPING = {
    "news": {
        "intents": ["Can you add a news?", "Can you add a news with title"],
        "help_intent": ["Can you help me add a news?", "Can you help me add a news with title"],
        "path": "cerai-hugo/content/english/news",
        "fields": [
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "date",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the date of the query?"],
            },
            {
                "name": "publisher",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the publisher of the query?"],
            },
            {
                "name": "draft",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["Is the query ask to make a draft?"],
            },
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "link",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["What is the url link to any article that query defines?"],
            },
            {
                "name": "description",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the description of the query?"],
            },
        ],
    },
    "event": {
        "intents": ["Can you add an event?", "Can you add an event with title"],
        "help_intent": ["Can you help me add an event?", "Can you help me add an event with title"],
        "path": "cerai-hugo/content/english/events",
        "fields": [
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "date",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the date of the query?"],
            },
            {
                "name": "venue",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the venue of the query?"],
            },
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "link",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the url link to any article that query defines?"],
            },
            {
                "name": "draft",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["Is the query ask to make a draft?"],
            },
        ],
    },
    "education": {
        "intents": ["Can you add an education?", "Can you add an education with title"],
        "help_intent": ["Can you help me add an education?", "Can you help me add an education with title"],
        "path": "cerai-hugo/content/english/education",
        "fields": [
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "date",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the date of the query?"],
            },
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "link",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the url link to any article that query defines?"],
            },
            {
                "name": "draft",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["Is the query ask to make a draft?"],
            },
        ],
    },
    "collaborators": {
        "intents": ["Can you add a collaborator?", "Can you add a collaborator with title"],
        "help_intent": ["Can you help me add a collaborator?", "Can you help me add a collaborator with title"],
        "path": "cerai-hugo/content/english/collaborators",
        "fields": [
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "subtitle",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the subtitle of the query?"],
            },
            {
                "name": "filter",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the filter of the query?"],
            },
            {
                "name": "date",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the date of the query?"],
            },
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "draft",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["Is the query ask to make a draft?"],
            },
            {
                "name": "description",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the description of the query?"],
            },
        ],
    },
    "careers": {
        "intents": ["Can you add a career?", "Can you add a career with title"],
        "help_intent": ["Can you help me add a career?", "Can you help me add a career with title"],
        "path": "cerai-hugo/content/english/careers",
        "fields": [
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "link",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the url link to any article that query defines?"],
            },
            {
                "name": "draft",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["Is the query ask to make a draft?"],
            },
            {
                "name": "weight",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the weight of the query?"],
            },
        ],
    },
    "announcements": {
        "intents": ["Can you add an announcement?", "Can you add an announcement with title"],
        "help_intent": ["Can you help me add an announcement?", "Can you help me add an announcement with title"],
        "path": "cerai-hugo/content/english/announcements",
        "fields": [
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "date",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the date of the query?"],
            },
            {
                "name": "venue",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the venue of the query?"],
            },
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "link",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the url link to any article that query defines?"],
            },
            {
                "name": "draft",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["Is the query ask to make a draft?"],
            },
        ],
    },
    "advisory": {
        "intents": ["Can you add an advisory?", "Can you add an advisory with title"],
        "help_intent": ["Can you help me add an advisory?", "Can you help me add an advisory with title"],
        "path": "cerai-hugo/content/english/advisory",
        "fields": [
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "subtitle",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the subtitle of the query?"],
            },
            {
                "name": "subsubtitle",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the subsubtitle of the query?"],
            },
            {
                "name": "date",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the date of the query?"],
            },
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "draft",
                "specs": {
                    "required": True,
                    "generate": False,
                },
                "extract": ["Is the query ask to make a draft?"],
            },
            {
                "name": "link",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the url link to any article that query defines?"],
            },
            {
                "name": "weight",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the weight of the query?"],
            },
            {
                "name": "caption",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the caption of the query?"],
            },
        ],
    },
    "activities": {
        "intents": ["Can you add an activity?", "Can you add an activity with title"],
        "help_intent": ["Can you help me add an activity?", "Can you help me add an activity with title"],
        "path": "cerai-hugo/content/english/activities",
        "fields": [
            {
                "name": "image",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the image url defined in query?"],
            },
            {
                "name": "title",
                "specs": {
                    "required": False,
                    "generate": True,
                },
                "extract": ["What is the title of the query?"],
            },
            {
                "name": "label",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the label of the query?"],
            },
            {
                "name": "link",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the url link to any article that query defines?"],
            },
            {
                "name": "weight",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the weight of the query?"],
            },
            {
                "name": "description",
                "specs": {
                    "required": False,
                    "generate": False,
                },
                "extract": ["What is the description of the query?"],
            },
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
        field = [field for field in category_map["fields"] if field["name"] == field_name]
        return field[0]["specs"]
    
    def get_field_extract(self, category, field_name):
        field = [field for field in MAPPING[category]["fields"] if field["name"] == field_name]
        return field[0]["extract"]
    
    def get_category_path(self, category):
        return MAPPING[category]["path"]
    
    def is_field_required(self, category, field_name):
        field = [field for field in MAPPING[category]["fields"] if field["name"] == field_name]
        return field[0]["specs"]["required"]
    
    def is_field_generatable(self, category, field_name):
        field = [field for field in MAPPING[category]["fields"] if field["name"] == field_name]
        return field[0]["specs"]["generate"]