from .generator import Generator
import random

# this class extends Generator
class WordGen(Generator):

    # constructor
    def __init__(self):
        super().__init__()
    
    # this function returns a gemini-generated word and definition
    def get_word(self):
        rand = random.randrange(1,26)
        char_one = chr(96 + rand)

        rand = random.randrange(1,26)
        char_two = chr(96 + rand)

        rand = random.randrange(1,26)
        char_three = chr(96 + rand)

        response = self.model.generate_content(
            f"""Teach me an interesting new word that includes the characters '{char_one}' and '{char_two}' and '{char_three}', and give its definition. 
            Make the format exactly like this: '(insert word): (insert definition)'. 
            All plain text, no bolds. Capitalize the first letter of the word and definition. 
            Keep the definition short and concise. Do not include names (including names of animals) or proper nouns."""
        )

        word, definition = response.text.split(': ')
    
        return {"word": word, "definition": definition}
