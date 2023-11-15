from time import time

class KeyDetect():
    def spell_check(self, sym):
        if self.letter == len(self.text) - 1:
            self.speed = int(60 * len(self.text) / (time() - self.time))
        if self.letter >= len(self.text):
            self.change = True
            return

        def cyrillic_to_sym(sym):
            sym_dict = {"а": "Cyrillic_a", "б": "Cyrillic_be", "в": "Cyrillic_ve",
                        "г": "Cyrillic_ghe", "д": "Cyrillic_de", "е": "Cyrillic_ie",
                        "ё": "Cyrillic_io", "ж": "Cyrillic_zhe", "з": "Cyrillic_ze",
                        "и": "Cyrillic_i", "й": "Cyrillic_shorti", "к": "Cyrillic_ka",
                        "л": "Cyrillic_el", "м": "Cyrillic_em", "н": "Cyrillic_en",
                        "о": "Cyrillic_o", "п": "Cyrillic_pe", "р": "Cyrillic_er",
                        "с": "Cyrillic_es", "т": "Cyrillic_te", "у": "Cyrillic_u",
                        "ф": "Cyrillic_ef", "х": "Cyrillic_ha", "ц": "Cyrillic_tse",
                        "ч": "Cyrillic_che", "ш": "Cyrillic_sha", "щ": "Cyrillic_shcha",
                        "ъ": "Cyrillic_hardsign", "ы": "Cyrillic_yeru", "ь": "Cyrillic_softsign",
                        "э": "Cyrillic_e", "ю": "Cyrillic_yu", "я": "Cyrillic_ya"}
            try:
                return sym_dict[sym]
            except KeyError:
                return "0"

        self.click_count += 1
        if (self.text[self.letter] == sym or cyrillic_to_sym(self.text[self.letter]) == sym or (self.text[self.letter] == " " and sym == "space")):
            self.color[self.letter] = "#dcedc2"
            if self.letter == 0:
                self.time = time()
            self.letter += 1
            if self.letter < len(self.text):
                self.color[self.letter] = "#ccc"
        else:
            self.errors += 1
            self.color[self.letter] = "#ff8c94"
        self.change = False

    def key_detect(self, event):
        self.spell_check(event.keysym)

    def __init__(self, root, text):
        self.root = root
        self.text = text
        self.letter = 0
        self.change = False
        self.root.bind("<KeyPress>", self.key_detect)
        self.color = ["#999" for i in range(len(self.text))]
        self.color[0] = "#ccc"
        self.time = 0
        self.speed = 0
        self.error_per = 0
        self.errors = 0
        self.error_count = 0
        self.click_count = 0
        self.total_click_count = 0

    def update_text(self, text):
        self.text = text
        self.color = ["#999" for i in range(len(self.text))]
        self.color[0] = "#ccc"
        self.letter = 0
        self.errors = 0
        self.click_count = 0
        self.change = False
