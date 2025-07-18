from .. import SeleneElement
from .common import Buttons


class Button(Buttons):

    def __init__(self, link: str = '', element: SeleneElement = None, label: str = None, label_selector: str = None) -> None:
        self._name = 'Button'
        super().__init__(link=link, element=element, label=label, label_selector=label_selector)
