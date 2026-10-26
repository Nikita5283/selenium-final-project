from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Кнопка 'Добавить в корзину' не найдена"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Название товара отсутствует на странице"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Цена товара отсутствует на странице"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self, expected_name):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Сообщение об успешном добавлении в корзину не появилось"
        actual_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert expected_name == actual_name, \
            f"Название товара в сообщении ('{actual_name}') не совпадает с добавленным ('{expected_name}')"

    def should_be_correct_basket_total(self, expected_price):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Сообщение со стоимостью корзины не появилось"
        actual_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert expected_price == actual_price, \
            f"Стоимость корзины ('{actual_price}') не совпадает с ценой товара ('{expected_price}')"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"
