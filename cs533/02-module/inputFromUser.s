main:
    li $v0, 5     # Load immediate value 5 into register $v0
    syscall        # System call to read an integer from the user
    move $t0, $v0  # Move the read integer from $v0 to $t0

    li $v0, 10      # Load immediate value 10 into register $v0
    syscall        # System call to exit the program