import datetime
now = datetime.datetime.now()

class Person(object):
    """
    a person class to learn about python classes
    """
    
    def __init__(self, name, age, height, weight, gender, job):
        self.name = name
        self.AGE = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.job = job

######################################################################################## 
#get/ set
######################################################################################## 
## name ##

    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name
        
## age - constant, no setter ##

    def get_age(self):
        return self.AGE

## height ##

    def get_height(self):
        return self.name
        
    def set_height(self, height):
        self.height = height
        
## weight ##

    def get_weight(self):
        return self.weight
        
    def set_height(self, weight):
        self.weight = weight
        
## gender ##

    def get_gender(self):
        return self.gender
    
    def set_gender(self, gender):
        self.gender = gender
        
## job ##

    def get_job(self):
        return self.job
    
    def set_gender(self, job):
        self.gender = job
    
    def get_birthdate(self):
        return now.year - self.AGE

########################################################################################        
 ## to string ##   
    def __str__(self):
        print('this person is called '+self.name+ ' and is a ' +self.gender+ ' and is ' +self.age+ ' years old.')

        
