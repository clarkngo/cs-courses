.data
hello: .asciiz "Hello "
world: .asciiz "World\n"

.text
main:
    li $t0, 0
    li $t1, 0

    bne $t0, $t1, print_world

    # "Hello" printing
    la $a0, hello
    li $v0, 4
    syscall

print_world:
    # "World" printing
    la $a0, world
    li $v0, 4
    syscall

    # Exit
    li $v0, 10
    syscall