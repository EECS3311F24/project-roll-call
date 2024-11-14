from .generator import Generator

# this class extends Generator
class WordGen(Generator):
    
    # constructor
    def __init__(self):
        super().__init__()
    
    # this function returns a gemini-generated word and definition
    def get_word(self):
        response = self.model.generate_content(
            """Give me a COMPLETELY random non-explicit word and definition. Make the format exactly like this: '(insert word): (insert definition)', 
            all plain text, no bolds. Capitalize the first letter of the word and definition. Keep the definition short and succint.
            Do not use words you have used recently."""
        )
        return(response.text)
