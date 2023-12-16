import ast

print(dir(ast))
print(help("ast.parse"))
print(help("ast.dump"))

source = "1 - 2 * hoge(3)"

print("変換元の文字列 source=", end="")
print(source)

print("ast.Node に変換後")
node: ast.AST = ast.parse(source, mode='eval')
print(ast.dump(node, indent=4))

#print("eavl(source)=", end="")
#print(eval(source))

class PrintNodeVisitor(ast.NodeVisitor):
    def visit(self, node):
        print(node)
        return super().visit(node)
    
PrintNodeVisitor().visit(node)

