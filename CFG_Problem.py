from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon

# Creation of variables
var_E = Variable("E")
var_F = Variable("F")

# Creation of terminals
ter_a  = Terminal("a")
ter_b  = Terminal("b")
ter_0  = Terminal("0")
ter_1  = Terminal("1")
ter_pl = Terminal("+")
ter_ml = Terminal("*")
ter_fr = Terminal("(")
ter_bk = Terminal(")")

# Productions
p0  = Production(var_E, [var_E, ter_pl, var_E])
p1  = Production(var_E, [var_E, ter_ml, var_E])
p2  = Production(var_E, [ter_fr, var_E, ter_bk])
p3  = Production(var_E, [var_F])

p4  = Production(var_F, [var_F, var_F])
p5  = Production(var_F, [ter_0, var_F])
p6  = Production(var_F, [ter_1, var_F])
p7  = Production(var_F, [ter_a])
p8  = Production(var_F, [ter_b])
p9  = Production(var_F, [ter_0])
p10 = Production(var_F, [ter_1])

# Creation of the CFG
cfg = CFG(
    variables={var_E, var_F},
    terminals={ter_a, ter_b, ter_pl, ter_0, ter_1, ter_ml, ter_fr, ter_bk},
    start_symbol=var_E,
    productions=[p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
)

# Helper to convert user input to Terminals
terminal_map = {
    "a": ter_a,
    "b": ter_b,
    "0": ter_0,
    "1": ter_1,
    "+": ter_pl,
    "*": ter_ml,
    "(": ter_fr,
    ")": ter_bk
}

def string_to_terminals(s):
    terminals_list = []
    for ch in s:
        if ch in terminal_map:
            terminals_list.append(terminal_map[ch])
        else:
            print(f"Invalid character '{ch}' not in grammar terminals.")
            return None
    return terminals_list

# Check for containment
while True:
    user_input = input("Please Enter a string: ").strip()
    terminals_list = string_to_terminals(user_input)
    if terminals_list is None:
        print("It is not accepted by the grammar!")
    elif cfg.contains(terminals_list):
        print("It is accepted by the grammar")
    else:
        print("It is not accepted by the grammar!")

    loop = input("Do you want to continue? (Y/N): ")
    if loop.lower() == "n":
        break
