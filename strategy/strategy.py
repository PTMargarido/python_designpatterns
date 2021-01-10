from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):

    def start(self, items: list):
        pass

    def end(self, items: list):
        pass

    @abstractmethod
    def content(self, items: list, content: str):
        pass


class HtmlTextProcess(Strategy):

    def start(self, items: list):
        items.append("<ul>")

    def end(self, items: list):
        items.append("</ul>")

    def content(self, items: list, content: str):
        items.append("  <il>" + content + "</il>")


class MarkdownTextProcess(Strategy):

    def content(self, items: list, content: str):
        items.append("*" + content)


class TextProcess:

    def __init__(self, strat: Strategy):
        self._strat = strat
        # type: List[str]
        self._output = []

    def set_strategy(self, strat: Strategy):
        self._output = []
        self._strat = strat

    def execute_strategy(self, items: list):
        self._strat.start(self._output)
        for item in items:
            self._strat.content(self._output, item)
        self._strat.end(self._output)

    def get_output(self):
        return self._output


if __name__ == "__main__":

    tp = TextProcess(HtmlTextProcess())
    tp.execute_strategy(["foo", "bar", "baz"])
    print(tp.get_output())

    tp.set_strategy(MarkdownTextProcess())
    tp.execute_strategy(["foo", "bar", "baz"])
    print(tp.get_output())
