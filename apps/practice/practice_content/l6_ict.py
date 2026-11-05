"""ICT A Level (796), Lower Sixth practice sets (draft). Each set follows the matching lesson in
apps/courses/lesson_content/l6_ict.py.
"""

from .dsl import *  # noqa: F403

COURSE = ("ict", "lower-sixth")

M_HW = "Hardware Maintenance & Deployment"
M_ENT = "Enterprise Infrastructure"
M_WEB = "Web Development"

SETS = []

# ---------------------------------------------------------------------------
# PC hardware
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_HW, topic="PC hardware",
    title="Sockets, dual-channel RAM, UEFI and POST", lesson="pc-hardware-sockets-ram-uefi-post",
    questions=[
        MC("In an LGA (Land Grid Array) socket, where are the pins?", [
            C("In the socket on the motherboard; the CPU has flat contact pads", correct=True),
            C("On the underside of the CPU", why="That describes PGA, where the CPU pins fit into holes in the socket."),
            C("On the cooler", why="The cooler sits on top of the CPU with thermal paste; it has no connection pins."),
            C("There are no pins; the CPU is soldered to the board", why="A socket exists so the CPU can be fitted and removed; LGA sockets have pins."),
        ], steps=[S("Compare LGA and PGA", text="LGA: pins in the socket, pads on the CPU, risk of bent socket pins. PGA: pins on the CPU, risk of bent CPU pins.")],
           concept="CPU sockets: LGA and PGA", skill="Recall",
           hint="Think about why you keep the plastic cover on an LGA socket until the CPU is fitted."),
        MC("Which condition must be met before a new processor will work in a motherboard?", [
            C("It must fit the socket, and the chipset and firmware must support it", correct=True),
            C("It only needs to be from the same maker as the RAM", why="RAM maker has nothing to do with CPU compatibility; socket, chipset and firmware do."),
            C("Any CPU fits any socket if you press firmly", why="A CPU never needs force; a wrong socket will not fit and pressing bends pins."),
            C("It must have the same clock speed as the old CPU", why="Speed does not decide compatibility; the socket and support list do."),
        ], steps=[S("Check compatibility", text="Match the socket, then check the motherboard maker's CPU support list for chipset and firmware support.")],
           concept="CPU and motherboard compatibility", skill="Concept",
           hint="What list should you check on the motherboard maker's website before buying?"),
        NUM("A PC has one 8 GB module. The owner adds a second identical 8 GB module in the correct slot for dual-channel mode. "
            "What total memory, in GB, should the firmware setup report?", 16,
            steps=[S("Add the modules", math=r"8 + 8 = 16\ \text{GB}"),
                   S("Note the mode", text="Dual channel doubles the theoretical bandwidth, not the capacity.")],
            unit="GB", concept="Dual-channel memory installation", skill="Calculation",
            hint="Dual channel changes how fast memory is accessed. Does it change how much memory there is?"),
        MC("Two identical modules are installed side by side in slots A1 and A2, but the system reports single-channel mode. What is the most likely cause?", [
            C("Both modules are in the same channel; dual channel needs one module in each channel", correct=True),
            C("The modules are DDR5 in DDR4 slots", why="DDR4 and DDR5 slots are keyed differently, so the wrong type would not fit at all."),
            C("The CMOS battery is flat", why="A flat battery causes the date and settings to reset, not single-channel mode."),
            C("Secure Boot is enabled", why="Secure Boot checks boot software signatures; it does not affect memory channels."),
        ], steps=[S("Read the slot labels", text="A1 and A2 are both in channel A. Move one module to the manual's recommended pair, for example A2 and B2.")],
           concept="Dual-channel slot placement", skill="Application",
           hint="Look at the letters in the slot names."),
        NUM("In dual-channel mode the memory controller uses two separate 64-bit channels at the same time. What is the total width in bits?", 128,
            steps=[S("Add the channel widths", math=r"2 \times 64 = 128\ \text{bits}")],
            unit="bits", concept="Dual-channel memory bandwidth", skill="Calculation",
            hint="How many channels are there, and how wide is each?"),
        MC("Which statement about UEFI is correct?", [
            C("It supports GPT disks larger than 2 TB and Secure Boot", correct=True),
            C("It is stored on the hard disk", why="UEFI firmware is stored on a chip on the motherboard."),
            C("It can only boot from MBR disks", why="Booting from MBR is the legacy BIOS method; UEFI boots from GPT."),
            C("It replaces the operating system", why="Firmware starts the hardware and loads the operating system; it does not replace it."),
        ], steps=[S("Recall UEFI features", text="GPT support beyond 2 TB, graphical setup with mouse, faster start-up and Secure Boot.")],
           concept="BIOS and UEFI firmware", skill="Recall",
           hint="UEFI is the modern replacement for BIOS. What does it add?"),
        MC("Every morning a school PC shows an old date and asks the user to enter setup. What is the first thing to suspect?", [
            C("The coin cell battery on the motherboard is flat", correct=True),
            C("A faulty RAM module", why="Faulty RAM gives POST beep codes or crashes, not a date that resets overnight."),
            C("The boot order is wrong", why="A wrong boot order gives a 'no boot device' message, not a reset clock."),
            C("The CPU cooler is loose", why="A loose cooler causes overheating and shutdowns, not lost date settings."),
        ], steps=[S("Link symptom and part", text="The battery keeps the real-time clock running when the PC is unplugged; a flat battery loses the date overnight.")],
           concept="CMOS battery and firmware settings", skill="Application",
           hint="What keeps the clock running while the PC is unplugged?"),
        MC("A PC shows the maker's logo, then reports that no bootable device was found. Which component is the LEAST likely cause?", [
            C("The RAM", correct=True),
            C("A loose SSD data cable", why="If the disk is not detected, exactly this message appears."),
            C("The boot order in UEFI setup", why="If a USB stick or another device is tried first, the disk may never be reached."),
            C("A change of boot mode from UEFI to legacy", why="A boot mode mismatch stops the firmware finding the boot loader."),
        ], steps=[S("Note what works", text="The logo appears, so POST, CPU, RAM and graphics have passed."),
                  S("Locate the fault", text="The problem is detecting or loading the operating system: cable, boot order, boot mode or boot loader.")],
           concept="POST and boot diagnostics", skill="Reasoning",
           hint="Which parts must already be working for the logo to appear?"),
    ]))

# ---------------------------------------------------------------------------
# OS deployment
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_HW, topic="OS deployment",
    title="Installs, partitions, file systems and VMs", lesson="os-deployment-partitions-file-systems-vms",
    questions=[
        MC("A school must install the same configuration on 30 identical PCs connected to a LAN. Which method is best?", [
            C("Network deployment using PXE boot and a prepared image", correct=True),
            C("One USB stick used on each PC in turn", why="This works but is slow, and each install may end up configured differently."),
            C("Downloading the installer from the internet on each PC", why="This uses a lot of expensive data and gives inconsistent results."),
            C("Installing from DVDs", why="DVDs are slow and many modern PCs have no optical drive."),
        ], steps=[S("Match method to scale", text="With many identical PCs on a LAN, PXE lets each one boot from a server and receive the same image quickly.")],
           concept="Installation methods: USB, PXE and imaging", skill="Application",
           hint="Which method uses the network card to boot from a server?"),
        MC("Why must each copy of a captured disk image be generalized before it is deployed?", [
            C("So that each PC gets a unique name and identifiers", correct=True),
            C("So that the image becomes smaller than 4 GB", why="Generalizing is about unique identity, not file size."),
            C("So that it can be written to an MBR disk", why="The partition table is a separate choice from generalizing the image."),
            C("So that Secure Boot is turned off", why="Generalizing does not change firmware settings."),
        ], steps=[S("Recall disk imaging", text="A reference PC's disk is copied to the others; generalizing ensures they do not all share the same name and identifiers.")],
           concept="Disk imaging and generalization", skill="Concept",
           hint="What would happen on a network if 30 PCs had the same name?"),
        NUM("What is the maximum number of primary partitions on an MBR disk?", 4,
            steps=[S("Recall the MBR limit", text="MBR allows up to 4 primary partitions, or 3 primary plus 1 extended partition holding logical drives.")],
            concept="MBR partition limits", skill="Recall",
            hint="If you need more drives, one of these can become an extended partition."),
        NUM("By default, how many partitions does Windows allow on a GPT disk?", 128,
            steps=[S("Recall the GPT figure", text="GPT supports many partitions; Windows allows 128 by default.")],
            concept="GPT partition limits", skill="Recall",
            hint="It is a power of 2, far more than MBR's limit."),
        MC("A technician must install Windows on a new 4 TB disk and use all of the space. Which choice is correct?", [
            C("GPT with UEFI", correct=True),
            C("MBR with legacy BIOS", why="MBR can only address about 2 TB with 512-byte sectors, leaving about half the disk unusable."),
            C("MBR with four primary partitions", why="More partitions do not remove MBR's size limit."),
            C("FAT32 for the system partition", why="Windows must be installed on NTFS, and FAT32 limits single files to 4 GB."),
        ], steps=[S("Check the size limit", text="MBR is limited to about 2 TB; GPT supports far larger disks and boots with UEFI.")],
           concept="Choosing MBR or GPT", skill="Application",
           hint="Compare 4 TB with the size limit of MBR."),
        NUM("A 1000 GB SSD in a UEFI PC is planned as follows: EFI System Partition and Microsoft Reserved Partition together 1 GB, "
            "Windows system partition 250 GB, recovery partition 1 GB, and all remaining space for the data partition. "
            "What is the size of the data partition in GB?", 748,
            steps=[S("Add the fixed partitions", math=r"1 + 250 + 1 = 252\ \text{GB}"),
                   S("Subtract from the disk", math=r"1000 - 252 = 748\ \text{GB}")],
            unit="GB", concept="Planning a GPT partition layout", skill="Calculation",
            hint="Add up all the partitions with a fixed size first."),
        MC("A user cannot copy a 6 GB video onto a USB stick, although the stick has 16 GB free. What is the most likely reason?", [
            C("The stick is formatted as FAT32, which limits a single file to 4 GB", correct=True),
            C("The stick is formatted as NTFS, which cannot hold video files", why="NTFS supports large files; it is the recommended fix along with exFAT."),
            C("The stick uses GPT instead of MBR", why="The problem is a file-size limit of the file system, not the partition table."),
            C("ext4 is needed for any file over 2 GB", why="ext4 is a Linux file system; Windows cannot read it without extra software."),
        ], steps=[S("Identify the limit", text="FAT32 cannot store a single file larger than 4 GB. Reformat as NTFS or exFAT for large files.")],
           concept="File systems: NTFS, ext4 and FAT32", skill="Application",
           hint="Which file system has a maximum single-file size smaller than the video?"),
        MC("Which statement about hypervisors is correct?", [
            C("A type 1 hypervisor runs directly on the hardware; a type 2 runs as an application on a normal operating system", correct=True),
            C("A type 1 hypervisor runs as an application on a laptop's operating system", why="That describes type 2; type 1 runs directly on the hardware, common on servers."),
            C("A hypervisor is a kind of partition table", why="A hypervisor creates and runs virtual machines; partition tables are MBR and GPT."),
            C("Hypervisors work without any firmware support", why="Hardware virtualization support usually has to be enabled in BIOS/UEFI setup."),
        ], steps=[S("Compare the types", text="Type 1: directly on hardware, common on servers. Type 2: an application on a desktop or laptop OS.")],
           concept="Virtual machines and hypervisors", skill="Concept",
           hint="Ask which type needs no host operating system underneath it."),
    ]))

# ---------------------------------------------------------------------------
# Business technologies
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_ENT, topic="Business technologies",
    title="E-commerce, VPNs, VoIP and learning platforms", lesson="business-technologies-ecommerce-vpn-voip",
    questions=[
        MC("A small bakery in Bafoussam sells bread every morning to three restaurants on monthly invoices. Which type of e-commerce would suit this trade?", [
            C("B2B, because the customers are businesses", correct=True),
            C("B2C, because the bakery is a small business", why="B2B or B2C depends on who the customer is, not on the seller's size."),
            C("B2C, because bread is a consumer product", why="The buyers here are restaurants, which are businesses."),
            C("Neither, because e-commerce is only for large companies", why="Any business can sell online; size does not matter."),
        ], steps=[S("Identify the customer", text="The customers are restaurants buying on invoice, so this is business-to-business.")],
           concept="B2B and B2C e-commerce", skill="Application",
           hint="Ask who is buying, not who is selling."),
        MC("Which feature is typical of a B2C online shop rather than a B2B portal?", [
            C("A public catalogue with fixed prices, a shopping cart and instant payment through a payment gateway", correct=True),
            C("Negotiated price lists and 30-day credit terms", why="Negotiated prices and credit are B2B features."),
            C("A login for each trade customer with credit limits", why="Customer accounts with credit limits are B2B features."),
            C("Large bulk orders invoiced monthly", why="Bulk orders on invoice are typical of B2B."),
        ], steps=[S("Compare the models", text="B2C: many customers, small orders, fixed prices, instant payment. B2B: accounts, invoices, negotiated prices, credit.")],
           concept="Parts of an online sales system", skill="Concept",
           hint="Think of an individual buying one tin of paint and paying at once."),
        MC("A company joins its Douala and Garoua offices so staff can share a file server securely over the internet. Which technology is this?", [
            C("Site-to-site VPN", correct=True),
            C("Remote-access VPN", why="A remote-access VPN connects one user's device, not a whole office network."),
            C("VoIP", why="VoIP carries voice calls; it does not secure file sharing between offices."),
            C("B2C e-commerce", why="B2C is selling to consumers and has nothing to do with linking offices."),
        ], steps=[S("Count what is joined", text="Two whole networks joined through VPN gateways at each end form a site-to-site VPN.")],
           concept="Remote-access and site-to-site VPNs", skill="Application",
           hint="Is one person connecting, or are two whole networks being joined?"),
        MC("A sales agent uses a VPN on hotel Wi-Fi. Which statement about the protection it gives is correct?", [
            C("It encrypts data in transit, but it does not remove malware already on the laptop", correct=True),
            C("It makes the agent completely anonymous and safe from all threats", why="A common mistake: a VPN only protects data in transit, and the provider or company can still see traffic."),
            C("It removes viruses from the laptop", why="A VPN does not clean malware from a device."),
            C("It removes the need for passwords", why="A VPN depends on strong authentication such as good passwords, certificates and multi-factor authentication."),
        ], steps=[S("State the limits", text="A VPN is an encrypted tunnel protecting data on the way; device security and strong authentication are still needed.")],
           concept="VPN protection and its limits", skill="Reasoning",
           hint="The VPN protects the tunnel. Does it protect what is already on the device?"),
        MC("What does a codec do in a VoIP system?", [
            C("It converts the voice into digital data and compresses it", correct=True),
            C("It gives voice packets priority on the router", why="That is Quality of Service (QoS), a router setting."),
            C("It encrypts the link between two offices", why="That is the job of a VPN."),
            C("It measures the delay between packets", why="Uneven delay is jitter, a problem for VoIP; the codec handles conversion and compression."),
        ], steps=[S("Recall the definition", text="The codec digitizes and compresses voice; packets travel over the network and are turned back into sound.")],
           concept="How VoIP works", skill="Recall",
           hint="The word comes from coder and decoder."),
        NUM("A branch wants up to 8 simultaneous VoIP calls. Each call needs about 90 kbps in each direction. What upload bandwidth, in kbps, do the calls need?", 720,
            steps=[S("Multiply calls by bandwidth per call", math=r"8 \times 90 = 720\ \text{kbps}")],
            unit="kbps", concept="Estimating VoIP bandwidth", skill="Calculation",
            hint="Each call needs the same bandwidth, so multiply."),
        NUM("An office link has 1 Mbps upload. Each VoIP call needs about 90 kbps per direction, and 40 percent of the upload must be kept for other traffic. "
            "What is the maximum number of simultaneous calls?", 6,
            steps=[S("Capacity available for voice", math=r"0.6 \times 1000 = 600\ \text{kbps}"),
                   S("Divide by the bandwidth per call", math=r"600 \div 90 \approx 6.7"),
                   S("Round down", text="Only whole calls are possible and 7 calls would need 630 kbps, so at most 6.")],
            concept="Estimating VoIP bandwidth", skill="Calculation",
            hint="Convert 1 Mbps to kbps, then find the share left for voice."),
        MC("Which feature makes a learning platform most suitable for staff in areas with poor connectivity?", [
            C("Content can be downloaded for offline study, and results sync when a connection returns", correct=True),
            C("It streams only high-definition video", why="Large video needs a good connection; low-connectivity platforms use compressed video."),
            C("It requires a permanent internet connection for every quiz", why="This would fail exactly where connectivity is poor."),
            C("It only runs on high-end desktop computers", why="A good platform for these areas works on low-end phones."),
        ], steps=[S("Match the feature to the problem", text="Offline download, small pages, compressed video and later syncing let learners study without a constant connection.")],
           concept="Learning platforms in low-connectivity areas", skill="Reasoning",
           hint="What should still work when the network goes down?"),
    ]))

# ---------------------------------------------------------------------------
# Green computing
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_ENT, topic="Green computing",
    title="Energy use, solar backup and e-waste", lesson="green-computing-energy-and-e-waste",
    questions=[
        MC("A 50 W router runs 24 hours a day. How much energy does it use per day?", [
            C("1.2 kWh", correct=True),
            C("50 Wh", why="That is the energy for only one hour."),
            C("2.4 kWh", why="This doubles the correct answer: 50 times 24 is 1200, not 2400."),
            C("12 kWh", why="This is ten times too large: 1200 Wh is 1.2 kWh."),
        ], steps=[S("Energy equals power times time", math=r"50\ \text{W} \times 24\ \text{h} = 1200\ \text{Wh}"),
                  S("Convert to kWh", math=r"1200 \div 1000 = 1.2\ \text{kWh}")],
           concept="Power (W) and energy (kWh)", skill="Calculation",
           hint="Multiply power by time, then remember that 1 kWh is 1000 Wh."),
        NUM("A school lab has 15 PCs using 60 W each, switched on for 8 hours a day. What is the daily energy use in kWh?", 7.2,
            steps=[S("Energy in Wh", math=r"15 \times 60 \times 8 = 7200\ \text{Wh}"),
                   S("Convert to kWh", math=r"7200 \div 1000 = 7.2\ \text{kWh}")],
            tolerance=0.01, unit="kWh", concept="Calculating daily energy use", skill="Calculation",
            hint="Find the total power of all the PCs first, then multiply by the hours."),
        NUM("A cyber café replaces 12 PCs using 80 W each with low-power units using 40 W each. They run 10 hours a day. "
            "At an example tariff of 100 FCFA per kWh, what is the saving in FCFA over 30 days?", 14400,
            steps=[S("Power saved", math=r"12 \times (80 - 40) = 480\ \text{W}"),
                   S("Energy saved per day", math=r"480 \times 10 = 4800\ \text{Wh} = 4.8\ \text{kWh}"),
                   S("Money saved per day", math=r"4.8 \times 100 = 480\ \text{FCFA}"),
                   S("Over 30 days", math=r"480 \times 30 = 14\,400\ \text{FCFA}")],
            unit="FCFA", concept="Energy and cost savings", skill="Calculation",
            hint="Work out how many watts are saved in total, then turn that into kWh per day."),
        NUM("A router, laptop and server use 200 W in total and must run for 3 hours during a power cut from a 12 V lead-acid bank "
            "with 50 percent depth of discharge. What battery capacity is needed, in Ah?", 100,
            steps=[S("Energy needed", math=r"200 \times 3 = 600\ \text{Wh}"),
                   S("Allow for depth of discharge", math=r"600 \div 0.5 = 1200\ \text{Wh}"),
                   S("Convert to amp-hours", math=r"1200 \div 12 = 100\ \text{Ah}")],
            unit="Ah", concept="Battery sizing and depth of discharge", skill="Calculation",
            hint="Only half the battery may be used, so the bank must store more than the energy needed."),
        NUM("The same office needs 600 Wh per day from solar panels. With 20 percent system losses and 5 peak sun hours, what panel power is needed, in W?", 150,
            steps=[S("Allow for losses", math=r"600 \div 0.8 = 750\ \text{Wh}"),
                   S("Divide by the sun hours", math=r"750 \div 5 = 150\ \text{W}")],
            unit="W", concept="Sizing solar PV panels", skill="Calculation",
            hint="Losses mean the panels must produce more than 600 Wh. Then share it over the sun hours."),
        MC("Why is it a mistake to size a lead-acid battery bank to exactly the energy the equipment needs?", [
            C("It forces deep discharge, which shortens the battery's life", correct=True),
            C("Lead-acid batteries cannot be recharged by solar panels", why="A charge controller charges the bank from the panels."),
            C("The inverter would then convert AC into DC", why="The inverter converts the battery's DC into AC in any case."),
            C("Batteries are measured in watts, not watt-hours", why="Battery capacity is energy (Wh) or amp-hours; watts measure power."),
        ], steps=[S("Apply depth of discharge", text="Lead-acid batteries last longer if only about half their capacity is used, so divide the energy needed by the allowed DoD.")],
           concept="Depth of discharge", skill="Reasoning",
           hint="How much of a lead-acid battery's capacity should normally be used?"),
        MC("Which is the best way to reduce the number of half-idle servers in an office?", [
            C("Virtualization: run several virtual servers on one physical server", correct=True),
            C("Leave all servers on at night so they start faster", why="Leaving machines on wastes energy; shut down or use power management."),
            C("Replace SSDs with spinning hard disks", why="SSDs use less power than spinning hard disks."),
            C("Give every user a separate printer", why="Shared network printers save energy; one device per user wastes it."),
        ], steps=[S("Match measure to problem", text="Virtualization combines several lightly used servers on one machine, cutting energy use.")],
           concept="Reducing energy use: virtualization", skill="Application",
           hint="Think of running many computers inside one physical machine."),
        MC("Which action is highest in the waste hierarchy for an old but working school computer?", [
            C("Reusing it after wiping the data and refurbishing it", correct=True),
            C("Recycling it for metals", why="Recycling is good but comes after reuse in the hierarchy."),
            C("Burning it to recover copper", why="Burning releases toxic fumes and is harmful and unsafe."),
            C("Burying it in a landfill", why="Landfill is the last resort and can leak hazardous substances such as lead and mercury."),
        ], steps=[S("Apply the hierarchy", text="Reduce, then reuse and repair, then refurbish and donate, then recycle, and only then dispose safely. Wipe data first.")],
           concept="E-waste and the waste hierarchy", skill="Application",
           hint="The computer still works. Which option keeps it in use?"),
    ]))

# ---------------------------------------------------------------------------
# Database automation
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_ENT, topic="Database automation",
    title="Triggers, stored procedures, events and macros", lesson="database-automation-triggers-procedures",
    questions=[
        MC("Which statement correctly defines a database trigger?", [
            C("SQL attached to a table that runs automatically when an INSERT, UPDATE or DELETE happens on it", correct=True),
            C("A named block of SQL that a user runs with CALL", why="That is a stored procedure; a trigger cannot be called directly."),
            C("SQL that runs at fixed times, such as every night", why="That is a scheduled event or job."),
            C("A saved list of actions run from a button in Access", why="That is a macro in a desktop database."),
        ], steps=[S("Recall the definition", text="A trigger is attached to a table and fires on a data change event.")],
           concept="Triggers", skill="Recall",
           hint="Ask what starts it: a person, a clock, or a change to a table?"),
        MC("A pharmacy must never save a sale larger than the available stock. Which kind of trigger should enforce this?", [
            C("A BEFORE INSERT trigger that raises an error with SIGNAL", correct=True),
            C("An AFTER INSERT trigger", why="By the time an AFTER trigger runs, the row has already been written."),
            C("An AFTER DELETE trigger", why="The rule concerns new sales being inserted, not rows being deleted."),
            C("A scheduled event that runs every night", why="A nightly check would come too late; the bad sale would already be saved."),
        ], steps=[S("Choose the timing", text="To stop a row being saved, the check must run before the insert. SIGNAL cancels the INSERT with a message.")],
           concept="BEFORE and AFTER triggers", skill="Reasoning",
           hint="Must the check happen before or after the row is written?"),
        MC("In an AFTER INSERT ON sales trigger, which reference gives the quantity of the sale just inserted?", [
            C("NEW.quantity", correct=True),
            C("OLD.quantity", why="A newly inserted row has no previous version, so OLD does not exist in an INSERT trigger."),
            C("sales.quantity", why="Inside a row-level trigger the inserted row is reached through NEW."),
            C("products.quantity", why="The products table holds stock, not the quantity of the sale."),
        ], steps=[S("Recall NEW and OLD", text="NEW is the new row; OLD is the row before the change, used in UPDATE and DELETE triggers.")],
           concept="NEW and OLD rows", skill="Concept",
           hint="An inserted row has only one version. Which keyword names it?"),
        MC("A trigger contains: UPDATE products SET stock = stock - NEW.quantity. The WHERE clause has been left out. What happens on each sale?", [
            C("The stock of every product is reduced by the quantity sold", correct=True),
            C("Only the product sold is reduced, as intended", why="Without WHERE product_id = NEW.product_id, the update applies to every row."),
            C("The trigger refuses to run", why="The statement is valid SQL; it simply updates all rows."),
            C("The sale is rejected", why="Nothing in the statement checks or rejects the sale."),
        ], steps=[S("Apply the rule of UPDATE", text="UPDATE without WHERE changes every row in the table, so every product's stock falls.")],
           concept="Restricting trigger updates with WHERE", skill="Reasoning",
           hint="Which rows does an UPDATE change when it has no WHERE clause?"),
        NUM("A product has stock 50. With the AFTER INSERT trigger that subtracts NEW.quantity from stock, a sale of 3 is inserted. What is the stock now?", 47,
            steps=[S("Apply the trigger", math=r"50 - 3 = 47")],
            concept="AFTER INSERT trigger to update stock", skill="Application",
            hint="The trigger subtracts the quantity of the new sale from the stock."),
        NUM("A product starts with stock 10. The BEFORE INSERT trigger rejects any sale larger than the current stock, and the AFTER INSERT trigger "
            "reduces stock. Two sales of 6 each are then attempted. What is the stock afterwards?", 4,
            steps=[S("First sale", text="6 is not greater than 10, so it is saved and stock becomes 4."),
                   S("Second sale", text="6 is greater than 4, so SIGNAL rejects it and the stock stays at 4.")],
            concept="Business rules enforced by triggers", skill="Application",
            hint="Check each sale against the stock that remains at that moment."),
        MC("Which is an advantage of a stored procedure with a parameter, such as daily_sales(IN report_date DATE)?", [
            C("The same saved SQL can produce the report for any date, keeping the logic in one place", correct=True),
            C("It runs automatically whenever a sale is inserted", why="That describes a trigger; a procedure runs only when called."),
            C("It runs by itself every night at midnight", why="That describes a scheduled event."),
            C("It can only be run from an Access form button", why="Procedures are run with CALL by users, programs or events."),
        ], steps=[S("Recall procedures", text="A procedure is a named SQL block run with CALL; a parameter lets it work for different values, such as CALL daily_sales('2026-11-05').")],
           concept="Stored procedures and parameters", skill="Concept",
           hint="What does a parameter let you change each time you call it?"),
        MC("A manager wants a list of low-stock items produced every night at 23:00, whether or not anyone uses the database. Which tool fits best?", [
            C("A scheduled event or job", correct=True),
            C("An AFTER INSERT trigger", why="A trigger runs only when rows are inserted, so nothing happens on a night with no sales."),
            C("A BEFORE UPDATE trigger", why="This runs only when a row is updated, not at a fixed time."),
            C("A form macro", why="A macro needs a user to open a form or click a button."),
        ], steps=[S("Match tool to start condition", text="The task depends on the time, not on a data change or a user, so use a scheduled event.")],
           concept="Choosing an automation tool", skill="Application",
           hint="What starts this task: a data change, a user, or the clock?"),
    ]))

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_WEB, topic="Layout",
    title="Semantic HTML5, Flexbox and Grid", lesson="layout-semantic-html5-flexbox-grid",
    questions=[
        MC("Which HTML5 element should hold a block of main navigation links?", [
            C("nav", correct=True),
            C("aside", why="aside is for related side content such as adverts or a notice box."),
            C("main", why="main holds the main content of the page, used once per page."),
            C("div", why="div has no meaning; semantic elements replace it for the main parts of a page."),
        ], steps=[S("Match element and meaning", text="nav marks a block of main navigation links, so screen readers can announce it.")],
           concept="Semantic HTML5 elements", skill="Recall",
           hint="The element name is short for the word navigation."),
        MC("Which is a benefit of using semantic elements such as header, main and footer instead of div everywhere?", [
            C("Screen readers can announce page regions and search engines understand the content better", correct=True),
            C("The page automatically becomes responsive on phones", why="Responsiveness comes from CSS such as media queries and the viewport meta tag."),
            C("The page no longer needs any CSS", why="Semantic elements describe meaning; layout and style still need CSS."),
            C("The browser downloads the page faster because div is slow", why="The benefit is meaning for accessibility and search engines, not download speed."),
        ], steps=[S("Recall the benefits", text="Semantic structure helps accessibility, search engines and maintenance.")],
           concept="Semantic HTML and accessibility", skill="Concept",
           hint="Think about software that reads the page aloud to a blind user."),
        MC("A flex container has flex-direction: row. Which property centres its items vertically?", [
            C("align-items: center", correct=True),
            C("justify-content: center", why="justify-content works on the main axis, which is horizontal for a row."),
            C("text-align: center", why="text-align centres inline text inside an element, not flex items."),
            C("grid-area: center", why="grid-area is a Grid property for placing items in named areas."),
        ], steps=[S("Find the axes", text="For a row, the main axis is horizontal and the cross axis vertical."),
                  S("Choose the property", text="align-items controls the cross axis, so it centres items vertically.")],
           concept="Flexbox main axis and cross axis", skill="Application",
           hint="Which axis is vertical when the items are in a row?"),
        MC("A student puts justify-content: space-between on each nav link, but nothing changes. What is the mistake?", [
            C("justify-content belongs on the flex container (the parent), not on the items", correct=True),
            C("justify-content only works in CSS Grid", why="justify-content is a Flexbox property too; it must simply go on the container."),
            C("The links need flex-wrap: wrap first", why="Wrapping is not required for spacing items; the property is on the wrong element."),
            C("space-between is not a valid value", why="space-between is valid and is used in the lesson to push items apart."),
        ], steps=[S("Recall container and item properties", text="justify-content and align-items go on the container; items use flex, order or align-self.")],
           concept="Flex container and flex items", skill="Reasoning",
           hint="Which element has display: flex?"),
        NUM("A grid container is 1000px wide with grid-template-columns: 1fr 3fr and no gaps. How wide is the first column, in pixels?", 250,
            steps=[S("Count the fractions", math=r"1 + 3 = 4"),
                   S("Width of one fr", math=r"1000 \div 4 = 250\ \text{px}")],
            unit="px", concept="The fr unit in CSS Grid", skill="Calculation",
            hint="Add up the fractions, then share the width equally between them."),
        NUM("A grid container is 1000px wide with grid-template-columns: 2fr 1fr 1fr and gap: 20px between columns. "
            "The fr unit shares out the space left after the gaps. How wide is the first column, in pixels?", 480,
            steps=[S("Subtract the gaps", math=r"1000 - 2 \times 20 = 960\ \text{px}"),
                   S("Width of one fr", math=r"960 \div (2 + 1 + 1) = 240\ \text{px}"),
                   S("First column", math=r"2 \times 240 = 480\ \text{px}")],
            unit="px", concept="The fr unit with gaps", skill="Calculation",
            hint="Three columns have two gaps between them. Remove those first."),
        MC("In a Grid layout, the aside is nested inside main, and grid-area: aside has no effect. Why?", [
            C("Grid only positions direct children of the grid container", correct=True),
            C("aside cannot be used with CSS Grid", why="Any element can be a grid item if it is a direct child of the grid container."),
            C("grid-template-areas only accepts header and footer", why="Area names are chosen by the author, such as main and aside."),
            C("A media query is missing", why="The media query only changes the layout on narrow screens; the problem is nesting."),
        ], steps=[S("Check the structure", text="Move aside out of main so header, main, aside and footer are all direct children of body.")],
           concept="Grid items and named areas", skill="Reasoning",
           hint="Which elements does a grid container actually arrange?"),
        MC("Which tool is best for each job: a navigation bar, and the overall page skeleton with header, sidebar, content and footer?", [
            C("Flexbox for the navigation bar; Grid for the page skeleton", correct=True),
            C("Grid for the navigation bar; Flexbox for the page skeleton", why="This reverses them: a nav bar is one direction, a page skeleton is rows and columns."),
            C("Flexbox for both, because Grid cannot make columns", why="Grid is designed for rows and columns together."),
            C("Neither; only media queries can lay out a page", why="Media queries change a layout at a screen size; Flexbox and Grid create it."),
        ], steps=[S("Compare dimensions", text="Flexbox is one-dimensional (a row or column); Grid is two-dimensional (rows and columns together).")],
           concept="Choosing Flexbox or Grid", skill="Application",
           hint="Is each job one row of items, or rows and columns at the same time?"),
    ]))

# ---------------------------------------------------------------------------
# JavaScript
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_WEB, topic="JavaScript",
    title="Client-side JavaScript and the DOM", lesson="client-side-javascript-dom-manipulation",
    questions=[
        MC("Where does client-side JavaScript run?", [
            C("In the browser on the user's device", correct=True),
            C("On the web server before the page is sent", why="That is server-side code."),
            C("In the database management system", why="Code inside the DBMS includes triggers and stored procedures, not client-side scripts."),
            C("Only on the developer's computer", why="The code is sent with the page and run by every visitor's browser."),
        ], steps=[S("Recall the definition", text="Client-side JavaScript is sent with the page and run by the browser, so it can change the page without reloading.")],
           concept="Client-side scripting", skill="Recall",
           hint="Client means the visitor's side of the connection."),
        MC("What is the DOM?", [
            C("The browser's tree of objects representing the HTML page", correct=True),
            C("A CSS rule that lays out a page in rows and columns", why="That describes CSS Grid."),
            C("A server that stores web pages", why="The DOM lives in the browser, built from the page it received."),
            C("A list of JavaScript errors", why="The DOM represents the page's elements, not errors."),
        ], steps=[S("Recall the definition", text="Each element is a node in the DOM tree; JavaScript reads and changes these objects to change the page.")],
           concept="The Document Object Model", skill="Concept",
           hint="It is a tree, and each HTML element is one of its nodes."),
        MC("What does this code display in the span? let a = '2'; let b = 3; span.textContent = a + b;", [
            C("23", correct=True),
            C("5", why="That would need both values to be numbers, for example Number(a) + b."),
            C("6", why="The + operator does not multiply."),
            C("An error", why="Joining a string and a number is allowed in JavaScript; it does not cause an error."),
        ], steps=[S("Check the types", text="a is the string '2', so + joins the values as text: '2' followed by '3' gives '23'.")],
           concept="Strings and numbers in JavaScript", skill="Reasoning",
           hint="Look at the quotation marks around 2."),
        NUM("On the order page, a customer clicks Beignets (data-price 500), then Soya (data-price 1000), then Beignets again. "
            "The script converts each price with Number and adds it to total. What total, in FCFA, is shown?", 2000,
            steps=[S("Add the prices", math=r"500 + 1000 + 500 = 2000"),
                   S("Why Number matters", text="Without Number the strings would be joined as text instead of added.")],
            unit="FCFA", concept="Running totals with event handlers", skill="Application",
            hint="Each click adds that item's price to the running total."),
        MC("Which line correctly hides an element with id 'menu' by adding the CSS class 'hidden'?", [
            C("document.querySelector('#menu').classList.add('hidden');", correct=True),
            C("document.getElementById('#menu').classList.add('hidden');", why="getElementById takes the id alone, without the # sign, so this returns null."),
            C("document.querySelector('menu').class = 'hidden';", why="'menu' selects a menu element, not the id, and the property is className, not class."),
            C("document.getElementById('menu').addClass('hidden');", why="addClass is a jQuery method; plain JavaScript uses classList.add."),
        ], steps=[S("Check the selector", text="querySelector takes a CSS selector, so '#menu' selects by id."),
                  S("Check the method", text="classList.add adds a class to the element.")],
           concept="Selecting elements and changing classes", skill="Application",
           hint="Which method expects a CSS selector with the # sign?"),
        MC("A student writes button.addEventListener('click', update()); and update runs as soon as the page loads, not on click. Why?", [
            C("The brackets call update at once; the function itself should be passed: addEventListener('click', update)", correct=True),
            C("click is not a valid event name", why="click is the standard event name used in the lesson."),
            C("addEventListener only works on forms", why="It works on any element, including buttons."),
            C("The script tag is in the wrong place", why="A misplaced script makes getElementById return null; it does not make the handler run early."),
        ], steps=[S("Spot the call", text="update() runs the function immediately and passes its result; update passes the function to run later.")],
           concept="Event listeners", skill="Reasoning",
           hint="What is the difference between update and update() ?"),
        MC("In the form validation script, why is a submit listener added to the form rather than a click listener to the button?", [
            C("So that submitting by pressing Enter is also checked", correct=True),
            C("Because buttons cannot have event listeners", why="Buttons can have listeners; the reason is to catch every way of submitting."),
            C("Because preventDefault only exists in click events", why="preventDefault is called on the submit event in the lesson's script."),
            C("Because the submit event sends data to the server for checking", why="The check runs in the browser before anything is sent."),
        ], steps=[S("Think about all routes", text="A form can be submitted by clicking the button or pressing Enter; the submit event catches both, and preventDefault stops a bad submission.")],
           concept="Form validation and preventDefault", skill="Reasoning",
           hint="How else, apart from clicking, can a user send a form?"),
        MC("Why must the server validate data again even when the page validates it with JavaScript?", [
            C("Users can disable JavaScript or send data directly, bypassing client-side checks", correct=True),
            C("Client-side validation always gives wrong results", why="Client-side checks work and give instant feedback; they can simply be bypassed."),
            C("JavaScript cannot test regular expressions", why="The lesson's script uses a regular expression's test method in the browser."),
            C("The server cannot receive form data otherwise", why="Server-side checking is for safety, not for receiving the data."),
        ], steps=[S("State the limitation", text="Client-side checks improve the user experience but can be switched off or bypassed, so the server must check again.")],
           concept="Limits of client-side validation", skill="Concept",
           hint="Who controls the browser: the website or the user?"),
    ]))
