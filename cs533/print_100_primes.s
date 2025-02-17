# Start Program
.globl main

main:
    addu $s7, $0, $ra       # Save the return address in a global register.
    addi $s0, $0, 1         # x = 1 (number to check)
    add $s1, $0, $0         # count = 0
    addi $s2, $0, 100       # Stop when we find 100 primes

loop:
    beq $s1, $s2, exit      # if count == 100, exit

    add $a0, $s0, $0        # put x into $a0
    jal isprime             # Call isprime(x)

    beqz $v0, not_prime     # if isprime(x) == 0, skip print

    jal print               # if isprime(x) != 0, print x
    addi $s1, $s1, 1        # Increment prime count (count++)

not_prime:
    addi $s0, $s0, 1        # x++
    j loop                  # Repeat

exit:
    addu $ra, $0, $s7       # Restore return address
    jr $ra                  # Return to main program
    nop

# ===========================================
# isprime(x)
# Input: $a0 - number to check
# Output: $v0 = 1 if prime, 0 otherwise
.globl isprime
isprime:
    addi $sp, $sp, -8
    sw $ra, 4($sp)          # Save return address
    sw $a0, 0($sp)          # Save input number

    blt $a0, 2, not_prime_func  # If n < 2, it's not prime

    addi $s3, $0, 2         # i = 2
    add $s4, $a0, $0        # $s4 = n (for comparison)

test_loop:
    mul $t1, $s3, $s3       # t1 = i * i
    bgt $t1, $a0, is_prime_func # If i * i > n, number is prime

    div $t2, $a0, $s3       # n / i
    mfhi $t0                # Get remainder
    beqz $t0, not_prime_func # If n % i == 0, not prime

    addi $s3, $s3, 1        # i++
    j test_loop

is_prime_func:
    li $v0, 1               # Prime
    j isprime_return

not_prime_func:
    li $v0, 0               # Not prime

isprime_return:
    lw $a0, 0($sp)
    lw $ra, 4($sp)
    addi $sp, $sp, 8
    jr $ra

# ===========================================
# print(x)
# Prints the number in $s0 with a tab before it
.globl print
print:
    li $v0, 4
    la $a0, tab
    syscall

    li $v0, 1
    add $a0, $s0, $0
    syscall

    jr $ra

.data
tab: .asciiz "\t"
