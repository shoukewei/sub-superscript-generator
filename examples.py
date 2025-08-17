# Chemistry Formulas

from gen_sub import gen_unicode_sub

# Example: H2O and CO2
water = f"H{gen_unicode_sub(2)}O"
carbon_dioxide = f"CO{gen_unicode_sub(2)}"
print("Chemical formulas:")
print(" ", water)
print(" ", carbon_dioxide)

# # Example: Einstein's famous equation
from gen_sup import gen_unicode_sup
equation = f"E = mc{gen_unicode_sup(2)}"
print("Physics formula:")
print(" ", equation)

#
from gen_subsup import gen_unicode_subsup
# Example: x1², a2³, v0²
examples = [
    gen_unicode_subsup("x", sub=1, sup=2),
    gen_unicode_subsup("a", sub=2, sup=3),
    gen_unicode_subsup("v", sub=0, sup=2),
]
print("Math expressions:")
for e in examples:
    print(" ", e)