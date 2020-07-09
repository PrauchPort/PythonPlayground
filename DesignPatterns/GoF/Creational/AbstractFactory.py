# https://refactoring.guru/design-patterns/abstract-factory/python/example#lang-features

import typing
from abc import abstractmethod, ABC


class AbstractProductA(ABC):

    @abstractmethod
    def do_a(self):
        pass


class AbstractProductB(ABC):

    @abstractmethod
    def do_b(self):
        pass

    @abstractmethod
    def do_extra_b(self, collaborator):
        pass


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteProductA1(AbstractProductA):

    def do_a(self):
        return "Did A1!"


class ConcreteProductA2(AbstractProductA):

    def do_a(self):
        return "Did A2!"


class ConcreteProductB1(AbstractProductB):
    def do_b(self):
        return "Did B1!"

    def do_extra_b(self, collaborator: AbstractProductA):
        result = collaborator.do_a()
        return "Did B1! " + result


class ConcreteProductB2(AbstractProductB):
    def do_b(self):
        return "Did B2!"

    def do_extra_b(self, collaborator: AbstractProductA):
        result = collaborator.do_a()
        return "Did B2! " + result


class ConcreteFactoryA(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteFactoryB(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.do_b()}")
    print(f"{product_b.do_extra_b(product_a)}", end="")


if __name__ == "__main__":
    client_code(ConcreteFactoryA())
    client_code(ConcreteFactoryB())
