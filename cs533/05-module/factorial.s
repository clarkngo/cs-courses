.data
num: .asciiz "Enter a number: "
r:   .asciiz "!="
nl:  .asciiz "\n"
result: .asciiz "The factorial of "

.text
main:
    # Prompt for input
    li $v0, 4
    la $a0, num
    syscall

    # Read integer input
    li $v0, 5
    syscall
    move $t0, $v0

    # Initialize loop counter and result
    li $t1, 1
    li $t2, 1

for_loop:
    # Check loop condition
    bgt $t1, $t0, exit

    # Multiply result by current number
    mul $t2, $t2, $t1

    # Increment loop counter
    addi $t1, $t1, 1

    # Jump back to loop start
    j for_loop

exit:
    # Print the result message
    li $v0, 4
    la $a0, result
    syscall

    # Print the input number
    li $v0, 1
    move $a0, $t0
    syscall

    # Print the "!=" symbol
    li $v0, 4
    la $a0, r
    syscall

    # Print the factorial result
    li $v0, 1
    move $a0, $t2
    syscall

    # Print newline
    li $v0, 4
    la $a0, nl
    syscall

    # Exit the program
    li $v0, 10
    syscall