main:
    li $v0, 1      # print_int
    li $a0, 17
    syscall

    li $a0, 71
    syscall

    li $a0, 45
    syscall

    li $v0, 10     # exit
    syscall
