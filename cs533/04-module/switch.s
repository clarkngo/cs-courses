.data
zero_string: .asciiz "Choice is 0\n"
one_string:  .asciiz "Choice is 1\n"
two_string:  .asciiz "Choice is 2\n"
Def_string:   .asciiz "Invalid input\n"

.text
main:
    # Read user input
    li $v0, 5
    syscall
    move $t0, $v0

    # Check the input
    beq $t0, 0, zero
    beq $t0, 1, one
    beq $t0, 2, two
    j default

zero:
    li $v0, 4
    la $a0, zero_string
    syscall
    j end_case

one:
    li $v0, 4
    la $a0, one_string
    syscall
    j end_case

two:
    li $v0, 4
    la $a0, two_string
    syscall
    j end_case

default:
    li $v0, 4
    la $a0, Def_string 
    syscall

end_case:
    li $v0, 10
    syscall