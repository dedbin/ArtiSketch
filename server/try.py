def gfgfg(a: int, b: int) -> int:
    a,b = f'{a}', f'{b}'
    return int(b[:-3] + a + b[-3:])

print(gfgfg(3, 7890))