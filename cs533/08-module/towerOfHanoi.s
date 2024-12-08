.data
prompt: .asciiz "Move disk from peg "
to_peg: .asciiz " to peg "
newline: .asciiz "\n"

.text
.globl main

# hanoi(n, source, target, auxiliary)
# Arguments:
#   n in $a0
#   source in $a1
#   target in $a2
#   auxiliary in $a3

hanoi:
    # Set up stack frame: we need space for ra, s0, s1, s2, s3
    addi $sp, $sp, -20
    sw $ra, 16($sp)
    sw $s0, 12($sp)
    sw $s1, 8($sp)
    sw $s2, 4($sp)
    sw $s3, 0($sp)

    # Move arguments into saved registers
    move $s0, $a0   # n
    move $s1, $a1   # source
    move $s2, $a2   # target
    move $s3, $a3   # auxiliary

    # Base case: if n == 1
    li $t0, 1
    beq $s0, $t0, base_case

    # Recursive case:
    # Step 1: Move n-1 disks from source to auxiliary, using target as intermediate
    addi $s0, $s0, -1   # n = n-1
    # call hanoi(n-1, source, auxiliary, target)
    move $a0, $s0
    move $a1, $s1
    move $a2, $s3
    move $a3, $s2
    jal hanoi

    # Step 2: Print the move for the nth disk from source to target
    # (Since we've decremented s0, the current s0 is n-1, but we don't need n now)
print_move:
    li $v0, 4
    la $a0, prompt
    syscall

    move $a0, $s1
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, to_peg
    syscall

    move $a0, $s2
    li $v0, 1
    syscall

    li $v0, 4
    la $a0, newline
    syscall

    # Step 3: Move n-1 disks from auxiliary to target, using source as intermediate
    # hanoi(n-1, auxiliary, target, source)
    move $a0, $s0
    move $a1, $s3
    move $a2, $s2
    move $a3, $s1
    jal hanoi

    # Restore registers and return
    lw $s3, 0($sp)
    lw $s2, 4($sp)
    lw $s1, 8($sp)
    lw $s0, 12($sp)
    lw $ra, 16($sp)
    addi $sp, $sp, 20
    jr $ra

base_case:
    # If n == 1, print a single move: from s1 (source) to s2 (target)
    li $v0,4
    la $a0,prompt
    syscall

    move $a0,$s1
    li $v0,1
    syscall

    li $v0,4
    la $a0,to_peg
    syscall

    move $a0,$s2
    li $v0,1
    syscall

    li $v0,4
    la $a0,newline
    syscall

    # Restore registers and return
    lw $s3,0($sp)
    lw $s2,4($sp)
    lw $s1,8($sp)
    lw $s0,12($sp)
    lw $ra,16($sp)
    addi $sp,$sp,20
    jr $ra

main:
    # Set initial conditions: n=3, source=1, target=2, auxiliary=3
    li $a0, 3
    li $a1, 1
    li $a2, 2
    li $a3, 3
    jal hanoi

    # Exit the program
    li $v0, 10
    syscall
