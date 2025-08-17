def gen_unicode_subsup(base, sub=None, sup=None):
    """Format a string with optional Unicode subscript and superscript"""
    subscript_map = {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉'}
    superscript_map = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'}
    
    result = base
    if sub is not None:
        result += ''.join(subscript_map.get(d, d) for d in str(sub))
    if sup is not None:
        result += ''.join(superscript_map.get(d, d) for d in str(sup))
    return result