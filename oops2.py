class Calculator:
    def add(self,a,b):
        return a+b 
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def action(self,action,a,b):
        if action=="add":
            print(self.add(a,b))
        elif action=="sub":
            print(self.sub(a,b))
        elif action=="mul":
            print(action.mul(a,b))
        elif action=="div":
            print(self.div(a,b))
        else:
            print("default action")

cal=Calculator()
action=input("enter the action" )
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
cal.action(action,num1,num2)