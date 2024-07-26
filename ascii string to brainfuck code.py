ascii_string = input("Введите сообщение состоящие из ascii символов для перевода в BrainFuck: \n")
brainfuck_code = ""

symbols_ascii = list()
for symbol in ascii_string:
    symbols_ascii.append(ord(symbol.encode("Windows-1251")))

brainfuck_code += "+" * 10 + "["

for symbol_ascii in symbols_ascii:
    brainfuck_code = brainfuck_code + ">" + "+" * (symbol_ascii // 10)

brainfuck_code = brainfuck_code + "<" * len(symbols_ascii) + "-]"

for symbol_ascii in symbols_ascii:
    brainfuck_code = brainfuck_code + ">" + "+" *  (symbol_ascii - ((symbol_ascii // 10) * 10))\
    + "."

print(brainfuck_code)