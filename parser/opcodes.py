opcodes = {
    56: 'set_stack_size_1',
    14: 'swap_1',

    50: 'from_stack_arr',
    62: 'init_stack_arr',
    1: 'set_stack_arr',

    26: 'attach_window',
    8: 'set_top_1',
    31: 'push_1',

    42: 'push_false',
    41: 'push_true',

    24: 'pop',

    29: 'sub_pop',
    27: 'add_pop',
    43: 'right_pop',
    2: 'left_pop',
    32: 'xor_pop',
    33: 'or_pop',
    34: 'div_pop',
    46: 'mul_pop',
    55: 'mod_pop',
    15: 'push_top',
    16: 'push_pop_as_array',

    66: 'mkchr_1',
    45: 'new_string',

    23: 'jump_1',
    52: 'jumpif_1',
    18: 'construct_1',
    64: 'call_1',
    0: 'combine',
    63: 'combine_arr',
}
for op, desc in opcodes.items():
    globals()[desc] = op

__all__ = ['set_stack_size_1', 'set_top_1', 'push_1', 'pop', 'sub_pop', 'add_pop', 'right_pop', 'left_pop', 'xor_pop', 'or_pop', 'div_pop', 'mul_pop', 'mod_pop', 'push_top', 'push_pop_as_array', 'mkchr_1',
           'new_string', 'jump_1', 'attach_window', 'construct_1', 'combine', 'combine_arr', 'jumpif_1', 'swap_1', 'call_1', 'from_stack_arr', 'push_false', 'push_true', 'set_stack_arr', 'init_stack_arr', 'opcodes']
