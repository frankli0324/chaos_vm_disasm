from naya import tokenize, stream_array
from .opcodes import *
from .utils import *
from .patterns import *


def get_string(ops):
    with ops as consumed:
        if next(ops) != new_string:
            return False
        s = ''
        for possib, func in char_pattrns:
            res = match([push_1] + possib, ops)
            if res:
                s += func(*res[1])
                ops.skip(res[0])
                break
        else:
            return False
        while True:
            for possib, func in char_pattrns:
                res = match([set_top_1] + possib, ops)
                if res:
                    s += func(*res[1])
                    ops.skip(res[0])
                    break
            else:
                break
        if (next_op := next(ops)) != pop:
            print('Warning: stack not balanced')
            ops.rollback(1)
        cnsmed = consumed()
    return cnsmed, s


def match(pattern, ops) -> tuple[int, list]:
    res = []
    with ops as consumed:
        for item in pattern:
            if item == '*' or item == '#':
                tmp_res = []
                pin = ops.layers[-1]
                for pat, fmt in patterns if item == '*' else push_1_patterns:
                    if pat == pattern:
                        continue
                    if (inner := match(pat, ops)) != False:
                        consumed_ops, inner_result = inner
                        tmp_res.append((consumed_ops, (inner, fmt)))
                if not tmp_res:
                    return False
                rb, r = max(tmp_res, key=lambda x: x[0])
                ops.skip(rb)
                res.append(r)
            elif item == 's':
                if s := get_string(ops):
                    res.append(s[1])
                    ops.skip(s[0])
                else:
                    return False
            elif item == '?':
                op = next(ops)
                if op == new_string:
                    ops.rollback(1)
                    if s := get_string(ops):
                        op = s[1]
                        ops.skip(s[0])
                    else:
                        op = next(ops)
                res.append(op)
            elif isinstance(item, str):
                string = get_string(ops)
                if not string or string[1] != item:
                    return False
                ops.skip(string[0])
            elif isinstance(item, list):
                op = next(ops)
                if all([op != i for i in item]):
                    return False
                res.append(op)
            elif next(ops) != item:
                return False
        cnsmd = consumed()
    return cnsmd, res


def recursive_fmt(res, fmt):
    b, res = res
    ret = ''
    for i in range(len(res)):
        if isinstance(res[i], tuple) and isinstance(res[i][1], type(lambda: None)):
            res[i] = recursive_fmt(res[i][0], res[i][1])
    return fmt(res)


def parse(file, start):
    ops = stream_array(tokenize(open(file)))
    for _ in range(start):
        next(ops)
    # ops = iter([1, 2, 3, 45, push_1, 1, push_1, 1, 4, 5, 6])
    ops = Buffered(ops)
    while True:
        try:
            line = str(ops.pointer)
            if res := match(['*'], ops):
                print(line.rjust(6), recursive_fmt(res, lambda x: f'{x[0]}'), sep='\t')
                ops.skip(res[0])
            else:
                next(ops)
        except StopIteration:
            return
