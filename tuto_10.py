# descriptors

import logging


class Lazy:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, cls, name):
        self.key = name

    def __get__(self, instance, cls):
        if instance:
            value = self.func(instance)
            instance.__dict__[self.key] = value
            return value
        else:
            return self


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    area = Lazy(lambda self: self.width * self.height)
    perimeter = Lazy(lambda self: 2*self.width + 2*self.height)


r = Rectangle(3, 4)

print(r.area)
print(r.perimeter)
print(r.__dict__)

# PROXIES IN WEAKREF

# LOGGING
debug = True
logging.basicConfig(level=logging.DEBUG,
                    format=f'%(process)d-%(levelname)s-%(message)s')

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    if debug:

        log = logging.getLogger(f'{__module__}.{__qualname__}')

        def deposit(self, amount):
            logging.info('This is an info message')
            logging.warning('This is a warning message')
            logging.error('This is an error message')
            logging.critical('This is a critical message')
            Account.log.debug('Depositing %f', amount)
            self.balance += amount

        def withdraw(self, amount):
            Account.log.debug('Withdrawing %f', amount)
            self.balance -= amount
    else:
        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            self.balance -= amount


acc = Account("NB", 1500)
acc.deposit(1500)
print(acc.balance)


# class mytype(type):
#     # Creates the class namespace

#     @classmethod
#     def __prepare__(meta, clsname, bases):


#         print("Preparing:", clsname, bases)
#         return super().__prepare__(clsname, bases)
#     # Creates the class instance after body has executed
#     @staticmethod
#     def __new__(meta, clsname, bases, namespace):


#         print("Creating:", clsname, bases, namespace)
#         return super().__new__(meta, clsname, bases, namespace)
#     # Initializes the class instance
#     def __init__(cls, clsname, bases, namespace):


#         print("Initializing:", clsname, bases, namespace)
#         super().__init__(clsname, bases, namespace)
#     # Creates new instances of the class
#     def __call__(cls, *args, **kwargs):


#         print("Creating instance:", args, kwargs)
#         return super().__call__(*args, **kwargs)
# # Example
# class Base(metaclass=mytype):
#     pass
# b = Base()

# class Account(Base):
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
# # print(type(Account))
