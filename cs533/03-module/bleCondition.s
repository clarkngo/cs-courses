.data
g: .asciiz "Greater\n"
ng: .asciiz "Not Greater\n"
hello: .asciiz "Hello again\n"

.text
main:
    li $t0, 0
    li $t1, 0

    ble $t0, $t1, else_statm

    # "Greater" printing
    la $a0, g
    li $v0, 4
    syscall
    j end_if

else_statm:
    # "Not Greater" printing
    la $a0, ng
    li $v0, 4
    syscall

end_if:
    # "Hello again" printing
    la $a0, hello
    li $v0, 4
    syscall

    # Exit
    li $v0, 10
    syscall