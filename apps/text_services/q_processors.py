from abc import ABC, abstractmethod

from . import cyrillic_latin_translator


class QProcessorBase(ABC):
    """
    Base class for all processors.
    create instance of processor and call `process` method to process text.
    """

    @abstractmethod
    def process(self, text: str) -> str:
        raise NotImplementedError


class QLatinCyrillicProcessor(QProcessorBase):
    """
    Convert `text` to latin or cyrillic characters depending on which characters are used in `text`.
    """

    def __init__(self, to):
        self.to = to

    def process(self, text: str) -> str:
        return cyrillic_latin_translator.transliterate(text, self.to)
