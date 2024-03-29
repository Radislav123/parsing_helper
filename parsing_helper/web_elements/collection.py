from typing import Callable, TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait

from parsing_helper.settings import Settings
from parsing_helper.web_elements.element import ExtendedWebElement


if TYPE_CHECKING:
    from parsing_helper.pages.base_page import BasePage


class ExtendedWebElementCollection:
    settings: Settings

    def __init__(self, page: "BasePage", xpath: str) -> None:
        self.page = page
        self.driver = page.driver
        self.settings = page.settings

        self.xpath = xpath
        self.wait = WebDriverWait(self.driver, self.settings.SELENIUM_DEFAULT_TIMEOUT)
        self.elements: None | list[ExtendedWebElement] = None
        self.initialized: dict[Callable, bool] = {}

    def reset(self) -> None:
        """Сбрасывает состояние коллекции к первоначальному."""

        self.initialized = {}

    def __len__(self) -> int:
        self.init_if_necessary()
        return len(self.elements)

    def __getitem__(self, index):
        self.init_if_necessary()
        return self.elements[index]

    def __iter__(self):
        self.init_if_necessary()
        for element in self.elements:
            yield element

    def init_if_necessary(self, wait_condition: Callable = presence_of_all_elements_located) -> None:
        if wait_condition not in self.initialized or not self.initialized[wait_condition]:
            self.init(wait_condition)

    def init(self, wait_condition: Callable = presence_of_all_elements_located) -> None:
        """Находит элементы коллекции в DOM-структуре страницы."""

        elements_amount = len(self.wait.until(wait_condition((By.XPATH, self.xpath))))
        self.elements = [
            # xpath начинает нумерацию в коллекциях с 1
            ExtendedWebElement(self.page, f"{self.xpath}[{number}]") for number in range(1, elements_amount)
        ]
        self.initialized[wait_condition] = True
