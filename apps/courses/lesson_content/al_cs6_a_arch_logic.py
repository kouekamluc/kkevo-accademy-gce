"""Lower Sixth Computer Science (A Level depth pass): machine models, the CPU, and digital logic.

KKEVO draft teaching material, written to go deeper than the topic overviews in l6_computer_science_a.py.
A reviewer checks each lesson against the official syllabus before publishing.
"""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "lower-sixth")

ARCH = "Computer Organization & Architecture"
LOGIC = "Digital Logic"
MM = "Machine models"
CPU = "The CPU"
COMB = "Combinational circuits"
SEQ = "Sequential circuits"
SIMP = "Simplification"

LESSONS = []

# ------------------------------------------------------------------ 1 Von Neumann vs Harvard compared
LESSONS.append(lesson(
    module=ARCH, topic=MM,
    title="Von Neumann and Harvard compared: choosing a model",
    slug="csa-von-neumann-harvard-compared",
    minutes=22,
    summary="Compare the two machine models point by point, count memory accesses for a short program under each, and justify the model (or a mixture) for a given device.",
    objectives=[
        "Explain why a program stored as data makes a computer general purpose",
        "Count memory accesses for a short program on a Von Neumann and a Harvard machine",
        "Explain the modified Harvard design used in modern processors",
        "Choose and justify a machine model for a stated device",
    ],
    key_concepts=["Stored program", "Von Neumann machine", "Harvard machine", "Modified Harvard",
                  "Instruction cache", "Memory access cycle"],
    blocks=[
        H("Introduction"),
        T(r"A phone in Douala, a solar charge controller on a roof in Maroua and a school laptop in Bamenda all run "
          r"programs, yet their processors are organised differently. The way instructions and data are stored and moved "
          r"is called the **machine model**."),
        T(r"The overview lesson named the two main models. Here you go further: you will *count* memory accesses, "
          r"see why modern processors mix both models, and practise choosing a model for a device."),
        H("Why the stored program matters"),
        D(r"In a **stored-program computer**, the instructions are held in memory as binary numbers, just like data. "
          r"To change what the computer does you change the contents of memory, not the wiring.",
          title="Stored program"),
        T(r"Because instructions are numbers in memory, a **compiler** can write a program into memory as its output, "
          r"and the operating system can **load** that program and run it. A program can also be treated as data: copied, "
          r"downloaded or updated. This is why one phone can run thousands of different apps."),
        H("The two models side by side"),
        KEY("Where the instructions live", r"The two models differ in memory and bus design.",
            cards=[
                ["Von Neumann", r"One memory holds instructions **and** data. One address bus and one data bus are shared. The CPU does one memory transfer at a time."],
                ["Harvard", r"Two memories: one for instructions, one for data. Each has its own address and data buses, so an instruction fetch and a data access can happen **in the same cycle**."],
            ]),
        D(r"The **Von Neumann bottleneck** is the limit set by the single shared path to memory. Every instruction "
          r"fetch and every data access must take turns, so the processor can spend time waiting.",
          title="Von Neumann bottleneck"),
        H("Counting memory accesses"),
        T(r"To compare the models, count how many cycles are spent on memory. Assume each memory access takes one cycle "
          r"and ignore decoding and the ALU. Take this four-instruction program:"),
        CODE("LDA 30   ; read memory 30 into ACC   (1 data read)\n"
             "ADD 31   ; add memory 31 to ACC      (1 data read)\n"
             "STA 33   ; store ACC in memory 33    (1 data write)\n"
             "HLT      ; stop                      (no data access)",
             "text", title="A short program"),
        EX("Worked example 1: Von Neumann count",
           intro=r"How many memory-access cycles does the program need on a Von Neumann machine?",
           steps=[
               S("Count instruction fetches", text=r"Four instructions, so 4 fetches."),
               S("Count data accesses", text=r"LDA, ADD and STA each use memory once: 3 data accesses."),
               S("One shared bus, so add them", math=r"4 + 3 = 7 \text{ cycles}"),
           ]),
        EX("Worked example 2: Harvard count",
           intro=r"How many cycles does the same program need on an ideal Harvard machine?",
           steps=[
               S("Cycle 1", text=r"Fetch instruction 1 (LDA) from instruction memory."),
               S("Cycle 2", text=r"Read data for LDA from data memory **while** instruction 2 (ADD) is fetched."),
               S("Cycles 3 and 4", text=r"The same overlap happens for ADD and STA. HLT is fetched in cycle 4."),
               S("Result", math=r"4 \text{ cycles}", text=r"Fetches and data accesses overlap, so the time is set by the longer of the two streams (4 fetches)."),
           ],
           check=r"7 \text{ cycles (Von Neumann) against } 4 \text{ cycles (Harvard)}"),
        TIP(r"Always state your assumptions in a counting question: 'one cycle per access, no other delays'. Examiners reward a clear assumption."),
        H("Modified Harvard: the mixed design"),
        T(r"Most modern processors are a **mixture**. Outside the chip there is one main memory (Von Neumann), so programs "
          r"can be loaded as data. Inside the chip there are separate **instruction** and **data caches** (Harvard). The CPU "
          r"fetches from the instruction cache while using the data cache, which removes most of the bottleneck."),
        T(r"Pure Harvard machines suit small **embedded** devices such as the controller in a solar charger, a washing "
          r"machine or a mobile money receipt printer. The program is fixed in read-only memory, a small RAM holds the "
          r"data, and the program can never be overwritten by a bug."),
        KEY("Choosing a model", r"Ask three questions.",
            cards=[
                ["Is the program fixed?", r"Yes: Harvard is safe and fast. No: Von Neumann, because programs must be loaded."],
                ["Is speed critical?", r"Yes: separate paths or separate caches help. If cost matters more: one memory is cheaper."],
                ["Is flexibility needed?", r"Yes: Von Neumann lets memory be shared between code and data as needs change."],
            ]),
        H("Common mistakes"),
        MISTAKE(r"Saying Harvard is always faster", r"It is faster only when the CPU needs an instruction and data in the same cycle. Say 'can be faster' and give the reason."),
        MISTAKE(r"Confusing the bottleneck with a slow CPU", r"The bottleneck is the shared **bus** to memory, not the processor speed. A faster CPU makes it worse because it waits more."),
        QUIZ(r"A farmer's irrigation timer runs one fixed program for years and never loads new software. Which model fits best?",
             ["Von Neumann, so the program can be changed while it runs", "Harvard, with the program in read-only instruction memory",
              "Neither, because it has no memory", "Von Neumann, because Harvard cannot store data"],
             1, r"A fixed program suits Harvard: the program sits in read-only memory and data in a small RAM.",
             hint=r"Does this device ever need to load a new program?",
             feedback=["Changing code while it runs is a feature of general-purpose computers, not needed here.", "",
                       "Every stored-program device has memory.", "Harvard machines store data in the data memory."]),
        QUIZ(r"What does a modified Harvard processor have inside the chip?",
             ["Two separate main memories", "Separate instruction and data caches", "No buses", "Only an ALU"],
             1, r"Separate caches give Harvard-style parallel access, while main memory is still one shared memory.",
             hint=r"Think of the cache, between the CPU and main memory.",
             feedback=["The main memory is still one shared memory outside the chip.", "", "Buses connect every part of the CPU.", "A CPU needs a control unit and registers as well."]),
        H("Practice questions"),
        PQ(r"Give two differences between the Von Neumann and Harvard architectures.",
           r"1. Von Neumann uses one memory for instructions and data; Harvard uses separate instruction and data memories. "
           r"2. Von Neumann uses one set of buses, so transfers take turns; Harvard has separate buses, so an instruction fetch and a data access can happen at the same time."),
        PQ(r"A program of 10 instructions has 6 data reads or writes. Assuming one cycle per memory access, give the memory cycles on (a) a Von Neumann machine and (b) an ideal Harvard machine.",
           r"(a) 10 fetches + 6 data accesses = 16 cycles. (b) The fetches and data accesses overlap, so the time is set by the 10 fetches: 10 cycles. Assumption: one cycle per access, no other delays."),
        PQ(r"Explain what the Von Neumann bottleneck is and one way modern processors reduce it.",
           r"Instructions and data share one bus to memory, so only one can be transferred at a time and the CPU waits. "
           r"Processors reduce it with separate instruction and data caches (modified Harvard), so fetch and data access can overlap, and with fast cache memory that is accessed instead of slow main memory."),
        PQ(r"A company designs a card reader for a bus station, with one fixed program. Choose a machine model and give two reasons.",
           r"Harvard. (1) The program is fixed, so it can sit in read-only instruction memory and cannot be overwritten by a fault. "
           r"(2) Instruction fetch and data access use separate buses, so it is faster and more predictable for a fixed task."),
        SUM(r"A stored-program computer keeps instructions in memory as numbers, so one machine can run any program.",
            r"Von Neumann: one memory and one bus set, so fetches and data accesses take turns.",
            r"Harvard: separate memories and buses, so fetch and data access can overlap.",
            r"Counting accesses: Von Neumann adds fetches and data accesses; ideal Harvard takes the longer stream.",
            r"Modern CPUs are modified Harvard: split caches inside, one main memory outside."),
    ],
))

# ------------------------------------------------------------------ 2 Buses, address space and the memory map
LESSONS.append(lesson(
    module=ARCH, topic=MM,
    title="Buses, address space and the memory map",
    slug="csa-buses-address-space-memory-map",
    minutes=24,
    summary="Work out how many locations an address bus can reach, how fast a data bus can move bytes, and how the top address lines select ROM, RAM or an I/O port in a memory map.",
    objectives=[
        "State the direction and job of the address, data and control buses",
        "Calculate the number of addressable locations from the address bus width, and the reverse",
        "Calculate the best-case transfer rate of a data bus",
        "Use the top address lines to find which memory block an address belongs to",
    ],
    key_concepts=["Address bus", "Data bus", "Control bus", "Address space", "Bus width", "Memory map",
                  "Address decoding", "Memory-mapped I/O"],
    blocks=[
        H("Introduction"),
        T(r"When a mobile money terminal in Bafoussam reads a customer's balance, the CPU has to say *where* the value "
          r"is, then *get* the value, then be told when it has arrived. Three groups of wires, called the **system buses**, "
          r"do those three jobs."),
        T(r"In this lesson you will use the number of wires in a bus to calculate memory sizes and speeds, and see how a "
          r"computer decides whether an address belongs to ROM, RAM or a device."),
        H("The three buses"),
        KEY("What each bus carries", r"All three connect the CPU, memory and input/output.",
            cards=[
                ["Address bus", r"Carries the **address** of the memory location or port. It is **one-way**, from the CPU to memory and devices."],
                ["Data bus", r"Carries the **data or instruction** being moved. It is **two-way**: read (memory to CPU) and write (CPU to memory)."],
                ["Control bus", r"Carries signals such as **memory read**, **memory write**, the **clock**, **interrupt request** and **reset**. Individual lines have their own directions."],
            ]),
        D(r"The **width** of a bus is its number of parallel wires, each carrying one bit. A 16-bit address bus has 16 "
          r"address lines.", title="Bus width"),
        H("Address bus width and address space"),
        D(r"With $n$ address lines the CPU can produce $2^n$ different addresses. This is the **address space**. If each "
          r"address holds one byte, the memory that can be reached is $2^n$ bytes.",
          title="Address space", formula=r"\text{locations} = 2^{n}"),
        CODE("Address lines   Locations              Size (1 byte each)\n"
             "10             1 024                  1 KiB\n"
             "16             65 536                 64 KiB\n"
             "20             1 048 576              1 MiB\n"
             "32             4 294 967 296          4 GiB",
             "text", title="Common address bus widths"),
        EX("Worked example 1: lines needed",
           intro=r"A controller needs to address 6 KiB (6144 bytes) of memory. How many address lines are needed?",
           steps=[
               S("Find the smallest power of 2 that is at least 6144", math=r"2^{12} = 4096 < 6144 \quad 2^{13} = 8192 \ge 6144"),
               S("Answer", text=r"13 address lines are needed. The extra 2048 addresses are unused."),
           ]),
        EX("Worked example 2: memory reached",
           intro=r"A CPU has a 24-bit address bus and each address holds one byte. How much memory can it address?",
           steps=[
               S("Locations", math=r"2^{24} = 16\,777\,216"),
               S("Convert to MiB", math=r"16\,777\,216 \div 1\,048\,576 = 16 \text{ MiB}"),
           ]),
        TIP(r"The address bus width limits the **maximum** memory. A computer can have less memory than that, but never more than the CPU can address directly."),
        H("Data bus width and transfer rate"),
        T(r"The data bus width decides how many bits move at once. A 32-bit data bus moves 4 bytes in one transfer. "
          r"If one transfer happens every clock cycle, the best-case rate is the bytes per transfer times the number of transfers per second."),
        F(r"\text{rate} = \frac{\text{bus width in bits}}{8} \times \text{transfers per second}", title="Best-case transfer rate"),
        EX("Worked example 3: transfer rate",
           intro=r"A 32-bit data bus makes one transfer per cycle at 200 MHz. What is the best-case rate in megabytes per second?",
           steps=[
               S("Bytes per transfer", math=r"32 \div 8 = 4"),
               S("Transfers per second", math=r"200 \times 10^{6}"),
               S("Rate", math=r"4 \times 200 = 800 \text{ MB/s}"),
           ]),
        H("The memory map"),
        T(r"The CPU puts one address on the address bus. Something must decide **which chip** answers. This is "
          r"**address decoding**: the top address lines go into a decoder that picks one block, and the lower lines choose "
          r"a byte inside it. Devices can share the same address space as memory; this is **memory-mapped I/O**."),
        IMG("al-csa-memory-map.svg",
            "A 16-bit address space split into four blocks of 16 KiB chosen by address lines A15 and A14: 00 is ROM at 0000 to 3FFF, 01 is RAM block 1 at 4000 to 7FFF, 10 is RAM block 2 at 8000 to BFFF, and 11 is I/O ports at C000 to FFFF. A 2-to-4 decoder sits between the two address lines and the blocks.",
            caption="Figure 1. The top two address lines select a 16 KiB block; the other 14 lines select a byte inside it."),
        EX("Worked example 4: which block?",
           intro=r"Using the map in Figure 1, which block does address 9A3C (hex) belong to, and what is the offset inside it?",
           steps=[
               S("Write the address in binary", math=r"9A3C_{16} = 1001\,1010\,0011\,1100_2"),
               S("Take the top two bits (A15, A14)", math=r"10", text=r"These select RAM block 2."),
               S("Offset inside the block", math=r"9A3C_{16} - 8000_{16} = 1A3C_{16}"),
           ],
           check=r"8000_{16} + 1A3C_{16} = 9A3C_{16}"),
        H("Common mistakes"),
        MISTAKE(r"Saying the address bus is two-way", r"Only the CPU (or a DMA controller) puts addresses on it. Memory never sends addresses back. The data bus is the two-way one."),
        MISTAKE(r"Doubling when adding one address line, but mixing it up with data lines", r"Each extra **address** line doubles the number of locations. Extra **data** lines make each transfer wider but do not add locations."),
        QUIZ(r"How many locations can a CPU with a 12-bit address bus address?",
             ["12", "144", "4096", "65536"], 2, r"2 to the power 12 is 4096.",
             hint=r"Locations = 2 to the power of the number of address lines.",
             feedback=["That is the number of lines, not the locations.", "That is 12 squared, not 2 to the power 12.", "", "That is 2 to the power 16, for a 16-bit bus."]),
        QUIZ(r"A 64-bit data bus makes 100 million transfers per second. What is the best-case rate?",
             ["800 MB/s", "6400 MB/s", "64 MB/s", "100 MB/s"], 0, r"64 bits is 8 bytes. 8 times 100 million is 800 million bytes per second.",
             hint=r"Convert the bus width to bytes first.",
             feedback=["", "This multiplies bits by the rate and forgets to divide by 8.", "This uses 64 as the byte count of the bus.", "This ignores the bus width."]),
        H("Practice questions"),
        PQ(r"State the direction of each bus and what it carries.",
           r"Address bus: one-way, CPU to memory and devices, carries the address. Data bus: two-way, carries data and instructions. Control bus: carries control signals such as read, write, clock and interrupt, with each line having its own direction."),
        PQ(r"A CPU has a 20-bit address bus. Calculate the number of locations it can address and give the size in MiB if each holds one byte.",
           r"2 to the power 20 = 1 048 576 locations. Each holds one byte, so the size is 1 MiB."),
        PQ(r"A device needs 40 000 addressable bytes. How many address lines are needed?",
           r"2 to the power 15 = 32 768 is too small; 2 to the power 16 = 65 536 is enough. So 16 address lines."),
        PQ(r"In a 16-bit memory map, ROM is selected when A15 A14 = 00 and I/O when A15 A14 = 11. State which is used for the address 2FFF (hex) and for C010 (hex).",
           r"2FFF in binary starts 0010 so A15 A14 = 00: ROM. C010 starts 1100 so A15 A14 = 11: I/O port area."),
        SUM(r"The address bus is one-way and sets how much memory can be reached: 2 to the power n locations for n lines.",
            r"The data bus is two-way and sets how many bits move at once; rate = bytes per transfer times transfers per second.",
            r"The control bus carries read, write, clock, interrupt and reset signals.",
            r"Address decoding uses the top address lines to choose a block of ROM, RAM or I/O; the other lines choose a byte inside it."),
    ],
))

# ------------------------------------------------------------------ 3 CPU components, registers and flags
LESSONS.append(lesson(
    module=ARCH, topic=CPU,
    title="Inside the CPU: ALU, control unit, registers and status flags",
    slug="csa-cpu-components-registers-flags",
    minutes=23,
    summary="Describe the job of the ALU, control unit, clock and each register, work out the status flags after an 8-bit addition, and relate clock speed to instruction rate.",
    objectives=[
        "State the role of the ALU, the control unit and the clock",
        "Distinguish general-purpose from special-purpose registers",
        "Work out the Z, N, C and V flags after an 8-bit addition",
        "Relate clock frequency, cycle time and instructions per second",
    ],
    key_concepts=["ALU", "Control unit", "Clock", "General-purpose register", "Status register",
                  "Zero flag", "Negative flag", "Carry flag", "Overflow flag", "Clock cycle"],
    blocks=[
        H("Introduction"),
        T(r"A phone processor can run billions of tiny steps every second, yet it is built from just a few kinds of part. "
          r"Knowing what each part does lets you explain *why* a program behaves as it does, and it is the base for "
          r"tracing the fetch-decode-execute cycle in the next lesson."),
        H("The main components"),
        KEY("Three parts that work together", r"Each has one clear job.",
            cards=[
                ["ALU (arithmetic logic unit)", r"Does the **arithmetic** (add, subtract), **logic** (AND, OR, NOT) and **shifts**. It also sets the status flags."],
                ["Control unit (CU)", r"**Decodes** the instruction in the CIR and sends **control signals** to the other parts, in the right order."],
                ["Clock", r"Sends a regular pulse. Each step of the CU is timed by it. Speed is in hertz: 1 GHz is one thousand million cycles per second."],
            ]),
        T(r"The CPU also contains the **registers** and, in modern chips, **cache** memory. Registers are the fastest storage "
          r"in the computer, but there are very few of them."),
        H("Registers"),
        D(r"A **general-purpose register** can hold any data the programmer chooses: a number being added, a loop counter, "
          r"an address. A **special-purpose register** has a fixed job in the machine.",
          title="General-purpose and special-purpose registers"),
        KEY("Special-purpose registers", r"The ones you must know.",
            cards=[
                ["PC", r"Program counter: address of the next instruction."],
                ["MAR and MDR", r"Memory address register and memory data register: the link between the CPU and the address and data buses."],
                ["CIR", r"Current instruction register: the instruction being decoded and executed."],
                ["ACC", r"Accumulator: holds the ALU result, or one input to it."],
                ["SP", r"Stack pointer: address of the top of the stack, used for subroutine calls."],
                ["Status register", r"A set of single-bit **flags** that record facts about the last ALU result."],
            ]),
        H("The status flags"),
        D(r"The **status register** holds flags set by the ALU after an operation. A program can test them with a "
          r"conditional jump.",
          title="Status flags",
          note=r"Z = result is zero. N = result is negative (top bit is 1). C = carry out of the top bit. V = signed overflow."),
        T(r"Take an 8-bit ALU. Unsigned values run from 0 to 255; signed (two's complement) values from -128 to 127. "
          r"The **carry** flag detects unsigned overflow; the **overflow** flag detects signed overflow."),
        CODE("Operation          8-bit result   Z N C V\n"
             "200 + 100          0010 1100 (44) 0 0 1 0   carry out: 300 does not fit in 8 bits\n"
             "127 + 1            1000 0000      0 1 0 1   signed overflow: two positives gave a negative\n"
             "255 + 1            0000 0000      1 0 1 0   wraps to zero with a carry out\n"
             "5 - 5              0000 0000      1 0 . .   result is zero\n"
             "3 - 5              1111 1110      0 1 . .   result is -2 in two's complement",
             "text", title="Flags after 8-bit operations (dots: not used here)"),
        EX("Worked example 1: flags after an addition",
           intro=r"An 8-bit ALU adds 200 and 100. Give the result and the Z, N, C and V flags.",
           steps=[
               S("Add in binary", math=r"1100\,1000 + 0110\,0100 = 1\,0010\,1100"),
               S("Keep 8 bits", text=r"The result is 0010 1100, which is 44. The ninth bit is lost as the carry out."),
               S("Set the flags", text=r"Z = 0 (not zero). N = 0 (top bit is 0). C = 1 (carry out). V = 0: as signed numbers, 200 is -56 and 100 is 100, and -56 + 100 = 44 fits, so no signed overflow."),
           ],
           check=r"200 + 100 = 300 = 256 + 44"),
        EX("Worked example 2: using a flag",
           intro=r"A loop must stop when a counter reaches zero. Which flag does a conditional jump test, and why?",
           steps=[
               S("The program subtracts 1 from the counter", text=r"Each SUB sets the flags from the new value."),
               S("Test the Zero flag", text=r"When the counter becomes 0, Z = 1. A jump-if-zero instruction then leaves the loop."),
           ]),
        H("Clock speed and instruction rate"),
        T(r"The **clock cycle time** is the reciprocal of the frequency. If instructions need several cycles each, "
          r"the instruction rate is the frequency divided by the cycles per instruction."),
        F(r"T = \frac{1}{f} \qquad \text{instructions per second} = \frac{f}{\text{cycles per instruction}}"),
        EX("Worked example 3: instruction rate",
           intro=r"A CPU runs at 2.5 GHz. Give the cycle time, and the number of instructions per second if each takes 4 cycles.",
           steps=[
               S("Cycle time", math=r"T = 1 \div (2.5 \times 10^{9}) = 0.4 \text{ ns}"),
               S("Instruction rate", math=r"2.5 \times 10^{9} \div 4 = 625 \times 10^{6} \text{ per second}"),
           ]),
        TIP(r"A higher clock speed is not the only measure of speed. More cores, larger cache, pipelining and a wider word also raise performance."),
        H("Common mistakes"),
        MISTAKE(r"Mixing up the carry and overflow flags", r"Carry is for **unsigned** numbers: a bit fell off the top. Overflow is for **signed** numbers: the sign of the result is wrong. They can differ, as 127 + 1 shows."),
        MISTAKE(r"Saying the control unit does the calculations", r"The ALU does the calculations. The control unit only decodes the instruction and tells the other parts what to do."),
        QUIZ(r"Which register tells the CPU where the next instruction is?",
             ["MAR", "ACC", "PC", "CIR"], 2, r"The program counter holds the address of the next instruction to fetch.",
             hint=r"Which register is incremented during the fetch?",
             feedback=["The MAR holds the address currently being read or written, not the next instruction.", "The ACC holds a result.", "", "The CIR holds the instruction already fetched."]),
        QUIZ(r"An 8-bit subtraction gives 0000 0000. Which flag is set?",
             ["Zero (Z)", "Negative (N)", "Overflow (V)", "Clock"], 0, r"A result of zero sets the Z flag.",
             hint=r"What does the result equal?",
             feedback=["", "N is set only when the top bit is 1.", "The result is exact, so no signed overflow.", "The clock is not a flag."]),
        H("Practice questions"),
        PQ(r"State the purpose of the ALU and of the control unit.",
           r"The ALU performs arithmetic, logic and shift operations and sets the status flags. The control unit decodes instructions and sends control signals that make the other parts carry them out, in the right order and timed by the clock."),
        PQ(r"An 8-bit ALU adds 255 and 1. State the result and the Z, N, C and V flags.",
           r"255 + 1 = 256, which in 8 bits is 0000 0000. Z = 1 (zero), N = 0, C = 1 (carry out), V = 0 (as signed: -1 + 1 = 0, no overflow)."),
        PQ(r"Explain the difference between the carry flag and the overflow flag.",
           r"The carry flag shows that an unsigned result did not fit: a bit was carried out of the top. The overflow flag shows that a signed (two's complement) result has the wrong sign because it did not fit, for example adding two positive numbers and getting a negative one."),
        PQ(r"A CPU runs at 1.6 GHz and each instruction needs 4 cycles on average. How many instructions does it run each second?",
           r"1.6 x 10^9 divided by 4 = 4 x 10^8, so 400 million instructions per second."),
        SUM(r"The ALU calculates; the control unit decodes and directs; the clock times every step.",
            r"General-purpose registers hold programmer data; special-purpose ones (PC, MAR, MDR, CIR, ACC, SP, status) have fixed jobs.",
            r"The status flags Z, N, C and V record facts about the last ALU result and are tested by conditional jumps.",
            r"Carry is unsigned overflow; overflow is signed overflow.",
            r"Cycle time is 1 divided by frequency; instructions per second is frequency divided by cycles per instruction."),
    ],
))

# ------------------------------------------------------------------ 4 Tracing the fetch-decode-execute cycle
FDE_TRACE = """Step                PC   MAR  MDR      CIR      ACC
1 MAR<-PC           10   10   -        -        0
2 MDR<-[MAR] PC+1   11   10   LDA 30   -        0
3 CIR<-MDR          11   10   LDA 30   LDA 30   0
4 LDA 30            11   30   5        LDA 30   5
1 MAR<-PC           11   11   5        LDA 30   5
2 MDR<-[MAR] PC+1   12   11   ADD 31   LDA 30   5
3 CIR<-MDR          12   11   ADD 31   ADD 31   5
4 ADD 31            12   31   7        ADD 31   12"""

FDE_PROGRAM = """Address  Contents
10       LDA 30     ; ACC <- memory[30]
11       ADD 31     ; ACC <- ACC + memory[31]
12       SUB 32     ; ACC <- ACC - memory[32]
13       STA 33     ; memory[33] <- ACC
14       HLT        ; stop
30       5
31       7
32       3
33       0"""

FDE_LOOP = """Address  Contents
20       LDA 42     ; load the running total
21       ADD 43     ; add the step
22       STA 42     ; save the total
23       LDA 40     ; load the counter
24       SUB 41     ; counter - 1
25       STA 40     ; save the counter
26       BRZ 28     ; if ACC = 0 then PC <- 28
27       JMP 20     ; PC <- 20
28       HLT
40       3          ; counter
41       1          ; the number one
42       0          ; total
43       4          ; step"""

FDE_LOOP_TRACE = """Instruction   ACC after   Memory changed      PC after
LDA 42        0                           21
ADD 43        4                           22
STA 42        4           [42] = 4        23
LDA 40        3                           24
SUB 41        2                           25
STA 40        2           [40] = 2        26
BRZ 28        2           (ACC not 0)     27
JMP 20        2                           20
... pass 2: [42] = 8, [40] = 1
... pass 3: [42] = 12, [40] = 0, BRZ jumps to 28
HLT"""

LESSONS.append(lesson(
    module=ARCH, topic=CPU,
    title="Tracing the fetch-decode-execute cycle step by step",
    slug="csa-fde-trace-programs",
    minutes=25,
    summary="Trace every register through the fetch-decode-execute cycle for a straight-line program and for a loop with a conditional jump, and count the instructions executed.",
    objectives=[
        "Write the four register transfers of the fetch and execute stages for LDA, ADD, SUB and STA",
        "Trace PC, MAR, MDR, CIR and ACC for a short program",
        "Show how BRZ and JMP change the PC",
        "Count instructions executed in a loop",
    ],
    key_concepts=["Fetch", "Decode", "Execute", "Register transfer", "Opcode", "Operand",
                  "Conditional jump", "Trace table"],
    blocks=[
        H("Introduction"),
        T(r"Exam questions on the CPU often hand you a tiny program and ask: *what is in each register now?* You answer "
          r"by tracing, one small step at a time. This lesson gives you a method, then two programs to trace: one "
          r"straight-line, one with a loop."),
        T(r"The machine here is an accumulator machine with a simple instruction set. Each instruction is one word with an "
          r"**opcode** (the action) and an **operand** (an address). Memory locations are written in square brackets: "
          r"[30] means the contents of location 30."),
        H("The method"),
        KEY("Four steps for each instruction", r"Do them in this order every time.",
            cards=[
                ["Step 1: MAR <- PC", r"Copy the address of the next instruction into the MAR."],
                ["Step 2: MDR <- [MAR], PC <- PC + 1", r"Read memory into the MDR and add 1 to the PC."],
                ["Step 3: CIR <- MDR", r"Copy the instruction into the CIR. Decode: split it into opcode and operand."],
                ["Step 4: Execute", r"Carry out the opcode. LDA, ADD and SUB set MAR to the operand and read data; STA writes ACC to memory; JMP and BRZ may load the PC."],
            ]),
        TIP(r"The PC is increased in step 2, **before** the instruction is executed. A jump then overwrites it. This is why a trace shows PC one higher than the address of the instruction being executed."),
        T(r"The instruction set used in this lesson:"),
        CODE("LDA n   ACC <- [n]            ADD n   ACC <- ACC + [n]\n"
             "SUB n   ACC <- ACC - [n]      STA n   [n] <- ACC\n"
             "JMP n   PC <- n               BRZ n   if ACC = 0 then PC <- n\n"
             "HLT     stop",
             "text", title="Instruction set"),
        H("Trace 1: a straight-line program"),
        CODE(FDE_PROGRAM, "text", title="Program 1"),
        T(r"The first two instructions are traced below. A dash means the register has not been used yet."),
        CODE(FDE_TRACE, "text", title="Trace of the first two instructions"),
        EX("Worked example 1: finish the trace",
           intro=r"Continue the trace for SUB 32 and STA 33. What are PC, MAR, MDR, CIR and ACC at the end of each, and what is in [33]?",
           steps=[
               S("SUB 32, fetch", text=r"MAR <- 12. MDR <- SUB 32 and PC <- 13. CIR <- SUB 32."),
               S("SUB 32, execute", text=r"MAR <- 32, MDR <- 3, ACC <- 12 - 3 = 9. PC stays 13."),
               S("STA 33, fetch", text=r"MAR <- 13. MDR <- STA 33 and PC <- 14. CIR <- STA 33."),
               S("STA 33, execute", text=r"MAR <- 33, MDR <- 9 (copied from ACC), and [33] <- 9. PC = 14, CIR = STA 33, ACC = 9."),
           ],
           check=r"5 + 7 - 3 = 9"),
        H("Trace 2: a loop with a conditional jump"),
        T(r"Program 2 adds the step (4) to a total, three times. The counter at [40] counts down; BRZ leaves the loop when the counter reaches zero."),
        CODE(FDE_LOOP, "text", title="Program 2"),
        CODE(FDE_LOOP_TRACE, "text", title="Trace of the first pass, then a summary"),
        EX("Worked example 2: how many instructions run?",
           intro=r"How many instructions are executed by Program 2, counting HLT? What is the final value of [42]?",
           steps=[
               S("One full pass", text=r"LDA, ADD, STA, LDA, SUB, STA, BRZ, JMP is 8 instructions."),
               S("Passes 1 and 2", text=r"BRZ does not jump (ACC is 2, then 1), so JMP runs: 8 instructions each, 16 in all."),
               S("Pass 3", text=r"ACC becomes 0, so BRZ jumps to 28 and JMP is skipped: 7 instructions, then HLT is 1 more."),
               S("Total", math=r"16 + 7 + 1 = 24 \text{ instructions}"),
               S("Final total", math=r"3 \times 4 = 12", text=r"So [42] = 12 and [40] = 0."),
           ]),
        H("Common mistakes"),
        MISTAKE(r"Forgetting the PC increment", r"Write the new PC in step 2 of **every** instruction, even when the instruction does not use it. Only jumps change it afterwards."),
        MISTAKE(r"Loading the PC when BRZ is not taken", r"BRZ copies its operand into the PC only if ACC is 0. Otherwise the PC stays as it was after the increment."),
        MISTAKE(r"Writing the address as the data", r"For LDA 30 the MDR gets the **contents** of location 30 (here 5), not the number 30. The 30 goes into the MAR."),
        QUIZ(r"During the fetch of the instruction at address 12, what are the MAR and the PC after step 2?",
             ["MAR = 12 and PC = 12", "MAR = 12 and PC = 13", "MAR = 13 and PC = 13", "MAR = 11 and PC = 12"],
             1, r"Step 1 copies 12 into the MAR; step 2 adds 1 to the PC, giving 13.",
             hint=r"Step 1 copies the PC into the MAR. Step 2 increments the PC.",
             feedback=["The PC is incremented in step 2, so it is no longer 12.", "", "The MAR holds the old PC value, not the new one.", "The MAR holds the address being fetched, 12."]),
        QUIZ(r"In Program 2, ACC is 0 after SUB 41 and STA 40. What does BRZ 28 do?",
             ["Nothing; the PC stays 27", "Sets PC to 28", "Sets ACC to 28", "Stops the clock"],
             1, r"ACC is 0 so the branch is taken and the PC is set to its operand, 28.",
             hint=r"BRZ means branch if zero.",
             feedback=["That happens only when ACC is not zero.", "", "BRZ never changes the ACC.", "Only HLT stops the program."]),
        H("Practice questions"),
        PQ(r"Write the register transfers for the fetch stage, in order.",
           r"MAR <- PC. Then MDR <- [MAR] and PC <- PC + 1. Then CIR <- MDR. The control unit then decodes the CIR into opcode and operand."),
        PQ(r"Program 1 is changed so that location 31 holds 10. Trace the program and give the final contents of ACC and [33].",
           r"LDA 30: ACC = 5. ADD 31: ACC = 5 + 10 = 15. SUB 32: ACC = 15 - 3 = 12. STA 33: [33] = 12. Final ACC = 12 and [33] = 12."),
        PQ(r"In Program 2 the counter at [40] starts at 5 and the step at [43] is 3. State the final value of [42] and how many instructions are executed.",
           r"Five passes add 3 each time: [42] = 15. Each of the first four passes runs 8 instructions (32). The last pass runs 7 and then HLT (8). Total 40 instructions."),
        PQ(r"Explain how a JMP instruction changes the normal fetch-decode-execute cycle.",
           r"During fetch the PC is incremented to point at the next instruction. A JMP copies its operand into the PC in the execute stage, replacing that value. The next fetch therefore begins at the new address instead of the next one in sequence."),
        SUM(r"Every instruction: MAR <- PC; MDR <- [MAR] and PC + 1; CIR <- MDR; then execute.",
            r"The PC already points at the next instruction before execution; only jumps change it afterwards.",
            r"LDA, ADD and SUB read the data at the operand address; STA writes the ACC to memory.",
            r"BRZ loads the PC only if ACC = 0; JMP always loads it.",
            r"In a loop, count instructions pass by pass; the last pass is shorter when BRZ exits."),
    ],
))

# ------------------------------------------------------------------ 5 Instruction format and addressing modes
LESSONS.append(lesson(
    module=ARCH, topic=CPU,
    title="Instruction format and addressing modes",
    slug="csa-instruction-format-addressing-modes",
    minutes=24,
    summary="Split an instruction into opcode, mode and operand, work out how many bits each field needs, and find the value loaded by immediate, direct, indirect and indexed addressing.",
    objectives=[
        "Describe the fields of a machine instruction and how field widths limit the instruction set and memory reached",
        "Evaluate immediate, direct, indirect and indexed addressing for a given memory",
        "Choose a suitable addressing mode for a task such as stepping through an array",
        "Calculate the number of addresses reachable from the operand field",
    ],
    key_concepts=["Opcode", "Operand", "Instruction format", "Immediate addressing", "Direct addressing",
                  "Indirect addressing", "Indexed addressing", "Index register"],
    blocks=[
        H("Introduction"),
        T(r"A bank clerk in Limbe looks up the balance of account number 40 and gets 7000. Another time, she is told "
          r"'go to the drawer whose number is written on card 42'. The first is a direct lookup; the second goes through one "
          r"extra step. The CPU faces the same choice every time an instruction names its data, and the rule it follows is the "
          r"**addressing mode**."),
        H("Instruction format"),
        D(r"An **instruction** is a binary word split into fields: the **opcode** says which operation to perform, an optional "
          r"**mode** field says how to interpret the operand, and the **operand** is an address or a value.",
          title="Instruction format"),
        CODE("16-bit instruction\n"
             "+--------+------+---------------+\n"
             "| opcode | mode |    operand    |\n"
             "| 5 bits | 2 b  |    9 bits     |\n"
             "+--------+------+---------------+",
             "text", title="An example format"),
        T(r"The field widths set limits. In this format, 5 opcode bits give 2 to the power 5 = 32 different operations. "
          r"2 mode bits give 4 modes. 9 operand bits can name 2 to the power 9 = 512 different addresses."),
        EX("Worked example 1: widths",
           intro=r"A 16-bit instruction has a 4-bit opcode and 2 mode bits. How many operations does it allow, and how many memory locations can the operand address directly?",
           steps=[
               S("Operations", math=r"2^4 = 16"),
               S("Operand bits", math=r"16 - 4 - 2 = 10"),
               S("Locations reachable", math=r"2^{10} = 1024"),
           ]),
        H("The four modes"),
        KEY("Where does the data come from?", r"Use the same memory in each case: [40] = 7, [41] = 12, [42] = 44, [43] = 25, [44] = 9, and index register IX = 2.",
            cards=[
                ["Immediate", r"The operand **is** the data. LDA #40 loads the number 40. No memory read for the data."],
                ["Direct", r"The operand is the **address** of the data. LDA 40 loads [40] = 7."],
                ["Indirect", r"The operand is the address of a **location that holds the address**. LDA (42) reads [42] = 44, then loads [44] = 9."],
                ["Indexed", r"The address is the operand **plus the index register**. LDA 40,X uses address 40 + 2 = 42 and loads [42] = 44."],
            ]),
        CODE("Instruction   Effective address   ACC loaded\n"
             "LDA #40       none (value = 40)   40\n"
             "LDA 40        40                  7\n"
             "LDA (42)      [42] = 44           9\n"
             "LDA 40,X      40 + IX = 42        44",
             "text", title="Results with [40..44] = 7, 12, 44, 25, 9 and IX = 2"),
        D(r"The **effective address** is the final memory address from which the data is read or to which it is written, "
          r"after the addressing mode has been applied.", title="Effective address"),
        EX("Worked example 2: indirect addressing",
           intro=r"Using the memory above, find the value loaded by LDA (42).",
           steps=[
               S("Read the pointer", math=r"[42] = 44", text=r"Location 42 does not hold the data: it holds an address."),
               S("Read the data", math=r"[44] = 9"),
               S("Result", text=r"ACC = 9. Two memory reads were needed for the data."),
           ]),
        H("When to use each mode"),
        T(r"**Immediate** is best for constants, such as the number 1 to subtract in a counter. **Direct** is best for a single "
          r"named variable. **Indirect** suits a *pointer*: the address of a value that changes, or a table of addresses. "
          r"**Indexed** suits **arrays**: the operand is the start of the array and the index register counts through it."),
        EX("Worked example 3: summing an array",
           intro=r"An array of five numbers 3, 8, 2, 6, 1 is stored at addresses 100 to 104. A loop uses LDA 100,X and ADD to total it, with IX going 0, 1, 2, 3, 4. Show the running total.",
           steps=[
               S("IX = 0: address 100", text=r"Value 3. Total 3."),
               S("IX = 1: address 101", text=r"Value 8. Total 3 + 8 = 11."),
               S("IX = 2 and 3: addresses 102 and 103", text=r"Values 2 and 6. Totals 13 and 19."),
               S("IX = 4: address 104", text=r"Value 1. Total 20."),
           ],
           check=r"3 + 8 + 2 + 6 + 1 = 20"),
        TIP(r"In a question, write down the **effective address** first, then the value stored there. Do not confuse the two."),
        H("Common mistakes"),
        MISTAKE(r"Loading the operand when the mode is direct", r"LDA 40 loads the contents of location 40, not the number 40. Only the immediate form LDA #40 loads 40 itself."),
        MISTAKE(r"Stopping after one read in indirect addressing", r"Indirect needs two reads: first the pointer, then the data it points to."),
        MISTAKE(r"Adding the index to the data", r"The index register is added to the **address**, not to the value that is loaded."),
        QUIZ(r"With [40] = 7, [41] = 12, [42] = 44 and [44] = 9, what does LDA (42) put in the ACC?",
             ["42", "44", "9", "7"], 2, r"[42] = 44 is a pointer; [44] = 9 is the data.",
             hint=r"Read location 42, treat its contents as an address, then read that location.",
             feedback=["42 is the operand itself, not any stored value.", "44 is the pointer; one more read is needed.", "", "7 is [40], reached by direct LDA 40."]),
        QUIZ(r"Which mode is most suitable for stepping through the elements of an array?",
             ["Immediate", "Direct", "Indexed", "None, arrays need a different CPU"], 2,
             r"Indexed addressing adds an index register to a base address, so changing the register moves along the array.",
             hint=r"Which mode lets you change the address without changing the instruction?",
             feedback=["Immediate holds a constant, not an element.", "Direct names one fixed address.", "", "Arrays are handled by ordinary instructions."]),
        H("Practice questions"),
        PQ(r"State the purpose of the opcode and of the operand in a machine instruction.",
           r"The opcode specifies the operation to be performed (for example load, add or jump). The operand gives the data or the address of the data to be used, interpreted according to the addressing mode."),
        PQ(r"Memory holds [60] = 5, [61] = 20, [62] = 61 and IX = 1. Give the value loaded by (a) LDA #60 (b) LDA 60 (c) LDA (62) (d) LDA 60,X.",
           r"(a) 60: the operand itself. (b) 5: direct, the contents of location 60. (c) [62] = 61, then [61] = 20, so 20. (d) address 60 + 1 = 61, so [61] = 20."),
        PQ(r"A 16-bit instruction uses 6 opcode bits and 2 mode bits. How many different operations can it have, and how many addresses can the operand name?",
           r"2 to the power 6 = 64 operations. Operand bits = 16 - 6 - 2 = 8, so 2 to the power 8 = 256 addresses."),
        PQ(r"Explain why indexed addressing is useful for processing an array.",
           r"The operand holds the address of the first element and the index register holds the offset. Adding 1 to the index register moves to the next element, so one short loop can process every element without changing the instruction."),
        SUM(r"An instruction has an opcode, usually a mode field, and an operand; the field widths limit the operations and addresses.",
            r"Immediate: the operand is the data. Direct: the operand is the address.",
            r"Indirect: the operand points to a location that holds the address. Indexed: operand plus index register gives the address.",
            r"Always find the effective address first, then the value stored there."),
    ],
))

# ------------------------------------------------------------------ 6 Pipelining calculations and hazards
LESSONS.append(lesson(
    module=ARCH, topic=CPU,
    title="Pipelining: timing diagrams, speed-up and hazards",
    slug="csa-pipelining-timing-hazards",
    minutes=24,
    summary="Draw and read pipeline timing diagrams, calculate cycles and speed-up with and without stalls, and explain structural, data and control hazards and how they are reduced.",
    objectives=[
        "Draw a timing diagram for a k-stage pipeline and read the cycle each stage happens in",
        "Calculate cycles, execution time and speed-up for n instructions",
        "Add stall cycles for data and branch hazards",
        "Describe three kinds of hazard and one remedy for each",
    ],
    key_concepts=["Pipeline stage", "Throughput", "Latency", "Speed-up", "Stall", "Data hazard",
                  "Control hazard", "Structural hazard", "Branch prediction", "Forwarding"],
    blocks=[
        H("Introduction"),
        T(r"Think of a small bakery in Bafoussam. One person kneads, a second shapes, a third bakes. While loaf 1 is baking, "
          r"loaf 2 is being shaped and loaf 3 is being kneaded. Each loaf still takes the same total time, but a finished "
          r"loaf comes out far more often. **Pipelining** does the same for instructions."),
        T(r"The overview lesson introduced pipelining. Here you will draw timing diagrams, do the calculations that "
          r"examiners ask for, and add the cost of **hazards**."),
        H("Reading a timing diagram"),
        IMG("al-csa-pipeline-gantt.svg",
            "A timing diagram with four stages Fetch, Decode, Execute and Write back. Instruction 1 uses cycles 1 to 4, instruction 2 uses cycles 2 to 5, and so on, so instruction 5 uses cycles 5 to 8. Eight cycles in total for five instructions.",
            caption="Figure 1. Five instructions in a 4-stage pipeline finish in 8 cycles. Without a pipeline they would need 20."),
        D(r"With $k$ stages, each taking one cycle, and $n$ instructions, the first instruction needs $k$ cycles to "
          r"complete. After that one instruction finishes every cycle.",
          title="Pipeline cycles", formula=r"\text{cycles} = k + (n - 1)",
          note=r"Without a pipeline: $k \times n$ cycles."),
        D(r"The **speed-up** is the time without the pipeline divided by the time with it.",
          title="Speed-up", formula=r"\text{speed-up} = \frac{k \times n}{k + (n - 1)}"),
        EX("Worked example 1: cycles and speed-up",
           intro=r"A 5-stage pipeline runs 100 instructions. Each stage takes one cycle. Find the cycles with and without a pipeline, and the speed-up.",
           steps=[
               S("With the pipeline", math=r"5 + (100 - 1) = 104 \text{ cycles}"),
               S("Without", math=r"5 \times 100 = 500 \text{ cycles}"),
               S("Speed-up", math=r"500 \div 104 \approx 4.81", text=r"As $n$ grows the speed-up approaches the number of stages, 5."),
           ]),
        H("Time, throughput and latency"),
        T(r"A pipeline raises **throughput** (instructions finished per second). It does **not** shorten the **latency** of "
          r"one instruction, which is still the time for all its stages."),
        EX("Worked example 2: execution time",
           intro=r"An instruction takes 10 ns in total without a pipeline. A 5-stage pipeline has a 2 ns clock cycle. How long do 1000 instructions take with and without the pipeline?",
           steps=[
               S("Without", math=r"1000 \times 10 = 10\,000 \text{ ns}"),
               S("With: cycles", math=r"5 + 999 = 1004 \text{ cycles}"),
               S("With: time", math=r"1004 \times 2 = 2008 \text{ ns}"),
               S("Speed-up", math=r"10\,000 \div 2008 \approx 4.98"),
               S("Latency of one instruction", text=r"Still 5 x 2 = 10 ns: pipelining raises throughput, not the speed of one instruction."),
           ]),
        H("Hazards"),
        D(r"A **hazard** is a situation that stops the next instruction from entering its stage in the next cycle. The "
          r"pipeline must **stall**: wait for one or more cycles, doing nothing useful.",
          title="Pipeline hazard"),
        KEY("Three kinds of hazard", r"Know each cause and one remedy.",
            cards=[
                ["Structural", r"Two instructions need the **same hardware** in the same cycle, for example one memory port for an instruction fetch and a data access. **Remedy:** duplicate the resource (for example split caches)."],
                ["Data", r"An instruction needs a result that an earlier instruction has not produced yet. **Remedy:** stall, **forwarding** the result straight from the ALU, or reorder the instructions."],
                ["Control", r"A branch changes the PC, so instructions fetched after it may be wrong and are **flushed**. **Remedy:** **branch prediction**: guess the outcome and fetch from the guessed path."],
            ]),
        EX("Worked example 3: cost of branches",
           intro=r"The same 5-stage pipeline runs 100 instructions, but 20 of them are taken branches. Each taken branch causes 2 stall cycles. Find the total cycles and the new speed-up against 500 cycles.",
           steps=[
               S("Ideal cycles", math=r"5 + 99 = 104"),
               S("Stall cycles", math=r"20 \times 2 = 40"),
               S("Total", math=r"104 + 40 = 144 \text{ cycles}"),
               S("Speed-up", math=r"500 \div 144 \approx 3.47"),
           ],
           check=r"4.81 \text{ without hazards, falling to } 3.47"),
        TIP(r"Always say what you assumed about stalls. 'Each taken branch costs 2 cycles' is an assumption given in the question: use it exactly."),
        H("Common mistakes"),
        MISTAKE(r"Using n times k for the pipelined time", r"That is the time **without** a pipeline. With a pipeline, use k + (n - 1)."),
        MISTAKE(r"Saying pipelining makes each instruction faster", r"Each instruction still takes k cycles. The pipeline raises **throughput**."),
        MISTAKE(r"Adding stalls to the speed-up instead of to the cycles", r"Add the stall cycles to the pipelined cycle count, then divide."),
        QUIZ(r"A 4-stage pipeline runs 10 instructions with no hazards, one cycle per stage. How many cycles does it need?",
             ["40", "14", "13", "10"], 2, r"4 + (10 - 1) = 13 cycles.",
             hint=r"Use k + (n - 1).",
             feedback=["40 is k times n, the time without a pipeline.", "That is 4 + 10, forgetting that the first instruction already counts one of the 10.", "", "That ignores the time to fill the pipeline."]),
        QUIZ(r"Which hazard is caused by a conditional branch?",
             ["Structural hazard", "Data hazard", "Control hazard", "No hazard"], 2,
             r"A branch changes the PC, so the following fetched instructions may be wrong: a control hazard.",
             hint=r"Which hazard involves the program counter?",
             feedback=["That needs two instructions to use the same hardware at once.", "That needs a result that is not yet ready.", "", "Branches do create hazards."]),
        H("Practice questions"),
        PQ(r"A 6-stage pipeline runs 50 instructions with one cycle per stage and no hazards. Calculate the cycles with and without the pipeline.",
           r"With: 6 + 49 = 55 cycles. Without: 6 x 50 = 300 cycles. Speed-up = 300 / 55 which is about 5.45."),
        PQ(r"A 4-stage pipeline runs 10 instructions. Three taken branches each cause 2 stall cycles. Find the total cycles and compare with no pipeline (40 cycles).",
           r"Ideal: 4 + 9 = 13. Stalls: 3 x 2 = 6. Total 19 cycles, against 40 without a pipeline."),
        PQ(r"Explain what a data hazard is and give one way to reduce it.",
           r"A data hazard happens when an instruction needs a value that an earlier instruction in the pipeline has not yet produced, so it must wait (stall). It can be reduced by forwarding the result from the ALU straight to the next instruction, or by reordering the instructions so independent ones fill the gap."),
        PQ(r"Explain why pipelining does not reduce the time taken by a single instruction but does increase throughput.",
           r"One instruction still passes through all the stages, so its latency is the number of stages times the cycle time. Because several instructions are in different stages at once, one finishes every cycle once the pipeline is full, so more instructions are completed per second."),
        SUM(r"With k stages and n instructions: pipelined cycles = k + (n - 1); without = k x n.",
            r"Speed-up approaches k as n grows, but pipelining raises throughput, not single-instruction latency.",
            r"Hazards force stalls: structural (shared hardware), data (result not ready), control (branches).",
            r"Remedies: duplicate resources, forwarding or reordering, and branch prediction.",
            r"Add stall cycles to the pipelined count before working out the speed-up."),
    ],
))

# ------------------------------------------------------------------ 7 Half and full adders
LESSONS.append(lesson(
    module=LOGIC, topic=COMB,
    title="Half adders and full adders: building binary addition from gates",
    slug="csa-half-full-adders",
    minutes=22,
    summary="Derive the half adder and full adder from their truth tables, build the full adder from two half adders and an OR gate, and use it to add three bits.",
    objectives=[
        "Write the truth tables of a half adder and a full adder",
        "Give the Boolean expressions for sum and carry",
        "Draw a full adder from two half adders and an OR gate",
        "Trace bit values through the circuit for a given input",
    ],
    key_concepts=["Combinational circuit", "Half adder", "Full adder", "Sum", "Carry", "XOR gate"],
    blocks=[
        H("Introduction"),
        T(r"When a phone adds 1 CFA franc to a balance, the ALU is doing binary addition with logic gates. The simplest circuits "
          r"that add are the **half adder** and the **full adder**. They are **combinational circuits**: the outputs depend only "
          r"on the inputs *now*, with no memory of earlier inputs."),
        T(r"Notation in this lesson: A AND B is written AB; A OR B is written A + B; NOT A is written A'; and XOR is written in words."),
        H("The half adder"),
        D(r"A **half adder** adds two bits, A and B. It has two outputs: the **sum** S and the **carry** C.",
          title="Half adder"),
        CODE("A  B | C  S\n"
             "0  0 | 0  0\n"
             "0  1 | 0  1\n"
             "1  0 | 0  1\n"
             "1  1 | 1  0     (1 + 1 = 10 in binary)",
             "text", title="Half adder truth table"),
        T(r"Reading the columns: S is 1 when exactly one input is 1, so **S = A XOR B**. C is 1 only when both are 1, so **C = A AND B**. "
          r"A half adder is therefore **one XOR gate and one AND gate**."),
        T(r"A half adder cannot be chained: it has no input for a carry that arrives from the column to its right. For that we need a full adder."),
        H("The full adder"),
        D(r"A **full adder** adds three bits: A, B and a **carry-in** Cin. It produces a sum S and a **carry-out** Cout.",
          title="Full adder"),
        CODE("A  B  Cin | Cout  S\n"
             "0  0  0   | 0     0\n"
             "0  0  1   | 0     1\n"
             "0  1  0   | 0     1\n"
             "0  1  1   | 1     0\n"
             "1  0  0   | 0     1\n"
             "1  0  1   | 1     0\n"
             "1  1  0   | 1     0\n"
             "1  1  1   | 1     1",
             "text", title="Full adder truth table"),
        T(r"Two patterns help. **S is 1 when an odd number of inputs are 1**, so S = A XOR B XOR Cin. **Cout is 1 when two or more inputs are 1**."),
        KEY("Expressions for the full adder", r"The two equal ways to write Cout.",
            cards=[
                ["Sum", r"S = A XOR B XOR Cin"],
                ["Carry-out, from two half adders", r"Cout = AB + (A XOR B)Cin"],
                ["Carry-out, majority form", r"Cout = AB + ACin + BCin"],
            ]),
        H("Building it from two half adders"),
        IMG("al-csa-full-adder.svg",
            "A full adder drawn as two half adders and an OR gate. Half adder 1 takes A and B and gives S1 and C1. Half adder 2 takes S1 and Cin and gives the Sum and C2. An OR gate combines C1 and C2 to give Cout.",
            caption="Figure 1. A full adder is two half adders and one OR gate."),
        T(r"Half adder 1 adds A and B. Half adder 2 adds that sum S1 to the carry-in. A carry can come from either half adder, "
          r"never from both at once, so an OR gate combines C1 and C2."),
        EX("Worked example 1: trace 1 + 1 + 1",
           intro=r"Find S and Cout for A = 1, B = 1 and Cin = 1 using the two-half-adder circuit.",
           steps=[
               S("Half adder 1", math=r"S1 = 1 \text{ XOR } 1 = 0, \quad C1 = 1 \text{ AND } 1 = 1"),
               S("Half adder 2", math=r"S = 0 \text{ XOR } 1 = 1, \quad C2 = 0 \text{ AND } 1 = 0"),
               S("OR gate", math=r"C_{out} = 1 \text{ OR } 0 = 1"),
               S("Read the result", text=r"Cout S = 11, which is 3 in binary: 1 + 1 + 1 = 3."),
           ],
           check=r"1 + 1 + 1 = 3 = 11_2"),
        EX("Worked example 2: trace 0 + 1 + 1",
           intro=r"Find S and Cout for A = 0, B = 1, Cin = 1.",
           steps=[
               S("Half adder 1", math=r"S1 = 0 \text{ XOR } 1 = 1, \quad C1 = 0"),
               S("Half adder 2", math=r"S = 1 \text{ XOR } 1 = 0, \quad C2 = 1 \text{ AND } 1 = 1"),
               S("OR gate", math=r"C_{out} = 0 \text{ OR } 1 = 1"),
               S("Result", text=r"Cout S = 10, which is 2: 0 + 1 + 1 = 2."),
           ]),
        TIP(r"Check any trace by adding the three input bits as ordinary numbers. The two output bits Cout S must be that total in binary."),
        T(r"Gate count: a half adder needs 2 gates; a full adder needs 2 XOR, 2 AND and 1 OR, which is 5 gates."),
        H("Common mistakes"),
        MISTAKE(r"Using OR instead of XOR for the sum", r"OR gives 1 for 1 + 1, but the sum bit of 1 + 1 is 0 with a carry. The sum is XOR."),
        MISTAKE(r"Forgetting the carry-in", r"A half adder has no Cin. Only a full adder can take a carry from the previous column."),
        MISTAKE(r"Using AND instead of OR to combine the carries", r"A carry is produced if **either** half adder makes one, so the final gate is OR."),
        QUIZ(r"In a half adder, which gate produces the carry output?",
             ["XOR", "AND", "OR", "NOT"], 1, r"The carry is 1 only when both inputs are 1: an AND gate.",
             hint=r"When is the carry 1 in the table?",
             feedback=["XOR gives the sum.", "", "OR would give a carry for 0 + 1.", "NOT has one input."]),
        QUIZ(r"A full adder has A = 1, B = 0 and Cin = 1. What are Cout and S?",
             ["Cout = 0, S = 0", "Cout = 1, S = 0", "Cout = 0, S = 1", "Cout = 1, S = 1"], 1,
             r"1 + 0 + 1 = 2, written 10 in binary: Cout = 1 and S = 0.",
             hint=r"Add the three bits as ordinary numbers.",
             feedback=["The total is 2, so the carry cannot be 0.", "", "S = 1 would mean an odd number of 1s; there are two.", "That is the result for three 1s."]),
        H("Practice questions"),
        PQ(r"Complete the half adder truth table for A = 1, B = 1 and give the expressions for S and C.",
           r"A = 1, B = 1 gives C = 1 and S = 0. S = A XOR B. C = A AND B."),
        PQ(r"State the values of Cout and S in a full adder when A = 1, B = 1 and Cin = 0, and explain how the two half adders give this.",
           r"Cout = 1 and S = 0 (1 + 1 + 0 = 2 = 10). Half adder 1: S1 = 0, C1 = 1. Half adder 2: S = 0 XOR 0 = 0, C2 = 0. Cout = C1 OR C2 = 1."),
        PQ(r"Explain why a full adder is needed to add the second and later columns of a binary addition.",
           r"These columns may receive a carry from the column to their right, so three bits must be added: the two data bits and the carry-in. A half adder has only two inputs, so it can add only the first column."),
        PQ(r"A full adder is built as two half adders and one more gate. Name the gate and explain its job.",
           r"An OR gate. It combines the carry from the first half adder and the carry from the second. At most one of them is 1, and Cout is 1 if either is 1."),
        SUM(r"Half adder: S = A XOR B, C = A AND B. It adds two bits.",
            r"Full adder: adds A, B and Cin; S = A XOR B XOR Cin; Cout = AB + (A XOR B)Cin.",
            r"A full adder is two half adders plus an OR gate on the two carries.",
            r"Check a trace by adding the input bits as numbers and writing Cout S in binary."),
    ],
))

# ------------------------------------------------------------------ 8 Ripple-carry adders and subtraction
LESSONS.append(lesson(
    module=LOGIC, topic=COMB,
    title="Ripple-carry adders, subtraction and overflow",
    slug="csa-ripple-carry-subtraction-overflow",
    minutes=23,
    summary="Chain full adders into a 4-bit ripple-carry adder, trace the carries, turn the adder into a subtractor with XOR gates, and detect signed overflow.",
    objectives=[
        "Trace carries through a 4-bit ripple-carry adder",
        "Explain why the carry ripples and how it limits speed",
        "Use XOR gates and a carry-in of 1 to make an adder subtract",
        "State when signed overflow occurs and detect it from the carries",
    ],
    key_concepts=["Ripple-carry adder", "Carry propagation delay", "Two's complement subtraction",
                  "Adder-subtractor", "Signed overflow"],
    blocks=[
        H("Introduction"),
        T(r"A phone needs to add 16-bit, 32-bit or 64-bit numbers, but a full adder handles only **one column**. To add whole "
          r"numbers, several full adders are chained. Each one passes its carry to the next, like a pupil passing a note along a row of desks."),
        H("The ripple-carry adder"),
        D(r"A **ripple-carry adder** is a row of full adders. The carry-out of each stage is connected to the carry-in of the "
          r"next stage on the left. The first stage has a carry-in of 0.",
          title="Ripple-carry adder"),
        CODE("Bit 3        Bit 2        Bit 1        Bit 0\n"
             "A3 B3        A2 B2        A1 B1        A0 B0\n"
             " |  |         |  |         |  |         |  |\n"
             "[ FA3 ]<-c3--[ FA2 ]<-c2--[ FA1 ]<-c1--[ FA0 ]<-- Cin = 0\n"
             " |  |                                            \n"
             "c4  S3         S2           S1           S0\n"
             "(Cout)",
             "text", title="A 4-bit ripple-carry adder (c is the carry into each bit)"),
        EX("Worked example 1: 0110 + 0111",
           intro=r"Add A = 0110 (6) and B = 0111 (7) in a 4-bit ripple-carry adder. Give each carry and the sum.",
           steps=[
               S("Bit 0: 0 + 1 + 0", text=r"S0 = 1, carry into bit 1 is 0."),
               S("Bit 1: 1 + 1 + 0", text=r"S1 = 0, carry into bit 2 is 1."),
               S("Bit 2: 1 + 1 + 1", text=r"S2 = 1, carry into bit 3 is 1."),
               S("Bit 3: 0 + 0 + 1", text=r"S3 = 1, carry out is 0."),
               S("Result", math=r"S = 1101_2 = 13, \quad C_{out} = 0"),
           ],
           check=r"6 + 7 = 13"),
        EX("Worked example 2: a carry out",
           intro=r"Add A = 1011 (11) and B = 0110 (6).",
           steps=[
               S("Bit 0: 1 + 0 + 0", text=r"S0 = 1, carry 0."),
               S("Bit 1: 1 + 1 + 0", text=r"S1 = 0, carry 1."),
               S("Bit 2: 0 + 1 + 1", text=r"S2 = 0, carry 1."),
               S("Bit 3: 1 + 0 + 1", text=r"S3 = 0, carry out = 1."),
               S("Result", math=r"C_{out} S = 1\,0001_2 = 17", text=r"The carry out shows the answer does not fit in 4 bits as an unsigned number."),
           ],
           check=r"11 + 6 = 17"),
        H("Why it is slow"),
        T(r"Bit 3 cannot finish until the carry has arrived from bit 2, which waited for bit 1, which waited for bit 0. "
          r"The carry **ripples** along the chain. If each stage takes time t to pass on the carry, an n-bit adder needs about n x t. "
          r"For t = 2 ns this is 8 ns for 4 bits, 16 ns for 8 bits and 64 ns for 32 bits. Faster adders, called **carry look-ahead** adders, work out the carries in advance."),
        H("Subtraction with the same adder"),
        T(r"In two's complement, A - B is the same as **A + (NOT B) + 1**. So the adder can subtract if we (1) invert every bit "
          r"of B and (2) set the carry-in to 1. A control line SUB does both: it is XORed with every bit of B and also fed to the first carry-in."),
        CODE("SUB = 0:  B passes through unchanged, Cin = 0   ->  A + B\n"
             "SUB = 1:  B is inverted by the XOR gates, Cin = 1 ->  A + (NOT B) + 1 = A - B",
             "text", title="An adder-subtractor"),
        EX("Worked example 3: 9 - 5",
           intro=r"Calculate 1001 - 0101 using the adder with SUB = 1.",
           steps=[
               S("Invert B", math=r"\text{NOT } 0101 = 1010"),
               S("Add with Cin = 1", math=r"1001 + 1010 + 1 = 1\,0100"),
               S("Drop the carry out", math=r"0100_2 = 4"),
           ],
           check=r"9 - 5 = 4"),
        EX("Worked example 4: 5 - 9",
           intro=r"Calculate 0101 - 1001 (5 - 9) the same way and read the result as a signed number.",
           steps=[
               S("Invert B", math=r"\text{NOT } 1001 = 0110"),
               S("Add with Cin = 1", math=r"0101 + 0110 + 1 = 1100"),
               S("Read as two's complement", math=r"1100_2 = 12 - 16 = -4"),
           ],
           check=r"5 - 9 = -4"),
        H("Signed overflow"),
        D(r"**Signed overflow** occurs when the true answer is outside the range that fits in the number of bits. For 4-bit "
          r"two's complement the range is -8 to +7. It happens only when two numbers of the **same sign** give an answer of the "
          r"**opposite sign**.",
          title="Signed overflow",
          note=r"Hardware test: overflow = the carry into the top bit XOR the carry out of the top bit."),
        EX("Worked example 5: detect overflow",
           intro=r"Add 0110 (+6) and 0101 (+5) as 4-bit signed numbers. Is there overflow?",
           steps=[
               S("Add", math=r"0110 + 0101 = 1011"),
               S("Read the sign", text=r"The top bit is 1, so the result reads as -5. Two positives gave a negative."),
               S("Carries", text=r"Carry into the top bit = 1; carry out of the top bit = 0. They differ, so overflow = 1."),
           ],
           check=r"6 + 5 = 11, which is outside -8 to +7"),
        TIP(r"Carry out and signed overflow are different. In 11 + 6 there is a carry out. Read as signed numbers, 1011 is -5 and 0110 is +6, so the sum should be +1 and it fits: no signed overflow. Use the flag that matches the number type."),
        H("Common mistakes"),
        MISTAKE(r"Forgetting to add 1 when subtracting", r"Inverting B gives only one's complement. You must also set the carry-in to 1, or the answer is one too small."),
        MISTAKE(r"Calling a carry out an overflow", r"Carry out relates to unsigned numbers; signed overflow is detected from the two carries at the top, or from the signs."),
        QUIZ(r"A 4-bit adder adds 0011 and 0101. What is the sum?",
             ["0110", "1000", "0111", "1100"], 1, r"3 + 5 = 8 = 1000 in binary.",
             hint=r"Add as ordinary numbers, then convert.",
             feedback=["That is 6.", "", "That is 7.", "That is 12."]),
        QUIZ(r"How does a ripple-carry adder subtract B from A?",
             ["It adds A and B and drops the carry", "It adds A, NOT B and a carry-in of 1", "It adds NOT A and B", "It uses a separate subtractor only"],
             1, r"A - B = A + (NOT B) + 1 in two's complement.",
             hint=r"Think two's complement: invert, then add 1.",
             feedback=["That would just add.", "", "That gives B - A minus 1, not A - B.", "The same adder can do both with XOR gates."]),
        H("Practice questions"),
        PQ(r"Add 0111 and 0011 in a 4-bit ripple-carry adder. Give the sum, the carry out and say whether the unsigned result fits.",
           r"7 + 3 = 10 = 1010. Carry out = 0 and the result fits in 4 bits as an unsigned number (as a signed number it would be -6, so there is signed overflow)."),
        PQ(r"Explain why a ripple-carry adder is slow for wide numbers.",
           r"Each stage must wait for the carry from the stage before it, so the delay grows with the number of bits, roughly n times the delay of one stage. Wide numbers therefore take longer."),
        PQ(r"Show how 7 - 7 is calculated by a 4-bit adder, using NOT and a carry-in of 1.",
           r"NOT 0111 = 1000. 0111 + 1000 + 1 = 1 0000. Drop the carry out: 0000 = 0."),
        PQ(r"State when signed overflow occurs and give one example with 4-bit numbers.",
           r"It occurs when two numbers of the same sign give an answer of the opposite sign because the true result is outside the range. Example: 0110 (+6) + 0101 (+5) = 1011, which reads as -5."),
        SUM(r"A ripple-carry adder chains full adders: each carry-out feeds the next carry-in.",
            r"The carry must ripple, so delay grows with the number of bits; look-ahead adders speed this up.",
            r"Subtraction: A + (NOT B) + 1, using XOR gates on B controlled by SUB, and Cin = SUB.",
            r"Signed overflow happens when same-sign operands give an opposite-sign result; carry into the top bit differs from carry out of it."),
    ],
))

# ------------------------------------------------------------------ 9 Multiplexers, demultiplexers and decoders
LESSONS.append(lesson(
    module=LOGIC, topic=COMB,
    title="Multiplexers, demultiplexers and decoders",
    slug="csa-multiplexers-demultiplexers-decoders",
    minutes=22,
    summary="Use multiplexers to select one of several inputs, decoders to switch on exactly one output, and both to build any logic function from its truth table.",
    objectives=[
        "State the number of select lines needed for a multiplexer or decoder of a given size",
        "Write the output of a 2-to-1 and a 4-to-1 multiplexer",
        "Write the truth table of a 2-to-4 decoder and use a decoder to implement a function",
        "Implement a three-input function with a 4-to-1 multiplexer",
    ],
    key_concepts=["Multiplexer", "Demultiplexer", "Decoder", "Select lines", "Minterm", "Chip select"],
    blocks=[
        H("Introduction"),
        T(r"A computer has to choose: which register goes to the ALU, which memory chip answers an address, which key on a "
          r"keypad was pressed. Three small combinational circuits do these jobs: the **multiplexer**, the **demultiplexer** and the **decoder**."),
        H("The multiplexer"),
        D(r"A **multiplexer (MUX)** has several data inputs, some **select lines** and one output. The select lines, "
          r"read as a binary number, choose which input is copied to the output. With $n$ select lines it has $2^n$ data inputs.",
          title="Multiplexer"),
        CODE("2-to-1 MUX (1 select line S):   Y = S'.I0 + S.I1\n"
             "   S = 0 -> Y = I0       S = 1 -> Y = I1\n"
             "\n"
             "4-to-1 MUX (2 select lines S1 S0):\n"
             "   S1 S0 | Y\n"
             "   0  0  | I0\n"
             "   0  1  | I1\n"
             "   1  0  | I2\n"
             "   1  1  | I3\n"
             "   Y = S1'S0'I0 + S1'S0 I1 + S1 S0'I2 + S1 S0 I3",
             "text", title="MUX behaviour (' means NOT, . or no sign means AND)"),
        TIP(r"A multiplexer is like a railway points switch: the select lines set the points, and exactly one input track is connected to the output."),
        H("The demultiplexer"),
        D(r"A **demultiplexer (DEMUX)** does the opposite: one data input is sent to **one of several outputs**, chosen by the select lines. "
          r"The other outputs stay at 0.",
          title="Demultiplexer"),
        T(r"For a 1-to-4 DEMUX with data input D = 1 and select lines 10 (2 in decimal), output 2 is 1 and outputs 0, 1 and 3 are 0."),
        H("The decoder"),
        D(r"A **decoder** has $n$ input lines and $2^n$ output lines. For each input combination **exactly one** output is 1. "
          r"Output $k$ is 1 when the input, read as a number, equals $k$.",
          title="Decoder"),
        CODE("2-to-4 decoder\n"
             "A1 A0 | D0 D1 D2 D3\n"
             "0  0  | 1  0  0  0\n"
             "0  1  | 0  1  0  0\n"
             "1  0  | 0  0  1  0\n"
             "1  1  | 0  0  0  1\n"
             "\n"
             "D0 = A1'A0'   D1 = A1'A0   D2 = A1 A0'   D3 = A1 A0",
             "text", title="Decoder truth table"),
        T(r"Each output of a decoder is a **minterm**: an AND of all the inputs, each in true or inverted form. So a decoder "
          r"followed by an OR gate can build any function written as a sum of minterms. Decoders are also used for **chip select**: "
          r"the top address lines go to a decoder (see the memory map lesson) and the active output enables one memory chip."),
        EX("Worked example 1: a full adder from a decoder",
           intro=r"Implement the full adder using a 3-to-8 decoder (inputs A, B, Cin; outputs D0 to D7) and OR gates.",
           steps=[
               S("List the minterms where S = 1", text=r"S = 1 for input values 1, 2, 4 and 7 (an odd number of 1s)."),
               S("List the minterms where Cout = 1", text=r"Cout = 1 for input values 3, 5, 6 and 7 (two or more 1s)."),
               S("Connect", math=r"S = D1 + D2 + D4 + D7 \quad C_{out} = D3 + D5 + D6 + D7", text=r"One 4-input OR gate for each output."),
           ],
           check=r"\text{Input } 011 = 3: D3 = 1 \Rightarrow C_{out} = 1, S = 0 \quad (0 + 1 + 1 = 10_2)"),
        H("Functions with a multiplexer"),
        T(r"A 4-to-1 MUX with select lines A and B can produce **any** function of three variables A, B, C. Use A and B as the select "
          r"lines. For each pair of rows with the same AB, look at the output column and decide what to connect to that data input: **0**, **1**, **C** or **NOT C**."),
        EX("Worked example 2: a function on a 4-to-1 MUX",
           intro=r"Implement F(A, B, C) = 1 for the input values 1, 2, 6 and 7 (decimal, ABC read as a binary number) using a 4-to-1 MUX with A and B as select lines.",
           steps=[
               S("AB = 00: rows 0 and 1", text=r"F = 0 for 000 and 1 for 001, so F = C. Connect I0 = C."),
               S("AB = 01: rows 2 and 3", text=r"F = 1 for 010 and 0 for 011, so F = NOT C. Connect I1 = C'."),
               S("AB = 10: rows 4 and 5", text=r"F = 0 for both, so I2 = 0."),
               S("AB = 11: rows 6 and 7", text=r"F = 1 for both, so I3 = 1."),
           ],
           check=r"\text{Input } 110: \ AB = 11 \Rightarrow I3 = 1 \Rightarrow F = 1 \ \checkmark"),
        EX("Worked example 3: choosing a register",
           intro=r"A 4-to-1 MUX, 8 bits wide, selects one of four registers R0 to R3 to send to the ALU. How many select lines does it need, and which register is chosen if S1 S0 = 11?",
           steps=[
               S("Select lines", math=r"2^2 = 4 \Rightarrow 2 \text{ select lines}"),
               S("Read the select value", text=r"S1 S0 = 11 is 3, so register R3 is connected to the ALU. The MUX has one such circuit for each of the 8 bits."),
           ]),
        H("Common mistakes"),
        MISTAKE(r"Mixing up MUX and decoder", r"A MUX has many data inputs and ONE output. A decoder has few inputs and many outputs, and exactly one is 1."),
        MISTAKE(r"Wrong number of select lines", r"Count powers of 2: 4 inputs need 2 lines, 8 inputs need 3, 16 inputs need 4. It is not the number of inputs itself."),
        MISTAKE(r"Reading select lines in the wrong order", r"S1 is the more significant bit. S1 S0 = 10 selects input 2, not input 1."),
        QUIZ(r"How many select lines does an 8-to-1 multiplexer have?",
             ["2", "3", "4", "8"], 1, r"2 to the power 3 = 8, so 3 select lines.",
             hint=r"2 to the power ? = 8.",
             feedback=["2 select lines choose among only 4 inputs.", "", "4 select lines would choose among 16 inputs.", "That is the number of inputs, not select lines."]),
        QUIZ(r"A 2-to-4 decoder has inputs A1 A0 = 10. Which output is 1?",
             ["D0", "D1", "D2", "D3"], 2, r"10 in binary is 2, so D2 is 1.",
             hint=r"Read A1 A0 as a binary number.",
             feedback=["D0 is 1 only for input 00.", "D1 is 1 for input 01.", "", "D3 is 1 for input 11."]),
        H("Practice questions"),
        PQ(r"State the difference between a multiplexer and a demultiplexer.",
           r"A multiplexer selects one of several inputs and sends it to a single output. A demultiplexer takes one input and sends it to one of several outputs. Select lines choose in both."),
        PQ(r"A 4-to-1 MUX has I0 = 1, I1 = 0, I2 = 1, I3 = 0. Give the output when S1 S0 = 10 and when S1 S0 = 01.",
           r"S1 S0 = 10 selects I2, so Y = 1. S1 S0 = 01 selects I1, so Y = 0."),
        PQ(r"Write the truth table of a 2-to-4 decoder and state which output is 1 when the input is 11.",
           r"Input 00: D0 = 1. Input 01: D1 = 1. Input 10: D2 = 1. Input 11: D3 = 1. All other outputs are 0 in each row. For input 11, D3 is 1."),
        PQ(r"Use a 4-to-1 MUX with A and B as select lines to implement the majority function F(A, B, C), which is 1 when two or more inputs are 1. State I0 to I3.",
           r"F is 1 for input values 3, 5, 6 and 7. AB = 00: F = 0 so I0 = 0. AB = 01: F = C so I1 = C. AB = 10: F = C so I2 = C. AB = 11: F = 1 so I3 = 1."),
        SUM(r"A MUX with n select lines chooses one of 2 to the power n inputs and has one output.",
            r"A DEMUX sends one input to one of several outputs, chosen by the select lines.",
            r"A decoder activates exactly one of 2 to the power n outputs; each output is a minterm of the inputs.",
            r"A decoder plus an OR gate, or a MUX with A and B as selects and 0, 1, C or NOT C on the data inputs, can implement any three-variable function."),
    ],
))

# ------------------------------------------------------------------ 10 SR latch and D flip-flop
LESSONS.append(lesson(
    module=LOGIC, topic=SEQ,
    title="The SR latch and the D flip-flop: how a circuit remembers",
    slug="csa-sr-latch-d-flip-flop",
    minutes=22,
    summary="See how two cross-coupled NOR gates store one bit, read the SR state table including the forbidden state, and use the clocked D flip-flop to capture data on a clock edge.",
    objectives=[
        "Explain why a sequential circuit needs feedback and a stored state",
        "Complete the state table of an SR latch from a sequence of inputs",
        "Explain the forbidden state S = R = 1",
        "Trace a D flip-flop through several clock edges and state the difference between a latch and a flip-flop"
    ],
    key_concepts=["Sequential circuit", "State", "SR latch", "Set", "Reset", "Forbidden state",
                  "D flip-flop", "Clock edge", "Level-triggered", "Edge-triggered", "Register"],
    blocks=[
        H("Introduction"),
        T(r"A combinational circuit forgets: change its inputs and the old output is gone. But your phone remembers a phone "
          r"number, and a till remembers a running total. Memory needs a circuit whose output depends on **what happened before** as well as on the inputs now. "
          r"This is a **sequential circuit**."),
        D(r"A **sequential circuit** has outputs that depend on the present inputs **and** on its stored **state**. The memory comes from "
          r"**feedback**: an output is wired back to an input.",
          title="Sequential circuit"),
        H("The SR latch"),
        T(r"Connect two NOR gates so that each one's output feeds the other's input. The result is an **SR latch**. "
          r"It has two inputs, **S (set)** and **R (reset)**, and two outputs, Q and Q' (the opposite of Q)."),
        CODE("Q  = NOR(R, Q')\n"
             "Q' = NOR(S, Q)",
             "text", title="SR latch from two NOR gates"),
        CODE("S  R | Q (next)      meaning\n"
             "0  0 | no change     hold the stored bit\n"
             "1  0 | 1             set\n"
             "0  1 | 0             reset\n"
             "1  1 | not allowed   forbidden",
             "text", title="State table of the SR latch"),
        EX("Worked example 1: a sequence of inputs",
           intro=r"The latch starts with Q = 0. The inputs (S, R) are applied in turn: (1,0), (0,0), (0,1), (0,0), (1,0), (0,0). Give Q after each.",
           steps=[
               S("(1,0): set", text=r"Q = 1."),
               S("(0,0): hold", text=r"Q stays 1."),
               S("(0,1): reset", text=r"Q = 0."),
               S("(0,0): hold", text=r"Q stays 0."),
               S("(1,0): set", text=r"Q = 1."),
               S("(0,0): hold", text=r"Q stays 1. The latch has remembered the last set."),
           ],
           check=r"Q: 1, 1, 0, 0, 1, 1"),
        D(r"**S = R = 1** is the **forbidden state**. In a NOR latch both Q and Q' become 0, which breaks the rule that they are opposites. "
          r"If S and R then return to 0 together, the final state is unpredictable.",
          title="Forbidden state"),
        H("Making it useful: the clock and the D flip-flop"),
        T(r"A plain SR latch reacts at once to its inputs, and has the forbidden state. A **D (data) flip-flop** removes both "
          r"problems. It has a single data input **D** and a **clock** input. At each **rising clock edge** (the moment the clock goes from 0 to 1) it copies D to Q, and "
          r"between edges it **ignores D** and holds Q."),
        CODE("D | Q (next, after the rising clock edge)\n"
             "0 | 0\n"
             "1 | 1",
             "text", title="D flip-flop state table"),
        F(r"Q_{\text{next}} = D", title="Characteristic equation"),
        EX("Worked example 2: tracing a D flip-flop",
           intro=r"A D flip-flop starts with Q = 0. D has the value 1, 0, 0, 1, 1, 0 at six successive rising edges. Give Q after each edge.",
           steps=[
               S("Rule", text=r"After each rising edge, Q takes the value D had at that edge."),
               S("Edges 1 to 3", text=r"Q = 1, 0, 0."),
               S("Edges 4 to 6", text=r"Q = 1, 1, 0."),
           ],
           check=r"The output copies the input, one clock edge later"),
        T(r"If D changes **between** edges, Q does not change. This protects the stored bit from noise and lets many flip-flops share one clock so that they all update together."),
        KEY("Latch or flip-flop?", r"Know the difference.",
            cards=[
                ["Latch (level-triggered)", r"Output can change **while** the enable level is active. Simple, but changes can pass through at any time in that period."],
                ["Flip-flop (edge-triggered)", r"Output changes **only** at the clock edge. Each edge stores one value, so circuits stay in step."],
            ]),
        H("Registers"),
        T(r"A **register** is a group of flip-flops sharing one clock. An 8-bit register uses 8 D flip-flops. It stores one byte, which is how a CPU keeps the ACC, PC and other registers in the previous lessons."),
        EX("Worked example 3: size of a register",
           intro=r"How many D flip-flops are needed for a 16-bit memory address register, and how many different addresses can it hold?",
           steps=[
               S("Flip-flops", text=r"One per bit: 16 flip-flops."),
               S("Values", math=r"2^{16} = 65\,536 \text{ different addresses}"),
           ]),
        H("Common mistakes"),
        MISTAKE(r"Saying a flip-flop changes whenever D changes", r"A D flip-flop changes only at the clock edge. Between edges Q is held."),
        MISTAKE(r"Using S = R = 1 as a way to 'toggle'", r"S = R = 1 is forbidden in an SR latch. Toggling needs a JK or T flip-flop."),
        MISTAKE(r"Confusing combinational and sequential circuits", r"A combinational circuit's output depends only on the present inputs. A sequential circuit's depends also on its stored state."),
        QUIZ(r"An SR latch has Q = 1. The inputs become S = 0 and R = 0. What is Q?",
             ["0", "1", "Unpredictable", "It depends on the clock"], 1,
             r"S = R = 0 means hold, so Q stays 1.",
             hint=r"What does S = 0 and R = 0 do in the state table?",
             feedback=["That would need R = 1.", "", "That is the forbidden state S = R = 1, not 00.", "A plain SR latch has no clock."]),
        QUIZ(r"A D flip-flop has Q = 0, D = 1, and no rising edge has arrived yet. What is Q?",
             ["1", "0", "Unpredictable", "It copies D immediately"], 1,
             r"A D flip-flop copies D only at the clock edge, so Q stays 0 until then.",
             hint=r"When does a D flip-flop look at D?",
             feedback=["It will become 1 only at the next rising edge.", "", "There is nothing unpredictable here.", "That describes a latch with its enable on."]),
        H("Practice questions"),
        PQ(r"Explain what is meant by a sequential circuit and how an SR latch stores a bit.",
           r"In a sequential circuit the output depends on the present inputs and on the stored state. An SR latch has two cross-coupled gates, so each output feeds the other gate's input. This feedback keeps the output at its last value when S = R = 0, so one bit is stored."),
        PQ(r"An SR latch starts with Q = 1. Inputs (S, R): (0,0), (0,1), (0,0), (1,0). Give Q after each.",
           r"(0,0) hold: 1. (0,1) reset: 0. (0,0) hold: 0. (1,0) set: 1. So Q = 1, 0, 0, 1."),
        PQ(r"Why is the input S = R = 1 not allowed in an SR latch?",
           r"It makes both outputs 0 in a NOR latch, so Q and Q' are not opposites. When S and R return to 0 together, the circuit settles in an unpredictable state."),
        PQ(r"A D flip-flop starts at Q = 1. D at successive rising edges is 0, 0, 1, 0. Give Q after each edge, and state what happens if D changes between two edges.",
           r"Q = 0, 0, 1, 0. A change in D between two edges has no effect: Q is only updated at the rising edge."),
        SUM(r"A sequential circuit's output depends on the inputs and the stored state; feedback provides the memory.",
            r"SR latch: 00 hold, 10 set, 01 reset, 11 forbidden.",
            r"D flip-flop: Q takes the value of D at each rising clock edge and holds it between edges.",
            r"A register is a group of D flip-flops sharing a clock; n flip-flops store n bits."),
    ],
))

# ------------------------------------------------------------------ 11 JK and T flip-flops
LESSONS.append(lesson(
    module=LOGIC, topic=SEQ,
    title="JK and T flip-flops: state tables, toggling and excitation",
    slug="csa-jk-t-flip-flops-state-tables",
    minutes=23,
    summary="Complete and use the state tables of the JK and T flip-flops, write their characteristic equations, read an excitation table, and use the T flip-flop to divide a frequency by two.",
    objectives=[
        "Complete the state table of a JK flip-flop and a T flip-flop",
        "Trace Q through a sequence of JK or T inputs over several clock edges",
        "Write and check the characteristic equations of SR, D, JK and T flip-flops",
        "Use the toggle action to divide a clock frequency"
    ],
    key_concepts=["JK flip-flop", "T flip-flop", "Toggle", "State table", "Characteristic equation",
                  "Excitation table", "Frequency division"],
    blocks=[
        H("Introduction"),
        T(r"The D flip-flop copies its input. But many circuits, such as a counter in a mobile data meter, need a bit that "
          r"**flips** on command. The **JK** and **T** flip-flops give this. The JK flip-flop is the SR latch fixed: its "
          r"forbidden input pair now has a useful meaning, **toggle**."),
        H("The JK flip-flop"),
        D(r"A **JK flip-flop** has inputs J (set) and K (reset) and a clock. At the clock edge: J = K = 0 holds, J = 1 K = 0 sets, "
          r"J = 0 K = 1 resets, and J = K = 1 **toggles** Q to the opposite of its present value.",
          title="JK flip-flop"),
        CODE("J  K | Q (next)    action\n"
             "0  0 | Q           hold\n"
             "0  1 | 0           reset\n"
             "1  0 | 1           set\n"
             "1  1 | Q'          toggle (Q becomes NOT Q)",
             "text", title="State table of a JK flip-flop (at each clock edge)"),
        F(r"Q_{\text{next}} = J\,\overline{Q} + \overline{K}\,Q", title="Characteristic equation of the JK flip-flop"),
        EX("Worked example 1: a JK sequence",
           intro=r"A JK flip-flop starts with Q = 1. At six successive clock edges (J, K) is (0,1), (1,0), (0,0), (1,1), (1,1), (1,1). Give Q after each edge.",
           steps=[
               S("(0,1) reset", text=r"Q = 0."),
               S("(1,0) set", text=r"Q = 1."),
               S("(0,0) hold", text=r"Q = 1."),
               S("(1,1) toggle", text=r"Q = 0."),
               S("(1,1) toggle", text=r"Q = 1."),
               S("(1,1) toggle", text=r"Q = 0."),
           ],
           check=r"Q: 0, 1, 1, 0, 1, 0"),
        H("The T flip-flop"),
        D(r"A **T (toggle) flip-flop** has one input T and a clock. If T = 0, Q holds. If T = 1, Q toggles at the clock edge.",
          title="T flip-flop"),
        CODE("T | Q (next)\n"
             "0 | Q        hold\n"
             "1 | Q'       toggle",
             "text", title="State table of a T flip-flop"),
        F(r"Q_{\text{next}} = T \oplus Q", title="Characteristic equation of the T flip-flop (XOR)"),
        T(r"A T flip-flop is a JK flip-flop with J and K joined to one input T. A D flip-flop is a JK flip-flop with K = NOT J."),
        EX("Worked example 2: a T sequence",
           intro=r"A T flip-flop starts with Q = 1. T is 0, 1, 1, 0, 1 at five successive clock edges. Give Q after each edge.",
           steps=[
               S("T = 0", text=r"Hold: Q = 1."),
               S("T = 1", text=r"Toggle: Q = 0."),
               S("T = 1", text=r"Toggle: Q = 1."),
               S("T = 0", text=r"Hold: Q = 1."),
               S("T = 1", text=r"Toggle: Q = 0."),
           ],
           check=r"Q: 1, 0, 1, 1, 0"),
        H("Excitation: what inputs give a required change?"),
        T(r"Sometimes you know the change you want, 0 to 1, say, and need the inputs. The table below shows them. An X means *do not care*: either value works."),
        CODE("Q -> Q(next) | J K       | T | D\n"
             "0 -> 0       | 0 X       | 0 | 0\n"
             "0 -> 1       | 1 X       | 1 | 1\n"
             "1 -> 0       | X 1       | 1 | 0\n"
             "1 -> 1       | X 0       | 0 | 1",
             "text", title="Excitation table"),
        EX("Worked example 3: finding the inputs",
           intro=r"A JK flip-flop must change from Q = 1 to Q = 0 at the next edge. What can J and K be?",
           steps=[
               S("Look at the table", text=r"For 1 to 0 you need K = 1. J can be 0 (reset) or 1 (toggle): both give 0."),
               S("Answer", text=r"K = 1 and J is a do-not-care."),
           ]),
        H("Dividing a frequency"),
        T(r"Set T = 1 (or J = K = 1). Q toggles at every rising clock edge, so one complete cycle of Q needs two clock cycles. "
          r"**The frequency of Q is half the clock frequency.** Two flip-flops in a row divide by 4, three divide by 8."),
        EX("Worked example 4: dividing",
           intro=r"A 1 MHz clock drives a chain of three T flip-flops, each clocked by the previous output. Give the output frequency of the last one.",
           steps=[
               S("Each stage halves", math=r"1\,000\,000 \div 2 = 500\,000"),
               S("Second stage", math=r"500\,000 \div 2 = 250\,000"),
               S("Third stage", math=r"250\,000 \div 2 = 125\,000 \text{ Hz} = 125 \text{ kHz}"),
           ],
           check=r"1\,000\,000 \div 2^3 = 125\,000"),
        TIP(r"In an exam, write the next-state column by applying the rule row by row from the starting Q. Do not try to do several edges in your head."),
        H("Common mistakes"),
        MISTAKE(r"Saying JK with J = K = 1 is forbidden", r"That is the forbidden state of the SR latch. In a JK flip-flop it is the **toggle** action."),
        MISTAKE(r"Toggling when T is 0", r"T = 0 means **hold**. Only T = 1 toggles."),
        MISTAKE(r"Showing a change before the clock edge", r"The next Q appears **at the clock edge**. Between edges the outputs stay fixed."),
        QUIZ(r"A JK flip-flop has Q = 0, J = 1, K = 1. What is Q after the clock edge?",
             ["0", "1", "Unpredictable", "It depends on the previous input"], 1, r"J = K = 1 toggles Q, so 0 becomes 1.",
             hint=r"What is the action when J and K are both 1?",
             feedback=["That would be reset or hold.", "", "That applies to the SR latch with S = R = 1, not a JK flip-flop.", "The next state depends on the present Q and on J, K, not on earlier inputs."]),
        QUIZ(r"A T flip-flop is clocked by a 4 kHz signal with T = 1. What is the frequency of Q?",
             ["8 kHz", "4 kHz", "2 kHz", "1 kHz"], 2, r"Q toggles once per clock cycle, so its frequency is half: 2 kHz.",
             hint=r"How many clock cycles for one full cycle of Q?",
             feedback=["That would double the frequency.", "The frequency would stay the same only if Q repeated every clock.", "", "That is a division by 4, which needs two flip-flops."]),
        H("Practice questions"),
        PQ(r"Complete: a JK flip-flop has Q = 1. State Q after one clock edge when (J, K) = (0,0), (0,1), (1,0) and (1,1).",
           r"(0,0): hold, Q = 1. (0,1): reset, Q = 0. (1,0): set, Q = 1. (1,1): toggle, Q = 0."),
        PQ(r"A JK flip-flop starts at Q = 0. At four edges (J, K) = (1,0), (1,1), (0,1), (1,1). Give Q after each edge.",
           r"(1,0) set: 1. (1,1) toggle: 0. (0,1) reset: 0. (1,1) toggle: 1. So Q = 1, 0, 0, 1."),
        PQ(r"Write the characteristic equation of a T flip-flop and use it to find Q(next) when T = 1 and Q = 1.",
           r"Q(next) = T XOR Q. With T = 1 and Q = 1: 1 XOR 1 = 0. Q toggles from 1 to 0."),
        PQ(r"Explain how a T flip-flop can be used to halve the frequency of a clock signal, and find the output of two in series for a 6 MHz clock.",
           r"With T = 1, Q toggles at each clock edge, so Q completes one cycle for every two clock cycles: the frequency is halved. Two in series divide by 4: 6 MHz / 4 = 1.5 MHz."),
        SUM(r"JK flip-flop: 00 hold, 01 reset, 10 set, 11 toggle. Q(next) = J Q' + K' Q.",
            r"T flip-flop: T = 0 hold, T = 1 toggle. Q(next) = T XOR Q.",
            r"Trace by applying the table one clock edge at a time from the starting Q.",
            r"With T = 1, a flip-flop halves the clock frequency; n in series divide by 2 to the power n."),
    ],
))

# ------------------------------------------------------------------ 12 Counters and shift registers
LESSONS.append(lesson(
    module=LOGIC, topic=SEQ,
    title="Counters and shift registers built from flip-flops",
    slug="csa-counters-shift-registers",
    minutes=23,
    summary="Build a binary counter from T flip-flops, trace its count sequence and timing, change its modulus with a reset, and use a shift register to move bits and to multiply or divide by 2.",
    objectives=[
        "Trace the count sequence of a 3-bit binary counter and read its timing diagram",
        "Work out the number of flip-flops needed for a counter of a given modulus",
        "Explain how a counter is made to count 0 to 5 instead of 0 to 7",
        "Trace a 4-bit serial-in shift register and describe shifts as multiplication and division by 2"
    ],
    key_concepts=["Binary counter", "Ripple (asynchronous) counter", "Synchronous counter", "Modulus",
                  "Shift register", "Serial-in parallel-out", "Logical shift"],
    blocks=[
        H("Introduction"),
        T(r"A digital clock in a Douala bar counts seconds, a mobile data meter counts bytes, and a serial port on a card reader "
          r"collects bits one at a time. All three are built from flip-flops joined in chains: **counters** and **shift registers**."),
        H("A 3-bit binary counter"),
        D(r"A **counter** is a register whose value goes up by 1 at each clock pulse. With $n$ flip-flops it counts through "
          r"$2^n$ values, then returns to 0. The number of values is its **modulus**.",
          title="Counter and modulus"),
        T(r"Make each bit a T flip-flop. Bit 0 toggles at every pulse. Bit 1 toggles when bit 0 is 1. Bit 2 toggles when bits 1 and 0 are both 1. "
          r"So T0 = 1, T1 = Q0 and T2 = Q1 AND Q0. All flip-flops share one clock: this is a **synchronous counter**."),
        CODE("Clock pulse   Q2 Q1 Q0   Value\n"
             "start         0  0  0    0\n"
             "1             0  0  1    1\n"
             "2             0  1  0    2\n"
             "3             0  1  1    3\n"
             "4             1  0  0    4\n"
             "5             1  0  1    5\n"
             "6             1  1  0    6\n"
             "7             1  1  1    7\n"
             "8             0  0  0    0   (wraps round)",
             "text", title="Count sequence of a 3-bit counter"),
        IMG("al-csa-counter-timing.svg",
            "A timing diagram of a 3-bit counter over eight clock pulses. Q0 changes at every pulse, Q1 changes every second pulse and Q2 changes every fourth pulse. The counts shown below are 0 to 7.",
            caption="Figure 1. Q0 has half the clock frequency, Q1 a quarter, Q2 an eighth."),
        T(r"In a **ripple (asynchronous) counter** the flip-flops are not clocked together: the output of each one clocks the next. "
          r"It needs fewer gates but the change ripples along, so outputs are briefly wrong, as with the ripple-carry adder."),
        EX("Worked example 1: output frequency",
           intro=r"A 3-bit counter is driven by a 1 kHz clock. Give the frequency of Q0, Q1 and Q2.",
           steps=[
               S("Q0", math=r"1000 \div 2 = 500 \text{ Hz}"),
               S("Q1", math=r"500 \div 2 = 250 \text{ Hz}"),
               S("Q2", math=r"250 \div 2 = 125 \text{ Hz}"),
           ],
           check=r"1000 \div 2^3 = 125"),
        H("Modulus and the number of flip-flops"),
        T(r"For a counter of modulus N you need the smallest n with $2^n \ge N$. A decimal digit counter (0 to 9, N = 10) needs 4 flip-flops, because $2^3 = 8$ is too small and $2^4 = 16$ is enough."),
        EX("Worked example 2: how many flip-flops?",
           intro=r"A timer must count seconds from 0 to 59. How many flip-flops are needed?",
           steps=[
               S("Count the values", text=r"60 different values."),
               S("Find n", math=r"2^5 = 32 < 60 \quad 2^6 = 64 \ge 60"),
               S("Answer", text=r"6 flip-flops. Four of the 64 values are never used."),
           ]),
        H("Counting 0 to 5"),
        T(r"To make a mod-6 counter from three flip-flops, detect the count 6 (110) with an AND gate on Q2 and Q1, and use its output to **clear** all flip-flops to 000. "
          r"The counter then goes 0, 1, 2, 3, 4, 5, then back to 0. The value 110 appears only for an instant."),
        CODE("0 1 2 3 4 5 0 1 2 3 4 5 ...   (six states, modulus 6)",
             "text", title="Sequence of a mod-6 counter"),
        H("Shift registers"),
        D(r"A **shift register** is a row of D flip-flops where each output feeds the next input. At each clock pulse every bit moves "
          r"one place along, and a new bit enters at one end.",
          title="Shift register"),
        EX("Worked example 3: serial in",
           intro=r"A 4-bit shift register Q3 Q2 Q1 Q0 starts at 0000. New bits enter at Q3 and every bit shifts right one place. The serial input is 1, 0, 1, 1 on four successive pulses. Give the contents after each pulse.",
           steps=[
               S("Pulse 1", text=r"Input 1 enters: 1000."),
               S("Pulse 2", text=r"Input 0 enters, the 1 moves right: 0100."),
               S("Pulse 3", text=r"Input 1 enters: 1010."),
               S("Pulse 4", text=r"Input 1 enters: 1101."),
               S("Read in parallel", text=r"After four pulses the register holds 1101, all four bits at once. This is **serial-in, parallel-out** conversion: 4 pulses to collect 4 bits."),
           ],
           check=r"\text{first bit in (1) is now at } Q_0, \text{ last bit in (1) is at } Q_3"),
        KEY("Shifts as arithmetic", r"A shift moves every bit one place.",
            cards=[
                ["Shift left", r"Every bit moves to a higher place value: **multiply by 2**. 0110 (6) becomes 1100 (12)."],
                ["Shift right", r"Every bit moves to a lower place value: **divide by 2** (whole number). 1100 (12) becomes 0110 (6)."],
            ],
            note=r"A bit shifted out of the end is lost. For signed numbers a different shift keeps the sign bit."),
        H("Common mistakes"),
        MISTAKE(r"Counting the wrong modulus", r"n flip-flops count 2 to the power n values, from 0 up to one less than that. A 3-bit counter's highest count is 7, not 8."),
        MISTAKE(r"Showing all flip-flops toggling at every pulse", r"In a binary counter Q0 toggles every pulse, but Q1 only when Q0 = 1, and Q2 only when Q1 and Q0 are both 1."),
        MISTAKE(r"Shifting the wrong way", r"Know which end the new bit enters, and which end loses a bit. Shifting left doubles; shifting right halves."),
        QUIZ(r"How many different values can a 4-bit counter show?",
             ["4", "8", "15", "16"], 3, r"2 to the power 4 = 16 values, from 0 to 15.",
             hint=r"2 to the power n.",
             feedback=["4 is the number of flip-flops.", "8 is for 3 flip-flops.", "15 is the highest count, but 0 is also a value.", ""]),
        QUIZ(r"The register 0011 (3) is shifted left one place with 0 entering on the right. What is the result?",
             ["0001", "0110", "1100", "0111"], 1, r"Shifting left doubles the value: 3 x 2 = 6 = 0110.",
             hint=r"Shifting left multiplies by 2.",
             feedback=["That is a right shift: 3 / 2 = 1.", "", "That would be 12, a shift left by two places.", "That is 7: a 1 would have been shifted in."]),
        H("Practice questions"),
        PQ(r"A 3-bit binary counter holds 101. Give the next three values.",
           r"110, then 111, then 000 (it wraps round after 7)."),
        PQ(r"Calculate the minimum number of flip-flops for a counter that counts from 0 to 99.",
           r"100 values are needed. 2 to the power 6 = 64 is too small; 2 to the power 7 = 128 is enough. So 7 flip-flops."),
        PQ(r"A 4-bit shift register starts at 0000 and bits enter at the left, shifting right. The serial input is 0, 1, 1, 0. Give the contents after each pulse.",
           r"Pulse 1: 0000. Pulse 2: 1000. Pulse 3: 1100. Pulse 4: 0110. (Each new bit enters at the left and earlier bits move right.)"),
        PQ(r"Explain how a shift register can be used to multiply an unsigned number by 4.",
           r"Shifting left by one place doubles the value, so shifting left twice multiplies by 4, provided no 1 is shifted out of the top end. For example 0011 (3) shifted left twice is 1100 (12)."),
        SUM(r"A binary counter built from T flip-flops goes through 2 to the power n values; Q0 toggles every pulse, Q1 when Q0 = 1, and so on.",
            r"Each flip-flop in the chain halves the frequency, so output k has frequency clock / 2 to the power (k + 1).",
            r"A counter with modulus N needs the smallest n where 2 to the power n is at least N; a reset gate shortens the sequence.",
            r"In a shift register each bit moves along one place per pulse; shifting left multiplies by 2, shifting right divides by 2."),
    ],
))

# ------------------------------------------------------------------ 13 Boolean laws and De Morgan
LAWS = """Law              AND form              OR form
Identity         A . 1 = A             A + 0 = A
Null             A . 0 = 0             A + 1 = 1
Idempotent       A . A = A             A + A = A
Complement       A . A' = 0            A + A' = 1
Double NOT       (A')' = A
Commutative      A . B = B . A         A + B = B + A
Associative      (AB)C = A(BC)         (A + B) + C = A + (B + C)
Distributive     A(B + C) = AB + AC    A + BC = (A + B)(A + C)
Absorption       A(A + B) = A          A + AB = A
De Morgan        (AB)' = A' + B'       (A + B)' = A' B'"""

LESSONS.append(lesson(
    module=LOGIC, topic=SIMP,
    title="Boolean algebra laws and De Morgan's theorems",
    slug="csa-boolean-laws-de-morgan",
    minutes=22,
    summary="Use the laws of Boolean algebra and De Morgan's theorems to rewrite expressions, and show that NAND alone (or NOR alone) can build every gate.",
    objectives=[
        "State and apply the identity, null, idempotent, complement, absorption and distributive laws",
        "Apply De Morgan's theorems to negate an expression",
        "Prove a law by a truth table",
        "Build NOT, AND and OR from NAND gates only"
    ],
    key_concepts=["Boolean algebra", "Identity law", "Complement law", "Absorption law", "Distributive law",
                  "De Morgan's theorems", "Universal gate", "NAND", "NOR"],
    blocks=[
        H("Introduction"),
        T(r"A circuit that has more gates than needed costs more money, uses more power and runs slower. Boolean algebra "
          r"lets us *rewrite* a logic expression into a shorter one that does the same job. This lesson gives you the rules; the next two use them."),
        T(r"Notation: AB or A . B means A AND B. A + B means A OR B. A' means NOT A (examiners often use a bar over the letter instead)."),
        H("The laws"),
        CODE(LAWS, "text", title="Laws of Boolean algebra"),
        T(r"Each law can be **proved with a truth table**: write all input combinations and show the two sides agree in every row. "
          r"Notice the **duality**: swap AND with OR and 0 with 1 in a law, and you get another true law."),
        KEY("Four useful extras", r"These follow from the laws above and are used all the time.",
            cards=[
                ["A + A'B = A + B", r"Remove a NOT from the second term."],
                ["A(A' + B) = AB", r"The dual form of the same rule."],
                ["AB + AB' = A", r"Combining: the variable that changes (B) drops out."],
                ["A + AB = A", r"Absorption: the longer term is absorbed."],
            ]),
        EX("Worked example 1: proving a law by truth table",
           intro=r"Show that A + A'B = A + B.",
           steps=[
               S("Write the four rows", text=r"For AB = 00: left side 0 + 1 . 0 = 0, right side 0 + 0 = 0."),
               S("Row AB = 01", text=r"Left: 0 + 1 . 1 = 1. Right: 0 + 1 = 1."),
               S("Rows AB = 10 and 11", text=r"Left: 1 + 0 = 1 in both rows. Right: 1 + 0 = 1 and 1 + 1 = 1."),
               S("Conclusion", text=r"All four rows agree, so A + A'B = A + B."),
           ]),
        H("De Morgan's theorems"),
        D(r"**De Morgan's theorems** tell you how to negate an AND or an OR. To negate a combination, negate each variable "
          r"and **swap AND with OR**.",
          title="De Morgan's theorems",
          formula=r"\overline{A \cdot B} = \overline{A} + \overline{B} \qquad \overline{A + B} = \overline{A} \cdot \overline{B}"),
        T(r"In words: NOT (A AND B) is the same as (NOT A) OR (NOT B). Check: A = 1, B = 0. A AND B = 0, so NOT of it is 1. And NOT A OR NOT B = 0 + 1 = 1. They agree."),
        EX("Worked example 2: negate an expression",
           intro=r"Simplify (AB + C)' so that no negation covers more than one variable.",
           steps=[
               S("Treat (AB) and C as two terms joined by OR", text=r"(AB + C)' = (AB)' . C'."),
               S("Apply De Morgan to (AB)'", math=r"(AB)' = A' + B'"),
               S("Result", math=r"(A' + B') \cdot C'"),
           ],
           check=r"A = B = C = 1: left = (1 + 1)' = 0; right = (0 + 0) . 0 = 0"),
        EX("Worked example 3: a second negation",
           intro=r"Simplify ((A + B')C)' .",
           steps=[
               S("Break the outer AND", math=r"((A + B')C)' = (A + B')' + C'"),
               S("De Morgan on (A + B')'", math=r"(A + B')' = A' \cdot B'' = A'B"),
               S("Result", math=r"A'B + C'"),
           ],
           check=r"A = 0, B = 1, C = 1: left = ((0 + 0) . 1)' = 1; right = 1 . 1 + 0 = 1"),
        TIP(r"When De Morgan is applied, **three things change together**: break the bar, swap the operator, and negate each part. Forgetting one of the three is the usual mistake."),
        H("Universal gates"),
        D(r"A **universal gate** can build every other gate. NAND and NOR are universal.",
          title="Universal gates"),
        CODE("NOT A  = NAND(A, A)\n"
             "A AND B = NAND( NAND(A, B), NAND(A, B) )          (a NAND then a NOT)\n"
             "A OR B  = NAND( NAND(A, A), NAND(B, B) )          (NOT A and NOT B, then NAND: De Morgan)",
             "text", title="NAND only"),
        T(r"Why does OR work? By De Morgan, A + B = (A' B')'. That is a NAND of A' and B', and A' and B' are each a NAND with its inputs joined. "
          r"Factories prefer one gate type because it is cheaper to make and stock."),
        EX("Worked example 4: an OR gate from NAND gates",
           intro=r"Show that NAND(NAND(A,A), NAND(B,B)) = A OR B.",
           steps=[
               S("Inner gates", text=r"NAND(A,A) = A' and NAND(B,B) = B'."),
               S("Outer gate", math=r"\text{NAND}(A', B') = (A' B')'"),
               S("De Morgan", math=r"(A' B')' = A'' + B'' = A + B"),
           ]),
        H("Common mistakes"),
        MISTAKE(r"Changing only the operator", r"(A + B)' is NOT A' + B'. You must also negate each variable, and swap the operator: A' B'."),
        MISTAKE(r"Cancelling terms wrongly", r"A + A = A, not 2A. Boolean values are only 0 and 1, so there are no coefficients."),
        MISTAKE(r"Treating A + BC as (A + B)C", r"AND is done first. A + BC means A OR (B AND C). Use the distributive law (A + B)(A + C) to expand the other way."),
        QUIZ(r"By De Morgan's theorem, (A + B)' equals...",
             ["A' + B'", "A' B'", "A B", "A + B'"], 1, r"Negate each variable and swap OR to AND: A' B'.",
             hint=r"Negate each variable and swap the operator.",
             feedback=["That keeps the OR, which is the mistake.", "", "That has no negations.", "Only B is negated and the operator is unchanged."]),
        QUIZ(r"Which law gives A + AB = A?",
             ["Complement", "Idempotent", "Absorption", "Identity"], 2, r"The longer term AB is absorbed by A.",
             hint=r"The extra term disappears into the shorter one.",
             feedback=["The complement law involves A and A'.", "The idempotent law is A + A = A.", "", "The identity law involves 0 or 1."]),
        H("Practice questions"),
        PQ(r"State De Morgan's theorems in words.",
           r"NOT (A AND B) = (NOT A) OR (NOT B). NOT (A OR B) = (NOT A) AND (NOT B). To negate a combination, negate each part and swap AND with OR."),
        PQ(r"Use De Morgan's theorem to rewrite (A'B)' without a negation over more than one variable.",
           r"(A'B)' = A'' + B' = A + B'."),
        PQ(r"Prove by truth table that A + AB = A.",
           r"For AB = 00: 0 + 0 = 0 and A = 0. For AB = 01: 0 + 0 = 0 and A = 0. For AB = 10: 1 + 0 = 1 and A = 1. For AB = 11: 1 + 1 = 1 and A = 1. The two sides agree in every row."),
        PQ(r"Show how an AND gate can be built using NAND gates only.",
           r"Feed A and B into one NAND gate, giving (AB)'. Join both inputs of a second NAND gate to that output, giving ((AB)')' = AB, because a NAND with its inputs joined is a NOT."),
        SUM(r"Boolean laws (identity, null, idempotent, complement, absorption, distributive) let you rewrite expressions.",
            r"Prove a law by a truth table: both sides must agree in every row.",
            r"De Morgan: (AB)' = A' + B' and (A + B)' = A' B': break the bar, swap the operator, negate each part.",
            r"NAND and NOR are universal gates: NOT, AND and OR can each be built from one of them."),
    ],
))

# ------------------------------------------------------------------ 14 SOP, POS and algebraic simplification
TT14 = """A B C | F    minterm / maxterm
0 0 0 | 0    M0 = A + B + C
0 0 1 | 1    m1 = A'B'C
0 1 0 | 0    M2 = A + B' + C
0 1 1 | 1    m3 = A'BC
1 0 0 | 0    M4 = A' + B + C
1 0 1 | 1    m5 = AB'C
1 1 0 | 1    m6 = ABC'
1 1 1 | 1    m7 = ABC"""

LESSONS.append(lesson(
    module=LOGIC, topic=SIMP,
    title="From truth table to expression: SOP, POS and algebraic simplification",
    slug="csa-sop-pos-algebraic-simplification",
    minutes=24,
    summary="Write a Boolean expression from a truth table as a sum of products or a product of sums, then simplify it step by step with Boolean algebra and check the result.",
    objectives=[
        "Write the sum-of-products expression for a truth table using minterms",
        "Write the product-of-sums expression using the rows where the output is 0",
        "Simplify an expression using the Boolean laws, naming the law at each step",
        "Check a simplified expression against the original by truth table"
    ],
    key_concepts=["Minterm", "Maxterm", "Sum of products (SOP)", "Product of sums (POS)",
                  "Canonical form", "Consensus", "Simplification"],
    blocks=[
        H("Introduction"),
        T(r"A designer of a door alarm for a shop in Kumba starts from a table: for each combination of sensors, should "
          r"the alarm sound? The table must become a circuit. The route is: truth table, then an expression, then a *simpler* "
          r"expression, then gates."),
        H("Minterms and maxterms"),
        D(r"A **minterm** is an AND of all the input variables, each in true or complemented form, that is 1 for exactly one row of the truth table. "
          r"For the row 101 it is AB'C.",
          title="Minterm"),
        D(r"A **maxterm** is an OR of all the variables that is 0 for exactly one row. For the row 010 it is A + B' + C: each variable "
          r"appears in the form that makes the term 0 in that row.",
          title="Maxterm"),
        CODE(TT14, "text", title="A truth table with its minterms (for 1s) and maxterms (for 0s)"),
        H("Sum of products"),
        T(r"For every row where F = 1, write its minterm. OR them together. This is the **sum-of-products (SOP)** form."),
        EX("Worked example 1: SOP from the table",
           intro=r"Write the SOP expression for F in the table above.",
           steps=[
               S("Rows where F = 1", text=r"Rows 1, 3, 5, 6 and 7 (ABC = 001, 011, 101, 110, 111)."),
               S("Write their minterms", math=r"F = A'B'C + A'BC + AB'C + ABC' + ABC"),
           ]),
        H("Product of sums"),
        T(r"For every row where F = 0, write its maxterm. AND them together. This is the **product-of-sums (POS)** form. It is useful when F is mostly 1."),
        EX("Worked example 2: POS from the table",
           intro=r"Write the POS expression for the same F.",
           steps=[
               S("Rows where F = 0", text=r"Rows 0, 2 and 4 (ABC = 000, 010, 100)."),
               S("Write their maxterms", math=r"F = (A + B + C)(A + B' + C)(A' + B + C)"),
           ]),
        H("Simplifying with algebra"),
        T(r"The SOP above has 5 terms of 3 variables: 15 inputs on the AND gates. Algebra can cut it down. "
          r"Work step by step and name the law each time."),
        EX("Worked example 3: simplify the SOP",
           intro=r"Simplify F = A'B'C + A'BC + AB'C + ABC' + ABC.",
           steps=[
               S("Use idempotence: write ABC twice", math=r"F = A'B'C + A'BC + AB'C + ABC + ABC' + ABC", text=r"A + A = A lets us reuse a term."),
               S("Group the four terms that contain C", math=r"C(A'B' + A'B + AB' + AB) + AB(C' + C)"),
               S("Complement law", math=r"A'B' + A'B + AB' + AB = 1 \text{ and } C' + C = 1"),
               S("Identity law", math=r"F = C + AB"),
           ],
           check=r"\text{Rows: } ABC = 110 \to 0 + 1 = 1 \checkmark; \quad 100 \to 0 + 0 = 0 \checkmark"),
        EX("Worked example 4: simplify with two combinations",
           intro=r"Simplify F = ABC + ABC' + AB'C.",
           steps=[
               S("Take out AB from the first two terms", math=r"ABC + ABC' = AB(C + C') = AB"),
               S("Rewrite", math=r"F = AB + AB'C"),
               S("Take out A", math=r"A(B + B'C)"),
               S("Use A + A'B = A + B on the bracket", math=r"B + B'C = B + C"),
               S("Result", math=r"F = A(B + C) = AB + AC"),
           ],
           check=r"A = 1, B = 0, C = 1: original = 0 + 0 + 1 = 1; simplified = 0 + 1 = 1 \checkmark"),
        KEY("Handy shortcuts", r"Look for these patterns.",
            cards=[
                ["Combine", r"XY + XY' = X. The variable that changes drops out."],
                ["Consensus", r"AB + A'C + BC = AB + A'C. The third term is redundant."],
                ["Absorb", r"X + XY = X, and X + X'Y = X + Y."],
            ]),
        EX("Worked example 5: consensus",
           intro=r"Simplify AB + A'C + BC.",
           steps=[
               S("Multiply BC by (A + A') = 1", math=r"BC = BC(A + A') = ABC + A'BC"),
               S("Absorb", math=r"AB + ABC = AB \quad \text{and} \quad A'C + A'BC = A'C"),
               S("Result", math=r"AB + A'C"),
           ]),
        TIP(r"**Always check.** Pick two or three input rows and evaluate the original and the simplified expression. If any row disagrees, you have made an error."),
        H("Common mistakes"),
        MISTAKE(r"Dropping a variable that does not appear in both terms", r"XY + XY' = X only because the *same* X is in both terms. AB + A'C cannot be simplified this way."),
        MISTAKE(r"Using the wrong form for the 0 rows", r"A maxterm is the **sum** that is 0 for that row: for row 010 it is A + B' + C, not A'BC'."),
        MISTAKE(r"Not stating the law used", r"Examiners give marks for the method. Write the name of the law beside each line."),
        QUIZ(r"Which minterm is 1 only for the row A = 1, B = 0, C = 1?",
             ["A'BC'", "AB'C", "A + B' + C", "ABC"], 1, r"A is true, B complemented, C is true: AB'C.",
             hint=r"Use A as it is when it is 1, and A' when it is 0.",
             feedback=["That is the minterm for row 010.", "", "That is a maxterm, a sum.", "That is the minterm for row 111."]),
        QUIZ(r"Simplify AB + AB'.",
             ["B", "A", "A + B", "1"], 1, r"AB + AB' = A(B + B') = A . 1 = A.",
             hint=r"Take out A.",
             feedback=["B is the variable that drops out.", "", "AB + AB' is 1 only when A = 1.", "It is 1 only when A = 1."]),
        H("Practice questions"),
        PQ(r"A circuit has output 1 only for the input rows ABC = 011 and 111. Write the SOP expression and simplify it.",
           r"F = A'BC + ABC = BC(A' + A) = BC."),
        PQ(r"Write the POS form for a function that is 0 only for the rows ABC = 001 and 110.",
           r"Row 001: maxterm A + B + C'. Row 110: maxterm A' + B' + C. F = (A + B + C')(A' + B' + C)."),
        PQ(r"Simplify A'B + AB + AB' and name the laws used.",
           r"A'B + AB = B(A' + A) = B (complement law, identity). Then B + AB' = B + A, using X + X'Y = X + Y (with X = B, Y = A). So F = A + B."),
        PQ(r"Show that A + A'B + A'B' simplifies to 1.",
           r"A'B + A'B' = A'(B + B') = A' (complement). Then A + A' = 1 (complement law). So the expression is 1."),
        SUM(r"A minterm is an AND of all variables that is 1 for one row; SOP is the OR of the minterms where F = 1.",
            r"A maxterm is an OR of all variables that is 0 for one row; POS is the AND of the maxterms where F = 0.",
            r"Simplify with the laws: combine XY + XY' = X, absorb X + XY = X, and X + X'Y = X + Y.",
            r"Name the law at each step and check the result against the truth table."),
    ],
))

# ------------------------------------------------------------------ 15 Karnaugh maps: 2 and 3 variables
KM3_A = """       BC=00 01 11 10
  A=0    0     1     1     0
  A=1    0     1     1     1"""

KM3_B = """       BC=00 01 11 10
  A=0    1     1     1     1
  A=1    0     0     0     1"""

KM3_C = """       BC=00 01 11 10
  A=0    1     0     0     1
  A=1    1     1     0     1"""

LESSONS.append(lesson(
    module=LOGIC, topic=SIMP,
    title="Karnaugh maps for two and three variables",
    slug="csa-karnaugh-maps-2-3-variables",
    minutes=24,
    summary="Draw a Karnaugh map from a truth table using Gray code order, group the 1s in powers of two including wrap-around, and read off the simplest sum-of-products expression.",
    objectives=[
        "Explain why Karnaugh map rows and columns use Gray code order",
        "Place the 1s of a truth table on a 2-variable or 3-variable map",
        "Group adjacent 1s into the largest possible groups, including wrap-around groups",
        "Read the simplified expression from the groups and check it"
    ],
    key_concepts=["Karnaugh map", "Gray code", "Adjacent cells", "Group (loop)", "Wrap-around",
                  "Prime implicant", "Simplified expression"],
    blocks=[
        H("Introduction"),
        T(r"Algebra works, but it needs insight. A **Karnaugh map (K-map)** turns simplification into a picture: you circle the 1s "
          r"and read off the answer. It is a truth table drawn so that cells that differ by one variable sit side by side."),
        H("The layout"),
        D(r"In a K-map each cell is one row of the truth table (one minterm). The row and column labels follow **Gray code**, "
          r"where only one bit changes between neighbours: 00, 01, 11, 10 and **not** 00, 01, 10, 11.",
          title="Gray code order"),
        T(r"Because of Gray code, two cells that touch differ in exactly one variable, so the term for the pair no longer needs that "
          r"variable. This is the same idea as XY + XY' = X in algebra, but you can *see* it. The left and right edges also touch (the map wraps round), as do the top and bottom edges in a 4-variable map."),
        T(r"A 2-variable map has 4 cells; a 3-variable map has 8. For a 3-variable map put A on the rows and BC on the columns in the order 00, 01, 11, 10."),
        KEY("Rules for grouping", r"Follow them in this order.",
            cards=[
                ["Group size", r"Each group is a **rectangle** of 1, 2, 4 or 8 cells: a power of 2. Never 3, 5 or 6."],
                ["Make groups as large as possible", r"Bigger group means fewer variables in the term."],
                ["Cover every 1", r"Cells may be used in more than one group. Use as few groups as you can."],
                ["Wrap round", r"The first and last columns are neighbours. Diagonal cells are NOT neighbours."],
            ]),
        KEY("Reading a group", r"For each group, keep the variables that **stay the same** and drop the ones that change.",
            cards=[
                ["Variable is 1 in all cells", r"Write it as it is, for example B."],
                ["Variable is 0 in all cells", r"Write it complemented, for example B'."],
                ["Variable changes inside the group", r"Leave it out."],
            ],
            note=r"Then OR the terms of all the groups together."),
        EX("Worked example 1: two variables",
           intro=r"Simplify F = 1 for the minterms 1, 2 and 3 (AB = 01, 10, 11) using a 2-variable map.",
           steps=[
               S("Place the 1s", text=r"Row A = 0: cells B = 0, 1 hold 0, 1. Row A = 1: cells B = 0, 1 hold 1, 1."),
               S("Group", text=r"Column B = 1 (cells 01 and 11) is one pair. Row A = 1 (cells 10 and 11) is another pair."),
               S("Read", math=r"B \quad \text{and} \quad A"),
               S("Result", math=r"F = A + B"),
           ],
           check=r"AB = 00: A + B = 0 \checkmark \text{ (the only 0)}"),
        EX("Worked example 2: three variables",
           intro=r"Simplify F for the minterms 1, 3, 5, 6 and 7 (the same function as in the previous lesson).",
           steps=[
               S("Place the 1s", text=r"See the map below."),
               S("Group of four", text=r"Columns BC = 01 and 11 in both rows: m1, m3, m5, m7. Here only C stays 1 (A and B change), so the term is C."),
               S("Group of two", text=r"m6 and m7 (A = 1, B = 1, C changes): the term is AB."),
               S("Result", math=r"F = C + AB"),
           ],
           check=r"\text{Row } 110: C + AB = 0 + 1 = 1 \checkmark"),
        CODE(KM3_A, "text", title="Map for minterms 1, 3, 5, 6, 7"),
        EX("Worked example 3: a group of four and a pair",
           intro=r"Simplify F = 1 for the minterms 0, 1, 2, 3 and 6.",
           steps=[
               S("Group of four", text=r"The whole row A = 0 (m0, m1, m2, m3). A is 0 all through; B and C change. The term is A'."),
               S("Pair", text=r"m2 and m6 (BC = 10, A changes): B = 1 and C = 0 stay the same. The term is BC'."),
               S("Result", math=r"F = A' + BC'"),
           ]),
        CODE(KM3_B, "text", title="Map for minterms 0, 1, 2, 3, 6"),
        EX("Worked example 4: wrap-around",
           intro=r"Simplify F = 1 for the minterms 0, 2, 4, 5 and 6.",
           steps=[
               S("Group of four with wrap-around", text=r"Columns BC = 00 and 10 are neighbours across the edge: m0, m2, m4, m6. C is 0 throughout; A and B change. The term is C'."),
               S("Pair", text=r"m4 and m5 (A = 1, B = 0, C changes): the term is AB'."),
               S("Result", math=r"F = C' + AB'"),
           ],
           check=r"\text{Row } 101: C' + AB' = 0 + 1 = 1 \checkmark; \quad \text{row } 011: 0 + 0 = 0 \checkmark"),
        CODE(KM3_C, "text", title="Map for minterms 0, 2, 4, 5, 6"),
        TIP(r"Mark the cells in each group with a different colour or shape. Before you stop, check that **every 1 is in at least one group** and that no group can be made larger."),
        H("Common mistakes"),
        MISTAKE(r"Grouping three or six cells", r"Groups must hold 1, 2, 4 or 8 cells. Make a group of 4 and overlap a pair to cover the rest."),
        MISTAKE(r"Using the binary order 00, 01, 10, 11 for the columns", r"With that order, cells that look like neighbours differ in two bits. Always use 00, 01, 11, 10."),
        MISTAKE(r"Forgetting the wrap-around", r"The left and right columns touch. Missing this gives an answer that works but is not simplest."),
        QUIZ(r"Which is the correct column order for the variables BC on a 3-variable K-map?",
             ["00, 01, 10, 11", "00, 01, 11, 10", "00, 11, 01, 10", "01, 10, 11, 00"], 1, r"Gray code: only one bit changes between neighbours.",
             hint=r"Which order changes only one bit each step?",
             feedback=["01 to 10 changes two bits.", "", "00 to 11 changes two bits at once.", "01 to 10 changes two bits."]),
        QUIZ(r"A group of 4 cells on a 3-variable map has A = 1 in all cells and B, C changing. What is its term?",
             ["A'", "A", "BC", "AB"], 1, r"A stays 1 and the others change, so the term is A.",
             hint=r"Keep the variables that never change.",
             feedback=["A' would mean A = 0 in all cells.", "", "B and C change inside the group.", "B changes inside the group."]),
        H("Practice questions"),
        PQ(r"Explain why the columns of a K-map are labelled 00, 01, 11, 10.",
           r"Gray code changes only one bit between neighbouring columns. Cells that touch then differ in exactly one variable, so that variable can be dropped when they are grouped."),
        PQ(r"Use a 3-variable K-map to simplify F = 1 for the minterms 3, 7, 0 and 1 (ABC read as a number).",
           r"Pair m3 and m7 (BC = 11, A changes): BC. Pair m0 and m1 (A = 0, B = 0, C changes): A'B'. F = A'B' + BC."),
        PQ(r"Simplify F = 1 for the minterms 0, 1, 4 and 5 with a K-map.",
           r"The four cells are the columns BC = 00 and 01 in both rows. A and C change; B stays 0. The term is B', so F = B'."),
        PQ(r"State the three rules for choosing groups in a Karnaugh map.",
           r"Groups are rectangles of 1, 2, 4 or 8 cells (powers of 2). Groups should be as large as possible. Every 1 must be in at least one group, using as few groups as possible. Cells can be reused; edges wrap round."),
        SUM(r"A K-map lays out the truth table so neighbouring cells differ in one variable; labels use Gray code 00, 01, 11, 10.",
            r"Group adjacent 1s in rectangles of 1, 2, 4 or 8; use the largest groups and cover every 1; edges wrap round.",
            r"Read each group: keep the variables that stay the same, drop the ones that change, then OR the terms.",
            r"Check the answer against the truth table for a couple of rows."),
    ],
))

# ------------------------------------------------------------------ 16 Karnaugh maps: 4 variables and don't cares
KM4_B = """          CD=00 01 11 10
  AB=00    0     0     1     1
  AB=01    0     0     1     1
  AB=11    0     0     1     1
  AB=10    1     0     1     1"""

KM4_C = """          CD=00 01 11 10
  AB=00    0     0     0     0
  AB=01    0     1     1     1
  AB=11    X     X     X     X
  AB=10    1     1     X     X"""

LESSONS.append(lesson(
    module=LOGIC, topic=SIMP,
    title="Karnaugh maps for four variables, with don't-care conditions",
    slug="csa-karnaugh-maps-4-variables-dont-care",
    minutes=25,
    summary="Simplify four-variable functions with Karnaugh maps using groups of 2, 4 and 8 cells including corners and edges, and use don't-care cells to make bigger groups.",
    objectives=[
        "Lay out a 4-variable map and place minterms from their numbers",
        "Group cells in pairs, quads and octets, including the four corners and edge wrap-around",
        "Read the product term of each group and write the simplified sum of products",
        "Use don't-care conditions to enlarge groups, and explain why this is allowed"
    ],
    key_concepts=["4-variable K-map", "Quad", "Octet", "Corner group", "Don't-care condition",
                  "Essential prime implicant", "BCD"],
    blocks=[
        H("Introduction"),
        T(r"Real designs have more than three inputs. A traffic controller at a Yaoundé junction may read four sensors. "
          r"The four-variable Karnaugh map has 16 cells and the same rules as before, but both pairs of opposite edges touch: "
          r"the map is wrapped like a tube in both directions."),
        H("The 4-variable map"),
        T(r"Put AB on the rows and CD on the columns, both in the order 00, 01, 11, 10. The minterm number of a cell is 8A + 4B + 2C + D."),
        CODE("          CD=00  01  11  10\n"
             "  AB=00     m0  m1  m3  m2\n"
             "  AB=01     m4  m5  m7  m6\n"
             "  AB=11    m12 m13 m15 m14\n"
             "  AB=10     m8  m9 m11 m10",
             "text", title="Minterm numbers on a 4-variable map"),
        KEY("Group sizes and what they drop", r"The larger the group, the fewer the variables.",
            cards=[
                ["1 cell", r"All 4 variables stay: a full minterm."],
                ["Pair (2 cells)", r"1 variable drops out: a term with 3 variables."],
                ["Quad (4 cells)", r"2 variables drop out: a term with 2 variables."],
                ["Octet (8 cells)", r"3 variables drop out: a term with 1 variable."],
            ],
            note=r"The four corners (m0, m2, m8, m10) form a quad. The four cells in a row or column form a quad too."),
        EX("Worked example 1: corners and the centre",
           intro=r"Simplify F = 1 for the minterms 0, 2, 5, 7, 8, 10, 13 and 15.",
           steps=[
               S("Place the 1s", text=r"See Figure 1."),
               S("Quad of corners", text=r"m0, m2, m8, m10. B = 0 and D = 0 in all four; A and C change. The term is B'D'."),
               S("Quad in the centre", text=r"m5, m7, m13, m15. B = 1 and D = 1 in all four; A and C change. The term is BD."),
               S("Result", math=r"F = BD + B'D'"),
           ],
           check=r"\text{Row } 1010 \ (m10): B'D' = 1 \checkmark; \quad \text{row } 0001 \ (m1): BD + B'D' = 0 \checkmark"),
        IMG("al-csa-kmap4.svg",
            "A 4-variable Karnaugh map with the 1s of minterms 0, 2, 5, 7, 8, 10, 13 and 15. The four corner cells form one group B'D', and the four centre cells form a second group BD.",
            caption="Figure 1. The four corners wrap round to form one group of four."),
        EX("Worked example 2: an octet and a pair",
           intro=r"Simplify F = 1 for the minterms 2, 3, 6, 7, 8, 10, 11, 14 and 15.",
           steps=[
               S("Octet", text=r"The two right-hand columns CD = 11 and 10 hold m2, m3, m6, m7, m10, m11, m14, m15. C = 1 in all eight; A, B and D change. The term is C."),
               S("Pair", text=r"m8 is still uncovered. It joins m10 across the map (CD = 00 and 10 touch): A = 1, B = 0, D = 0 stay; C changes. The term is AB'D'."),
               S("Result", math=r"F = C + AB'D'"),
           ],
           check=r"\text{Row } 1000 \ (m8): 0 + 1 = 1 \checkmark; \quad \text{row } 0100 \ (m4): 0 + 0 = 0 \checkmark"),
        CODE(KM4_B, "text", title="Map for minterms 2, 3, 6, 7, 8, 10, 11, 14, 15"),
        TIP(r"Start with the **hardest** cells: a 1 that can be grouped only one way. Make that group first, then cover what is left with the largest groups you can."),
        H("Don't-care conditions"),
        D(r"A **don't-care** condition is an input combination that never happens, or whose output does not matter. "
          r"In the map it is written X. An X may be treated as 1 if that makes a **bigger group**, and as 0 otherwise. "
          r"It never *has* to be covered.",
          title="Don't-care"),
        T(r"A classic case is **BCD**: a decimal digit 0 to 9 is stored in 4 bits, so the codes 1010 to 1111 (10 to 15) never occur. Their outputs are don't cares."),
        EX("Worked example 3: digit 5 or more",
           intro=r"A BCD digit ABCD enters a circuit. F = 1 when the digit is 5, 6, 7, 8 or 9. Codes 10 to 15 never occur. Find the simplest expression.",
           steps=[
               S("Place the 1s and the X cells", text=r"1s at m5, m6, m7, m8 and m9. X at m10 to m15 (see the map below)."),
               S("Group 1: the bottom half", text=r"Using X cells, m8, m9, m10, m11, m12, m13, m14, m15 (A = 1) make an octet. The term is A."),
               S("Group 2", text=r"m5, m7, m13 and m15 (B = 1, D = 1; m13 and m15 are X). The term is BD."),
               S("Group 3", text=r"m6, m7, m14 and m15 (B = 1, C = 1; m14 and m15 are X). The term is BC."),
               S("Result", math=r"F = A + BD + BC"),
           ],
           check=r"\text{Digit } 4 = 0100: 0 + 0 + 0 = 0 \checkmark; \quad \text{digit } 6 = 0110: BC = 1 \checkmark"),
        CODE(KM4_C, "text", title="Map for digit 5 or more (X = don't care)"),
        T(r"Without the don't cares, the same function would need more terms with more variables. That means fewer gates."),
        H("Common mistakes"),
        MISTAKE(r"Forgetting the corners", r"The four corner cells touch each other. A function with 1s in all four corners is the quad B'D' (when they are m0, m2, m8, m10)."),
        MISTAKE(r"Using an X as a 1 outside any group", r"A don't care is only used to make a group bigger. You do not need to cover every X."),
        MISTAKE(r"Making groups that are not a power of 2, or not rectangular", r"A group of 6 or an L-shape is not allowed. Split it into groups of 4 and 2, overlapping if needed."),
        QUIZ(r"The four corner cells m0, m2, m8 and m10 of a 4-variable map form one group. What is its term?",
             ["A'C'", "B'D'", "A'B'C'D'", "BD"], 1, r"B = 0 and D = 0 in all four; A and C change. The term is B'D'.",
             hint=r"Write the four minterms in binary and see which bits never change.",
             feedback=["A changes between m0 and m8.", "", "That is only the single cell m0.", "That would be the central four cells."]),
        QUIZ(r"How many variables does the term of an octet (8 cells) on a 4-variable map contain?",
             ["0", "1", "2", "3"], 1, r"Three variables change, so one stays: the term has 1 variable.",
             hint=r"Each doubling of the group drops one variable.",
             feedback=["A group of 16 (the whole map) gives 0 variables, the constant 1.", "", "That is a quad.", "That is a pair."]),
        H("Practice questions"),
        PQ(r"Simplify F = 1 for the minterms 0, 2, 8 and 10 with a K-map.",
           r"These are the four corner cells. B = 0 and D = 0 in all of them; A and C change. F = B'D'."),
        PQ(r"Simplify F = 1 for the minterms 0, 1, 2, 5, 8, 9, 10 and 13 using a 4-variable K-map.",
           r"Quad 1: the four corners m0, m2, m8, m10 (B = 0, D = 0): B'D'. Quad 2: the column CD = 01, m1, m5, m9, m13 (C = 0, D = 1): C'D. All eight 1s are covered. F = B'D' + C'D."),
        PQ(r"A BCD digit circuit gives 1 for the digits 8 and 9 only. Codes 10 to 15 never occur (don't cares). Find the simplest expression.",
           r"The cells m8 to m15 (the whole bottom half, A = 1) are each a 1 or a don't care, so they form an octet. B, C and D change; A stays 1. F = A."),
        PQ(r"Explain what a don't-care condition is and why it can make the circuit simpler.",
           r"It is an input combination that never occurs, or whose output does not matter. In a K-map we may take it as 1 when this makes a larger group, so the term has fewer variables and the circuit needs fewer or smaller gates. We take it as 0 when it would not help."),
        SUM(r"A 4-variable map has 16 cells in Gray code order; both pairs of opposite edges touch, and the four corners form a quad.",
            r"Group sizes 1, 2, 4, 8: a quad drops two variables, an octet three.",
            r"Read each group by keeping the variables that do not change; OR the terms together.",
            r"Don't cares (X) can be used as 1s to enlarge groups but need not be covered; BCD codes 10 to 15 are the classic case."),
    ],
))
