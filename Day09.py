import time

start_time = time.time()

checksum = 0

with open('inputs/09_1.txt', 'r') as file:
    line = file.readline().rstrip()

    dbs = [int(i) for i in line]
    current_db_i = 0
    current_db_id = 0
    current_db_cnt = dbs[0]

    last_db_i = len(dbs) - 2 if len(dbs) % 2 == 0 else len(dbs) - 1
    last_db_id = (len(dbs)- 1) // 2
    last_db_cnt = dbs[last_db_i]

    position = 0

    breaken = False

    while not breaken:
        while (current_db_cnt > 0):
            checksum += position * current_db_id
            current_db_cnt -= 1
            position += 1
        empty_db_i = current_db_i + 1
        empty_db_cnt = dbs[empty_db_i]
        while empty_db_cnt > 0:
            while last_db_cnt == 0:
                last_db_i -= 2
                last_db_id -= 1
                last_db_cnt = dbs[last_db_i]
            
            if last_db_i <= current_db_i:
                breaken = True
                break
            
            checksum += position * last_db_id
            dbs[last_db_i] -= 1
            last_db_cnt -= 1

            empty_db_cnt -= 1
            position += 1
        current_db_i += 2
        current_db_id += 1
        current_db_cnt = dbs[current_db_i]

print(f"Part 1: {checksum}") # 6382875730645

with open('inputs/09_1.txt', 'r') as file:
    line = file.readline().rstrip()
    dbs = [(int(ch), i // 2) for i, ch in enumerate(line)]
    
    current_empty_i = 1
    current_empty_cnt = dbs[current_empty_i]

    last_db_i = len(dbs) - 2 if len(dbs) % 2 == 0 else len(dbs) - 1

    while last_db_i > 0:
        last_db_cnt = dbs[last_db_i][0]
        for i in range(1, last_db_i, 2):
            if dbs[i][0] >= last_db_cnt:
                space = dbs[i][0]
                dbs[i] = (0, 0)
                dbs.insert(i + 1, (last_db_cnt, dbs[last_db_i][1]))
                dbs.insert(i + 2, (space - last_db_cnt, 0))

                # dbs[last_db_i + 1] = (dbs[last_db_i + 1][0] + last_db_cnt, 0)
                # dbs[last_db_i + 2] = (0, 0)

                if last_db_i + 3 < len(dbs):
                    dbs[last_db_i + 1] = (dbs[last_db_i + 1][0] + last_db_cnt + dbs[last_db_i + 3][0], 0)
                    del dbs[last_db_i + 3]
                    del dbs[last_db_i + 2]
                else:
                    dbs[last_db_i + 1] = (dbs[last_db_i + 1][0] + last_db_cnt, 0)
                    dbs[last_db_i + 2] = (0, 0)
                last_db_i += 2
                break
        last_db_i -= 2

    checksum = 0

    current_db_i = 0

    position = 0
    # print(dbs)

    while current_db_i < len(dbs):
        current_db_id = dbs[current_db_i][1]
        current_db_cnt = dbs[current_db_i][0]

        while (current_db_cnt > 0):
            checksum += position * current_db_id
            current_db_cnt -= 1
            position += 1

        empty_db_i = current_db_i + 1
        if empty_db_i == len(dbs):
            break
        empty_db_cnt = dbs[empty_db_i][0]
        position += empty_db_cnt

        current_db_i += 2



print(f"Part 2: {checksum}") # 6420913943576

print(f"Time: {time.time() - start_time}, array len: {len(dbs)}")

