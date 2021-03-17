let window = new Proxy({}, {
    get: (targ, name) => {
        if (targ[name] !== undefined)
            return targ[name];
        else return global[name]
    }
});
window.window = window;
var __TENCENT_CHAOS_STACK = function () {
    function __TENCENT_CHAOS_VM(current, opcode, window, stack, h, b, t) {
        // var fs = require('fs');
        // fs.writeFileSync(`${current}.txt`, JSON.stringify(opcode), (err) => 0);
        var is_empty_stack = !stack, I = [], g = null;
        current = +current, opcode = opcode || [0];
        stack = stack || [[this], [{}]];
        let cmds = {
            0: function () { var C = stack.pop(); stack.push(C[0][C[1]]) },
            1: function () { stack[stack[stack.length - 2][0]][0] = stack[stack.length - 1] },
            2: function () { stack[stack.length - 2] = stack[stack.length - 2] << stack.pop() },
            3: function () { stack.push(typeof stack.pop()) },
            4: function () { stack.push(null) },
            5: function () { stack[stack.length - 2] = stack[stack.length - 2] == stack.pop() },
            6: function () { var C = stack.pop(), I = stack[stack.length - 1]; stack[I[0]][0] = C[0][C[1]] },
            7: function () { stack.push([stack.pop(), stack.pop()].reverse()) },
            8: function () { stack[stack.length - 1] = opcode[current++] },
            9: function () { I.push([opcode[current++], stack.length, opcode[current++]]) },
            10: function () { stack.length -= opcode[current++] },
            11: function () { stack[stack.length - 2] = stack[stack.length - 2] in stack.pop() },
            12: function () { var C = stack.pop(); stack.push([stack[stack.pop()][0], C]) },
            14: function () { var C = opcode[current++], I = stack[stack.length - 2 - C]; stack[stack.length - 2 - C] = stack.pop(), stack.push(I) },
            15: function () { stack.push(stack[stack.length - 1]) },
            16: function () { stack.push([stack.pop()]) },
            18: function () {
                var C = opcode[current++], I = C ? stack.slice(-C) : [];
                stack.length -= C, I.unshift(null);
                stack.push(new (Function.prototype.bind.apply(stack.pop(), I)))
            },
            21: function () { stack.push(~stack.pop()) },
            22: function () { stack[stack.length - 2] = stack[stack.length - 2] & stack.pop() },
            23: function () { current = opcode[current++] },
            24: function () { stack.pop() },
            25: function () {
                var C = opcode[current++], I = C ? stack.slice(-C) : [];
                stack.length -= C;
                stack.push(stack.pop().apply(window, I))
            },
            26: function () { stack.push([window, stack.pop()]) },
            27: function () { stack[stack.length - 2] = stack[stack.length - 2] + stack.pop() },
            28: function () { var C = stack.pop(); stack.push(delete C[0][C[1]]) },
            29: function () { stack[stack.length - 2] = stack[stack.length - 2] - stack.pop() },
            30: function () { var C = stack[stack.length - 2]; C[0][C[1]] = stack[stack.length - 1] },
            31: function () { stack.push(opcode[current++]) },
            32: function () { stack[stack.length - 2] = stack[stack.length - 2] ^ stack.pop() },
            33: function () { stack[stack.length - 2] = stack[stack.length - 2] | stack.pop() },
            34: function () { stack[stack.length - 2] = stack[stack.length - 2] / stack.pop() },
            35: function () { stack[stack.length - 2] = stack[stack.length - 2] >= stack.pop() },
            36: function () {
                var C = opcode[current++], I = C ? stack.slice(-C) : []; stack.length -= C, I.unshift(null);
                var g = stack.pop();
                stack.push(
                    new (Function.prototype.bind.apply(g[0][g[1]], I))
                )
            },
            37: function () { stack.push(!stack.pop()) },
            39: function () {
                stack[stack.length - 2] = stack[stack.length - 2] >>> stack.pop()
            },
            40: function () { stack.push(undefined) },
            41: function () { stack.push(!0) },
            42: function () { stack.push(!1) },
            43: function () { stack[stack.length - 2] = stack[stack.length - 2] >> stack.pop() },
            44: function () {
                var g = opcode[current++], Q = [];
                let C = opcode[current++];
                let I = opcode[current++], H = [];
                for (let A = 0; A < C; A++)
                    Q[opcode[current++]] = stack[opcode[current++]];
                for (A = 0; A < I; A++)
                    H[A] = opcode[current++];
                stack.push(function B() {
                    var C = Q.slice(0); C[0] = [this], C[1] = [arguments], C[2] = [B];
                    for (var I = 0; I < H.length && I < arguments.length; I++)
                        0 < H[I] && (C[H[I]] = [arguments[I]]);
                    return __TENCENT_CHAOS_VM(g, opcode, window, C, h, b, t)
                })
            },
            45: function () { stack.push("") },
            46: function () { stack[stack.length - 2] = stack[stack.length - 2] * stack.pop() },
            47: function () { g = null },
            49: function () { I.pop() },
            50: function () { stack.push(stack[stack.pop()[0]][0]) },
            51: function () { var C = stack.pop(), I = stack[stack.length - 1]; I[0][I[1]] = stack[C[0]][0] },
            52: function () {
                var C = opcode[current++]; stack[stack.length - 1] && (current = C)
            },
            53: function () { throw stack[stack.length - 1] },
            54: function () { return !0 },
            55: function () { stack[stack.length - 2] = stack[stack.length - 2] % stack.pop() },
            56: function () { stack.length = opcode[current++] },
            58: function () { stack[stack.length - 2] = stack[stack.length - 2] === stack.pop() },
            60: function () { var C = stack.pop(), I = stack[stack.length - 1]; I[0][I[1]] = C[0][C[1]] },
            61: function () { stack[stack.length - 2] = stack[stack.length - 2] > stack.pop() },
            62: function () { stack[stack[stack.length - 1][0]] = stack[stack[stack.length - 1][0]] === undefined ? [] : stack[stack[stack.length - 1][0]] },
            63: function () {
                var C = stack.pop(), I = stack.pop();
                stack.push([I[0][I[1]], C])
            },
            64: function () {
                var C = opcode[current++], I = C ? stack.slice(-C) : [];
                stack.length -= C; var g = stack.pop();
                stack.push(g[0][g[1]].apply(g[0], I));
            },
            66: function () {
                stack[stack.length - 2] += String.fromCharCode(opcode[current++] + stack[stack.length - 1]);
            },
            67: function () { return !!g },
        };
        for (0; ;)
            try {
                for (var H = !1; !H;) {
                    H = cmds[opcode[current++]]();
                }
                if (0, g) throw g;
                return is_empty_stack ? (stack.pop(), stack.slice(3 + __TENCENT_CHAOS_VM.v)) : stack.pop()
            } catch (B) {
                0; var A = I.pop(); if (A === undefined) throw B; g = B, current = A[0], stack.length = A[1], A[2] && (stack[A[2]][0] = g)
            }
    }
    function C(C) {
        for (var I = [], g = 0; g < C.length; g++)try {
            I.push(eval(C[g]))
        } catch (Q) { I.push(undefined) } return I
    }
    function G(C, I, g) {
        if ("function" == typeof Array.prototype.indexOf)
            return Array.prototype.indexOf.call(C, I, g);
        var Q; if (null == C) throw new TypeError('"array" is null or not defined');
        var H = Object(C), A = H.length >>> 0; if (0 == A) return -1;
        var B = 0 | g; if (A <= B) return -1;
        for (Q = Math.max(0 <= B ? B : A - Math.abs(B), 0); Q < A; Q++)
            if (Q in H && H[Q] === I) return Q; return -1
    }
    function b64decode(C) {
        var I, Q = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".split(""), H = String(C).replace(/[=]+$/, ""), A = 0, B = 0, f = "";
        for (var g; g = H.charAt(B++); ~g && (I = A % 4 ? 64 * I + g : g, A++ % 4) && (f += String.fromCharCode(255 & I >> (-2 * A & 6))))
            g = G(Q, g);
        return f
    }
    function compile(C) {
        var I = C[0], g = C[1], Q = [], H = b64decode(I), A = g.shift(), B = g.shift(), f = 0;
        function G() {
            for (; f === A;)
                Q.push(B), f++, A = g.shift(), B = g.shift()
        }
        for (var w = 0; w < H.length; w++) {
            var x = H.charAt(w).charCodeAt(0);
            G(), Q.push(x), f++
        }
        G();
        return Q
    }

    __TENCENT_CHAOS_VM.v = 5;
    return __TENCENT_CHAOS_VM(0, require('./ops.js').g, window)
}();
console.log(__TENCENT_CHAOS_STACK)
console.log(window.F3B9B832({
    'a': [92400, 93371, 42183, 11182, 72352, 48612, 60166, 95303, 15670, 64797, 51763, 90802, 67637, 97126, 13569, 44834]
}))
