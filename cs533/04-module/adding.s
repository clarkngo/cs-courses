.data
prompt: .asciiz "Enter an integer: "
result: .asciiz "The sum is: "

.text
.globl main

main:
    li $t0, 0  # Initialize the sum to 0

loop:
    li $v0, 4
    la $a0, prompt
    syscall

    li $v0, 5
    syscall
    move $t1, $v0

    beqz $t1, end_loop  # If input is 0, exit the loop

    add $t0, $t0, $t1  # Add the input to the sum

    j loop

end_loop:
    li $v0, 4
    la $a0, result
    syscall

    li $v0, 1
    move $a0, $t0
    syscall

    li $v0, 10
    syscall