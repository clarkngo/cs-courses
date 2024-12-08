        .data
list:   .word 3, 4, 5, 6
        .text

main:
    la $t0, list     # Load the address of the beginning of the array list[0] into $t0
    lw $t1, 4($t0)   # $t1 = first element in the array list[1] = 4

    li $v0, 1        # System call code for printing an integer
    move $a0, $t1    # Move the value of $t1 into $a0 to be printed
    syscall

    li $v0, 10       # System call code for terminating the program
    syscall