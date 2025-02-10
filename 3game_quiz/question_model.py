import requests

class Question:
    def __init__(self,text, answer):
        self.question_text = text or ""
        self.question_answer = answer or ""


