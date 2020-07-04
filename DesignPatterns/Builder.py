import typing
from abc import ABC, abstractmethod, abstractproperty


class Builder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_product_a(self) -> None:
        pass

    @abstractmethod
    def produce_product_b(self) -> None:
        pass

    @abstractmethod
    def produce_product_c(self) -> None:
        pass


class ConcreteBuilderA1(Builder):
    