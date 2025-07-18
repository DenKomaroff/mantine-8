from selene.support import by
from selene.support.jquery_style_selectors import s


class SimpleElement:

    linkAttribute: str = 'data-test-id'

    def __init__(self, link: str = None) -> None:
        if link is not None:
            self.linkElement = s(by.xpath(f'(//*[@{self.linkAttribute}="{link}"])'))
        else:
            raise ValueError('You should pass a link')

    def click(self):
        self.linkElement.click()
