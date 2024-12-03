.data
num: .asciiz "Please enter a number: "
msg: .asciiz "The prime factorization of "
is:  .asciiz "is "
comma: .asciiz ","
nl:  .asciiz "\n"

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

    # Print "The prime factorization of "
    li $v0, 4
    la $a0, msg
    syscall

    # Print the input number
    li $v0, 1
    move $a0, $t0
    syscall

    # Print "is "
    li $v0, 4
    la $a0, is
    syscall

    # Initialize loop counter
    li $t1, 2  # Counter starts from 2

    # Loop to find prime factors
    while:
        # Check if the current number is a factor
        div $t0, $t1
        mfhi $t2  # Remainder in $t2

        # If not a factor, increment the counter
        bnez $t2, else

        # Print the factor and a comma
        li $v0, 1
        move $a0, $t1
        syscall

        li $v0, 4
        la $a0, comma
        syscall

        # Divide the input number by the factor
        mflo $t0

        # Jump back to the beginning of the loop
        j while

    else:
        # Increment the counter
        addi $t1, $t1, 1

        # Jump back to the beginning of the loop
        j while

    # Print a newline
    li $v0, 4
    la $a0, nl
    syscall

    # Exit the program
    li $v0, 10
    syscall