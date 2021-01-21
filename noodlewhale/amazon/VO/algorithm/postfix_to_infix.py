def getInfix(str):
    stack=[]
    for j in range(len(str)) :
        if operand(str[j]) :
            stack.append(str[j])
        else :
            operator1=stack.pop()
            operator2=stack.pop()
            stack.append("(" + operator2 + str[j] + operator1 + ")")
    return stack.pop()        
def operand(char) :
    if (char &gt= 'a' and char &lt= 'z') or (char &gt= 'A' and char &lt= 'Z') : 
         return True 
    else :
        return False     
str=['a','b','*','c','+','d','*','e','/']
print(getInfix(str)) 
