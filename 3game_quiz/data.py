# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# https://opentdb.com/api_config.php

import requests

class Data:
    def __init__(self,url):
        self.url = url or ""
        self.question_data = []


    def crawl_opentdb(self):
        try:
            response = requests.get(url=self.url)
            response.raise_for_status()

            data = response.json()
            if data["response_code"] == 0:
                # print(type(data["results"])) --> <class 'list'>
                list_data = data["results"]
                for item in list_data:
                    item_line = {}
                    item_line["text"] = item["question"]
                    item_line["answer"] = item["correct_answer"]
                    self.question_data.append(item_line)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
        return self.question_data


# _data = Data(url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
# question_data = _data.crawl_opentdb()
# print(question_data)