.data
hello: .asciiz "Hello\n"
newline: .asciiz "\n"

.text
main:
    # Print "Hello"
    li $v0, 4          # syscall code for print_string
    la $a0, hello      # load address of "Hello"
    syscall

    # Print newline
    la $a0, newline    # load address of newline
    syscall

    # Print "2020"
    li $v0, 1          # syscall code for print_int
    li $a0, 2020       # load integer 2020
    syscall

    # Exit
    li $v0, 10         # syscall code for exit
    syscall
