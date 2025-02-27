### biếu thức này nhứ sau mếu 3*6+1 chuyển qua biểu thức hậu tố sẽ là 361+*
## Post
def DictOperaterIndex(operand):
    StrOperate={'+':1,'-':1,'*':2,'/':2,'^':3}
    if operand in  StrOperate.keys():
        return StrOperate[operand]

def operandPrioritizedBrackets(stack,operate1,operate2):
    pass



def BieuThucHauTo(numStr):
# PostFix làm nhiệm vụ chưa toán tữ và đưa vào các toán hạng
    Operand=["+","-","*","/","^"]
    PostFix=[]
# StackOperater đưa vào các toán hạng
    StackOperater=[]

    for operate in numStr:
        if operate not in Operand:
            PostFix.append(operate)
        elif operate in Operand:
            if len(StackOperater)==0:
                StackOperater.append(operate)
            else:
                # Nếu toán tử SAU cs độ ưu tiên cao hơn thì
                if DictOperaterIndex(StackOperater[-1])<= DictOperaterIndex(operate):
                    StackOperater.append(operate)
                else:
                # tRƯỜNG HỢP CÁI SAU CÓ ĐỘ ƯU TIÊN THẤP HƠN
                    while len(StackOperater)>0:
                        Stack=StackOperater.pop()
                        PostFix.append(Stack)
                    StackOperater.append(operate)
        # Trường hợp nó là dấu mỡ ngoặc

    str_postfix="".join(PostFix)
    return str_postfix


Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators

# 1*2+3
# 
def infixToPostfix(expression):
    stack = []  # initialization of empty stack

    output = ''

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output += character

        elif character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] < Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output += stack.pop()

    return output

# 1-2^3^3 -(4+5*6)*7


expression = input('Enter infix expression ')

print('infix notation: ', expression)

print('postfix notation: ', infixToPostfix(expression))







