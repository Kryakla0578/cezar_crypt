import string

alpha = list(string.ascii_lowercase * 2)
print(alpha)

move_ = int(input('Choose ur move' '\n''(1 - code. 2 - decode):'))
code_ = list(input('Enter ur phrase: ').lower())
step_ = int(input('Enter quantity of steps (1-25): '))

def coder(coder):
    coder1 = list(coder)
    final_code = []
    for i in coder1:
        position = alpha.index(i)
        new_position = position + step_
        _code = alpha[new_position]
        final_code.append(_code)
    print(str(final_code))

def decoder (coder):
    coder1 = list(coder)
    final_code = []
    for i in coder1:
        position = alpha.index(i)
        new_position = position - step_
        _code = alpha[new_position]
        final_code.append(_code)
    print(str(final_code))


if int(move_) == 1:
    coder(code_)
elif move_ == 2:
    decoder(code_)
elif move_ != 1 or 2:
    print('Mistake, choose 1 or 2!')

if step_ > 25:
    print('Mistake, so many steps!!!')




