"""ICT A Level (796), Lower Sixth: draft lessons for every topic in the outline."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "lower-sixth")

LESSONS = []

# ---------------------------------------------------------------------------
# Hardware Maintenance & Deployment / PC hardware
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Hardware Maintenance & Deployment",
    topic="PC hardware",
    title="PC hardware: sockets, dual-channel RAM, BIOS/UEFI and POST diagnostics",
    slug="pc-hardware-sockets-ram-uefi-post",
    minutes=30,
    summary="Match CPUs to sockets, install RAM in dual-channel mode, configure BIOS/UEFI settings and use POST "
            "beeps and on-screen messages to diagnose a PC that will not boot.",
    objectives=[
        "Explain what a CPU socket is and why a processor must match the motherboard socket and chipset",
        "Install memory modules so that they run in dual-channel mode",
        "Describe the role of BIOS/UEFI firmware and change common setup options safely",
        "Use the POST sequence, beep codes and error messages to diagnose boot failures step by step",
    ],
    key_concepts=["CPU socket", "LGA and PGA", "Dual-channel memory", "BIOS", "UEFI", "Secure Boot",
                  "POST", "Beep code", "Boot order"],
    blocks=[
        H("Introduction"),
        T("Imagine you run a cyber café in Buea with twelve desktop computers. After a power cut, two machines "
          "refuse to start. One beeps and shows nothing on the screen. The other shows a message about a missing "
          "boot device. Customers are waiting and every hour of downtime costs you money."),
        T("A good technician does not guess. They know what is inside the system unit, they know the order in which "
          "a PC starts, and they follow a logical method to find the fault. This lesson gives you that knowledge."),
        H("CPU sockets"),
        D("A **CPU socket** is the connector on the motherboard that holds the processor and links its pins or pads "
          "to the rest of the board. A processor will only work in a socket designed for it, and the motherboard "
          "chipset and firmware must also support that processor.", title="Definition"),
        KEY("Two main socket designs", "Sockets differ in where the pins are.", cards=[
            ["LGA (Land Grid Array)", "The pins are in the socket on the motherboard. The CPU has flat contact pads. "
             "Bent socket pins are the main risk, so keep the plastic cover on until you fit the CPU."],
            ["PGA (Pin Grid Array)", "The pins are on the underside of the CPU and fit into holes in the socket. "
             "Bent CPU pins are the main risk. A ZIF lever releases the grip so the CPU drops in without force."],
        ], note="Intel and AMD each use their own socket families, and these change between generations. Always check "
                "the motherboard maker's CPU support list before buying."),
        TIP("Line up the small triangle on the corner of the CPU with the matching mark on the socket. A CPU never needs "
            "force. Thermal paste and a correctly mounted cooler are required before power-on, or the CPU will overheat "
            "and shut down within seconds."),
        H("Dual-channel RAM"),
        D("In **dual-channel** mode the memory controller talks to two memory modules at the same time over two "
          "separate 64-bit channels. This doubles the theoretical bandwidth compared with one module in "
          "single-channel mode.", title="Definition",
          note="Best results come from a matched pair: same capacity, same speed and same type (for example two DDR4 "
               "modules of the same speed). DDR4 and DDR5 slots are keyed differently, so the wrong type will not fit."),
        EX("Worked example 1: installing RAM in dual-channel mode", intro=(
            "A client in Douala brings a PC with one 8 GB module in slot A1. The motherboard has four slots labelled "
            "A1, A2, B1, B2 and its manual recommends A2 and B2 for two modules. The client buys a second identical "
            "8 GB module. How should you install it?"), steps=[
            S("Power down safely", text="Shut down, switch off at the wall, unplug, and press the power button to drain "
              "remaining charge. Wear an anti-static wrist strap clipped to the bare metal of the case."),
            S("Read the manual", text="Dual channel needs one module in each channel. Here the recommended pair is A2 and B2."),
            S("Move the first module", text="Open the slot clips, remove the module from A1 and fit it in A2. Line up the "
              "notch with the key in the slot."),
            S("Fit the second module", text="Insert the new module into B2 and press evenly on both ends until the clips snap shut."),
            S("Check in firmware", text="Power on, enter BIOS/UEFI setup and confirm the total is 16 GB and the memory mode "
              "shows dual channel. The result: 16 GB running in dual-channel mode."),
        ]),
        H("BIOS and UEFI firmware"),
        D("**BIOS** (Basic Input/Output System) is the older firmware stored on a chip on the motherboard. It tests the "
          "hardware and loads the operating system from an MBR disk. **UEFI** (Unified Extensible Firmware Interface) is "
          "its modern replacement. UEFI supports GPT disks larger than 2 TB, a graphical setup with mouse support, faster "
          "start-up and **Secure Boot**, which only loads boot software that has a trusted digital signature.",
          title="Definition"),
        T("Common setup options you will change: the boot order (which device is tried first), the date and time, enabling "
          "or disabling Secure Boot and CSM (legacy BIOS compatibility), enabling virtualization support for virtual "
          "machines, setting a setup password, and loading optimized defaults if settings have been corrupted."),
        T("Settings are kept in a small amount of non-volatile memory. On many boards a coin cell battery keeps the real-time "
          "clock running when the PC is unplugged. If the date resets to an old value every morning, the battery is the first suspect."),
        H("POST and boot diagnostics"),
        D("**POST** (Power-On Self-Test) is the set of checks the firmware runs every time the PC is switched on. It tests "
          "the CPU, memory, graphics and key controllers before looking for a bootable device. If POST finds a fault "
          "before the screen works, it reports it with **beep codes** or diagnostic LEDs.", title="Definition",
          note="Beep code meanings differ between firmware makers and motherboard models. Always look up the pattern in "
               "the motherboard manual instead of memorising one list."),
        EX("Worked example 2: a PC that beeps and shows no picture", intro=(
            "After a power cut in the Buea cyber café, a PC powers on, the fans spin, it gives a repeating pattern of "
            "beeps and the monitor stays black. Diagnose the fault."), steps=[
            S("Confirm power reaches the PC", text="Fans spinning and beeping show the power supply and motherboard are alive. "
              "The fault is not a dead PSU."),
            S("Look up the beep pattern", text="Count the beeps and check the manual. On many boards a repeating pattern at "
              "this stage points to a memory problem."),
            S("Reseat the RAM", text="Power off and unplug. Remove the modules, clean the gold contacts gently with a dry cloth "
              "or eraser, and reinsert them firmly until the clips lock."),
            S("Test one module at a time", text="If the beeps continue, try each module alone in the first recommended slot. "
              "A module that always fails is faulty."),
            S("Conclude", text="If the PC passes POST with one module, replace the faulty module. If no module works, test a "
              "known-good module or suspect the slot or board."),
        ]),
        EX("Worked example 3: POST passes but there is no operating system", intro=(
            "A second PC shows the maker's logo, then the message that no bootable device was found. Diagnose it."), steps=[
            S("Note what works", text="The logo appears, so POST, the CPU, RAM and graphics are fine. The problem is finding or "
              "loading the operating system."),
            S("Check detection", text="Enter setup. Is the SSD or hard disk listed? If not, power off and reseat its data and "
              "power cables, or test it in another PC."),
            S("Check the boot order", text="If the disk is detected, make sure it is first in the boot order and that a USB "
              "stick left in a port is not being tried first."),
            S("Check the boot mode", text="A disk installed in UEFI mode on a GPT disk will not boot if CSM or legacy mode has "
              "been switched on, and the reverse. Restore the original mode."),
            S("Conclude", text="If the disk is detected and the settings are correct but it still fails, the boot loader is "
              "damaged. Repair it with the OS installation media, or restore from backup."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up beep codes from different makers", "A pattern that means memory on one board can mean graphics "
                "on another. Always use the manual for that exact motherboard."),
        MISTAKE("Filling the wrong slots for dual channel", "Two modules side by side in A1 and A2 are often in the same "
                "channel and run in single-channel mode. Follow the manual's slot order."),
        MISTAKE("Working on a live PC", "Removing parts with the power cable connected can damage components. Unplug, drain "
                "the charge and use an anti-static strap."),
        QUIZ("A PC passes POST and shows the logo, but then reports that no boot device was found. Which component is "
             "the LEAST likely cause?",
             ["The RAM", "The SSD data cable", "The boot order in UEFI setup", "A boot mode change from UEFI to legacy"], 0,
             "The PC completed POST and displayed the logo, so the RAM was tested and is working. The fault is in finding "
             "or loading the operating system.",
             hint="Which parts must already be working for the logo to appear?",
             feedback=["", "A loose data cable means the disk is not detected, which causes exactly this message.",
                       "If another device is tried first or the disk is missing from the list, this message appears.",
                       "A boot mode mismatch stops the firmware from finding the boot loader on the disk."]),
        QUIZ("Which statement about UEFI is correct?",
             ["It can only boot from disks smaller than 2 TB", "It supports Secure Boot and GPT disks",
              "It is stored on the hard disk", "It replaces the need for an operating system"], 1,
             "UEFI supports GPT, which allows disks far larger than 2 TB, and Secure Boot, which checks boot software signatures.",
             feedback=["That limit applies to MBR partitioning used with legacy BIOS, not to UEFI with GPT.", "",
                       "UEFI firmware is stored on a chip on the motherboard, not on the disk.",
                       "Firmware only starts the hardware and loads the operating system. It does not replace it."]),
        H("Practice questions"),
        PQ("(a) State two differences between an LGA and a PGA socket. (b) Give one precaution when fitting a CPU.",
           "(a) In LGA the pins are in the motherboard socket and the CPU has flat pads; in PGA the pins are on the CPU and "
           "fit into holes in the socket. With LGA the risk is bent socket pins; with PGA the risk is bent CPU pins. "
           "(b) Any one: align the triangle marker; never force the CPU; apply thermal paste and fit the cooler before power-on; "
           "use an anti-static strap."),
        PQ("A user installs two identical 4 GB modules but the system reports single-channel mode. Explain the likely cause "
           "and how to fix it.",
           "The modules are probably in two slots of the same channel (for example A1 and A2). Dual channel needs one module "
           "in each channel. Power off, unplug and move one module so they sit in the slots the manual recommends for two "
           "modules (for example A2 and B2), then confirm dual-channel mode in the firmware setup."),
        PQ("Every morning a school computer shows the wrong date and asks the user to enter setup. Identify the most likely "
           "fault and the remedy.",
           "The coin cell battery on the motherboard is flat, so the real-time clock and stored settings are lost when the PC "
           "is unplugged overnight. Replace the battery with the same type, then set the date, time and boot options again."),
        PQ("Describe the purpose of POST and explain why a PC uses beep codes instead of on-screen messages for some faults.",
           "POST checks the CPU, memory, graphics and key controllers each time the PC starts, so that faults are found before "
           "the operating system loads. Some faults, such as missing or faulty RAM or graphics, happen before the display can "
           "work, so the firmware uses a speaker pattern (beep codes) or diagnostic LEDs to report them."),
        SUM("A CPU must match the motherboard socket, and the chipset and firmware must support it.",
            "Dual-channel memory needs matched modules, one in each channel, in the slots the manual names.",
            "BIOS is legacy firmware; UEFI adds GPT support, Secure Boot and a modern setup interface.",
            "POST tests the hardware at power-on and reports early faults with beep codes or LEDs.",
            "Diagnose step by step: what works, what the code means, reseat, swap with known-good parts, conclude."),
    ],
))

# ---------------------------------------------------------------------------
# Hardware Maintenance & Deployment / OS deployment
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Hardware Maintenance & Deployment",
    topic="OS deployment",
    title="Deploying operating systems: USB and network installs, MBR vs GPT, NTFS, ext4 and virtual machines",
    slug="os-deployment-partitions-file-systems-vms",
    minutes=30,
    summary="Plan and carry out Windows and Linux installations from USB or over the network, choose between MBR and "
            "GPT, pick NTFS or ext4, and use virtual machines to test deployments safely.",
    objectives=[
        "Prepare bootable USB media and describe network (PXE) installation for many PCs",
        "Compare MBR and GPT partitioning and plan a partition layout for a given disk and firmware",
        "Choose an appropriate file system (NTFS, ext4, FAT32) and justify the choice",
        "Explain what a virtual machine and a hypervisor are and why technicians use them",
    ],
    key_concepts=["Bootable USB", "PXE network boot", "Disk image", "MBR", "GPT", "EFI System Partition",
                  "NTFS", "ext4", "Virtual machine", "Hypervisor"],
    blocks=[
        H("Introduction"),
        T("A secondary school in Bamenda has received thirty donated computers for its new ICT room. Each one needs an "
          "operating system before students can use it. Installing them one by one from a single USB stick would take "
          "days. A technician who understands deployment can plan the disk layout once, test it in a virtual machine, "
          "and then install every PC quickly and consistently."),
        T("Deployment means more than clicking Next in an installer. You must choose how the installer reaches the PC, "
          "how the disk is divided into partitions, and which file system each partition uses."),
        H("Installation methods"),
        KEY("Three ways to deliver an operating system", "Choose the method by the number of PCs and the network available.", cards=[
            ["Bootable USB", "An installer image (ISO) is written to a USB flash drive with an imaging tool. Good for one "
             "or a few PCs and where there is no reliable network."],
            ["Network install (PXE)", "The PC's network card boots from a server on the LAN using PXE. The server supplies "
             "the installer or a ready-made image. Good for labs with many identical PCs."],
            ["Disk imaging", "One reference PC is installed and configured, then its disk is captured as an image and copied "
             "to the others. Each copy must be generalized so PCs get unique names and identifiers."],
        ]),
        TIP("In places where the internet is slow or expensive, a local network install server or a set of prepared USB "
            "sticks saves a lot of data. Download the installer once, verify its checksum, then reuse it on every PC."),
        H("Partition tables: MBR and GPT"),
        D("A **partition table** records where each partition starts and ends on a disk. **MBR** (Master Boot Record) is the "
          "older scheme used with legacy BIOS. **GPT** (GUID Partition Table) is the modern scheme used with UEFI.",
          title="Definition"),
        KEY("MBR compared with GPT", "The key differences you must be able to state:", cards=[
            ["MBR", "Up to 4 primary partitions, or 3 primary plus 1 extended partition holding logical drives. Usable "
             "size about 2 TB with 512-byte sectors. One copy of the table, so it is easy to corrupt."],
            ["GPT", "Many partitions (Windows allows 128 by default). Supports disks far larger than 2 TB. Keeps a backup "
             "copy of the table at the end of the disk and uses checksums to detect damage. Boots with UEFI."],
        ]),
        EX("Worked example 1: planning a partition layout", intro=(
            "Plan a layout for a new 1 TB SSD in a UEFI PC that will run Windows for an SME in Douala. Staff files must "
            "survive a future reinstall of Windows."), steps=[
            S("Choose the partition table", text="The firmware is UEFI and Windows on UEFI requires GPT, so use GPT."),
            S("EFI System Partition (ESP)", text="A small FAT32 partition, typically a few hundred MB, that holds the boot "
              "loaders the UEFI firmware reads."),
            S("Microsoft Reserved Partition (MSR)", text="A small reserved partition that Windows creates on GPT disks. "
              "It has no drive letter."),
            S("System partition", text="NTFS, about 250 GB, mounted as C: for Windows and programs."),
            S("Data partition", text="NTFS, most of the remaining space, mounted as D: for staff files. Reinstalling Windows "
              "on C: leaves D: untouched."),
            S("Recovery partition", text="A small NTFS partition at the end for the Windows recovery environment. The final "
              "plan: GPT with ESP, MSR, C: system, D: data and recovery."),
        ]),
        H("File systems"),
        D("A **file system** organizes how files and folders are stored and found on a partition. **NTFS** is the standard "
          "Windows file system: it supports large files, permissions on files and folders, and journaling to recover "
          "after a crash. **ext4** is the common default on Linux: it is journaled and supports Linux ownership and "
          "permissions. **FAT32** is simple and readable by almost every device, but a single file cannot exceed 4 GB.",
          title="Definition"),
        T("Windows cannot read ext4 without extra software, and Linux can read and write NTFS with suitable drivers. FAT32 "
          "is still used for the EFI System Partition and for USB sticks that must work on many devices."),
        EX("Worked example 2: preparing a Linux data disk", intro=(
            "A cyber café server running Linux has a new second disk, seen as /dev/sdb. Create one GPT partition formatted "
            "as ext4 and mount it at /srv/data. Listing 1 shows the commands."), steps=[
            S("Identify the disk", text="Run lsblk and check the size, so you are certain /dev/sdb is the new, empty disk. "
              "Choosing the wrong disk destroys its data."),
            S("Create a GPT table", text="parted with mklabel gpt writes a new, empty GPT partition table."),
            S("Create the partition", text="mkpart creates one partition from 1 MiB to 100 percent of the disk. Starting at "
              "1 MiB keeps it aligned for good performance."),
            S("Format it", text="mkfs.ext4 creates an ext4 file system on /dev/sdb1."),
            S("Mount it", text="Create the folder /srv/data and mount the partition there. To mount it at every boot, add an "
              "entry to /etc/fstab using the partition's UUID."),
        ]),
        CODE("""
lsblk                                   # list disks and partitions
sudo parted /dev/sdb mklabel gpt        # new GPT partition table
sudo parted -a optimal /dev/sdb mkpart data ext4 1MiB 100%
sudo mkfs.ext4 /dev/sdb1                # format as ext4
sudo mkdir -p /srv/data
sudo mount /dev/sdb1 /srv/data
sudo blkid /dev/sdb1                    # shows the UUID for /etc/fstab
""", "bash", title="Listing 1", caption="Partitioning, formatting and mounting a second disk on Linux"),
        H("Virtual machines"),
        D("A **virtual machine (VM)** is a software computer with its own virtual CPU, memory, disk and network card. "
          "A **hypervisor** creates and runs VMs. A type 1 hypervisor runs directly on the hardware (common on servers). "
          "A type 2 hypervisor runs as an application on a normal operating system (common on desktops and laptops).",
          title="Definition",
          note="Hardware virtualization support must usually be enabled in the BIOS/UEFI setup before VMs will run well."),
        T("Technicians use VMs to test an installation or an image before deploying it to real PCs, to run an old program "
          "that needs an older operating system, and to run several servers on one physical machine. A snapshot saves the "
          "VM's state so you can roll back after a failed test."),
        H("Common mistakes"),
        MISTAKE("Formatting the wrong disk", "Disk names such as /dev/sdb or Disk 1 can change when drives are added. Always "
                "confirm by size and model before partitioning, and back up first."),
        MISTAKE("Mismatching firmware mode and partition table", "Booting the installer in legacy mode on a UEFI PC leads to an "
                "MBR install. Choose the UEFI entry for the USB stick in the boot menu so Windows installs on GPT."),
        MISTAKE("Using FAT32 for large files", "A 6 GB video or VM disk cannot be copied to FAT32. Use NTFS or exFAT for "
                "portable drives that must hold large files."),
        QUIZ("A technician must install Windows on a new 4 TB disk and use all of the space. Which choice is correct?",
             ["MBR with legacy BIOS", "GPT with UEFI", "MBR with four primary partitions", "FAT32 for the system partition"], 1,
             "MBR can only address about 2 TB with 512-byte sectors. GPT with UEFI can use the whole 4 TB disk.",
             feedback=["MBR would leave about half of the disk unusable.", "",
                       "More partitions do not remove MBR's size limit.",
                       "Windows must be installed on NTFS, and FAT32 limits single files to 4 GB."]),
        QUIZ("Which is the best method to install the same configuration on 30 identical lab PCs connected to a LAN?",
             ["One USB stick used on each PC in turn", "Network deployment using PXE boot and a prepared image",
              "Copying files from the internet on each PC", "Installing from DVDs"], 1,
             "PXE lets each PC boot from the LAN and receive the same image, so the lab is installed quickly and consistently.",
             feedback=["This works but is slow and each install may be configured differently.", "",
                       "This uses a lot of expensive data and gives inconsistent results.",
                       "DVDs are slow and many modern PCs have no optical drive."]),
        H("Practice questions"),
        PQ("State three differences between MBR and GPT partitioning.",
           "Any three: MBR allows 4 primary partitions (or 3 plus an extended partition), GPT allows many (128 by default in "
           "Windows); MBR is limited to about 2 TB with 512-byte sectors, GPT supports much larger disks; GPT stores a backup "
           "copy of the partition table and uses checksums, MBR has one copy; MBR is used with legacy BIOS, GPT with UEFI."),
        PQ("A shop owner wants Windows and Linux on the same 500 GB disk in a UEFI laptop. Propose a partition layout with "
           "a file system for each partition.",
           "Use GPT. One shared EFI System Partition (FAT32, a few hundred MB) for both boot loaders; the Microsoft Reserved "
           "Partition; Windows partition (NTFS, for example 200 GB); Linux root partition (ext4, for example 100 GB); a shared "
           "data partition (NTFS so both systems can use it); optionally a Linux swap partition or swap file."),
        PQ("Give two reasons why a technician might test a deployment in a virtual machine first.",
           "Any two: mistakes do not affect real PCs or data; snapshots allow quick roll-back and repeated testing; no extra "
           "hardware is needed; drivers, settings and software can be checked before the image is copied to many PCs."),
        PQ("Explain why NTFS is preferred to FAT32 for the system partition of a Windows PC.",
           "NTFS supports files larger than 4 GB, file and folder permissions for security, and journaling that helps it "
           "recover after a power cut or crash. FAT32 has none of these. Windows also requires NTFS for its system partition."),
        SUM("Install from USB for a few PCs, and use PXE network boot or disk imaging for many identical PCs.",
            "MBR suits legacy BIOS: 4 primary partitions and about 2 TB. GPT suits UEFI: many partitions, huge disks, backup table.",
            "A typical UEFI Windows layout is ESP, MSR, system, data and recovery partitions.",
            "NTFS for Windows, ext4 for Linux, FAT32 for the ESP and widely compatible USB sticks.",
            "Virtual machines and snapshots let you test a deployment safely before rolling it out."),
    ],
))

# ---------------------------------------------------------------------------
# Enterprise Infrastructure / Business technologies
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Enterprise Infrastructure",
    topic="Business technologies",
    title="Business technologies: e-commerce, VPNs, VoIP and learning platforms",
    slug="business-technologies-ecommerce-vpn-voip",
    minutes=30,
    summary="How businesses use e-commerce (B2B and B2C), virtual private networks, voice over IP and online learning "
            "platforms, with practical planning examples for Cameroonian SMEs.",
    objectives=[
        "Distinguish B2B and B2C e-commerce and describe the parts of an online sales system",
        "Explain how a VPN protects data travelling over the internet and when a business needs one",
        "Describe how VoIP works and estimate the bandwidth needed for a number of calls",
        "Evaluate the benefits and limits of learning platforms in low-connectivity areas",
    ],
    key_concepts=["E-commerce", "B2B", "B2C", "Payment gateway", "VPN", "Tunnelling and encryption", "VoIP",
                  "Codec", "Learning management system"],
    blocks=[
        H("Introduction"),
        T("A small supplier of building materials in Douala sells cement and iron rods to hardware shops across the "
          "Littoral region. It also wants to sell paint directly to home owners. Its manager travels often and needs to "
          "reach the company's files safely, and the branch in Yaoundé spends a lot on phone calls between offices."),
        T("Four technologies can help: e-commerce to sell online, a VPN for safe remote access, VoIP for cheaper calls and a "
          "learning platform to train staff. In this lesson you will learn what each one does and how to plan it."),
        H("E-commerce"),
        D("**E-commerce** is buying and selling goods or services over electronic networks, mainly the internet. In **B2B** "
          "(business-to-business) e-commerce a business sells to other businesses. In **B2C** (business-to-consumer) "
          "e-commerce a business sells to individual customers.", title="Definition"),
        KEY("B2B and B2C compared", "The same company can do both, but the systems differ.", cards=[
            ["B2B", "Fewer customers, larger orders, negotiated prices, credit terms and invoices. Often uses customer "
             "accounts, order portals and links to stock systems."],
            ["B2C", "Many customers, small orders, fixed displayed prices, instant payment. Needs a simple catalogue, a "
             "shopping cart, a payment gateway and delivery tracking."],
        ]),
        T("A typical online shop has a product catalogue, a shopping cart, a checkout, a payment gateway that accepts cards "
          "or mobile money, an order database and a way to arrange delivery. HTTPS must protect every page where customers "
          "enter personal or payment details."),
        EX("Worked example 1: choosing an e-commerce model", intro=(
            "The Douala supplier wants to sell (i) cement in bulk to hardware shops on 30-day credit and (ii) tins of paint "
            "to home owners who pay immediately. Recommend a model and features for each."), steps=[
            S("Classify sale (i)", text="The buyers are businesses ordering large quantities on credit. This is B2B."),
            S("Features for (i)", text="A login portal for each shop, agreed price lists, order history, invoices and credit "
              "limits checked against the accounts database."),
            S("Classify sale (ii)", text="The buyers are individual consumers paying at once. This is B2C."),
            S("Features for (ii)", text="A public catalogue with photos and prices, a shopping cart, checkout over HTTPS, a "
              "payment gateway that supports mobile money and cards, and SMS order confirmation."),
            S("Recommendation", text="Run a B2B portal for trade customers and a B2C shop for the public, both linked to the "
              "same stock database so stock levels stay correct."),
        ]),
        H("Virtual private networks (VPNs)"),
        D("A **VPN** creates an encrypted tunnel across a public network such as the internet. Data inside the tunnel cannot "
          "be read or changed by others on the way, and the remote user appears to be on the company network.",
          title="Definition"),
        T("A **remote-access VPN** connects one user, such as the travelling manager on hotel Wi-Fi, to the office. A "
          "**site-to-site VPN** joins two office networks, such as Douala and Yaoundé, through VPN gateways at each end, so "
          "staff can share files and printers as if on one LAN."),
        T("A VPN protects data in transit. It does not stop malware already on a laptop, and it depends on strong "
          "authentication, so it should be used with good passwords or certificates and multi-factor authentication."),
        H("Voice over IP (VoIP)"),
        D("**VoIP** carries voice calls as data packets over an IP network. A **codec** converts the voice into digital data "
          "and compresses it. The packets travel over the LAN or internet and are turned back into sound at the other end.",
          title="Definition",
          note="Voice quality suffers from high latency (delay), jitter (uneven delay) and packet loss. Quality of Service "
               "(QoS) settings on routers give voice packets priority."),
        EX("Worked example 2: estimating VoIP bandwidth", intro=(
            "The Yaoundé branch wants up to 6 simultaneous VoIP calls to Douala. The codec chosen needs about 90 kbps per call "
            "in each direction, including packet overhead. The branch internet link has 2 Mbps upload. Is it enough?"), steps=[
            S("Bandwidth for all calls", text="6 calls multiplied by 90 kbps gives 540 kbps in each direction."),
            S("Convert units", text="2 Mbps is 2000 kbps of upload capacity."),
            S("Compare", text="540 kbps is about 27 percent of 2000 kbps, leaving about 1460 kbps for other traffic."),
            S("Consider other traffic", text="If staff also upload large files, voice can be delayed. Configure QoS to give "
              "voice priority."),
            S("Conclusion", text="The link is enough for 6 calls, provided QoS is enabled to protect call quality."),
        ]),
        H("Learning platforms"),
        D("A **learning platform** or **learning management system (LMS)** is software that delivers courses, tracks "
          "progress, hosts quizzes and lets teachers and learners communicate. Businesses use it for staff training and "
          "schools use it for online lessons.", title="Definition"),
        T("In areas with poor connectivity, a good platform works on low-end phones, uses small pages and compressed video, "
          "allows content to be downloaded for offline study and syncs results when a connection returns."),
        H("Common mistakes"),
        MISTAKE("Thinking a VPN makes a user anonymous and fully safe", "A VPN encrypts traffic in transit only. The VPN "
                "provider or company can still see traffic, and malware on the device is not removed."),
        MISTAKE("Confusing B2B with large companies", "B2B depends on who the customer is, not on company size. A small "
                "bakery selling bread to restaurants is doing B2B."),
        MISTAKE("Ignoring upload speed for VoIP", "A call sends voice in both directions. Many home and office links have much "
                "less upload than download, so check upload capacity."),
        QUIZ("A company joins its Douala and Garoua offices so staff can share a file server securely over the internet. "
             "Which technology is this?",
             ["Remote-access VPN", "Site-to-site VPN", "VoIP", "B2C e-commerce"], 1,
             "Two whole networks are joined through gateways at each office, so it is a site-to-site VPN.",
             feedback=["A remote-access VPN connects one user's device, not a whole office.", "",
                       "VoIP carries voice calls; it does not secure file sharing.",
                       "B2C is selling to consumers and has nothing to do with linking offices."]),
        H("Practice questions"),
        PQ("Distinguish between B2B and B2C e-commerce, giving one Cameroonian example of each.",
           "B2B is trade between businesses, for example a cocoa exporter in Kribi selling to a processing company, or a "
           "wholesaler supplying shops. B2C is a business selling directly to individual consumers, for example an online "
           "shop in Yaoundé selling phones to the public with mobile money payment."),
        PQ("Explain two ways in which a VPN protects a sales agent who uses public Wi-Fi in a hotel.",
           "Encryption: data in the tunnel cannot be read by others on the same Wi-Fi, so passwords and customer data stay "
           "confidential. Integrity and authentication: data cannot be changed in transit without detection, and only "
           "authenticated users can connect to the company network."),
        PQ("An office link has 1 Mbps upload. Each VoIP call needs about 90 kbps per direction. Calculate the maximum number "
           "of simultaneous calls if 40 percent of the upload must be kept for other traffic.",
           "Capacity for voice is 60 percent of 1000 kbps, which is 600 kbps. 600 divided by 90 is about 6.7, so at most 6 "
           "simultaneous calls can be supported."),
        PQ("Give two advantages and one disadvantage of using a learning platform to train staff in several branches.",
           "Advantages: staff learn at their own pace without travelling, saving cost; progress and quiz results are tracked "
           "centrally; the same content reaches every branch. Disadvantage: it needs devices and a reliable connection, and "
           "some staff may lack digital skills or motivation without face-to-face support."),
        SUM("B2B sells to businesses (accounts, invoices, credit); B2C sells to consumers (cart, instant payment).",
            "An online shop needs a catalogue, cart, HTTPS checkout, payment gateway, order database and delivery.",
            "A VPN is an encrypted tunnel over the internet: remote-access for users, site-to-site for offices.",
            "VoIP turns voice into packets using a codec; plan bandwidth per call and use QoS.",
            "Learning platforms deliver and track training and should work offline in low-connectivity areas."),
    ],
))

# ---------------------------------------------------------------------------
# Enterprise Infrastructure / Green computing
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Enterprise Infrastructure",
    topic="Green computing",
    title="Green computing: reducing energy use and managing e-waste",
    slug="green-computing-energy-and-e-waste",
    minutes=25,
    summary="Measure and reduce the energy used by ICT equipment, size a simple solar backup for power cuts, and manage "
            "electronic waste responsibly through reuse, refurbishment and recycling.",
    objectives=[
        "Calculate the daily energy use and cost of a group of computers",
        "Describe practical ways to reduce the energy used by ICT equipment",
        "Estimate the solar panel and battery size needed to keep key equipment running",
        "Explain the dangers of e-waste and the reduce, reuse, recycle approach to managing it",
    ],
    key_concepts=["Green computing", "Power (W) and energy (kWh)", "Power management", "Virtualization",
                  "Solar PV and battery backup", "Depth of discharge", "E-waste", "Reduce, reuse, recycle"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian towns, power cuts are part of daily life. A cyber café in Buea may run a petrol generator for "
          "hours, which is noisy, expensive and polluting. At the same time, old monitors, phones and batteries are often "
          "burned or dumped, releasing toxic substances into the soil and air."),
        T("Green computing is about using ICT in a way that wastes less energy and causes less harm, from the day equipment "
          "is bought to the day it is thrown away. It saves money as well as protecting the environment."),
        D("**Green computing** is the design, use and disposal of computers and related equipment in ways that reduce energy "
          "consumption, pollution and waste.", title="Definition"),
        H("Power and energy"),
        D("**Power** is the rate at which a device uses electricity, measured in watts (W). **Energy** is power used over "
          "time, measured in watt-hours (Wh) or kilowatt-hours (kWh). Energy in Wh equals power in W multiplied by time in "
          "hours, and 1 kWh is 1000 Wh. Electricity bills charge for kWh.", title="Definition"),
        EX("Worked example 1: energy use and savings in a cyber café", intro=(
            "A cyber café has 10 desktop PCs with monitors, each using about 80 W, open 10 hours a day. The owner is "
            "considering replacing them with low-power units using about 30 W each. Assume a tariff of 100 FCFA per kWh "
            "(an example figure only). Find the daily energy use now, and the monthly saving over 30 days."), steps=[
            S("Energy per day now", text="10 PCs times 80 W times 10 h equals 8000 Wh, which is 8 kWh per day."),
            S("Energy per day with low-power units", text="10 times 30 W times 10 h equals 3000 Wh, which is 3 kWh per day."),
            S("Daily saving in energy", text="8 kWh minus 3 kWh equals 5 kWh per day."),
            S("Daily saving in money", text="5 kWh times 100 FCFA equals 500 FCFA per day."),
            S("Monthly saving", text="500 FCFA times 30 days equals 15 000 FCFA per month, before counting lower generator use."),
        ]),
        H("Reducing energy use"),
        KEY("Practical energy savings", "Small changes add up across a whole office or lab.", cards=[
            ["Power management", "Set displays to turn off and PCs to sleep after a few idle minutes. Shut down fully at "
             "night instead of leaving machines on."],
            ["Efficient hardware", "Choose laptops, mini PCs or thin clients, LED monitors and efficient power supplies. "
             "SSDs use less power than spinning hard disks."],
            ["Virtualization", "Run several virtual servers on one physical server instead of many half-idle machines."],
            ["Cloud and sharing", "Use shared network printers and cloud services instead of a device for every user."],
        ]),
        H("Solar power for ICT"),
        T("Solar photovoltaic (PV) panels produce electricity in daylight. A charge controller charges a battery bank, and an "
          "inverter converts the battery's DC into AC for normal equipment. Sizing depends on the energy needed and the number "
          "of peak sun hours, the equivalent hours of full sunshine per day at the site."),
        D("**Depth of discharge (DoD)** is the fraction of a battery's capacity that is used before recharging. Lead-acid "
          "batteries last longer if only about half their capacity is used. Lithium batteries can usually be discharged "
          "further. Always follow the battery maker's figure.", title="Key fact"),
        EX("Worked example 2: sizing a solar backup", intro=(
            "A small office wants to run a router, a laptop and a small server, using 300 W in total, for 4 hours during power "
            "cuts. Assume 5 peak sun hours, 20 percent system losses, a 12 V lead-acid battery bank and 50 percent depth of "
            "discharge. Estimate the battery capacity and panel size."), steps=[
            S("Energy needed", text="300 W times 4 h equals 1200 Wh."),
            S("Battery energy allowing for DoD", text="Only half the battery may be used, so the bank must store 1200 divided "
              "by 0.5, which is 2400 Wh."),
            S("Battery capacity in amp-hours", text="2400 Wh divided by 12 V equals 200 Ah."),
            S("Panel energy needed per day", text="To replace 1200 Wh with 20 percent losses: 1200 divided by 0.8 equals 1500 Wh."),
            S("Panel power", text="1500 Wh divided by 5 sun hours equals 300 W of panels. Answer: about 200 Ah at 12 V and 300 W "
              "of panels, with an inverter rated above 300 W."),
        ]),
        H("E-waste management"),
        D("**E-waste** is discarded electrical and electronic equipment, such as computers, phones, batteries and cables. It "
          "can contain hazardous substances such as lead, mercury and cadmium, as well as valuable metals that can be "
          "recovered.", title="Definition"),
        T("Burning cables to recover copper or dumping batteries pollutes the air, soil and water and harms health. The waste "
          "hierarchy gives the order of preference: first reduce what you buy, then reuse and repair, then refurbish and "
          "donate, then recycle through approved collectors, and only dispose of what is left safely."),
        T("Before any device leaves the organization, all data must be securely wiped or the storage physically destroyed, "
          "so customer and staff data cannot be recovered."),
        H("Common mistakes"),
        MISTAKE("Mixing up watts and watt-hours", "Watts measure power at an instant. Watt-hours measure energy over time. "
                "Multiply watts by hours to get Wh, then divide by 1000 for kWh."),
        MISTAKE("Forgetting depth of discharge", "Sizing a lead-acid battery to the exact energy needed leads to deep "
                "discharge and a short battery life. Divide by the allowed DoD."),
        MISTAKE("Donating computers with data still on them", "Deleting files or formatting quickly does not remove data "
                "securely. Use a proper wiping tool or destroy the drive."),
        QUIZ("A 50 W router runs 24 hours a day. How much energy does it use per day?",
             ["50 Wh", "1.2 kWh", "2.4 kWh", "12 kWh"], 1,
             "50 W times 24 h equals 1200 Wh, which is 1.2 kWh.",
             hint="Energy equals power times time, then divide by 1000.",
             feedback=["That is the energy for only one hour.", "",
                       "This doubles the correct answer. Check your multiplication.",
                       "This is ten times too large: 1200 Wh is 1.2 kWh, not 12 kWh."]),
        QUIZ("Which action is highest in the waste hierarchy for an old but working school computer?",
             ["Recycling it for metals", "Burning it to recover copper", "Reusing it after wiping and refurbishing",
              "Burying it in a landfill"], 2,
             "Reuse keeps the device working and avoids the energy and pollution of making a new one.",
             feedback=["Recycling is good but comes after reuse in the hierarchy.",
                       "Burning releases toxic fumes and is harmful and unsafe.", "",
                       "Landfill is the last resort and can leak hazardous substances."]),
        H("Practice questions"),
        PQ("A school lab has 20 PCs using 100 W each for 6 hours a day, 5 days a week. Calculate the weekly energy use in kWh.",
           "Per day: 20 times 100 W times 6 h equals 12 000 Wh, which is 12 kWh. Per week: 12 kWh times 5 equals 60 kWh."),
        PQ("Describe three ways a business in Douala could reduce the energy used by its ICT equipment.",
           "Any three, explained: enable sleep and display power-off settings and shut down at night; replace old desktops and "
           "monitors with laptops or efficient LED monitors; virtualize several servers on one machine; use shared network "
           "printers; use solar power to reduce generator use."),
        PQ("A device uses 150 W and must run for 5 hours from a 12 V battery with 50 percent depth of discharge. Calculate the "
           "battery capacity needed in Ah.",
           "Energy: 150 times 5 equals 750 Wh. Allowing for DoD: 750 divided by 0.5 equals 1500 Wh. Capacity: 1500 divided by "
           "12 equals 125 Ah."),
        PQ("Explain two dangers of poor e-waste disposal and two ways an organization can manage e-waste responsibly.",
           "Dangers: toxic metals such as lead, mercury and cadmium pollute soil and water; burning plastics and cables "
           "releases harmful fumes; data left on devices can be stolen. Responsible management: reuse and refurbish working "
           "equipment or donate it after secure data wiping; send unusable equipment to an approved recycler."),
        SUM("Green computing reduces energy use, pollution and waste across a device's whole life.",
            "Energy in Wh equals power in W times hours; 1 kWh is 1000 Wh and bills charge per kWh.",
            "Power management, efficient hardware, virtualization and sharing all cut energy use.",
            "Size solar backup from the energy needed, the sun hours, system losses and the battery's depth of discharge.",
            "Manage e-waste by reduce, reuse, refurbish, recycle, and always wipe data first."),
    ],
))

# ---------------------------------------------------------------------------
# Enterprise Infrastructure / Database automation
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Enterprise Infrastructure",
    topic="Database automation",
    title="Automating relational databases: triggers, stored procedures, scheduled jobs and macros",
    slug="database-automation-triggers-procedures",
    minutes=30,
    summary="Use triggers, stored procedures, scheduled events and form macros to make a relational database update "
            "itself, enforce business rules and produce routine reports without manual work.",
    objectives=[
        "Explain why businesses automate databases and name the main automation tools",
        "Write a trigger that updates one table when rows are inserted into another",
        "Write a stored procedure that runs a routine query with a parameter",
        "Describe scheduled jobs and macros and choose the right tool for a task",
    ],
    key_concepts=["Database automation", "Trigger", "BEFORE and AFTER triggers", "NEW and OLD rows",
                  "Stored procedure", "Parameter", "Scheduled event", "Macro", "Audit log"],
    blocks=[
        H("Introduction"),
        T("A pharmacy in Limbe records every sale in a database. At the end of each day, a worker counts what was sold and "
          "subtracts it from the stock list by hand. Mistakes are common, and the pharmacy sometimes runs out of important "
          "medicines without noticing."),
        T("Database automation lets the database do this work itself. When a sale is saved, the stock goes down "
          "automatically. When stock is low, a reorder list is produced every night. Rules such as no sale beyond the "
          "available stock are checked every time, by the database, not by a tired worker."),
        D("**Database automation** is the use of features inside the database management system (DBMS), or tools around it, "
          "to carry out tasks automatically: enforcing rules, updating related data, running routine queries and producing "
          "reports.", title="Definition"),
        KEY("The main automation tools", "Each tool is started in a different way.", cards=[
            ["Trigger", "Runs automatically when a row is inserted, updated or deleted in a table."],
            ["Stored procedure", "A named, saved block of SQL that a user or program calls, often with parameters."],
            ["Scheduled event or job", "Runs SQL at fixed times, such as every night at midnight."],
            ["Macro", "In desktop databases such as Access, a saved list of actions run from a button or form event."],
        ]),
        H("Triggers"),
        D("A **trigger** is SQL code attached to a table that runs automatically when a chosen event (INSERT, UPDATE or DELETE) "
          "happens. A BEFORE trigger runs before the change and can check or reject it. An AFTER trigger runs once the change "
          "is saved. Inside the trigger, NEW refers to the new row and OLD to the row before the change.",
          title="Definition"),
        T("The examples use two tables: products(product_id, name, stock, reorder_level) and sales(sale_id, product_id, "
          "quantity, sale_date). The SQL is written in MySQL syntax; other DBMSs use slightly different wording."),
        EX("Worked example 1: an AFTER INSERT trigger to update stock", intro=(
            "Write a trigger so that whenever a sale is inserted into sales, the stock of that product in products goes down "
            "by the quantity sold. Listing 1 shows the result."), steps=[
            S("Choose the event and timing", text="The action follows a new sale, so use AFTER INSERT ON sales."),
            S("Decide on row level", text="FOR EACH ROW makes the trigger run once for every sale row inserted."),
            S("Write the action", text="UPDATE products and subtract NEW.quantity from stock."),
            S("Match the right product", text="Use WHERE product_id = NEW.product_id so only the product sold is changed."),
            S("Test it", text="If a product has stock 50 and a sale of 3 is inserted, stock becomes 47 with no manual work."),
        ]),
        CODE("""
CREATE TRIGGER trg_sale_update_stock
AFTER INSERT ON sales
FOR EACH ROW
UPDATE products
SET stock = stock - NEW.quantity
WHERE product_id = NEW.product_id;
""", "sql", title="Listing 1", caption="AFTER INSERT trigger that reduces stock automatically"),
        EX("Worked example 2: a BEFORE INSERT trigger that enforces a business rule", intro=(
            "The pharmacy must never record a sale larger than the available stock. Write a trigger to reject such a sale. "
            "Listing 2 shows the result."), steps=[
            S("Choose the timing", text="The sale must be stopped before it is saved, so use BEFORE INSERT."),
            S("Find the current stock", text="A subquery reads stock from products for NEW.product_id."),
            S("Compare", text="IF NEW.quantity is greater than that stock, the rule is broken."),
            S("Reject the row", text="SIGNAL raises an error with a clear message, and the INSERT is cancelled."),
            S("Handle delimiters", text="The trigger body has several statements, so DELIMITER changes the end marker while "
              "the trigger is created."),
        ]),
        CODE("""
DELIMITER //
CREATE TRIGGER trg_check_stock
BEFORE INSERT ON sales
FOR EACH ROW
BEGIN
  IF NEW.quantity > (SELECT stock FROM products
                     WHERE product_id = NEW.product_id) THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Not enough stock for this sale';
  END IF;
END //
DELIMITER ;
""", "sql", title="Listing 2", caption="BEFORE INSERT trigger that rejects sales above the stock level"),
        H("Stored procedures and scheduled events"),
        D("A **stored procedure** is a named block of SQL saved in the database and run with CALL. It can take "
          "**parameters**, so the same procedure works for different values. Procedures keep business logic in one place, "
          "reduce network traffic and can be granted to users who are not allowed to edit tables directly.",
          title="Definition"),
        EX("Worked example 3: a daily sales report procedure", intro=(
            "Write a procedure that lists the total quantity sold of each product on a given date. Listing 3 shows the "
            "procedure, how to call it, and a nightly event that fills a reorder list."), steps=[
            S("Name and parameter", text="Call it daily_sales and give it one input parameter, report_date, of type DATE."),
            S("Join the tables", text="Join sales to products on product_id to show product names."),
            S("Filter and group", text="WHERE sale_date = report_date, then GROUP BY the product and SUM the quantity."),
            S("Run it", text="CALL daily_sales('2026-11-05') produces the report for that day."),
            S("Schedule related work", text="An event runs every day and copies products whose stock is at or below the "
              "reorder level into a reorder_list table for the manager."),
        ]),
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

CREATE EVENT ev_nightly_reorder
ON SCHEDULE EVERY 1 DAY
DO
  INSERT INTO reorder_list (product_id, stock, listed_on)
  SELECT product_id, stock, CURRENT_DATE
  FROM products
  WHERE stock <= reorder_level;
""", "sql", title="Listing 3", caption="Stored procedure with a parameter, and a scheduled event (the event scheduler must be enabled)"),
        H("Macros in desktop databases"),
        T("In a desktop database such as Microsoft Access, a **macro** is a saved list of actions, for example open a form, "
          "run a query, print a report and show a message. Macros are attached to buttons or form events such as After "
          "Update. They suit small offices where users work through forms rather than writing SQL."),
        H("Common mistakes"),
        MISTAKE("Using OLD in an INSERT trigger", "A newly inserted row has no previous version, so only NEW exists. OLD is "
                "used in UPDATE and DELETE triggers."),
        MISTAKE("Forgetting the WHERE clause in a trigger update", "Without WHERE product_id = NEW.product_id, every product's "
                "stock would be reduced on each sale."),
        MISTAKE("Using an AFTER trigger to block bad data", "By the time an AFTER trigger runs, the row has already been "
                "written. Use a BEFORE trigger or a constraint to reject invalid data."),
        QUIZ("A manager wants an email list of low-stock items produced every night at 23:00, whether or not anyone uses the "
             "database. Which tool fits best?",
             ["An AFTER INSERT trigger", "A scheduled event or job", "A BEFORE UPDATE trigger", "A form macro"], 1,
             "The task depends on the time, not on a change to a table, so a scheduled event or job is the right tool.",
             feedback=["A trigger only runs when rows are inserted, so nothing happens on a night with no sales.", "",
                       "A trigger runs only when a row is updated, not at a fixed time.",
                       "A macro needs a user to open a form or click a button."]),
        H("Practice questions"),
        PQ("Define a database trigger and give two examples of tasks a trigger could automate in a school fees database.",
           "A trigger is SQL attached to a table that runs automatically when an INSERT, UPDATE or DELETE happens on it. "
           "Examples: after a payment is inserted, reduce the student's outstanding balance; before a payment is inserted, "
           "reject a negative amount; after a record is updated, write the old and new values to an audit log table."),
        PQ("Distinguish between a trigger and a stored procedure.",
           "A trigger runs automatically when a specified data change happens on its table and cannot be called directly. A "
           "stored procedure is run only when it is explicitly called (for example with CALL) by a user, program or event, "
           "and it can accept parameters."),
        PQ("Write a MySQL trigger that, after a row is deleted from sales, adds the quantity back to the product's stock.",
           "CREATE TRIGGER trg_sale_delete AFTER DELETE ON sales FOR EACH ROW UPDATE products SET stock = stock + OLD.quantity "
           "WHERE product_id = OLD.product_id; OLD is used because the deleted row no longer has a NEW version."),
        PQ("Give three benefits of automating routine database tasks for an SME.",
           "Any three: fewer human errors because calculations are done the same way every time; time saved for staff; "
           "business rules are always enforced; reports are ready on time; data stays consistent across related tables; "
           "changes can be logged automatically for auditing."),
        SUM("Database automation makes the DBMS enforce rules, update related data and run routine work itself.",
            "Triggers run on INSERT, UPDATE or DELETE; BEFORE triggers can reject data, AFTER triggers react to saved data.",
            "Use NEW for the new row and OLD for the previous row, and always restrict updates with WHERE.",
            "Stored procedures are named SQL blocks run with CALL and can take parameters.",
            "Scheduled events run at fixed times; macros automate actions from forms in desktop databases."),
    ],
))

# ---------------------------------------------------------------------------
# Web Development / Layout
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Web Development",
    topic="Layout",
    title="Page layout with semantic HTML5, CSS Flexbox and CSS Grid",
    slug="layout-semantic-html5-flexbox-grid",
    minutes=30,
    summary="Structure web pages with semantic HTML5 elements and lay them out with CSS Flexbox for rows of items and "
            "CSS Grid for whole-page layouts that adapt to phones and computers.",
    objectives=[
        "Use semantic HTML5 elements to describe the structure of a page",
        "Build a one-dimensional layout with Flexbox using justify-content, align-items and flex-wrap",
        "Build a two-dimensional page layout with CSS Grid and named grid areas",
        "Make a layout responsive with a media query and choose between Flexbox and Grid",
    ],
    key_concepts=["Semantic HTML5", "Accessibility", "Flex container and flex items", "Main axis and cross axis",
                  "CSS Grid", "fr unit", "grid-template-areas", "Media query", "Responsive design"],
    blocks=[
        H("Introduction"),
        T("A tailoring workshop in Bafoussam wants a website that shows its services, prices and a contact section. Most of "
          "its customers will visit on a phone, but the owner also wants it to look good on a computer. The page must load "
          "quickly on a slow connection and be readable by search engines and screen readers."),
        T("Two skills make this possible. Semantic HTML5 describes what each part of the page is. CSS Flexbox and Grid control "
          "where each part appears on screens of different sizes."),
        H("Semantic HTML5"),
        D("**Semantic elements** are HTML tags whose names describe their meaning, such as header, nav, main, section, "
          "article, aside and footer. They replace anonymous div elements for the main parts of a page.",
          title="Definition",
          note="Semantic structure helps screen readers announce page regions, helps search engines understand content, and "
               "makes code easier for other developers to maintain."),
        KEY("Common HTML5 structural elements", "Choose the element that matches the content's meaning.", cards=[
            ["header and footer", "Introductory content (logo, title) and closing content (contact, copyright)."],
            ["nav", "A block of main navigation links."],
            ["main", "The main content, used once per page."],
            ["section and article", "A themed group of content, and a self-contained item such as a news post."],
            ["aside", "Related side content such as adverts or a notice box."],
        ]),
        CODE("""
<body>
  <header>
    <h1>Bafoussam Tailors</h1>
    <nav>
      <a href="#services">Services</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>
  <main>
    <section id="services">
      <h2>Our services</h2>
      <article class="card">Kaba and dresses</article>
      <article class="card">Suits and shirts</article>
      <article class="card">School uniforms</article>
    </section>
    <aside>Open Monday to Saturday</aside>
  </main>
  <footer id="contact">Market road, Bafoussam</footer>
</body>
""", "html", title="Listing 1", caption="Semantic structure for the workshop page"),
        H("Flexbox: one-dimensional layout"),
        D("**Flexbox** lays items out in one direction at a time, a row or a column. Setting display: flex on a parent makes it "
          "a **flex container** and its children **flex items**. The **main axis** follows flex-direction (row by default) "
          "and the **cross axis** is at right angles to it.", title="Definition"),
        T("justify-content places items along the main axis (for example space-between). align-items places them along the "
          "cross axis (for example center). flex-wrap: wrap lets items move to a new line when space runs out, and gap sets "
          "the space between items."),
        EX("Worked example 1: a navigation bar and service cards with Flexbox", intro=(
            "Using Listing 1, put the title on the left and the links on the right of the header, vertically centred. Then "
            "show the service cards side by side, wrapping onto new lines on narrow screens. Listing 2 shows the CSS."), steps=[
            S("Make the header a flex container", text="header gets display: flex, so h1 and nav become flex items in a row."),
            S("Push the items apart", text="justify-content: space-between puts h1 at the left and nav at the right."),
            S("Centre vertically", text="align-items: center lines them up on the cross axis."),
            S("Lay out the cards", text="The services section gets display: flex, flex-wrap: wrap and gap: 1rem."),
            S("Size each card", text="flex: 1 1 200px lets each card grow and shrink from a base width of 200px, so three fit "
              "on a computer and they stack on a phone."),
        ]),
        CODE("""
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}
nav a { margin-left: 1rem; }

#services {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
#services h2 { flex-basis: 100%; }   /* heading takes a full line */
.card {
  flex: 1 1 200px;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
}
""", "css", title="Listing 2", caption="Flexbox header and wrapping cards"),
        H("CSS Grid: two-dimensional layout"),
        D("**CSS Grid** lays items out in rows and columns at the same time. grid-template-columns and grid-template-rows "
          "define the tracks. The **fr unit** shares out the remaining free space, so 3fr 1fr gives the first column three "
          "times the width of the second. grid-template-areas lets you name regions and place elements by name.",
          title="Definition"),
        EX("Worked example 2: a responsive page layout with Grid", intro=(
            "Lay out the whole page: header across the top, main content and aside side by side, footer across the bottom. "
            "On screens narrower than 600px everything should stack in one column. Listing 3 shows the CSS."), steps=[
            S("Make body a grid", text="body gets display: grid and a gap between areas."),
            S("Define columns", text="grid-template-columns: 3fr 1fr gives a wide main column and a narrow aside column."),
            S("Name the areas", text="grid-template-areas draws the layout: header spans both columns, main and aside share "
              "the middle row, footer spans both columns."),
            S("Place each element", text="Each element gets grid-area with its name, for example main gets grid-area: main."),
            S("Add a media query", text="Inside @media (max-width: 600px), use one column and stack the areas in the order "
              "header, main, aside, footer. The layout now adapts to phones."),
        ]),
        CODE("""
body {
  display: grid;
  grid-template-columns: 3fr 1fr;
  grid-template-areas:
    "header header"
    "main   aside"
    "footer footer";
  gap: 1rem;
}
header { grid-area: header; }
main   { grid-area: main; }
aside  { grid-area: aside; }
footer { grid-area: footer; }

@media (max-width: 600px) {
  body {
    grid-template-columns: 1fr;
    grid-template-areas: "header" "main" "aside" "footer";
  }
}
""", "css", title="Listing 3", caption="Grid page layout with a media query for phones"),
        TIP("Note that in Listing 1 the aside is inside main. For Listing 3 to work, move aside out so that header, main, "
            "aside and footer are all direct children of body: grid only positions direct children of the grid container."),
        KEY("Flexbox or Grid?", "Both are often used on the same page.", cards=[
            ["Flexbox", "Best for one direction: navigation bars, rows of buttons, a list of cards that wraps."],
            ["Grid", "Best for two directions: the overall page skeleton, galleries and dashboards with rows and columns."],
        ]),
        H("Common mistakes"),
        MISTAKE("Applying flex properties to the wrong element", "justify-content and align-items go on the container (the "
                "parent), not on the items. Each item uses flex, order or align-self."),
        MISTAKE("Forgetting the viewport meta tag", "Without the viewport meta tag in the head, phones show a zoomed-out "
                "desktop page and media queries seem not to work."),
        MISTAKE("Using div for everything", "A page made only of div elements works visually but gives no meaning to screen "
                "readers or search engines. Use header, nav, main, section and footer."),
        QUIZ("A flex container has flex-direction: row. Which property centres its items vertically?",
             ["justify-content: center", "align-items: center", "text-align: center", "grid-area: center"], 1,
             "With flex-direction: row the cross axis is vertical, and align-items controls the cross axis.",
             feedback=["justify-content works on the main axis, which is horizontal for a row.", "",
                       "text-align centres inline text inside an element, not flex items.",
                       "grid-area is a Grid property for placing items in named areas."]),
        QUIZ("In grid-template-columns: 2fr 1fr 1fr on a container 800px wide with no gaps, how wide is the first column?",
             ["200px", "266px", "400px", "533px"], 2,
             "There are 2 + 1 + 1 = 4 fractions. Each fr is 800 divided by 4, which is 200px, so 2fr is 400px.",
             feedback=["That is the width of one fr, the size of the second and third columns.",
                       "This divides 800 by 3, ignoring that the first column has 2 fractions.", "",
                       "This treats the first column as two thirds of the width, but there are four fractions in total."]),
        H("Practice questions"),
        PQ("State three advantages of using semantic HTML5 elements instead of div elements.",
           "Screen readers can identify page regions such as nav and main, improving accessibility; search engines better "
           "understand the content; the code is clearer and easier to maintain; consistent structure makes styling simpler."),
        PQ("Write CSS that makes a footer display its three child elements in a row, evenly spaced, and stack them in a column "
           "on screens up to 500px wide.",
           "footer { display: flex; justify-content: space-around; } then @media (max-width: 500px) { footer { "
           "flex-direction: column; align-items: center; } }. The media query changes the main axis to vertical on small screens."),
        PQ("Write grid-template-areas for a layout with a header across the top, a nav on the left, main content on the right "
           "taking three times the width of the nav, and a footer across the bottom.",
           "grid-template-columns: 1fr 3fr; grid-template-areas: \"header header\" \"nav main\" \"footer footer\"; Then set "
           "grid-area: header, nav, main and footer on the matching elements."),
        PQ("Explain the difference between Flexbox and CSS Grid, and give one suitable use for each.",
           "Flexbox is one-dimensional: it arranges items along a single row or column. Grid is two-dimensional: it controls "
           "rows and columns together. Flexbox suits a navigation bar or wrapping row of cards; Grid suits a full page layout "
           "with header, sidebar, content and footer."),
        SUM("Semantic HTML5 elements describe page structure and help accessibility and search engines.",
            "Flexbox arranges items in one direction; justify-content works on the main axis, align-items on the cross axis.",
            "flex-wrap and flex-basis let rows of cards adapt to narrow screens.",
            "CSS Grid controls rows and columns together; fr shares free space and named areas make layouts readable.",
            "Media queries and the viewport meta tag make layouts responsive for phones."),
    ],
))

# ---------------------------------------------------------------------------
# Web Development / JavaScript
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Web Development",
    topic="JavaScript",
    title="Client-side JavaScript and DOM manipulation",
    slug="client-side-javascript-dom-manipulation",
    minutes=30,
    summary="Use client-side JavaScript to select page elements, respond to events, change content and styles, create new "
            "elements and validate forms in the browser.",
    objectives=[
        "Explain what client-side JavaScript is and what the DOM represents",
        "Select elements with getElementById and querySelector and change their text, attributes and classes",
        "Respond to user events with addEventListener",
        "Create and add new elements, and validate a form before it is submitted",
    ],
    key_concepts=["Client-side scripting", "DOM", "Element selection", "textContent", "Event and event listener",
                  "classList", "createElement and appendChild", "Form validation", "preventDefault"],
    blocks=[
        H("Introduction"),
        T("A fast-food stand in Yaoundé takes orders through a simple web page. Customers choose items, and the page should "
          "show the running total at once, without reloading. If someone forgets to type a phone number, the page should "
          "say so before the order is sent."),
        T("This instant behaviour comes from JavaScript running in the customer's browser. It saves data on slow "
          "connections because the page does not have to go back to the server for every small change."),
        D("**Client-side JavaScript** is code sent with a web page and run by the browser on the user's device. It can react "
          "to the user and change the page immediately. Server-side code, by contrast, runs on the web server.",
          title="Definition",
          note="Client-side checks improve the user experience, but users can switch them off or bypass them. The server must "
               "always check data again."),
        H("The Document Object Model (DOM)"),
        D("The **DOM** is the browser's tree of objects representing the HTML page. Each element, such as a heading, button "
          "or paragraph, is a node in the tree. JavaScript changes the page by reading and changing these objects.",
          title="Definition"),
        KEY("Core DOM operations", "Almost every script follows the same pattern: select, listen, change.", cards=[
            ["Select", "document.getElementById('total') or document.querySelector('.card') returns an element; "
             "querySelectorAll returns all matches."],
            ["Listen", "element.addEventListener('click', handler) runs the handler function when the event happens."],
            ["Change", "Set textContent, change attributes such as src or disabled, or add and remove CSS classes with classList."],
            ["Create", "document.createElement('li') makes a new element; appendChild adds it to the page."],
        ]),
        TIP("Put the script tag just before the closing body tag, or add the defer attribute in the head. Otherwise the script "
            "may run before the elements exist and getElementById will return null."),
        H("Worked example 1: a running order total"),
        CODE("""
<h2>Order</h2>
<button class="add" data-name="Beignets" data-price="500">Beignets (500 FCFA)</button>
<button class="add" data-name="Soya" data-price="1000">Soya (1000 FCFA)</button>
<ul id="items"></ul>
<p>Total: <span id="total">0</span> FCFA</p>
<script src="order.js"></script>
""", "html", title="Listing 1", caption="Order page: each button stores the item name and price in data attributes"),
        EX("Worked example 1: adding items and updating the total", intro=(
            "Using Listing 1, write a script so that clicking an item adds it to the list and updates the total. "
            "Listing 2 shows the script."), steps=[
            S("Select the elements", text="Get the list with getElementById('items'), the total span with "
              "getElementById('total'), and all item buttons with querySelectorAll('.add')."),
            S("Keep the total in a variable", text="let total = 0; stores the running total as a number."),
            S("Listen to each button", text="Loop over the buttons with forEach and add a click listener to each one."),
            S("Read the data", text="Inside the handler, read button.dataset.name and convert button.dataset.price to a number "
              "with Number, because data attributes are strings."),
            S("Create a list item", text="createElement('li'), set its textContent to the name and price, and appendChild it "
              "to the list."),
            S("Update the total", text="Add the price to total and write it into the span with textContent. Clicking "
              "Beignets then Soya shows a total of 1500 FCFA."),
        ]),
        CODE("""
const list = document.getElementById('items');
const totalSpan = document.getElementById('total');
const buttons = document.querySelectorAll('.add');
let total = 0;

buttons.forEach(function (button) {
  button.addEventListener('click', function () {
    const name = button.dataset.name;
    const price = Number(button.dataset.price);

    const li = document.createElement('li');
    li.textContent = name + ' - ' + price + ' FCFA';
    list.appendChild(li);

    total = total + price;
    totalSpan.textContent = total;
  });
});
""", "javascript", title="Listing 2", caption="order.js: select, listen, create and change"),
        H("Worked example 2: validating a form"),
        CODE("""
<form id="orderForm">
  <label for="phone">Phone number</label>
  <input id="phone" type="tel">
  <p id="error" class="hidden"></p>
  <button type="submit">Send order</button>
</form>
""", "html", title="Listing 3", caption="Order form with a place for an error message"),
        EX("Worked example 2: checking the phone number before submitting", intro=(
            "Using Listing 3, stop the form from submitting if the phone number is not exactly 9 digits, and show a red error "
            "message. Assume the stand only accepts 9-digit local numbers. Listing 4 shows the script."), steps=[
            S("Listen for submit", text="Add a submit listener to the form, not a click listener to the button, so pressing "
              "Enter is also checked."),
            S("Read and tidy the value", text="Read phone.value and remove spaces at the ends with trim()."),
            S("Test the pattern", text="The regular expression in Listing 4 matches from the start to the end of the value and "
              "allows only the digits 0 to 9, exactly nine of them. Its test method returns true or false."),
            S("Stop a bad submission", text="If the test fails, call event.preventDefault() so the form is not sent."),
            S("Show the message", text="Set the error text and remove the hidden class with classList so it appears; add the "
              "error class to colour it red. If the number is valid, hide the message and let the form submit."),
        ]),
        CODE("""
const form = document.getElementById('orderForm');
const phone = document.getElementById('phone');
const error = document.getElementById('error');

form.addEventListener('submit', function (event) {
  const value = phone.value.trim();
  if (!/^[0-9]{9}$/.test(value)) {
    event.preventDefault();
    error.textContent = 'Please enter a 9-digit phone number.';
    error.classList.remove('hidden');
    error.classList.add('error');
  } else {
    error.classList.add('hidden');
  }
});
""", "javascript", title="Listing 4", caption="Client-side validation with preventDefault and classList"),
        H("Common mistakes"),
        MISTAKE("Adding numbers that are really strings", "Values from inputs and data attributes are strings, so '500' + '1000' "
                "gives '5001000'. Convert with Number() or parseInt() before adding."),
        MISTAKE("Calling the handler instead of passing it", "addEventListener('click', update()) runs update at once. Pass "
                "the function itself: addEventListener('click', update)."),
        MISTAKE("Using innerHTML with user input", "Putting text typed by users into innerHTML can run injected code. Use "
                "textContent for plain text."),
        MISTAKE("Relying only on client-side validation", "A user can disable JavaScript or send data directly. Always "
                "validate again on the server."),
        QUIZ("What does this code display in the span? let a = '2'; let b = 3; span.textContent = a + b;",
             ["5", "23", "6", "An error"], 1,
             "a is a string, so + joins the values as text: '2' followed by '3' gives '23'.",
             hint="Look at the quotation marks around 2.",
             feedback=["That would need both values to be numbers, for example Number(a) + b.", "",
                       "+ does not multiply.", "Joining a string and a number is allowed in JavaScript; it does not cause an error."]),
        QUIZ("Which line correctly hides an element with id 'menu' by adding the CSS class 'hidden'?",
             ["document.getElementById('#menu').classList.add('hidden');",
              "document.querySelector('#menu').classList.add('hidden');",
              "document.querySelector('menu').class = 'hidden';",
              "document.getElementById('menu').addClass('hidden');"], 1,
             "querySelector takes a CSS selector, so '#menu' selects the element with id menu, and classList.add adds the class.",
             feedback=["getElementById takes the id alone, without the # sign, so this returns null.", "",
                       "'menu' would select a menu element, not the id, and the property is className, not class.",
                       "addClass is a jQuery method; plain JavaScript uses classList.add."]),
        H("Practice questions"),
        PQ("Explain the term DOM and describe how JavaScript uses it to change a web page.",
           "The DOM (Document Object Model) is the browser's tree of objects representing every element of an HTML page. "
           "JavaScript selects nodes from the tree (for example with getElementById), then changes their properties such as "
           "textContent, attributes or classes, or adds and removes nodes. The browser redraws the page to show the changes."),
        PQ("Write JavaScript so that clicking a button with id 'dark' adds the class 'dark-mode' to the body element, and a "
           "second click removes it.",
           "document.getElementById('dark').addEventListener('click', function () { "
           "document.body.classList.toggle('dark-mode'); }); classList.toggle adds the class if it is missing and removes it "
           "if it is present."),
        PQ("A page has an input with id 'price' and a paragraph with id 'cost'. Delivery costs 500 FCFA. Write a script that "
           "updates the paragraph with the price plus delivery every time the price typed changes.",
           "const price = document.getElementById('price'); const cost = document.getElementById('cost'); "
           "price.addEventListener('input', function () { const p = Number(price.value); cost.textContent = 'Total: ' + "
           "(p + 500) + ' FCFA'; }); Number() is needed because input values are strings: without it, typing 2000 would show "
           "2000500 instead of 2500."),
        PQ("Give two advantages and one limitation of client-side validation.",
           "Advantages: users get instant feedback without waiting for the server; fewer invalid requests reach the server, "
           "saving bandwidth and server load. Limitation: it can be bypassed by disabling JavaScript or sending requests "
           "directly, so the server must validate again."),
        SUM("Client-side JavaScript runs in the browser and changes the page without reloading it.",
            "The DOM is a tree of objects for the page; scripts select, listen and change.",
            "Select with getElementById or querySelector; react with addEventListener.",
            "Change content with textContent and styles with classList; build elements with createElement and appendChild.",
            "Validate forms on submit with preventDefault, convert strings to numbers, and always re-check on the server."),
    ],
))

# END OF LESSONS
