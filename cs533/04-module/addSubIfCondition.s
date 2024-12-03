.text
main:
    li $t0, 2
    li $t1, 5

    bge $t0, $t1, else_statm

    # Addition
    add $a0, $t0, $t1
    li $v0, 1
    syscall
    j end_if_statement

else_statm:
    # Subtraction
    sub $a0, $t0, $t1
    li $v0, 1
    syscall

end_if_statement:
    # Exit
    li $v0, 10
    syscall