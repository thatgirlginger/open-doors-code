class Keywords:
    def __init__(self):
        self.notes = ["note", "Note", "notes", "Notes", "A/n", "a/n", "A/N", "disclaimer", "Disclaimer", "DISCLAIMER"]
        self.warnings = ["warning", "Warning", "warnings", "Warnings", "cw", "CW", "content warning", "Content Warning", "trigger warning", 
                    "Trigger Warning", "Content warning", "Trigger warning", "tw", "TW"]
        self.summary = ["summary", "Summary", "summaries", "Summaries", "prompt", "Prompt"]
        self.commercial = ["Patreon", "patreon", "mailto", "Ko-fi", "ko-fi", "Ko-Fi", "gofundme", "GoFundMe"]
        # self.ratings
        # self.wordcount
        # self.pairings
        # self.characters
        # others defined
    def detect(self, type, text):
        match type:
            case "notes":
                keywords = self.notes
            case "warnings":
                keywords = self.warnings
            case "summary":
                keywords = self.summary
            case "commercial":
                keywords = self.commercial
            case _:
                raise NameError(
                    "unsupported type: must be 'notes', 'warnings', 'summary', or 'commercial'; check config file"
                )
        for k in keywords:
            if k in text:
                return True
        return False
