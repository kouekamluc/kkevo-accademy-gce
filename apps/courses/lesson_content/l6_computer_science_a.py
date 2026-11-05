"""Lower Sixth Computer Science (part A): architecture, digital logic, operating systems and translators.

KKEVO draft teaching material. A reviewer checks each lesson against the official syllabus before publishing.
"""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "lower-sixth")

LESSONS = []

# ---------------------------------------------------------------- Machine models
LESSONS.append(lesson(
    module="Computer Organization & Architecture",
    topic="Machine models",
    title="Von Neumann and Harvard architectures, and the system buses",
    slug="von-neumann-harvard-and-buses",
    minutes=25,
    summary="Compare the Von Neumann and Harvard machine models and explain how the data, address and control buses connect the CPU, memory and I/O.",
    objectives=[
        "Describe the stored-program concept and the Von Neumann architecture",
        "Compare Von Neumann and Harvard architectures and give a use for each",
        "State the role and direction of the data, address and control buses",
        "Calculate addressable memory from the width of the address bus",
    ],
    key_concepts=["Stored-program concept", "Von Neumann architecture", "Harvard architecture",
                  "Von Neumann bottleneck", "Data bus", "Address bus", "Control bus"],
    blocks=[
        H("Introduction"),
        T(r"Every computer, from a laptop in a Yaoundé cyber café to the small controller inside a mobile money "
          r"receipt printer, follows a **machine model**. The model says where instructions and data are kept and how "
          r"they travel to the processor."),
        T(r"Two models matter at A Level: the **Von Neumann** model used by most general-purpose computers, and the "
          r"**Harvard** model used by many microcontrollers and digital signal processors. Both rely on **buses** to "
          r"move information."),
        H("The stored-program concept"),
        D(r"In the **stored-program concept**, program instructions are stored in main memory in the same way as data. "
          r"The processor fetches instructions from memory one at a time and executes them in sequence, unless an "
          r"instruction changes the order (a jump or branch).",
          title="Stored-program concept"),
        D(r"The **Von Neumann architecture** has a single memory that holds both instructions and data, and a single "
          r"set of buses connecting that memory to the CPU. The CPU contains a control unit, an arithmetic logic unit "
          r"(ALU) and registers.",
          title="Von Neumann architecture",
          note=r"Because instructions and data share one path, only one of them can be transferred at a time."),
        D(r"The **Harvard architecture** keeps instructions and data in **physically separate memories**, each with its "
          r"own buses. The CPU can fetch the next instruction while it reads or writes data.",
          title="Harvard architecture"),
        KEY("Von Neumann vs Harvard", r"The key difference is whether instructions and data share one memory and one set of buses.",
            cards=[
                ["Von Neumann", r"One memory, one set of buses. Simple and flexible: memory can be split between program and data as needed. Suffers from the Von Neumann bottleneck."],
                ["Harvard", r"Separate instruction and data memories and buses. Instruction fetch and data access can happen at the same time, so it is faster for fixed tasks. More complex, and spare program memory cannot be used for data."],
            ],
            note=r"Many modern CPUs are a mix: separate instruction and data caches (Harvard-like) in front of one shared main memory (Von Neumann)."),
        IMG("cs-von-neumann-vs-harvard.svg",
            "Von Neumann: one CPU joined to one memory, holding instructions and data, by a single set of buses. Harvard: one CPU joined to an instruction memory and a data memory, each by its own buses, so both can be used at the same time.",
            caption="Figure 1. Von Neumann uses one memory and one set of buses; Harvard uses separate instruction and data memories, each with its own buses."),
        D(r"The **Von Neumann bottleneck** is the limit on performance caused by instructions and data sharing a single "
          r"bus to memory. The CPU often waits for memory transfers rather than doing useful work.",
          title="Von Neumann bottleneck"),
        H("The system buses"),
        T(r"A **bus** is a set of parallel wires (lines) that carries signals between components. The **system bus** is "
          r"made of three parts."),
        KEY("The three buses", r"Learn each bus by what it carries and in which direction.",
            cards=[
                ["Address bus", r"Carries the memory address (or I/O port) the CPU wants to use. **Unidirectional**: from the CPU to memory and I/O. Its width decides how many locations can be addressed."],
                ["Data bus", r"Carries data and instructions being transferred. **Bidirectional**: CPU to memory when writing, memory to CPU when reading. Its width decides how many bits move per transfer."],
                ["Control bus", r"Carries control and timing signals such as memory read, memory write, clock, interrupt request and bus request. Individual lines go in either direction, so the bus as a whole is **bidirectional**."],
            ]),
        IMG("cs-system-buses.svg",
            "CPU, memory and I/O joined to three buses. Address bus arrows go only from the CPU to memory and I/O (one-way). Data bus and control bus links have arrows at both ends (two-way).",
            caption="Figure 2. The address bus is one-way (CPU to memory and I/O); the data and control buses are two-way."),
        D(r"With $n$ address lines, the CPU can form $2^n$ different addresses. If each address holds one byte, the "
          r"addressable memory is $2^n$ bytes.",
          title="Address bus width", formula=r"\text{number of addresses} = 2^{n}"),
        EX("Worked example 1: memory size from the address bus",
           intro=r"A microcontroller has a 16-bit address bus and each memory location stores one byte. (a) How many "
                 r"locations can it address? (b) Give the answer in KiB. (c) What is the highest address in hexadecimal?",
           steps=[
               S("Count the addresses", math=r"2^{16} = 65\,536 \text{ locations}"),
               S("Convert to bytes", text=r"Each location holds 1 byte, so the memory is 65 536 bytes."),
               S("Convert to KiB", math=r"65\,536 \div 1024 = 64 \text{ KiB}"),
               S("Highest address", text=r"Addresses run from 0 to $2^{16} - 1 = 65\,535$. In hexadecimal that is FFFF (sixteen 1s in binary)."),
           ],
           check=r"0000_{16} \text{ to } \text{FFFF}_{16} \text{ is } 65\,536 \text{ addresses}"),
        EX("Worked example 2: word-addressable memory and the data bus",
           intro=r"A processor has a 24-bit address bus and a 16-bit data bus. Memory is **word-addressable** with "
                 r"16-bit (2-byte) words. (a) Find the maximum memory in MiB. (b) How many bus transfers are needed to "
                 r"read a 64-bit value?",
           steps=[
               S("Count the addresses", math=r"2^{24} = 16\,777\,216 \text{ words}"),
               S("Bytes per word", text=r"Each word is 16 bits = 2 bytes."),
               S("Total bytes", math=r"2^{24} \times 2 = 2^{25} = 33\,554\,432 \text{ bytes}"),
               S("Convert to MiB", math=r"2^{25} \div 2^{20} = 2^{5} = 32 \text{ MiB}"),
               S("Transfers for 64 bits", math=r"64 \div 16 = 4 \text{ transfers}"),
           ]),
        EX("Worked example 3: the buses during a memory read",
           intro=r"Describe the use of the buses when the CPU reads the byte stored at address 2A0F (hexadecimal).",
           steps=[
               S("Place the address", text=r"The CPU puts 2A0F on the **address bus**."),
               S("Signal a read", text=r"The control unit activates the **memory read** line on the control bus."),
               S("Memory responds", text=r"Memory decodes the address and places the stored byte on the **data bus**."),
               S("CPU stores the value", text=r"The CPU copies the value from the data bus into a register (the MDR). The data bus carried data towards the CPU, which is why it must be bidirectional."),
           ]),
        H("Common mistakes"),
        MISTAKE("Saying the address bus is bidirectional",
                r"Only the CPU (or a DMA controller acting for it) places addresses on the bus, so the address bus is one-way. The data bus is the two-way one."),
        MISTAKE("Mixing up bus width and memory size",
                r"Address bus width sets **how many locations** exist ($2^n$). Data bus width sets **how many bits move per transfer**. A wider data bus does not add memory."),
        MISTAKE("Saying Harvard is better in every case",
                r"Harvard allows simultaneous instruction and data access, but it is less flexible: unused program memory cannot be given to data. Always state the trade-off."),
        QUIZ(r"A CPU has 20 address lines and byte-addressable memory. What is the maximum memory it can address?",
             [r"20 bytes", r"1 MiB", r"1 KiB", r"400 bytes"], 1,
             r"$2^{20} = 1\,048\,576$ bytes, which is exactly 1 MiB.",
             hint=r"Work out $2^{n}$ with $n = 20$.",
             feedback=[r"The number of lines is not the number of addresses; each extra line doubles the count.", "",
                       r"$2^{10}$ bytes is 1 KiB; you need $2^{20}$.",
                       r"$20^2$ squares the number of lines; the rule is $2^{20}$."]),
        QUIZ(r"Which feature best describes the Harvard architecture?",
             [r"Instructions and data share one memory", r"There is no control bus",
              r"Instructions and data are held in separate memories with separate buses", r"It cannot run stored programs"], 2,
             r"Separate instruction and data memories, each with its own bus, define the Harvard model.",
             feedback=[r"That describes Von Neumann.", r"Both models need control signals.", "",
                       r"Harvard machines still store their programs, in instruction memory."]),
        H("Practice questions"),
        PQ(r"(a) State what is meant by the stored-program concept. (b) Explain the Von Neumann bottleneck. [4 marks]",
           r"(a) Program instructions are stored in main memory alongside data (1); they are fetched and executed one at a time in sequence (1). (b) Instructions and data share one bus between CPU and memory (1), so only one transfer happens at a time and the CPU must wait for memory, limiting speed (1)."),
        PQ(r"A computer has a 32-bit address bus and byte-addressable memory. Calculate the maximum memory in GiB. Show your working. [2 marks]",
           r"$2^{32}$ bytes (1). $2^{32} \div 2^{30} = 2^{2} = 4$ GiB (1)."),
        PQ(r"Give **two** advantages of the Harvard architecture and **one** typical use. [3 marks]",
           r"Instruction fetch and data access can happen at the same time, giving higher throughput (1). Instruction and data memories can have different word lengths and technologies, for example the program in flash and data in RAM, and a data write cannot accidentally overwrite the program (1). Typical use: microcontrollers in embedded devices or digital signal processors (1)."),
        PQ(r"Explain why the data bus is bidirectional but the address bus is unidirectional. [2 marks]",
           r"Data must travel to memory when the CPU writes and from memory when it reads, so the data bus works both ways (1). Addresses are generated by the CPU and sent to memory or I/O, so the address bus only goes one way (1)."),
        SUM(r"Stored-program concept: instructions and data are kept in memory and fetched one at a time.",
            r"Von Neumann: one memory and one set of buses for instructions and data; flexible but limited by the Von Neumann bottleneck.",
            r"Harvard: separate instruction and data memories and buses; simultaneous access, common in microcontrollers and DSPs.",
            r"Address bus: one-way, CPU to memory; $n$ lines give $2^n$ addresses.",
            r"Data bus: two-way; its width is the number of bits per transfer. Control bus: read, write, clock and interrupt signals."),
    ],
))

# ---------------------------------------------------------------- The CPU
CPU_TRACE = """
Program in memory (accumulator machine)
  Address  Contents
  100      LDA 200     ; ACC <- contents of 200
  101      ADD 201     ; ACC <- ACC + contents of 201
  102      STO 202     ; contents of 202 <- ACC
  200      15
  201      27
  202      0

Step                         PC    MAR   MDR       CIR       ACC
Start                        100   -     -         -         0
Fetch: MAR <- PC             100   100   -         -         0
Fetch: MDR <- [MAR]          100   100   LDA 200   -         0
Fetch: PC <- PC + 1          101   100   LDA 200   -         0
Fetch: CIR <- MDR            101   100   LDA 200   LDA 200   0
Execute: MAR <- 200          101   200   LDA 200   LDA 200   0
Execute: MDR <- [MAR]        101   200   15        LDA 200   0
Execute: ACC <- MDR          101   200   15        LDA 200   15
Fetch: MAR <- PC             101   101   15        LDA 200   15
Fetch: MDR <- [MAR]          101   101   ADD 201   LDA 200   15
Fetch: PC <- PC + 1          102   101   ADD 201   LDA 200   15
Fetch: CIR <- MDR            102   101   ADD 201   ADD 201   15
Execute: MAR <- 201          102   201   ADD 201   ADD 201   15
Execute: MDR <- [MAR]        102   201   27        ADD 201   15
Execute: ACC <- ACC + MDR    102   201   27        ADD 201   42
"""

PIPELINE = """
3-stage pipeline, 6 instructions (I1 to I6), one clock cycle per stage
F = fetch, D = decode, E = execute

Cycle:   1   2   3   4   5   6   7   8
I1       F   D   E
I2           F   D   E
I3               F   D   E
I4                   F   D   E
I5                       F   D   E
I6                           F   D   E

Without pipelining: 6 x 3 = 18 cycles
With pipelining:    3 + (6 - 1) = 8 cycles
"""

LESSONS.append(lesson(
    module="Computer Organization & Architecture",
    topic="The CPU",
    title="The fetch–decode–execute cycle, registers and pipelining",
    slug="fetch-decode-execute-and-pipelining",
    minutes=30,
    summary="Trace the fetch–decode–execute cycle register by register using the PC, MAR, MDR, CIR and ACC, and explain how pipelining speeds up execution.",
    objectives=[
        "State the purpose of the PC, MAR, MDR, CIR and ACC",
        "Describe the fetch–decode–execute cycle in register transfer notation",
        "Trace the contents of registers while a short program runs",
        "Explain pipelining, calculate cycle counts and describe a branch hazard",
    ],
    key_concepts=["Program Counter (PC)", "Memory Address Register (MAR)", "Memory Data Register (MDR)",
                  "Current Instruction Register (CIR)", "Accumulator (ACC)", "Fetch–decode–execute cycle",
                  "Pipelining", "Pipeline hazard"],
    blocks=[
        H("Introduction"),
        T(r"A processor runs millions of instructions every second, but each one goes through the same three stages: "
          r"**fetch** it from memory, **decode** it, then **execute** it. Exam questions often ask you to trace this "
          r"cycle step by step, showing what each register holds."),
        T(r"In this lesson you will learn the special-purpose registers, write the cycle in register transfer "
          r"notation, trace a short program, and see how **pipelining** overlaps instructions to save time."),
        H("The special-purpose registers"),
        KEY("Registers used in the cycle", r"A register is a very fast storage location inside the CPU.",
            cards=[
                ["PC (Program Counter)", r"Holds the **address of the next instruction** to be fetched."],
                ["MAR (Memory Address Register)", r"Holds the **address** of the memory location about to be read or written. Connected to the address bus."],
                ["MDR (Memory Data Register)", r"Holds the **data or instruction** just read from memory, or about to be written. Connected to the data bus. Also called the MBR."],
                ["CIR (Current Instruction Register)", r"Holds the **instruction being decoded and executed**, split into opcode and operand."],
                ["ACC (Accumulator)", r"A general working register that holds the **result** of ALU operations."],
            ]),
        IMG("cs-cpu-registers.svg",
            "CPU containing the control unit, ALU, ACC, PC, MAR, CIR and MDR. Arrows: PC to MAR, MDR to CIR, CIR to control unit. MAR sends addresses to main memory on the address bus; MDR uses the two-way data bus; the control bus links the control unit and memory.",
            caption="Figure 1. The special-purpose registers and how they connect to main memory. Blue arrows show the path of an instruction during fetch."),
        D(r"Square brackets mean **the contents of**. So $[\text{PC}]$ is the value held in the PC, and "
          r"$[[\text{MAR}]]$ is the contents of the memory location whose address is in the MAR. The arrow "
          r"$\leftarrow$ means **is copied into**.",
          title="Register transfer notation"),
        H("The fetch–decode–execute cycle"),
        F(r"\begin{aligned}&\text{MAR} \leftarrow [\text{PC}]\\&\text{PC} \leftarrow [\text{PC}] + 1 \quad \text{and} \quad \text{MDR} \leftarrow [[\text{MAR}]]\\&\text{CIR} \leftarrow [\text{MDR}]\end{aligned}",
          title="The fetch stage"),
        T(r"The PC is incremented while the memory read takes place, so it already points to the next instruction. "
          r"In the **decode** stage the control unit splits the instruction in the CIR into its **opcode** (what to "
          r"do) and **operand** (what to do it to). In the **execute** stage the control unit sends signals to carry "
          r"it out, for example loading a value, using the ALU, or changing the PC for a jump."),
        IMG("cs-fde-cycle.svg",
            "Three boxes in a loop. Fetch: MAR gets [PC]; PC gets [PC] + 1 and MDR gets [[MAR]]; CIR gets [MDR]. Decode: the CU splits the CIR into opcode and operand. Execute: the CU sends signals to load, use the ALU, store or jump. Then back to fetch.",
            caption="Figure 2. The fetch–decode–execute cycle repeats for every instruction."),
        TIP(r"A jump instruction is executed by copying its operand into the PC: $\text{PC} \leftarrow$ operand. The next fetch then starts from the new address."),
        T(r"The trace below shows a short program on an accumulator machine. Each row is one register transfer. A dash means the register value is not yet known or not relevant."),
        CODE(CPU_TRACE, "text", title="Trace of LDA 200 then ADD 201",
             caption="Fetch steps are the same for every instruction; execute steps depend on the opcode."),
        EX("Worked example 1: what happens next",
           intro=r"Continue the trace above for the instruction at address 102, STO 202. Give the final contents of PC, MAR, MDR, CIR, ACC and memory location 202.",
           steps=[
               S("Fetch: copy PC to MAR", math=r"\text{MAR} \leftarrow 102"),
               S("Fetch: read memory and increment PC", math=r"\text{MDR} \leftarrow \text{STO 202}, \quad \text{PC} \leftarrow 103"),
               S("Fetch: copy MDR to CIR", math=r"\text{CIR} \leftarrow \text{STO 202}"),
               S("Decode", text=r"Opcode STO (store), operand 202."),
               S("Execute: set the address", math=r"\text{MAR} \leftarrow 202"),
               S("Execute: put the accumulator value in the MDR", math=r"\text{MDR} \leftarrow [\text{ACC}] = 42"),
               S("Execute: write to memory", text=r"Location 202 now holds 42. Final values: PC = 103, MAR = 202, MDR = 42, CIR = STO 202, ACC = 42."),
           ],
           check=r"15 + 27 = 42"),
        H("Pipelining"),
        D(r"**Pipelining** splits instruction processing into stages and lets different instructions occupy different "
          r"stages at the same time. While one instruction is executed, the next is decoded and the one after that is "
          r"fetched.",
          title="Pipelining",
          formula=r"\text{cycles} = k + (n - 1)",
          note=r"For a $k$-stage pipeline with $n$ instructions and one cycle per stage, ignoring hazards. Without a pipeline it takes $k \times n$ cycles."),
        CODE(PIPELINE, "text", title="Pipeline timing diagram"),
        EX("Worked example 2: pipeline speed-up",
           intro=r"A 4-stage pipeline (fetch, decode, execute, write back) runs 20 instructions. Each stage takes one clock cycle. Find the cycles needed with and without pipelining, and the speed-up.",
           steps=[
               S("Without pipelining", math=r"4 \times 20 = 80 \text{ cycles}"),
               S("With pipelining", math=r"4 + (20 - 1) = 23 \text{ cycles}"),
               S("Speed-up", math=r"80 \div 23 \approx 3.48"),
               S("Comment", text=r"As $n$ grows, the speed-up approaches the number of stages, 4. Hazards reduce it in practice."),
           ]),
        D(r"A **pipeline hazard** stops the next instruction entering or completing a stage on time. A **control "
          r"(branch) hazard** happens when a jump is taken: the instructions already fetched after it are wrong and "
          r"must be **flushed**, wasting cycles. A **data hazard** happens when an instruction needs a result that an "
          r"earlier instruction has not yet produced.",
          title="Pipeline hazards"),
        H("Common mistakes"),
        MISTAKE("Saying the PC holds the current instruction",
                r"The PC holds an **address**, the address of the **next** instruction. The current instruction itself is in the CIR."),
        MISTAKE("Putting data straight into the CIR or ACC from memory",
                r"Everything read from memory passes through the MDR first. Write MDR $\leftarrow$ [[MAR]] before CIR $\leftarrow$ [MDR] or ACC $\leftarrow$ [MDR]."),
        MISTAKE("Using k times n for pipelined time",
                r"That is the non-pipelined time. With a pipeline the first instruction takes $k$ cycles and each later one finishes one cycle after the previous: $k + n - 1$."),
        QUIZ(r"During the fetch stage, which register receives the address held in the PC?",
             [r"MDR", r"CIR", r"MAR", r"ACC"], 2,
             r"The first step of fetch is $\text{MAR} \leftarrow [\text{PC}]$, because the MAR is the register connected to the address bus.",
             feedback=[r"The MDR receives the instruction after the memory read, not the address.",
                       r"The CIR receives the instruction from the MDR at the end of fetch.", "",
                       r"The ACC holds data results, not addresses for fetching."]),
        QUIZ(r"A 5-stage pipeline executes 10 instructions with no hazards, one cycle per stage. How many cycles are needed?",
             [r"50", r"15", r"14", r"10"], 2,
             r"$5 + (10 - 1) = 14$ cycles.",
             feedback=[r"$5 \times 10$ is the time without pipelining.",
                       r"$5 + 10$ counts the first instruction twice; subtract 1.", "",
                       r"Even with a pipeline, the first instruction needs 5 cycles to pass through all stages."]),
        H("Practice questions"),
        PQ(r"Describe, using register transfer notation, the fetch stage of the fetch–decode–execute cycle. [4 marks]",
           r"$\text{MAR} \leftarrow [\text{PC}]$: the address of the next instruction is copied to the MAR (1). $\text{MDR} \leftarrow [[\text{MAR}]]$: the instruction at that address is read into the MDR via the data bus (1). $\text{PC} \leftarrow [\text{PC}] + 1$: the PC is incremented to point to the next instruction (1). $\text{CIR} \leftarrow [\text{MDR}]$: the instruction is copied into the CIR ready for decoding (1)."),
        PQ(r"Memory holds: 50: LDA 60, 51: SUB 61, 52: STO 62, 60: 90, 61: 35. The PC starts at 50. State the contents of the PC, CIR and ACC after the instruction at 51 has been executed. [3 marks]",
           r"PC = 52, since it was incremented during the fetch of the instruction at 51 (1). CIR = SUB 61 (1). ACC = 90 minus 35 = 55 (1)."),
        PQ(r"(a) Explain what is meant by pipelining. (b) Explain why a conditional jump can reduce the benefit of pipelining. [4 marks]",
           r"(a) Instruction processing is divided into stages (1) and the stages of different instructions are overlapped, so several instructions are being processed at once (1). (b) The instructions after the jump are fetched and decoded before the jump is executed (1); if the jump is taken they are the wrong instructions and must be flushed, so cycles are wasted (1)."),
        PQ(r"A 3-stage pipeline runs 100 instructions, one clock cycle per stage, no hazards. The clock is 1 GHz. Find the time taken with and without pipelining. [3 marks]",
           r"One cycle takes $1 \div 10^{9}$ s = 1 ns. Without pipelining: $3 \times 100 = 300$ cycles = 300 ns (1). With pipelining: $3 + 99 = 102$ cycles (1) = 102 ns (1)."),
        SUM(r"PC holds the address of the next instruction; MAR holds the address being accessed; MDR holds the data or instruction transferred.",
            r"CIR holds the instruction being decoded and executed; ACC holds ALU results.",
            r"Fetch: MAR $\leftarrow$ [PC]; MDR $\leftarrow$ [[MAR]] and PC $\leftarrow$ [PC] + 1; CIR $\leftarrow$ [MDR].",
            r"Decode splits the instruction into opcode and operand; execute carries it out.",
            r"Pipelining overlaps stages: $k + n - 1$ cycles instead of $k \times n$; branch and data hazards reduce the gain."),
    ],
))

# ---------------------------------------------------------------- Combinational circuits
HALF_ADDER_TT = """
Half adder
A  B | S  C
0  0 | 0  0
0  1 | 1  0
1  0 | 1  0
1  1 | 0  1
"""

FULL_ADDER_TT = """
Full adder
A  B  Cin | S  Cout
0  0  0   | 0  0
0  0  1   | 1  0
0  1  0   | 1  0
0  1  1   | 0  1
1  0  0   | 1  0
1  0  1   | 0  1
1  1  0   | 0  1
1  1  1   | 1  1
"""

RIPPLE_ADD = """
4-bit ripple carry adder: 0110 + 0111

Bit        A  B  Cin | S  Cout
bit 0      0  1  0   | 1  0
bit 1      1  1  0   | 0  1
bit 2      1  1  1   | 1  1
bit 3      0  0  1   | 1  0

Result S3 S2 S1 S0 = 1101, final carry out = 0
Check: 6 + 7 = 13 = 1101 in binary
"""

MUX_DECODER_TT = """
4-to-1 multiplexer            2-to-4 decoder (A is the MSB)
S1  S0 | Y                    A  B | D0  D1  D2  D3
0   0  | I0                   0  0 | 1   0   0   0
0   1  | I1                   0  1 | 0   1   0   0
1   0  | I2                   1  0 | 0   0   1   0
1   1  | I3                   1  1 | 0   0   0   1
"""

LESSONS.append(lesson(
    module="Digital Logic",
    topic="Combinational circuits",
    title="Adders, multiplexers and decoders",
    slug="adders-multiplexers-and-decoders",
    minutes=30,
    summary="Build and analyse half adders, full adders, ripple carry adders, multiplexers and decoders using truth tables and Boolean expressions.",
    objectives=[
        "Define a combinational circuit",
        "Derive the truth tables and Boolean expressions for half and full adders",
        "Trace binary addition through a ripple carry adder",
        "Describe multiplexers and decoders and write their output expressions",
    ],
    key_concepts=["Combinational circuit", "Half adder", "Full adder", "Ripple carry adder",
                  "Multiplexer", "Decoder", "Select line"],
    blocks=[
        H("Introduction"),
        T(r"Inside the ALU, binary numbers are added by circuits built from simple gates. Other circuits choose "
          r"between several signals or pick out one memory chip from many. All of these are **combinational "
          r"circuits**. In this lesson we write AND as $A \cdot B$, OR as $A + B$, NOT as $\overline{A}$, and exclusive "
          r"OR (XOR) as $A \oplus B$, which is 1 when exactly one input is 1."),
        D(r"A **combinational circuit** is a logic circuit whose outputs depend **only on the current inputs**. It has "
          r"no memory: the same inputs always give the same outputs.",
          title="Combinational circuit",
          note=r"Compare with sequential circuits (next lesson), whose outputs also depend on what happened before."),
        H("The half adder"),
        D(r"A **half adder** adds two single bits $A$ and $B$. It produces a **sum** bit $S$ and a **carry** bit $C$. "
          r"It cannot accept a carry in from a previous column.",
          title="Half adder",
          formula=r"S = A \oplus B = \overline{A}\cdot B + A\cdot\overline{B}, \qquad C = A \cdot B"),
        CODE(HALF_ADDER_TT, "text", title="Truth table: half adder",
             caption="1 + 1 = 10 in binary: sum 0, carry 1. S matches XOR and C matches AND, so a half adder is one XOR gate and one AND gate."),
        IMG("cs-half-adder.svg",
            "Half adder circuit. Inputs A and B go to an XOR gate giving the sum S = A XOR B, and to an AND gate giving the carry C = A AND B.",
            caption="Figure 1. A half adder: one XOR gate gives S and one AND gate gives C."),
        H("The full adder"),
        D(r"A **full adder** adds three bits: $A$, $B$ and a carry in $C_{in}$. It produces $S$ and a carry out $C_{out}$.",
          title="Full adder",
          formula=r"S = A \oplus B \oplus C_{in}, \qquad C_{out} = A\cdot B + C_{in}\cdot(A \oplus B)"),
        CODE(FULL_ADDER_TT, "text", title="Truth table: full adder"),
        EX("Worked example 1: checking the full adder expressions",
           intro=r"Use the expressions to find $S$ and $C_{out}$ when $A = 1$, $B = 0$, $C_{in} = 1$, and compare with the truth table.",
           steps=[
               S("Work out the XOR of A and B", math=r"A \oplus B = 1 \oplus 0 = 1"),
               S("Sum bit", math=r"S = 1 \oplus C_{in} = 1 \oplus 1 = 0"),
               S("First carry term", math=r"A \cdot B = 1 \cdot 0 = 0"),
               S("Second carry term", math=r"C_{in}\cdot(A \oplus B) = 1 \cdot 1 = 1"),
               S("Carry out", math=r"C_{out} = 0 + 1 = 1", text=r"Row 1 0 1 of the table gives S = 0, Cout = 1. It matches: $1 + 0 + 1 = 10_2$."),
           ]),
        TIP(r"A full adder can be built from **two half adders and an OR gate**: the first half adder adds $A$ and $B$, the second adds that sum to $C_{in}$, and the two carries are ORed together."),
        IMG("cs-full-adder.svg",
            "Full adder circuit. A XOR B, then XOR with Cin, gives S. One AND gate gives Cin AND (A XOR B), another gives A AND B, and an OR gate combines them to give Cout.",
            caption="Figure 2. A full adder built from two half adders (XOR and AND pairs) and an OR gate: S = A ⊕ B ⊕ Cin, Cout = A·B + Cin·(A ⊕ B)."),
        H("The ripple carry adder"),
        T(r"To add $n$-bit numbers, connect $n$ full adders in a chain. The carry out of each column becomes the carry in of the next. Because each carry must ripple through before the next column is final, this adder is simple but slow for long words."),
        CODE(RIPPLE_ADD, "text", title="Worked example 2: tracing a ripple carry adder"),
        H("Multiplexers and decoders"),
        D(r"A **multiplexer** (MUX) has $2^n$ data inputs, $n$ **select lines** and one output. The binary number on the select lines chooses which input is passed to the output.",
          title="Multiplexer",
          formula=r"Y = \overline{S}\cdot I_0 + S\cdot I_1 \quad \text{(2-to-1 MUX)}"),
        IMG("cs-mux-2-to-1.svg",
            "2-to-1 multiplexer circuit. S goes through a NOT gate. NOT S and I0 feed one AND gate; S and I1 feed another. An OR gate combines them into Y. S = 0 gives Y = I0; S = 1 gives Y = I1.",
            caption="Figure 3. A 2-to-1 multiplexer built from NOT, AND and OR gates: Y = (NOT S)·I0 + S·I1."),
        D(r"A **decoder** has $n$ inputs and up to $2^n$ outputs. For each input combination exactly **one** output is 1 (active). Decoders are used to select one memory chip or device from an address.",
          title="Decoder",
          formula=r"D_0 = \overline{A}\cdot\overline{B},\ D_1 = \overline{A}\cdot B,\ D_2 = A\cdot\overline{B},\ D_3 = A\cdot B"),
        CODE(MUX_DECODER_TT, "text", title="Truth tables: 4-to-1 MUX and 2-to-4 decoder"),
        EX("Worked example 3: a 4-to-1 multiplexer",
           intro=r"A 4-to-1 MUX has inputs $I_0 = 1$, $I_1 = 0$, $I_2 = 0$, $I_3 = 1$. Write its output expression and find $Y$ when $S_1 S_0 = 10$ and when $S_1 S_0 = 11$.",
           steps=[
               S("Output expression", math=r"Y = \overline{S_1}\,\overline{S_0}\, I_0 + \overline{S_1}\, S_0\, I_1 + S_1\,\overline{S_0}\, I_2 + S_1\, S_0\, I_3"),
               S("Select 10", text=r"Only the term $S_1\overline{S_0} I_2$ can be 1, so $Y = I_2 = 0$."),
               S("Select 11", text=r"Only the term $S_1 S_0 I_3$ can be 1, so $Y = I_3 = 1$."),
           ]),
        H("Common mistakes"),
        MISTAKE("Using OR for the sum bit",
                r"$1 + 1$ in binary gives sum 0, carry 1. OR would give 1. The sum bit is XOR, not OR."),
        MISTAKE("Confusing a multiplexer with a decoder",
                r"A MUX has many data inputs and **one** output. A decoder has a few inputs and **many** outputs, with one active at a time."),
        MISTAKE("Wrong number of select lines",
                r"A MUX with $m$ data inputs needs $\log_2 m$ select lines: 8 inputs need 3, 16 inputs need 4."),
        QUIZ(r"A half adder has inputs $A = 1$, $B = 1$. What are $S$ and $C$?",
             [r"S = 1, C = 1", r"S = 0, C = 1", r"S = 1, C = 0", r"S = 0, C = 0"], 1,
             r"$1 + 1 = 10_2$: $S = 1 \oplus 1 = 0$ and $C = 1 \cdot 1 = 1$.",
             feedback=[r"That would be $1 + 1 = 11_2 = 3$.", "",
                       r"That treats the sum as OR and forgets the carry.",
                       r"$1 + 1$ is not zero; the carry is 1."]),
        QUIZ(r"How many select lines does a 16-to-1 multiplexer need?",
             [r"16", r"8", r"2", r"4"], 3,
             r"$2^4 = 16$, so 4 select lines can choose any one of 16 inputs.",
             feedback=[r"16 is the number of data inputs.", r"8 select lines could choose among 256 inputs.",
                       r"2 select lines choose among only 4 inputs.", ""]),
        H("Practice questions"),
        PQ(r"(a) Draw up the truth table for a half adder. (b) Write Boolean expressions for its outputs. (c) State one limitation of a half adder. [5 marks]",
           r"(a) A B S C: 0 0 0 0; 0 1 1 0; 1 0 1 0; 1 1 0 1 (2). (b) $S = A \oplus B$ (1), $C = A \cdot B$ (1). (c) It has no carry-in input, so it cannot be used for any column except the least significant one of a multi-bit adder (1)."),
        PQ(r"Show the sum and carry at each stage when a 4-bit ripple carry adder adds 1011 and 0110. State whether there is a final carry out. [4 marks]",
           r"Bit 0: $1 + 0 + 0$ gives S = 1, carry 0. Bit 1: $1 + 1 + 0$ gives S = 0, carry 1. Bit 2: $0 + 1 + 1$ gives S = 0, carry 1. Bit 3: $1 + 0 + 1$ gives S = 0, carry 1. Result 0001 with a final carry out of 1, so the true result 10001 (17) does not fit in 4 bits: $11 + 6 = 17$."),
        PQ(r"A 3-to-8 decoder is used to select one of eight memory chips. Inputs are $A_2 A_1 A_0$ with $A_2$ the most significant. (a) Which output is active when the inputs are 101? (b) Write the Boolean expression for that output. [2 marks]",
           r"(a) 101 is 5, so output $D_5$ is active (1). (b) $D_5 = A_2 \cdot \overline{A_1} \cdot A_0$ (1)."),
        SUM(r"Combinational circuits have outputs that depend only on the current inputs.",
            r"Half adder: $S = A \oplus B$, $C = A\cdot B$; no carry in.",
            r"Full adder: $S = A \oplus B \oplus C_{in}$, $C_{out} = A\cdot B + C_{in}\cdot(A \oplus B)$.",
            r"A ripple carry adder chains full adders; each carry out feeds the next carry in.",
            r"A MUX selects one of $2^n$ inputs using $n$ select lines; a decoder activates one of $2^n$ outputs."),
    ],
))

# ---------------------------------------------------------------- Sequential circuits
FLIPFLOP_TABLES = """
SR latch (NOR gates)          D flip-flop (on clock edge)
S  R | Q next                 D | Q next
0  0 | Q   (no change)        0 | 0
0  1 | 0   (reset)            1 | 1
1  0 | 1   (set)
1  1 | not allowed

JK flip-flop (on clock edge)  T flip-flop (on clock edge)
J  K | Q next                 T | Q next
0  0 | Q      (no change)     0 | Q       (no change)
0  1 | 0      (reset)         1 | not Q   (toggle)
1  0 | 1      (set)
1  1 | not Q  (toggle)
"""

SR_TRACE = """
SR latch made from NOR gates, Q starts at 0

Time   S  R | Q   Q-bar | Action
t1     1  0 | 1   0     | set
t2     0  0 | 1   0     | hold (remembers 1)
t3     0  1 | 0   1     | reset
t4     0  0 | 0   1     | hold (remembers 0)
t5     1  0 | 1   0     | set
"""

JK_TRACE = """
JK flip-flop, Q starts at 0, changes on each clock pulse

Pulse  J  K | Q before | Q after | Action
1      1  0 | 0        | 1       | set
2      0  0 | 1        | 1       | no change
3      1  1 | 1        | 0       | toggle
4      1  1 | 0        | 1       | toggle
5      0  1 | 1        | 0       | reset
6      1  1 | 0        | 1       | toggle
"""

COUNTER_TRACE = """
Synchronous 2-bit counter: T0 = 1, T1 = Q0, both flip-flops share the clock

Clock  Q1 Q0 before | T1 T0 | Q1 Q0 after | Count
1      0  0         | 0  1  | 0  1        | 1
2      0  1         | 1  1  | 1  0        | 2
3      1  0         | 0  1  | 1  1        | 3
4      1  1         | 1  1  | 0  0        | 0
"""

LESSONS.append(lesson(
    module="Digital Logic",
    topic="Sequential circuits",
    title="Flip-flops: SR, D, JK and T",
    slug="sr-d-jk-and-t-flip-flops",
    minutes=30,
    summary="Understand how sequential circuits store a bit, and trace the behaviour of SR latches and D, JK and T flip-flops, including a simple counter.",
    objectives=[
        "Distinguish sequential circuits from combinational circuits",
        "State the characteristic tables of SR, D, JK and T flip-flops",
        "Trace the output of a flip-flop for a given sequence of inputs",
        "Explain uses of flip-flops in registers and counters",
    ],
    key_concepts=["Sequential circuit", "Flip-flop", "SR latch", "D flip-flop", "JK flip-flop",
                  "T flip-flop", "Clock", "Characteristic table"],
    blocks=[
        H("Introduction"),
        T(r"A calculator must remember the number you typed before you press the next key. Registers in the CPU must "
          r"hold the PC and the accumulator between clock ticks. Circuits that **remember** are called **sequential "
          r"circuits**, and the basic memory element is the **flip-flop**."),
        D(r"A **sequential circuit** is a logic circuit whose outputs depend on the current inputs **and** on its "
          r"previous state. It contains feedback, so it can store information.",
          title="Sequential circuit"),
        D(r"A **flip-flop** is a sequential circuit with two stable states that stores **one bit**. Its output $Q$ is "
          r"the stored bit and $\overline{Q}$ is its complement. A **clocked** flip-flop changes state only on a clock "
          r"pulse (usually on the rising or falling edge).",
          title="Flip-flop",
          note=r"An unclocked bistable is often called a latch; a clocked one a flip-flop."),
        CODE(FLIPFLOP_TABLES, "text", title="Characteristic tables of the four flip-flops",
             caption="A characteristic table gives the next state of Q for each combination of inputs and the present state."),
        H("The SR latch"),
        T(r"An SR latch can be built from two cross-coupled NOR gates. **S** (set) makes $Q = 1$, **R** (reset) makes "
          r"$Q = 0$. When both are 0 the latch **holds** its previous value: this is the memory. $S = R = 1$ is not "
          r"allowed, because both NOR outputs become 0, so $Q$ and $\overline{Q}$ are no longer complements, and the "
          r"final state is unpredictable when both inputs return to 0."),
        IMG("cs-sr-latch-nor.svg",
            "Two cross-coupled NOR gates. R and Q-bar feed the top gate, whose output is Q. S and Q feed the bottom gate, whose output is Q-bar. S = 1 sets, R = 1 resets, S = R = 0 holds, S = R = 1 is not allowed.",
            caption="Figure 1. An SR latch: each NOR output is fed back into the other NOR gate, which lets the circuit remember one bit."),
        CODE(SR_TRACE, "text", title="Worked example 1: SR latch trace"),
        EX("Worked example 1: reading the SR trace",
           intro=r"Explain why $Q$ is different at $t_2$ and $t_4$ even though the inputs are the same ($S = R = 0$).",
           steps=[
               S("At t1", text=r"$S = 1$ sets the latch, so $Q = 1$."),
               S("At t2", text=r"With $S = R = 0$ the latch holds its previous state, so $Q$ stays 1."),
               S("At t3", text=r"$R = 1$ resets the latch, so $Q = 0$."),
               S("At t4", text=r"With $S = R = 0$ it holds again, now holding 0. Same inputs, different outputs: the output depends on the previous state, which is exactly what makes it sequential."),
           ]),
        H("The D flip-flop"),
        T(r"The **D (data) flip-flop** removes the forbidden input of the SR latch. On the clock edge, $Q$ takes the value of $D$; between edges, $Q$ does not change. A row of D flip-flops sharing one clock forms a **register**, such as an 8-bit MDR. Its characteristic equation is $Q_{next} = D$."),
        H("The JK flip-flop"),
        T(r"The **JK flip-flop** behaves like an SR flip-flop ($J$ = set, $K$ = reset) except that $J = K = 1$ is allowed: it makes the output **toggle** (change to the opposite value). Its characteristic equation is $Q_{next} = J\cdot\overline{Q} + \overline{K}\cdot Q$."),
        CODE(JK_TRACE, "text", title="Worked example 2: JK flip-flop trace"),
        EX("Worked example 2: checking pulses 3 and 4 with the equation",
           intro=r"Use $Q_{next} = J\cdot\overline{Q} + \overline{K}\cdot Q$ to confirm pulses 3 and 4 of the trace.",
           steps=[
               S("Pulse 3: Q = 1, J = 1, K = 1", math=r"Q_{next} = 1\cdot 0 + 0 \cdot 1 = 0"),
               S("Pulse 4: Q = 0, J = 1, K = 1", math=r"Q_{next} = 1 \cdot 1 + 0 \cdot 0 = 1"),
               S("Conclusion", text=r"With $J = K = 1$ the output toggles on every pulse, as the table shows."),
           ]),
        H("The T flip-flop and counters"),
        T(r"The **T (toggle) flip-flop** has one input. If $T = 1$, the output toggles on each clock pulse; if $T = 0$, it holds. It can be made from a JK flip-flop by joining $J$ and $K$ together. With $T = 1$ the output changes at half the clock frequency, so T flip-flops are used for **frequency division** and **counters**. Its characteristic equation is $Q_{next} = T \oplus Q$."),
        CODE(COUNTER_TRACE, "text", title="Worked example 3: a 2-bit synchronous counter"),
        EX("Worked example 3: why the counter counts",
           intro=r"In the counter above, $T_0 = 1$ and $T_1 = Q_0$. Explain clock pulses 2 and 4.",
           steps=[
               S("Pulse 2", text=r"Before: $Q_1 Q_0 = 01$. $T_0 = 1$ so $Q_0$ toggles to 0. $T_1 = Q_0 = 1$ so $Q_1$ toggles to 1. After: 10, which is 2."),
               S("Pulse 4", text=r"Before: 11. Both T inputs are 1, so both toggle. After: 00. The counter wraps round from 3 to 0."),
               S("Pattern", text=r"$Q_1$ toggles only when $Q_0$ was 1, just like carrying in binary counting: 00, 01, 10, 11, 00."),
           ]),
        H("Common mistakes"),
        MISTAKE("Forgetting the hold state",
                r"When $S = R = 0$ (or $J = K = 0$, or $T = 0$) the output is not 0: it is whatever it was before. Always track the previous $Q$ in a trace."),
        MISTAKE("Allowing S = R = 1 in an SR latch",
                r"This input is invalid for a NOR SR latch. If asked what happens, say both outputs go to 0 and the next state is unpredictable when the inputs are removed."),
        MISTAKE("Changing a clocked flip-flop between clock pulses",
                r"A clocked D, JK or T flip-flop only changes on the active clock edge. Inputs that change between edges have no effect until the next edge."),
        QUIZ(r"A JK flip-flop has $Q = 1$. On the next clock pulse $J = 0$ and $K = 0$. What is $Q$ after the pulse?",
             [r"0", r"1", r"It toggles", r"Not allowed"], 1,
             r"$J = K = 0$ is the no-change state, so $Q$ stays 1. Check: $Q_{next} = 0\cdot 0 + 1\cdot 1 = 1$.",
             feedback=[r"That would happen with $K = 1$, $J = 0$ (reset).", "",
                       r"Toggling needs $J = K = 1$.",
                       r"Every input combination is allowed for a JK flip-flop; that is its advantage over SR."]),
        QUIZ(r"Which flip-flop is most suitable for building a register that stores the data on its input at each clock edge?",
             [r"SR latch", r"T flip-flop", r"D flip-flop", r"JK flip-flop with J = K = 1"], 2,
             r"A D flip-flop copies $D$ to $Q$ on each clock edge, which is exactly what a storage register needs.",
             feedback=[r"An SR latch needs two inputs and has a forbidden state.",
                       r"A T flip-flop toggles; it does not copy an input value.", "",
                       r"With $J = K = 1$ it only toggles."]),
        H("Practice questions"),
        PQ(r"(a) State the difference between a combinational and a sequential circuit. (b) Explain why $S = R = 1$ is not used in an SR latch made from NOR gates. [4 marks]",
           r"(a) In a combinational circuit the outputs depend only on the present inputs (1); in a sequential circuit they also depend on the previous state, because of feedback / stored state (1). (b) Both outputs become 0, so $Q$ and $\overline{Q}$ are not complements (1); when the inputs return to 0 the latch may settle in either state, so the result is unpredictable (1)."),
        PQ(r"A T flip-flop starts with $Q = 0$. The inputs on six successive clock pulses are $T$ = 1, 1, 0, 1, 0, 1. Give $Q$ after each pulse. [3 marks]",
           r"Pulse 1: toggle, Q = 1. Pulse 2: toggle, Q = 0. Pulse 3: hold, Q = 0. Pulse 4: toggle, Q = 1. Pulse 5: hold, Q = 1. Pulse 6: toggle, Q = 0. So Q = 1, 0, 0, 1, 1, 0."),
        PQ(r"A JK flip-flop starts with $Q = 1$. The inputs $(J, K)$ on four clock pulses are (0, 1), (1, 0), (1, 1), (0, 0). Give $Q$ after each pulse and name the action. [4 marks]",
           r"(0, 1): reset, Q = 0 (1). (1, 0): set, Q = 1 (1). (1, 1): toggle, Q = 0 (1). (0, 0): no change, Q = 0 (1)."),
        SUM(r"Sequential circuits remember: their outputs depend on inputs and the previous state.",
            r"SR latch: set, reset, hold; $S = R = 1$ is not allowed.",
            r"D flip-flop: $Q_{next} = D$ on the clock edge; used in registers.",
            r"JK flip-flop: like SR, but $J = K = 1$ toggles; $Q_{next} = J\cdot\overline{Q} + \overline{K}\cdot Q$.",
            r"T flip-flop: toggles when $T = 1$; $Q_{next} = T \oplus Q$; used in counters and frequency dividers."),
    ],
))

# ---------------------------------------------------------------- Simplification
KMAP_LAYOUT = """
Cell numbering (minterm m = decimal value of the input bits)

3 variables: rows A, columns BC in Gray code order

          BC=00  BC=01  BC=11  BC=10
A=0        m0     m1     m3     m2
A=1        m4     m5     m7     m6

4 variables: rows AB, columns CD in Gray code order

          CD=00  CD=01  CD=11  CD=10
AB=00      m0     m1     m3     m2
AB=01      m4     m5     m7     m6
AB=11      m12    m13    m15    m14
AB=10      m8     m9     m11    m10
"""

KMAP_3VAR = """
F(A, B, C) = sum of minterms 1, 3, 6, 7

          BC=00  BC=01  BC=11  BC=10
A=0        0      1      1      0
A=1        0      0      1      1

Group 1 (pair): m1, m3  -> A = 0 and C = 1 in both, B changes  -> NOT A . C
Group 2 (pair): m7, m6  -> A = 1 and B = 1 in both, C changes  -> A . B
"""

KMAP_4VAR = """
F(A, B, C, D) = sum of minterms 0, 2, 5, 7, 8, 10, 13, 15

          CD=00  CD=01  CD=11  CD=10
AB=00      1      0      0      1
AB=01      0      1      1      0
AB=11      0      1      1      0
AB=10      1      0      0      1

Group 1 (quad, the four corners): m0, m2, m8, m10 -> B = 0, D = 0 -> NOT B . NOT D
Group 2 (quad, the centre):       m5, m7, m13, m15 -> B = 1, D = 1 -> B . D
"""

LESSONS.append(lesson(
    module="Digital Logic",
    topic="Simplification",
    title="Boolean algebra, De Morgan's laws and Karnaugh maps",
    slug="boolean-algebra-de-morgan-and-karnaugh-maps",
    minutes=30,
    summary="Simplify Boolean expressions using the laws of Boolean algebra and De Morgan's laws, and with Karnaugh maps of up to four variables.",
    objectives=[
        "Apply the laws of Boolean algebra to simplify expressions",
        "Use De Morgan's laws to rewrite complemented expressions",
        "Draw 3- and 4-variable Karnaugh maps in Gray code order",
        "Group 1s correctly and read off a minimal sum-of-products expression",
    ],
    key_concepts=["Boolean algebra", "De Morgan's laws", "Absorption law", "Sum of products", "Minterm",
                  "Karnaugh map", "Gray code", "Grouping"],
    blocks=[
        H("Introduction"),
        T(r"A logic circuit with fewer gates is cheaper to build, uses less power and is faster. Before building a "
          r"circuit, engineers **simplify** its Boolean expression. You will learn two methods: algebra, using a set "
          r"of laws, and **Karnaugh maps**, a visual method that works well for up to four variables."),
        H("The laws of Boolean algebra"),
        KEY("Laws to learn", r"Each law has an AND form and an OR form.",
            cards=[
                ["Identity and null", r"$A \cdot 1 = A$, $A + 0 = A$, $A \cdot 0 = 0$, $A + 1 = 1$"],
                ["Idempotent and complement", r"$A \cdot A = A$, $A + A = A$, $A \cdot \overline{A} = 0$, $A + \overline{A} = 1$, $\overline{\overline{A}} = A$"],
                ["Distributive", r"$A\cdot(B + C) = A\cdot B + A\cdot C$ and $A + B\cdot C = (A + B)\cdot(A + C)$"],
                ["Absorption", r"$A + A\cdot B = A$, $A\cdot(A + B) = A$, $A + \overline{A}\cdot B = A + B$"],
            ],
            note=r"Commutative and associative laws also hold: the order and grouping of AND or OR terms does not matter."),
        D(r"To complement an AND, complement each term and change AND to OR. To complement an OR, complement each term and change OR to AND.",
          title="De Morgan's laws",
          formula=r"\overline{A \cdot B} = \overline{A} + \overline{B}, \qquad \overline{A + B} = \overline{A} \cdot \overline{B}",
          note=r"Memory aid: break the bar, change the sign."),
        EX("Worked example 1: simplifying with algebra",
           solve=r"F = \overline{A}\cdot B + A\cdot B + A\cdot\overline{B}",
           steps=[
               S("Factor B from the first two terms", math=r"F = B\cdot(\overline{A} + A) + A\cdot\overline{B}"),
               S("Complement law", math=r"\overline{A} + A = 1, \text{ so } F = B + A\cdot\overline{B}"),
               S("Absorption law in the form X + not X . Y = X + Y", math=r"F = B + A"),
           ],
           check=r"F = 1 \text{ for } AB = 01, 11, 10 \text{ and } 0 \text{ for } 00: \text{ the OR function}"),
        EX("Worked example 2: applying De Morgan's laws",
           solve=r"F = \overline{\overline{A}\cdot B + C}",
           steps=[
               S("Break the outer bar over the OR", math=r"F = \overline{\overline{A}\cdot B}\cdot\overline{C}"),
               S("Break the bar over the AND", math=r"\overline{\overline{A}\cdot B} = \overline{\overline{A}} + \overline{B} = A + \overline{B}"),
               S("Write the result", math=r"F = (A + \overline{B})\cdot\overline{C}"),
           ],
           check=r"A = 0, B = 1, C = 0: \ \overline{1\cdot 1 + 0} = 0 \text{ and } (0 + 0)\cdot 1 = 0"),
        H("Karnaugh maps"),
        D(r"A **Karnaugh map** (K-map) is a grid with one cell for each **minterm** (each row of the truth table). Rows and columns are labelled in **Gray code** order (00, 01, 11, 10), so neighbouring cells differ in only one variable.",
          title="Karnaugh map",
          note=r"A minterm is an AND term containing every variable once, e.g. $\overline{A}\cdot B\cdot C$ is minterm 3 (binary 011)."),
        CODE(KMAP_LAYOUT, "text", title="Where each minterm goes"),
        KEY("Grouping rules", r"Follow these rules to get the simplest sum of products.",
            cards=[
                ["Size", r"Groups contain 1, 2, 4, 8 or 16 cells (powers of 2) and are rectangles. Only 1s are grouped."],
                ["As large as possible", r"Make each group as large as possible, and use as few groups as possible. Groups may overlap."],
                ["Wrap around", r"The map wraps: the left and right edges are neighbours, so are the top and bottom. The four corners of a 4-variable map form one group."],
                ["Reading a group", r"Keep only the variables that stay the same in every cell of the group. A pair removes 1 variable, a quad 2, an octet 3."],
            ]),
        CODE(KMAP_3VAR, "text", title="Worked example 3: a 3-variable K-map"),
        EX("Worked example 3: the steps",
           intro=r"Simplify $F(A, B, C) = \sum m(1, 3, 6, 7)$ using the K-map above.",
           steps=[
               S("Place the 1s", text=r"m1 = 001 and m3 = 011 go in row A = 0; m6 = 110 and m7 = 111 go in row A = 1."),
               S("First group", text=r"m1 and m3 are adjacent. In both, A = 0 and C = 1; B changes, so B is removed.", math=r"\overline{A}\cdot C"),
               S("Second group", text=r"m7 and m6 are adjacent. In both, A = 1 and B = 1; C changes.", math=r"A\cdot B"),
               S("Write the sum of products", math=r"F = \overline{A}\cdot C + A\cdot B"),
           ],
           check=r"m3: \overline{0}\cdot 1 = 1, \quad m6: 1\cdot 1 = 1, \quad m4: \overline{1}\cdot 0 + 1\cdot 0 = 0"),
        CODE(KMAP_4VAR, "text", title="Worked example 4: a 4-variable K-map"),
        IMG("cs-kmap-4var.svg",
            "4-variable K-map, rows AB and columns CD in order 00, 01, 11, 10. 1s at m0, m2, m8, m10 (corners) and m5, m7, m13, m15 (centre). Corner quad gives NOT B AND NOT D; centre quad gives B AND D. F = NOT B . NOT D + B . D.",
            caption="Figure 1. Worked example 4 on the K-map: the corner quad (wrapping round the edges) gives B̄·D̄ and the centre quad gives B·D."),
        EX("Worked example 4: the steps",
           intro=r"Simplify $F(A, B, C, D) = \sum m(0, 2, 5, 7, 8, 10, 13, 15)$.",
           steps=[
               S("Place the 1s", text=r"Use $m = 8A + 4B + 2C + D$. For example m13 = 1101 is row AB = 11, column CD = 01."),
               S("Corner quad", text=r"m0, m2, m8 and m10 are the four corners, which are adjacent by wrap-around. In all four, B = 0 and D = 0.", math=r"\overline{B}\cdot\overline{D}"),
               S("Centre quad", text=r"m5, m7, m13 and m15 form a square. In all four, B = 1 and D = 1.", math=r"B\cdot D"),
               S("Write the result", math=r"F = \overline{B}\cdot\overline{D} + B\cdot D"),
           ],
           check=r"F = 1 \text{ exactly when } B = D, \text{ i.e. } F = \overline{B \oplus D}"),
        H("Common mistakes"),
        MISTAKE("Labelling K-map columns 00, 01, 10, 11",
                r"That is binary order, not Gray code. The cells for 01 and 10 differ in two variables, so groups read from them will be wrong. Always use 00, 01, 11, 10."),
        MISTAKE("Forgetting to change the sign with De Morgan",
                r"$\overline{A \cdot B}$ is **not** $\overline{A}\cdot\overline{B}$. Breaking the bar changes AND to OR: $\overline{A} + \overline{B}$."),
        MISTAKE("Making groups of 3 or 6",
                r"Groups must have a power-of-two size. Three adjacent 1s are covered by two overlapping pairs."),
        MISTAKE("Missing wrap-around groups",
                r"Cells on opposite edges are adjacent. Check edges and corners before writing pairs that could be a bigger group."),
        QUIZ(r"Which expression is equal to $\overline{A + \overline{B}}$?",
             [r"$\overline{A} + B$", r"$\overline{A}\cdot B$", r"$A\cdot\overline{B}$", r"$\overline{A}\cdot\overline{B}$"], 1,
             r"De Morgan: $\overline{A + \overline{B}} = \overline{A}\cdot\overline{\overline{B}} = \overline{A}\cdot B$.",
             feedback=[r"The bar was broken but OR was not changed to AND.", "",
                       r"This is the original expression without the bar, not its complement.",
                       r"$\overline{\overline{B}} = B$, so $B$ should not be complemented."]),
        QUIZ(r"In a 4-variable K-map, a group of four 1s removes how many variables from the term?",
             [r"1", r"4", r"3", r"2"], 3,
             r"A quad has $2^2$ cells, so 2 variables change and are removed; 2 variables remain.",
             feedback=[r"A pair removes 1 variable.", r"Removing all 4 would need a group of 16 cells.",
                       r"An octet (8 cells) removes 3.", ""]),
        H("Practice questions"),
        PQ(r"Use Boolean algebra to show that $A\cdot(A + B) = A$. State each law used. [3 marks]",
           r"Distributive law: $A\cdot A + A\cdot B$ (1). Idempotent law: $A + A\cdot B$ (1). Absorption, or factorise: $A\cdot(1 + B) = A\cdot 1 = A$ using the null law $1 + B = 1$ and the identity law (1)."),
        PQ(r"Use De Morgan's laws to show that $\overline{\overline{A}\cdot\overline{B}} = A + B$. Hence explain how an OR gate can be made from NAND gates. [3 marks]",
           r"$\overline{\overline{A}\cdot\overline{B}} = \overline{\overline{A}} + \overline{\overline{B}} = A + B$ (1). So OR is a NAND gate whose inputs are $\overline{A}$ and $\overline{B}$ (1). Each NOT is made from a NAND with both inputs joined, so three NAND gates make an OR gate (1)."),
        PQ(r"Use a Karnaugh map to simplify $F(A, B, C) = \sum m(0, 2, 4, 6)$. [2 marks]",
           r"The 1s are in columns BC = 00 and BC = 10 in both rows, which wrap round to form one quad (1). In all four cells C = 0, so $F = \overline{C}$ (1)."),
        PQ(r"Use a Karnaugh map to simplify $F(A, B, C, D) = \sum m(0, 1, 2, 3, 5, 7)$. [3 marks]",
           r"Row AB = 00 is all 1s (m0, m1, m3, m2): quad $\overline{A}\cdot\overline{B}$ (1). m1, m3, m5, m7 (columns CD = 01 and 11 in rows 00 and 01) form a second quad: $\overline{A}\cdot D$ (1). $F = \overline{A}\cdot\overline{B} + \overline{A}\cdot D$, which can also be written $\overline{A}\cdot(\overline{B} + D)$ (1)."),
        SUM(r"Boolean laws (identity, null, complement, distributive, absorption) simplify expressions step by step.",
            r"De Morgan: $\overline{A \cdot B} = \overline{A} + \overline{B}$ and $\overline{A + B} = \overline{A}\cdot\overline{B}$; break the bar, change the sign.",
            r"K-map rows and columns use Gray code order 00, 01, 11, 10.",
            r"Group 1s in rectangles of 1, 2, 4, 8 or 16 cells, as large as possible; edges and corners wrap round.",
            r"Each group gives one product term containing only the variables that do not change."),
    ],
))

# ---------------------------------------------------------------- Process management
SCHED_DATA = """
Process   Arrival time   Burst time (ms)
P1        0              7
P2        0              4
P3        0              2
P4        0              5
(All arrive at time 0 in the order P1, P2, P3, P4.)
"""

FCFS_SJF = """
FCFS (first come, first served)

| P1                | P2       | P3   | P4          |
0                   7          11     13            18

Process  Start  Finish  Turnaround = Finish - Arrival  Waiting = Turnaround - Burst
P1       0      7       7                              0
P2       7      11      11                             7
P3       11     13      13                             11
P4       13     18      18                             13
Average waiting time    = (0 + 7 + 11 + 13) / 4 = 31 / 4 = 7.75 ms
Average turnaround time = (7 + 11 + 13 + 18) / 4 = 49 / 4 = 12.25 ms

SJF (shortest job first, non-preemptive)

| P3   | P2       | P4          | P1                |
0      2          6             11                  18

Process  Start  Finish  Turnaround  Waiting
P3       0      2       2           0
P2       2      6       6           2
P4       6      11      11          6
P1       11     18      18          11
Average waiting time    = (0 + 2 + 6 + 11) / 4 = 19 / 4 = 4.75 ms
Average turnaround time = (2 + 6 + 11 + 18) / 4 = 37 / 4 = 9.25 ms
"""

RR_TRACE = """
Round Robin, time quantum = 3 ms

| P1    | P2    | P3  | P4    | P1    | P2 | P4  | P1 |
0       3       6     8       11      14   15    17   18

Time    Runs   Remaining after   Ready queue after (front first)
0-3     P1     P1: 4             P2, P3, P4, P1
3-6     P2     P2: 1             P3, P4, P1, P2
6-8     P3     P3: 0 (done)      P4, P1, P2
8-11    P4     P4: 2             P1, P2, P4
11-14   P1     P1: 1             P2, P4, P1
14-15   P2     P2: 0 (done)      P4, P1
15-17   P4     P4: 0 (done)      P1
17-18   P1     P1: 0 (done)      empty

Process  Finish  Turnaround  Waiting = Turnaround - Burst
P1       18      18          18 - 7 = 11
P2       15      15          15 - 4 = 11
P3       8       8           8 - 2  = 6
P4       17      17          17 - 5 = 12
Average waiting time    = (11 + 11 + 6 + 12) / 4 = 40 / 4 = 10 ms
Average turnaround time = (18 + 15 + 8 + 17) / 4 = 58 / 4 = 14.5 ms
"""

SEMAPHORE_TRACE = """
Counting semaphore S guards 2 printers. S starts at 2.
wait(S):   if S > 0 then S = S - 1, else block the process
signal(S): if a process is blocked on S then wake it (it takes the printer),
           else S = S + 1

Event          S after   Printers in use   Blocked
start          2         -                 -
A: wait(S)     1         A                 -
B: wait(S)     0         A, B              -
C: wait(S)     0         A, B              C
A: signal(S)   0         B, C              -      (C is woken)
B: signal(S)   1         C                 -
C: signal(S)   2         -                 -
"""

LESSONS.append(lesson(
    module="Operating Systems & Translators",
    topic="Process management",
    title="CPU scheduling, semaphores and deadlock",
    slug="cpu-scheduling-semaphores-and-deadlock",
    minutes=30,
    summary="Schedule processes with FCFS, SJF and Round Robin, calculate waiting and turnaround times, and explain semaphores and deadlock.",
    objectives=[
        "Describe the states of a process and the role of the scheduler",
        "Draw Gantt charts for FCFS, SJF and Round Robin scheduling",
        "Calculate waiting and turnaround times and their averages",
        "Explain how semaphores give mutual exclusion",
        "State the conditions for deadlock and ways of handling it",
    ],
    key_concepts=["Process", "Process states", "Scheduler", "FCFS", "SJF", "Round Robin", "Time quantum",
                  "Waiting time", "Turnaround time", "Semaphore", "Mutual exclusion", "Deadlock"],
    blocks=[
        H("Introduction"),
        T(r"A computer in a school lab may run a browser, a word processor and an antivirus scan at the same time, yet "
          r"a single-core CPU can only execute one instruction stream at once. The operating system shares the CPU "
          r"between programs so quickly that they appear to run together. Deciding **who runs next** is called "
          r"**scheduling**."),
        D(r"A **process** is a program in execution, together with its current state: the PC value, register contents, "
          r"memory and open files. The OS stores this in a **process control block** (PCB).",
          title="Process"),
        KEY("Process states", r"A process moves between three main states.",
            cards=[
                ["Ready", r"Waiting in the ready queue for its turn on the CPU."],
                ["Running", r"Currently executing on the CPU."],
                ["Blocked", r"Waiting for an event, such as input/output finishing. It cannot use the CPU even if offered."],
            ],
            note=r"Running to ready happens when a time slice ends (preemption); running to blocked when it requests I/O; blocked to ready when the I/O completes."),
        D(r"**Turnaround time** = finish time minus arrival time. **Waiting time** = turnaround time minus burst time, "
          r"that is, the time spent in the ready queue.",
          title="Measuring a schedule",
          formula=r"\text{waiting} = (\text{finish} - \text{arrival}) - \text{burst}"),
        KEY("Three scheduling algorithms", r"Compare how each chooses the next process.",
            cards=[
                ["FCFS", r"First come, first served. Non-preemptive: processes run in arrival order until they finish. Simple, but short jobs can wait behind a long one (the convoy effect)."],
                ["SJF", r"Shortest job first. Runs the waiting process with the smallest burst time. Gives the minimum average waiting time, but burst times must be known or estimated, and long jobs may starve."],
                ["Round Robin", r"Each process gets a fixed **time quantum**. If it has not finished, it goes to the back of the ready queue. Fair and good for interactive systems; performance depends on the quantum size."],
            ]),
        H("Worked examples: scheduling"),
        CODE(SCHED_DATA + FCFS_SJF, "text", title="Gantt charts and calculations: FCFS and SJF"),
        EX("Worked example 1: the steps for SJF",
           intro=r"Using the data above, schedule the processes with non-preemptive SJF and find the average waiting time.",
           steps=[
               S("Order by burst time", text=r"P3 (2), P2 (4), P4 (5), P1 (7)."),
               S("Build the timeline", text=r"P3 runs 0 to 2, P2 runs 2 to 6, P4 runs 6 to 11, P1 runs 11 to 18."),
               S("Waiting times", text=r"All arrived at 0, so each waiting time equals its start time: P3 = 0, P2 = 2, P4 = 6, P1 = 11."),
               S("Average", math=r"\frac{0 + 2 + 6 + 11}{4} = \frac{19}{4} = 4.75 \text{ ms}"),
           ],
           check=r"\text{FCFS average } = 7.75 \text{ ms, so SJF is better here}"),
        CODE(RR_TRACE, "text", title="Round Robin with a 3 ms quantum"),
        EX("Worked example 2: the steps for Round Robin",
           intro=r"Using the same data with a time quantum of 3 ms, find each process's waiting time.",
           steps=[
               S("First round", text=r"P1 runs 0 to 3 (4 left), P2 runs 3 to 6 (1 left), P3 runs 6 to 8 and finishes early, P4 runs 8 to 11 (2 left)."),
               S("Second round", text=r"P1 runs 11 to 14 (1 left), P2 runs 14 to 15 and finishes, P4 runs 15 to 17 and finishes."),
               S("Last slice", text=r"P1 runs 17 to 18 and finishes."),
               S("Waiting = finish minus burst (arrival 0)", text=r"P1: 18 minus 7 = 11, P2: 15 minus 4 = 11, P3: 8 minus 2 = 6, P4: 17 minus 5 = 12."),
               S("Average", math=r"\frac{11 + 11 + 6 + 12}{4} = \frac{40}{4} = 10 \text{ ms}",
                 text=r"Round Robin has a higher average wait than SJF here, but no process waits long for its first turn, which is why it suits interactive systems."),
           ],
           check=r"\text{chart length } = 7 + 4 + 2 + 5 = 18 \text{ ms, the sum of the bursts}"),
        H("Semaphores"),
        D(r"A **critical section** is part of a program that uses a shared resource (a variable, file or printer). "
          "**Mutual exclusion** means only one process may be in its critical section for that resource at a time.\n\n"
          r"A **semaphore** is an integer variable used by processes to control access to shared resources. It is "
          r"changed only by two atomic operations: **wait** (also called P) before using the resource and **signal** "
          r"(also called V) after using it. A **binary semaphore** (values 0 and 1) gives mutual exclusion; a "
          r"**counting semaphore** controls a pool of identical resources.",
          title="Critical sections and semaphores"),
        CODE(SEMAPHORE_TRACE, "text", title="Worked example 3: a counting semaphore for two printers"),
        H("Deadlock"),
        D(r"**Deadlock** is a situation in which two or more processes are each waiting for a resource held by another, so none of them can ever continue.",
          title="Deadlock"),
        KEY("The four conditions for deadlock", r"Deadlock can only happen if all four hold at the same time.",
            cards=[
                ["Mutual exclusion", r"A resource can be used by only one process at a time."],
                ["Hold and wait", r"A process holds one resource while waiting for another."],
                ["No preemption", r"A resource cannot be taken away from a process; it must be released voluntarily."],
                ["Circular wait", r"A closed chain of processes exists, each waiting for a resource held by the next."],
            ],
            note=r"Handling deadlock: prevention (break one condition, e.g. request all resources at once or in a fixed order), avoidance (only grant requests that keep the system safe, e.g. the banker's algorithm), or detection and recovery (find the cycle, then terminate a process or take back a resource)."),
        EX("Worked example 4: recognising deadlock",
           intro=r"Process A holds the scanner and requests the printer. Process B holds the printer and requests the scanner. Explain why deadlock occurs and suggest one way to prevent it.",
           steps=[
               S("Mutual exclusion", text=r"The scanner and printer can each be used by only one process."),
               S("Hold and wait", text=r"Each process holds one device while waiting for the other."),
               S("No preemption and circular wait", text=r"Neither device can be taken away, and A waits for B while B waits for A: a cycle."),
               S("Prevention", text=r"Make every process request resources in the same fixed order, for example scanner before printer. Then B would have to request the scanner first, and the cycle cannot form."),
           ]),
        H("Common mistakes"),
        MISTAKE("Confusing waiting time with turnaround time",
                r"Turnaround includes the time spent running. Waiting time excludes it: waiting = turnaround minus burst."),
        MISTAKE("Ignoring arrival times",
                r"When processes arrive at different times, a process cannot start before it arrives, and its waiting time is measured from its arrival, not from time 0."),
        MISTAKE("Putting a finished process back in the Round Robin queue",
                r"A process that completes within its quantum leaves the system and gives up the rest of the slice; the next process starts immediately."),
        QUIZ(r"Three processes arrive at time 0 with bursts P1 = 6, P2 = 3, P3 = 1 ms, in that order. What is the average waiting time under FCFS?",
             [r"3 ms", r"5 ms", r"1.67 ms", r"10 ms"], 1,
             r"FCFS: P1 waits 0, P2 waits 6, P3 waits 9. Average = 15 / 3 = 5 ms.",
             feedback=[r"That is close to the average burst, not the average wait.", "",
                       r"1.67 ms is the SJF average: waits 0, 1, 4 give 5 / 3.",
                       r"10 ms is the length of the whole schedule."]),
        QUIZ(r"Which condition is broken if every process must request all the resources it needs before it starts?",
             [r"Mutual exclusion", r"Hold and wait", r"No preemption", r"Circular wait"], 1,
             r"A process never holds one resource while waiting for another, so hold and wait cannot happen.",
             feedback=[r"Resources are still used by one process at a time.", "",
                       r"Resources are still not taken away from processes.",
                       r"This rule works by removing hold and wait; ordering requests is what breaks circular wait."]),
        H("Practice questions"),
        PQ(r"Processes arrive as follows: P1 at 0 ms (burst 5), P2 at 1 ms (burst 3), P3 at 2 ms (burst 1). Draw Gantt charts and find the average waiting time for (a) FCFS and (b) non-preemptive SJF. [6 marks]",
           r"(a) FCFS: P1 0 to 5, P2 5 to 8, P3 8 to 9 (1). Waits: P1 = 0, P2 = 5 minus 1 = 4, P3 = 8 minus 2 = 6 (1). Average = 10 / 3 = 3.33 ms (1). (b) SJF: only P1 has arrived at 0, so P1 runs 0 to 5; at 5 both others wait and P3 is shorter, so P3 5 to 6, then P2 6 to 9 (1). Waits: P1 = 0, P3 = 5 minus 2 = 3, P2 = 6 minus 1 = 5 (1). Average = 8 / 3 = 2.67 ms (1)."),
        PQ(r"Four processes arrive at time 0 in the order A (burst 5), B (burst 2), C (burst 4), D (burst 1). Using Round Robin with a quantum of 2 ms, draw the Gantt chart and calculate the average turnaround time. [5 marks]",
           r"Gantt chart: A 0 to 2, B 2 to 4 (done), C 4 to 6, D 6 to 7 (done), A 7 to 9, C 9 to 11 (done), A 11 to 12 (done) (2). Finish times: A = 12, B = 4, C = 11, D = 7 (1). Turnaround equals finish time since all arrive at 0 (1). Average = (12 + 4 + 11 + 7) / 4 = 34 / 4 = 8.5 ms (1)."),
        PQ(r"(a) Explain what is meant by a semaphore. (b) Describe how a binary semaphore ensures that two processes do not update a shared variable at the same time. [4 marks]",
           r"(a) An integer variable, accessed only through the atomic operations wait and signal, used to control access to a shared resource (1). (b) The semaphore starts at 1 (1). A process calls wait before its critical section; if the value is 1 it becomes 0 and the process enters (1). A second process calling wait finds 0 and is blocked until the first calls signal when it leaves its critical section (1)."),
        PQ(r"State the four conditions necessary for deadlock and describe one method of recovering from deadlock once detected. [5 marks]",
           r"Mutual exclusion, hold and wait, no preemption, circular wait (1 each, 4). Recovery: terminate one or more deadlocked processes, or preempt a resource from a process and roll it back, until the cycle is broken (1)."),
        SUM(r"A process is a program in execution; it moves between ready, running and blocked states.",
            r"Turnaround = finish minus arrival; waiting = turnaround minus burst.",
            r"FCFS is simple but suffers the convoy effect; SJF minimises average waiting time but may starve long jobs.",
            r"Round Robin gives each process a time quantum in turn; good for interactive systems.",
            r"Semaphores use atomic wait and signal operations to give mutual exclusion over shared resources.",
            r"Deadlock needs mutual exclusion, hold and wait, no preemption and circular wait; break one to prevent it."),
    ],
))

# ---------------------------------------------------------------- Memory management
FIFO_TRACE = """
FIFO, 3 frames, reference string 7 0 1 2 0 3 0 4 2 3
(F = page fault; a dash is an empty frame)

Reference  7   0   1   2   0   3   0   4   2   3
Frame 0    7   7   7   2   2   2   2   4   4   4
Frame 1    -   0   0   0   0   3   3   3   2   2
Frame 2    -   -   1   1   1   1   0   0   0   3
Fault      F   F   F   F       F   F   F   F   F

Page faults = 9, hits = 1
"""

LRU_TRACE = """
LRU, 3 frames, same reference string

Reference  7   0   1   2   0   3   0   4   2   3
Frame 0    7   7   7   2   2   2   2   4   4   4
Frame 1    -   0   0   0   0   0   0   0   0   3
Frame 2    -   -   1   1   1   3   3   3   2   2
Fault      F   F   F   F       F       F   F   F

Page faults = 8, hits = 2
"""

LESSONS.append(lesson(
    module="Operating Systems & Translators",
    topic="Memory management",
    title="Paging, segmentation and virtual memory",
    slug="paging-segmentation-and-virtual-memory",
    minutes=30,
    summary="Explain paging and segmentation, translate logical addresses to physical addresses, and count page faults under FIFO and LRU page replacement.",
    objectives=[
        "Explain paging, frames and the page table",
        "Translate a logical address into a physical address",
        "Compare paging with segmentation",
        "Explain virtual memory, page faults and thrashing",
        "Count page faults for FIFO and LRU replacement",
    ],
    key_concepts=["Paging", "Page", "Frame", "Page table", "Segmentation", "Virtual memory", "Page fault",
                  "FIFO replacement", "LRU replacement", "Thrashing"],
    blocks=[
        H("Introduction"),
        T(r"Many programs are loaded into main memory at the same time, and together they may need more memory than "
          r"the RAM installed. The operating system's **memory manager** decides where each program goes, keeps "
          r"programs from overwriting each other, and uses the disk to extend memory when RAM runs out. Two methods of "
          r"dividing memory are **paging** and **segmentation**."),
        D(r"In **paging**, a program's logical address space is divided into fixed-size blocks called **pages**, and "
          r"physical memory is divided into blocks of the same size called **frames**. Any page can be placed in any "
          r"free frame. A **page table** for each process records which frame holds each page.",
          title="Paging",
          note=r"Because pages and frames are the same size, there are no gaps between blocks (no external fragmentation), but the last page of a program may be partly empty (internal fragmentation)."),
        D(r"**Virtual memory** uses part of secondary storage as if it were main memory. Only the pages a program is "
          r"currently using need to be in RAM; the rest stay on disk until needed. Programs can therefore be larger "
          r"than the physical memory.",
          title="Virtual memory"),
        KEY("Paging vs segmentation", r"Both divide a program into parts, but in different ways.",
            cards=[
                ["Paging", r"Fixed-size pages, chosen by the OS and hardware. Invisible to the programmer. Address = page number + offset. Causes internal fragmentation."],
                ["Segmentation", r"Variable-size **segments** that match logical parts of the program, such as the code, the stack or a data array. Address = segment number + offset, checked against the segment's **limit**. Causes external fragmentation."],
            ]),
        H("Address translation in paging"),
        D(r"A logical address is split into a **page number** and an **offset** within the page. The page table gives "
          r"the frame number, and the offset stays the same.",
          title="Translating an address",
          formula=r"\text{physical address} = \text{frame number} \times \text{page size} + \text{offset}"),
        EX("Worked example 1: logical to physical address",
           intro=r"Page size is 4 KiB (4096 bytes). Part of a process's page table is: page 0 in frame 3, page 1 in frame 7, page 2 in frame 5. Find the physical address for logical address 9000.",
           steps=[
               S("Find the page number", math=r"9000 \div 4096 = 2 \text{ remainder } 808"),
               S("Page and offset", text=r"Page 2, offset 808 (because $2 \times 4096 = 8192$ and $9000 - 8192 = 808$)."),
               S("Look up the page table", text=r"Page 2 is in frame 5."),
               S("Calculate the physical address", math=r"5 \times 4096 + 808 = 20\,480 + 808 = 21\,288"),
           ],
           check=r"21\,288 \div 4096 = 5 \text{ remainder } 808"),
        H("Page faults and page replacement"),
        D(r"A **page fault** occurs when a program refers to a page that is not currently in main memory. The OS "
          r"suspends the process, finds the page on disk, loads it into a free frame (or replaces a page if none is "
          r"free), updates the page table, and then restarts the instruction.",
          title="Page fault"),
        KEY("Page replacement algorithms", r"When all frames are full, the OS must choose a **victim** page to remove.",
            cards=[
                ["FIFO", r"First in, first out: replace the page that has been in memory **longest**. Simple, but may remove a heavily used page."],
                ["LRU", r"Least recently used: replace the page that has not been **used** for the longest time. Usually fewer faults, but the OS must record when each page was used."],
                ["Optimal", r"Replace the page that will not be used for the longest time in the future. Gives the fewest faults but needs future knowledge, so it is used only as a benchmark."],
            ]),
        CODE(FIFO_TRACE, "text", title="Worked example 2: FIFO page replacement"),
        CODE(LRU_TRACE, "text", title="Worked example 2: LRU page replacement"),
        EX("Worked example 2: the key decisions",
           intro=r"Explain the replacements made at references 3 (the sixth reference) and 4 (the eighth) under each algorithm.",
           steps=[
               S("Both algorithms, first four references", text=r"7, 0 and 1 fill the empty frames (3 faults). Page 2 is a fault; 7 is both the oldest and the least recently used, so both replace 7."),
               S("Reference 3 under FIFO", text=r"Frames hold 2, 0, 1. Loading order was 0, 1, 2, so 0 is the oldest and is replaced, even though 0 was just used."),
               S("Reference 3 under LRU", text=r"Last uses: 1 at step 3, 2 at step 4, 0 at step 5. Page 1 is least recently used and is replaced."),
               S("Reference 4", text=r"FIFO replaces 2 (now the oldest). LRU looks at last uses 2 at step 4, 3 at step 6, 0 at step 7, so it also replaces 2."),
               S("Totals", text=r"FIFO causes 9 page faults and LRU causes 8 for this reference string."),
           ]),
        D(r"**Thrashing** happens when a process has too few frames, so it spends more time swapping pages between "
          r"disk and RAM than executing instructions. The CPU utilisation falls sharply. Remedies include adding RAM, "
          r"running fewer processes at once, or giving each process enough frames for its working set.",
          title="Thrashing"),
        EX("Worked example 3: segmentation",
           intro=r"A segment table contains: segment 0 base 1400 limit 1000; segment 1 base 6300 limit 400; segment 2 base 4300 limit 1100. Translate (a) segment 2, offset 53 and (b) segment 1, offset 852.",
           steps=[
               S("(a) Check the offset", text=r"53 is less than the limit 1100, so the address is valid."),
               S("(a) Add the base", math=r"4300 + 53 = 4353"),
               S("(b) Check the offset", text=r"852 is greater than the limit 400 of segment 1."),
               S("(b) Result", text=r"The address is outside the segment, so the hardware raises an addressing error (trap) and the OS handles it. No physical address is produced."),
           ]),
        H("Common mistakes"),
        MISTAKE("Changing the offset during translation",
                r"Only the page number is replaced by a frame number. The offset is copied unchanged into the physical address."),
        MISTAKE("Counting the first loads as hits",
                r"When the frames start empty, every first reference to a page is a page fault. Count these faults too."),
        MISTAKE("Mixing up FIFO and LRU",
                r"FIFO looks at when a page was **loaded**; LRU looks at when it was last **used**. A hit changes the LRU order but not the FIFO order."),
        QUIZ(r"Pages are 1 KiB (1024 bytes). Logical address 3100 is in which page, at what offset?",
             [r"Page 3, offset 28", r"Page 3, offset 100", r"Page 2, offset 1052", r"Page 31, offset 0"], 0,
             r"$3100 \div 1024 = 3$ remainder $3100 - 3072 = 28$.",
             feedback=["", r"That assumes 1000-byte pages; the page size is 1024 bytes.",
                       r"An offset must be less than the page size (1024).",
                       r"The page number is the quotient after dividing by the page size."]),
        QUIZ(r"Which statement about virtual memory is correct?",
             [r"It makes RAM physically larger", r"It lets programs larger than RAM run by keeping some pages on disk",
              r"It removes the need for a page table", r"It always makes programs run faster"], 1,
             r"Virtual memory uses disk space to hold pages not currently needed, so the logical address space can exceed physical RAM.",
             feedback=[r"The amount of RAM is unchanged; disk space is used instead.", "",
                       r"Virtual memory depends on page tables to find each page.",
                       r"Disk access is much slower than RAM; too many page faults slow programs down."]),
        H("Practice questions"),
        PQ(r"A system uses 2 KiB pages. A process's page table maps page 0 to frame 6, page 1 to frame 2 and page 2 to frame 9. Find the physical address of logical address 5000. [3 marks]",
           r"Page size = 2048. $5000 \div 2048 = 2$ remainder $5000 - 4096 = 904$, so page 2, offset 904 (1). Page 2 is in frame 9 (1). Physical address = $9 \times 2048 + 904 = 18\,432 + 904 = 19\,336$ (1)."),
        PQ(r"A process has 3 frames, initially empty, and references pages in the order 2, 3, 2, 1, 5, 2, 4, 5, 3, 2. Find the number of page faults using (a) FIFO and (b) LRU. [6 marks]",
           r"(a) FIFO: 2 F, 3 F, 2 hit, 1 F (frames 2, 3, 1), 5 F replaces 2, 2 F replaces 3, 4 F replaces 1, 5 hit, 3 F replaces 5, 2 hit. Total 7 page faults (3). (b) LRU: 2 F, 3 F, 2 hit, 1 F, 5 F replaces 3 (least recently used), 2 hit, 4 F replaces 1, 5 hit, 3 F replaces 2, 2 F replaces 4. Total 7 page faults (3)."),
        PQ(r"Using FIFO and the reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5, the number of page faults is 9 with 3 frames but 10 with 4 frames. (a) Comment on this result. (b) Explain why LRU is generally preferred to FIFO. [4 marks]",
           r"(a) Adding a frame increased the number of faults (1); with FIFO, more memory does not always mean fewer faults (this is known as Belady's anomaly) (1). (b) LRU uses recent past use to predict future use (1); pages in heavy use stay in memory, so it usually gives fewer faults than FIFO, which may remove a busy page just because it was loaded early (1)."),
        PQ(r"(a) Explain what is meant by thrashing. (b) State two differences between paging and segmentation. [4 marks]",
           r"(a) The system spends most of its time swapping pages between disk and main memory because processes do not have enough frames (1), so little useful processing is done (1). (b) Pages are fixed size, segments vary in size (1); paging is invisible to the programmer while segments match logical units of the program such as code, data or stack (1)."),
        SUM(r"Paging divides programs into fixed-size pages placed in any free frames; the page table maps pages to frames.",
            r"Physical address = frame number times page size plus offset; the offset never changes.",
            r"Segmentation uses variable-size logical segments; each offset is checked against the segment limit.",
            r"Virtual memory keeps unused pages on disk; a page fault loads a missing page into RAM.",
            r"FIFO replaces the oldest page, LRU the least recently used; count every first load as a fault.",
            r"Thrashing occurs when too much time is spent swapping pages instead of executing."),
    ],
))

# ---------------------------------------------------------------- Translators
LEXICAL = """
Source statement:   total = price * qty + 250;   // cost in FCFA

Lexeme   Token type
total    identifier
=        assignment operator
price    identifier
*        arithmetic operator
qty      identifier
+        arithmetic operator
250      integer literal
;        separator

Removed by the lexical analyser: spaces and the comment // cost in FCFA
Symbol table entries created: total, price, qty
"""

PARSE_TREE = """
Grammar (simplified BNF)
  <assignment> ::= <identifier> = <expression> ;
  <expression> ::= <term> | <expression> + <term>
  <term>       ::= <factor> | <term> * <factor>
  <factor>     ::= <identifier> | <integer>

Parse tree for  total = price * qty + 250 ;

               <assignment>
         /      |       \\        \\
      total     =    <expression>   ;
                    /     |     \\
           <expression>   +    <term>
                |                |
             <term>          <factor>
            /  |   \\             |
      <term>   *   <factor>     250
        |             |
    <factor>         qty
        |
      price

The multiplication sits lower in the tree, so it is done before the addition.
"""

ASSEMBLER = """
Assembly program               Pass 1: symbol table
Addr  Label  Opcode  Operand   Symbol  Address
0            LDA     NUM1      NUM1    4
1            ADD     NUM2      NUM2    5
2            STO     SUM       SUM     6
3            HLT
4     NUM1   DAT     15
5     NUM2   DAT     27
6     SUM    DAT     0

Pass 2: replace each symbol with its address
Addr  Instruction
0     LDA 4
1     ADD 5
2     STO 6
3     HLT
"""

LESSONS.append(lesson(
    module="Operating Systems & Translators",
    topic="Translators",
    title="Compilers, interpreters and assemblers",
    slug="compilers-interpreters-and-assemblers",
    minutes=30,
    summary="Describe the stages of compilation (lexical, syntax and semantic analysis), compare compilers with interpreters, and explain how a two-pass assembler works.",
    objectives=[
        "Explain why translators are needed",
        "Describe lexical, syntax and semantic analysis and the errors each detects",
        "Compare compilers and interpreters",
        "Explain how a two-pass assembler builds and uses a symbol table",
    ],
    key_concepts=["Translator", "Compiler", "Interpreter", "Assembler", "Lexical analysis", "Token",
                  "Symbol table", "Syntax analysis", "Parse tree", "Semantic analysis", "Object code"],
    blocks=[
        H("Introduction"),
        T(r"A processor only understands **machine code**: binary instructions for its own instruction set. "
          r"Programmers write in high-level languages such as Python or C, or in assembly language. A **translator** "
          r"converts this **source code** into a form the machine can execute. There are three kinds: compilers, "
          r"interpreters and assemblers."),
        KEY("Three kinds of translator", r"Each translates a different kind of source code, in a different way.",
            cards=[
                ["Compiler", r"Translates a whole high-level program into **object code** (machine code) before it runs. The object code can be run many times without the compiler."],
                ["Interpreter", r"Translates and executes a high-level program **one statement at a time**. No object code file is produced; the interpreter is needed every time the program runs."],
                ["Assembler", r"Translates **assembly language** into machine code. Each assembly instruction usually becomes one machine instruction."],
            ]),
        H("The stages of compilation"),
        D(r"The **lexical analyser** reads the source code character by character and groups the characters into "
          r"**lexemes**, each classified as a **token** (identifier, keyword, operator, literal, separator). It removes "
          r"spaces and comments, adds identifiers to the **symbol table**, and reports errors such as an illegal "
          r"character or a badly formed number.",
          title="Stage 1: lexical analysis"),
        CODE(LEXICAL, "text", title="Worked example 1: lexical analysis of one statement"),
        D(r"The **syntax analyser** (parser) checks that the sequence of tokens follows the **grammar** of the "
          r"language, often written in BNF. It builds a **parse tree** (or syntax tree) and reports syntax errors such "
          r"as a missing bracket or a missing operand.",
          title="Stage 2: syntax analysis"),
        CODE(PARSE_TREE, "text", title="Worked example 2: a parse tree"),
        EX("Worked example 2: finding a syntax error",
           intro=r"Using the grammar above, explain why the statement total = price + ; is rejected, and which stage rejects it.",
           steps=[
               S("Lexical analysis", text=r"The tokens are identifier, assignment operator, identifier, operator, separator. Every token is legal, so there is no lexical error."),
               S("Try to match the grammar", text=r"After + the grammar needs a term, which must be a factor: an identifier or an integer."),
               S("What is found", text=r"The next token is the separator ; so no term can be formed."),
               S("Conclusion", text=r"The syntax analyser reports an error such as missing operand after +. The program is not compiled."),
           ]),
        D(r"The **semantic analyser** checks that a syntactically correct program makes **sense**: variables are "
          r"declared before use, types are compatible in assignments and expressions, and subroutines are called with "
          r"the right number and type of parameters. It uses and updates the symbol table (for example, adding the "
          r"data type of each identifier).",
          title="Stage 3: semantic analysis"),
        EX("Worked example 3: semantic errors",
           intro=r'In C, a program declares int count; and later contains the statements count = "ten"; and total = count + 5; where total was never declared. Which stage detects each problem?',
           steps=[
               S("First statement", text=r"Its syntax is correct: identifier, =, literal, separator."),
               S("Type check", text=r"The symbol table says count is an int, but a string literal is being assigned. This is a type mismatch: a **semantic** error."),
               S("Second statement", text=r"Its syntax is correct too, but total is not in the symbol table."),
               S("Conclusion", text=r"Use of an undeclared identifier is also a **semantic** error. Both are found by the semantic analyser, not the parser."),
           ]),
        T(r"After analysis, the compiler goes on to **code generation**, producing object code, and usually **optimisation**, which makes the code faster or smaller without changing what it does. Linkers and loaders then combine object code with library routines and place it in memory."),
        H("Compilers versus interpreters"),
        KEY("Comparing the two", r"Exam questions often ask for advantages of each.",
            cards=[
                ["Compiler: advantages", r"The finished program runs faster, because translation happens once. Object code can be distributed without the source code, protecting it. The compiler is not needed to run the program."],
                ["Interpreter: advantages", r"Errors are reported as soon as the faulty line is reached, so testing and debugging are easier. Changes can be run immediately without recompiling. The same source runs on any machine that has the interpreter."],
            ],
            note=r"A compiler lists all the errors it finds after translating the whole program; an interpreter stops at the first error it meets."),
        H("Assemblers"),
        T(r"Assembly programs use **labels** (names for addresses). A label may be used before it is defined, for example a jump forward or data stored after the code. This is a **forward reference**. A **two-pass assembler** handles it: pass 1 builds a symbol table of labels and addresses; pass 2 uses the table to produce the machine code."),
        CODE(ASSEMBLER, "text", title="Worked example 4: a two-pass assembler"),
        EX("Worked example 4: the two passes",
           intro=r"Explain how the assembler translates the program above.",
           steps=[
               S("Pass 1", text=r"The assembler reads every line, counting addresses from 0. When it meets a label it records the label and the current address: NUM1 = 4, NUM2 = 5, SUM = 6."),
               S("Why one pass is not enough", text=r"At address 0, LDA NUM1 refers to NUM1, which is not defined until address 4. On a single pass its address would be unknown."),
               S("Pass 2", text=r"The assembler reads the program again, converts each opcode mnemonic to its binary code and replaces each label by its address from the symbol table: LDA 4, ADD 5, STO 6."),
           ]),
        H("Common mistakes"),
        MISTAKE("Calling every error a syntax error",
                r"Illegal characters are lexical errors; breaking the grammar is a syntax error; type mismatches and undeclared variables are semantic errors. Name the stage that actually detects the error."),
        MISTAKE("Saying an interpreter produces object code",
                r"An interpreter executes each statement as it translates it. It does not produce a separate executable file."),
        MISTAKE("Saying the lexical analyser checks grammar",
                r"The lexical analyser only identifies tokens. Checking the order of tokens against the grammar is the syntax analyser's job."),
        QUIZ(r"Which stage of compilation removes comments and white space from the source code?",
             [r"Syntax analysis", r"Semantic analysis", r"Lexical analysis", r"Code optimisation"], 2,
             r"The lexical analyser reads the raw characters, so it is the stage that discards comments and spaces before producing tokens.",
             feedback=[r"The parser works on tokens; comments have already gone.",
                       r"Semantic analysis checks meaning, such as types, using the tokens and parse tree.", "",
                       r"Optimisation works on generated code, long after comments were removed."]),
        QUIZ(r"A student wants to find and fix errors line by line while developing a program. Which translator is most suitable, and why?",
             [r"A compiler, because it produces faster code", r"An interpreter, because it stops at the first error and runs code immediately",
              r"An assembler, because it uses labels", r"A compiler, because it hides the source code"], 1,
             r"An interpreter reports each error as soon as the line is reached and lets the student rerun at once without recompiling.",
             feedback=[r"Speed of the final program does not help with finding errors during development.", "",
                       r"An assembler translates assembly language, not a high-level program.",
                       r"Protecting source code matters when distributing software, not when debugging it."]),
        H("Practice questions"),
        PQ(r"Describe the tasks carried out during the lexical analysis stage of compilation. [4 marks]",
           r"Any four: reads the source code character by character (1); groups characters into lexemes and converts them to tokens (1); removes white space and comments (1); enters identifiers into the symbol table (1); reports lexical errors such as illegal characters or invalid identifiers (1)."),
        PQ(r"For each error, state the compilation stage that detects it: (a) a variable used without being declared; (b) a missing closing bracket; (c) the character # in a place where the language does not allow it; (d) adding a string to an integer. [4 marks]",
           r"(a) Semantic analysis (1). (b) Syntax analysis (1). (c) Lexical analysis (1). (d) Semantic analysis, as a type mismatch (1)."),
        PQ(r"(a) Give two advantages of compiling a program rather than interpreting it. (b) Explain why an assembler needs two passes. [4 marks]",
           r"(a) The compiled program runs faster because it is translated only once (1); the object code can be distributed without the source code, and users do not need the translator (1). (b) Labels may be used before they are defined (forward references) (1); the first pass builds a symbol table of all labels and their addresses so the second pass can replace each label with its address (1)."),
        PQ(r"A program written in assembly language contains: 0 LDA X, 1 SUB Y, 2 STO Z, 3 HLT, 4 X DAT 40, 5 Y DAT 12, 6 Z DAT 0. Give the symbol table built in pass 1 and the translated first three instructions. [3 marks]",
           r"Symbol table: X = 4, Y = 5, Z = 6 (1). Translated: LDA 4 (1), SUB 5 and STO 6 (1)."),
        SUM(r"Translators convert source code to machine code: compilers, interpreters and assemblers.",
            r"Lexical analysis forms tokens, removes spaces and comments, and builds the symbol table.",
            r"Syntax analysis checks tokens against the grammar and builds a parse tree.",
            r"Semantic analysis checks meaning: declarations, types and parameters.",
            r"Compiled code runs faster; interpreters make debugging easier and need no recompiling.",
            r"A two-pass assembler builds a symbol table in pass 1 and generates machine code in pass 2."),
    ],
))

# ---------------------------------------------------------------- END OF LESSONS
