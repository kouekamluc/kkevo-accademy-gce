"""ICT (A Level) Upper Sixth: draft lessons for every syllabus topic."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "upper-sixth")

LESSONS = []

# ---------------------------------------------------------------------------
# Network Engineering / Cabling and switching
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Network Engineering",
    topic="Cabling and switching",
    title="RJ-45 termination, VLANs and DHCP scopes",
    slug="rj45-termination-vlans-and-dhcp-scopes",
    minutes=30,
    summary="Terminate twisted-pair cable to T568A and T568B, explain how a switch forwards frames, divide a school LAN into VLANs and plan a DHCP scope for each one.",
    objectives=[
        "State the T568A and T568B pin orders and say when to use straight-through and crossover cables",
        "Explain how a switch learns MAC addresses and forwards frames",
        "Describe VLANs, access ports and trunk ports (IEEE 802.1Q)",
        "Plan a DHCP scope with a pool, exclusions, gateway, DNS server and lease time",
    ],
    key_concepts=["T568A", "T568B", "Straight-through cable", "Crossover cable", "MAC address table",
                  "VLAN", "Trunk port", "DHCP scope"],
    blocks=[
        H("Introduction"),
        T("Imagine a secondary school in Buea that has just received 40 computers for its new lab. The administration office "
          "also has 6 computers holding marks and fee records. All of them will plug into the same switches.\n\n"
          "Three engineering questions come up at once. How do we make the cables? How do the switches move data between "
          "machines? And how do we stop students in the lab from reaching the administration computers, while every machine "
          "still gets an IP address automatically? This lesson answers all three."),
        H("Twisted-pair cabling and RJ-45 termination"),
        D("A **UTP (unshielded twisted pair)** cable such as Cat5e or Cat6 contains **8 wires in 4 twisted pairs**: orange, "
          "green, blue and brown. Each pair has a solid wire and a white-striped wire. Twisting reduces electromagnetic "
          "interference and crosstalk.", title="UTP cable",
          note="An **RJ-45** connector has 8 pins. Holding it with the clip underneath and the gold pins facing you, pin 1 is on the left."),
        D("**T568A** and **T568B** are the two standard pin orders (from the TIA/EIA-568 standard) for terminating UTP cable "
          "in an RJ-45 connector. They differ only by swapping the orange and green pairs.", title="T568A and T568B"),
        CODE("""
Pin   T568A            T568B
 1    White-Green      White-Orange
 2    Green            Orange
 3    White-Orange     White-Green
 4    Blue             Blue
 5    White-Blue       White-Blue
 6    Orange           Green
 7    White-Brown      White-Brown
 8    Brown            Brown
""", "text", title="Listing 1: T568A and T568B pin orders",
             caption="Pins 4, 5, 7 and 8 are identical in both standards. Only the orange and green pairs swap."),
        KEY("Which cable do I need?", "The two ends decide the cable type.",
            cards=[["Straight-through", "Same standard at both ends (B to B, or A to A). Used for unlike devices: PC to switch, switch to router."],
                   ["Crossover", "T568A at one end and T568B at the other. Traditionally used for like devices: PC to PC, switch to switch, router to router."]],
            note="Most modern switches support **Auto-MDI/MDI-X**, which detects the cable and adjusts, but you should still know the traditional rule."),
        EX("Worked example 1: making a patch cable", intro=(
            "A technician must connect a lab PC to a switch using T568B at both ends. List the steps and the wire order for pin 1 to pin 8."),
           steps=[
               S("Decide the cable type", text="PC to switch means unlike devices, so a straight-through cable: T568B at both ends."),
               S("Strip and untwist", text="Strip about 2.5 cm of the outer jacket. Untwist the pairs only as much as needed, keeping the untwisted length short (about 1.3 cm) to limit crosstalk."),
               S("Arrange the wires in T568B order", text="White-Orange, Orange, White-Green, Blue, White-Blue, Green, White-Brown, Brown."),
               S("Trim and insert", text="Cut the wires straight and push them fully into the RJ-45 so each copper end reaches the front of the connector, with the jacket inside the connector for strain relief."),
               S("Crimp and test", text="Crimp with the crimping tool, repeat at the other end, then use a cable tester: lights 1 to 8 should flash in the same order on both units."),
           ]),
        MISTAKE("Mixing the two standards by accident", "If one end is T568A and the other T568B you have made a crossover cable, not a patch cable. Decide the standard first and use it at both ends."),
        MISTAKE("Untwisting too much", "Long untwisted sections increase crosstalk and can make a Cat6 cable fail at gigabit speed. Keep the twists as close to the connector as possible."),
        H("How a switch forwards frames"),
        T("A **switch** works at layer 2 (the data link layer). It reads the **source MAC address** of each frame that arrives and "
          "records which port it came from in its **MAC address table**. It then reads the **destination MAC address**. If that "
          "address is in the table, the frame goes out of that one port only. If not, the switch **floods** it out of every port "
          "except the one it came in on. Broadcast frames are always flooded.\n\n"
          "Because each port is its own collision domain, a switch performs far better than an old hub, which repeated "
          "every signal out of every port. But all ports of a plain switch are still in **one broadcast domain**."),
        QUIZ("PC1 on port 3 sends a frame to PC7, whose MAC address is not yet in the switch's MAC address table. What does the switch do?",
             ["Drops the frame", "Floods the frame out of every port except port 3", "Sends the frame back out of port 3",
              "Sends the frame to the router"], 1,
             "An unknown destination is flooded out of all ports except the incoming one. When PC7 replies, the switch learns PC7's port.",
             feedback=["Switches do not drop frames just because the destination is unknown.", "",
                       "The switch never sends a frame back out of the port it arrived on.",
                       "The switch does not need a router to reach a destination on the same LAN."]),
        H("VLANs: several LANs on one switch"),
        D("A **VLAN (virtual LAN)** is a logical group of switch ports that forms its own broadcast domain, even though the ports "
          "share the same physical switches. Devices in different VLANs cannot talk to each other unless a router or a layer 3 "
          "switch routes between them.", title="VLAN",
          note="An **access port** belongs to one VLAN and connects an end device. A **trunk port** carries several VLANs between switches or to a router, adding an **IEEE 802.1Q tag** (containing a 12-bit VLAN ID) to each frame."),
        T("VLANs improve **security** (lab students cannot reach the administration machines directly), reduce **broadcast "
          "traffic** in each group, and make **management** easier because a user can be moved to a new VLAN by changing a "
          "port setting instead of rewiring."),
        D("A **DHCP scope** is the range of addresses a DHCP server may lease on one subnet, together with its options "
          "(subnet mask, default gateway, DNS servers, lease time). A client obtains an address in four messages: "
          "**Discover, Offer, Request, Acknowledge (DORA)**.", title="DHCP scope"),
        EX("Worked example 2: designing VLANs and a DHCP scope for a school", intro=(
            "The Buea school has an administration office (6 PCs and 1 printer), a student lab (40 PCs) and a staff Wi-Fi "
            "access point (up to 60 phones and laptops). Design the VLANs, choose IP networks and plan a DHCP scope for the lab."),
           steps=[
               S("Group users by role and security need", text="VLAN 10 ADMIN, VLAN 20 LAB, VLAN 30 STAFF-WIFI. Leave the default VLAN 1 unused for user traffic."),
               S("Give each VLAN its own network", text="VLAN 10: 192.168.10.0/24, VLAN 20: 192.168.20.0/24, VLAN 30: 192.168.30.0/24. Each /24 offers 254 usable host addresses, more than enough."),
               S("Choose the default gateway", text="The router sub-interface for each VLAN takes the .1 address, for example 192.168.20.1 for the lab."),
               S("Exclude static addresses from the lab scope", text="Reserve 192.168.20.1 to 192.168.20.20 for the gateway, the lab printer and any server that needs a fixed address."),
               S("Define the pool", text="Lease 192.168.20.21 to 192.168.20.254: that is 234 addresses for 40 PCs, leaving room for growth."),
               S("Set the options", text="Subnet mask 255.255.255.0, default gateway 192.168.20.1, a DNS server, and a lease time of 8 hours (one school day) so the addresses of absent machines are reused."),
           ]),
        CODE("""
! Switch: create the VLANs and assign ports
vlan 10
 name ADMIN
vlan 20
 name LAB
vlan 30
 name STAFF-WIFI
interface range fa0/1 - 7
 switchport mode access
 switchport access vlan 10
interface range fa0/8 - 47
 switchport mode access
 switchport access vlan 20
interface fa0/48
 switchport mode access
 switchport access vlan 30
interface gi0/1
 switchport mode trunk
!
! Router: DHCP scope for the lab VLAN
ip dhcp excluded-address 192.168.20.1 192.168.20.20
ip dhcp pool LAB
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 192.168.10.5
 lease 0 8
""", "bash", title="Listing 2: Cisco IOS-style configuration for the school design",
             caption="Ports fa0/1-7 serve the 6 admin PCs and printer, fa0/8-47 the 40 lab PCs, fa0/48 the Wi-Fi access point. The trunk on gi0/1 carries all three VLANs to the router. 'lease 0 8' means 0 days and 8 hours."),
        MISTAKE("Forgetting exclusions", "If the printer has the fixed address 192.168.20.10 but that address is still in the pool, the server may lease it to a PC and cause an IP address conflict. Always exclude static addresses."),
        MISTAKE("Thinking VLANs can talk to each other on their own", "Two VLANs are separate networks. Without a router or layer 3 switch, a lab PC cannot reach even a shared printer in the admin VLAN."),
        QUIZ("Which port type carries traffic for VLAN 10, VLAN 20 and VLAN 30 between a switch and a router?",
             ["Access port", "Trunk port", "Console port", "Crossover port"], 1,
             "A trunk port carries frames from several VLANs, each tagged with its 802.1Q VLAN ID.",
             feedback=["An access port belongs to only one VLAN.", "",
                       "A console port is for configuring the device, not for carrying user traffic.",
                       "There is no such port type; crossover describes a way of wiring a cable."]),
        H("Practice questions"),
        PQ("State the colour of the wire on pin 2 and on pin 6 in T568A and in T568B.",
           "T568A: pin 2 is Green and pin 6 is Orange. T568B: pin 2 is Orange and pin 6 is Green. The orange and green pairs swap; pins 4, 5, 7 and 8 stay the same."),
        PQ("A technician connects two old switches that do not support Auto-MDI/MDI-X. (a) Which cable is needed? (b) How should each end be terminated?",
           "(a) A crossover cable, because the two devices are alike (switch to switch). (b) One end T568A and the other end T568B."),
        PQ("A microfinance office in Bamenda uses the network 10.1.5.0/24. The router is at 10.1.5.1, a server at 10.1.5.2 and two printers at 10.1.5.3 and 10.1.5.4. Plan the DHCP scope.",
           "Exclude 10.1.5.1 to 10.1.5.4 (or a wider block such as .1 to .20 for future fixed devices). Pool: 10.1.5.5 (or .21) to 10.1.5.254. Options: subnet mask 255.255.255.0, default gateway 10.1.5.1, a DNS server (for example the office server 10.1.5.2 or the ISP's DNS server) and a lease time such as 8 hours or 1 day."),
        PQ("Give three reasons why a school should put its administration computers and its student lab in different VLANs.",
           "Security: students cannot reach the marks and fees computers directly, and traffic between the VLANs can be filtered at the router. Performance: each VLAN is a smaller broadcast domain, so less broadcast traffic reaches each PC. Management: users are grouped by role and can be moved by changing a port setting instead of rewiring."),
        H("Summary"),
        SUM("UTP cable has 4 twisted pairs; T568A and T568B differ only by swapping the orange and green pairs.",
            "Same standard at both ends gives a straight-through cable; A at one end and B at the other gives a crossover cable.",
            "A switch learns source MAC addresses, forwards known destinations to one port and floods unknown ones.",
            "A VLAN is a separate broadcast domain; access ports carry one VLAN, trunk ports carry many using 802.1Q tags.",
            "A DHCP scope needs a pool, exclusions for static devices, a gateway, DNS servers and a lease time."),
    ],
))

# ---------------------------------------------------------------------------
# Cybersecurity / Security principles
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Cybersecurity",
    topic="Security principles",
    title="The CIA triad: confidentiality, integrity and availability",
    slug="the-cia-triad",
    minutes=25,
    summary="Use the CIA triad to classify security incidents, from Mobile Money fraud to a crashed results portal, and choose controls that protect each property.",
    objectives=[
        "Define confidentiality, integrity and availability",
        "Classify a security incident by the property or properties it breaks",
        "Distinguish threats, vulnerabilities and risk",
        "Choose suitable controls for each part of the triad",
    ],
    key_concepts=["Confidentiality", "Integrity", "Availability", "Threat", "Vulnerability", "Risk",
                  "Least privilege", "Social engineering"],
    blocks=[
        H("Introduction"),
        T("A trader in Douala receives a call: \"This is your Mobile Money agent. We sent you 50 000 FCFA by mistake. Please "
          "dial this code and give us the confirmation number.\" Many Cameroonians have heard such calls. The caller wants "
          "secret information (a PIN or code) so that money can leave the account.\n\n"
          "Security professionals describe what is being attacked using three words: **confidentiality, integrity and "
          "availability**, known as the **CIA triad**. Every security incident and every security control can be explained "
          "with these three ideas."),
        H("The three properties"),
        KEY("The CIA triad", "Information is secure when all three properties hold.",
            cards=[["Confidentiality", "Only authorised people can read the data. Broken by: stolen PINs, eavesdropping, a leaked database."],
                   ["Integrity", "Data is accurate and has not been changed without authorisation. Broken by: altered marks, a modified transfer amount."],
                   ["Availability", "Authorised users can get the data and services when they need them. Broken by: power cuts, server crashes, denial-of-service attacks."]]),
        D("**Confidentiality** means preventing unauthorised disclosure of information.", title="Confidentiality",
          note="Controls: passwords and multi-factor authentication, access control lists, encryption, least privilege, staff awareness training."),
        D("**Integrity** means preventing unauthorised or accidental modification of information, and being able to detect it when it happens.", title="Integrity",
          note="Controls: hashing and checksums, digital signatures, validation and verification, audit logs, version control, write permissions."),
        D("**Availability** means that systems and data are usable by authorised people when needed.", title="Availability",
          note="Controls: backups, UPS and generators, redundant servers and links (RAID, failover), anti-DDoS protection, maintenance plans."),
        H("Threats, vulnerabilities and risk"),
        T("A **threat** is anything that could cause harm: a hacker, a fraudster, a virus, a flood, a careless employee. "
          "A **vulnerability** is a weakness that a threat could exploit: a weak password, unpatched software, no backup. "
          "**Risk** combines the two: how likely the harm is and how bad its impact would be."),
        T("**Social engineering** is a threat that attacks people instead of machines: phishing emails, fake SMS messages and "
          "calls like the Mobile Money example. The defence is awareness: a genuine operator never asks for your PIN."),
        EX("Worked example 1: classifying incidents with the CIA triad", intro=(
            "For each incident, state which property of the CIA triad is mainly broken and suggest one control. "
            "(a) A fraudster tricks a customer into revealing a Mobile Money PIN. (b) A student changes his mark from 8 to 15 "
            "in the school database. (c) The school results portal crashes on results day because too many people connect."),
           steps=[
               S("Incident (a): Mobile Money PIN", text="A secret has been disclosed to an unauthorised person, so **confidentiality** is broken first. If money is then transferred, the account balance is also changed without authorisation."),
               S("Control for (a)", text="Customer awareness (never share a PIN or code), multi-factor confirmation of transfers, and transaction alerts by SMS."),
               S("Incident (b): changed mark", text="The data is no longer accurate, so **integrity** is broken."),
               S("Control for (b)", text="Only teachers get write access (least privilege), every change is recorded in an audit log, and printed mark sheets are cross-checked."),
               S("Incident (c): portal crash", text="Authorised users cannot reach the service, so **availability** is broken."),
               S("Control for (c)", text="More server capacity or load balancing, a cached static results page, and a tested plan for peak traffic."),
           ]),
        QUIZ("A virus encrypts all files on the accounts computer of a cooperative in Bafoussam and demands payment to unlock them. Which property is MOST directly affected?",
             ["Confidentiality", "Integrity", "Availability", "Non-repudiation"], 2,
             "Ransomware stops authorised users from using their own files, which is a loss of availability. Good offline backups restore it without paying.",
             feedback=["The files are locked, not necessarily read by the attacker (though some ransomware also steals data).",
                       "The files are scrambled, but the main harm is that staff cannot use them.", "",
                       "Non-repudiation is about proving who did an action; it is not the main issue here."]),
        H("Worked example 2: protecting a microfinance office"),
        EX("Worked example 2: choosing controls for each property", intro=(
            "A microfinance office in Bamenda keeps customer savings records on one server. The manager wants a short plan "
            "that protects all three CIA properties. Propose two controls for each and justify them."),
           steps=[
               S("Confidentiality", text="Give each cashier a personal account with a strong password and only the access needed for their job (least privilege). Encrypt the server disk and backups so a stolen machine reveals nothing."),
               S("Integrity", text="Keep an audit log of every deposit and withdrawal, showing who made it and when. Use input validation so an amount like 5000O (letter O) or a negative deposit is rejected."),
               S("Availability", text="Install a UPS with a generator so power cuts do not stop the server. Back up the database every evening and keep a copy off-site."),
               S("Check the balance", text="Each property now has at least one technical and one organisational control, and no control breaks another property (encryption keys are also backed up so availability is not lost)."),
           ]),
        TIP("When a question asks you to \"justify\" a control, name the property it protects and the threat it stops. One clear sentence for each is enough."),
        MISTAKE("Confusing integrity with confidentiality", "Reading data without permission breaks confidentiality. Changing data without permission breaks integrity. A leaked list of fees is confidentiality; an edited list of fees is integrity."),
        MISTAKE("Thinking security is only about hackers", "Floods, fire, power cuts and honest mistakes also break availability and integrity. A good answer includes natural and accidental threats."),
        MISTAKE("Making systems so secure nobody can use them", "Locking everything down can destroy availability. Good security balances all three properties."),
        H("Practice questions"),
        PQ("Define the CIA triad and give one example of a control for each property.",
           "Confidentiality: only authorised people can read data (control: passwords or encryption). Integrity: data is accurate and not changed without authorisation (control: hashing, audit logs or access rights). Availability: authorised users can access data and services when needed (control: backups, UPS, redundant servers)."),
        PQ("Explain the difference between a threat and a vulnerability, using a school computer lab as an example.",
           "A threat is something that can cause harm, for example a student who wants to change marks, or a virus on a USB stick. A vulnerability is a weakness the threat can use, for example the teacher's password written on a sticky note, or antivirus software that is out of date. Risk is high when a likely threat meets a serious vulnerability."),
        PQ("A customer receives an SMS: \"Your MoMo account is blocked. Send your PIN to 6XX XXX XXX to unblock it.\" (a) Name this type of attack. (b) Which CIA property is the attacker trying to break? (c) Give two pieces of advice to the customer.",
           "(a) Phishing by SMS (often called smishing), a form of social engineering. (b) Confidentiality, because the attacker wants the secret PIN; with it they can then make unauthorised transfers. (c) Never share a PIN or one-time code with anyone, even someone claiming to be the operator; contact the operator only through its official customer service number; report the message."),
        H("Summary"),
        SUM("The CIA triad: confidentiality (no unauthorised reading), integrity (no unauthorised changes), availability (access when needed).",
            "Every incident can be classified by the property it breaks; some incidents break more than one.",
            "A threat exploits a vulnerability; risk depends on likelihood and impact.",
            "Controls include technical ones (encryption, hashing, backups, UPS) and human ones (training, least privilege, procedures).",
            "Social engineering, such as fake Mobile Money calls, is defeated mainly by awareness."),
    ],
))

# ---------------------------------------------------------------------------
# Cybersecurity / Cryptography
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Cybersecurity",
    topic="Cryptography",
    title="Cryptography: AES, RSA, PKI, digital signatures and SHA-256",
    slug="cryptography-aes-rsa-pki-and-hashing",
    minutes=30,
    summary="Compare symmetric AES with asymmetric RSA, work through a toy RSA example with small primes, and see how SHA-256 hashing, digital signatures and certificates protect online banking.",
    objectives=[
        "Compare symmetric (AES) and asymmetric (RSA) encryption",
        "Carry out a toy RSA key generation, encryption and decryption with small primes",
        "State the properties of a cryptographic hash function such as SHA-256",
        "Explain how digital signatures and PKI certificates provide authentication, integrity and non-repudiation",
    ],
    key_concepts=["Plaintext and ciphertext", "Symmetric encryption", "AES", "Asymmetric encryption", "RSA",
                  "Hash function", "SHA-256", "Digital signature", "PKI", "Digital certificate"],
    blocks=[
        H("Introduction"),
        T("When a student in Yaounde pays school fees through a bank app, the amount, the account number and the PIN all travel "
          "across the internet. Anyone on the same Wi-Fi network could capture those packets. Cryptography makes captured data "
          "useless to the eavesdropper (confidentiality), shows if anything was changed (integrity) and proves who sent it "
          "(authentication).\n\n"
          "**Plaintext** is readable data. **Encryption** uses an algorithm and a **key** to turn it into unreadable "
          "**ciphertext**, and **decryption** reverses the process. The security rests on keeping the right key secret, not on "
          "hiding the algorithm."),
        H("Symmetric encryption: AES"),
        D("In **symmetric encryption** the same secret key encrypts and decrypts. **AES (Advanced Encryption Standard)** is the "
          "most widely used symmetric cipher. It encrypts data in 128-bit blocks using a key of 128, 192 or 256 bits.", title="Symmetric encryption and AES",
          note="AES is very fast, so it is used for bulk data: Wi-Fi (WPA2/WPA3), encrypted disks, and the data part of HTTPS sessions."),
        T("The weakness of symmetric encryption is the **key distribution problem**: both sides need the same secret key, but "
          "how do you send the key safely to someone you have never met? Sending it over the same network exposes it."),
        H("Asymmetric encryption: RSA"),
        D("In **asymmetric (public-key) encryption** each person has a **key pair**: a **public key** that anyone may know and a "
          "**private key** kept secret. Data encrypted with the public key can only be decrypted with the matching private key. "
          "**RSA** is the classic example; its security relies on the difficulty of factorising a very large number n = p × q "
          "back into its two primes.", title="Asymmetric encryption and RSA",
          note="Real RSA keys use n of 2048 bits or more. RSA is much slower than AES, so it is mainly used to exchange keys and to sign."),
        KEY("AES vs RSA", "In practice the two work together (hybrid encryption).",
            cards=[["AES (symmetric)", "One shared secret key. Fast. Used for bulk data. Problem: distributing the key safely."],
                   ["RSA (asymmetric)", "Public and private key pair. Slow. Used to exchange an AES session key and to create digital signatures."]],
            note="HTTPS uses public-key cryptography to agree a session key, then AES to encrypt the actual web traffic."),
        EX("Worked example 1: a toy RSA computation", intro=(
            "Generate RSA keys with the small primes p = 5 and q = 11, choose e = 3, then encrypt the message m = 8 and decrypt the result. "
            "(Real keys use primes hundreds of digits long; small numbers just show the method.)"),
           steps=[
               S("Compute the modulus n", math=r"n = p \times q = 5 \times 11 = 55"),
               S("Compute Euler's totient", math=r"\varphi(n) = (p-1)(q-1) = 4 \times 10 = 40"),
               S("Check e is valid", text="e = 3 must share no factor with 40. Since gcd(3, 40) = 1, e = 3 is valid. Public key: (e, n) = (3, 55)."),
               S("Find d, the inverse of e mod 40", math=r"3d \equiv 1 \pmod{40} \Rightarrow d = 27,\ \text{since } 3 \times 27 = 81 = 2 \times 40 + 1"),
               S("Private key", text="(d, n) = (27, 55). Keep d secret; destroy p, q and the totient."),
               S("Encrypt m = 8 with the public key", math=r"c = m^e \bmod n = 8^3 \bmod 55 = 512 \bmod 55 = 17"),
               S("Decrypt: square repeatedly", math=r"17^2 \equiv 14,\ 17^4 \equiv 31,\ 17^8 \equiv 26,\ 17^{16} \equiv 16 \pmod{55}"),
               S("Combine the powers, since 27 = 16 + 8 + 2 + 1", math=r"17^{27} \equiv 16 \times 26 \times 14 \times 17 \equiv 8 \pmod{55}"),
           ], check=r"512 = 9 \times 55 + 17,\quad 16 \times 26 = 416 \equiv 31,\ 31 \times 14 = 434 \equiv 49,\ 49 \times 17 = 833 \equiv 8"),
        MISTAKE("Choosing e that shares a factor with the totient", "With a totient of 40, e = 5 or e = 4 has no inverse, so decryption is impossible. Always check gcd(e, totient) = 1."),
        MISTAKE("Encrypting with the private key for confidentiality", "To send a secret to Ama, encrypt with Ama's public key so only her private key can open it. Using your own private key gives a signature, not secrecy."),
        H("Hashing and SHA-256"),
        D("A **cryptographic hash function** takes input of any length and produces a fixed-length **digest**. **SHA-256** "
          "always produces 256 bits, written as 64 hexadecimal characters. Hashing is one-way: there is no key and no way to "
          "\"decrypt\" a hash.", title="Hash function"),
        KEY("Properties of a good hash function", "These properties make hashes useful for integrity and passwords.",
            cards=[["Deterministic and fixed length", "The same input always gives the same 256-bit digest, whatever the input size."],
                   ["Pre-image resistant", "Given a digest, it is infeasible to find an input that produces it."],
                   ["Collision resistant", "It is infeasible to find two different inputs with the same digest."],
                   ["Avalanche effect", "Changing one character changes about half the output bits."]]),
        CODE("""
SHA-256("abc")           = ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
SHA-256("abd")           = a52d159f262b2c6ddb724a61840befc36eb30c88877a4030b65cbe86298449c9
SHA-256("Pay 5000 FCFA") = 852f6dfd973fc61e29a6d528e4323cfe77a581abd141b7ed06f3b9c45133706e
SHA-256("Pay 6000 FCFA") = df741c950ef03283eba2e570b52d9725fb668e426702c57734798be6f007a1ec
""", "text", title="Listing 1: the avalanche effect in SHA-256",
             caption="One changed character gives a completely different digest, so any tampering with a message is detected."),
        T("Systems should store **hashes of passwords**, not the passwords. At login the typed password is hashed and compared "
          "with the stored hash. A random **salt** added to each password before hashing stops attackers from using precomputed "
          "tables of common password hashes."),
        H("Digital signatures and PKI"),
        D("A **digital signature** is created by hashing a message and encrypting the hash with the sender's **private key**. "
          "The receiver decrypts the signature with the sender's **public key** and compares the result with their own hash of "
          "the message. If they match, the message is authentic and unchanged, and the sender cannot later deny sending it "
          "(**non-repudiation**).", title="Digital signature"),
        EX("Worked example 2: signing and verifying with the toy keys", intro=(
            "Using the keys from Worked example 1 (public (3, 55), private (27, 55)), a bank signs a message whose (toy) hash is h = 9. "
            "Show how the customer's app verifies it."),
           steps=[
               S("Bank signs with its private key", math=r"s = h^d \bmod n = 9^{27} \bmod 55 = 4"),
               S("Bank sends the message and the signature s = 4", text="The message itself may be sent in plaintext or encrypted; the signature travels with it."),
               S("App recomputes the hash of the received message", text="The app hashes the message it received and gets h = 9."),
               S("App decrypts the signature with the bank's public key", math=r"s^e \bmod n = 4^3 \bmod 55 = 64 \bmod 55 = 9"),
               S("Compare", text="9 = 9, so the signature is valid: the message came from the holder of the private key and was not altered. If an attacker changed the message, its hash would no longer be 9."),
           ]),
        D("**PKI (public key infrastructure)** is the system of **certificate authorities (CAs)**, **digital certificates** and "
          "policies that links a public key to a real identity. A certificate (X.509 format) contains the owner's name, their "
          "public key, an expiry date and the **CA's digital signature**. Browsers trust a list of CAs, so they can check a "
          "bank's certificate before showing the padlock for HTTPS.", title="PKI and digital certificates"),
        QUIZ("Which statement about SHA-256 is correct?",
             ["It can be decrypted with the right key", "Its output length depends on the input length",
              "A one-character change to the input changes the digest completely", "It is used to encrypt bulk data like AES"], 2,
             "This is the avalanche effect, which is why hashes detect tampering.",
             feedback=["Hashing is one-way and uses no key; it cannot be decrypted.",
                       "SHA-256 always gives 256 bits (64 hex characters), whatever the input size.", "",
                       "A hash gives no way back to the data, so it cannot be used for encryption."]),
        QUIZ("Ama wants to send Kofi a confidential file. Which key should she use to encrypt it with RSA?",
             ["Ama's private key", "Ama's public key", "Kofi's public key", "Kofi's private key"], 2,
             "Only Kofi's private key can decrypt data encrypted with Kofi's public key.",
             feedback=["Anyone with Ama's public key could decrypt it: that is a signature, not secrecy.",
                       "Then only Ama's private key could decrypt it, and Kofi does not have it.", "",
                       "Ama never has Kofi's private key; it stays secret with Kofi."]),
        H("Practice questions"),
        PQ("Using p = 3, q = 11 and e = 3: (a) find n and the totient, (b) find d, (c) encrypt m = 4.",
           "(a) n = 3 × 11 = 33; totient = 2 × 10 = 20. (b) We need 3d ≡ 1 (mod 20). d = 7, since 3 × 7 = 21 = 20 + 1. (c) c = 4³ mod 33 = 64 mod 33 = 31. Check: decrypting gives 31⁷ mod 33 = 4."),
        PQ("Explain why a website uses both RSA and AES during an HTTPS session.",
           "RSA (public-key cryptography) solves the key distribution problem: it lets the browser and server agree a secret session key safely, and certificates signed with it prove the server's identity. But RSA is slow. AES is fast, so once both sides share the session key, all the page data is encrypted with AES. This combination is called hybrid encryption."),
        PQ("A school stores teachers' passwords as SHA-256 hashes with a salt. (a) Why not store the passwords themselves? (b) What is the purpose of the salt? (c) How is a password checked at login?",
           "(a) If the database is stolen, the attacker sees only hashes; because hashing is one-way, the passwords cannot be read back. (b) A random salt makes identical passwords produce different hashes and defeats precomputed tables of common password hashes. (c) The system adds the stored salt to the typed password, hashes it with SHA-256 and compares the result with the stored hash; access is granted only if they match."),
        PQ("Describe how a digital signature provides integrity, authentication and non-repudiation.",
           "The sender hashes the message and encrypts the hash with their private key. The receiver decrypts the signature with the sender's public key and compares it with a fresh hash of the received message. Integrity: any change to the message changes its hash, so the comparison fails. Authentication: only the owner of the private key could create a signature that the public key opens. Non-repudiation: since only the sender holds the private key, they cannot later deny signing. A certificate from a CA confirms that the public key really belongs to that sender."),
        H("Summary"),
        SUM("Symmetric encryption (AES) uses one shared key: fast, but the key must be distributed safely.",
            "Asymmetric encryption (RSA) uses a public and a private key; security rests on the difficulty of factorising n = p × q.",
            "RSA steps: n = pq, totient = (p−1)(q−1), choose e coprime to it, find d with ed ≡ 1, encrypt c = mᵉ mod n, decrypt m = cᵈ mod n.",
            "SHA-256 is a one-way hash giving a fixed 256-bit digest; it is used for integrity checks and salted password storage.",
            "A digital signature is a hash encrypted with the sender's private key; PKI certificates signed by CAs link public keys to identities."),
    ],
))

# ---------------------------------------------------------------------------
# Cybersecurity / Defence and recovery
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Cybersecurity",
    topic="Defence and recovery",
    title="Firewalls, IDS/IPS and disaster recovery planning",
    slug="firewalls-ids-ips-and-disaster-recovery",
    minutes=30,
    summary="Read and write a firewall rule set, compare intrusion detection and prevention systems, and plan backups and recovery so a business survives a disaster.",
    objectives=[
        "Describe packet-filtering, stateful and application-level firewalls",
        "Apply a firewall rule set to packets using first-match and implicit deny",
        "Compare IDS and IPS, and signature-based and anomaly-based detection",
        "Plan backups and a disaster recovery strategy using RPO and RTO",
    ],
    key_concepts=["Firewall", "Rule set", "Implicit deny", "DMZ", "IDS", "IPS", "Disaster recovery plan",
                  "Full, incremental and differential backup", "RPO", "RTO"],
    blocks=[
        H("Introduction"),
        T("A microfinance office in Bafoussam connects its savings database to the internet so that agents in the villages can "
          "record deposits. That connection is useful, but it also opens a door for attackers. And even with perfect defences, a "
          "fire, a flood or a failed disk can still destroy the data.\n\n"
          "Good security therefore has two halves: **defence** (keep attackers out and detect them quickly) and **recovery** "
          "(get the business running again after something goes wrong)."),
        H("Firewalls"),
        D("A **firewall** is hardware or software that controls traffic between networks of different trust levels, such as the "
          "office LAN and the internet, by allowing or blocking packets according to a **rule set**.", title="Firewall"),
        KEY("Types of firewall", "Each type looks deeper into the traffic than the one before.",
            cards=[["Packet filter", "Checks each packet's source and destination IP, protocol and port. Fast but simple; has no memory of connections."],
                   ["Stateful inspection", "Tracks connections, so replies to traffic that started inside are allowed back in automatically."],
                   ["Application-level (proxy)", "Understands protocols such as HTTP; can block particular websites, file types or commands. Slower."]],
            note="Public servers (web, email) are often placed in a **DMZ**, a separate network segment, so an attacker who breaks into them still cannot reach the internal LAN."),
        T("Rules are checked **from top to bottom** and the **first matching rule** decides what happens. The last rule is "
          "normally an **implicit deny**: anything not explicitly allowed is blocked. This is the principle of default deny."),
        CODE("""
Rule  Action  Protocol  Source            Destination       Dest. port
 1    ALLOW   TCP       192.168.10.0/24   any               443   (staff HTTPS out)
 2    ALLOW   UDP       192.168.10.0/24   192.168.10.53     53    (internal DNS)
 3    ALLOW   TCP       any               192.168.50.10     443   (public web server in DMZ)
 4    DENY    TCP       any               any               23    (Telnet)
 5    DENY    any       any               any               any   (implicit deny)
""", "text", title="Listing 1: firewall rule set for the microfinance office",
             caption="The LAN is 192.168.10.0/24 and the DMZ web server is 192.168.50.10. The firewall is stateful, so replies to allowed connections return automatically."),
        EX("Worked example 1: applying the rule set", intro=(
            "Using Listing 1, decide what happens to each packet and which rule decides it. "
            "(a) 192.168.10.25 to 41.202.0.10, TCP port 443. (b) 102.244.0.7 (internet) to 192.168.50.10, TCP port 443. "
            "(c) 102.244.0.7 to 192.168.50.10, TCP port 23. (d) 192.168.10.25 to 41.202.0.10, TCP port 80."),
           steps=[
               S("Packet (a)", text="Source is in 192.168.10.0/24, protocol TCP, port 443: rule 1 matches first. ALLOWED."),
               S("Packet (b)", text="Rules 1 and 2 need a LAN source, so they do not match. Rule 3 matches (any source, DMZ server, port 443). ALLOWED."),
               S("Packet (c)", text="Rules 1 to 3 do not match port 23. Rule 4 matches. DENIED."),
               S("Packet (d)", text="Port 80 (plain HTTP) is not allowed by rules 1 to 4, so it reaches rule 5. DENIED by the implicit deny. Staff must use HTTPS."),
               S("Why order matters", text="If rule 5 were moved to the top, it would match every packet first and block all traffic, including the web server."),
           ]),
        MISTAKE("Putting a broad rule above a specific one", "Because the first match wins, a rule such as ALLOW any any placed at the top makes every DENY below it useless. Put specific rules first and the default deny last."),
        H("Intrusion detection and prevention"),
        D("An **IDS (intrusion detection system)** monitors traffic or activity and **raises an alert** when it sees something "
          "suspicious. An **IPS (intrusion prevention system)** sits in the path of the traffic and can **block** the suspicious "
          "packets automatically.", title="IDS and IPS",
          note="A network-based system (NIDS/NIPS) watches a network segment; a host-based system (HIDS) watches one computer's logs and files."),
        KEY("How they detect attacks", "Most products combine both methods.",
            cards=[["Signature-based", "Compares traffic with a database of known attack patterns. Accurate for known attacks, misses new (zero-day) ones; signatures must be updated."],
                   ["Anomaly-based", "Learns normal behaviour and flags anything unusual, such as a cashier PC sending data at 3 a.m. Can catch new attacks but gives more false positives."]],
            note="A **false positive** is an alert on harmless traffic; a **false negative** is a real attack that is missed. An IPS with many false positives can block genuine users."),
        QUIZ("A bank wants a system that automatically blocks a known attack the moment it appears on the network. Which should it install?",
             ["A signature-based IDS", "A signature-based IPS", "An anomaly-based IDS", "A packet-filtering firewall only"], 1,
             "An IPS is inline and can block; signature-based detection recognises known attacks.",
             feedback=["An IDS only raises alerts; it does not block traffic.", "",
                       "An IDS does not block, and anomaly detection is aimed more at unknown attacks.",
                       "A packet filter checks addresses and ports, not attack patterns in the content."]),
        H("Disaster recovery planning"),
        D("A **disaster recovery plan (DRP)** is a documented, tested set of procedures for restoring IT systems and data after "
          "a disruptive event such as fire, flood, theft, ransomware or hardware failure.", title="Disaster recovery plan",
          note="A DRP usually includes: a risk assessment and business impact analysis, a backup strategy, recovery sites, staff roles and contact lists, and a schedule for testing the plan."),
        KEY("Recovery targets", "The business decides these before choosing the technology.",
            cards=[["RPO (recovery point objective)", "The maximum amount of data, measured in time, the business can afford to lose. An RPO of 24 hours needs at least daily backups."],
                   ["RTO (recovery time objective)", "The maximum time allowed to get the system running again after the disaster."]]),
        KEY("Backup types", "Each type trades backup time against restore time.",
            cards=[["Full", "Copies everything. Slowest to make, simplest to restore."],
                   ["Incremental", "Copies only what changed since the last backup of any type. Fast to make; restore needs the full plus every incremental in order."],
                   ["Differential", "Copies everything changed since the last full backup. Grows each day; restore needs only the full plus the latest differential."]],
            note="The **3-2-1 rule**: keep 3 copies of data, on 2 different kinds of media, with 1 copy off-site. Recovery sites can be **hot** (ready to run at once), **warm** (equipment ready, data must be loaded) or **cold** (space and power only)."),
        EX("Worked example 2: restoring after a disk failure", intro=(
            "The microfinance office makes a full backup every Sunday at 22:00 and an incremental backup Monday to Friday at 22:00. "
            "The server disk fails on Thursday at 15:00. Its RPO is 24 hours. (a) Which backups are needed to restore? "
            "(b) How much data is lost? (c) Is the RPO met? (d) What would change with differential backups?"),
           steps=[
               S("Find the last full backup", text="Sunday 22:00."),
               S("List the incrementals made since then", text="Monday, Tuesday and Wednesday at 22:00. Thursday's has not run yet."),
               S("(a) Restore order", text="Restore the Sunday full backup, then the Monday, Tuesday and Wednesday incrementals, in that order."),
               S("(b) Data lost", text="Everything entered after Wednesday 22:00 until Thursday 15:00: 17 hours of transactions. These must be re-entered from paper receipts."),
               S("(c) Compare with the RPO", text="17 hours is less than 24 hours, so the RPO is met."),
               S("(d) With differentials", text="Restore the Sunday full backup and only Wednesday's differential. Restoring is quicker, but each differential takes longer to make as the week goes on."),
           ]),
        MISTAKE("Keeping the only backup next to the server", "A fire or theft destroys both. Keep at least one copy off-site or in the cloud, and encrypt it."),
        MISTAKE("Never testing restores", "A backup that has never been restored may be corrupt or incomplete. A DRP must be tested regularly."),
        MISTAKE("Saying an IDS blocks attacks", "An IDS detects and alerts. Only an IPS (or a firewall) blocks traffic."),
        H("Practice questions"),
        PQ("Using the rule set in Listing 1, state with reasons what happens to: (a) a DNS request (UDP 53) from 192.168.10.40 to 192.168.10.53; (b) a Telnet request from 192.168.10.40 to a router on the internet.",
           "(a) Allowed by rule 2: the source is in the LAN, the protocol is UDP, the destination is the internal DNS server and the port is 53. (b) Denied by rule 4: rules 1 to 3 do not match TCP port 23, and rule 4 denies Telnet from any source."),
        PQ("Distinguish between an IDS and an IPS, and explain one disadvantage of anomaly-based detection.",
           "An IDS monitors traffic and raises alerts but does not stop the traffic; an IPS sits inline and can block or drop suspicious packets automatically. Anomaly-based detection flags anything that differs from normal behaviour, so legitimate but unusual activity (for example end-of-month processing) can trigger false positives; with an IPS this can block genuine users."),
        PQ("A school backs up its records server with a full backup every Friday evening and differential backups every other evening. The server is destroyed by fire on Wednesday afternoon. (a) Which backups are needed? (b) Give two other items that should be in the school's disaster recovery plan.",
           "(a) The previous Friday's full backup and Tuesday evening's differential (the most recent one), restored onto replacement hardware. This only works if the backups were stored off-site. (b) Any two of: a list of staff responsibilities and contact numbers; the location of off-site or cloud backups and how to access them; the RPO and RTO; arrangements for replacement hardware or a recovery site; a schedule for testing the plan."),
        H("Summary"),
        SUM("A firewall filters traffic with a rule set checked top to bottom; the first match wins and the last rule should be a default deny.",
            "Packet filters check addresses and ports, stateful firewalls track connections, application-level firewalls understand protocols.",
            "An IDS detects and alerts; an IPS sits inline and blocks. Signature-based detection finds known attacks, anomaly-based finds unusual behaviour.",
            "A disaster recovery plan sets an RPO and RTO and describes backups, recovery sites, roles and regular testing.",
            "Incremental backups are fast to make but restore needs the full plus every incremental; differential restore needs the full plus the latest differential."),
    ],
))

# ---------------------------------------------------------------------------
# Productivity & Project Management / Advanced Excel
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Productivity & Project Management",
    topic="Advanced Excel",
    title="Advanced Excel: lookups, pivot tables, Solver and VBA macros",
    slug="advanced-excel-lookups-pivots-solver-vba",
    minutes=30,
    summary="Use XLOOKUP and INDEX/MATCH to find data, plan a pivot table to summarise sales, set up Solver to find the best production mix, and automate a task with a VBA macro.",
    objectives=[
        "Write XLOOKUP formulas, including a not-found value and approximate matching",
        "Combine INDEX and MATCH for one-way and two-way lookups",
        "Plan a pivot table by choosing rows, columns, values and filters",
        "Set up a Solver model with an objective, variable cells and constraints",
        "Read and write a simple VBA macro",
    ],
    key_concepts=["XLOOKUP", "INDEX", "MATCH", "Absolute reference", "Pivot table", "Solver", "VBA macro"],
    blocks=[
        H("Introduction"),
        T("A school bursar in Kumba keeps fee payments for 400 students in one Excel sheet. Parents arrive asking \"How much has "
          "my child paid?\" Scrolling through 400 rows is slow and error-prone. A provision store with branches in Bafoussam, "
          "Dschang and Mbouda faces the same problem with thousands of sales records.\n\n"
          "Advanced Excel tools solve these problems: **lookup functions** find one record instantly, **pivot tables** summarise "
          "thousands of rows in seconds, **Solver** finds the best decision under constraints, and **VBA macros** automate "
          "repeated jobs."),
        H("Looking up data with XLOOKUP"),
        D("**XLOOKUP** searches one range for a value and returns the matching item from another range. It replaces the older "
          "VLOOKUP and HLOOKUP and is available in Excel 2021 and Microsoft 365.", title="XLOOKUP",
          note="Arguments: lookup_value, lookup_array, return_array, then optional if_not_found, match_mode (0 exact, -1 exact or next smaller, 1 exact or next larger) and search_mode."),
        CODE("""
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])

Sample data (sheet Fees):
      A        B            C       D
 1    ID       Name         Class   Fees paid (FCFA)
 2    S101     Ngwa Paul    L6A     75000
 3    S102     Fon Mary     L6B     50000
 4    S103     Tabi Eric    U6A     90000
 5    S104     Ewane Joy    U6A     60000
""", "text", title="Listing 1: XLOOKUP syntax and sample data"),
        EX("Worked example 1: XLOOKUP for the bursar", intro=(
            "Using Listing 1, the bursar types a student ID in G2. Write formulas that (a) return the student's name, "
            "(b) show \"Not found\" for a wrong ID, (c) return the name, class and fees in one go."),
           steps=[
               S("Identify the three ranges", text="Look for the ID in A2:A5 (lookup_array) and return from B2:B5 (return_array)."),
               S("(a) Basic formula", text="=XLOOKUP(G2, A2:A5, B2:B5). If G2 contains S103 the result is Tabi Eric."),
               S("(b) Add the if_not_found argument", text="=XLOOKUP(G2, A2:A5, B2:B5, \"Not found\"). For S999 the cell shows Not found instead of the error #N/A."),
               S("(c) Return several columns", text="=XLOOKUP(G2, A2:A5, B2:D5). The result spills across three cells: Tabi Eric, U6A, 90000."),
           ]),
        CODE("""
In H2, then copied down to H40:
=XLOOKUP(G2, $A$2:$A$401, $D$2:$D$401, "Not found")

Approximate match: grade from the school's own scale (lower bounds in K2:K6, grades in L2:L6)
=XLOOKUP(B2, $K$2:$K$6, $L$2:$L$6, , -1)
""", "text", title="Listing 2: absolute references and approximate matching",
             caption="The dollar signs lock the ranges so they do not shift when the formula is copied. match_mode -1 returns the grade for the largest lower bound that is not above the mark."),
        MISTAKE("Copying a lookup formula without absolute references", "If the ranges are relative, copying the formula down one row shifts A2:A401 to A3:A402 and records are silently missed. Lock the lookup and return ranges as in Listing 2 (press F4 after selecting a range)."),
        H("INDEX and MATCH"),
        D("**MATCH(lookup_value, lookup_array, 0)** returns the **position** of a value in a range (0 means exact match). "
          "**INDEX(array, row_num, [column_num])** returns the value at a given position. Together they look up in any "
          "direction and work in every version of Excel.", title="INDEX and MATCH"),
        EX("Worked example 2: one-way and two-way INDEX/MATCH", intro=(
            "(a) Using Listing 1, find the fees paid by S104 with INDEX/MATCH. (b) A store's monthly sales are in A1:D4: "
            "row 1 holds the months Jan, Feb, Mar in B1:D1; column A holds the branches Bafoussam, Dschang, Mbouda in A2:A4. "
            "Dschang's Feb sales (cell C3) are 410000 FCFA. Write a formula that returns the sales for the branch in G1 and the month in G2."),
           steps=[
               S("(a) Find the position", text="=MATCH(\"S104\", A2:A5, 0) returns 4, because S104 is the 4th item in A2:A5."),
               S("(a) Return the value at that position", text="=INDEX(D2:D5, MATCH(\"S104\", A2:A5, 0)) becomes INDEX(D2:D5, 4), which is 60000."),
               S("(b) Find the row", text="MATCH(G1, A2:A4, 0): for Dschang this gives 2."),
               S("(b) Find the column", text="MATCH(G2, B1:D1, 0): for Feb this gives 2."),
               S("(b) Combine", text="=INDEX(B2:D4, MATCH(G1, A2:A4, 0), MATCH(G2, B1:D1, 0)) becomes INDEX(B2:D4, 2, 2), the cell C3, which is 410000."),
           ]),
        MISTAKE("Leaving out the 0 in MATCH", "Without 0, MATCH assumes the data is sorted and does an approximate match, which can return the wrong row for IDs or names. Use 0 for exact matches."),
        QUIZ("Using Listing 1, what does =INDEX(B2:B5, MATCH(\"S102\", A2:A5, 0)) return?",
             ["2", "Fon Mary", "L6B", "#N/A"], 1,
             "MATCH finds S102 in position 2, and INDEX(B2:B5, 2) returns the second name, Fon Mary.",
             feedback=["2 is the result of MATCH alone; INDEX turns the position into a value.", "",
                       "L6B is in column C, but INDEX returns from B2:B5.",
                       "S102 exists in A2:A5, so there is no error."]),
        H("Pivot tables"),
        D("A **pivot table** summarises a large list by grouping it: you drag fields into **Rows**, **Columns**, **Values** "
          "(with a calculation such as Sum or Count) and **Filters**. The source data must be a clean list: one header row, one "
          "record per row, no blank rows or merged cells.", title="Pivot table"),
        EX("Worked example 3: planning a pivot table", intro=(
            "The store records each sale with the fields Date, Branch, Product, Category, Quantity and Amount (FCFA). The manager "
            "wants total sales for each category in each branch, for one month at a time. Plan the pivot table."),
           steps=[
               S("Prepare the data", text="Check there are no blank rows, then convert the range to an Excel Table (Ctrl+T) so new sales are included when the pivot table is refreshed."),
               S("Insert the pivot table", text="Insert, PivotTable, choose the Table as the source and a new worksheet as the destination."),
               S("Rows and Columns", text="Category in Rows, Branch in Columns."),
               S("Values", text="Amount in Values, summarised by Sum (Sum of Amount). Format it with thousands separators."),
               S("Filter by month", text="Put Date in Filters and group it by Months, or add a slicer, so the manager can choose one month."),
               S("Keep it up to date", text="After new data is added, use Refresh (PivotTable Analyze, Refresh); a pivot table does not update by itself."),
           ]),
        H("Solver: finding the best decision"),
        D("**Solver** is an Excel add-in that changes **variable cells** to make an **objective cell** as large or as small as "
          "possible (or equal to a target) while obeying **constraints**. For linear problems choose the Simplex LP method.", title="Solver",
          note="Example: a tailor in Bamenda makes shirts (profit 2500 FCFA each) and trousers (profit 3000 FCFA each). A shirt uses 2 m of fabric and 2 hours of work; trousers use 3 m and 1 hour. Each week there are 60 m of fabric and 40 hours of work."),
        CODE("""
B2  Number of shirts       (variable cell)
B3  Number of trousers     (variable cell)
B5  Profit         =2500*B2 + 3000*B3          (objective)
B6  Fabric used    =2*B2 + 3*B3
B7  Hours used     =2*B2 + B3

Data > Solver
  Set Objective:            $B$5    To: Max
  By Changing Variable Cells: $B$2:$B$3
  Subject to the Constraints: $B$6 <= 60
                              $B$7 <= 40
                              $B$2:$B$3 >= 0
                              $B$2:$B$3 = integer
  Solving Method:           Simplex LP

Result: B2 = 15, B3 = 10, B5 = 67500
Check:  fabric 2(15) + 3(10) = 60 m, hours 2(15) + 10 = 40 h, profit 37500 + 30000 = 67500 FCFA
""", "text", title="Listing 3: Solver model for the tailor",
             caption="Other corner points give less profit: 20 shirts only gives 50000 FCFA, 20 trousers only gives 60000 FCFA."),
        H("Automating with VBA macros"),
        D("A **macro** is a recorded or written sequence of instructions that automates a task. Excel macros are written in "
          "**VBA (Visual Basic for Applications)** in the Visual Basic Editor (Alt+F11) and saved in a macro-enabled workbook "
          "(.xlsm). Because macros can contain malicious code, Excel disables them in files from unknown sources.", title="VBA macro"),
        CODE("""
Sub FlagWeakMarks()
    ' Highlights every mark below 10 out of 20 in C2:C41 of the Marks sheet
    Dim cell As Range
    For Each cell In Worksheets("Marks").Range("C2:C41")
        If Not IsEmpty(cell.Value) And IsNumeric(cell.Value) Then
            If cell.Value < 10 Then
                cell.Interior.Color = RGB(255, 199, 206)   ' light red
            Else
                cell.Interior.ColorIndex = xlNone          ' clear old colour
            End If
        End If
    Next cell
    MsgBox "Marks checked."
End Sub
""", "vba", title="Listing 4: a VBA macro that flags weak marks",
             caption="The For Each loop visits every cell in the range; the If statement decides the colour. Assign the macro to a button so teachers can run it with one click."),
        QUIZ("A teacher saves the workbook containing Listing 4 as an ordinary .xlsx file and reopens it. What happens?",
             ["The macro runs automatically", "The macro is lost, because .xlsx files cannot store macros",
              "The macro is converted to a formula", "The marks are deleted"], 1,
             "Macros must be saved in a macro-enabled format such as .xlsm.",
             feedback=["Macros do not run automatically unless written as event procedures, and here the macro is gone.", "",
                       "Excel never converts VBA code into formulas.", "Saving in .xlsx keeps the data; only the VBA code is removed."]),
        H("Practice questions"),
        PQ("Using the data in Listing 1, write a formula that returns the class of the student whose ID is in G5, showing \"Unknown\" if the ID is not in the list. State the result when G5 contains S101.",
           "=XLOOKUP(G5, A2:A5, C2:C5, \"Unknown\"). For S101 the result is L6A. (Equivalent: =IFERROR(INDEX(C2:C5, MATCH(G5, A2:A5, 0)), \"Unknown\").)"),
        PQ("Give two advantages of INDEX/MATCH over VLOOKUP.",
           "INDEX/MATCH can return values from a column to the left of the lookup column, which VLOOKUP cannot. It refers to the return range directly instead of using a column number, so inserting or deleting columns does not break the formula. It also works for two-way lookups by using two MATCH functions."),
        PQ("A bakery in Limbe makes bread (profit 150 FCFA a loaf) and cakes (profit 400 FCFA each). A loaf uses 0.5 kg of flour, a cake 0.25 kg; each day there are at most 100 kg of flour and the oven can bake at most 300 items. Describe how you would set up Solver to maximise profit.",
           "Variable cells: B2 = loaves, B3 = cakes. Objective cell B5 = 150 times B2 plus 400 times B3, set to Max. Constraint cells: B6 = 0.5 times B2 plus 0.25 times B3 (flour), with B6 at most 100; B7 = B2 + B3 (oven), with B7 at most 300. Also B2 and B3 at least 0 and integer. Choose Simplex LP and click Solve, then check that the answer satisfies every constraint."),
        H("Summary"),
        SUM("XLOOKUP(value, lookup range, return range, not-found text, match mode) finds data in any direction and can return several columns.",
            "MATCH with 0 gives a position; INDEX returns the value at a position; two MATCH functions give a two-way lookup.",
            "Lock lookup ranges with absolute references before copying formulas.",
            "A pivot table needs clean data; choose Rows, Columns, Values and Filters, and refresh after changes.",
            "Solver changes variable cells to optimise an objective subject to constraints; VBA macros automate tasks and need .xlsm files."),
    ],
))

# ---------------------------------------------------------------------------
# Productivity & Project Management / IT project management
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Productivity & Project Management",
    topic="IT project management",
    title="IT project management: WBS, critical path and Gantt charts",
    slug="it-project-management-wbs-cpm-gantt",
    minutes=30,
    summary="Break an IT project into a work breakdown structure, find the critical path with early and late start times and float, and draw the schedule as a Gantt chart.",
    objectives=[
        "Produce a work breakdown structure for an IT project",
        "Draw up an activity table with durations and dependencies",
        "Calculate earliest and latest start and finish times, float and the critical path",
        "Draw and interpret a Gantt chart",
    ],
    key_concepts=["Project", "Work breakdown structure", "Dependency", "Critical path method", "Earliest start",
                  "Latest start", "Float", "Critical path", "Gantt chart", "Milestone"],
    blocks=[
        H("Introduction"),
        T("A secondary school in Ebolowa has received funding to build a new computer lab. The equipment must be ordered, the "
          "room wired, the network cabled, the computers set up and the teachers trained, all before the new term starts. If "
          "the cabling is late, the computers cannot be set up; if setup is late, training slips too.\n\n"
          "IT project management gives tools to plan such work: a **work breakdown structure** lists the tasks, the **critical "
          "path method** finds the tasks that cannot be delayed, and a **Gantt chart** shows the schedule on a timeline."),
        D("A **project** is a temporary piece of work with a defined start, end, budget and goal. Its success is usually judged "
          "against three linked constraints: **scope, time and cost**. Changing one (for example adding more computers) affects "
          "the others.", title="Project"),
        H("Work breakdown structure"),
        D("A **work breakdown structure (WBS)** divides the whole project into smaller and smaller deliverables until each "
          "lowest-level item (a **work package**) is small enough to estimate, assign to someone and track.", title="Work breakdown structure"),
        CODE("""
1   New computer lab
1.1   Planning
1.1.1   Survey the room and power supply
1.1.2   Order equipment
1.2   Installation
1.2.1   Install electrical wiring and trunking
1.2.2   Run network cabling
1.2.3   Set up computers
1.2.4   Configure network and software
1.3   Handover
1.3.1   Train teachers
1.3.2   Official handover (milestone)
""", "text", title="Listing 1: WBS for the computer lab project",
             caption="A WBS lists what must be delivered, not the order of work. The order comes from the dependencies."),
        H("The critical path method"),
        D("The **critical path method (CPM)** uses each activity's duration and its **dependencies** (the activities that must "
          "finish before it can start) to calculate the shortest possible project duration.", title="Critical path method",
          note="**Earliest start (ES)** and **earliest finish (EF = ES + duration)** come from a forward pass. **Latest finish (LF)** and **latest start (LS = LF − duration)** come from a backward pass. **Float = LS − ES**. Activities with zero float form the **critical path**."),
        CODE("""
Activity                                 Duration (days)   Depends on
A  Survey the room and power supply            2              -
B  Order equipment                             5              A
C  Install electrical wiring and trunking      4              A
D  Run network cabling                         3              C
E  Set up computers                            2              B, D
F  Configure network and software              3              E
G  Train teachers                              2              E
H  Official handover                           1              F, G
""", "text", title="Listing 2: activity table for the lab project"),
        EX("Worked example 1: forward pass (earliest times)", intro=(
            "Using Listing 2, calculate the earliest start and earliest finish of every activity and the minimum project duration."),
           steps=[
               S("Start activities begin at day 0", text="A: ES = 0, EF = 0 + 2 = 2."),
               S("B and C depend only on A", text="B: ES = 2, EF = 7. C: ES = 2, EF = 6."),
               S("D depends on C", text="D: ES = 6, EF = 9."),
               S("E depends on B and D: take the LARGER earliest finish", text="ES = max(7, 9) = 9, EF = 11."),
               S("F and G depend on E", text="F: ES = 11, EF = 14. G: ES = 11, EF = 13."),
               S("H depends on F and G", text="ES = max(14, 13) = 14, EF = 15. The minimum project duration is 15 days."),
           ]),
        EX("Worked example 2: backward pass, float and the critical path", intro=(
            "Continue from Worked example 1. Work backwards from day 15 to find each latest finish and latest start, then the float."),
           steps=[
               S("The end activity finishes at day 15", text="H: LF = 15, LS = 15 − 1 = 14."),
               S("F and G must finish before H starts", text="F: LF = 14, LS = 11. G: LF = 14, LS = 12."),
               S("E feeds F and G: take the SMALLER latest start", text="LF = min(11, 12) = 11, LS = 9."),
               S("B and D feed E", text="B: LF = 9, LS = 4. D: LF = 9, LS = 6."),
               S("C feeds D", text="C: LF = 6, LS = 2."),
               S("A feeds B and C: take the smaller latest start", text="LF = min(4, 2) = 2, LS = 0."),
               S("Float = LS − ES", text="A 0, B 2, C 0, D 0, E 0, F 0, G 1, H 0."),
               S("Critical path", text="The zero-float activities give A, C, D, E, F, H. Check: 2 + 4 + 3 + 2 + 3 + 1 = 15 days, equal to the project duration."),
           ]),
        CODE("""
Activity  Dur  ES  EF  LS  LF  Float  Critical?
   A       2    0   2   0   2    0      yes
   B       5    2   7   4   9    2      no
   C       4    2   6   2   6    0      yes
   D       3    6   9   6   9    0      yes
   E       2    9  11   9  11    0      yes
   F       3   11  14  11  14    0      yes
   G       2   11  13  12  14    1      no
   H       1   14  15  14  15    0      yes
""", "text", title="Listing 3: completed CPM table",
             caption="B can start up to 2 days late (for example if the supplier in Douala is slow) without delaying the handover; G has 1 day of float."),
        MISTAKE("Taking the minimum in the forward pass", "When an activity has several predecessors, its earliest start is the LARGEST of their earliest finishes, because it must wait for all of them. In the backward pass use the SMALLEST latest start of the successors."),
        MISTAKE("Calling the longest single activity the critical path", "The critical path is the longest chain of dependent activities through the whole project, not the activity with the biggest duration. B (5 days) is the longest activity here but it is not critical."),
        QUIZ("In the lab project, the equipment supplier delivers 3 days late, so B takes 8 days instead of 5. What is the new project duration?",
             ["15 days", "16 days", "18 days", "20 days"], 1,
             "B had only 2 days of float. A 3-day delay uses the float and adds 1 day: E now starts at day 2 + 8 = 10 instead of 9, so the project ends at day 16.",
             feedback=["B has only 2 days of float, so a 3-day delay cannot be absorbed completely.", "",
                       "Only the part of the delay beyond the float (1 day) moves the end date, not all 3 days.",
                       "That would mean the delay was counted more than once."]),
        H("Gantt charts"),
        D("A **Gantt chart** is a bar chart of the schedule: activities are listed down the side, time runs along the top, and "
          "each activity is a bar from its start to its finish. Float can be shown as a dotted extension and **milestones** "
          "(zero-duration events such as handover) as diamonds.", title="Gantt chart"),
        CODE("""
Day:         1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
A Survey    ## ##
B Order           ## ## ## ## ## .. ..
C Wiring          ## ## ## ##
D Cabling                     ## ## ##
E Setup                                ## ##
F Config                                     ## ## ##
G Training                                   ## ## ..
H Handover                                            ## <>

## = scheduled at earliest start    .. = float    <> = milestone
""", "text", title="Listing 4: Gantt chart for the lab project (earliest start)",
             caption="Critical activities (A, C, D, E, F, H) have no float and run end to end. Project management software such as Microsoft Project or GanttProject draws this automatically."),
        TIP("A Gantt chart shows when things happen and lets the manager track progress, but it shows dependencies less clearly than a CPM network. Use the two together."),
        QUIZ("What does a float of 0 days tell the project manager about an activity?",
             ["It can be skipped", "It is on the critical path, so any delay delays the whole project",
              "It has already finished", "It has no predecessors"], 1,
             "Zero float means ES = LS: the activity must start exactly on time.",
             feedback=["Every activity in the plan is needed; float is about timing, not importance.", "",
                       "Float is calculated in the plan before work starts; it says nothing about progress.",
                       "Activity A has no predecessors, but other critical activities like E have several."]),
        H("Practice questions"),
        PQ("A small network upgrade has these activities: P (3 days, no predecessor), Q (4 days, no predecessor), R (2 days, after P), S (5 days, after P and Q), T (3 days, after R and S). Find the earliest and latest start of each activity, the float, the critical path and the project duration.",
           "Forward pass: P ES 0 EF 3; Q ES 0 EF 4; R ES 3 EF 5; S ES max(3, 4) = 4, EF 9; T ES max(5, 9) = 9, EF 12. Duration 12 days. Backward pass: T LF 12, LS 9; S LF 9, LS 4; R LF 9, LS 7; P LF min(7, 4) = 4, LS 1; Q LF 4, LS 0. Float: P 1, Q 0, R 4, S 0, T 0. Critical path Q, S, T (4 + 5 + 3 = 12 days)."),
        PQ("Explain the difference between a work breakdown structure and a Gantt chart.",
           "A WBS is a hierarchical breakdown of the project into deliverables and work packages; it shows what must be done but not when or in what order. A Gantt chart is a timeline showing when each activity starts and finishes, how long it lasts and (often) float and milestones; it is used to schedule and track progress."),
        PQ("In the lab project (Listing 3), the teacher training (G) must be extended from 2 days to 4 days. Does the handover date change? Explain.",
           "Yes, by 1 day. G had 1 day of float (ES 11, LS 12). With 4 days, G finishes at day 11 + 4 = 15, so H cannot start until day 15 and finishes at day 16. G becomes critical and the critical path changes to A, C, D, E, G, H."),
        H("Summary"),
        SUM("A project has a defined goal, start, end and budget, and balances scope, time and cost.",
            "A work breakdown structure splits the project into deliverables and work packages.",
            "Forward pass: ES is the largest EF of the predecessors, EF = ES + duration. Backward pass: LF is the smallest LS of the successors, LS = LF − duration.",
            "Float = LS − ES; activities with zero float form the critical path, which fixes the minimum project duration.",
            "A Gantt chart shows activities as bars on a timeline, with float and milestones, and is used to schedule and track progress."),
    ],
))
