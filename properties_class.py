class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        # cool validation here
        self.__name = value

presenter = Presenter('Chris')
# presenter.name = 'Christopher'
print(presenter.name)