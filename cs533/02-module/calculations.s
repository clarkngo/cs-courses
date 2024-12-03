.data
nl: .asciiz "\n"

.text
main:
    li $t0, 2  # $t0=2
    li $t1, 7  # $t1=7
    li $t2, 5  # $t2=5
    li $t3, 8  # $t3=8

    add $a0, $t0, $t3  # $a0 = $t0 + $t3 (2+8)
    li $v0, 1          # print integer
    syscall            # print the result of the addition
    li $v0, 4          # print new line
    la $a0, nl
    syscall

    addi $a0, $t2, 17  # $a0 = $t2 + 17 (5+17)
    li $v0, 1          # print integer
    syscall            # print the result of the addition
    li $v0, 4          # print new line
    la $a0, nl
    syscall

    sub $a0, $t0, $t1  # $a0 = $t0 - $t1 (2-7)
    li $v0, 1          # print integer
    syscall            # print the result of the subtraction

    li $v0, 4
    la $a0, nl
    syscall

    mult $t1, $t2   # sizeof one register is 32 bits, then multiplication of two registers are 64 bits
    mflo $a0        # the result will be saved in two registers (Hi Lo)
                    # we multiplied small numbers so we used mflo to see the result, then $a0 = $t1*$t2
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, nl
    syscall

    div $t1, $t2   # Hi - remainder, lo - quotient = $t1 / $t2
    mflo $a0        # $a0 = $t1 / $t2
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, nl
    syscall

    mfhi $a0        # mfhi will copy the remainder of the division operation of t1/t2 value into a0
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, nl
    syscall

    rem $a0, $t1, $t0   # another way to get the remainder a0=t1 % t0
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, nl        # print new line
    syscall

    li $v0, 10
    syscall