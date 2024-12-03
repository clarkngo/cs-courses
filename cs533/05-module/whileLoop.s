.data
num: .asciiz "Please enter a number: "
Thanku: .asciiz "Thank you"

.text
main:
    li $t0, 5  # t0 = 5

while:
    beq $t0, $t1, exitt  # if cond = 5

    li $v0, 4
    la $a0, num
    syscall  # please enter a number

    li $v0, 5
    syscall  # Read input
    move $t1, $v0  # $t1 = value read

    j while

exitt:
    li $v0, 4
    la $a0, Thanku
    syscall  # print thank you

    li $v0, 10
    syscall  # exit