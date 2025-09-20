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
ter_i  = Terminal("i")  # Added definition for ter_i

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
p11 = Production(var_F, [ter_i])

# Creation of the CFG
cfg = CFG(
    variables={var_E, var_F},
    terminals={ter_a, ter_b, ter_pl, ter_0, ter_1, ter_ml, ter_fr, ter_bk, ter_i},
    start_symbol=var_E,
    productions=[p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
)

# Print the CFG to verify
print(cfg)
