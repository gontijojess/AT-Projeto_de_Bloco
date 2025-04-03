def hanoi(disc, ori, dest, aux):
    if disc == 1:
        print(f'Move disc {disc} from tower {ori} to the tower {dest}')
        return
    hanoi(disc - 1, ori, aux, dest)
    print(f'Move disc {disc} from tower {ori} to the tower {dest}')
    hanoi(disc - 1, aux, dest, ori)

num_disks = 3
hanoi(num_disks, "A", "C", "B")