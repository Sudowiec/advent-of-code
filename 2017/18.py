import threading
import time
import queue
from collections import defaultdict
instructions = []
while True:
    try:
        instructions.append(input())
    except EOFError:
        break

glob = [0, 0]
def thread_func(qread, qwrite, p):
    global instructions
    global glob
    registers = defaultdict(lambda: 0)
    registers['p'] = p
    index = 0
    while index < len(instructions):
        cur_ins = instructions[index]
        cur_ins = cur_ins.split(" ")
        if cur_ins[0] == "snd":
            amount = cur_ins[1]
            if cur_ins[1] in registers:
                amount = registers[cur_ins[1]]
            qwrite.put(int(amount))
            glob[p] += 1
            print("sd" + str(p) + str(amount))
        elif cur_ins[0] == "set":
            amount = cur_ins[2]
            if cur_ins[2] in registers:
                amount = registers[cur_ins[2]]
            registers[cur_ins[1]] = int(amount)
        elif cur_ins[0] == "add":
            amount = cur_ins[2]
            if cur_ins[2] in registers:
                amount = registers[cur_ins[2]]
            registers[cur_ins[1]] += int(amount)
        elif cur_ins[0] == "mul":
            amount = cur_ins[2]
            if cur_ins[2] in registers:
                amount = registers[cur_ins[2]]
            registers[cur_ins[1]] *= int(amount)
        elif cur_ins[0] == "mod":
            amount = cur_ins[2]
            if cur_ins[2] in registers:
                amount = registers[cur_ins[2]]
            registers[cur_ins[1]] %= int(amount)
        elif cur_ins[0] == "jgz":
            amountone = cur_ins[1]
            if cur_ins[1] in registers:
                amountone = registers[cur_ins[1]]
            if int(amountone) > 0:
                amount = cur_ins[2]
                if cur_ins[2] in registers:
                    amount = registers[cur_ins[2]]
                index += int(amount)
                continue
        elif cur_ins[0] == "rcv":
            try:
                registers[cur_ins[1]] = qread.get(timeout=5)
            except queue.Empty:
                print("ret")
                return
            print("rv" + str(p) + str(registers[cur_ins[1]]))
        else:
            print("AAAAAAAA")
            exit(1)
        index += 1

qzero = queue.Queue() # zero czyta, one wysyła
qone = queue.Queue() # one czyta, zero wysyła
zero = threading.Thread(target=thread_func, args=(qzero, qone, 0))
one = threading.Thread(target=thread_func, args=(qone, qzero, 1))

zero.start()
one.start()
zero.join()
one.join()
print(glob[1], glob[0])