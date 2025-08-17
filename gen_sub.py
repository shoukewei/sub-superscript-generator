def gen_unicode_sub(num):
    """Convert number to unicode subscript"""
    subscript_map = {
        '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
        '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'
    }
    return ''.join(subscript_map.get(digit, digit) for digit in str(num))
