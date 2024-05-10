class BaseNote():
    def __init__(self, note_dict = None): 
    # initialize a basenote instance with attributes from a dictionary if provided
        if note_dict is not None:

            # define note attributes from the dictionary
            self.title = note_dict['title']
            self.text = note_dict['text']
            self.link = note_dict['link']
            self.tags = note_dict['tags']
            self.meta = note_dict['meta']
            self.note_id = note_dict["note_id"]
            self.author = note_dict["author"]
        else:
            # Define default values for note attributes when dictionary is not provided
            self.title = "title"
            self.text = ""
            self.link = ""
            self.tags = ""
            self.meta = ""
            self.note_id = 0
            self.author = ""

    def to_dictionary(self):
        # Convert the BaseNote instance to a dictionary representation
        dict = {"note_id":self.note_id,"title":self.title,"text":self.text,"link":self.link,"tags":self.tags,"meta":self.meta, "author":self.author}
        return dict  # Return the dictionary representation of the note

class Note(BaseNote):
    def __init__(self, note_dict = None): 
    # Initialize a Note instance by calling the parent class (BaseNote) constructor
        super().__init__(note_dict)
        if note_dict is not None:
        # Define the snippet attribute from the dictionary
            self.snippet = note_dict['snippet']
        else:
         # Define a default value for the snippet attribute when dictionary is not provided
            self.snippet = ""

    def to_dictionary(self):
        # Convert the Note instance to a dictionary representation
        dict = super().to_dictionary() # Get the base dictionary from the parent class
        dict["snippet"] = self.snippet # Add the snippet attribute to the dictionary
        return dict # Return the dictionary representation of the note






    


