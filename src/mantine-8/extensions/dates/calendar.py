from .. import SeleneElement, MantineComponent
from selene.support import by
from ...components import MantineUnstyledButton



class Calendar(MantineComponent):

    error_msg = 'Can not set date: {date}'


    class CalendarHeader:

        def __init__(self, owner: SeleneElement):
            self.previous_btn = MantineUnstyledButton(
                element=owner.ss(by.xpath(
                    f'''//*[contains(@class, "{MantineComponent().selector('calendarHeaderControl', name='Calendar')}")]'''))[0])
            self.next_btn = MantineUnstyledButton(
                element=owner.ss(by.xpath(
                    f'''//*[contains(@class, "{MantineComponent().selector('calendarHeaderControl', name='Calendar')}")]'''))[1])
            self.level_up_btn = MantineUnstyledButton(
                element=owner.s(by.xpath(
                    f'''//*[contains(@class, "{MantineComponent().selector('calendarHeaderLevel', name='Calendar')}")]''')))

        @property
        def text(self):
            return self.level_up_btn.rootElement.text

        def previous(self):
            self.previous_btn.click()

        def next(self):
            self.next_btn.click()

        def level_up(self):
            self.level_up_btn.click()


    class CalendarMonth:
        pass


    class CalendarMonthsList:
        pass


    class CalendarYearsList:
        pass


    def _init__(self, link: str = '', element: SeleneElement = None) -> None:
        self._name = 'Calendar'
        super().__init__(link=link, element=element)
        self.header = self.CalendarHeader(owner=self.rootElement.s(by.xpath(f'''//*[contains(@class, "{self.selector('calendarHeader')}"''')))


    def set_date(self, date):

        # переводим календарь в режим выбора года
        self.header.level_up()

        # # btn_level = self.rootElement.s('.mantine-CalendarHeader-calendarHeaderLevel')
        # btn_level = self.rootElement.s(by.xpath(f'.//button[contains(@class, "{self.HeaderLevelClass}")]'))
        # btn_level.click()
        # btn_previous = self.rootElement.ss(by.xpath(f'.//button[contains(@class, "{self.HeaderControlClass}")]'))[0]
        # btn_next = self.rootElement.ss(by.xpath(f'.//button[contains(@class, "{self.HeaderControlClass}")]'))[1]



        if date.year != int(self.header.text):
            if date.year < int(self.header.text):
                while date.year != int(self.header.text):
                    if not self.header.previous_btn.rootElement.get_attribute('disabled'):
                        self.header.previous_btn.click()
                    else:
                        raise Exception(self.error_msg.format(date=date.strftime("%d.%m.%Y")))
        #     if date.year > int(self.header.text):
        #         while date.year != int(self.header.text):
        #             if not btn_next.get_attribute('disabled'):
        #                 btn_next.click()
        #             else:
        #                 raise Exception(except_message)

        # # btn_month = self.rootElement.ss('.mantine-PickerControl-pickerControl')[date.month - 1]
        # btn_month = self.rootElement.ss(by.xpath(f'.//button[contains(@class, "{self.MonthsControlClass}")]'))[date.month - 1]


        # if not btn_month.get_attribute('disabled'):
        #     btn_month.click()
        # else:
        #     raise Exception(except_message)
        # # btn_days = self.rootElement.ss('.mantine-Day-day')
        # btn_days = self.rootElement.ss(by.xpath(f'.//button[contains(@class, "{self.DaysControlClass}")]'))
        # # 'mantine-DatePickerInput-day'
        # i = 0
        # while i < 35 and btn_days[i].text != '1':
        #     i += 1
        #
        # btn_day = btn_days[date.day + i - 1]
        # if not btn_day.get_attribute('disabled'):
        #     btn_day.click()
        # else:
        #     raise Exception(except_message)
