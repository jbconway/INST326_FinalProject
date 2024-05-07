class BaseNote():
    def __init__(self, note_dict = None): 
        if note_dict is not None:

            # define note attributes
            self.title = note_dict['title']
            self.text = note_dict['text']
            self.link = note_dict['link']
            self.tags = note_dict['tags']
            self.meta = note_dict['meta']
            self.note_id = note_dict["note_id"]
            self.author = note_dict["author"]
        else:
            self.title = "title"
            self.text = ""
            self.link = ""
            self.tags = ""
            self.meta = ""
            self.note_id = 0
            self.author = ""

    def to_dictionary(self):
        dict = {"note_id":self.note_id,"title":self.title,"text":self.text,"link":self.link,"tags":self.tags,"meta":self.meta, "author":self.author}
        return dict

class Note(BaseNote):
    def __init__(self, note_dict = None): 
        super().__init__(note_dict)
        if note_dict is not None:
            self.snippet = note_dict['snippet']
        else:
            self.snippet = ""

    def to_dictionary(self):
        dict = super().to_dictionary()
        dict["snippet"] = self.snippet
        return dict


