.data
num: .asciiz "Please enter a number: "
msg: .asciiz "Hello \n"

.text
main:
    # Prompt for input
    li $v0, 4
    la $a0, num
    syscall

    # Read integer input
    li $v0, 5
    syscall
    move $t1, $v0

    # Initialize loop counter
    li $t0, 0

for_loop:
    # Check loop condition
    bge $t0, $t1, exit

    # Print message
    li $v0, 4
    la $a0, msg
    syscall

    # Increment loop counter
    addi $t0, $t0, 1
    j for_loop

exit:
    # Exit program
    li $v0, 10
    syscall