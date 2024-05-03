
class ParserHelper:
    """Helper class for parsing inputs and outputs to and from the LLM API."""      
    keyword_store = {
        "his" : "her",
        "he" : "she",
        "him" : "her",
        "mr." : "ms.",
        "mr" : "ms",
        "sir" : "ma'am",
    }

    def __init__(self, keyword_store: None):
        if keyword_store is not None:
            self.keyword_store = keyword_store
    


    def replace_keywords(self, input_string):
        """Replace keywords in the input string with their corresponding values.
        
        Args:
            input_string (str): The input string to be processed.
        """
        input_string = input_string.lower()
        input_string_list = input_string.split()
        for word in input_string_list:
            if word in keyword_store:
                index = input_string_list.index(word)
                input_string_list[index] = keyword_store[word]
        return ' '.join(input_string_list)
    
    def parse_user_input_for_llm(self, user_input):
        """Parse user input for the LLM API.
        
        Args:
            user_input (str): The user input to be parsed.
        """
        return ""
    
    def parse_llm_output_for_user(self, llm_output):
        """Parse LLM output for the user.
        
        Args:
            llm_output (str): The LLM output to be parsed.
        """
        return ""
    
