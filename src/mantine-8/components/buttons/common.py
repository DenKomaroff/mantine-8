from .. import SeleneElement, MantineComponent
from selene.support import by
from selene.support.jquery_style_selectors import s


class Buttons(MantineComponent):

    def get_element_by_label(self, text: str) -> None:
        root = 'root'
        label = 'label'
        self.rootElement = s(by.xpath(
            f'//button[contains(@class, "{self.selector(root)}") and '
            f'(.//*[contains(@class, "{self.labelSelector or self.selector(label)}") and '
            f'(text()="{text}")])]'))

    def __init__(self, link: str = None, element: SeleneElement = None, label: str = None, label_selector: str = None) -> None:
        self.labelSelector = label_selector
        if label is not None:
            self.get_element_by_label(label)
        else:
            super().__init__(link=link, element=element)

    def click(self):
        self.rootElement.click()
