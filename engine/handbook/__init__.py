from engine.handbook._lexer import HandbookLexer
from engine.handbook._parser import HandbookParser

class HandbookLang():

    def __init__(self):
        self.lexer = HandbookLexer()
        self.parser = HandbookParser()
    
    def execute(self, text):
        token_list = self.lexer.lex_raw_string(text)
        self.parser.parse_token_list(token_list)
