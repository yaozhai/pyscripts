def make_instance(cls):
    """Return a new object instance"""
    
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
        
    def set_value(name, value):
        attributes[name] = value
        
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value
    
def make_class(attributes = {}, base_class = None):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
        else:
            return 'Err: Specified attribute not defined.'
        
    def set_value(name, value):
        attributes[name] = value
        
    def new(*args):
        return init_instance(cls, *args)
    
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls

def init_instance(cls, *args):
    instance = make_instance(cls)
    init = cls['get']('__init__')
    
    if init:
        init(instance, *args)
    
    return instance

def make_account_class():
    
    interest = 0.2
    
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)
        
    def deposit(self, balance):
        new_balance = self['get']('balance') + balance
        self['set']('balance', new_balance)
        
        return self['get']('balance')
    
    def withdraw(self, amount):
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        
        self['set']('balance', balance - amount)
        return self['get']('balance')
    
    return make_class(locals())

Account = make_account_class()