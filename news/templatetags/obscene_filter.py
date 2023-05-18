import os
import re

class ObscenceFilter:
    def __init__(self):
        # Список цензурируемых слов
        self._censor_list = []

        # Каким символом замемняем
        self._censor_char = "*"

        # Где найти список цензурируемых слов
        self._BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        self._words_file = os.path.join(self._BASE_DIR, 'wordlist.txt')

    def _load_words(self):
        # Получение списка цензурируемых слов
        with open(self._words_file, 'r', encoding='utf-8') as f:
            self._censor_list = [line.strip() for line in f.readlines()]
            profane_words = [w for w in self._censor_list]
            return profane_words  

    def censor(self, input_text):
        # Возвращает input_text с замененными обсценными словами, заменёнными '*'
        bad_words = self._load_words()
        res = input_text

        for word in bad_words:
            word = r'\b%s\b' % word  
            regex = re.compile(word, re.IGNORECASE)
            res = regex.sub(self._censor_char * (len(word) - 4), res)

        return res