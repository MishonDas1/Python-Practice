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

# Example productions (You should define your grammar rules here)
# For demonstration, let's create a simple production:
productions = [
    Production(var_E, [var_E, ter_pl, var_F]),
    Production(var_E, [var_F]),
    Production(var_F, [ter_fr, var_E, ter_bk]),
    Production(var_F, [ter_a]),
    Production(var_F, [ter_b]),
    Production(var_F, [ter_0]),
    Production(var_F, [ter_1]),
]

# Create the CFG
cfg = CFG(start_symbol=var_E, productions=productions)

# Print CFG
print(cfg)
