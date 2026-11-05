"""ICT A Level (796), Lower Sixth: in-depth lessons for every topic (KKEVO draft material for review).

Slugs start with ic6-. Existing overview lessons live in l6_ict.py and are not repeated here.
"""

from .dsl import *  # noqa: F403

COURSE = ("ict", "lower-sixth")

LESSONS = []

HW = "Hardware Maintenance & Deployment"
ENT = "Enterprise Infrastructure"
WEB = "Web Development"

# ===========================================================================
# PC hardware
# ===========================================================================
LESSONS.append(lesson(
    module=HW, topic="PC hardware",
    title="CPU sockets and chipsets: choosing parts that fit and work together",
    slug="ic6-cpu-sockets-chipsets", minutes=20,
    summary="Tell LGA, PGA and BGA sockets apart, check that a CPU, chipset, firmware and RAM type are compatible, and fit a processor and cooler in the correct order.",
    objectives=[
        "Distinguish LGA, PGA and BGA processor packages and name the main handling risk of each",
        "Apply the four compatibility checks before buying or fitting a CPU",
        "Explain why a motherboard may need a firmware update before it accepts a newer CPU",
        "List the steps for fitting a CPU and cooler safely, in order",
    ],
    key_concepts=["CPU socket", "LGA", "PGA", "BGA", "Chipset", "ZIF lever", "Thermal paste", "TDP"],
    blocks=[
        H("Introduction"),
        T("A computer shop in Bonaberi receives a customer with a brand new processor in a box. He bought it online "
          "for his old desktop and cannot understand why it will not go in. The seller is far away and the money is spent. "
          "A technician who knows how sockets and chipsets work could have told him in one minute that the part would not fit."),
        T("This lesson goes deeper than the overview. You will learn the three package types, a four-step compatibility "
          "check, and the safe order for fitting a CPU. These are the jobs a hardware technician does every week."),
        H("What a socket does"),
        D("A **CPU socket** is the mechanical and electrical interface between the processor and the motherboard. It holds "
          "the CPU in place and connects each of its contacts to the motherboard circuits that carry power, memory signals "
          "and data to the chipset.", title="Definition"),
        T("Every socket has a fixed number of contacts and a fixed layout. A processor made for one socket cannot be "
          "forced into another: the pattern of contacts, the notches and often the cooler holes are different. "
          "Manufacturers change sockets when a new generation needs more connections, such as new memory standards."),
        KEY("Three package types", "The difference is where the contacts are.", cards=[
            ["LGA (Land Grid Array)", "Flat gold pads under the CPU touch spring pins inside the motherboard socket. A clamp holds the CPU down. The fragile part is the socket pins, so keep the plastic cover on until the CPU is fitted."],
            ["PGA (Pin Grid Array)", "Pins stick out from the underside of the CPU and drop into holes in the socket. A ZIF (zero insertion force) lever opens the holes so no pushing is needed. The fragile part is the CPU pins."],
            ["BGA (Ball Grid Array)", "The chip is soldered to the board with tiny solder balls. It cannot be removed or upgraded by a normal technician. Laptops, tablets and phones use it."],
        ]),
        IMG("al-ic6-socket-types.svg", alt="Three diagrams side by side: LGA with pins in the socket and flat pads on the CPU, PGA with pins on the CPU, and BGA with solder balls fixed to the board.",
            caption="Figure 1. Where the contacts are in LGA, PGA and BGA"),
        H("The chipset and firmware"),
        D("The **chipset** is the group of controller chips on the motherboard that links the CPU to memory slots, storage "
          "ports, USB ports and expansion slots. The chipset decides how many ports and which features the board offers.",
          title="Definition"),
        T("Two boards can have the same socket but different chipsets. A cheaper chipset may offer fewer USB ports, fewer "
          "storage connections or no overclocking. And the same chipset may support a newer CPU only after the firmware "
          "(BIOS or UEFI) has been updated, because the old firmware does not contain the code that starts the new processor."),
        H("The four compatibility checks"),
        KEY("Check these in order before you buy", "Write the answers down.", cards=[
            ["1. Socket", "Does the CPU box name the same socket as the motherboard?"],
            ["2. Chipset and firmware", "Does the board maker's CPU support list include this exact CPU, and with which firmware version?"],
            ["3. Memory type", "Does the CPU and board use DDR4 or DDR5? The slots are keyed differently and the types are not interchangeable."],
            ["4. Power and cooling", "Does the cooler support this socket and the CPU's TDP (the heat in watts it is designed to give off)?"],
        ]),
        EX("Worked example 1: will this CPU work?", intro=(
            "A customer in Douala has a motherboard with socket X, chipset B, DDR4 memory. He wants to buy a CPU for socket X "
            "that needs DDR5. The board maker's list shows the CPU is supported only from firmware version 3. The board has "
            "version 2. Decide whether the upgrade works."), steps=[
            S("Socket", text="Both are socket X. The first check passes."),
            S("Chipset and firmware", text="The CPU is on the support list, but only from version 3. The board has version 2, so a firmware update is needed first."),
            S("Memory type", text="The board has DDR4 slots but the CPU needs DDR5. The check fails and the CPU cannot work here."),
            S("Decision", text="Do not buy. The memory type fails, and this cannot be fixed by firmware. The customer needs a different CPU or a different board."),
        ]),
        EX("Worked example 2: the order for fitting a CPU", intro=(
            "A technician must fit a new LGA processor and its cooler on a bare motherboard. Put the steps in a safe order."), steps=[
            S("Prepare", text="Work on a clean desk with an anti-static wrist strap clipped to bare metal. The board is not yet in the case, so no power cable is involved."),
            S("Open the socket", text="Lift the lever and the metal clamp. The plastic cover pops off by itself when the CPU is fitted. Keep it for later."),
            S("Align and lower", text="Match the triangle on the CPU corner and the notches with the socket. Lower the CPU straight down with no pressure. Never slide it."),
            S("Close the clamp", text="Lower the clamp and push the lever back under its catch. A little resistance is normal."),
            S("Paste and cooler", text="Apply a pea-sized amount of thermal paste, mount the cooler evenly, tighten the screws in a cross pattern, and connect the fan cable to the CPU fan header."),
        ]),
        EX("Worked example 3: an old board and a newer CPU", intro=(
            "A school ICT room has boards with the right socket, but they fail to start with newer CPUs of the same family. "
            "Explain a safe plan."), steps=[
            S("Find the cause", text="The socket matches, so the old firmware is the likely problem. It does not know the new CPU."),
            S("Update before upgrading", text="Fit the old CPU first, update the firmware with the board maker's tool, then power off."),
            S("Swap the CPU", text="Fit the new CPU and cooler as before and power on. Enter setup and check that the CPU is recognised."),
            S("If the old CPU is gone", text="Some boards have a flash button that updates firmware from a USB stick with no CPU. Check the manual."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking same socket means compatible", "Chipset, firmware version and memory type must also be checked. The socket is only the first of four checks."),
        MISTAKE("Forcing a CPU in", "If it does not drop in under its own weight, it is the wrong way round or the wrong socket. Force bends pins on either side."),
        MISTAKE("Forgetting the cooler's socket support", "A cooler bracket that fits one socket may not fit another, and a cooler too weak for the TDP makes the CPU slow down or shut off."),
        QUIZ("Which package type makes the CPU impossible to replace without special equipment?",
             ["LGA", "PGA", "BGA", "ZIF"], 2,
             "BGA chips are soldered to the board with solder balls, as in laptops and phones.",
             hint="Which one has the chip soldered down?",
             feedback=["LGA CPUs are removable: they sit under a clamp.", "PGA CPUs lift out when the ZIF lever is opened.", "",
                       "ZIF is a type of lever on a socket, not a package type."]),
        QUIZ("A new CPU fits the socket of an old motherboard, but the board does not start. What should be checked FIRST?",
             ["Whether the monitor cable is long enough", "Whether the motherboard firmware supports that CPU", "Whether the keyboard is USB", "Whether the case has a window"], 1,
             "The socket matches, so the likely cause is a firmware version that does not yet include the new CPU.",
             feedback=["The cable has nothing to do with the CPU not starting.", "",
                       "The keyboard type does not stop the board from recognising the CPU.",
                       "A window in the case has no effect on starting."]),
        H("Practice questions"),
        PQ("Explain the difference between an LGA and a PGA processor, and state one handling risk for each.",
           "In LGA the CPU has flat contact pads and the pins are in the motherboard socket. In PGA the pins are on the CPU "
           "and go into holes in the socket. LGA risk: bent socket pins if the CPU is dropped on wrongly or the cover is off. "
           "PGA risk: bent CPU pins when it is handled or forced."),
        PQ("List the four checks you would make before buying a processor for an existing motherboard.",
           "1. The socket named on the CPU matches the board. 2. The chipset and firmware version on the board maker's support list "
           "include the CPU. 3. The memory type of the CPU matches the board (for example DDR4 or DDR5). 4. The cooler supports the socket "
           "and the CPU's TDP."),
        PQ("A technician fits a cooler without thermal paste. Describe what will happen and why.",
           "The metal surfaces of the CPU and cooler are not perfectly flat, so air gaps remain between them. Air conducts heat badly, so "
           "heat is not carried away. The CPU overheats, slows down to protect itself and then shuts down."),
        PQ("Why can a motherboard with a matching socket still fail to start with a newer CPU? State how it is fixed.",
           "Its firmware (BIOS or UEFI) does not yet contain the code for that CPU. Fix: update the firmware, using a compatible older CPU "
           "or the board's flash feature, then fit the new CPU."),
        SUM("A socket connects the CPU to the board; LGA has pins in the socket, PGA has pins on the CPU and BGA is soldered.",
            "The chipset controls the ports and features the board offers around the CPU.",
            "Check four things: socket, chipset and firmware, memory type, cooling and TDP.",
            "Fit a CPU with no force: align the marker, close the clamp, paste, then cooler, then fan cable.",
            "A firmware update may be needed before a newer CPU of the same socket will start."),
    ]))

LESSONS.append(lesson(
    module=HW, topic="PC hardware",
    title="RAM types, channels and memory bandwidth",
    slug="ic6-ram-channels-bandwidth", minutes=22,
    summary="Compare DDR memory generations, work out theoretical bandwidth for single and dual channel, and install matched modules in the correct slots.",
    objectives=[
        "Describe the role of RAM and why memory speed and capacity both matter",
        "Calculate theoretical bandwidth for single-channel and dual-channel memory",
        "Install modules in the correct slots to get dual-channel operation",
        "Choose between more capacity and more speed for a stated user need",
    ],
    key_concepts=["RAM", "DDR", "MT/s", "Bandwidth", "Channel", "Dual-channel", "Matched pair", "DIMM and SO-DIMM"],
    blocks=[
        H("Introduction"),
        T("A secretary in Yaounde complains that her office PC freezes when she has the spreadsheet, the browser and a video call "
          "open together. The manager wants to buy a faster processor. A technician opens the system information and sees only "
          "4 GB of memory with one module installed. Memory, not the processor, is the weak part."),
        T("Memory has two main properties that matter: how much it holds (capacity) and how fast data can move to and from "
          "the CPU (bandwidth). This lesson shows you how to calculate bandwidth and how channels double it."),
        H("RAM basics"),
        D("**RAM** (random access memory) is the fast, volatile working memory that holds the programs and data the CPU is using "
          "now. It loses its contents when power is removed.", title="Definition"),
        T("Modern desktop memory is **DDR SDRAM** (double data rate). DDR sends data on both the rising and the falling edge of the "
          "clock, which is why speeds are quoted in **MT/s** (mega-transfers per second). Each new generation (DDR3, DDR4, DDR5) "
          "is faster and uses less voltage, but the slots are keyed differently so the generations cannot be mixed."),
        T("Desktops use full-size **DIMM** modules. Laptops use the shorter **SO-DIMM** modules. The two are not interchangeable."),
        H("Bandwidth"),
        D("**Memory bandwidth** is the amount of data that can be moved between memory and the CPU each second. For a 64-bit "
          "(8-byte) channel it is the transfer rate multiplied by 8 bytes.", title="Definition",
          formula=r"\text{bandwidth (MB/s)} = \text{MT/s} \times 8 \times \text{number of channels}"),
        EX("Worked example 1: bandwidth of one module", intro=(
            "A DDR4 module is labelled 3200 MT/s. Find its theoretical bandwidth in single-channel mode, in GB per second."), steps=[
            S("Write the formula", math=r"3200 \times 8 \text{ MB/s}"),
            S("Multiply", math=r"3200 \times 8 = 25\,600 \text{ MB/s}"),
            S("Convert", text="1000 MB make 1 GB for this calculation, so the answer is 25.6 GB/s."),
        ]),
        EX("Worked example 2: dual channel", intro=(
            "Two identical DDR4 modules of 3200 MT/s each are installed, one in each channel. Find the bandwidth. A second PC has "
            "the same two modules placed in the same channel. Compare."), steps=[
            S("Dual channel", math=r"3200 \times 8 \times 2 = 51\,200 \text{ MB/s}", text="That is 51.2 GB/s: both channels work at the same time."),
            S("Same channel", text="Two modules on one channel share a single 64-bit path. The bandwidth stays at 25.6 GB/s."),
            S("Compare", text="The correct placement gives twice the theoretical bandwidth with the same hardware."),
        ]),
        IMG("al-ic6-dual-channel.svg", alt="A memory controller connected to two channels, each channel with one module in a slot, showing 25.6 GB per second per channel and 51.2 GB per second together.",
            caption="Figure 1. One module per channel gives double the bandwidth"),
        T("Real programs do not reach the theoretical figure, so we call it the maximum possible. A dual-channel system gives the "
          "biggest gain when the CPU and the integrated graphics share the memory, as in many low-cost office PCs."),
        H("Installing for dual channel"),
        KEY("Rules for dual channel", "Follow all four.", cards=[
            ["Use a matched pair", "Same capacity, same speed and same type. Modules sold in a kit are tested together."],
            ["Use one module per channel", "The board manual shows which slots belong to which channel, often marked A1, A2, B1, B2."],
            ["Check the colour coding", "Many boards colour the slots to show which ones to fill first for two modules. The manual is the final word, because layouts differ."],
            ["Confirm in firmware", "Setup or system information shows 2 channels or dual-channel mode."],
        ]),
        EX("Worked example 3: capacity or speed?", intro=(
            "A video editor in Limbe has 8 GB of DDR4-2666 in one module and the PC is slow with large projects. Budget allows 16 GB "
            "of RAM. Advise what to buy."), steps=[
            S("Find the main bottleneck", text="Large projects exceed 8 GB, so the PC swaps data to the disk, which is far slower than RAM. Capacity is the first problem."),
            S("Choose a kit", text="Buy two matched 8 GB DDR4-2666 modules and replace the single module, so that the memory runs as 16 GB in dual channel."),
            S("Bandwidth gain", math=r"2666 \times 8 \times 2 = 42\,656 \text{ MB/s}", text="About 42.7 GB/s, twice the 21.3 GB/s of the old single module."),
            S("Conclusion", text="Capacity removes the swapping, and dual channel raises the speed. Buying a faster single module alone would fix neither well."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing MT/s and MHz", "DDR4-3200 runs its clock at 1600 MHz and transfers twice per clock, so the rate is 3200 MT/s. Use the transfer rate in the bandwidth formula."),
        MISTAKE("Forgetting the 8 bytes", "A 64-bit channel moves 8 bytes per transfer. Dividing or multiplying by the wrong number gives a wrong answer."),
        MISTAKE("Believing more RAM always means faster", "Extra RAM only helps when the PC was running out of memory. Capacity cures slowness caused by swapping; it does not speed up a lightly used system."),
        QUIZ("Two identical modules are installed in slots of the same channel. What is the effect?",
             ["The system runs in dual-channel mode", "The system will not start", "The bandwidth stays at single-channel level", "The capacity is halved"], 2,
             "A channel is a single 64-bit path. Two modules on it share the path, so bandwidth does not double. Capacity still adds up.",
             feedback=["Dual channel needs one module in each channel.", "Both modules are valid, so the PC starts. Only performance is lower than it could be.", "",
                       "Capacity adds up whatever the slots; it is not halved."]),
        QUIZ("What is the theoretical bandwidth of one DDR4 module rated at 2400 MT/s?",
             ["9.6 GB/s", "19.2 GB/s", "38.4 GB/s", "2.4 GB/s"], 1,
             "2400 x 8 = 19 200 MB/s = 19.2 GB/s.",
             hint="Multiply by 8 bytes for one channel.",
             feedback=["That is 2400 x 4: 4 bytes is the width of a 32-bit path, not a 64-bit channel.", "",
                       "That is the dual-channel figure, which needs two modules.", "That forgets the multiplication by 8 bytes."]),
        H("Practice questions"),
        PQ("Calculate the theoretical bandwidth, in GB/s, of two DDR4-2666 modules in dual channel.",
           "2666 x 8 x 2 = 42 656 MB/s, about 42.7 GB/s (21.3 GB/s per channel)."),
        PQ("A technician installs two 4 GB modules in the first two slots, which share a channel. Explain what is wrong and how to correct it.",
           "Both modules share one channel, so the bandwidth is single-channel. Move one module to a slot of the other channel as shown in the board manual "
           "(for example A2 and B2), then confirm dual-channel mode in the firmware setup."),
        PQ("State two rules for choosing modules when installing a dual-channel kit.",
           "Any two: same capacity; same speed; same memory type (for example both DDR4); preferably from the same kit; correct form (DIMM for desktops)."),
        PQ("Explain why adding RAM can make a slow PC faster, and when it will not.",
           "If the PC runs out of RAM, the operating system uses the disk for virtual memory, which is much slower, so adding RAM removes that delay. "
           "If the PC is slow for other reasons (full disk, malware, weak CPU) and memory is not nearly full, more RAM gives little change."),
        SUM("RAM is volatile working memory; DDR generations are keyed differently and cannot be mixed.",
            "Bandwidth for a 64-bit channel is MT/s multiplied by 8 bytes, and by the number of channels.",
            "Dual channel needs matched modules in different channels, in the slots the manual names.",
            "Capacity stops swapping to disk; bandwidth speeds up each transfer. Choose by the real bottleneck."),
    ]))

LESSONS.append(lesson(
    module=HW, topic="PC hardware",
    title="BIOS and UEFI setup: settings, security and firmware updates",
    slug="ic6-bios-uefi-setup", minutes=22,
    summary="Compare legacy BIOS with UEFI, change boot order, Secure Boot and virtualization settings, recover from lost settings and update firmware without risking the board.",
    objectives=[
        "Compare legacy BIOS and UEFI on disk support, start-up and security",
        "Change the boot order, Secure Boot and virtualization settings for a stated job",
        "Explain the role of the CMOS battery and how setup settings are reset",
        "State the precautions needed before a firmware update",
    ],
    key_concepts=["BIOS", "UEFI", "CSM", "Secure Boot", "Boot order", "CMOS battery", "Firmware update", "Virtualization support"],
    blocks=[
        H("Introduction"),
        T("A lab technician at a secondary school in Bafoussam must reinstall the operating system on twenty old PCs from a USB "
          "stick. On every PC the machine ignores the stick and loads the old system. Pressing the right key to open the firmware "
          "setup and changing one setting solves it. Firmware is the first program that runs, and the technician controls it."),
        H("What firmware is"),
        D("**Firmware** is permanent software stored on a chip on the motherboard. When the power button is pressed, the firmware "
          "starts first. It tests the hardware, lets the user change hardware settings, and then hands control to the "
          "boot loader of an operating system.", title="Definition"),
        D("**Legacy BIOS** (Basic Input/Output System) is the older firmware design. It starts in a simple 16-bit mode, reads the "
          "first sector of a disk (the master boot record) and runs the code found there. **UEFI** (Unified Extensible Firmware "
          "Interface) is the modern design. It loads a boot loader file from a special small partition, supports large GPT disks, "
          "has a graphical setup with mouse support and offers Secure Boot.", title="Definition"),
        CODE("""
Feature                 Legacy BIOS             UEFI
Boot data read from     MBR (first sector)      EFI system partition (a file)
Partition style         MBR                     GPT (MBR possible in CSM mode)
Disk size limit         about 2 TB (MBR)        far above 2 TB (GPT)
Setup interface         text menus, keyboard    graphical, often mouse
Secure Boot             not available           available
Start-up speed          slower                  faster (fast boot options)
""", "text", title="Table 1", caption="Legacy BIOS compared with UEFI"),
        T("**CSM** (Compatibility Support Module) is a UEFI option that lets a UEFI board behave like an old BIOS, so older "
          "systems on MBR disks can still start. A board in UEFI mode will not start an MBR-only installation, and a board in CSM "
          "mode will not start a UEFI-only installation. The boot mode must match the way the operating system was installed."),
        H("Settings you must know"),
        KEY("Six common settings", "Open setup with the key shown at start-up (often Delete, F2 or F10; check your model).", cards=[
            ["Boot order", "The list of devices the firmware tries, in order. Put the USB device first to install, then put the disk first again."],
            ["Secure Boot", "Only boot loaders with a trusted digital signature are allowed. It blocks some boot-sector malware. Some older Linux media may need it switched off."],
            ["Virtualization support", "Lets the CPU run virtual machines efficiently. It is often off by default, so a hypervisor refuses to start until it is enabled."],
            ["Date and time", "Wrong time breaks website certificates and logs. The CMOS battery keeps the clock running."],
            ["Setup password", "Stops other people from changing boot order or turning off Secure Boot. Keep a written record in a safe place."],
            ["Load defaults", "Resets all settings to the maker's values when something has been set wrongly."],
        ]),
        IMG("al-ic6-boot-sequence.svg", alt="Flow from power on, to firmware start, POST, then boot order, then boot loader, then operating system.",
            caption="Figure 1. From power button to operating system"),
        H("The CMOS battery and resetting settings"),
        T("Settings are kept in a tiny amount of memory powered by a coin cell battery on the board (commonly called the CMOS "
          "battery). When the battery is flat, the date resets and custom settings are lost each time the PC is unplugged. "
          "Replace it with the same type. To clear settings or a forgotten setup password on a desktop, the usual method is to "
          "power off, unplug, move the clear-CMOS jumper (or remove the battery for a minute), then restore it. Always follow "
          "the board manual."),
        H("Updating firmware"),
        D("A **firmware update** (flashing) replaces the firmware with a newer version from the board maker. It can add support "
          "for new CPUs, fix security flaws and correct faults. It also carries a risk: if power fails during the update, the "
          "firmware may be left half written and the board may not start.", title="Definition"),
        KEY("Before you flash", "Treat it as a risky job.", cards=[
            ["Need", "Update only for a reason, such as CPU support or a security fix. Do not update just because a newer version exists."],
            ["Power", "Use a UPS or a laptop with a charged battery. Power cuts are a real danger in many workshops."],
            ["Source", "Download only from the maker's own website, for the exact model and revision."],
            ["Notes", "Read the release notes and save the current settings before starting. Never switch off during the update."],
        ]),
        EX("Worked example 1: booting from USB for an installation", intro=(
            "A PC will not start from the installer USB stick. Explain the steps to make it boot from the stick."), steps=[
            S("Insert the stick", text="Plug it into a USB port on the back of the PC, which is more reliable."),
            S("Open setup", text="Restart and press the setup key shown on the first screen, or the one-time boot menu key."),
            S("Check the mode", text="If the stick was made for UEFI, keep the board in UEFI mode. For an older stick, enable CSM."),
            S("Change the order", text="Move the USB device to the top of the boot order, or select it once from the boot menu."),
            S("Save and restart", text="Save changes and exit. After the installation finishes, put the disk first again so the stick is not used again."),
        ]),
        EX("Worked example 2: a virtual machine will not start", intro=(
            "A student installs a hypervisor on her laptop. It reports that hardware virtualization is not available. "
            "The CPU is known to support it. What is the fault and the fix?"), steps=[
            S("Spot the cause", text="Virtualization support is a CPU feature that the firmware can switch off. It is often disabled by default."),
            S("Open setup", text="Restart, enter setup and find the advanced CPU or security page."),
            S("Enable it", text="Turn on the virtualization option, save and restart."),
            S("Test", text="Start the virtual machine again. If it still fails, check that another hypervisor is not using the feature."),
        ]),
        EX("Worked example 3: recovering from a bad settings change", intro=(
            "A user changes several advanced settings and the PC now shows no picture at all. Describe a recovery plan."), steps=[
            S("Power off safely", text="Switch off at the wall and unplug."),
            S("Clear the stored settings", text="Move the clear-CMOS jumper or remove the coin cell for about a minute, then restore it, following the manual."),
            S("Power on and reload defaults", text="Enter setup, load optimized defaults, set the date and time, and set the boot order again."),
            S("Keep a record", text="Write down the original values before any future change."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mismatching boot mode and installation", "An OS installed in UEFI mode on GPT will not start if the board is later switched to CSM mode. Keep a note of which mode was used."),
        MISTAKE("Flashing firmware during a power cut", "A failed update can leave the board unusable. Use a UPS and do not start if the power is unreliable."),
        MISTAKE("Leaving the USB stick first in the boot order", "The installer starts again after every restart and may wipe the disk. Reset the order after installing."),
        QUIZ("Which feature of UEFI helps to block malware that tries to replace the boot loader?",
             ["CSM", "Secure Boot", "Dual channel", "Fast boot"], 1,
             "Secure Boot allows only boot loaders with a trusted digital signature to run.",
             feedback=["CSM provides old BIOS behaviour and does not check signatures.", "",
                       "Dual channel is a memory feature, not a security feature.",
                       "Fast boot shortens start-up checks; it is not a protection."]),
        QUIZ("A laptop forgets the date every time it is unplugged. What is the most likely fault?",
             ["The hard disk has bad sectors", "The CMOS battery is flat", "Secure Boot is switched on", "The RAM is in single-channel mode"], 1,
             "The coin cell battery powers the clock and settings memory. When it is flat, they are lost on power-off.",
             feedback=["Bad sectors cause read errors, not a lost date.", "",
                       "Secure Boot decides which boot software may start, not the clock.",
                       "Channel mode affects speed, not the clock."]),
        H("Practice questions"),
        PQ("State three differences between legacy BIOS and UEFI.",
           "Any three: UEFI supports GPT disks above 2 TB, BIOS uses MBR; UEFI offers Secure Boot; UEFI has a graphical setup with mouse; "
           "UEFI starts faster; UEFI loads a boot loader file from the EFI system partition, BIOS runs code from the first sector of the disk."),
        PQ("Explain why a technician should set the boot order back to the disk after installing an operating system from USB.",
           "If the USB device stays first, the PC may start the installer again after each restart, delaying start-up and risking repeating the install "
           "or erasing the disk. The disk should be tried first so the PC loads the installed system."),
        PQ("Give three precautions to take before updating the firmware of a motherboard.",
           "Any three: confirm that an update is needed; download only from the maker for the exact model; read release notes; save current settings; "
           "use a UPS or fully charged battery; never switch off during the update."),
        PQ("A user cannot enter the BIOS setup because a password was set and forgotten. Describe one way to recover on a desktop board.",
           "Power off and unplug, then clear the CMOS using the board's jumper or by removing the coin cell for about a minute and refitting it, "
           "as in the manual. This resets the stored settings including the password. Then set the date, boot order and a new password that is recorded safely."),
        SUM("Firmware starts first, tests the hardware and passes control to the boot loader.",
            "UEFI adds GPT support, Secure Boot and a graphical setup; CSM gives old BIOS behaviour.",
            "Boot mode must match how the OS was installed. Reset the boot order after installing from USB.",
            "The CMOS battery keeps the clock and settings; clearing it resets the board.",
            "Update firmware only when needed, with stable power and the maker's file."),
    ]))

LESSONS.append(lesson(
    module=HW, topic="PC hardware",
    title="Fault finding: POST, beep codes and a method for a PC that will not start",
    slug="ic6-post-fault-finding", minutes=22,
    summary="Follow the order of events from power-on, read POST signals, and use a systematic method with known-good parts to find faults in power, memory, display and heat.",
    objectives=[
        "Describe the stages from pressing the power button to the loading of the operating system",
        "Use beeps, LEDs and screen messages as clues, always checking the board manual",
        "Apply a structured fault-finding method with a minimal configuration and known-good parts",
        "Link common symptoms to likely faults and to a first action",
    ],
    key_concepts=["POST", "Beep code", "Diagnostic LED", "Minimal configuration", "Known-good part", "PSU", "Overheating"],
    blocks=[
        H("Introduction"),
        T("A trader in Mokolo brings a desktop to your workshop. He says it is dead. Before you buy any part, a good technician "
          "asks questions and tests in order. Most faults are found in the first ten minutes if you follow a method."),
        H("What happens at power-on"),
        T("When the power button is pressed, the power supply (PSU) checks its own voltages and signals the motherboard that "
          "power is good. The CPU then starts and runs the firmware. The firmware runs the **POST** (power-on self-test): it checks the CPU, memory, "
          "graphics and key controllers. If POST passes, the firmware reads the boot order and passes control to the boot loader."),
        D("A **beep code** is a pattern of short and long beeps, made by a small speaker on the motherboard, that reports a fault "
          "found by POST before the display works. Many boards also have **diagnostic LEDs** or a small display showing a code. "
          "The meaning of each pattern is different from one maker to another and is in the motherboard manual.", title="Definition"),
        IMG("al-ic6-boot-sequence.svg", alt="Flow from power on, to firmware start, POST, then boot order, then boot loader, then operating system.",
            caption="Figure 1. The sequence of events; a fault stops the sequence at one step"),
        T("The key idea: the last step that worked tells you where the fault is. If there is no light, no fan and no sound, "
          "the problem is before the POST, in power. If fans spin and there are beeps, the problem is found by POST. If the logo "
          "appears and then a message says no boot device was found, POST passed and the fault is in storage, boot order or the OS."),
        H("A method for finding faults"),
        KEY("Six steps", "Do not skip steps.", cards=[
            ["1. Ask and observe", "What happened just before? Power cut, new part, water, move? Look and smell for damage."],
            ["2. Check the simple things", "Wall socket, extension lead, power switch on the PSU, monitor cable and monitor power."],
            ["3. Use the clues", "Beeps, LEDs, messages, fan behaviour. Look up codes in the manual."],
            ["4. Reduce to the minimum", "Remove everything not needed to start: extra drives, cards, USB devices. Keep CPU, one RAM module, PSU and (if needed) a graphics source."],
            ["5. Swap with known-good parts", "Replace one suspected part at a time with a part that is known to work. Change one thing at a time."],
            ["6. Record and fix", "When the fault goes, note the cause, replace the faulty part and test over a period."],
        ]),
        CODE("""
Symptom                               Likely cause                 First action
No power, no fan, no light            Wall socket, lead, PSU       Test socket with another device; check PSU switch
Fans spin, no beep, no picture        CPU, board, RAM seating      Reseat RAM; minimal configuration
Repeating beeps, no picture           RAM or graphics fault        Look up code; reseat RAM / card
Picture, then no boot device found    Disk, cable, boot order      Check disk is detected in setup
Shuts down after a few minutes        Overheating or weak PSU      Check fan, dust, thermal paste
Date resets each day                  Flat CMOS battery            Replace the coin cell
""", "text", title="Table 1", caption="Symptoms, likely causes and first actions (a guide, not a rule)"),
        EX("Worked example 1: the dead PC", intro=(
            "The trader's PC shows no light and no fan. Describe how you would find the fault."), steps=[
            S("Ask", text="He says a lightning storm happened last night."),
            S("Simple checks", text="Plug a phone charger into the same socket to test it. Check the lead and the PSU rear switch."),
            S("Test the PSU", text="If the socket is good, try a known-good power cable and then a known-good PSU of suitable rating."),
            S("Result", text="With a known-good PSU the PC starts, so the old PSU had failed. Replace it and advise the trader to use a surge protector or UPS."),
        ]),
        EX("Worked example 2: fans spin but no picture", intro=(
            "A PC powers up, fans spin, nothing appears on the screen, and there is one long beep followed by two short beeps. "
            "The manual (for this board) says that pattern means a graphics fault. Find the fault."), steps=[
            S("Trust the manual", text="The pattern is a clue for this board only, so use the table in its manual."),
            S("Check the display chain", text="Check the monitor is on and set to the right input, and the cable is fully inserted."),
            S("Reseat the graphics card", text="Switch off, unplug, remove the card and refit it until the latch clicks. Check the power connector."),
            S("Use a known-good test", text="Try the monitor on the board's built-in output, or put the card in another PC."),
            S("Conclude", text="If the picture returns using another card or the built-in output, the card was faulty."),
        ]),
        EX("Worked example 3: random shutdowns", intro=(
            "A customer's PC works for ten minutes and then switches off without warning. Diagnose the problem."), steps=[
            S("Think of heat", text="A time delay before failure suggests temperature rising until a safety shut-down."),
            S("Inspect", text="Open the case. Check that the CPU fan spins, remove dust from the heatsink with a brush and check the thermal paste."),
            S("Measure", text="Use the temperature readings in setup or a monitoring tool at idle and under load. A CPU close to its maximum temperature points to cooling faults."),
            S("Fix and retest", text="Clean the fan, refit the cooler with new paste and run the PC for a long test. If the shutdowns continue, test the PSU under load."),
        ]),
        H("Common mistakes"),
        MISTAKE("Changing several things at once", "If you replace RAM, PSU and graphics card together and the PC starts, you do not know which was faulty."),
        MISTAKE("Assuming beep codes are universal", "A pattern means different things on different boards. Always check the manual for that model."),
        MISTAKE("Skipping the simple checks", "A loose power cable or a dead extension lead causes many faults. Check these before opening the case."),
        QUIZ("A PC shows no light, no fan and no sound. In which stage of the start-up sequence is the fault?",
             ["Boot loader", "Before POST, in the power chain", "In the operating system", "In the screen resolution settings"], 1,
             "With no sign of life, power never reached the point where POST runs. Check the socket, lead and PSU.",
             feedback=["The boot loader runs much later, after POST and the boot order.", "",
                       "The operating system has not even started.",
                       "Resolution settings need a working display and operating system."]),
        QUIZ("Why do you change only one part at a time when swapping with known-good parts?",
             ["It uses less electricity", "So that you know which part was the cause", "Because boards only accept one part", "To avoid reading the manual"], 1,
             "If several parts change together and the fault disappears, you cannot tell which one was faulty.",
             feedback=["Power use is not the reason.", "", "Boards accept many parts; the point is the logic of testing.",
                       "The manual is still needed for codes and slot positions."]),
        H("Practice questions"),
        PQ("Describe the purpose of POST and say what it checks.",
           "POST is the self-test run by the firmware at power-on. It checks the CPU, memory, graphics and key controllers before looking for an operating system, "
           "so that hardware faults are found early. Faults found before the display works are shown by beep codes or diagnostic LEDs."),
        PQ("A PC gives repeated beeps and no display. Explain why you must use the motherboard manual and what you do next.",
           "Beep codes differ between firmware makers and models, so the same pattern can mean different faults. Look up the pattern for the exact board. "
           "If it points to memory, reseat the RAM, test one module at a time and try a known-good module."),
        PQ("Explain what a minimal configuration is and why it is used.",
           "It is the smallest set of parts that lets a PC start: PSU, motherboard, CPU, one RAM module and a display source. Other devices are removed. "
           "It removes unrelated parts that might cause the fault, so the faulty part can be found by adding items back one at a time."),
        PQ("A PC works for a short time and then switches off. List three checks.",
           "Any three: CPU fan spinning; dust in the heatsink and vents; thermal paste on the CPU; temperature readings in setup; case airflow; PSU under load; room temperature."),
        SUM("Start-up order: PSU power good, CPU starts, firmware, POST, boot order, boot loader, OS.",
            "The last stage that worked shows where the fault is.",
            "Beep codes and LEDs are clues whose meaning must be checked in the board manual.",
            "Use a method: ask, simple checks, clues, minimal configuration, swap one known-good part at a time, record.",
            "Common faults: power supply, RAM seating, graphics, disk or cables, and overheating."),
    ]))

# ===========================================================================
# OS deployment
# ===========================================================================
LESSONS.append(lesson(
    module=HW, topic="OS deployment",
    title="Partition styles: MBR and GPT",
    slug="ic6-mbr-gpt-partitioning", minutes=22,
    summary="Compare MBR and GPT, calculate the 2 TiB limit of MBR, explain why UEFI normally uses GPT and decide which style suits a given disk and firmware.",
    objectives=[
        "Explain what a partition table is and what MBR and GPT each store",
        "Calculate the maximum disk size addressable by MBR from the sector count and sector size",
        "State the partition and size limits of MBR and the main benefits of GPT",
        "Choose MBR or GPT for a disk from its size and the firmware mode",
    ],
    key_concepts=["Partition", "Partition table", "MBR", "GPT", "Sector", "EFI system partition", "Primary partition", "Protective MBR"],
    blocks=[
        H("Introduction"),
        T("A computer shop in Bamenda buys a 4 TB external drive for a school's video archive. The technician initialises the "
          "disk with the old style and finds that only about 2.2 TB can be used. The rest is wasted. The reason lies in the "
          "partition table, and the fix is a different partition style."),
        H("Disks, sectors and partitions"),
        D("A **partition** is a defined section of a disk that the operating system treats as a separate volume. A **partition "
          "table** is the record, stored on the disk, that says where each partition starts and how large it is.", title="Definition"),
        T("Disks are divided into **sectors**, the smallest units that can be addressed. Older disks use 512-byte sectors, and many "
          "new disks use 4096-byte sectors. A partition table stores start positions as sector numbers, so the number of bits "
          "used for the sector number sets the largest size it can describe."),
        H("MBR"),
        D("**MBR** (Master Boot Record) is the older partition style. It sits in the first sector of the disk. It holds a "
          "small boot program and a table with room for only **four** primary partitions. Each partition's start and size are "
          "stored as **32-bit** sector numbers.", title="Definition"),
        F(r"\text{maximum size} = 2^{32} \times 512 \text{ bytes} = 2\,199\,023\,255\,552 \text{ bytes} = 2 \text{ TiB}", title="MBR limit with 512-byte sectors"),
        T("To get more than four partitions on an MBR disk, one of the four slots is made an **extended partition**, which holds "
          "logical partitions inside it. This works, but it is a workaround."),
        EX("Worked example 1: the 4 TB drive", intro=(
            "A drive advertised as 4 TB has 4 000 000 000 000 bytes. It uses 512-byte sectors and is initialised as MBR. How much "
            "space cannot be used?"), steps=[
            S("Find the MBR limit", math=r"2^{32} \times 512 = 2\,199\,023\,255\,552 \text{ bytes}"),
            S("Subtract", math=r"4\,000\,000\,000\,000 - 2\,199\,023\,255\,552 = 1\,800\,976\,744\,448 \text{ bytes}"),
            S("Say it in TB", text="About 1.8 TB is wasted. Only about 2.2 TB (decimal) is usable."),
            S("Fix", text="Convert the disk to GPT. The data must be backed up first, because converting normally means clearing the disk unless the tool supports a safe conversion."),
        ]),
        T("Note that 2 TiB means 2 binary terabytes (2 x 2 to the power 40 bytes). That equals about 2.2 decimal terabytes, which is "
          "why a disk marked 2 TB fits an MBR table, but a 3 TB disk does not."),
        H("GPT"),
        D("**GPT** (GUID Partition Table) is the modern partition style. It stores sector numbers in **64 bits**, so it can describe "
          "disks of many zebibytes. It normally allows **128** partitions by default, keeps a **backup copy** of the table at the "
          "end of the disk and uses **checksums** (CRC) to detect damage to the table.", title="Definition"),
        KEY("MBR compared with GPT", "", cards=[
            ["MBR", "32-bit sector numbers: about 2 TiB maximum with 512-byte sectors. Four primary partitions. One copy of the table. Boots on legacy BIOS."],
            ["GPT", "64-bit sector numbers: huge limit. 128 partitions by default. Backup table at the end of the disk plus checksums. Required for UEFI booting of Windows and normal for Linux on UEFI."],
        ]),
        IMG("al-ic6-mbr-gpt.svg", alt="Two disk bars. The MBR disk has a boot record at the start followed by up to four partitions. The GPT disk has a protective MBR, a primary table, partitions, and a backup table at the end.",
            caption="Figure 1. Layout of an MBR disk and a GPT disk"),
        T("A GPT disk keeps a **protective MBR** in its first sector. It reports one large partition so that old tools that "
          "only understand MBR do not think the disk is empty and write over it. A UEFI system also needs a small **EFI system "
          "partition** (a FAT-formatted partition) that holds the boot loader files."),
        H("Choosing the style"),
        EX("Worked example 2: which style for each case?", intro=(
            "Decide between MBR and GPT for (a) a 500 GB disk in a 2009 PC with legacy BIOS, (b) a 4 TB data disk in a modern PC, "
            "(c) a new laptop with UEFI that will run Windows."), steps=[
            S("Case a", text="Legacy BIOS boots from MBR. 500 GB is below the MBR limit. Use MBR."),
            S("Case b", text="4 TB is above the MBR limit of about 2.2 TB. Use GPT."),
            S("Case c", text="UEFI Windows installations boot from GPT with an EFI system partition. Use GPT."),
        ]),
        EX("Worked example 3: a partition plan", intro=(
            "A 1 TB disk must be planned for UEFI Windows: an EFI system partition of 100 MB, a system "
            "partition of 400 GB and a data partition using the remainder. Take 1 TB as 1000 GB and 1 GB as 1000 MB. Find the size of the data partition."), steps=[
            S("Add what is used", math=r"100 \text{ MB} + 400 \text{ GB} = 400.1 \text{ GB}"),
            S("Subtract from the total", math=r"1000 - 400.1 = 599.9 \text{ GB}"),
            S("Answer", text="The data partition is about 599.9 GB. In real use a small recovery partition and rounding by the tool change the figure slightly."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying GPT is only for big disks", "GPT works on small disks too. It is chosen for UEFI booting as well as for size."),
        MISTAKE("Converting a disk without a backup", "Switching partition style often removes the partitions. Back up first."),
        MISTAKE("Mixing decimal TB and binary TiB", "The MBR limit is 2 TiB, about 2.2 TB. A disk marked 2 TB fits; one marked 3 TB does not."),
        QUIZ("What is the largest disk size an MBR table can describe with 512-byte sectors?",
             ["2 GiB", "2 TiB", "128 TiB", "8 ZiB"], 1,
             "2 to the power 32 sectors multiplied by 512 bytes gives 2 TiB.",
             hint="Multiply the number of possible sector numbers by the sector size.",
             feedback=["That is 1000 times too small: 2 to the 32 sectors is billions, not millions.", "",
                       "128 is the default number of GPT partitions, not a size.",
                       "That is the GPT limit with 512-byte sectors, not the MBR limit."]),
        QUIZ("Which is a benefit of GPT compared with MBR?",
             ["Only four partitions are allowed", "A backup copy of the table is kept at the end of the disk", "It uses a 32-bit sector address", "It cannot be used with UEFI"], 1,
             "GPT stores a backup table and uses checksums so damage to the table can be detected and repaired.",
             feedback=["Four primary partitions is an MBR limit.", "", "A 32-bit address is the MBR design.", "GPT is the normal partition style for UEFI."]),
        H("Practice questions"),
        PQ("Calculate the maximum size, in bytes, that an MBR can address with 512-byte sectors and 32-bit sector numbers.",
           "2^32 x 512 = 4 294 967 296 x 512 = 2 199 023 255 552 bytes (2 TiB)."),
        PQ("Give three advantages of GPT over MBR.",
           "Any three: much larger disks; 128 partitions by default instead of four primary; backup copy of the table; checksums to detect damage; "
           "needed to boot Windows in UEFI mode."),
        PQ("Explain why a 3 TB disk cannot be fully used when initialised as MBR.",
           "MBR stores sector numbers in 32 bits, so with 512-byte sectors it can address only 2 TiB (about 2.2 TB). The remaining space has no address in the table and is unusable."),
        PQ("What is the purpose of the EFI system partition and the protective MBR on a GPT disk?",
           "The EFI system partition holds the boot loader files that UEFI firmware loads. The protective MBR in the first sector shows one partition covering the disk, "
           "so old tools that only know MBR do not treat the disk as empty and overwrite it."),
        SUM("A partition table records where each partition starts and its size.",
            "MBR: 32-bit sector numbers, 2 TiB limit with 512-byte sectors, four primary partitions.",
            "GPT: 64-bit numbers, 128 partitions by default, backup table and checksums.",
            "Use GPT for UEFI booting and disks larger than 2 TiB; MBR suits legacy BIOS on small disks.",
            "Back up before changing the partition style."),
    ]))

LESSONS.append(lesson(
    module=HW, topic="OS deployment",
    title="File systems compared: FAT32, exFAT, NTFS and ext4",
    slug="ic6-file-systems-ntfs-ext4", minutes=22,
    summary="Explain what a file system does, compare FAT32, exFAT, NTFS and ext4 on limits, security and journaling, and calculate wasted space from cluster size.",
    objectives=[
        "Explain the role of a file system and the terms cluster, journal and permission",
        "Compare FAT32, exFAT, NTFS and ext4 for a stated job",
        "Calculate the space used by files for a given cluster size and the slack wasted",
        "Choose a file system for a USB stick, a Windows disk and a Linux server",
    ],
    key_concepts=["File system", "Cluster", "Slack space", "Journaling", "Permissions", "FAT32", "exFAT", "NTFS", "ext4"],
    blocks=[
        H("Introduction"),
        T("A video editor in Douala copies a 6 GB film from his laptop to a flash drive to give to a client. The copy stops with "
          "an error halfway, although the drive has 32 GB free. The drive is formatted as FAT32, which cannot hold a single file "
          "of 4 GiB or more. Formatting the drive with a different file system solves the problem."),
        H("What a file system is"),
        D("A **file system** is the method an operating system uses to name, store, find and protect files on a storage device. "
          "It keeps an index of which parts of the disk belong to which file, the file names, sizes, dates and, in some systems, "
          "the owner and permissions.", title="Definition"),
        D("A **cluster** (or block) is the smallest unit of disk space the file system gives to a file. A file always uses a "
          "whole number of clusters. The unused part of the last cluster is **slack space**.", title="Definition"),
        D("A **journal** is a log in which the file system records its planned changes before it makes them. After a crash or power cut, "
          "the system reads the journal and either completes or cancels the unfinished changes, so the file system stays consistent.", title="Definition"),
        H("The four main file systems"),
        KEY("Comparison", "Limits and features are quoted for common versions.", cards=[
            ["FAT32", "Works on almost every device. Maximum file size is just under 4 GiB. No permissions and no journal. Used on small USB sticks, cameras and boot partitions."],
            ["exFAT", "Designed for flash drives and cards. Very large files allowed. No journal and almost no security features. Good for moving big files between PCs, phones and cameras."],
            ["NTFS", "The Windows system disk format. Journaling, file permissions (ACLs), compression, encryption and very large files and volumes."],
            ["ext4", "The common Linux file system. Journaling, Unix permissions (owner, group, others), large files and volumes, and fast fault recovery."],
        ]),
        CODE("""
Feature              FAT32        exFAT        NTFS         ext4
Max single file      4 GiB - 1B   very large   very large   16 TiB (4 KiB blocks)
Journal              no           no           yes          yes
File permissions     no           no           yes          yes (owner/group/others)
Typical use          small USB    flash/cards  Windows disk Linux disk
""", "text", title="Table 1", caption="A summary of limits and features (standard figures; check the tool for your version)"),
        H("Cluster size and wasted space"),
        T("If a file needs 4097 bytes and the cluster is 4096 bytes, it uses two clusters, which is 8192 bytes. Almost a whole "
          "cluster is wasted. A bigger cluster size makes the disk faster for large files but wastes more space for many small files."),
        F(r"\text{space used} = \lceil \text{file size} \div \text{cluster size} \rceil \times \text{cluster size}", title="Space used by one file"),
        EX("Worked example 1: slack for three files", intro=(
            "The cluster size is 4096 bytes. Find the space used and the slack for files of 100 bytes, 4097 bytes and 10 000 bytes."), steps=[
            S("File of 100 bytes", math=r"1 \text{ cluster} = 4096 \text{ bytes};\ \text{slack} = 4096 - 100 = 3996"),
            S("File of 4097 bytes", math=r"2 \text{ clusters} = 8192 \text{ bytes};\ \text{slack} = 8192 - 4097 = 4095"),
            S("File of 10 000 bytes", math=r"\lceil 10000 \div 4096 \rceil = 3 \text{ clusters} = 12\,288 \text{ bytes};\ \text{slack} = 2288"),
            S("Total slack", math=r"3996 + 4095 + 2288 = 10\,379 \text{ bytes}"),
        ]),
        EX("Worked example 2: the effect of cluster size", intro=(
            "A folder holds 100 files of 1 KB each (1024 bytes). Compare the space used with a 4 KB cluster and a 32 KB cluster."), steps=[
            S("4 KB cluster", math=r"100 \times 4 = 400 \text{ KB used;}\ \text{wasted} = 400 - 100 = 300 \text{ KB}"),
            S("32 KB cluster", math=r"100 \times 32 = 3200 \text{ KB used;}\ \text{wasted} = 3200 - 100 = 3100 \text{ KB}"),
            S("Conclusion", text="Each tiny file takes a whole cluster, so large clusters waste a lot with many small files. They suit a disk that stores a few large files."),
        ]),
        H("Journaling"),
        T("Suppose power fails while a file is being saved. Without a journal, the index and the data may disagree, and the "
          "disk must be checked in full at the next start. This can take a long time on a big disk. With a journal, the system "
          "replays the log and fixes only the last few changes in seconds. This is important in places with frequent power cuts."),
        EX("Worked example 3: choose the file system", intro=(
            "Choose a file system for each: (a) a flash drive for moving 6 GB video files between Windows and a Mac, (b) a Windows "
            "10 system disk that needs per-user folder permissions, (c) a Linux web server."), steps=[
            S("Case a", text="FAT32 cannot hold files of 4 GiB or more. exFAT supports large files and works on both systems. Choose exFAT."),
            S("Case b", text="Permissions and a journal are needed. Choose NTFS."),
            S("Case c", text="Choose ext4: journaling, Unix permissions and the standard Linux support."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying FAT32 cannot hold a 4 GB drive", "The limit is on a single file (under 4 GiB). FAT32 can be used on larger volumes; only each file is limited."),
        MISTAKE("Forgetting the slack in the last cluster", "A file always takes whole clusters. Round the number of clusters up, not to the nearest."),
        MISTAKE("Believing a journal protects against every loss", "A journal keeps the file system consistent after a crash. It does not recover deleted files or replace backups."),
        QUIZ("A 5 GB file cannot be copied to a USB stick. Which file system is the stick most likely using?",
             ["NTFS", "ext4", "FAT32", "exFAT"], 2,
             "FAT32 cannot store a single file of 4 GiB or more.",
             feedback=["NTFS supports very large files.", "ext4 supports files up to 16 TiB.", "",
                       "exFAT allows very large files."]),
        QUIZ("A file of 6000 bytes is stored with a cluster size of 4096 bytes. How much space is wasted?",
             ["0 bytes", "2192 bytes", "4096 bytes", "6000 bytes"], 1,
             "6000 bytes need 2 clusters = 8192 bytes. Slack = 8192 - 6000 = 2192 bytes.",
             hint="Round the number of clusters up first.",
             feedback=["The file is not an exact multiple of the cluster size, so some space is wasted.", "",
                       "That would be a whole cluster; only the unused part of the last cluster is wasted.",
                       "That is the size of the file, not the waste."]),
        H("Practice questions"),
        PQ("State what a journal is and why it helps after a power cut.",
           "A journal is a log in which the file system records planned changes before making them. After a power cut, the system reads the journal and completes or cancels the "
           "unfinished changes, so the file system stays consistent and does not need a long full check."),
        PQ("Calculate the space used and the slack for a file of 9000 bytes with a cluster size of 4096 bytes.",
           "9000 / 4096 = 2.2, rounded up to 3 clusters. Space used = 3 x 4096 = 12 288 bytes. Slack = 12 288 - 9000 = 3288 bytes."),
        PQ("Give two features NTFS has that FAT32 does not, and say why they matter in a school with shared computers.",
           "NTFS has file permissions, journaling, encryption and compression, and supports very large files. Permissions let teachers' folders be protected from students; "
           "journaling lowers the chance of corrupted files after power cuts."),
        PQ("A technician formats a 64 GB flash drive that will carry 8 GB video files between Windows and Linux PCs. Recommend a file system with a reason.",
           "exFAT. It supports files larger than 4 GiB, unlike FAT32, and is widely readable on Windows, Linux and phones. NTFS and ext4 are less portable, "
           "and the journal and permissions are not needed for a transfer drive."),
        SUM("A file system names, locates and protects files; files use whole clusters, and the unused part of the last cluster is slack.",
            "FAT32 has a 4 GiB file limit and no security; exFAT suits big files on flash drives.",
            "NTFS (Windows) and ext4 (Linux) provide journaling and permissions.",
            "Larger clusters waste more space for many small files.",
            "A journal keeps the file system consistent after crashes; it is not a backup."),
    ]))

LESSONS.append(lesson(
    module=HW, topic="OS deployment",
    title="Installing an operating system by USB or network, and deploying many PCs",
    slug="ic6-install-os-usb-network", minutes=24,
    summary="Prepare bootable media, install Windows or Linux step by step, plan a dual-boot disk, and compare manual installation with imaging and network deployment for many PCs.",
    objectives=[
        "Prepare and use bootable USB installation media",
        "Describe the main installation steps and the post-installation checklist",
        "Plan a dual-boot disk and explain the install order",
        "Compare manual, image-based and network (PXE) deployment for a computer room",
    ],
    key_concepts=["Bootable media", "ISO image", "Clean install", "Dual boot", "Boot loader", "Disk image", "PXE", "Unattended installation"],
    blocks=[
        H("Introduction"),
        T("A school in Garoua receives thirty second-hand computers from a donor. Each must be given a fresh operating system "
          "before students can use it. Doing this by hand, one at a time, takes days. Technicians use installation media for a "
          "single PC and images or network deployment for a whole room."),
        H("Installation media"),
        D("An **ISO image** is a single file that holds an exact copy of an installation disc. **Bootable media** is a USB stick "
          "(or disc) prepared so that firmware can start the installer from it. A tool copies the ISO to the stick and makes it bootable. "
          "Simply copying the ISO file onto the stick as an ordinary file is not enough.", title="Definition"),
        KEY("Before you begin", "Do these first.", cards=[
            ["Back up", "Copy the user's documents, photos and licence keys to another drive. A clean install erases the target partition."],
            ["Check requirements", "Does the PC meet the minimum RAM, disk space and CPU for the system? Is it 64-bit?"],
            ["Get the media", "Download the ISO only from the official site. Check its checksum, if given, to be sure it is not damaged or changed."],
            ["Know the boot mode", "UEFI and GPT, or legacy BIOS and MBR. The installer follows the mode in which it was started."],
        ]),
        H("The installation steps"),
        EX("Worked example 1: a clean installation from USB", intro=(
            "Install an operating system on one donated PC in the Garoua school, wiping the old system."), steps=[
            S("Boot from the stick", text="Insert it, restart, open the one-time boot menu or set the USB device first in setup."),
            S("Choose language and edition", text="Select the language, keyboard and the edition that the licence allows."),
            S("Choose a clean (custom) install", text="Do not choose upgrade if the old system is damaged or you want a fresh start."),
            S("Partition the disk", text="Delete old partitions or select the unallocated space. The installer creates the needed partitions, such as the EFI system partition on UEFI. Choose NTFS for Windows or ext4 for Linux."),
            S("Copy files and restart", text="The installer copies files, then restarts. Remove the stick when asked, so the PC starts from the new system."),
            S("Create the first account", text="Set the computer name, an administrator account with a strong password and a standard account for daily use."),
        ]),
        T("After the installation, a technician follows a checklist: install the hardware drivers (especially network and "
          "graphics), run system updates, install antivirus and the office programs, set the date and time, create restore "
          "points or a backup image, and test printing and internet. Then reset the boot order so the PC starts from the disk."),
        H("Dual boot"),
        D("**Dual boot** means two operating systems installed on the same PC. A **boot loader** shows a menu at start-up where "
          "the user chooses which system to run. Each system needs its own partition.", title="Definition"),
        T("The usual advice is to install Windows first and Linux second. The Linux installer detects Windows and adds it to its "
          "menu. If Windows is installed second, it replaces the boot loader and Linux no longer appears until the loader is repaired."),
        EX("Worked example 2: plan a dual-boot disk", intro=(
            "A 500 GB disk is to hold Windows (200 GB), Linux (root 100 GB, swap 8 GB) and a shared data partition using the rest. "
            "Ignore the small EFI partition. Find the size of the shared partition and name the file systems."), steps=[
            S("Add the planned partitions", math=r"200 + 100 + 8 = 308 \text{ GB}"),
            S("Find the remainder", math=r"500 - 308 = 192 \text{ GB}"),
            S("Choose file systems", text="Windows partition: NTFS. Linux root: ext4. Swap: swap format. Shared data: exFAT or NTFS, both readable from Windows and Linux."),
            S("Order", text="Install Windows first, then Linux, so the Linux boot loader offers both."),
        ]),
        H("Deploying many PCs"),
        KEY("Three methods", "The choice depends on the number of PCs.", cards=[
            ["Manual installation", "Repeat the full installation on every PC. Simple for one or two machines but slow and uneven."],
            ["Disk imaging", "Build one PC with the system and programs, capture its disk as an image, and copy that image to the other PCs with the same or similar hardware."],
            ["Network deployment (PXE)", "PCs boot over the network using PXE and pull the installer or image from a server. No USB sticks are needed, and many PCs can be done at once."],
        ]),
        T("An **unattended installation** uses an answer file so the installer asks no questions. It is used with network deployment so that "
          "every PC is set up in the same way. Images should be updated regularly, as old ones lack recent updates."),
        EX("Worked example 3: compare the time", intro=(
            "The school has 30 PCs. A manual installation takes 45 minutes per PC, one PC at a time. Network imaging takes "
            "15 minutes per batch of 10 PCs. These are example figures, not measurements. Compare the total times."), steps=[
            S("Manual", math=r"30 \times 45 = 1350 \text{ minutes} = 22.5 \text{ hours}"),
            S("Imaging", math=r"30 \div 10 = 3 \text{ batches};\ 3 \times 15 = 45 \text{ minutes}"),
            S("Compare", math=r"1350 \div 45 = 30", text="Imaging is 30 times faster here, and every PC gets exactly the same set-up."),
            S("Add the cost of preparation", text="Building the master image and the server also takes time, so the saving is greatest for many identical PCs."),
        ]),
        H("Common mistakes"),
        MISTAKE("Copying the ISO file onto the USB stick like a document", "The stick must be made bootable by a tool, or the firmware cannot start the installer."),
        MISTAKE("Installing without a backup", "A clean install erases the chosen partition. Back up first and check the backup opens."),
        MISTAKE("Installing Windows second in a dual boot", "Windows replaces the boot loader and hides the Linux system. Install Windows first."),
        QUIZ("Which method is best for setting up 200 identical PCs in a university lab?",
             ["Installing from a disc on each PC", "Network deployment with an image and an answer file", "Copying the ISO file to each desktop", "Asking each student to install their own"], 1,
             "A network deployment installs many PCs at once from one image, so they all have the same setup.",
             feedback=["It is slow and gives different results on every PC.", "",
                       "An ISO file on the desktop does not install anything.",
                       "Students would give different set-ups, with mistakes and licence problems."]),
        QUIZ("Why is a checksum often given with an ISO download?",
             ["To make the download faster", "To check that the file is complete and unchanged", "To decrypt the ISO", "To make the stick bootable"], 1,
             "A checksum is a short value calculated from the file. If your own calculation matches, the file was not damaged or changed.",
             feedback=["The checksum does not affect speed.", "", "ISO files are not encrypted by the checksum.",
                       "A special tool is used to make a stick bootable."]),
        H("Practice questions"),
        PQ("State four steps taken after installing an operating system, before giving the PC to a user.",
           "Install drivers; run system updates; install antivirus and required programs; set the date and time; create the user accounts; test the network and printing; "
           "set boot order back to the disk; make a backup image. Any four."),
        PQ("Explain why Windows should be installed before Linux on a dual-boot PC.",
           "Windows installation replaces the boot loader and shows only Windows. The Linux installer detects existing systems and adds them to its menu, so both appear."),
        PQ("Describe how disk imaging helps a technician set up 20 identical PCs.",
           "One PC is set up with the operating system, programs and settings, and its disk is saved as an image. The image is copied to the other PCs, which saves the time of "
           "installing each one and gives identical configuration. It works best when the hardware is the same or similar."),
        PQ("A disk of 1000 GB is divided into Windows 250 GB, Linux root 120 GB, swap 16 GB and a shared partition. Find the size of the shared partition.",
           "250 + 120 + 16 = 386 GB used. 1000 - 386 = 614 GB for the shared partition."),
        SUM("Bootable media must be made with a tool; back up and check the boot mode before installing.",
            "Steps: boot from media, choose clean install, partition, copy, create accounts, then drivers, updates and testing.",
            "Dual boot: Windows first, Linux second, separate partitions and a boot loader menu.",
            "For many PCs use imaging or PXE network deployment with answer files.",
            "Always keep the original media, a backup and a record of the settings."),
    ]))

LESSONS.append(lesson(
    module=HW, topic="OS deployment",
    title="Virtual machines: hypervisors, resources and snapshots",
    slug="ic6-virtual-machines", minutes=22,
    summary="Explain how a hypervisor runs guest systems on one host, share RAM, CPU and disk between virtual machines by calculation, and use snapshots and network modes sensibly.",
    objectives=[
        "Define virtual machine, host, guest and hypervisor, and compare type 1 and type 2 hypervisors",
        "Allocate RAM and disk to virtual machines without starving the host",
        "Explain snapshots, dynamic and fixed virtual disks, and NAT and bridged networking",
        "State the benefits and limits of virtualization for a school or small business",
    ],
    key_concepts=["Virtual machine", "Hypervisor", "Host", "Guest", "Snapshot", "Virtual disk", "NAT", "Bridged network"],
    blocks=[
        H("Introduction"),
        T("A teacher in Ngaoundere wants his students to practise installing Linux, but he does not want them to erase the school "
          "PCs. A virtual machine lets each student install and break a whole operating system inside a window, and then simply "
          "delete it. The real computer stays untouched."),
        H("Key terms"),
        D("A **virtual machine (VM)** is a software-made computer that has its own virtual CPU, memory, disk and network adapter, "
          "and runs its own operating system. The real computer is the **host**; the system inside the VM is the **guest**. The program "
          "that creates and runs VMs is the **hypervisor**.", title="Definition"),
        KEY("Two kinds of hypervisor", "The difference is what runs underneath.", cards=[
            ["Type 1 (bare metal)", "Runs directly on the hardware with no ordinary operating system under it. Used on servers because it is efficient and manages many VMs."],
            ["Type 2 (hosted)", "Runs as a program inside a normal host operating system such as Windows or Linux. Used on desktops and laptops for learning and testing."],
        ]),
        T("Virtual machines depend on CPU support for virtualization, which must be switched on in the firmware setup on many PCs. "
          "The host shares its CPU, RAM and disk among the VMs, so the total given to VMs must always leave enough for the host."),
        H("Sharing resources"),
        EX("Worked example 1: how many VMs can the host run?", intro=(
            "A lab PC has 16 GB RAM and 300 GB of free disk. The host operating system needs 4 GB RAM to stay responsive. Each VM is "
            "given 2 GB RAM and a fixed 40 GB virtual disk. How many VMs can run at once?"), steps=[
            S("RAM left for VMs", math=r"16 - 4 = 12 \text{ GB}"),
            S("VMs allowed by RAM", math=r"12 \div 2 = 6"),
            S("VMs allowed by disk", math=r"300 \div 40 = 7.5 \rightarrow 7"),
            S("Take the smaller", text="RAM allows 6 and disk allows 7, so the answer is 6 VMs. RAM is the limit."),
        ]),
        T("CPU is shared differently. A host with 8 logical cores can give each of several VMs 2 virtual cores. The hypervisor schedules "
          "them over the real cores, so more virtual cores than real cores can be defined (this is called over-commitment), but when "
          "all VMs are busy they slow down. RAM is usually the first hard limit."),
        H("Virtual disks and snapshots"),
        D("A **virtual disk** is a file on the host that the guest sees as a hard disk. A **fixed** disk reserves its full size at "
          "once. A **dynamic** disk starts small and grows as the guest writes data, up to its maximum size.", title="Definition"),
        D("A **snapshot** records the state of a VM at one moment, so that you can return to it later. It is quick to take and quick "
          "to restore, but it is not a backup: it is stored with the VM and grows as changes are made.", title="Definition"),
        EX("Worked example 2: using a snapshot in a lesson", intro=(
            "A student will test a risky configuration change in a Linux VM. Explain how a snapshot protects the work."), steps=[
            S("Before the change", text="Shut down or pause the VM at a stable point and take a snapshot, called, for example, before network change."),
            S("Make the change", text="Edit the configuration. The service stops working."),
            S("Restore", text="Restore the snapshot. The VM returns to the exact state when it was taken, and the failed change disappears."),
            S("Housekeeping", text="Delete old snapshots when they are no longer needed, because they take disk space and slow the VM."),
        ]),
        H("Networking modes"),
        KEY("Two common modes", "The choice decides who can reach the VM.", cards=[
            ["NAT", "The VM shares the host's address and can reach the internet, but other computers on the network cannot start a connection to it. Safe and simple for testing."],
            ["Bridged", "The VM appears on the physical network as its own computer with its own address. Other computers can reach it, which suits a test server."],
        ]),
        EX("Worked example 3: should a school use virtualization?", intro=(
            "A small office in Kumba has one strong PC and wants a web server, a file server and a test system. Give two benefits "
            "and two limits of putting each on a VM."), steps=[
            S("Benefits", text="One machine is used for several roles, which saves money and electricity. Each VM is isolated, so a fault in the test system does not stop the file server."),
            S("Easy management", text="A VM can be copied to another host as a file, and snapshots allow quick rollback."),
            S("Limits: shared resources", text="All VMs share one host's RAM, CPU and disk. If the host fails, every VM stops. A strong host and a backup plan are needed."),
            S("Limits: skills and licences", text="Staff need training and each guest operating system may need its own licence."),
        ]),
        H("Common mistakes"),
        MISTAKE("Giving all RAM to the VMs", "The host needs memory too. If the host runs out, everything becomes slow or crashes."),
        MISTAKE("Using a snapshot as a backup", "A snapshot lives with the VM on the same disk. If the disk fails, both are lost."),
        MISTAKE("Forgetting to enable virtualization support", "Hypervisors may report that virtualization is not available until it is enabled in UEFI/BIOS."),
        QUIZ("What does a hypervisor do?",
             ["It increases the screen resolution of the guest", "It creates and runs virtual machines and shares host resources among them", "It repairs damaged hard disks", "It connects the PC to the internet"], 1,
             "A hypervisor is the software that creates, runs and manages virtual machines on a host.",
             feedback=["Resolution is a display setting.", "", "Disk repair is done by file system tools.", "The network adapter and router give the internet connection."]),
        QUIZ("A host has 8 GB RAM, reserves 2 GB for itself, and each VM needs 1.5 GB. How many VMs can run?",
             ["3", "4", "5", "6"], 1,
             "8 - 2 = 6 GB for VMs. 6 / 1.5 = 4 VMs.",
             hint="Subtract the host's share first.",
             feedback=["That uses only 4.5 GB; there is room for another.", "", "5 VMs need 7.5 GB, but only 6 GB is available.", "Six VMs would need 9 GB, more than the 6 GB available."]),
        H("Practice questions"),
        PQ("Distinguish between a type 1 and a type 2 hypervisor.",
           "A type 1 hypervisor runs directly on the hardware, without a normal host operating system, and is used on servers. A type 2 hypervisor is an ordinary program that "
           "runs inside a host operating system, and is used on desktops and laptops."),
        PQ("A host has 32 GB RAM and 500 GB of free disk. It keeps 8 GB for itself. Each VM uses 4 GB RAM and a 50 GB fixed disk. Find the maximum number of VMs.",
           "RAM: (32 - 8) / 4 = 6. Disk: 500 / 50 = 10. The smaller is 6, so at most 6 VMs."),
        PQ("Explain why a snapshot is not a replacement for a backup.",
           "A snapshot is stored with the VM on the same storage. If the disk fails or the VM files are deleted or infected, the snapshot is lost too. A backup is a separate copy kept on other storage."),
        PQ("Give three benefits of using virtual machines in a school ICT lab.",
           "Any three: students can practise installing systems without risk to the real PC; several operating systems on one PC; easy reset with snapshots; "
           "saves hardware cost; isolated from the host so malware testing is safer; VMs can be copied between PCs as files."),
        SUM("A hypervisor runs guest VMs on a host; type 1 runs on hardware, type 2 inside an operating system.",
            "Total VM resources must leave enough for the host. RAM is often the limit; take the smaller of the RAM and disk limits.",
            "Snapshots give quick rollback but are not backups.",
            "NAT is simple and protected; bridged makes the VM visible on the network.",
            "Enable CPU virtualization support in firmware before using a hypervisor."),
    ]))

# ===========================================================================
# Business technologies
# ===========================================================================
LESSONS.append(lesson(
    module=ENT, topic="Business technologies",
    title="E-commerce: B2C and B2B models, payments and delivery",
    slug="ic6-ecommerce-b2b-b2c", minutes=22,
    summary="Classify business-to-consumer and business-to-business e-commerce, follow an online order from basket to delivery, compare payment methods and calculate the net income of an online sale.",
    objectives=[
        "Define e-commerce and distinguish B2C, B2B and C2C models with examples",
        "Describe the stages of an online order and the technology used at each stage",
        "Compare payment methods used in Cameroon on cost, trust and reach",
        "Calculate gross and net income from an online shop, and name benefits, risks and controls",
    ],
    key_concepts=["E-commerce", "B2C", "B2B", "C2C", "Payment gateway", "Mobile money", "Cash on delivery", "Order fulfilment"],
    blocks=[
        H("Introduction"),
        T("A woman in Bafoussam sells traditional Ndop fabric from a small shop. Customers in Douala, Yaounde and abroad see her "
          "photos on social media and ask to buy. When she builds a simple online shop with prices, a basket and a way to pay "
          "by mobile money, she turns a local shop into an e-commerce business. The goods are still physical. What has moved online is the buying and paying."),
        H("Models of e-commerce"),
        D("**E-commerce** is the buying and selling of goods and services over the internet or other computer networks, "
          "including the ordering, payment and the sending of information that goes with them.", title="Definition"),
        KEY("Who sells to whom", "The model is named by the two sides of the trade.", cards=[
            ["B2C (business to consumer)", "A business sells to the public. Example: an online shop selling clothes to individuals, or a ticket website for a bus company."],
            ["B2B (business to business)", "A business sells to another business. Example: a wholesaler selling cartons of soap to market retailers, or a supplier selling raw materials to a factory. Orders are larger, prices may be negotiated and invoices with credit terms are common."],
            ["C2C (consumer to consumer)", "Individuals sell to each other through a platform. Example: a classifieds site or social-media marketplace for second-hand phones."],
        ]),
        CODE("""
Feature              B2C                          B2B
Customer             Individual                   Another business
Order size           Small                        Large, repeated
Price                Fixed, public                Often negotiated, bulk discounts
Payment              Mobile money, card, cash     Bank transfer, invoice with credit terms
Decision             Quick, emotional             Slower, several people, contract
""", "text", title="Table 1", caption="B2C compared with B2B"),
        H("Stages of an online order"),
        T("An online order passes through several stages, and each uses a technology. The customer browses a catalogue stored in "
          "a database and fills a basket. At checkout the customer enters delivery details and chooses a payment method. A "
          "**payment gateway** (the service that securely passes payment details between the shop, the customer's account and the "
          "bank or mobile money operator) confirms the payment. The shop sends a confirmation message, the store prepares the "
          "goods, a courier delivers them, and the system records the sale and updates stock."),
        D("**Order fulfilment** is everything that happens after the customer pays: picking and packing the items, delivery, "
          "handling returns and updating stock and accounting records.", title="Definition"),
        H("Payment methods"),
        CODE("""
Method              Strength                          Weakness
Mobile money        Widely used, no bank card needed  Transaction fee; network outages
Bank card           Works across borders              Few customers hold cards; card fraud risk
Cash on delivery    Builds trust for new shops        Courier handles cash; refusals at the door
Bank transfer (B2B) Good for large amounts            Slower; needs bank details
""", "text", title="Table 2", caption="Payment methods compared"),
        EX("Worked example 1: net income of an online shop", intro=(
            "An online shop in Douala sells 40 orders a day, each worth 12 500 FCFA on average. Mobile money charges the shop 1.5 percent "
            "of each payment. Delivery costs the shop 1000 FCFA per order. Find the net income per day before the cost of the goods. "
            "(The 1.5 percent is an assumed figure for practice.)"), steps=[
            S("Gross income", math=r"40 \times 12\,500 = 500\,000 \text{ FCFA}"),
            S("Payment fee", math=r"500\,000 \times 0.015 = 7500 \text{ FCFA}"),
            S("Delivery cost", math=r"40 \times 1000 = 40\,000 \text{ FCFA}"),
            S("Net income", math=r"500\,000 - 7500 - 40\,000 = 452\,500 \text{ FCFA}", text="This is before paying for the goods themselves and other costs."),
        ]),
        EX("Worked example 2: classify the transaction", intro=(
            "Classify each as B2C, B2B or C2C: (a) a bakery orders flour in bulk from a supplier through the supplier's website, "
            "(b) a student sells a used laptop through a classifieds site, (c) a family orders a pizza from a restaurant's app."), steps=[
            S("Case a", text="Both sides are businesses. B2B."),
            S("Case b", text="Two individuals, with the site as a platform. C2C."),
            S("Case c", text="A business sells to individuals. B2C."),
        ]),
        EX("Worked example 3: choose payment options", intro=(
            "A new online shop in Limbe sells phone accessories to young customers, many of whom have no bank card. Recommend payment options and explain."), steps=[
            S("Main option", text="Mobile money, because most customers already have it and it needs no bank card."),
            S("Trust option", text="Cash on delivery for the first orders, so that hesitant customers can inspect the goods first."),
            S("Control the risk", text="Confirm orders by phone, and require mobile money pre-payment for large orders to limit refusals at the door."),
            S("Records", text="Record every payment reference in the system for reconciliation with the mobile money statement."),
        ]),
        H("Benefits, risks and controls"),
        KEY("Weighing e-commerce", "", cards=[
            ["Benefits", "Wider market beyond the town; open at all hours; lower rent and staff costs; customer data helps marketing; faster ordering for B2B."],
            ["Risks", "Fraud and fake orders; weak internet and power; delivery delays; returns; customers worried about security; competition from larger sites."],
            ["Controls", "Encrypted pages (HTTPS); trusted payment gateways; verification of orders; clear return policy; backups; reliable couriers; compliance with consumer and data protection law."],
        ]),
        H("Common mistakes"),
        MISTAKE("Calling every website a B2C site", "The model depends on who buys. A supplier's portal for shops is B2B even though it is a website."),
        MISTAKE("Counting gross income as profit", "Fees, delivery, goods, rent and tax must be subtracted. Gross income is only the total of the sales."),
        MISTAKE("Ignoring after-sale work", "Delivery, returns and stock updates are part of e-commerce, and poor fulfilment loses customers."),
        QUIZ("A hotel orders 200 kg of rice from a wholesaler through the wholesaler's website. Which model is this?",
             ["B2C", "B2B", "C2C", "Not e-commerce"], 1,
             "Both the buyer and the seller are businesses, and the order is placed online.",
             feedback=["The buyer is a hotel (a business), not an individual consumer.", "",
                       "Neither side is an individual selling to another individual.", "Buying and selling over a network is e-commerce."]),
        QUIZ("What does a payment gateway do?",
             ["It designs the shop's web pages", "It passes payment details securely between the shop, the customer and the payment provider", "It delivers the goods", "It stores the shop's stock list"], 1,
             "The gateway confirms and processes online payments safely.",
             feedback=["Page design is done with HTML, CSS and design tools.", "", "A courier delivers goods.", "Stock is stored in the shop's database."]),
        H("Practice questions"),
        PQ("Distinguish between B2C and B2B e-commerce and give one Cameroonian example of each.",
           "B2C: a business sells to individual consumers, for example an online shop selling clothes to customers in Douala. B2B: a business sells to another business, "
           "for example a wholesaler selling cartons of soap to market traders through an ordering website. B2B orders are usually larger and may use credit terms."),
        PQ("List four stages between a customer filling a basket and receiving the goods.",
           "Checkout with delivery details; payment through a gateway or mobile money; confirmation to the customer; picking and packing; delivery; update of stock and records. Any four in order."),
        PQ("An online shop sells 25 items a day at 8000 FCFA each. The payment fee is 2 percent. Delivery costs 1500 FCFA per order. Find the daily income after fees and delivery.",
           "Gross = 25 x 8000 = 200 000 FCFA. Fee = 0.02 x 200 000 = 4000 FCFA. Delivery = 25 x 1500 = 37 500 FCFA. Net = 200 000 - 4000 - 37 500 = 158 500 FCFA (before goods cost)."),
        PQ("Give two risks of e-commerce for a small business and a control for each.",
           "Fraud or fake orders: confirm orders by phone and use a trusted payment gateway. Customer data theft: use HTTPS and protect stored data with access controls and backups. "
           "Other answers: delivery delays (reliable courier, clear time), weak connection (offline order taking)."),
        SUM("E-commerce is trade over networks: B2C sells to consumers, B2B to businesses, C2C between individuals.",
            "An order moves from catalogue to basket, payment through a gateway, fulfilment and records.",
            "Mobile money is widely used; cash on delivery builds trust but has risks.",
            "Gross income minus fees, delivery and other costs gives net income.",
            "Controls: encryption, trusted gateways, verification, backups and fulfilment quality."),
    ]))

LESSONS.append(lesson(
    module=ENT, topic="Business technologies",
    title="Virtual private networks (VPNs): tunnels, encryption and uses",
    slug="ic6-vpn-tunnels", minutes=22,
    summary="Explain how a VPN uses tunnelling and encryption to protect data over the internet, compare remote-access and site-to-site VPNs, and judge what a VPN does and does not protect.",
    objectives=[
        "Define a VPN and explain tunnelling and encapsulation",
        "Explain how encryption and authentication protect data in a VPN",
        "Choose between a remote-access and a site-to-site VPN for a business case",
        "State the limits of VPNs and calculate the overhead added to packets",
    ],
    key_concepts=["VPN", "Tunnelling", "Encapsulation", "Encryption", "Authentication", "Remote-access VPN", "Site-to-site VPN", "Overhead"],
    blocks=[
        H("Introduction"),
        T("A company has its head office in Douala and a branch in Yaounde. The branch needs to reach the accounting server in "
          "Douala. Renting a private line between the two towns is expensive. Sending the data over the public internet is cheap "
          "but anyone along the route could read it. A **virtual private network** gives a middle way: a private connection built over a public network."),
        H("What a VPN is"),
        D("A **VPN** (virtual private network) is a secure, encrypted connection between two points over a public network such as the "
          "internet. To the users it behaves as if the two networks, or a user and a network, were on the same private network.", title="Definition"),
        D("**Tunnelling** places each original packet inside another packet (**encapsulation**) so that it can cross the public network. "
          "At the far end, the outer packet is removed (decapsulation) to reveal the original. In a VPN the original packet is also "
          "**encrypted**, so the content and often the inner addresses are unreadable while in the tunnel.", title="Definition"),
        IMG("al-ic6-vpn-tunnel.svg", alt="A branch network and a head office network linked by an encrypted tunnel across the internet, with the inner packet wrapped inside an outer packet.",
            caption="Figure 1. A site-to-site VPN: the inner packet is wrapped and encrypted across the internet"),
        H("How security is provided"),
        KEY("Three protections", "", cards=[
            ["Encryption", "Data is scrambled with a key, so someone capturing the traffic sees unreadable data (confidentiality)."],
            ["Authentication", "Both ends prove who they are with passwords, certificates or keys, so a stranger cannot join the tunnel. Often a second factor is added for users."],
            ["Integrity", "Each packet carries a check that shows if it was changed on the way."],
        ]),
        T("Common VPN technologies include IPsec, and VPNs based on TLS (the same technology that protects secure websites). The principle is "
          "the same: authenticate, agree keys, then encrypt and encapsulate each packet."),
        H("Types of VPN"),
        KEY("Two main kinds", "", cards=[
            ["Remote-access VPN", "One user connects from a laptop or phone, in a hotel or at home, to the company network through VPN software. The user gets access to internal files and systems."],
            ["Site-to-site VPN", "Two whole networks, such as head office and branch, are joined by VPN devices (routers or firewalls) that are always connected. Users at either site notice nothing."],
        ]),
        EX("Worked example 1: choose the VPN type", intro=(
            "(a) A sales manager travels between towns and needs the order database. (b) A bank links its Douala and Bamenda offices all day. Choose the VPN type for each."), steps=[
            S("Case a", text="One mobile user connects from changing places. Remote-access VPN."),
            S("Case b", text="Two fixed offices need a permanent link for many users. Site-to-site VPN, set up on the office routers or firewalls."),
            S("Reason", text="Remote access needs software on each user device. Site-to-site hides the VPN from users inside the offices."),
        ]),
        EX("Worked example 2: what an eavesdropper sees", intro=(
            "An employee uses a cafe's open wireless network. Compare what an attacker on that network sees with and without a VPN while she opens the company intranet."), steps=[
            S("Without VPN", text="If the site does not use HTTPS, the attacker can read the pages and passwords. Even with HTTPS, the attacker sees which servers she contacts."),
            S("With VPN", text="All her traffic goes inside an encrypted tunnel to the company VPN server. The attacker sees only unreadable data going to one address, the VPN server."),
            S("Conclusion", text="The VPN protects against eavesdropping on the local network. It does not make her device clean of malware."),
        ]),
        H("Overhead and limits"),
        T("Encapsulation and encryption add extra bytes to every packet. This is the **overhead**. It uses a small part of the link and may "
          "reduce speed, especially on slow connections or devices with weak processors."),
        EX("Worked example 3: calculating overhead", intro=(
            "A VPN adds 60 bytes to each packet. A packet carries 1400 bytes of data. Find the size of the packet on the link and the overhead as a percentage of the packet. (60 bytes is an assumed figure.)"), steps=[
            S("Total size", math=r"1400 + 60 = 1460 \text{ bytes}"),
            S("Overhead share", math=r"\frac{60}{1460} \times 100 = 4.1\%"),
            S("Meaning", text="About 4 percent of the link is used by the tunnel. A link with 2 Mbps capacity gives the user about 96 percent of the speed, if nothing else slows it."),
        ]),
        KEY("What a VPN does not do", "", cards=[
            ["Not a cure for malware", "If the user's device is infected, the VPN carries the infection to the company network."],
            ["Not anonymous", "The VPN provider or company can see the traffic leaving the tunnel. A provider must be trusted."],
            ["Not a replacement for a firewall", "Users still need access rules, patches and strong passwords on the network behind the tunnel."],
        ]),
        H("Common mistakes"),
        MISTAKE("Saying a VPN makes you invisible", "It hides the content from the local network but the VPN endpoint sees it. It is for privacy on untrusted networks, not complete anonymity."),
        MISTAKE("Forgetting authentication", "Encryption without authentication could encrypt data to the wrong party. Both parts are needed."),
        MISTAKE("Confusing tunnelling with encryption", "Tunnelling wraps one packet in another so it can cross a network. Encryption makes the content unreadable. A VPN usually does both."),
        QUIZ("What is the purpose of encapsulation in a VPN?",
             ["To compress files", "To place the original packet inside another packet so it can cross the public network", "To remove viruses", "To increase the Wi-Fi range"], 1,
             "Encapsulation wraps the original packet inside an outer packet for travel through the tunnel.",
             feedback=["Compression is a different process.", "", "A VPN does not remove viruses.", "Wireless range is a radio matter."]),
        QUIZ("A company wants its two offices to be permanently joined so users do not need any software. Which is best?",
             ["Remote-access VPN", "Site-to-site VPN", "A USB stick", "A public wireless hotspot"], 1,
             "The routers or firewalls at each site keep the tunnel up for everyone.",
             feedback=["It needs client software on each user device and is for individuals.", "",
                       "A USB stick is not a network link.", "A public hotspot is not private or secure."]),
        H("Practice questions"),
        PQ("Explain what is meant by a tunnel in a VPN.",
           "A tunnel is a logical path across a public network in which each original packet is wrapped (encapsulated) inside another packet and is usually encrypted. "
           "It carries data between the two ends as though they were on a private link."),
        PQ("State three ways in which a VPN protects data sent over the internet.",
           "Encryption keeps the data confidential; authentication ensures both ends are who they claim to be; integrity checks show if packets were altered; "
           "the original addresses are hidden inside the tunnel."),
        PQ("A packet of 1200 bytes of data gains 50 bytes from the VPN. Calculate the overhead as a percentage of the total packet, to 1 decimal place.",
           "Total = 1250 bytes. 50 / 1250 x 100 = 4.0 percent."),
        PQ("Give two reasons why a VPN does not make a company network completely safe.",
           "An infected device can pass malware through the tunnel; stolen passwords or keys let an attacker authenticate; the VPN does not replace firewalls, patching and access control; "
           "the VPN server itself must be trusted and secured."),
        SUM("A VPN builds a private, encrypted connection over a public network using tunnelling.",
            "Encryption, authentication and integrity checks provide the protection.",
            "Remote-access VPN connects one user; site-to-site VPN joins two networks.",
            "Overhead from the extra headers reduces useful bandwidth slightly.",
            "A VPN does not remove malware or the need for other security controls."),
    ]))

LESSONS.append(lesson(
    module=ENT, topic="Business technologies",
    title="VoIP: how voice travels as packets, and how to size the bandwidth",
    slug="ic6-voip-bandwidth", minutes=22,
    summary="Describe how VoIP turns speech into packets, explain delay, jitter and packet loss, and calculate the bandwidth needed for calls with different codecs.",
    objectives=[
        "Explain how analogue speech becomes digital packets in VoIP",
        "Define latency, jitter and packet loss and state their effect on call quality",
        "Calculate the bandwidth of one call from codec rate, packet interval and header size",
        "Check whether a given internet link can carry a number of simultaneous calls",
    ],
    key_concepts=["VoIP", "Codec", "Packetization", "RTP", "Latency", "Jitter", "Packet loss", "QoS"],
    blocks=[
        H("Introduction"),
        T("A small firm in Douala pays a high bill for calls between its head office and its branch in Yaounde. Its manager asks "
          "if the calls could travel over the internet connection the offices already have. This is **VoIP**, voice over IP. It can "
          "save money, but only if the network is sized correctly, and a technician must be able to calculate how many calls a link can carry."),
        H("How VoIP works"),
        D("**VoIP** (Voice over Internet Protocol) sends speech as digital packets over an IP network instead of over a dedicated telephone circuit.", title="Definition"),
        KEY("Steps in a VoIP call", "", cards=[
            ["1. Digitise", "The microphone signal is sampled and converted to digital data."],
            ["2. Compress (codec)", "A **codec** (coder-decoder) compresses the voice data. Different codecs trade quality against bit rate."],
            ["3. Packetize", "The data is cut into small slices, for example every 20 ms, and each slice is put in a packet with headers."],
            ["4. Send", "Packets cross the network, usually using UDP with RTP headers that carry numbering and timing."],
            ["5. Rebuild", "The receiver places packets in order in a short buffer, decodes them and plays the sound."],
        ]),
        T("A call is set up and ended by a signalling protocol. A VoIP phone, a softphone on a laptop or a gateway to the normal phone network may take part. "
          "Calls between two VoIP users on the same network can be free of per-minute charges."),
        H("Quality problems"),
        KEY("Three enemies of a good call", "", cards=[
            ["Latency (delay)", "The time for speech to reach the other side. If one-way delay becomes large, people talk over each other."],
            ["Jitter", "Variation in the arrival time of packets. A buffer smooths small jitter but adds delay."],
            ["Packet loss", "Packets that never arrive. Lost slices make the voice choppy or silent for a moment."],
        ]),
        T("To protect calls, networks use **QoS (quality of service)**: rules that give voice packets priority over bulk downloads, "
          "and enough bandwidth set aside for calls. A busy shared link without QoS is a common cause of poor calls."),
        H("Calculating bandwidth"),
        T("The bandwidth of one call in one direction depends on the codec bit rate, the interval at which packets are sent, "
          "and the headers on each packet. For IPv4, UDP and RTP the headers add 20 + 8 + 12 = 40 bytes per packet. (Link-level headers add more; "
          "this lesson leaves them out.)"),
        F(r"\text{payload (bytes)} = \frac{\text{codec rate (bit/s)} \times \text{interval (s)}}{8}", title="Payload per packet"),
        F(r"\text{bandwidth (bit/s)} = (\text{payload} + 40) \times 8 \times \text{packets per second}", title="Bandwidth per call, one direction"),
        EX("Worked example 1: a 64 kbit/s codec", intro=(
            "A codec has a rate of 64 000 bit/s and sends a packet every 20 ms. Find the bandwidth of one call in one direction."), steps=[
            S("Payload per packet", math=r"\frac{64\,000 \times 0.02}{8} = 160 \text{ bytes}"),
            S("Packets per second", math=r"1 \div 0.02 = 50"),
            S("Bytes per packet with headers", math=r"160 + 40 = 200 \text{ bytes}"),
            S("Bandwidth", math=r"200 \times 8 \times 50 = 80\,000 \text{ bit/s} = 80 \text{ kbit/s}"),
        ]),
        EX("Worked example 2: a compressed codec", intro=(
            "A codec with a rate of 8000 bit/s also sends a packet every 20 ms. Find the bandwidth per call. Why is it more than the codec rate?"), steps=[
            S("Payload per packet", math=r"\frac{8000 \times 0.02}{8} = 20 \text{ bytes}"),
            S("With headers", math=r"20 + 40 = 60 \text{ bytes}"),
            S("Bandwidth", math=r"60 \times 8 \times 50 = 24\,000 \text{ bit/s} = 24 \text{ kbit/s}"),
            S("Why larger", text="The 40 bytes of headers are bigger than the 20-byte voice slice. For low-rate codecs, headers dominate the bandwidth."),
        ]),
        EX("Worked example 3: can the link carry the calls?", intro=(
            "The firm's internet link has an upload speed of 2 Mbit/s. Management wants up to 12 simultaneous calls with the 64 kbit/s codec. "
            "Use the figure from example 1. Will it fit? What changes if the codec of example 2 is used?"), steps=[
            S("Total for 12 calls", math=r"12 \times 80 = 960 \text{ kbit/s}"),
            S("Compare with the link", math=r"2 \text{ Mbit/s} = 2000 \text{ kbit/s};\ 960 < 2000", text="The calls fit, leaving about 1040 kbit/s for other traffic."),
            S("Compressed codec", math=r"12 \times 24 = 288 \text{ kbit/s}", text="Much less bandwidth, but a little more quality loss."),
            S("Advice", text="Keep some bandwidth free for web traffic, and use QoS so voice has priority. Check the download direction too, since calls use both directions."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using the codec rate as the call bandwidth", "Each packet carries headers. The real bandwidth is larger than the codec rate."),
        MISTAKE("Forgetting that calls use both directions", "A call sends and receives at the same time, so upload and download are both needed."),
        MISTAKE("Planning with the full link speed", "Other users also share the link. Plan calls to use only part of it."),
        QUIZ("Which problem is described as variation in the arrival time of packets?",
             ["Latency", "Jitter", "Packet loss", "Compression"], 1,
             "Jitter is the variation in packet arrival times.",
             feedback=["Latency is the delay itself.", "", "Packet loss is when packets never arrive.", "Compression is done by the codec before sending."]),
        QUIZ("A codec produces 160 bytes of voice every 20 ms. With 40 bytes of headers, what is the bandwidth in one direction?",
             ["64 kbit/s", "80 kbit/s", "160 kbit/s", "200 kbit/s"], 1,
             "(160 + 40) x 8 x 50 = 80 000 bit/s.",
             hint="Add the headers first, then use bits and 50 packets per second.",
             feedback=["That is the codec rate only; headers are missing.", "", "This is the payload bytes shown as kilobits, not the bandwidth.", "That is the packet size in bytes, not in kbit/s."]),
        H("Practice questions"),
        PQ("Explain why a buffer is used at the receiving end of a VoIP call.",
           "Packets arrive at uneven times (jitter) and sometimes out of order. A short buffer holds them so they can be put in order and played at an even rate. "
           "A larger buffer smooths more jitter but adds delay."),
        PQ("A codec rate is 16 000 bit/s with a packet every 20 ms. Calculate the bandwidth of one call, one direction, with 40 bytes of headers.",
           "Payload = 16 000 x 0.02 / 8 = 40 bytes. With headers 80 bytes. 80 x 8 x 50 = 32 000 bit/s = 32 kbit/s."),
        PQ("An office link has 1 Mbit/s upload. How many simultaneous calls of 80 kbit/s each can it carry if 25 percent of the link is kept for other traffic?",
           "Usable = 0.75 x 1000 = 750 kbit/s. 750 / 80 = 9.4, so 9 calls."),
        PQ("State two benefits and two problems of VoIP for a business.",
           "Benefits: lower call charges, especially between sites; one network for data and voice; easy to add extensions. Problems: poor quality if the network has delay, jitter or loss; "
           "calls fail in a power or internet outage; needs enough bandwidth and QoS."),
        SUM("VoIP digitises, compresses, packetizes and sends speech over IP, and the receiver buffers and decodes it.",
            "Latency, jitter and packet loss are the main quality problems; QoS gives voice priority.",
            "Call bandwidth = (payload + 40 bytes) x 8 x packets per second, per direction.",
            "Check total calls against the link capacity, leaving room for other traffic."),
    ]))

LESSONS.append(lesson(
    module=ENT, topic="Business technologies",
    title="Learning management systems: features, roles and low-bandwidth delivery",
    slug="ic6-learning-platforms-lms", minutes=18,
    summary="Describe what a learning management system does, the roles of administrator, teacher and student, and how to plan online learning that works with limited data and power.",
    objectives=[
        "Define a learning management system and list its main features",
        "Describe the roles and permissions of administrator, teacher and student",
        "Compare synchronous and asynchronous online learning",
        "Plan an LMS course for students with limited data, devices and electricity",
    ],
    key_concepts=["LMS", "Course", "Assessment", "Role", "Synchronous", "Asynchronous", "Progress tracking", "Low-bandwidth delivery"],
    blocks=[
        H("Introduction"),
        T("A teacher at a secondary school in Maroua puts his notes on a messaging group. Students lose them, cannot find which "
          "homework is new, and the teacher does not know who has finished what. A **learning management system** puts the notes, "
          "tasks, marks and messages in one place. Schools, universities and companies use them for training."),
        H("What an LMS is"),
        D("A **learning management system (LMS)** is a web-based application used to deliver, manage and track learning. It "
          "stores courses, lets teachers set tasks and tests, lets students submit work, and records progress and results.", title="Definition"),
        KEY("Main features", "", cards=[
            ["Content", "Lessons as pages, documents, video links and audio, organised in modules."],
            ["Assessment", "Quizzes marked automatically, assignments with file upload and teacher feedback, and a grade book."],
            ["Communication", "Announcements, discussion forums and messages."],
            ["Tracking and reports", "Who opened what, who finished, scores over time, so that teachers can help students who are falling behind."],
            ["Enrolment and access", "Students join courses by code or by the administrator; each person sees only what their role allows."],
        ]),
        H("Roles and permissions"),
        CODE("""
Role            Can do
Administrator   Create accounts and courses, set up the system, manage backups
Teacher         Add and edit content in own courses, set and mark work, see progress
Student         Open content, take quizzes, submit work, see own grades and feedback
Guest           View only public material, if allowed
""", "text", title="Table 1", caption="Typical roles in an LMS"),
        T("Roles are an example of **access control**: each user receives only the permissions needed for their job. A student must not be able to edit grades."),
        H("Synchronous and asynchronous learning"),
        KEY("Two ways to learn online", "", cards=[
            ["Synchronous", "Everyone takes part at the same time, such as a live video class or chat. It needs good connections and fixed times."],
            ["Asynchronous", "Students study when they like using recorded lessons, notes and forums, and submit work by a deadline. It suits poor connections and students with other duties."],
        ]),
        EX("Worked example 1: choose the delivery for a community college", intro=(
            "Students at a rural college share a few phones and have power for only some hours a day. Choose between synchronous and asynchronous delivery and explain."), steps=[
            S("Look at the constraints", text="Connection and power are unreliable and students cannot all be online at the same time."),
            S("Choose", text="Asynchronous, with a weekly deadline. Students can use the hours when power and data are available."),
            S("Add support", text="Use a short live session by voice or messaging, only once a week for questions, and record it."),
        ]),
        EX("Worked example 2: plan a low-bandwidth course", intro=(
            "A teacher will put a six-week ICT course on an LMS for students on mobile data. Give a plan that keeps data use low."), steps=[
            S("Prefer text", text="Write lessons as short pages and downloadable PDF notes instead of long videos."),
            S("Compress", text="Reduce image sizes and give a download link for audio at low quality."),
            S("Offline use", text="Let students download the week's materials once and work offline, then upload at the end."),
            S("Quizzes", text="Use short auto-marked quizzes that need little data, and give feedback immediately."),
            S("Support", text="Give a data-use estimate for each week so students can plan."),
        ]),
        EX("Worked example 3: use the reports", intro=(
            "The LMS report shows that 6 of 30 students have not opened Week 2, and 4 scored below 40 percent in the Week 1 quiz. What percentage needs follow-up, if the two groups do not overlap?"), steps=[
            S("Add the two groups", math=r"6 + 4 = 10"),
            S("Find the percentage", math=r"\frac{10}{30} \times 100 = 33.3\%"),
            S("Action", text="Message these students, offer an extra session and check whether the problem is access or understanding."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using an LMS only as a file store", "The value comes from structure, assessment and tracking as well as from files."),
        MISTAKE("Assuming all students are online at the same time", "Plan asynchronous options when data, devices and power are limited."),
        MISTAKE("Giving all users the same permissions", "Roles protect grades and course content. Give each person only what the job needs."),
        QUIZ("Which feature of an LMS lets a teacher see which students have not started a topic?",
             ["The grade book", "Progress tracking and reports", "The forum", "The announcement board"], 1,
             "Tracking and reports record who opened which items and who completed them.",
             feedback=["The grade book shows marks, not whether materials were opened.", "", "The forum is for discussion.", "Announcements send messages out; they do not record activity."]),
        QUIZ("Which is an example of asynchronous learning?",
             ["A live video class at 10:00", "Students reading recorded notes and submitting work by Friday", "A phone call between teacher and student", "A live chat session"], 1,
             "Asynchronous learning does not need everyone to be online at the same time.",
             feedback=["Everyone must be online at 10:00, so it is synchronous.", "",
                       "A call happens in real time, so it is synchronous.", "A live chat needs everyone present at the same time."]),
        H("Practice questions"),
        PQ("Define an LMS and give three of its features.",
           "An LMS is a web-based system used to deliver, manage and track learning. Features: course content; quizzes and assignments with a grade book; forums and messages; "
           "progress tracking and reports; user roles and enrolment. Any three."),
        PQ("Explain the difference between synchronous and asynchronous learning, with one advantage of asynchronous for a school with weak internet.",
           "Synchronous: all take part at the same time, such as a live video class. Asynchronous: students study and submit work at times of their choice. "
           "Advantage of asynchronous: students can use the hours when the connection and power are available, and need not be online together."),
        PQ("Describe two differences between the permissions of a teacher and a student in an LMS.",
           "A teacher can add and edit content, create and mark assessments and see progress of all students in the course. A student can only open content, submit work and see own grades. "
           "Students cannot change content or other students' marks."),
        PQ("Suggest three ways to reduce the data used by LMS course materials.",
           "Use text and PDF files rather than long video; compress images; allow downloading for offline use; offer low-quality audio; keep pages short; avoid autoplay media."),
        SUM("An LMS delivers, manages and tracks learning in one web-based system.",
            "Features: content, assessment, communication, tracking and enrolment.",
            "Roles (administrator, teacher, student) give people only the permissions they need.",
            "Asynchronous learning suits limited data and power; synchronous needs everyone online together.",
            "Low-bandwidth plans use text, small files and offline downloads."),
    ]))

# ===========================================================================
# Green computing
# ===========================================================================
LESSONS.append(lesson(
    module=ENT, topic="Green computing",
    title="Energy use in ICT: measuring, costing and reducing it",
    slug="ic6-green-energy-use", minutes=22,
    summary="Calculate the energy and cost of running ICT equipment from power and time, estimate the saving from power management and efficient devices, and describe green practices in offices and data centres.",
    objectives=[
        "Define green computing and explain why ICT energy use matters for cost and the environment",
        "Calculate energy in kilowatt-hours and cost from power in watts and hours of use",
        "Estimate savings from power management and more efficient equipment",
        "Describe practical measures for offices, labs and data centres, including power usage effectiveness",
    ],
    key_concepts=["Green computing", "Watt", "Kilowatt-hour", "Standby power", "Power management", "Thin client", "PUE", "Carbon footprint"],
    blocks=[
        H("Introduction"),
        T("A school computer lab in Kribi has 20 PCs. The head teacher is shocked by the electricity bill and asks the ICT teacher how "
          "much the lab really uses and how it could be cut. To answer, the teacher needs to calculate energy, not just guess."),
        D("**Green computing** (sustainable ICT) is the design, use and disposal of computers and related equipment in ways that use "
          "less energy and fewer resources and reduce harm to the environment, while still meeting the needs of users.", title="Definition"),
        T("There are three good reasons to care. Electricity costs money, especially for organisations with many devices. In many places "
          "the supply is limited or unreliable, so lower use means fewer overloads. And producing electricity often causes pollution, so less use lowers the carbon footprint."),
        H("Power and energy"),
        D("**Power** is the rate at which a device uses energy, measured in **watts (W)**. **Energy** is the total used over time. Electricity is "
          "sold in **kilowatt-hours (kWh)**: one kilowatt (1000 W) used for one hour.", title="Definition",
          formula=r"\text{energy (kWh)} = \frac{\text{power (W)} \times \text{time (h)}}{1000}"),
        F(r"\text{cost} = \text{energy (kWh)} \times \text{price per kWh}", title="Cost"),
        EX("Worked example 1: monthly energy of the lab", intro=(
            "The lab has 20 PCs, each using 120 W with its monitor. They run 8 hours a day for 22 days a month. Find the energy used in a month and its cost, "
            "if electricity costs 100 FCFA per kWh. (The tariff is an assumed figure for practice; use the real price on your bill.)"), steps=[
            S("Energy of one PC for one day", math=r"\frac{120 \times 8}{1000} = 0.96 \text{ kWh}"),
            S("For 20 PCs, 22 days", math=r"0.96 \times 20 \times 22 = 422.4 \text{ kWh}"),
            S("Cost", math=r"422.4 \times 100 = 42\,240 \text{ FCFA}"),
        ]),
        H("Reducing energy use"),
        KEY("Practical measures", "", cards=[
            ["Power management", "Set screens to turn off and PCs to sleep after a short idle time. Shut down at the end of the day."],
            ["Efficient devices", "Laptops, tablets, mini PCs and LED screens use far less power than old desktop towers and bulky monitors."],
            ["Switch off standby", "Many devices use power when switched off at the button. Use a switched power strip so everything can be cut at once."],
            ["Thin clients and sharing", "A lab of low-power terminals using one strong server can use less than many full PCs. Shared printers replace one per desk."],
            ["Virtualization", "Several servers on one host replace several machines that each idle most of the time."],
            ["Cooling and layout", "Keep vents clear, avoid direct sun, use fans before air conditioning and arrange hot equipment to share cool airflow."],
        ]),
        EX("Worked example 2: saving from sleep mode", intro=(
            "Each lab PC is idle for 3 hours a day. In sleep mode a PC uses 5 W instead of 120 W. Find the monthly saving in kWh and FCFA for the 20 PCs over 22 days at 100 FCFA per kWh."), steps=[
            S("Power saved", math=r"120 - 5 = 115 \text{ W}"),
            S("Energy saved by one PC per day", math=r"\frac{115 \times 3}{1000} = 0.345 \text{ kWh}"),
            S("For 20 PCs, 22 days", math=r"0.345 \times 20 \times 22 = 151.8 \text{ kWh}"),
            S("Money saved", math=r"151.8 \times 100 = 15\,180 \text{ FCFA}", text="About 36 percent of the 42 240 FCFA bill, from changing one setting."),
        ]),
        EX("Worked example 3: replace desktops with laptops?", intro=(
            "A desktop and monitor use 120 W; a laptop uses 65 W. Each is used 8 hours a day for 22 days. Compare the monthly energy and the saving per device in kWh, then in FCFA at 100 FCFA per kWh."), steps=[
            S("Desktop", math=r"\frac{120 \times 8 \times 22}{1000} = 21.12 \text{ kWh}"),
            S("Laptop", math=r"\frac{65 \times 8 \times 22}{1000} = 11.44 \text{ kWh}"),
            S("Saving per device", math=r"21.12 - 11.44 = 9.68 \text{ kWh} \rightarrow 968 \text{ FCFA a month}"),
            S("Judge it", text="Laptops also work during short power cuts on battery. But buying 20 laptops costs a lot, and the energy saving alone takes years to repay it. The decision uses cost, security and repair, as well as energy."),
        ]),
        H("Data centres and PUE"),
        D("**Power usage effectiveness (PUE)** measures how much of a data centre's power reaches the IT equipment. It is the total facility power divided by the IT equipment power. "
          "A PUE of 1.0 would be perfect; the closer to 1, the less is lost on cooling and other overheads.", title="Definition",
          formula=r"\text{PUE} = \frac{\text{total facility power}}{\text{IT equipment power}}"),
        T("For example, a server room using 150 kW in total, of which 100 kW powers the IT equipment, has a PUE of 150 divided by 100, which is 1.5. "
          "The other 50 kW goes on cooling, lighting and power conversion. Reducing cooling losses is the usual way to improve it."),
        T("Carbon footprint can be estimated by multiplying the energy by an emission factor for the electricity supply. The factor differs between "
          "countries and years, so use a figure from an official source. If a lab used 422.4 kWh and the factor were 0.5 kg per kWh (an assumed figure), the footprint would be 211.2 kg."),
        H("Common mistakes"),
        MISTAKE("Mixing watts and kilowatt-hours", "Watts measure power now; kilowatt-hours measure energy used over time. Divide by 1000 only once, after multiplying by hours."),
        MISTAKE("Thinking a screen saver saves energy", "A moving picture still uses power. Turning the screen off, or sleep mode, is what reduces use."),
        MISTAKE("Ignoring the cost of new equipment", "A more efficient device saves energy but costs money and creates e-waste. Compare the full picture."),
        QUIZ("A 200 W device runs for 5 hours. How much energy does it use?",
             ["1 kWh", "10 kWh", "0.04 kWh", "1000 kWh"], 0,
             "200 x 5 = 1000 Wh = 1 kWh.",
             hint="Multiply watts by hours, then divide by 1000.",
             feedback=["", "That multiplies without dividing by 1000 correctly: 200 x 5 = 1000 watt-hours, not 10 kWh.", "That divides 200 by 5 and then by 1000, instead of multiplying power by time.", "1000 is the number of watt-hours, not kilowatt-hours."]),
        QUIZ("A data centre uses 240 kW in total, and 200 kW reaches the IT equipment. What is its PUE?",
             ["0.83", "1.2", "1.4", "2.4"], 1,
             "PUE = 240 / 200 = 1.2.",
             feedback=["That is 200 / 240, the wrong way round. PUE is total power divided by IT power.", "", "That would be 280 / 200.", "That is 240 / 100; the IT power is 200 kW."]),
        H("Practice questions"),
        PQ("Define green computing and give two benefits of it to a school.",
           "Green computing is designing, using and disposing of ICT equipment in ways that use less energy and fewer resources and cause less environmental harm. "
           "Benefits: lower electricity costs, fewer demands on an unreliable supply, a lower carbon footprint, and less e-waste if equipment lasts longer. Any two."),
        PQ("A projector of 250 W is used 6 hours a day for 20 days. Find the monthly energy and the cost at 100 FCFA per kWh.",
           "250 x 6 x 20 = 30 000 Wh = 30 kWh. Cost = 30 x 100 = 3000 FCFA."),
        PQ("Explain how setting PCs to sleep after 10 minutes of inactivity reduces energy use. State one disadvantage.",
           "A sleeping PC uses only a few watts instead of its full power, so idle time costs little energy. A disadvantage: it takes a few seconds to wake, and work not saved "
           "could be lost if the power fails while the machine sleeps."),
        PQ("A server room uses 90 kW in total and its IT equipment uses 60 kW. Calculate the PUE and explain what it means.",
           "PUE = 90 / 60 = 1.5. One third of the power (30 kW) is used for cooling and other overheads rather than computing. A lower figure, closer to 1, means a more efficient facility."),
        SUM("Energy (kWh) = power (W) x hours / 1000, and cost = energy x price per kWh.",
            "Power management, efficient devices, switching off standby and virtualization all reduce energy use.",
            "Calculate savings before deciding; weigh them against the cost of new equipment.",
            "PUE = total facility power / IT power; closer to 1 is better.",
            "Carbon footprint depends on the emission factor of the electricity supply."),
    ]))

LESSONS.append(lesson(
    module=ENT, topic="Green computing",
    title="E-waste management: hazards, the 5 Rs and safe disposal",
    slug="ic6-ewaste-management", minutes=20,
    summary="Explain what e-waste is, why it is hazardous, how to reduce, reuse, repair and recycle equipment, and how to protect data before disposal.",
    objectives=[
        "Define e-waste and name the hazards of careless disposal",
        "Apply the waste hierarchy: reduce, reuse, repair, recycle, dispose",
        "Describe how to remove data safely before equipment leaves an organisation",
        "Write a simple e-waste plan for a school or business",
    ],
    key_concepts=["E-waste", "Hazardous substances", "Reduce, reuse, repair, recycle", "Refurbishment", "Data sanitisation", "Producer responsibility", "Life cycle"],
    blocks=[
        H("Introduction"),
        T("Behind a market in Douala there is a heap of broken monitors, old phones and cables. Young workers burn the cable coating to get "
          "the copper inside. The smoke is dark and sharp. This work earns a little money, but it also puts poisons in the air, "
          "soil and the lungs of the workers. This is the problem of electronic waste."),
        D("**E-waste** (electronic waste) is discarded electrical and electronic equipment, such as computers, phones, monitors, printers, batteries and cables, "
          "including whole items and their parts.", title="Definition"),
        H("Why e-waste is a problem"),
        KEY("Hazards and losses", "", cards=[
            ["Toxic materials", "Devices can contain lead, mercury, cadmium and flame-retardant chemicals. When burned or broken without care, these can pollute air, soil and water and harm health."],
            ["Burning and acid", "Burning cables releases harmful smoke. Acid baths used to recover metals can poison workers and rivers."],
            ["Lost resources", "Circuit boards contain copper, gold and other metals that can be recovered. Throwing them away wastes materials that need mining."],
            ["Data theft", "An old hard disk or phone may contain bank details, personal documents and passwords that someone could recover."],
            ["Growing volume", "Short product lives, falling prices and imports of second-hand equipment add to the total."],
        ]),
        T("Imported second-hand equipment can be helpful, since it gives affordable access to computers. It becomes a problem when items arrive "
          "already broken, so the cost of disposal falls on the importing country. Check the national rules and the Basel Convention principles on trade in hazardous waste."),
        H("The waste hierarchy"),
        D("The **waste hierarchy** lists actions in order of preference. It is often taught as the Rs: **reduce**, **reuse**, **repair**, **recycle**, and only last **dispose** safely. "
          "The best waste is the waste never created.", title="Definition"),
        CODE("""
1. Reduce    Buy only what is needed; choose durable, upgradeable devices
2. Reuse     Give working equipment to another user, school or charity
3. Repair    Fix faults; replace batteries, memory or disks to extend life
4. Recycle   Send broken items to a recycler that recovers materials safely
5. Dispose   Last resort, by an approved facility, never by burning or dumping
""", "text", title="Table 1", caption="The waste hierarchy from best to last resort"),
        EX("Worked example 1: life of a laptop", intro=(
            "A school needs working laptops for 15 years. It compares replacing laptops every 3 years with replacing them every 5 years. How many laptops are bought per seat in each case?"), steps=[
            S("Replace every 3 years", math=r"15 \div 3 = 5 \text{ laptops}"),
            S("Replace every 5 years", math=r"15 \div 5 = 3 \text{ laptops}"),
            S("Difference", math=r"5 - 3 = 2", text="Two fewer laptops per seat means less manufacturing, less cost and less waste. Repairing batteries and upgrading memory can make the longer life possible."),
        ]),
        EX("Worked example 2: decide what to do with 40 old PCs", intro=(
            "A school is replacing 40 old PCs. 25 work but are slow, 10 fail to start because of power supply faults, and 5 have broken boards. Apply the waste hierarchy."), steps=[
            S("Reuse the 25", text="Add memory or an SSD if it makes them useful, install a light operating system, and donate or use them in a less demanding room."),
            S("Repair the 10", text="Replace the faulty power supplies; this is cheaper than buying new PCs. Then reuse them."),
            S("Recycle the 5", text="Remove useful parts such as memory and drives, and send the rest to an approved recycler."),
            S("Count the result", math=r"25 + 10 = 35 \text{ PCs back in use;}\ 5 \text{ recycled}", text="Only 5 of 40 (12.5 percent) are sent for recycling."),
        ]),
        H("Protecting data before disposal"),
        D("**Data sanitisation** is the permanent removal of data from storage so it cannot be recovered. Deleting files or quick-formatting does not do this, "
          "because the data stays on the disk until it is overwritten.", title="Definition"),
        KEY("Methods", "Choose by the media and the sensitivity of the data.", cards=[
            ["Overwrite", "Write over the whole disk with new data, once or more, using a trusted tool. Works for hard disks."],
            ["Secure erase or encryption key deletion", "Many SSDs and phones support a built-in erase command. If the drive was always encrypted, destroying the key makes the data unreadable."],
            ["Physical destruction", "Drilling, shredding or crushing the drive. Used when the data is very sensitive or the drive is broken."],
        ]),
        EX("Worked example 3: write a short e-waste plan", intro=(
            "Write the main points of an e-waste plan for a school computer room."), steps=[
            S("Inventory", text="Keep a list of all equipment with age, condition and the planned replacement date."),
            S("Prevention", text="Buy equipment that can be repaired and upgraded, and teach students to look after it."),
            S("Data", text="Before any item leaves the school, sanitise its drives and record that it was done."),
            S("Collection", text="Keep a secure store for broken equipment and arrange collection by an approved recycler or a supplier take-back scheme."),
            S("Records", text="Keep receipts for recycling, which show that the waste went to the right place."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking deleting files protects data", "Deleted files can be recovered. Use overwrite, secure erase, encryption key deletion or destruction."),
        MISTAKE("Treating recycling as the first choice", "Reducing, reusing and repairing come first because they save the energy and materials of making a new device."),
        MISTAKE("Burning cables for copper", "It creates toxic smoke. Give cables to a recycler that recovers copper safely."),
        QUIZ("Which action comes FIRST in the waste hierarchy?",
             ["Recycle", "Dispose", "Reduce", "Repair"], 2,
             "Reduce means preventing waste, which is the best option.",
             feedback=["Recycling comes later in the order.", "Disposal is the last resort.", "", "Repair is better than recycling but comes after reducing and reusing."]),
        QUIZ("A school sells old laptops. Which step best protects the data on them?",
             ["Deleting the documents folder", "Emptying the recycle bin", "Sanitising the drive with an overwrite or secure-erase tool", "Removing the battery"], 2,
             "Sanitising permanently removes the data so it cannot be recovered.",
             feedback=["Deleted files stay on the disk and can be recovered.", "Emptying the bin only removes the pointers.", "", "The battery has nothing to do with the stored data."]),
        H("Practice questions"),
        PQ("Define e-waste and give two examples.",
           "E-waste is discarded electrical or electronic equipment. Examples: old computers, mobile phones, monitors, printers, batteries and cables."),
        PQ("Explain two dangers of burning electronic cables and circuit boards.",
           "The smoke contains toxic chemicals that harm the lungs and health of workers and nearby people; ash and residues contaminate soil and water with metals such as lead and cadmium. "
           "Valuable materials are also lost or recovered with poor yield."),
        PQ("State the order of the waste hierarchy and give an ICT example of reuse.",
           "Reduce, reuse, repair, recycle, dispose. Reuse example: donating working PCs to a primary school or giving them a light operating system for a less demanding use."),
        PQ("A business is about to give away 30 old laptops. Describe the steps it should take to protect its data.",
           "Back up anything still needed, then sanitise each drive by overwriting with a trusted tool, using the manufacturer's secure-erase command or deleting the encryption key; "
           "destroy drives that are faulty or hold very sensitive data. Record the process for each device, and check a sample to confirm the data cannot be recovered."),
        SUM("E-waste is discarded electronic equipment; it contains hazardous and valuable materials.",
            "Follow the waste hierarchy: reduce, reuse, repair, recycle, dispose.",
            "Longer equipment life means fewer devices bought and less waste.",
            "Sanitise data before disposal; deleting or quick formatting is not enough.",
            "Use approved recyclers and keep records."),
    ]))

# ===========================================================================
# Database automation
# ===========================================================================
LESSONS.append(lesson(
    module=ENT, topic="Database automation",
    title="Triggers in practice: keeping stock correct, rejecting bad data and logging changes",
    slug="ic6-db-triggers-practice", minutes=24,
    summary="Write and trace BEFORE and AFTER triggers that update stock, reject invalid rows and keep an audit log, and predict the result of a sequence of inserts.",
    objectives=[
        "State the events, timing and row access (NEW and OLD) of a trigger",
        "Write an AFTER INSERT trigger that updates a related table",
        "Write a BEFORE INSERT trigger that rejects invalid data",
        "Write an audit trigger and trace the tables after a series of statements",
    ],
    key_concepts=["Trigger", "BEFORE and AFTER", "NEW and OLD", "Audit log", "Business rule", "Referential consistency"],
    blocks=[
        H("Introduction"),
        T("A pharmacy in Limbe records each sale in a database. Without automation, someone must also reduce the stock by hand. If "
          "they forget, the shelf and the computer disagree, and the pharmacy sells a medicine it no longer has. A trigger makes the "
          "database do the second job every time, without fail."),
        T("The overview lesson introduced triggers and their syntax in MySQL style. This lesson is about practice: three triggers that businesses really need, "
          "and how to trace what they do. The SQL below runs as written in SQLite. MySQL differs in two places that are marked."),
        D("A **trigger** is a named block of SQL attached to a table. It runs automatically when a chosen event (INSERT, UPDATE or DELETE) happens on the table. "
          "It is defined with a timing (BEFORE or AFTER) and, for row triggers, runs once for each row affected. Inside it, **NEW** is the row being written and **OLD** is the row as it was.", title="Definition"),
        CODE("""
Event    NEW available?   OLD available?
INSERT   yes              no
UPDATE   yes              yes
DELETE   no               yes
""", "text", title="Table 1", caption="Which row references each event can use"),
        T("Our database has three tables. The data at the start is shown in Listing 1."),
        CODE("""
CREATE TABLE products(product_id INTEGER PRIMARY KEY, name TEXT, stock INTEGER, reorder_level INTEGER);
CREATE TABLE sales(sale_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, sale_date TEXT);
CREATE TABLE stock_log(log_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, old_stock INTEGER, new_stock INTEGER);

INSERT INTO products VALUES (1,'Paracetamol',50,20),(2,'Amoxicillin',12,15),(3,'ORS sachets',30,10);
""", "sql", title="Listing 1", caption="Tables and starting data"),
        H("Trigger 1: update stock after a sale"),
        CODE("""
CREATE TRIGGER trg_sale_update_stock
AFTER INSERT ON sales
FOR EACH ROW
BEGIN
  UPDATE products SET stock = stock - NEW.quantity
  WHERE product_id = NEW.product_id;
END;
""", "sql", title="Listing 2", caption="AFTER INSERT trigger"),
        EX("Worked example 1: trace one sale", intro=(
            "Run INSERT INTO sales(product_id, quantity, sale_date) VALUES (1, 3, '2026-11-05'). What are the stock values afterwards?"), steps=[
            S("Event", text="A row is inserted into sales, so the trigger fires after it is saved."),
            S("NEW", text="NEW.product_id is 1 and NEW.quantity is 3."),
            S("Update", text="The WHERE clause selects only product 1. Its stock changes from 50 to 47."),
            S("Other products", text="Products 2 and 3 keep 12 and 30 because the WHERE clause protects them."),
        ]),
        H("Trigger 2: reject a sale larger than the stock"),
        CODE("""
CREATE TRIGGER trg_sale_check
BEFORE INSERT ON sales
FOR EACH ROW
WHEN NEW.quantity > (SELECT stock FROM products WHERE product_id = NEW.product_id)
BEGIN
  SELECT RAISE(ABORT, 'Not enough stock');
END;
""", "sql", title="Listing 3", caption="BEFORE INSERT trigger that blocks the row (SQLite). In MySQL write IF ... THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Not enough stock'; END IF;"),
        EX("Worked example 2: a sale that is too large", intro=(
            "With the stock as in Listing 1, run INSERT INTO sales(product_id, quantity, sale_date) VALUES (2, 20, '2026-11-05'). What happens?"), steps=[
            S("Timing", text="The trigger is BEFORE INSERT, so it runs before the row is stored."),
            S("Test the condition", text="Amoxicillin has stock 12. The sale asks for 20. 20 is greater than 12, so the condition is true."),
            S("Abort", text="RAISE(ABORT) stops the statement with the message Not enough stock. No row is added to sales."),
            S("Effect on stock", text="Because the insert failed, the AFTER trigger of Listing 2 does not run either. Stock stays at 12."),
        ]),
        H("Trigger 3: an audit log"),
        CODE("""
CREATE TRIGGER trg_stock_audit
AFTER UPDATE OF stock ON products
FOR EACH ROW
BEGIN
  INSERT INTO stock_log(product_id, old_stock, new_stock)
  VALUES (OLD.product_id, OLD.stock, NEW.stock);
END;
""", "sql", title="Listing 4", caption="An audit trigger records every change of stock"),
        T("An **audit log** is a record of changes to data: what changed, from what, to what, and usually when and by whom. It supports "
          "accountability and helps to find errors. Here the trigger uses OLD for the previous value and NEW for the new one."),
        EX("Worked example 3: trace a sequence", intro=(
            "Starting from Listing 1 with all three triggers created, run these inserts in order: "
            "(1) product 1, quantity 3; (2) product 2, quantity 20; (3) product 2, quantity 5; (4) product 1, quantity 10; (5) product 1, quantity 2. "
            "Give the final stock and the contents of stock_log."), steps=[
            S("Insert 1", text="Product 1: 50 to 47. The audit trigger logs (1, 50, 47)."),
            S("Insert 2", text="Rejected: 20 is more than the stock of 12. Nothing changes, nothing is logged."),
            S("Insert 3", text="Product 2: 12 to 7. Log (2, 12, 7)."),
            S("Insert 4", text="Product 1: 47 to 37. Log (1, 47, 37)."),
            S("Insert 5", text="Product 1: 37 to 35. Log (1, 37, 35)."),
            S("Final state", text="Stock: product 1 = 35, product 2 = 7, product 3 = 30. The log has four rows. Sales holds four rows: the rejected one is absent."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using OLD in an INSERT trigger", "A new row has no earlier version. Use NEW for inserts, OLD for deletes and both for updates."),
        MISTAKE("Leaving out the WHERE clause", "Without WHERE product_id = NEW.product_id, every product's stock would change on each sale."),
        MISTAKE("Using an AFTER trigger to refuse a row", "AFTER runs once the row is saved. To stop invalid data, use a BEFORE trigger or a constraint."),
        QUIZ("Which trigger timing should be used to reject a sale before it is saved?",
             ["AFTER INSERT", "BEFORE INSERT", "AFTER DELETE", "AFTER UPDATE"], 1,
             "A BEFORE INSERT trigger runs before the row is stored and can stop the statement.",
             feedback=["AFTER INSERT runs when the row is already saved.", "", "DELETE triggers react to removed rows.", "UPDATE triggers react to changed rows."]),
        QUIZ("Which row reference can a DELETE trigger use?",
             ["NEW only", "OLD only", "Both NEW and OLD", "Neither"], 1,
             "A deleted row has an old version but no new one.",
             feedback=["There is no new row in a delete.", "", "Both exist only in an UPDATE.", "The trigger can read the deleted row through OLD."]),
        H("Practice questions"),
        PQ("Write an AFTER DELETE trigger that returns the quantity to stock when a row is deleted from sales.",
           "CREATE TRIGGER trg_sale_delete AFTER DELETE ON sales FOR EACH ROW BEGIN UPDATE products SET stock = stock + OLD.quantity WHERE product_id = OLD.product_id; END; "
           "OLD is used because a deleted row has no NEW version. Deleting the 3-unit sale of product 1 in the trace raises its stock by 3."),
        PQ("Explain why the update trigger in Listing 2 needs a WHERE clause.",
           "Without WHERE, UPDATE would apply to every row of products, so each sale would reduce the stock of every product. The clause restricts the change to the product sold."),
        PQ("Starting with product stock 12, a sale of 12 is inserted using the triggers above. State whether it is accepted and the new stock.",
           "The condition NEW.quantity > stock is 12 > 12, which is false, so the BEFORE trigger allows the row. The AFTER trigger reduces stock to 0."),
        PQ("Give two reasons a business keeps an audit log of stock changes.",
           "To find who or what caused a stock error; to show changes for checks and audits; to detect theft or unusual changes; to rebuild what happened on a given day."),
        SUM("A trigger runs automatically on INSERT, UPDATE or DELETE, BEFORE or AFTER the change.",
            "NEW holds the new row (insert, update) and OLD the previous one (update, delete).",
            "Use BEFORE triggers to reject data and AFTER triggers to react to saved data.",
            "Always restrict updates with a WHERE clause linking the rows.",
            "An audit trigger records old and new values to a log table."),
    ]))

LESSONS.append(lesson(
    module=ENT, topic="Database automation",
    title="Stored procedures, scheduled jobs and macros: choosing the right tool",
    slug="ic6-db-procedures-jobs-macros", minutes=22,
    summary="Write a parameterised report as a stored procedure, schedule a nightly reorder list, describe macros in desktop databases, and choose between triggers, procedures, jobs and macros.",
    objectives=[
        "Explain what a stored procedure is and how a parameter makes it reusable",
        "Write the query behind a daily sales report and an overnight reorder list, and check the results by tracing",
        "Describe scheduled jobs and macros and when each is used",
        "Choose the correct automation tool for a business need",
    ],
    key_concepts=["Stored procedure", "Parameter", "Scheduled job", "Macro", "Batch report", "Automation tool choice"],
    blocks=[
        H("Introduction"),
        T("Every evening the pharmacy owner in Limbe asks for two things: a list of what was sold today and a list of what must be reordered. "
          "Her assistant writes the same SQL by hand each day and sometimes makes a typing mistake. Automation can save the query once and run it at a set time or at a click."),
        H("Stored procedures"),
        D("A **stored procedure** is a named, saved block of SQL kept in the database and run on request, for example with CALL. It can take "
          "**parameters**, which are values supplied when it is called. Because the code is saved on the server, everyone runs the same, tested version.", title="Definition"),
        T("Benefits: the logic is written once; users do not need to know the table structure; parameters give flexibility; and "
          "access can be given to the procedure rather than to the tables themselves. SQLite does not support stored procedures, so the check below runs the query that forms the body of the procedure with a parameter. "
          "The MySQL form is shown in Listing 1."),
        CODE("""
DELIMITER //
CREATE PROCEDURE daily_sales(IN report_date DATE)
BEGIN
  SELECT p.name, SUM(s.quantity) AS total_sold
  FROM sales s
  JOIN products p ON p.product_id = s.product_id
  WHERE s.sale_date = report_date
  GROUP BY p.product_id, p.name
  ORDER BY total_sold DESC;
END //
DELIMITER ;

CALL daily_sales('2026-11-05');
""", "sql", title="Listing 1", caption="MySQL form. DELIMITER lets the semicolons inside the body be read as part of the procedure."),
        EX("Worked example 1: trace the report", intro=(
            "The sales table holds these rows (product_id, quantity, sale_date): (1, 3, 2026-11-05), (2, 5, 2026-11-05), (1, 10, 2026-11-05), (1, 2, 2026-11-06). "
            "Product 1 is Paracetamol and product 2 is Amoxicillin. What does CALL daily_sales('2026-11-05') return?"), steps=[
            S("Filter by date", text="Keep the first three rows. The fourth is dated 2026-11-06."),
            S("Group by product", text="Product 1 has 3 and 10. Product 2 has 5."),
            S("Add up", math=r"3 + 10 = 13 \text{ for Paracetamol;}\ 5 \text{ for Amoxicillin}"),
            S("Sort", text="ORDER BY total_sold DESC gives Paracetamol 13, then Amoxicillin 5."),
        ]),
        T("Calling it with '2026-11-06' would give one row, Paracetamol with total 2. Only the parameter changed."),
        H("Scheduled jobs"),
        D("A **scheduled job** (called an event in MySQL, an agent job in some other systems, or a task scheduled in the operating system) runs SQL at fixed times, "
          "without anyone starting it.", title="Definition"),
        CODE("""
CREATE TABLE reorder_list(product_id INTEGER, stock INTEGER, listed_on TEXT);

INSERT INTO reorder_list (product_id, stock, listed_on)
SELECT product_id, stock, '2026-11-05'
FROM products
WHERE stock <= reorder_level;
""", "sql", title="Listing 2", caption="The statement run each night. In MySQL it is wrapped in CREATE EVENT ... ON SCHEDULE EVERY 1 DAY DO ... and listed_on uses CURRENT_DATE."),
        EX("Worked example 2: what the nightly job lists", intro=(
            "At the end of the day the products table holds: Paracetamol stock 35 (reorder level 20), Amoxicillin stock 7 (level 15), ORS sachets stock 30 (level 10). Which products enter the reorder list?"), steps=[
            S("Test each product", text="Paracetamol: 35 is more than 20, so no. Amoxicillin: 7 is not more than 15, so yes. ORS sachets: 30 is more than 10, so no."),
            S("Result", text="One row: product 2, stock 7. The list is ready every morning with no human work."),
            S("Why a job, not a trigger", text="No change to a table starts this task. It depends on the time of day, so a scheduled job fits."),
        ]),
        T("If the system has no event scheduler, the operating system can schedule a script that connects to the database and runs the statement. "
          "Typical examples are nightly backups and monthly summaries. Remember to monitor jobs: a job that fails silently is worse than none."),
        H("Macros"),
        T("In a desktop database such as Microsoft Access, a **macro** is a saved list of actions, for example open a form, run a query, print a report and "
          "show a message. It is attached to a button or a form event such as After Update. Macros suit small offices where staff work from forms and do not write SQL. "
          "Larger systems use stored procedures or code instead."),
        H("Choosing the tool"),
        CODE("""
Need                                              Tool
React when a row is added, changed or deleted     Trigger
Run a saved query or task on request, with input  Stored procedure
Run something at a fixed time or interval         Scheduled job / event
Automate steps from a form or button in a         Macro
desktop database
""", "text", title="Table 1", caption="Matching the need to the tool"),
        EX("Worked example 3: pick the tool", intro=(
            "Choose the best tool for each: (a) record the old and new price whenever a price is edited, (b) send the weekly sales summary every Monday at 07:00, "
            "(c) let a cashier press a button on a form to print today's receipts, (d) show the total sales of any chosen month."), steps=[
            S("a", text="It reacts to a data change. Trigger (AFTER UPDATE)."),
            S("b", text="Time-based. Scheduled job."),
            S("c", text="Started from a form button in a desktop database. Macro."),
            S("d", text="The user chooses the month, so a parameter is needed. Stored procedure."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using a trigger for a time-based task", "A trigger fires on a data change only. If nobody inserts anything, it never runs. Use a scheduled job."),
        MISTAKE("Hard-coding the date in the saved query", "A procedure should take the date as a parameter, or the job should use the current date, so it works tomorrow."),
        MISTAKE("Not checking that jobs ran", "Log each run and check the log, or failures stay unnoticed."),
        QUIZ("A manager wants a report of any chosen month's sales. Which feature makes one saved query handle every month?",
             ["A trigger", "A parameter in a stored procedure", "A macro button without input", "A larger hard disk"], 1,
             "A parameter lets the user give the month when calling the procedure.",
             feedback=["Triggers react to changes, not to a chosen month.", "", "A macro without input would always run the same thing.", "Disk size has nothing to do with it."]),
        QUIZ("Which tool is correct for creating a backup copy of the database every night at 02:00?",
             ["A BEFORE INSERT trigger", "A scheduled job", "A form macro", "A foreign key"], 1,
             "The task depends on time, so it needs a scheduled job.",
             feedback=["It would run only when rows are inserted.", "", "It needs somebody to press a button.", "A foreign key protects relationships between tables; it does not start tasks."]),
        H("Practice questions"),
        PQ("Distinguish between a trigger and a stored procedure.",
           "A trigger runs automatically when its table has an INSERT, UPDATE or DELETE and cannot be called directly. A stored procedure runs only when it is called "
           "(for example with CALL) by a user, program or event, and may take parameters."),
        PQ("A procedure monthly_total(month_number) is called with the value 3. Explain what the parameter does.",
           "The parameter carries the value 3 into the procedure, so the saved query is run for March only. Calling it with another value runs the same code for another month, "
           "so one procedure serves many requests."),
        PQ("Which of the nightly reorder list rows are created if Soap has stock 8 and level 8, and Rice has stock 9 and level 8? Use the condition stock <= reorder_level.",
           "Soap: 8 <= 8 is true, so it is listed. Rice: 9 <= 8 is false, so it is not listed. One row."),
        PQ("Give two advantages of automating a daily report with a scheduled job instead of running it by hand.",
           "It runs on time even if staff are absent; it removes typing errors in the query; it saves staff time; results are produced the same way each day. Any two."),
        SUM("A stored procedure is a named saved block of SQL, run with CALL and given parameters.",
            "A scheduled job runs SQL at fixed times; a macro automates actions from forms in desktop databases.",
            "Triggers react to data changes; procedures run on request; jobs run on a timetable.",
            "Choose the tool from how the task is started.",
            "Log and check automated tasks."),
    ]))

# ===========================================================================
# Web Development / Layout
# ===========================================================================
LESSONS.append(lesson(
    module=WEB, topic="Layout",
    title="Semantic HTML5: giving a page meaningful structure",
    slug="ic6-semantic-html5", minutes=20,
    summary="Replace anonymous div blocks with header, nav, main, article, section, aside, figure and footer; use headings and alt text correctly; and explain the benefits for accessibility and search.",
    objectives=[
        "Define semantic HTML and explain its benefits for screen readers, search engines and maintenance",
        "Choose the correct semantic element for each part of a page",
        "Build a page skeleton with a sensible heading outline",
        "Convert a page made of div elements into semantic HTML",
    ],
    key_concepts=["Semantic element", "header and footer", "nav", "main", "article and section", "aside", "figure and figcaption", "Heading outline", "alt text"],
    blocks=[
        H("Introduction"),
        T("A student in Bamenda builds the website for her school. Everything is a div with a class name such as box1 or box2. "
          "It looks fine on her phone. But a blind classmate using a screen reader cannot find the menu, and a search engine cannot tell the news from the footer. "
          "The page has no meaning that software can read. Semantic HTML fixes this."),
        D("A **semantic element** is an HTML element whose name describes the meaning of its content, such as nav for navigation links or footer for the closing "
          "information of a page. A non-semantic element such as div or span says nothing about its content.", title="Definition"),
        KEY("Why use semantic elements", "", cards=[
            ["Accessibility", "Screen readers can list landmarks (header, nav, main, footer) and jump straight to the main content."],
            ["Search engines", "Search programs understand which text is the main article and which is navigation or an advertisement."],
            ["Maintenance", "A developer reading main and aside understands the page faster than reading twenty divs."],
            ["Consistency", "Browsers give meaningful defaults, such as keyboard focus on links and buttons."],
        ]),
        H("The main elements"),
        CODE("""
header   Introductory content of a page or section: logo, title, sometimes nav
nav      A block of major navigation links
main     The central content of the page; use only one per page
article  A self-contained item that makes sense alone: news story, blog post, product card
section  A themed group of content, normally with its own heading
aside    Related side content: a note, a list of links, an advertisement
figure   An image, chart or code listing with an optional figcaption
footer   Closing content: contact details, copyright, links
""", "text", title="Table 1", caption="Common semantic elements and their meaning"),
        T("**article** and **section** are often confused. If the content could be copied to another website and still make sense on its own, use article. "
          "If it is only one part of a larger page, grouped by theme, use section."),
        H("Headings and images"),
        T("Headings (h1 to h6) form an outline of the page, like the chapter titles of a book. Use one h1 for the main title of the page. Use h2 for major parts and h3 inside them. "
          "Do not skip levels to get a bigger or smaller font: use CSS for the size. Screen reader users move through the page by headings."),
        T("Every meaningful image needs an **alt** attribute with a short description of what it shows. If the image is only decoration, use an empty alt, alt with two quotation marks and nothing between, "
          "so that screen readers skip it. Add figcaption when you want a visible caption."),
        EX("Worked example 1: build the skeleton of a school home page", intro=(
            "Write the HTML skeleton for Green Hills School with a header holding the title and a menu, a main area with a news article and a side box, and a footer."), steps=[
            S("Document set-up", text="Start with the doctype, the html element with a language, and a head with the character set, viewport and title."),
            S("Header and nav", text="Put the school name in h1. Put the links in a nav element, as a list inside it."),
            S("Main content", text="Use one main element. Inside it, an article for the news story with an h2, and an aside for the dates."),
            S("Footer", text="Add a footer with contact details. Listing 1 shows the result."),
        ]),
        CODE("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Green Hills School, Bamenda</title>
</head>
<body>
  <header>
    <h1>Green Hills School</h1>
    <nav aria-label="Main menu">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="news.html">News</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article>
      <h2>Science fair results</h2>
      <p>Form 5 students won first prize for a low-cost water filter.</p>
      <figure>
        <img src="fair.jpg" alt="Three students showing a water filter made from sand and charcoal">
        <figcaption>The winning team with their filter.</figcaption>
      </figure>
    </article>
    <aside>
      <h2>Important dates</h2>
      <p>Open day: first Saturday of next month.</p>
    </aside>
  </main>
  <footer>
    <p>Green Hills School, Bamenda. Phone: see the contact page.</p>
  </footer>
</body>
</html>
""", "html", title="Listing 1", caption="A semantic page skeleton"),
        EX("Worked example 2: convert div soup", intro=(
            "Rewrite using semantic elements: div id=top containing div class=logo and div class=menu; div class=content containing div class=post with div class=posttitle; div class=side; div class=bottom."), steps=[
            S("div id=top", text="It is the introductory part of the page, so use header."),
            S("div class=menu", text="It holds navigation links, so use nav."),
            S("div class=content", text="It is the central part of the page, so use main."),
            S("div class=post and posttitle", text="A self-contained post becomes article, and its title becomes a heading, h2."),
            S("div class=side and div class=bottom", text="Related side content becomes aside, and the closing area becomes footer."),
        ]),
        EX("Worked example 3: fix the heading outline", intro=(
            "A page uses h1 for the title, then h4 for each news item (because h4 looks smaller), then h2 for the footer. Explain what is wrong and correct it."), steps=[
            S("Problem 1", text="Skipping from h1 to h4 breaks the outline. Screen reader users jump by level and see a gap."),
            S("Problem 2", text="Using a heading element only for its size is wrong. Size is a presentation matter."),
            S("Fix", text="Use h2 for each news item and style it smaller with CSS. Use h2 for a footer heading only if it is a real section of the page."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using div for everything", "div is correct only when no semantic element fits. Choose header, nav, main, article, section, aside and footer first."),
        MISTAKE("More than one main element", "A page has one main content area. Use sections or articles inside it."),
        MISTAKE("Missing or useless alt text", "Describe what the image shows or means. Do not write image or photo1, and do not leave out alt."),
        QUIZ("Which element should hold the main navigation links of a page?",
             ["aside", "nav", "footer", "section"], 1,
             "nav is the element for a block of major navigation links.",
             feedback=["aside is for related side content.", "", "footer is for closing information.", "section is a themed group of content."]),
        QUIZ("A news story that could be copied to another website and still make sense should be marked up as:",
             ["header", "div", "article", "figure"], 2,
             "article is for a self-contained item such as a news story or blog post.",
             feedback=["header introduces a page or section.", "div has no meaning.", "", "figure holds an image or illustration with a caption."]),
        H("Practice questions"),
        PQ("Define semantic HTML and give two benefits of using it.",
           "Semantic HTML uses elements whose names describe the meaning of the content, such as nav or footer. Benefits: screen readers can navigate by landmarks; search engines understand the page; "
           "the code is easier to read and maintain. Any two."),
        PQ("State the correct element for each: (a) page title and logo area, (b) a list of links to other pages, (c) copyright notice, (d) a photo with a caption.",
           "(a) header; (b) nav; (c) footer; (d) figure with figcaption."),
        PQ("Explain the difference between article and section.",
           "An article is a self-contained piece of content that makes sense on its own, such as a news story. A section is a themed group of related content within a page, normally with its own heading, "
           "that does not stand alone."),
        PQ("Explain why every informative image needs an alt attribute.",
           "Screen readers read the alt text to users who cannot see the image; it is also shown if the image fails to load, which is useful on slow connections, and it helps search engines understand the image."),
        SUM("Semantic elements name the meaning of content; div and span have no meaning.",
            "Use header, nav, main, article, section, aside, figure and footer to give a page structure.",
            "Use one h1, then h2 and h3 in order. Do not choose headings for their size.",
            "Give informative images alt text; use empty alt for pure decoration.",
            "Semantic HTML helps accessibility, search engines and maintenance."),
    ]))

LESSONS.append(lesson(
    module=WEB, topic="Layout",
    title="CSS Flexbox: laying out rows and columns of items",
    slug="ic6-css-flexbox", minutes=24,
    summary="Use display flex, direction, justify-content, align-items, gap, wrap and the flex shorthand to build menus and card rows, and calculate the widths flexbox gives.",
    objectives=[
        "Explain the main axis and cross axis of a flex container",
        "Use justify-content, align-items, gap and flex-wrap to arrange items",
        "Use the flex shorthand (grow, shrink, basis) and calculate resulting widths",
        "Choose flexbox for one-dimensional layouts such as menus and card rows",
    ],
    key_concepts=["Flex container", "Flex item", "Main axis", "Cross axis", "justify-content", "align-items", "flex-wrap", "flex-grow", "flex-basis", "gap"],
    blocks=[
        H("Introduction"),
        T("A shop in Douala wants a web page where the logo is on the left, the menu is in the middle and the cart button is on the right edge, "
          "all on one line and centred vertically. Older CSS needed tricks with floats to do this. Flexbox does it with a few lines."),
        D("**Flexbox** is a CSS layout model for arranging items in one direction, in a row or in a column. Setting display: flex on an element turns it into a "
          "**flex container**, and its direct children become **flex items** that can share, grow and shrink to fill the available space.", title="Definition"),
        H("Axes"),
        T("Flexbox is based on two axes. The **main axis** is the direction items are laid out. By default (flex-direction: row) it runs left to right. "
          "The **cross axis** is perpendicular to it. With flex-direction: column the main axis runs top to bottom, and the cross axis runs across."),
        IMG("al-ic6-flex-axes.svg", alt="A flex container with three items in a row. A horizontal arrow marks the main axis and a vertical arrow marks the cross axis. Labels show justify-content along the main axis and align-items along the cross axis.",
            caption="Figure 1. Main axis and cross axis in a row container"),
        KEY("The container properties", "", cards=[
            ["flex-direction", "row (default), column, row-reverse, column-reverse. Sets the main axis."],
            ["justify-content", "Spacing along the main axis: flex-start, center, flex-end, space-between, space-around, space-evenly."],
            ["align-items", "Alignment along the cross axis: stretch (default), flex-start, center, flex-end."],
            ["gap", "Space between items. No margins needed."],
            ["flex-wrap", "nowrap (default) keeps all items on one line; wrap lets them move to a new line."],
        ]),
        CODE("""
.bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}
""", "css", title="Listing 1", caption="A header bar: logo left, menu in the middle, cart button on the right"),
        EX("Worked example 1: space-between", intro=(
            "A container 600 px wide holds three items of 100 px each with justify-content: space-between and no gap. At what x positions do the items start?"), steps=[
            S("Free space", math=r"600 - 3 \times 100 = 300 \text{ px}"),
            S("Number of gaps", text="Space-between puts the free space between the items. Three items have 2 gaps."),
            S("Size of each gap", math=r"300 \div 2 = 150 \text{ px}"),
            S("Start positions", math=r"0,\ 100 + 150 = 250,\ 250 + 100 + 150 = 500", text="The items start at 0, 250 and 500 px. The last item ends at 600 px, at the right edge."),
        ]),
        H("Flex items: grow, shrink and basis"),
        D("**flex-grow** says how much of the leftover space an item takes, as a share. **flex-shrink** says how much it shrinks if space is short. **flex-basis** is the starting size "
          "before growing or shrinking. The shorthand flex: 1 means grow 1, and the item shares leftover space equally with other flex: 1 items.", title="Definition"),
        CODE("""
.row { display: flex; gap: 20px; width: 800px; }
.a { flex: 1; }
.b { flex: 2; }
.c { flex: 1; }
""", "css", title="Listing 2", caption="Three items sharing space 1 : 2 : 1"),
        EX("Worked example 2: widths with flex 1, 2, 1", intro=(
            "Find the width of each item in Listing 2, whose container is 800 px wide with a gap of 20 px."), steps=[
            S("Remove the gaps", math=r"800 - 2 \times 20 = 760 \text{ px}", text="There are 2 gaps between 3 items."),
            S("Total shares", math=r"1 + 2 + 1 = 4"),
            S("One share", math=r"760 \div 4 = 190 \text{ px}"),
            S("Widths", math=r"190,\ 380,\ 190 \text{ px}", text="The items start at x = 0, 210 and 610."),
        ]),
        EX("Worked example 3: wrapping cards", intro=(
            "Cards use flex: 1 1 200px inside a flex container with flex-wrap: wrap, gap 10 px. Find the card width when the container is (a) 700 px wide, (b) 500 px wide. There are 3 cards."), steps=[
            S("Case a: how many fit?", math=r"3 \times 200 + 2 \times 10 = 620 \le 700", text="All three fit on one line."),
            S("Case a: share the leftover", math=r"700 - 620 = 80;\ 80 \div 3 = 26.7", text="Each card is 200 + 26.7 = 226.7 px wide."),
            S("Case b: how many fit?", math=r"2 \times 200 + 10 = 410 \le 500;\ 3 \times 200 + 20 = 620 > 500", text="Two cards fit; the third wraps to a new line."),
            S("Case b: widths", math=r"(500 - 10) \div 2 = 245", text="The first two cards are 245 px wide. The third card is alone on its line, so it grows to the full 500 px."),
        ]),
        T("The last point is a common surprise: a single card on the last line grows to full width because flexbox shares space only within each line. Grid, which you meet next, avoids this."),
        H("Flexbox or grid"),
        T("Use flexbox when you arrange items in one direction: a menu, a toolbar, a row of buttons, a card strip, or centring one item. Use grid when you control rows and columns together."),
        CODE("""
.center-box {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
}
""", "css", title="Listing 3", caption="Centring a child in both directions: in a 400 px by 200 px container a 100 px by 50 px child starts at x = 150, y = 75"),
        H("Common mistakes"),
        MISTAKE("Styling the wrong element", "display: flex goes on the parent. The properties for items, such as flex, go on the children."),
        MISTAKE("Confusing justify-content and align-items", "justify-content works along the main axis; align-items works across it. When flex-direction is column, they swap directions."),
        MISTAKE("Expecting wrap to happen by itself", "Without flex-wrap: wrap, items stay on one line and shrink, possibly overflowing."),
        QUIZ("In a row flex container, which property centres items vertically?",
             ["justify-content: center", "align-items: center", "flex-wrap: wrap", "gap: 0"], 1,
             "In a row, the vertical direction is the cross axis, controlled by align-items.",
             feedback=["justify-content works along the main axis, which is horizontal in a row.", "", "flex-wrap lets items move to new lines.", "gap sets the space between items."]),
        QUIZ("A 900 px wide flex container has three items with flex: 1, flex: 1 and flex: 2 and no gap. How wide is the item with flex: 2?",
             ["225 px", "300 px", "450 px", "600 px"], 2,
             "There are 4 shares in total. One share is 900 / 4 = 225 px, so the flex: 2 item is 450 px.",
             hint="Add up the shares first.",
             feedback=["That is one share.", "That divides by 3 as if all items were equal.", "", "That is two thirds of the container, which would need shares of 1, 1 and 4, not 1, 1 and 2."]),
        H("Practice questions"),
        PQ("State what the main axis and cross axis are in a flex container with flex-direction: row.",
           "The main axis runs horizontally, left to right, along the direction in which items are placed. The cross axis runs vertically, perpendicular to the main axis."),
        PQ("Write CSS to place three buttons in a row, spaced evenly with the first at the left edge and the last at the right edge, and centred vertically in a 60 px high bar.",
           ".bar { display: flex; justify-content: space-between; align-items: center; height: 60px; }"),
        PQ("A container is 1000 px wide with a gap of 20 px. It holds items with flex: 1, flex: 3 and flex: 1. Find the width of each item.",
           "Gaps: 2 x 20 = 40 px. Space = 960 px. Shares 1 + 3 + 1 = 5, so one share = 192 px. Widths: 192, 576 and 192 px."),
        PQ("Explain why flex-wrap: wrap is useful for a row of product cards on a phone.",
           "A phone screen is narrow. With wrap, cards that do not fit on one line move to the next line instead of being squeezed or overflowing, so the page remains readable without sideways scrolling."),
        SUM("display: flex makes a flex container whose children are flex items.",
            "The main axis follows flex-direction; justify-content works along it and align-items across it.",
            "flex: 1 shares leftover space equally; flex: 1 1 200px starts at 200 px, then grows and shrinks.",
            "Use gap for spacing and flex-wrap: wrap to allow new lines.",
            "Flexbox suits one-dimensional layouts; grid suits rows and columns together."),
    ]))

LESSONS.append(lesson(
    module=WEB, topic="Layout",
    title="CSS Grid: page layouts, fr units and responsive columns",
    slug="ic6-css-grid-responsive", minutes=24,
    summary="Build two-dimensional layouts with grid-template-columns, fr units, grid areas and spans, make columns respond to screen width with auto-fit and media queries, and calculate track sizes.",
    objectives=[
        "Define a grid container with columns, rows and gaps",
        "Calculate the size of fr tracks after fixed tracks and gaps are removed",
        "Place items with grid-column span and grid-template-areas",
        "Make a layout responsive with repeat(auto-fit, minmax()) and a media query",
    ],
    key_concepts=["Grid container", "Track", "fr unit", "repeat()", "minmax()", "grid-template-areas", "Span", "Media query", "Responsive design"],
    blocks=[
        H("Introduction"),
        T("A school website needs the classic page: a header across the top, a menu on the left, the main text on the right, and a footer across the bottom. On a phone, the same "
          "parts should simply stack one above the other. CSS Grid describes rows and columns together, so this layout is declared in a few lines and changed for phones with a small rule."),
        D("**CSS Grid** is a layout model that divides an element into rows and columns. Setting display: grid makes a **grid container**. The lines it is divided by form "
          "**tracks** (rows and columns), and the children are placed in the cells.", title="Definition"),
        H("Columns, fr and gap"),
        D("The **fr** unit is a share of the free space in the grid container. After fixed sizes and gaps are removed, the rest is divided between fr tracks in proportion to their numbers.", title="Definition"),
        CODE("""
.grid {
  display: grid;
  grid-template-columns: 200px 1fr 2fr;
  gap: 20px;
}
""", "css", title="Listing 1", caption="One fixed column and two flexible columns"),
        EX("Worked example 1: track sizes", intro=(
            "The container in Listing 1 is 900 px wide. Find the width of each column."), steps=[
            S("Remove the gaps", math=r"2 \times 20 = 40 \text{ px}"),
            S("Remove the fixed column", math=r"900 - 40 - 200 = 660 \text{ px free}"),
            S("Divide by the fr shares", math=r"660 \div (1 + 2) = 220 \text{ px per fr}"),
            S("Column widths", math=r"200,\ 220,\ 440 \text{ px}", text="The columns start at x = 0, 220 and 460."),
        ]),
        T("repeat(3, 1fr) is a short way to write three equal columns. An item can cover several columns with grid-column: span 2."),
        EX("Worked example 2: spanning", intro=(
            "The container is 620 px wide with grid-template-columns: repeat(3, 1fr) and gap: 10px. The first item has grid-column: span 2. How wide is that item and the item beside it?"), steps=[
            S("Column width", math=r"(620 - 2 \times 10) \div 3 = 200 \text{ px}"),
            S("Spanning item", math=r"2 \times 200 + 10 = 410 \text{ px}", text="It covers two columns and the gap between them."),
            S("Next item", text="The remaining column on the first row holds the second item, 200 px wide. The rest fill the next row in three 200 px cells."),
        ]),
        H("Named areas for a page layout"),
        IMG("al-ic6-grid-areas.svg", alt="A page grid with a header across the top, a nav column at the left, a main area, and a footer across the bottom, with the area names written in each cell.",
            caption="Figure 1. grid-template-areas for a page: header, nav, main and footer"),
        CODE("""
.page {
  display: grid;
  grid-template-columns: 220px 1fr;
  grid-template-areas:
    "head head"
    "nav  main"
    "foot foot";
  gap: 10px;
}
header { grid-area: head; }
nav    { grid-area: nav;  }
main   { grid-area: main; }
footer { grid-area: foot; }

@media (max-width: 600px) {
  .page {
    grid-template-columns: 1fr;
    grid-template-areas:
      "head"
      "nav"
      "main"
      "foot";
  }
}
""", "css", title="Listing 2", caption="Page layout that stacks on screens up to 600 px wide"),
        T("A **media query** applies its rules only when a condition is true, here a viewport at most 600 px wide. Changing the template areas "
          "is enough to reorder the page without touching the HTML."),
        EX("Worked example 3: read the layout", intro=(
            "Use Listing 2 with a viewport 1000 px wide, then 500 px wide. Describe where the nav and main sit and their widths. Take the page to fill the viewport width."), steps=[
            S("At 1000 px", text="The media query condition is false. Nav is the left column, 220 px wide. Main is in the second column."),
            S("Main width at 1000 px", math=r"1000 - 220 - 10 = 770 \text{ px}"),
            S("At 500 px", text="The condition is true. There is only one column, 500 px wide, so header, nav, main and footer are stacked and each is 500 px wide."),
        ]),
        H("Responsive columns without media queries"),
        CODE("""
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 10px;
}
""", "css", title="Listing 3", caption="As many columns of at least 160 px as will fit"),
        T("minmax(160px, 1fr) means each column is at least 160 px and at most one fraction of the free space. auto-fit puts in as many columns as fit, then shares any space left. "
          "With 4 cards: in a 1000 px container, 4 columns of 242.5 px; in a 500 px container, 3 columns of 160 px with the fourth card on a second row."),
        EX("Worked example 4: how many columns?", intro=(
            "A cards container is 700 px wide with Listing 3 rules. How many columns and how wide?"), steps=[
            S("Columns that fit", math=r"n \times 160 + (n - 1) \times 10 \le 700 \Rightarrow n \le \frac{710}{170} = 4.2", text="So n = 4."),
            S("Width of each", math=r"(700 - 3 \times 10) \div 4 = 167.5 \text{ px}"),
            S("Conclusion", text="Four columns of 167.5 px. A fifth card would start a new row."),
        ]),
        H("Grid or flexbox?"),
        KEY("Choose by the shape of the layout", "", cards=[
            ["Grid", "Two directions at once: page layouts, galleries and dashboards. You define the tracks first, then place items."],
            ["Flexbox", "One direction: menus, toolbars, rows of buttons. Items decide their own size, and extra items wrap."],
        ], note="They work together: a grid page layout can contain flexbox menus."),
        H("Common mistakes"),
        MISTAKE("Forgetting the viewport meta tag", "Without the viewport meta tag in the head, phones pretend to be wide screens and media queries do not behave as expected."),
        MISTAKE("Counting gaps wrongly", "n columns have n - 1 gaps. Remove them before sharing fr space."),
        MISTAKE("Using fixed pixel widths everywhere", "Fixed widths cause sideways scrolling on phones. Use fr, percentages and minmax."),
        QUIZ("A grid has grid-template-columns: 1fr 3fr and is 800 px wide with no gap. How wide is the second column?",
             ["200 px", "400 px", "600 px", "800 px"], 2,
             "One fr is 800 / 4 = 200 px, so the second column is 3 x 200 = 600 px.",
             feedback=["That is the first column.", "That divides equally as if the columns were 1fr 1fr.", "", "That is the whole container."]),
        QUIZ("What does repeat(auto-fit, minmax(150px, 1fr)) achieve?",
             ["Always exactly 150 px columns", "As many columns of at least 150 px as fit, sharing leftover space", "A single column on every screen", "Three equal columns"], 1,
             "auto-fit places as many columns as fit, each at least 150 px, and the columns share the extra space.",
             feedback=["The 1fr maximum lets columns grow.", "", "The number of columns increases with the screen width.", "Three equal columns would be repeat(3, 1fr)."]),
        H("Practice questions"),
        PQ("Write the CSS for a grid of three equal columns with a 15 px gap.",
           ".grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }"),
        PQ("A grid is 1000 px wide with grid-template-columns: 250px 1fr 1fr and gap 25px. Find the width of each column.",
           "Gaps: 2 x 25 = 50 px. Free space after the fixed column: 1000 - 50 - 250 = 700 px. Each 1fr = 350 px. Widths: 250, 350 and 350 px."),
        PQ("Explain the purpose of a media query with max-width: 600px in Listing 2.",
           "It applies the rules inside it only on screens up to 600 px wide. In Listing 2 it changes the page to a single column with the areas stacked, so the page is readable on a phone."),
        PQ("Give one situation where flexbox is the better choice than grid and one where grid is better.",
           "Flexbox: a navigation menu, where items sit in one row and are spaced along it. Grid: a whole page layout with header, sidebar, main and footer, where rows and columns are defined together."),
        SUM("Grid divides a container into rows and columns; display: grid on the parent.",
            "fr shares the free space after fixed tracks and gaps; n columns have n - 1 gaps.",
            "grid-template-areas names the parts of a page layout; span lets an item cover several tracks.",
            "repeat(auto-fit, minmax()) and media queries make layouts respond to screen width.",
            "Use the viewport meta tag, and combine grid for the page with flexbox for components."),
    ]))

# ===========================================================================
# Web Development / JavaScript
# ===========================================================================
LESSONS.append(lesson(
    module=WEB, topic="JavaScript",
    title="The DOM: selecting elements and changing text, styles and classes",
    slug="ic6-js-dom-select-change", minutes=22,
    summary="Explain the DOM as a tree, select elements with getElementById and querySelector, and change text, styles, classes and attributes, with outputs traced step by step.",
    objectives=[
        "Describe the DOM as a tree of nodes that JavaScript can read and change",
        "Select one or many elements with getElementById, querySelector and querySelectorAll",
        "Change text, style, classes and attributes of an element",
        "Explain why a script placed before its elements fails, and how to avoid it",
    ],
    key_concepts=["DOM", "Node", "document", "getElementById", "querySelector", "querySelectorAll", "textContent", "classList", "style"],
    blocks=[
        H("Introduction"),
        T("On a school results website, a message at the top of the page should change from Welcome to Welcome to KKEVO when the page loads, and the second note should turn red "
          "when an error is found. The browser can do this without loading a new page, because JavaScript can change the page while the user watches. The tool for this is the DOM."),
        D("The **DOM** (Document Object Model) is the browser's live model of an HTML page, organised as a tree of objects called **nodes**. Each element, attribute and piece of text is a node. "
          "JavaScript reads and changes the page by reading and changing the DOM. The root object is **document**.", title="Definition"),
        IMG("al-ic6-dom-tree.svg", alt="A tree. The document has an html node with head and body. The body has an h1 with id title, two p elements with class note, and a ul with id list containing two li elements.",
            caption="Figure 1. The DOM tree of the example page"),
        CODE("""
<h1 id="title">Welcome</h1>
<p class="note">First</p>
<p class="note">Second</p>
<ul id="list">
  <li>Rice</li>
  <li>Beans</li>
</ul>
""", "html", title="Listing 1", caption="The page used in all examples in this lesson"),
        H("Selecting elements"),
        KEY("Three ways to select", "", cards=[
            ["getElementById", "document.getElementById(\"title\") returns the element with that id, or null if there is none. Ids are unique."],
            ["querySelector", "document.querySelector(\"#list li\") returns the first element that matches any CSS selector, or null."],
            ["querySelectorAll", "document.querySelectorAll(\".note\") returns a list of all matching elements. Its length is in the length property; items are numbered from 0."],
        ]),
        T("Because querySelector uses CSS selectors, you already know the syntax: a dot for a class, a hash for an id, and a space for a descendant."),
        H("Changing the page"),
        CODE("""
const title = document.getElementById("title");
title.textContent = "Welcome to KKEVO";

const notes = document.querySelectorAll(".note");
console.log(notes.length);              // 2
notes[1].style.color = "red";
console.log(notes[1].style.color);      // red

console.log(document.querySelector("#list li").textContent);   // Rice

notes[0].classList.add("highlight");
console.log(notes[0].className);        // note highlight
notes[0].classList.toggle("highlight");
console.log(notes[0].className);        // note

title.setAttribute("title", "School portal");
""", "javascript", title="Listing 2", caption="Selecting and changing, with the output of each console.log (checked by running it in a browser)"),
        EX("Worked example 1: trace Listing 2", intro=(
            "Explain what each part of Listing 2 does and what it prints."), steps=[
            S("Change the heading", text="getElementById finds the h1. Setting textContent replaces its text, so the page now shows Welcome to KKEVO."),
            S("Select all notes", text="querySelectorAll(\".note\") returns both paragraphs. notes.length is 2. notes[0] is First and notes[1] is Second."),
            S("Change style", text="notes[1].style.color = \"red\" turns the second paragraph red. Reading it back prints red."),
            S("First list item", text="querySelector(\"#list li\") returns the first li inside the list, whose text is Rice."),
            S("Classes", text="classList.add adds highlight to the class list, which becomes note highlight. toggle removes it again because it is present, giving note."),
        ]),
        D("**textContent** reads or sets the plain text of an element. **style** changes one CSS property directly. **classList** (add, remove, toggle, contains) changes the classes, which is the better way "
          "to change a look, because the CSS stays in the stylesheet. **setAttribute** sets any attribute, such as src, href or title.", title="Definition"),
        H("Where to put the script"),
        T("JavaScript can only select elements that already exist. If the script is in the head, the browser runs it before the body is built, and getElementById returns null. "
          "Trying to read textContent of null gives an error: Cannot set properties of null. Put the script just before the closing body tag, or in the head with the defer attribute."),
        CODE("""
<body>
  ... all the page content ...
  <script src="app.js"></script>
</body>

<!-- or, in the head -->
<script src="app.js" defer></script>
""", "html", title="Listing 3", caption="Two safe places for the script"),
        EX("Worked example 2: why null?", intro=(
            "A script in the head contains document.getElementById(\"title\").textContent = \"Hi\". The console shows an error saying it cannot set properties of null. Explain and fix."), steps=[
            S("Find the cause", text="The script ran before the h1 existed, so getElementById returned null."),
            S("Fix 1", text="Move the script tag to just before the closing body tag."),
            S("Fix 2", text="Keep it in the head and add the defer attribute, which makes the browser wait until the page is parsed."),
            S("Check", text="Reload and look at the console. No error should appear and the heading should show Hi."),
        ]),
        EX("Worked example 3: highlight the long list items", intro=(
            "Write code to give the class low to every li in the list whose text is Beans."), steps=[
            S("Select all items", text="const items = document.querySelectorAll(\"#list li\");"),
            S("Loop", text="items.forEach(function (item) { ... });"),
            S("Test the text", text="Inside the loop: if (item.textContent === \"Beans\") { item.classList.add(\"low\"); }"),
            S("Result", text="Only the second item receives the class low."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using = instead of === in a test", "A single equals sign assigns a value. Compare with ===."),
        MISTAKE("Forgetting the index on querySelectorAll", "The result is a list. Use notes[0], or loop through it, to change one element."),
        MISTAKE("Putting the hash or dot in getElementById", "getElementById(\"title\") takes the id only. querySelector(\"#title\") takes the CSS selector."),
        QUIZ("Which call returns ALL elements with the class note?",
             ["document.getElementById(\"note\")", "document.querySelector(\".note\")", "document.querySelectorAll(\".note\")", "document.note"], 2,
             "querySelectorAll with a CSS selector returns every match.",
             feedback=["getElementById looks for an id and returns one element.", "querySelector returns only the first match.", "", "There is no such property."]),
        QUIZ("A script in the head runs document.getElementById(\"title\").textContent = \"Hi\" and fails. What is the most likely cause?",
             ["The h1 has too much text", "The script ran before the element existed", "textContent is a CSS property", "Browsers do not allow changing text"], 1,
             "The element was not yet in the page, so getElementById returned null.",
             feedback=["The length of the text is not the problem.", "", "textContent is a DOM property, not CSS.", "Changing text is allowed."]),
        H("Practice questions"),
        PQ("Define the DOM and say what the document object is.",
           "The DOM is the browser's tree-shaped model of an HTML page, in which every element, attribute and text is a node that JavaScript can read and change. "
           "document is the root object from which the page is reached."),
        PQ("Write JavaScript to change the text of the element with id total to 2900 FCFA and make it bold using a class named strong.",
           "const t = document.getElementById(\"total\"); t.textContent = \"2900 FCFA\"; t.classList.add(\"strong\"); The CSS .strong { font-weight: bold; } supplies the look."),
        PQ("State two differences between querySelector and querySelectorAll.",
           "querySelector returns the first matching element (or null); querySelectorAll returns a list of all matching elements, accessed by index or a loop."),
        PQ("Explain why classList.add is usually better than setting style properties one by one.",
           "The look is described in the CSS file, so changing a class changes many properties at once, keeps appearance and behaviour separate, and is easier to maintain and reverse with remove or toggle."),
        SUM("The DOM is the live tree of the page; document is its root.",
            "getElementById returns one element; querySelector the first match; querySelectorAll all matches.",
            "textContent changes text; classList and style change appearance; setAttribute changes attributes.",
            "A script can only select elements that already exist: place it at the end of body or use defer.",
            "Null means no element was found."),
    ]))

LESSONS.append(lesson(
    module=WEB, topic="JavaScript",
    title="Building and removing elements from data with JavaScript",
    slug="ic6-js-dom-create-remove", minutes=22,
    summary="Create list items from an array, add and remove elements, read data attributes, compute totals and avoid the security risk of innerHTML with user input.",
    objectives=[
        "Create elements with createElement and add them with appendChild",
        "Build a list or table from an array of objects with a loop",
        "Remove elements and read data attributes, remembering they are strings",
        "Explain why textContent is safer than innerHTML for user text",
    ],
    key_concepts=["createElement", "appendChild", "remove", "forEach", "dataset", "innerHTML", "Cross-site scripting"],
    blocks=[
        H("Introduction"),
        T("A trader in Mokolo keeps a price list in the JavaScript of a small web page. When prices change, she does not want to rewrite the HTML by hand. "
          "The page should build its price list from data, and a total should update when items are added or removed. This is how all modern web pages work."),
        H("Creating elements"),
        T("Three steps create a new element: make it, fill it, place it. createElement makes an element that is not yet in the page. Set its content. appendChild puts it at the end of a parent."),
        CODE("""
const list = document.getElementById("list");     // <ul> holding Rice and Beans

const li = document.createElement("li");          // 1. make
li.textContent = "Plantain";                      // 2. fill
list.appendChild(li);                             // 3. place
console.log(list.children.length);                // 3

list.firstElementChild.remove();                  // remove Rice
const names = [];
for (const item of list.children) { names.push(item.textContent); }
console.log(names.join(","));                     // Beans,Plantain
""", "javascript", title="Listing 1", caption="Adding and removing a list item (checked by running it in a browser)"),
        EX("Worked example 1: trace Listing 1", intro=(
            "The list starts as Rice, Beans. Give the length and content after each step."), steps=[
            S("Before", text="Two children: Rice, Beans."),
            S("After appendChild", text="Three children: Rice, Beans, Plantain. list.children.length prints 3."),
            S("After remove", text="firstElementChild is Rice. Removing it leaves Beans, Plantain, so two children."),
            S("Output", text="The join prints Beans,Plantain."),
        ]),
        H("Building from an array"),
        CODE("""
const items = [
  { name: "Rice",  price: 600 },
  { name: "Beans", price: 800 },
  { name: "Oil",   price: 1500 }
];

const ul = document.getElementById("list");
ul.textContent = "";                              // clear the old list

items.forEach(function (it) {
  const row = document.createElement("li");
  row.textContent = it.name + ": " + it.price + " FCFA";
  ul.appendChild(row);
});

const sum = items.reduce(function (s, i) { return s + i.price; }, 0);
console.log(sum);                                 // 2900
""", "javascript", title="Listing 2", caption="One list item for each object in the array"),
        EX("Worked example 2: what appears on the page", intro=(
            "Give the text of each list item built by Listing 2 and the printed total."), steps=[
            S("Clear", text="Setting ul.textContent to an empty string removes the old children."),
            S("Loop", text="forEach runs the function once for each object, in order."),
            S("Items", text="Rice: 600 FCFA, Beans: 800 FCFA, Oil: 1500 FCFA."),
            S("Total", math=r"0 + 600 + 800 + 1500 = 2900", text="reduce adds the prices, starting from 0, so 2900 is printed."),
        ]),
        H("Data attributes are strings"),
        T("Information can be attached to an element with a data attribute, for example data-price=\"600\". JavaScript reads it from the dataset property. "
          "The value is always a **string**, so convert it with Number() before calculating."),
        CODE("""
<ul id="cart">
  <li data-price="600">Rice</li>
  <li data-price="800">Beans</li>
  <li data-price="1500">Oil</li>
</ul>
<p id="total"></p>

<script>
const cart = document.getElementById("cart");
let total = 0;
cart.querySelectorAll("li").forEach(function (item) {
  total += Number(item.dataset.price);
});
document.getElementById("total").textContent = "Total: " + total + " FCFA";
</script>
""", "html", title="Listing 3", caption="Totals from data attributes. The paragraph shows: Total: 2900 FCFA"),
        EX("Worked example 3: the string trap", intro=(
            "Without Number(), what would item.dataset.price + 1 give for the first item, and why?"), steps=[
            S("Type", text="dataset.price is the string \"600\"."),
            S("Plus with a string", text="When one side is a string, + joins text instead of adding."),
            S("Result", text="\"600\" + 1 is the string \"6001\". With Number(): 600 + 1 gives 601."),
        ]),
        H("textContent and innerHTML"),
        D("**innerHTML** sets the HTML inside an element: the text is parsed as markup. **textContent** treats everything as plain text. If text typed by a user is placed with innerHTML, "
          "a user could insert a script or markup that changes the page for others. This attack is called **cross-site scripting (XSS)**. Use textContent for user text.", title="Definition"),
        KEY("A safe habit", "", cards=[
            ["Safe", "li.textContent = userInput;   The input is shown as text, whatever it contains."],
            ["Risky", "li.innerHTML = userInput;   The input is treated as HTML and may be used to attack other users."],
        ]),
        H("Common mistakes"),
        MISTAKE("Adding the same element to two parents", "An element exists in one place. appendChild moves it. Create a new element for each place."),
        MISTAKE("Forgetting to clear the list before rebuilding", "If you do not empty it first, the new items are added after the old ones and you see duplicates."),
        MISTAKE("Doing arithmetic on dataset values", "dataset values are text. Convert with Number() or parseInt() first."),
        QUIZ("What is the correct order to add a new list item to a page?",
             ["appendChild, createElement, set text", "createElement, set text, appendChild", "set text, appendChild, createElement", "createElement, appendChild, remove"], 1,
             "Make the element, fill it, then place it in the page.",
             feedback=["You cannot append an element that does not exist yet.", "", "There is nothing to set text on before the element is created.", "remove would delete the item you just added."]),
        QUIZ("The first li has data-price=\"600\". What does item.dataset.price + 1 evaluate to?",
             ["601", "\"6001\"", "NaN", "undefined"], 1,
             "dataset values are strings, so + joins them: \"600\" and 1 give the text \"6001\".",
             hint="What type is a data attribute value?",
             feedback=["That would be right only after Number() is used.", "", "NaN happens when a non-number is used in arithmetic such as subtraction of text that is not numeric.", "The attribute exists, so a value is returned."]),
        H("Practice questions"),
        PQ("Write JavaScript that adds a list item with the text Salt to the ul with id list.",
           "const li = document.createElement(\"li\"); li.textContent = \"Salt\"; document.getElementById(\"list\").appendChild(li);"),
        PQ("An array holds names: [\"Aisha\", \"Paul\", \"Ngwa\"]. Write code to display each name as a paragraph inside a div with id roll.",
           "const roll = document.getElementById(\"roll\"); names.forEach(function (n) { const p = document.createElement(\"p\"); p.textContent = n; roll.appendChild(p); });"),
        PQ("Prices of 500, 750 and 1250 are stored as data-price on three elements. State the total calculated with the loop in Listing 3, and the result if Number() is left out and total starts at 0.",
           "With Number(): 500 + 750 + 1250 = 2500. Without Number(): 0 + \"500\" gives the string \"0500\", then adding \"750\" gives \"0500750\", and adding \"1250\" gives \"05007501250\". The result is text, not a total."),
        PQ("Explain why using textContent is safer than innerHTML when displaying a visitor's comment.",
           "textContent shows the comment as plain text, so any tags in it appear as text and do not run. innerHTML would treat the comment as HTML, allowing a visitor to inject markup or script that attacks other users (cross-site scripting)."),
        SUM("Create, fill, place: createElement, textContent, appendChild.",
            "Build lists from arrays with forEach, and sum with reduce.",
            "remove() deletes an element. Clear a list before rebuilding it.",
            "dataset values are strings: use Number() before arithmetic.",
            "Use textContent, not innerHTML, for text typed by users."),
    ]))

LESSONS.append(lesson(
    module=WEB, topic="JavaScript",
    title="Events and form validation in JavaScript",
    slug="ic6-js-events-forms", minutes=24,
    summary="Respond to clicks, typing and form submission with addEventListener, validate a form before it is sent with preventDefault, and handle clicks on many items with event delegation.",
    objectives=[
        "Attach event listeners and use the event object",
        "Update the page when the user clicks or types",
        "Validate a form on submit and stop sending it when it has errors",
        "Use event delegation to handle clicks on many list items with one listener",
    ],
    key_concepts=["Event", "addEventListener", "Event object", "preventDefault", "Form validation", "Regular expression", "Event delegation", "Server-side validation"],
    blocks=[
        H("Introduction"),
        T("A registration form for an inter-school quiz collects a name and a phone number. A student mistypes the phone number and only learns about it after waiting for the server on a slow connection. "
          "A good page checks the entries in the browser first and shows a clear message at once. This needs events."),
        D("An **event** is something that happens on the page that code can react to: a click, a key press, typing in a field, a form being submitted. An **event listener** is a function "
          "registered with addEventListener that the browser calls when that event happens on that element.", title="Definition"),
        H("Click and input events"),
        CODE("""
<button id="add">Add</button> <span id="count">0</span>
<textarea id="text"></textarea> <span id="chars">0</span>

<script>
const btn = document.getElementById("add");
let count = 0;
btn.addEventListener("click", function () {
  count++;
  document.getElementById("count").textContent = count;
});

const ta = document.getElementById("text");
ta.addEventListener("input", function () {
  document.getElementById("chars").textContent = ta.value.length;
});
</script>
""", "html", title="Listing 1", caption="A click counter and a live character count"),
        EX("Worked example 1: trace Listing 1", intro=(
            "The user clicks the button three times, then types Hello in the text area. What do the two spans show?"), steps=[
            S("Click 1", text="count becomes 1 and the span shows 1."),
            S("Clicks 2 and 3", text="count becomes 2 and then 3. The span shows 3."),
            S("Typing", text="Each keystroke fires an input event. After Hello is typed, ta.value.length is 5."),
            S("Result", text="The spans show 3 and 5."),
        ]),
        H("Validating a form"),
        T("A form sends its data when the user presses the submit button. The **submit** event fires first. If the code calls **event.preventDefault()**, the browser does not send the form. "
          "The code can then show error messages and let the user correct them."),
        CODE(r"""
<form id="reg" action="thanks.html">
  <input name="name">
  <input name="phone">
  <p id="msg"></p>
  <button type="submit">Send</button>
</form>

<script>
const form = document.getElementById("reg");
const msg = document.getElementById("msg");

form.addEventListener("submit", function (e) {
  const name = form.elements["name"].value.trim();
  const phone = form.elements["phone"].value.trim();
  const errors = [];

  if (name === "") {
    errors.push("Name is required");
  }
  if (!/^6\d{8}$/.test(phone)) {
    errors.push("Phone must be 9 digits starting with 6");
  }
  if (errors.length > 0) {
    e.preventDefault();
    msg.textContent = errors.join(". ");
  }
});
</script>
""", "html", title="Listing 2", caption="Form validation. The pattern means: start, the digit 6, exactly 8 more digits, end."),
        T("trim() removes spaces from both ends. The pattern between the slashes is a regular expression: the text must start (the caret), then the digit 6, then exactly eight digits (backslash d, with the number 8 in braces), then end (the dollar sign). "
          "regex.test(text) gives true or false. The exclamation mark in front reverses the test, so the error is added when the phone does not match."),
        EX("Worked example 2: test four inputs", intro=(
            "Predict the message for each pair (name, phone) in Listing 2: (1) empty name and 12345; (2) Amina and 677123456; (3) Amina and 77123456; (4) the name Paul with spaces around it and 612345678."), steps=[
            S("Input 1", text="Name is empty, so the first error. 12345 does not match. Both errors are shown: Name is required. Phone must be 9 digits starting with 6. The form is not sent."),
            S("Input 2", text="677123456 starts with 6 and has 8 more digits, so it is valid. The name is present. No errors, so the form is sent."),
            S("Input 3", text="77123456 is 8 digits and starts with 7. Only the phone error is shown, and the form is not sent."),
            S("Input 4", text="trim() removes the spaces around Paul. 612345678 is valid. No errors."),
        ]),
        KEY("Client-side checks are not enough", "", cards=[
            ["Why check in the browser", "It is fast and gives help at once, which is especially useful when the connection is slow."],
            ["Why also check on the server", "A user can switch off JavaScript or send data without the form. The server must repeat every check, because browser checks can be bypassed."],
        ]),
        H("Event delegation"),
        T("If a list has many items and each needs a click action, adding a listener to every item is wasteful and fails for items added later. "
          "Instead, add one listener to the parent. Events bubble up from the clicked item to its parents, and e.target tells which element was clicked."),
        CODE("""
<ul id="todo">
  <li>Wash</li><li>Cook</li><li>Study</li>
</ul>

<script>
const todo = document.getElementById("todo");
todo.addEventListener("click", function (e) {
  if (e.target.tagName === "LI") {
    e.target.classList.toggle("done");
  }
});
</script>
""", "html", title="Listing 3", caption="One listener for every list item, including ones added later"),
        EX("Worked example 3: trace Listing 3", intro=(
            "The user clicks Cook once, then clicks Cook again. What are the classes of the three items after each click?"), steps=[
            S("Start", text="All three have no class."),
            S("First click on Cook", text="The click bubbles to the ul. e.target is the second li, so tagName is LI. toggle adds done. Classes: none, done, none."),
            S("Second click on Cook", text="toggle removes done, because it is present. Classes: none, none, none."),
            S("Click between the items", text="If the click lands on the ul itself, tagName is UL, the condition is false and nothing happens."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling the function instead of passing it", "addEventListener(\"click\", doIt) passes the function. doIt() would run it at once and pass its result."),
        MISTAKE("Forgetting preventDefault", "Without it, the form is sent even when errors were found, and the message flashes and disappears as the page reloads."),
        MISTAKE("Trusting only browser validation", "Always validate on the server as well."),
        QUIZ("What does event.preventDefault() do in a submit handler?",
             ["Sends the form faster", "Stops the browser's normal action, so the form is not sent", "Deletes the form", "Reloads the page"], 1,
             "preventDefault cancels the default action of the event; for a submit event, the sending of the form.",
             feedback=["It stops the sending; it does not speed it up.", "", "The form stays in the page.", "Reloading would be the result if the form were sent to the same page."]),
        QUIZ("Why can the server not rely on browser validation alone?",
             ["Browsers cannot test numbers", "A user can bypass the browser by turning off JavaScript or sending the data some other way", "Servers are faster", "Validation is illegal in JavaScript"], 1,
             "Anyone can send data to a server without using the form, so the server must check again.",
             feedback=["JavaScript can test numbers well.", "", "Speed is not the reason.", "JavaScript validation is allowed and common."]),
        H("Practice questions"),
        PQ("Write JavaScript so that when the button with id hello is clicked, the paragraph with id out shows Hello.",
           "document.getElementById(\"hello\").addEventListener(\"click\", function () { document.getElementById(\"out\").textContent = \"Hello\"; });"),
        PQ("A form has a field age. Write the code for a submit handler that blocks sending if the age is not between 15 and 25 and shows Age must be 15 to 25 in a paragraph with id msg.",
           "form.addEventListener(\"submit\", function (e) { const age = Number(form.elements[\"age\"].value); if (age < 15 || age > 25) { e.preventDefault(); document.getElementById(\"msg\").textContent = \"Age must be 15 to 25\"; } }); "
           "Note: an empty field gives Number(\"\") = 0, which is also rejected."),
        PQ("Using the rule in Listing 2, state whether each phone number is accepted: 655443322, 755443322, 65544332, 6554433221.",
           "655443322: accepted (starts with 6, 9 digits). 755443322: rejected (starts with 7). 65544332: rejected (only 8 digits). 6554433221: rejected (10 digits; the pattern needs exactly 9)."),
        PQ("Explain what event delegation is and give one advantage.",
           "Event delegation uses a single listener on a parent element to handle events from its children, found with e.target as events bubble up. Advantage: fewer listeners, and it works for items added after the page loaded."),
        SUM("Events are reactions to user actions; addEventListener registers a function for an event.",
            "The input event fires as the user types; click fires on clicks; submit fires before a form is sent.",
            "preventDefault() stops the form being sent, so errors can be shown.",
            "Validate with trim, comparisons and regular expressions, and always validate again on the server.",
            "Event delegation: one listener on the parent, using e.target."),
    ]))

# ===========================================================================
# Examination / Practice paper
# ===========================================================================
LESSONS.append(lesson(
    module="Examination", topic="Practice paper",
    title="Approaching the Lower Sixth ICT practice paper: time, method and formulas",
    slug="ic6-exam-practice-paper-approach", minutes=20,
    summary="Plan your time on a 40-question multiple-choice practice paper, use elimination and quick checks on calculation questions, and revise the key formulas and traps from every topic of the year.",
    objectives=[
        "Plan the time for a 40-question, 90-minute practice paper in three passes",
        "Use elimination and working checks to choose between four options",
        "Recall the key formulas and procedures from all Lower Sixth ICT topics",
        "Review a mock result by topic and decide what to revise next",
    ],
    key_concepts=["Time plan", "Three-pass method", "Elimination", "Formula recall", "Topic review", "Common traps"],
    blocks=[
        H("Introduction"),
        T("This lesson prepares you for the KKEVO practice paper for Lower Sixth ICT. The practice paper has 40 four-option multiple-choice questions across all the topics of the year, "
          "and it is set for 90 minutes in the practice system. The real examination format, the number of papers and the timing must be checked with your teacher or your school. "
          "The timings in this lesson are KKEVO practice settings and KKEVO advice, not official figures."),
        T("In the real exam, ICT questions can be multiple choice, structured questions and practical tasks, depending on the paper. In the practice, you train the habits that help in all of them: "
          "plan your time, read carefully, and check your work."),
        H("Time plan (KKEVO advice)"),
        KEY("Three passes in 90 minutes", "A suggestion for the practice setting.", cards=[
            ["Pass 1: 60 minutes", "Go through all 40 questions once. About 90 seconds each. Answer what you know and mark any question that needs a long calculation or that you doubt."],
            ["Pass 2: 20 minutes", "Return to the marked questions. Use the longer time for calculations and tracing."],
            ["Pass 3: 10 minutes", "Check that every question has an answer. Re-read two or three calculations. Do not change an answer without a clear reason."],
        ]),
        EX("Worked example 1: the time budget", intro=(
            "Check that the plan fits the 90 minutes, and find the average time per question if the paper has 40 questions and you use the whole time."), steps=[
            S("Add the passes", math=r"60 + 20 + 10 = 90 \text{ minutes}"),
            S("Average per question", math=r"90 \div 40 = 2.25 \text{ minutes} = 2 \text{ min } 15 \text{ s}"),
            S("First pass rate", math=r"60 \times 60 \div 40 = 90 \text{ seconds}", text="So the first pass is quicker than the average. Fast answers on easy questions leave time for the hard ones."),
        ]),
        H("Method for each question"),
        KEY("Read, decide, check", "", cards=[
            ["Read the stem", "Underline what is asked: which, not, best, most likely, calculate. Many errors come from missing the word NOT."],
            ["Try before looking", "Think of the answer before reading the options, so a tempting wrong option does not steer you."],
            ["Eliminate", "Cross out options that are wrong for a clear reason. Distractors are often real mistakes, such as a wrong unit, upside-down fraction or a wrong axis."],
            ["Check", "For a calculation, check the unit and the size of the answer. For code, trace it with the given data."],
        ]),
        EX("Worked example 2: a calculation with eliminated options", intro=(
            "Two DDR4-3200 modules run in dual channel. What is the theoretical bandwidth? Options: 25.6 GB/s, 51.2 GB/s, 12.8 GB/s, 102.4 GB/s."), steps=[
            S("Try first", math=r"3200 \times 8 \times 2 = 51\,200 \text{ MB/s}", text="That is 51.2 GB/s."),
            S("Eliminate", text="25.6 GB/s is the single-channel value. 12.8 GB/s would be a lower rate. 102.4 GB/s is double the correct figure."),
            S("Choose", text="51.2 GB/s. The three wrong options come from missing the channels, mistaking the rate, or doubling twice."),
        ]),
        EX("Worked example 3: tracing a trigger", intro=(
            "Product stock is 20. A trigger reduces stock after each insert into sales. Sales of 5 and 8 are inserted. What is the stock? Options: 7, 12, 15, 33."), steps=[
            S("Try first", math=r"20 - 5 - 8 = 7"),
            S("Eliminate", text="12 only subtracts 8. 15 only subtracts 5. 33 adds the sales."),
            S("Choose", text="7. Tracing step by step catches the slips that the wrong options are designed around."),
        ]),
        H("Formula and procedure sheet for the year"),
        KEY("Hardware and deployment", "", cards=[
            ["Memory bandwidth", "MT/s x 8 bytes x channels, divided by 1000 for GB/s."],
            ["MBR limit", "2 to the 32 sectors x 512 bytes = 2 TiB (16 TiB with 4096-byte sectors)."],
            ["Slack space", "Round the clusters up, multiply by the cluster size, subtract the file size."],
            ["VM capacity", "(Host RAM - host share) divided by RAM per VM; also check disk; take the smaller."],
        ]),
        KEY("Enterprise infrastructure", "", cards=[
            ["Net income", "Gross income minus fees, delivery and other costs."],
            ["VoIP bandwidth", "Payload = rate x interval / 8; add 40 bytes; x 8 x packets per second."],
            ["Energy", "kWh = watts x hours / 1000; cost = kWh x price."],
            ["PUE", "Total facility power divided by IT power."],
            ["Triggers", "BEFORE can reject; AFTER reacts. NEW for insert and update, OLD for update and delete."],
        ]),
        KEY("Web development", "", cards=[
            ["Flexbox", "Free space after gaps, divided by the total of the flex shares."],
            ["Grid", "Free space after gaps and fixed columns, divided by the fr shares. n columns have n - 1 gaps."],
            ["DOM", "Select, then change. Scripts need the elements to exist first. dataset values are strings."],
            ["Events", "addEventListener with the function; preventDefault on submit when there are errors."],
        ]),
        H("Common traps"),
        MISTAKE("Mixing units", "Watts and kilowatt-hours, MB and GB, bits and bytes, TB and TiB. Write the unit in each step."),
        MISTAKE("Rounding the wrong way", "Clusters and VMs must be whole numbers. Think whether to round up (clusters) or down (VMs that fit)."),
        MISTAKE("Spending too long on one question", "If a question has taken more than three minutes, mark it, make your best guess and move on."),
        H("Using your mock result"),
        T("After the mock, the results page shows your score by topic. Revise the topic with the lowest score first, then do its practice set again. "
          "Read the explanation of every option you got wrong, because the wrong options are the real mistakes that examiners expect."),
        QUIZ("A 40-question paper is set for 90 minutes. Which first-pass plan leaves time for review?",
             ["Spend 2 minutes 15 seconds on every question and finish exactly at 90 minutes", "Spend about 90 seconds on each question, marking difficult ones, then return to them", "Answer only the first 20 questions", "Skip all calculations"], 1,
             "A quick first pass banks time for the hard questions and for checking.",
             feedback=["That leaves no time for checking or for hard questions.", "",
                       "Unanswered questions score nothing.", "Calculations can be learned and are often the easiest marks when checked."]),
        QUIZ("A calculation question has options 25.6, 51.2, 12.8 and 102.4. You worked out 51.2. What is the best next step?",
             ["Choose 25.6 because it is first", "Check the unit and that the answer matches your working, then choose 51.2", "Leave it blank", "Change to 102.4 because bigger is safer"], 1,
             "Check the unit and the working, then commit. Do not change an answer without a reason.",
             feedback=["The position of an option has no meaning.", "", "Never leave a question blank.", "Bigger is not safer; it is the doubled-twice error."]),
        H("Practice questions"),
        PQ("A 40-question paper lasts 90 minutes. Find the average time per question in minutes and seconds.",
           "90 / 40 = 2.25 minutes, which is 2 minutes 15 seconds."),
        PQ("List the three passes of the KKEVO time plan and the minutes for each.",
           "Pass 1: 60 minutes, first full run, marking hard questions. Pass 2: 20 minutes on marked questions. Pass 3: 10 minutes to check that all are answered and to re-read two or three calculations."),
        PQ("An answer option is 1.5 and the working gave PUE = 90 divided by 60. Explain how you check that the option is correct.",
           "PUE is total power divided by IT power, so 90 / 60 = 1.5, which is more than 1, as PUE always is. The unit is a plain ratio. The option 0.67 would be the upside-down fraction and can be eliminated."),
        PQ("Choose the first topic to revise if your mock result shows: PC hardware 5 of 6, OS deployment 3 of 6, Business technologies 6 of 7, Green computing 4 of 5, Database automation 2 of 5, Layout 5 of 6, JavaScript 4 of 5. Explain.",
           "Database automation, with 2 of 5, which is 40 percent, the lowest share. OS deployment is 3 of 6, which is 50 percent. Revise Database automation first, then OS deployment."),
        SUM("Check the real exam format with your teacher; the timings here are KKEVO practice settings.",
            "Use three passes: 60 minutes for a quick first pass, 20 for marked questions, 10 for checking.",
            "Read the stem, try before looking at the options, eliminate, and check units and working.",
            "Keep the formula sheet in mind: bandwidth, MBR limit, slack, VM capacity, net income, VoIP, energy, PUE, flex and grid widths.",
            "After a mock, revise the weakest topic first and read every wrong-option explanation."),
    ]))
