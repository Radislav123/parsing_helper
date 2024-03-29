from selenium.webdriver import Chrome

from parsing_helper.settings import Settings


class BasePage:
    settings: Settings
    # элементы url
    scheme: str
    domain: str
    path: str
    parameters = {}

    def __init__(self, driver: Chrome) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.url)

    @property
    def url(self) -> str:
        return self.construct_url()

    def construct_url(self, scheme = None, domain = None, path = None, parameters = None) -> str:
        if scheme is None:
            scheme = self.scheme
        if domain is None:
            domain = self.domain
        if path is None:
            path = self.path
        if parameters is None:
            parameters = self.parameters

        url = f"{scheme}://{domain}/{path}"
        if parameters:
            url += '?'
            for parameter_name in parameters:
                url += f"{parameter_name}={parameters[parameter_name]}&"
            url = url[:-1]
        return url

    def scroll(self, x_offset, y_offset) -> None:
        self.driver.execute_script(f"window.scrollBy({x_offset}, {y_offset});")

    def scroll_up(self, offset) -> None:
        self.scroll(0, -offset)

    def scroll_down(self, offset) -> None:
        self.scroll(0, offset)

    def transfer_cookies(self, donor_driver: Chrome) -> None:
        self.open()
        for cookie in donor_driver.get_cookies():
            self.driver.add_cookie(cookie)
        self.open()

    def set_cookies(self, cookies: list[dict[str, bool | int | str]]) -> None:
        self.open()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.open()

    def reset_cookies(self) -> None:
        self.driver.delete_all_cookies()
        self.open()
