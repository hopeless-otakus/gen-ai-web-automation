from hug_chat import HugChat
from mapping import Mapping
from rag import extract_context

chatbot = HugChat()
map = Mapping()

event_prompt = "Please create an event titled 'Test Event' on 21/21/21 at the venue 'something'. The event image is 'asd.png' and you can find more details at the link 'something'."

def get_crud_interface_callback(prompt):

    instruction = ""
    categories = map.get_categories()
    for category in categories:
        fields = map.get_category_fields(category)
        instruction += f"For {category} category the required fields are:"
        field_str = "\n".join(["- " + field for field in fields])
        instruction += field_str + "\n"

    context = extract_context(prompt)
    instruction += "CONTEXT: \n" + context + "\n"

    instruction += "Please extract the required fields from the prompt and provide the values for each field. in the following format: python crud_interface.py <category> --<field1> <value1> --<field2> <value2> ... \n\nJust give the code and nothing else without language name."
    final_prompt = "PROMPT: \n" + event_prompt + "\nINSTRUCTION:\n" + instruction

    callback = chatbot.chat(final_prompt)
    return callback

# result = get_crud_interface_callback(event_prompt)
# print(result)