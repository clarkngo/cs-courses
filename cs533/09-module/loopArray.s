        .data
arr:    .word 3, 2, 1, 8, 6
        .text

main:
    la $t1, arr     # Load the address of the array into $t1
    li $t0, 0       # Initialize the loop counter to 0

loop1:
    bge $t0, 5, exit # Check if the loop counter has reached 5 (array size)

    # Load word from address and move to the next address
    lw $t2, 0($t1)
    addi $t1, $t1, 4

    # System call to print the value
    li $v0, 1
    move $a0, $t2
    syscall

    # Optional: System call to print a space character
    li $v0, 11
    li $a0, 32
    syscall

    # Increment the loop counter
    addi $t0, $t0, 1
    j loop1

exit:
    li $v0, 10
    syscall