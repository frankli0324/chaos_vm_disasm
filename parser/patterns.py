from .opcodes import *

chrops = {
    sub_pop: '-',
    add_pop: '+',
    right_pop: '>>',
    left_pop: '<<',
    xor_pop: '^',
    or_pop: '|',
    div_pop: '/',
    mul_pop: '*',
    mod_pop: '%',
}

push_1_patterns = [
    (
        [push_1, '?', push_1, '?', push_1, '?', list(chrops.keys()), list(chrops.keys())],
        lambda x:str(eval(f'{x[0]} {chrops[x[4]]} {eval(f"{x[1]} {chrops[x[3]]} {x[2]}")}'))),
    ([push_1, '?', push_1, '?', list(chrops.keys())],
        lambda x:str(eval(f'{x[0]} {chrops[x[2]]} {x[1]}'))),
    ([push_1, '?'], lambda x:f'{x[0]}'),
    # ([push_1, '?', push_pop_as_array], lambda x: f'[{x[0]}]'),
    ([push_1, '?', push_pop_as_array, from_stack_arr], lambda x: f'stack[{x[0]}][0]'),
    (['s', attach_window, combine, construct_1, 0], lambda x: f'window.{x[0]}()'),
    (['s', attach_window, '?', combine_arr], lambda x:f'[window.{x[0]}, {x[1]}]'),
    (['s', attach_window], lambda x: f'window["{x[0]}"]'),
    (['s'], lambda x: f'"{x[0]}"'),
]

patterns = [
    ([swap_1, 1, swap_1, 0], lambda x: 'rotate(stack[-3:])'),
    ([swap_1, '?', pop], lambda x: f'pop_stack({-2-x[0]})'),
    # ([jumpif_1, '?'], lambda x: f'jump to({x[1]}) if {x[0][1](x[0][0])}'),
    ([jumpif_1, '?'], lambda x: f'jump_if to({x[0]})'),
    (
        ['#', push_pop_as_array, '#', set_stack_arr],
        lambda x: f'stack[{x[0]}][0] = stack[{x[1]}]'),
    ([push_1, '?', push_pop_as_array, init_stack_arr], lambda x: f'stack[{x[0]}] = [] if undefined'),
    (['#', 's', 36], lambda x: [
        esc := lambda x: x.replace('"', '\\"'),
        f'{x[0]}("{esc(x[1])}")'
    ][-1]),
    (['#', push_pop_as_array], lambda x:f'[{x[0]}]'),
    (['#', attach_window, combine], lambda x: f'window[{x[0]}]'),
    (['#', push_top], lambda x:f'push({x[0]});push({x[0]});'),
    ([push_1, '?', push_pop_as_array], lambda x: f'[{x[0]}]'),
    ([set_top_1, '?'], lambda x:f'top = {x[0]};'),
    ([set_top_1, '?', push_pop_as_array], lambda x:f'top = [{x[0]}];'),
    ([set_stack_size_1, '?'], lambda x:f'stack.length = {x[0]}'),  # warning
    ([jump_1, '?'], lambda x:f'jump({x[0]})'),
    ([push_true], lambda x: "true"),
    ([push_false], lambda x: "false"),
    (['?'], lambda x: opcodes[x[0]] if x[0] in opcodes else f'opcode {x[0]}')
]
patterns.sort(key=lambda x: len(x[0]), reverse=True)
patterns += push_1_patterns

char_pattrns = [
    (
        ['?', push_1, '?', list(chrops.keys()), mkchr_1, '?'],
        lambda p1, p2, op, p3: chr(eval(f'(p1 {chrops[op]} p2) + p3'))),
    (
        ['?', push_top, list(chrops.keys()), mkchr_1, '?'],
        lambda p1, op, p2: chr(eval(f'(p1 {chrops[op]} p1) + p2'))),
    (['?', mkchr_1, '?'], lambda p1, p2: chr(p1 + p2)),
]
