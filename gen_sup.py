def gen_unicode_sup(num):
    """Convert number to unicode superscript"""
    superscript_map = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }
    return ''.join(superscript_map.get(digit, digit) for digit in str(num))

