class DecafException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        #TODO: 完善报错信息
        return self.message