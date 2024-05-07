class Note():
    def __init__(self, note_dict = None): 
        if note_dict is not None:

            # define note attributes
            self.title = note_dict['title']
            self.text = note_dict['text']
            self.link = note_dict['link']
            self.tags = note_dict['tags']
            self.meta = note_dict['meta']
        else:
            self.title = "title"
            self.text = ""
            self.link = ""
            self.tags = ""
            self.meta = ""

    def to_dictionary(self):
        dict = {"title":self.title,"text":self.text,"link":self.link,"tags":self.tags,"meta":self.meta}
        return dict

class Snippet():
    def __init__(self, note_dict = None): 
        if note_dict is not None:

            # define note attributes
            self.title = note_dict['title']
            self.snippet = note_dict['snippet']
            self.meta = note_dict['meta']
            self.language = note_dict["language"]
        else:
            self.title = "title"
            self.snippet = ""
            self.meta = ""
            self.language = "python"
    def to_dictionary(self):
        dict = {"title":self.title,"snippet":self.snippet,"meta":self.meta,"language":self.language}
        return dict


