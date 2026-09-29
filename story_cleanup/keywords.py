class Keywords:
    def __init__(self):
        self.notes = [
            "note",
            "Note",
            "notes",
            "Notes",
            "A/n",
            "a/n",
            "A/N",
            "disclaimer",
            "Disclaimer",
            "DISCLAIMER",
            "disclamer",
            "copyright",
            "Disclamer",
        ]
        self.warnings = [
            "warnings",
            "Warnings",
            "WARNING",
            "Warning",
            "cw ",
            "CW ",
            "content warning",
            "Content Warning",
            "trigger warning",
            "Trigger Warning",
            "Content warning",
            "Trigger warning",
            "tw ",
            "TW ",
            "tw:",
            "TW:",
            "tw-",
            "TW-",
            "cw:",
            "CW:",
            "cw-",
            "CW-",
        ]
        self.summary = [
            "summary",
            "Summary",
            "summaries",
            "Summaries",
            "prompt ",
            "Prompt ",
            "summery",
            "Summery",
        ]
        self.commercial = [
            "Patreon",
            "patreon",
            "mailto",
            "Ko-fi",
            "ko-fi",
            "Ko-Fi",
            "gofundme",
            "GoFundMe",
        ]
        self.ratings = ["rating", "Rating", "rated", "Rated"]
        self.wordcount = [
            "words:",
            "words-",
            "wordcount",
            "Wordcount",
            "Words:",
            "Words-",
            "word count",
            "Word count",
            "Word Count",
        ]
        self.pairings = ["pairing", "Pairing", "relationship", "Relationship"]

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
            case "rating":
                keywords = self.ratings
            case "wordcount":
                keywords = self.wordcount
            case "pairings":
                keywords = self.pairings
            case _:
                raise NameError(
                    "unsupported type: must be 'notes', 'warnings', 'summary', 'rating', 'pairings', 'wordcount', or 'commercial'; check config file"
                )
        for k in keywords:
            if k in text:
                return True
        return False
