.data

.text
.globl main

# Function: test_prime
# Input: $a0 (number to test)
# Output: $v0 (1 if prime, 0 otherwise)
test_prime:
    # Save registers
    addi $sp, $sp, -8
    sw $ra, 0($sp)
    sw $s0, 4($sp)

    # Edge case: numbers less than 2 are not prime
    blt $a0, 2, not_prime

    # Initialize divisor to 2
    li $s0, 2

    # Loop to check divisors
test_prime_loop:
    mul $t1, $s0, $s0       # t1 = s0 * s0
    bgt $t1, $a0, is_prime   # If s0^2 > n, n is prime

    div $t2, $a0, $s0        # Perform a0 / s0
    mfhi $t0                 # Get remainder
    beqz $t0, not_prime      # If remainder is 0, n is not prime

    addi $s0, $s0, 1         # Increment divisor
    j test_prime_loop

is_prime:
    li $v0, 1                # Number is prime
    j return

not_prime:
    li $v0, 0                # Number is not prime
    j return

return:
    # Restore registers
    lw $ra, 0($sp)
    lw $s0, 4($sp)
    addi $sp, $sp, 8
    jr $ra

# Main program
# This program takes a number input and determines if it is prime.
main:
    # Prompt user for input
    li $v0, 4                # Print string syscall
    la $a0, prompt           # Load prompt message
    syscall

    # Read integer input
    li $v0, 5                # Read integer syscall
    syscall
    move $a0, $v0            # Store input in $a0

    # Test if the number is prime
    jal test_prime           # Call test_prime function

    # Print the result
    beqz $v0, print_not_prime
    li $v0, 4                # Print string syscall
    la $a0, is_prime_msg     # Load "is prime" message
    syscall
    j exit

print_not_prime:
    li $v0, 4                # Print string syscall
    la $a0, not_prime_msg    # Load "not prime" message
    syscall

exit:
    li $v0, 10               # Exit syscall
    syscall

# Data section
.data
prompt:         .asciiz "Enter a number to check if it is prime: "
is_prime_msg:   .asciiz "The number is prime.\n"
not_prime_msg:  .asciiz "The number is not prime.\n"
