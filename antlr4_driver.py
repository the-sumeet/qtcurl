import sys
from typing import Dict

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.FileStream import FileStream

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import ErrorNodeImpl

from parser.CurlLexer import CurlLexer
from parser.CurlListener import CurlListener
from parser.CurlParser import CurlParser


class Listener(CurlListener):
    result: Dict

    def __init__(self, result: Dict):
        self.result = result
        super().__init__()

    def enterUri(self, ctx: CurlParser.UriContext):
        self.result['uri'] = str(ctx.getText())

    def enterMethod(self, ctx: CurlParser.MethodContext):

        if isinstance(ctx.METHOD(), ErrorNodeImpl):
            return

        self.result['method'] = str(ctx.METHOD())

    def enterHeader(self, ctx: CurlParser.HeaderContext):
        if len(ctx.children) != 6:
            return
        self.result['headers'] = [
            *self.result.get('headers', []),
            {
                str(ctx.headerName().getText()): str(ctx.headerValue().getText())
            }
        ]

class ThrowingErrorListener(ErrorListener):
  def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    raise ValueError(f"Line {line}:{column}: {msg}")

def parse_curl(curl_content: str):
    input_stream = InputStream(curl_content)
    lexer = CurlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CurlParser(stream)
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.curl()

    result = dict()
    listener = Listener(result)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(result)


parse_curl('curl -X GET -H "A : B -H "F:G" http://example.com?a=b&c=d')
