main:
    li $t1, 7     # binary equivalent of 7 = 111
    li $t2, 5     # binary equivalent of 5 = 101

    xor $t0, $t1, $t2  # 111 xor 101 = 110 = 6 in decimal

    li $v0, 1
    move $a0, $t0
    syscall

    li $v0, 10
    syscall