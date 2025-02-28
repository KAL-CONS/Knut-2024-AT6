from main import UserInputValidator
instance1 = UserInputValidator([-100,-50,-5,0,1,2,3,-1,-2,-3,4,5,6,7,8,9,10])
instance2 = UserInputValidator(["-5","0","1","2","3","-1"])
instance1.validate_positive_integers()
instance2.validate_positive_integers()

