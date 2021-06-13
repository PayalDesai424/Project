class Student:

    #def __init__(self):
     #   self.sid=0;
      #  self.snm="Payal";

    def __init__(self, sid, snm):
        self.sid = sid;
        self.snm = snm;

    def say_hello(self):
        print("Hello from student class")

    def say_good_bye(self):
        print("Good bye from class student")

    def display(self):
        print(self.sid,self.snm)
