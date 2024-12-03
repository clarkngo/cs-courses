.data
if: .asciiz "If\n"
else: .asciiz "Else\n"
hello: .asciiz "Hello again\n"

.text
main:
    li $t0, 0
    li $t1, 1

    bge $t0, $t1, else_statm

    # "If" printing
    la $a0, if
    li $v0, 4
    syscall
    j end_if

else_statm:
    # "Else" printing
    la $a0, else
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