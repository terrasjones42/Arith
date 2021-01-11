import ast
# import astpretty


x="1+12+3"

# 1*2*3+5

exp=[]

prev=""
curr=""

for i in x:
    # print (i)
    if(i.isdigit()):
        if(prev.isdigit()):
            curr=curr+i
        else:
            curr=i
    else:
        exp.append(int(curr))
        curr=""
        exp.append(i)
    prev=i

exp.append(curr)

print(exp)

print(exp[0]+10)
if(exp[1]=="+"):
    print(True)



class AST():
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op=op


class Num(AST):
    def __init__(self, value):
        self.value = value



