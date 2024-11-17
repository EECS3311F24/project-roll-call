from .generator import Generator
import random

# this class extends Generator
class QuoteGen(Generator):

    # constructor
    def __init__(self):
        super().__init__()
    
    # this function returns a gemini-generated word and definition
    def get_quote(self):
        rand = random.randrange(1,26)
        char = chr(96 + rand)

        rand = random.randrange(1,26)
        char_two = chr(96 + rand)

        response = self.model.generate_content(
            f"""Give me a random quote that really speaks to the soul. Let it start with the letter {char}, and include the letter {char_two}. 
            Make it this format: '"quote" - person'"""
        )

        return (response.text)
