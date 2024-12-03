.data
Thanku: .asciiz "\nThank You"

.text
main:
    li $t0, 5
    li $t1, 2

    ble $t0, $t1, else_statm

    # Subtraction
    sub $a0, $t0, $t1
    li $v0, 1
    syscall
    j end_if

else_statm:
    # Addition
    addi $a0, $t0, 20
    li $v0, 1
    syscall

end_if:
    # Print "Thank You"
    li $v0, 4
    la $a0, Thanku
    syscall

    # Exit
    li $v0, 10
    syscall