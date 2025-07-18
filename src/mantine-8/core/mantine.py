# https://mantine.dev/

from selene.elements import SeleneElement
from selene.support import by
from selene.support.jquery_style_selectors import s

class MantineComponent:

    @property
    def name(self) -> str:
        return self._name

    @property
    def link_attribute(self) -> str:
        return self._link_attribute

    @property
    def link_value(self) -> str:
        return self._link_value

    def selector(self, level, name=None):
        if name is not None:
            name = self.name
        return f'mantine-{name}-{level.lower()}'

    def get_element_by_link(self, value: str, start: SeleneElement = None, root = 'root') -> None:

        self.linkElement = s(by.xpath(
            f'(//*[@{self.link_attribute}="{value}"])'))

        if start is None:
            self.rootElement = s(by.xpath(
                f'//*[contains(@class, "{self.selector(root)}") '
                f'and (.//*[@{self.link_attribute}="{value}"] '
                f'or @{self.link_attribute}="{value}")]'))
        else:
            self.rootElement = start.s(by.xpath(
                f'//*[contains(@class, "{self.selector(root)}") '
                f'and (.//*[@{self.link_attribute}="{value}"] '
                f'or @{self.link_attribute}="{value}")]'))

    def get_element_by_placeholder(self):
        pass

    # def __init__(self, link: str = None, start: SeleneElement = None, element: SeleneElement = None, root = 'root') -> None:
    def __init__(self, **kwargs) -> None:
        if self.name is None:
            self._name = 'Component'
        self._link_attribute: str = kwargs.get('link_attribute') or 'data-test-id'
        self._link_value = kwargs.get('link_attribute')
        self._element = kwargs.get('element')
        if self._link_value is not None:
            self.get_element_by_link(value=self._link_value, start=kwargs.get('start'), root=kwargs.get('root'))
        elif self._element is not None:
            self.rootElement = self._element
            self.linkElement = self._element
        else:
            raise ValueError('You should pass a link or an element')

    def click(self):
        self.rootElement.click()


class SimpleElement:

    linkAttribute: str = 'data-test-id'

    def __init__(self, link: str = None) -> None:
        if link is not None:
            self.linkElement = s(by.xpath(f'(//*[@{self.linkAttribute}="{link}"])'))
        else:
            raise ValueError('You should pass a link')

    def click(self):
        self.linkElement.click()


