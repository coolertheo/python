import ast

CODE = """
addition_lambda = lambda a, b: a + b
test = "test"
test2 = 66

class Test:
    def __init__(self):
        pass

def addition(a: int, b: int) -> int:
    return a + b
"""

parsed = ast.parse(CODE)

for item in parsed.body:
    type_map = {
        ast.FunctionDef: "eine function",
        ast.AsyncFunctionDef: "eine async function",
        ast.ClassDef: "eine class",
        ast.Lambda: "eine lambda function"
    }

    if isinstance(item, ast.Assign):
        name = item.targets[0].id
        item = item.value
    else:
        name = item.name

    if isinstance(item, ast.Constant):
        start = item.lineno
        end = item.end_lineno
        print(
            f"{name} ist eine variable mit \"{item.value}\" als "
            f"wert und sie start bei zeile {start} und endet bei zeile {end}"
        )
    else:

        _type = type_map.get(type(item), "von einem unbekannten typ")
        start = item.lineno
        end = item.end_lineno
        print(f"{name} ist {_type} welche bei zeile {start} started und bei zeile {end} endet")
