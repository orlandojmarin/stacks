"""
Orlando Marin
Project 5 - Stacks
November 7, 2024

Project 5 is to create a program to evaluate a postfix notation using a stack. 
You must use a Stack class to implement this Abstract Data Type.
Given a postfix notation: 3 5 1 - * 2 +

Process each term / token in the expression (operand or operator) one by one.
If a token is an operand, push it into the stack.

If a token is an operator, pop the stack top item as the 2nd operand and pop 
the next item as the 1st operand. Evaluate the expression and push the result 
back into the stack. This result will be either the operand for the next 
operation or, if that was the last operation, the result of the entire postfix 
notation.

For a valid postfix notation, when you are done processing the expression, 
there should be exactly one token on the stack, which is the answer to your 
expression. If your program is attempting to pop an empty stack, or if your 
expression evaluation ends with more than one token in the stack, the postfix 
notation is invalid.

Your program should be able to take any postfix notation as input and evaluate 
to give the result. It should also be able to determine if an expression is 
valid or invalid.

Your program submission must be documented, with both internal and external
documentation. Code without documentation will either be returned, or you will 
be asked to meet with me to explain your code.
"""

# import pydoc for documentation purposes
import pydoc


class Stack:
    """
    Implements a stack data structure with methods for common stack operations.
    
    Methods:
        - isEmpty: Checks if the stack is empty and returns a boolean result.
        - push: Adds an item to the top of the stack.
        - pop: Removes and returns the top item from the stack.
        - peek: Returns the top item without removing it.
        - size: Returns the number of items in the stack.
    """
    
    # constructor
    def __init__(self):
        self.items = []
    
    # tests to see whether the stack is empty - returns boolean
    def isEmpty(self):
        return self.items == []
    
    # adds a new item to the top of the stack
    def push(self, item):
        self.items.append(item)
    
    # removes the top item from the stack  
    def pop(self):
        return self.items.pop()
    
    # returns the top item from the stack but doesn't remove it   
    def peek(self):
        return self.items[len(self.items) - 1]
    
    # returns the number of items on the stack
    def size(self):
        return len(self.items)
        
        
def main():
    """
    Evaluates a postfix expression using a stack.
    
    Processes each item (number or operator) in the given postfix list.
    - Numbers are pushed onto the stack.
    - Operators pop the top two numbers from the stack, perform the operation,
      and push the result back onto the stack.
    
    At the end, if the expression is valid, one final result remains on the 
    stack.
    If the expression is invalid, an error message is printed.
    """
    
    # create a postfix notation with each term in a list called postFixList
    postFixList = [3, 5, 1, "-", "*", 2, "+"]
    
    # create an empty stack called postFixStack
    postFixStack = Stack()
    
    # iterate through each element of the postFixList
    for element in postFixList:
        # if the element is an operand (+, -, *, /), pop the top item in the
        # stack as the 2nd operand, then pop the new top item as the 1st
        # operand, perform the corresponding calculation (evaluation), and push
        # the evaluation to the top of the postFixStack
        if element == "+":
            if postFixStack.size() >= 2:
                secondOperand = postFixStack.pop()
                firstOperand = postFixStack.pop()
                evaluation = firstOperand + secondOperand
                postFixStack.push(evaluation)
            else:
                print("The postfix expression provided is invalid")
                return None
            
        elif element == "-":
            if postFixStack.size() >= 2:
                secondOperand = postFixStack.pop()
                firstOperand = postFixStack.pop()
                evaluation = firstOperand - secondOperand
                postFixStack.push(evaluation)
            else:
                print("The postfix expression provided is invalid")
                return None
            
        elif element == "*":
            if postFixStack.size() >= 2:
                secondOperand = postFixStack.pop()
                firstOperand = postFixStack.pop()
                evaluation = firstOperand * secondOperand
                postFixStack.push(evaluation)
            else:
                print("The postfix expression provided is invalid")
                return None
            
        elif element == "/":
            if postFixStack.size() >= 2:
                secondOperand = postFixStack.pop()
                if secondOperand == 0:
                    print("Error: Can't divide by 0.")
                    return None
                firstOperand = postFixStack.pop()
                evaluation = firstOperand / secondOperand
                postFixStack.push(evaluation)
            else:
                print("The postfix expression provided is invalid")
                return None
            
        else:
            postFixStack.push(element)
    
    # once we are done iterating through each element in the list, if there is
    # one item in the postFixStack, then that item is the answer (result) of
    # the post fix expression! Print the result. 
    # If there isn't exactly one item left in the postFixStack, then something 
    # went wrong and the expression is invalid.
    if postFixStack.size() == 1:   
        result = postFixStack.pop()
        print(result)
    else:
        print("The postfix expression provided is invalid")
    
      
# call main
if __name__ == "__main__":
    main()

# documentation
pydoc.writedoc("main")