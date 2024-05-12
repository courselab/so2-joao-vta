	# Boot, say hello, and halt
	# NASM assembly, naive char by char, manually
	
	.section .text
	.globl _start
	
_start:
	mov $0xe, %ah       # set BIOS teletype mode

	mov $0x48, %al      # Load 'H' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x65, %al      # Load 'e' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x6c, %al      # Load 'l' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x6c, %al      # Load 'l' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x6f, %al      # Load 'o' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x20, %al      # Load ' ' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x57, %al      # Load 'W' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x6f, %al      # Load 'o' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x72, %al      # Load 'r' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x6c, %al      # Load 'l' ascii code
	int $0x10           # Issue BIOS interrupt

	mov $0x64, %al      # Load 'd' ascii code
	int $0x10           # Issue BIOS interrupt
	
	hlt                 # Halt the machine
	jmp _start          # Safeguard 

	.fill 510 - (. - _start), 1, 0    # Pad with zeros
	.word 0xaa55        # Boot signature
