"""A Level Computer Science (795), Lower Sixth: Networks & Software Engineering, Procedural Programming."""
from .dsl import *  # noqa: F403

COURSE = ("computer-science", "lower-sixth")

NET = "Networks & Software Engineering"
PROC = "Procedural Programming"

LESSONS = [
    # ------------------------------------------------------------------ Network models
    lesson(
        module=NET,
        topic="Network models",
        title="The OSI and TCP/IP network models",
        slug="osi-and-tcp-ip-models",
        minutes=25,
        summary="Learn the seven layers of the OSI model and the four layers of the TCP/IP model, what each layer does, and how data is encapsulated as it travels across a network.",
        objectives=[
            "Name the seven OSI layers in order and state the function of each",
            "Name the four TCP/IP layers and map them onto the OSI layers",
            "Explain encapsulation and the protocol data unit (PDU) at each layer",
            "Identify the layer at which common protocols and devices operate",
        ],
        key_concepts=["Layered model", "OSI model", "TCP/IP model", "Protocol", "Encapsulation", "Protocol data unit"],
        blocks=[
            H("Introduction"),
            T("Imagine a student at a secondary school in Bamenda sending an assignment to a teacher in Buea over the internet. "
              "The file must be split into pieces, given addresses, turned into electrical or radio signals, checked for errors "
              "and put back together at the other end.\n\n"
              "No single program does all of this. Instead, the work is divided into **layers**. Each layer does one job and "
              "only talks to the layers directly above and below it. This lesson covers the two layered models you must know: "
              "the **OSI model** and the **TCP/IP model**."),
            D("A **protocol** is an agreed set of rules for communication between devices: the format of messages, their order, "
              "and what to do when something goes wrong. Examples are HTTP, TCP, IP and Ethernet. A **layered model** groups "
              "protocols into layers, each providing a service to the layer above it.", title="Definition: protocol and layered model"),
            KEY("Why use layers?", "Layering splits a hard problem into smaller, independent problems.", cards=[
                ["Independence", "A layer can be changed (for example Wi-Fi replacing a cable) without changing the layers above it."],
                ["Standards", "Different manufacturers can build hardware and software that work together if they follow the same layer protocols."],
                ["Easier debugging", "A fault can be traced to one layer, for example a broken cable is a physical layer problem."],
            ]),
            H("The OSI 7-layer model"),
            T("The **Open Systems Interconnection (OSI)** model was published by the ISO as a reference model. It has seven layers. "
              "Layer 7 is nearest the user and layer 1 is nearest the wire. A common memory aid from layer 7 down is "
              "\"All People Seem To Need Data Processing\"."),
            CODE("""
Layer  Name           Main job                                        PDU       Examples
-----  -------------  ----------------------------------------------  --------  -----------------------
  7    Application    Network services for user programs              Data      HTTP, FTP, SMTP, DNS
  6    Presentation   Data format, encryption, compression            Data      TLS/SSL, JPEG, ASCII
  5    Session        Open, manage and close sessions (dialogues)     Data      RPC, NetBIOS
  4    Transport      End-to-end delivery, segmentation, ports,       Segment   TCP, UDP
                      flow control, error recovery
  3    Network        Logical (IP) addressing and routing             Packet    IP, ICMP; routers
  2    Data link      Framing, physical (MAC) addressing,             Frame     Ethernet, Wi-Fi; switches
                      error detection on one link (e.g. CRC)
  1    Physical       Bits as signals on the medium                   Bits      Cables, hubs, radio
""", "text", title="Figure 1. The OSI model"),
            TIP("Learn the PDU names with the layers: data at the top, then **segment** (layer 4), **packet** (layer 3), "
                "**frame** (layer 2) and **bits** (layer 1). Examiners often ask for them."),
            H("The TCP/IP model"),
            T("The **TCP/IP model** is the model the internet actually uses. It has four layers. It merges the top three OSI "
              "layers into one Application layer, and the bottom two into one Network access (link) layer."),
            IMG("cs-osi-vs-tcpip.svg",
                "OSI layers 7 to 1 on the left, TCP/IP layers on the right. Application, presentation and session map to Application (HTTP, DNS, SMTP, FTP); transport to Transport (TCP, UDP); network to Internet (IP, ICMP); data link and physical to Network access (Ethernet, Wi-Fi).",
                caption="Figure 2. Mapping the OSI layers onto the TCP/IP layers."),
            D("**Encapsulation** is the process in which each layer, on the sending side, adds its own **header** (and the data "
              "link layer also adds a **trailer**) to the data it receives from the layer above. The unit of data at each layer is "
              "its **protocol data unit (PDU)**. On the receiving side each layer removes its header and passes the rest up: "
              "this is **decapsulation**.", title="Definition: encapsulation"),
            EX("Worked example 1: encapsulating a web request", intro=(
                "A pupil in the computer lab of a school in Bamenda types a web address into a browser. Describe how the request "
                "is encapsulated using the TCP/IP model."), steps=[
                S("Application layer", text="The browser builds an HTTP GET request. This is the data."),
                S("Transport layer", text="TCP adds a header containing the source port (for example 50312), the destination port "
                  "(80 for HTTP or 443 for HTTPS) and a sequence number. The result is a segment."),
                S("Internet layer", text="IP adds a header with the source IP address of the lab PC and the destination IP address of "
                  "the web server. The result is a packet."),
                S("Network access layer", text="Ethernet adds a header with the source and destination MAC addresses (the destination is "
                  "the next hop, the school router) and a trailer containing a CRC check value. The result is a frame."),
                S("Transmission and decapsulation", text="The frame is sent as bits on the cable. The server reverses the process, removing "
                  "one header at each layer until the HTTP request reaches the web server program."),
            ]),
            CODE("""
Application:                                  [ HTTP data ]
Transport:                       [TCP hdr][ HTTP data ]                 <- segment
Internet:                 [IP hdr][TCP hdr][ HTTP data ]                <- packet
Network access:  [Eth hdr][IP hdr][TCP hdr][ HTTP data ][Eth trailer]   <- frame
""", "text", title="Figure 3. Headers added during encapsulation"),
            EX("Worked example 2: locating faults and devices by layer", intro=(
                "The ICT technician of a school network in Bamenda reports three problems. State the OSI layer most closely linked to each."),
                steps=[
                S("A cable between a PC and the switch is cut", text="Signals cannot travel, so this is a layer 1 (physical) fault."),
                S("Packets for the internet are sent the wrong way because a routing table is wrong",
                  text="Routing using IP addresses is a layer 3 (network) job."),
                S("The switch forwards frames to the wrong port because its MAC address table is corrupted",
                  text="A switch works with MAC addresses and frames, so this is layer 2 (data link)."),
                S("Conclusion", text="Physical: hubs and cables. Data link: switches and network cards. Network: routers. "
                  "Thinking in layers lets the technician test one layer at a time, starting from the bottom."),
            ]),
            H("TCP and UDP"),
            T("Both work at the transport layer. **TCP** is connection-oriented: it sets up a connection (the three-way handshake), "
              "numbers segments, sends acknowledgements and retransmits lost segments, so delivery is reliable and in order.\n\n"
              "**UDP** is connectionless: it simply sends datagrams with no acknowledgement. It is faster and has less overhead, "
              "so it suits live voice and video calls and DNS look-ups, where a late packet is useless anyway."),
            H("Common mistakes"),
            MISTAKE("Mixing up the order of the layers", "Layer 1 is physical (bottom), layer 7 is application (top). Use the memory aid and always state the number with the name."),
            MISTAKE("Saying the application layer is the program itself", "The application layer provides network services (such as HTTP) to programs. The browser uses the application layer; it is not the layer."),
            MISTAKE("Confusing MAC and IP addresses", "MAC addresses are physical addresses used on one link (layer 2). IP addresses are logical addresses used for routing between networks (layer 3)."),
            MISTAKE("Saying TCP/IP has seven layers", "TCP/IP has four layers. The OSI model is the seven-layer reference model."),
            QUIZ("At which OSI layer does a router make its forwarding decisions?",
                 ["Physical", "Data link", "Network", "Transport"], 2,
                 "A router reads the destination IP address in each packet and chooses the next hop. IP addressing and routing are layer 3 (network) functions.",
                 hint="Which address does a router look at?",
                 feedback=["The physical layer only carries bits; it makes no forwarding decisions.",
                           "Switches use MAC addresses at the data link layer. Routers look further into the packet.",
                           "",
                           "The transport layer handles end-to-end delivery between ports, not routing between networks."]),
            QUIZ("Which PDU is created at the transport layer when TCP is used?",
                 ["Frame", "Segment", "Packet", "Bit"], 1,
                 "TCP takes application data, splits it if necessary and adds a TCP header. The result is called a segment.",
                 feedback=["A frame is the data link layer PDU.", "", "A packet is the network layer PDU.", "Bits are what the physical layer sends."]),
            H("Practice questions"),
            PQ("(a) Name the seven layers of the OSI model, starting with layer 1. (b) State one function of the presentation layer. [4 marks]",
               "(a) Physical, Data link, Network, Transport, Session, Presentation, Application. "
               "(b) Any one of: translating data between formats (for example character codes), encryption and decryption, compression."),
            PQ("Explain two differences between the OSI model and the TCP/IP model. [4 marks]",
               "The OSI model has seven layers while TCP/IP has four: TCP/IP combines the OSI application, presentation and session layers "
               "into a single application layer, and combines the data link and physical layers into a network access layer. "
               "Also, OSI is a general reference model designed before its protocols, while TCP/IP was built around protocols "
               "already in use and is the model the internet is based on."),
            PQ("A mobile money app sends a payment request from a phone to a server. Explain why the request uses TCP rather than UDP. [3 marks]",
               "A payment must arrive completely and correctly. TCP is connection-oriented: it acknowledges each segment and retransmits "
               "any that are lost, and it uses sequence numbers to put segments back in order. UDP gives no guarantee of delivery or order, "
               "so part of the request could be lost without the sender knowing."),
            PQ("Describe what happens to a frame when it arrives at the destination computer. [3 marks]",
               "The data link layer checks the destination MAC address and uses the trailer (for example the CRC) to detect errors, then removes "
               "the frame header and trailer and passes the packet up. The network layer removes the IP header and passes the segment to "
               "the transport layer, which removes the TCP header, reorders segments and passes the data to the correct application using "
               "the port number. This is decapsulation."),
            SUM("Network protocols are organised into layers; each layer serves the layer above and uses the layer below.",
                "OSI layers from 1 to 7: physical, data link, network, transport, session, presentation, application.",
                "TCP/IP has four layers: network access, internet, transport, application.",
                "Encapsulation adds a header at each layer (and a trailer at the data link layer); the PDUs are data, segment, packet, frame, bits.",
                "Routers work at layer 3 with IP addresses; switches at layer 2 with MAC addresses; hubs and cables at layer 1.",
                "TCP is reliable and connection-oriented; UDP is fast and connectionless."),
        ],
    ),
    # ------------------------------------------------------------------ Addressing and errors
    lesson(
        module=NET,
        topic="Addressing and errors",
        title="IP addressing, CIDR subnetting and CRC error detection",
        slug="ip-addressing-subnetting-and-crc",
        minutes=30,
        summary="Understand IPv4 and IPv6 addresses, use CIDR notation to find network and broadcast addresses and split a network into subnets, and detect transmission errors with a cyclic redundancy check.",
        objectives=[
            "Describe the structure of IPv4 and IPv6 addresses and shorten an IPv6 address",
            "Use a CIDR prefix to find the subnet mask, network address, broadcast address and number of hosts",
            "Divide a network into equal subnets",
            "Calculate a CRC check value by modulo-2 division and use it to detect an error",
        ],
        key_concepts=["IPv4", "IPv6", "Subnet mask", "CIDR", "Network address", "Broadcast address", "CRC", "Generator polynomial"],
        blocks=[
            H("Introduction"),
            T("A school in Bamenda is building a network for its computer lab, its library and its administration block. Every device "
              "needs a unique **IP address**, and the technician wants to split the school's address range into separate **subnets** "
              "so that traffic from the lab does not slow down the bursar's office.\n\n"
              "Signals on cables and radio links are also affected by noise, so some bits arrive flipped. The receiver must be able to "
              "**detect** that a frame is damaged. In this lesson you will learn how addresses are organised and how the "
              "**cyclic redundancy check (CRC)** detects errors."),
            H("IPv4 and IPv6 addresses"),
            D("An **IPv4 address** is a 32-bit logical address, written as four bytes in **dotted decimal**, for example 192.168.10.75. "
              "Each byte (octet) is a value from 0 to 255. There are 2 to the power 32, about 4.3 billion, possible IPv4 addresses.",
              title="Definition: IPv4 address"),
            D("An **IPv6 address** is a 128-bit address, written as eight groups of four hexadecimal digits separated by colons, "
              "for example 2001:0db8:0000:0000:0000:ff00:0042:8329. IPv6 was introduced because the IPv4 address space is too small "
              "for the number of devices now connected.", title="Definition: IPv6 address"),
            T("Two rules shorten an IPv6 address. First, leading zeros in a group may be left out (0042 becomes 42). Second, **one** "
              "run of consecutive all-zero groups may be replaced by a double colon. So the address above becomes "
              "2001:db8::ff00:42:8329. The double colon can be used only once, otherwise the reader cannot tell how many groups each one hides.\n\n"
              "Some IPv4 ranges are **private**: they are used inside organisations and are not routed on the internet. They are "
              "10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16. A router using **NAT** (network address translation) lets many private "
              "devices share one public address."),
            H("Subnet masks and CIDR"),
            D("An IP address has two parts: the **network part** (which network) and the **host part** (which device on that network). "
              "The **subnet mask** has 1s over the network part and 0s over the host part. In **CIDR** (Classless Inter-Domain Routing) "
              "notation the mask is written as a prefix length after a slash: /26 means the first 26 bits are the network part.",
              title="Definition: subnet mask and CIDR"),
            KEY("Rules for a prefix /n", "For an IPv4 address with prefix length n, there are 32 minus n host bits.", cards=[
                ["Network address", "Address AND mask: all host bits set to 0. It identifies the network itself."],
                ["Broadcast address", "All host bits set to 1. A packet sent here goes to every host on the subnet."],
                ["Usable hosts", "2 to the power (32 minus n), minus 2, because the network and broadcast addresses cannot be given to devices."],
            ]),
            EX("Worked example 1: analysing 192.168.10.75/26", intro=(
                "A PC in the school lab has the address 192.168.10.75/26. Find the subnet mask, the network address, the broadcast "
                "address, the range of usable host addresses and the number of usable hosts."), steps=[
                S("Count the host bits", text="32 minus 26 = 6 host bits. The first three octets are entirely network bits, so only the last octet needs working."),
                S("Write the mask", text="26 ones = 8 + 8 + 8 + 2. The last octet is 11000000 = 192, so the mask is 255.255.255.192."),
                S("Convert the last octet of the address to binary", text="75 = 64 + 8 + 2 + 1 = 01001011."),
                S("AND with the mask to get the network address", text="01001011 AND 11000000 = 01000000 = 64. Network address: 192.168.10.64."),
                S("Set the host bits to 1 for the broadcast address", text="01111111 = 127. Broadcast address: 192.168.10.127."),
                S("State the host range and count", text="Usable hosts are 192.168.10.65 to 192.168.10.126. Number of usable hosts = 2 to the power 6, minus 2 = 64 minus 2 = 62."),
            ]),
            CODE("""
Address   75  = 0 1 | 0 0 1 0 1 1
Mask     192  = 1 1 | 0 0 0 0 0 0
                ----+------------
AND (network) = 0 1 | 0 0 0 0 0 0  = 64
Broadcast     = 0 1 | 1 1 1 1 1 1  = 127
               net  |   host bits
""", "text", title="Figure 1. Binary working for the last octet of 192.168.10.75/26"),
            TIP("Shortcut: the **block size** is 256 minus the interesting mask octet. For /26 the block size is 256 minus 192 = 64, so "
                "subnets start at 0, 64, 128 and 192. The address 75 lies in the block starting at 64. Always show the binary as well in an exam."),
            EX("Worked example 2: splitting a /24 into four subnets", intro=(
                "The school is given 192.168.20.0/24. It needs four subnets of equal size: lab (50 PCs), library (20), administration (15) "
                "and staff room (25). Find the new prefix and list each subnet."), steps=[
                S("Find the bits to borrow", text="Four subnets need 2 extra network bits, because 2 to the power 2 = 4. New prefix = 24 + 2 = /26."),
                S("Check the largest subnet fits", text="/26 leaves 6 host bits: 64 minus 2 = 62 usable hosts. The lab needs 50, so it fits."),
                S("Find the block size", text="Mask 255.255.255.192, block size 256 minus 192 = 64."),
                S("List the subnets", text="Lab 192.168.20.0/26 (hosts .1 to .62, broadcast .63). Library 192.168.20.64/26 (hosts .65 to .126, broadcast .127). "
                  "Administration 192.168.20.128/26 (hosts .129 to .190, broadcast .191). Staff room 192.168.20.192/26 (hosts .193 to .254, broadcast .255)."),
            ]),
            H("Error detection with CRC"),
            D("A **cyclic redundancy check (CRC)** treats the data bits as a polynomial and divides them by an agreed **generator "
              "polynomial** using modulo-2 arithmetic (XOR, with no carries or borrows). The remainder is the **check value**. It is "
              "sent after the data, usually in the frame trailer.", title="Definition: CRC"),
            KEY("CRC procedure", "The generator has degree k (it has k + 1 bits).", cards=[
                ["Sender", "Append k zeros to the data. Divide by the generator using XOR. Replace the k zeros with the k-bit remainder and send."],
                ["Receiver", "Divide the whole received bit string by the same generator. Remainder 0: accept. Non-zero remainder: an error has been detected."],
            ], note="CRC detects all single-bit errors and all burst errors no longer than the degree of the generator, so it is much "
                    "stronger than a single parity bit. It only detects errors; it cannot say which bit is wrong, so the frame is sent again."),
            EX("Worked example 3: calculating a CRC", intro=(
                "Data 110101 is to be sent using the generator polynomial x cubed + x + 1. Find the transmitted bit string."), steps=[
                S("Write the generator in binary", text="x cubed + x + 1 has coefficients 1, 0, 1, 1, so the generator is 1011. Its degree is 3."),
                S("Append 3 zeros", text="The dividend is 110101 000 = 110101000."),
                S("Divide with XOR", text="Whenever the leading bit of the current position is 1, XOR the generator under it. When it is 0, move on. The full working is in Figure 2."),
                S("Read the remainder", text="The last 3 bits after division are 111."),
                S("Form the transmitted string", text="Replace the appended zeros with the remainder: 110101 111, so 110101111 is sent."),
            ]),
            CODE("""
Dividend (data + 000):   110101000
XOR at bit 1:            1011
                         ---------
                         011001000
XOR at bit 2:             1011
                         ---------
                         001111000
XOR at bit 3:              1011
                         ---------
                         000100000
XOR at bit 4:               1011
                         ---------
                         000001100
Bit 5 is 0: no XOR
XOR at bit 6:                 1011
                         ---------
                         000000111
Remainder (last 3 bits):       111
""", "text", title="Figure 2. Modulo-2 division of 110101000 by 1011"),
            EX("Worked example 4: checking at the receiver", intro=(
                "Show that 110101111 is accepted, and that 110001111 (bit 4 flipped by noise) is rejected."), steps=[
                S("Divide the correct string by 1011", text="Using the same XOR steps, 110101111 leaves remainder 000, so the frame is accepted."),
                S("Divide the damaged string by 1011", text="110001111 leaves remainder 111. This is not zero, so the error is detected and the frame is discarded or a retransmission is requested."),
            ]),
            H("Common mistakes"),
            MISTAKE("Forgetting to subtract 2 from the host count", "A /26 has 64 addresses but only 62 usable hosts. The network and broadcast addresses cannot be assigned to devices."),
            MISTAKE("Appending the wrong number of zeros", "Append as many zeros as the **degree** of the generator, which is one less than its number of bits. For 1011 append 3 zeros, not 4."),
            MISTAKE("Using ordinary subtraction in CRC division", "CRC uses XOR: 1 XOR 1 = 0, 1 XOR 0 = 1, 0 XOR 0 = 0, with no borrowing."),
            QUIZ("What is the network address of the host 10.4.37.130/27?",
                 ["10.4.37.0", "10.4.37.128", "10.4.37.96", "10.4.37.159"], 1,
                 "For /27 the last octet mask is 11100000 = 224, block size 32. 130 = 10000010; AND 11100000 gives 10000000 = 128.",
                 hint="Find the block size: 256 minus the mask octet.",
                 feedback=["That would be the network address for a /24 prefix.", "",
                           "96 starts the block 96 to 127, which does not contain 130.",
                           "159 is the broadcast address of the 128 block (128 + 31)."]),
            QUIZ("Data is protected with the generator 10011. How many zeros are appended before division?",
                 ["5", "4", "3", "2"], 1,
                 "10011 represents x to the power 4 + x + 1, of degree 4, so 4 zeros are appended and the remainder has 4 bits.",
                 feedback=["5 is the number of bits in the generator, not its degree.", "", "3 would be correct for a 4-bit generator.", "Too few: the remainder has as many bits as the degree."]),
            H("Practice questions"),
            PQ("A host has IP address 172.16.45.200/20. (a) Write the subnet mask in dotted decimal. (b) Find the network address and the broadcast address. (c) How many usable host addresses are on this subnet? [6 marks]",
               "(a) 20 ones: 255.255.240.0 (third octet 11110000 = 240). "
               "(b) Third octet 45 = 00101101; AND 11110000 = 00100000 = 32. Network address 172.16.32.0. Broadcast: set the 12 host bits to 1; third octet 00101111 = 47 and last octet 255, giving 172.16.47.255. "
               "(c) 12 host bits: 2 to the power 12, minus 2 = 4096 minus 2 = 4094."),
            PQ("Shorten the IPv6 address fe80:0000:0000:0000:0204:61ff:fe9d:f156 as far as possible. State one reason for the introduction of IPv6. [3 marks]",
               "fe80::204:61ff:fe9d:f156 (three zero groups replaced by a double colon, leading zero of 0204 removed). "
               "Reason: the 32-bit IPv4 address space (about 4.3 billion addresses) is too small for the number of devices; IPv6 gives 2 to the power 128 addresses."),
            PQ("Using the generator 10011, the data 1101011011 is to be transmitted. Find the CRC check value and the transmitted bit string. [4 marks]",
               "Degree 4, so append 4 zeros: 11010110110000. XOR 10011 under each leading 1 in turn: after bit 1 the string is 01001110110000; "
               "after bit 2 it is 00000010110000; after bit 7 it is 00000000101000; after bit 9 it is 00000000001110. "
               "Remainder 1110. Transmitted string: 1101011011 1110, that is 11010110111110."),
            SUM("IPv4 addresses are 32 bits in dotted decimal; IPv6 addresses are 128 bits in eight hexadecimal groups.",
                "In CIDR notation /n gives n network bits; there are 32 minus n host bits.",
                "Network address = address AND mask (host bits 0); broadcast address has all host bits 1; usable hosts = 2 to the power of host bits, minus 2.",
                "To make 2 to the power b equal subnets, borrow b host bits; the block size gives the subnet starting addresses.",
                "CRC: append k zeros, divide by the generator with XOR, send the remainder; a non-zero remainder at the receiver means an error."),
        ],
    ),
    # ------------------------------------------------------------------ Software development
    lesson(
        module=NET,
        topic="Software development",
        title="Software development models and design diagrams",
        slug="software-development-models-and-diagrams",
        minutes=30,
        summary="Compare the Waterfall, Agile (Scrum) and Spiral development models, and learn to read and draw data flow diagrams, entity-relationship diagrams and UML use case and class diagrams.",
        objectives=[
            "Describe the stages of the Waterfall model and its strengths and weaknesses",
            "Explain how Agile development and the Scrum framework work",
            "Explain the Spiral model and its focus on risk",
            "Choose a suitable model for a given project and justify the choice",
            "Draw and interpret simple DFDs, ERDs and UML diagrams",
        ],
        key_concepts=["Software development life cycle", "Waterfall model", "Agile", "Scrum", "Spiral model",
                      "Data flow diagram", "Entity-relationship diagram", "UML"],
        blocks=[
            H("Introduction"),
            T("A group of students in Douala wants to build a mobile payment app, similar to the mobile money services people use every "
              "day to pay for taxis, airtime and school fees. Before writing any code they must decide **how** to organise the project: "
              "who decides what the app does, when it is tested, and what happens when the client changes their mind.\n\n"
              "A **software development model** answers these questions. **Design diagrams** let the team describe the system clearly "
              "before and during coding."),
            D("The **software development life cycle (SDLC)** is the series of stages a software product passes through: feasibility, "
              "requirements analysis, design, implementation (coding), testing, deployment (installation) and maintenance. "
              "Development models differ in how they order and repeat these stages.", title="Definition: SDLC"),
            H("The Waterfall model"),
            T("In the **Waterfall model** the stages are done one after another, like water falling down steps. Each stage is finished "
              "and documented (and usually signed off) before the next begins. The usual order is requirements, design, implementation, testing, deployment and maintenance. Going back to an earlier stage is possible but costly."),
            KEY("Waterfall: when it works and when it fails", "", cards=[
                ["Strengths", "Simple to manage; clear milestones and documents; suits projects with fixed, well-understood requirements (for example a payroll system following known tax rules)."],
                ["Weaknesses", "The client sees working software only near the end; changes in requirements are expensive; errors in requirements are found late."],
            ]),
            H("Agile, Scrum and the Spiral model"),
            T("**Agile** methods deliver software in small working increments, with the client involved all the time. They value working "
              "software and responding to change over long documents and rigid plans."),
            D("**Scrum** is an Agile framework. Work is done in short fixed-length **sprints** (often 1 to 4 weeks). The **product owner** "
              "keeps the **product backlog**, a prioritised list of features (user stories). At **sprint planning** the team picks items "
              "for the **sprint backlog**. A short **daily stand-up** meeting checks progress. At the end, a **sprint review** shows the "
              "working increment to the client and a **retrospective** improves the process. The **Scrum master** removes obstacles "
              "and makes sure the team follows Scrum.", title="Definition: Scrum"),
            T("The **Spiral model** (Boehm) repeats four phases in loops of growing size: determine objectives, **identify and resolve "
              "risks** (often by building a prototype), develop and test, then plan the next loop. It is driven by **risk analysis**, "
              "so it suits large, expensive or safety-critical projects where failure would be very costly. Its weaknesses are cost "
              "and the need for risk-analysis expertise."),
            EX("Worked example 1: choosing a model", intro=(
                "For each project, choose Waterfall, Agile (Scrum) or Spiral and justify your choice: (a) the student mobile payment app, "
                "where the client keeps suggesting new features; (b) a system to calculate GCE results using fixed, published rules; "
                "(c) control software for a new national power-grid monitoring system."), steps=[
                S("(a) Mobile payment app: Agile (Scrum)", text="Requirements are changing. Short sprints give the client a working "
                  "version every few weeks, so feedback (for example on the payment screen) can be included in the next sprint."),
                S("(b) Results system: Waterfall", text="The rules are fixed and well understood at the start, and strong documentation "
                  "and sign-off are needed for an official system. Few changes are expected."),
                S("(c) Power-grid software: Spiral", text="The project is large and failure is dangerous and expensive. The Spiral model's "
                  "risk analysis and prototypes in every loop reduce the chance of a costly failure."),
            ]),
            H("Design diagrams: DFDs, ERDs and UML"),
            D("A **data flow diagram (DFD)** shows how data moves through a system. It uses four symbols: **external entities** "
              "(sources or destinations of data outside the system, drawn as rectangles), **processes** (which transform data, drawn "
              "as rounded rectangles or circles), **data stores** (files or tables, drawn as open-ended rectangles) and **data flows** "
              "(labelled arrows). A **level 0 DFD** (context diagram) shows the whole system as one process; a **level 1 DFD** breaks it into main processes.",
              title="Definition: DFD"),
            EX("Worked example 2: a level 1 DFD for paying school fees", intro=(
                "A school in Bamenda lets parents pay fees with the mobile payment app. The app sends a payment confirmation to the "
                "school system, which updates the student's fee record and prints a receipt for the bursar. Draw a level 1 DFD."), steps=[
                S("Identify external entities", text="Parent, Payment app (provider) and Bursar are outside the school system."),
                S("Identify processes", text="1 Record payment; 2 Update fee balance; 3 Produce receipt."),
                S("Identify data stores", text="D1 Students; D2 Payments."),
                S("Connect them with labelled data flows", text="Every flow is labelled with the data it carries; data never flows "
                  "directly between two entities or two stores without a process in between. The result is shown in Figure 2."),
            ]),
            IMG("cs-dfd-school-fees.svg",
                "Level 1 DFD. Parent sends payment details to Payment app, which sends a confirmation to 1 Record payment. It writes to D2 Payments and sends student ID and amount to 2 Update fee balance, which uses D1 Students and sends the new balance to 3 Produce receipt, which sends a receipt to Bursar.",
                caption="Figure 2. Level 1 DFD for school fee payment. The dashed flow happens outside the school system."),
            D("An **entity-relationship diagram (ERD)** shows the **entities** (things about which data is stored, such as Student or "
              "Subject), their **attributes**, and the **relationships** between them, with their degree: one-to-one (1:1), one-to-many "
              "(1:M) or many-to-many (M:N). A many-to-many relationship cannot be stored directly in a relational database, so it is "
              "resolved with a **link entity**.", title="Definition: ERD"),
            EX("Worked example 3: resolving a many-to-many relationship", intro=(
                "A student takes many subjects and each subject is taken by many students. Draw an ERD that can be implemented in a relational database."),
                steps=[
                S("Identify the relationship", text="Student to Subject is M:N."),
                S("Create a link entity", text="Create Enrolment. Each enrolment belongs to one student and one subject."),
                S("Replace the M:N with two 1:M relationships", text="Student 1:M Enrolment and Subject 1:M Enrolment. Enrolment holds the "
                  "foreign keys StudentID and SubjectCode, plus data about the pair, such as the grade (Figure 3)."),
            ]),
            CODE("""
 +-----------+ 1        M +----------------+ M        1 +-------------+
 |  STUDENT  |------------<   ENROLMENT    >------------|   SUBJECT   |
 +-----------+            +----------------+            +-------------+
 | StudentID |            | StudentID FK   |            | SubjectCode |
 | Name      |            | SubjectCode FK |            | Title       |
 | Class     |            | Grade          |            | Teacher     |
 +-----------+            +----------------+            +-------------+
""", "text", title="Figure 3. ERD with the link entity Enrolment"),
            T("The **Unified Modelling Language (UML)** is a standard set of diagrams for object-oriented design. A **use case diagram** "
              "shows **actors** (users or other systems, drawn as stick figures) and the **use cases** (functions, drawn as ovals) they "
              "can carry out, inside a system boundary. A **class diagram** shows classes as boxes with three parts: name, attributes "
              "and methods, joined by associations. Other UML diagrams include sequence and activity diagrams."),
            IMG("cs-uml-student-payment.svg",
                "Two UML class boxes. Student: private studentID, name, feeBalance; public recordPayment(amount) and getBalance(). Payment: private paymentID, amount, date; public printReceipt(). One Student makes 0..* Payments.",
                caption="Figure 4. A small UML class diagram for the school fees system: one Student makes 0..* Payments (- private, + public)."),
            H("Common mistakes"),
            MISTAKE("Saying Agile means no planning or documentation", "Agile plans every sprint and keeps a backlog. It prefers working software over heavy documents, but it is still disciplined."),
            MISTAKE("Drawing data flows between two external entities in a DFD", "Every data flow must start or end at a process. Flows between entities are outside the system and are not shown."),
            MISTAKE("Leaving many-to-many relationships in a final ERD", "Resolve every M:N relationship with a link entity holding both foreign keys."),
            QUIZ("Which feature most clearly distinguishes the Spiral model from the Waterfall model?",
                 ["It has a testing stage", "It is driven by repeated risk analysis in each loop",
                  "It needs a requirements specification", "It produces documentation"], 1,
                 "Each loop of the Spiral model includes identifying and resolving risks, often by prototyping. Waterfall has no repeated risk-analysis phase.",
                 feedback=["Both models include testing.", "", "Both models gather requirements.", "Both models produce documentation."]),
            QUIZ("In Scrum, who is responsible for prioritising the product backlog?",
                 ["The Scrum master", "The development team", "The product owner", "The end users directly"], 2,
                 "The product owner represents the client and decides the order of items in the product backlog.",
                 feedback=["The Scrum master supports the team and removes obstacles; they do not set priorities.",
                           "The team chooses how much work to take into a sprint, but does not prioritise the product backlog.", "",
                           "Users give feedback, but the product owner makes the priority decisions."]),
            H("Practice questions"),
            PQ("State two advantages and two disadvantages of the Waterfall model. [4 marks]",
               "Advantages: easy to manage because each stage has clear deliverables and sign-off; good documentation helps maintenance; suits fixed requirements. "
               "Disadvantages: working software appears only late in the project; changes to requirements are costly; mistakes in requirements may only be found at testing or after delivery."),
            PQ("A bank in Yaounde wants a new mobile app. The managers are not sure exactly which features customers want. Recommend a development model and justify your answer. [4 marks]",
               "Agile (for example Scrum). Requirements are unclear and will change. Short sprints deliver a working increment regularly, "
               "which can be shown to the bank and to test customers at each sprint review. Their feedback is added to the product backlog "
               "and reprioritised, so the final app matches what customers actually want, and problems are found early."),
            PQ("A library system records members and books. A member can borrow many books over time, and a book can be borrowed by many members. "
               "(a) State the degree of the Member to Book relationship. (b) Explain how it should be represented in a relational design, naming suitable attributes. [4 marks]",
               "(a) Many-to-many (M:N). (b) Introduce a link entity Loan. Member 1:M Loan and Book 1:M Loan. Loan holds the foreign keys "
               "MemberID and BookID, plus attributes of the loan such as DateBorrowed and DateDue."),
            SUM("The SDLC stages are feasibility, analysis, design, implementation, testing, deployment and maintenance.",
                "Waterfall is sequential with sign-off at each stage: good for fixed requirements, poor at handling change.",
                "Agile delivers in increments; Scrum uses sprints, a product backlog, daily stand-ups, reviews and retrospectives.",
                "The Spiral model repeats loops driven by risk analysis and prototyping: suited to large, high-risk projects.",
                "DFDs show data flow (entities, processes, stores, flows); ERDs show entities and relationships; UML gives use case and class diagrams."),
        ],
    ),
    # ------------------------------------------------------------------ Structured programming
    lesson(
        module=PROC,
        topic="Structured programming",
        title="Subroutines, scope, recursion and stack frames",
        slug="subroutines-scope-recursion-stack-frames",
        minutes=30,
        summary="Write programs as subroutines with parameters, understand local and global scope, and trace recursive functions using stack frames on the call stack, with examples in C and Python.",
        objectives=[
            "Explain the principles of structured programming and top-down design",
            "Distinguish procedures from functions and parameters passed by value from those passed by reference",
            "Explain local and global scope and predict the output of programs that use them",
            "Write recursive subroutines with a base case and a general case",
            "Trace recursive calls using stack frames on the call stack",
        ],
        key_concepts=["Structured programming", "Subroutine", "Parameter", "Scope", "Local variable", "Global variable",
                      "Recursion", "Base case", "Stack frame"],
        blocks=[
            H("Introduction"),
            T("A team writing a mobile payment app does not write one enormous program. They split it into small named pieces: one checks "
              "the PIN, one calculates the transfer fee, one updates the balance, one sends the SMS receipt. Each piece can be written, "
              "tested and corrected on its own.\n\n"
              "This is **structured programming**. In this lesson you will write subroutines, control where variables can be used, "
              "and see how the computer keeps track of subroutine calls, including recursive ones, using the **call stack**."),
            D("**Structured programming** builds programs only from three control structures, **sequence**, **selection** (if, switch) "
              "and **iteration** (loops), organised into **subroutines** with one entry and one exit, and avoids unstructured jumps (goto). "
              "It is usually combined with **top-down design**: the problem is broken into sub-problems, which are broken down again "
              "until each one is small enough to code as a subroutine.", title="Definition: structured programming"),
            D("A **subroutine** is a named block of code that performs a task and can be called from elsewhere. A **function** returns "
              "a value to the caller; a **procedure** does not (in C, a void function; in Python, a function with no return value). "
              "A **parameter** is the variable named in the subroutine heading; an **argument** is the actual value passed in the call.",
              title="Definition: subroutine, function and procedure"),
            CODE("""
def transfer_fee(amount):          # amount is a parameter
    fee = amount // 100            # 1 percent, whole francs
    if fee < 50:
        fee = 50                   # minimum fee of 50 FCFA
    return fee

print(transfer_fee(25000))         # argument 25000 -> prints 250
print(transfer_fee(3000))          # 30 is below the minimum -> prints 50
""", "python", title="Listing 1. A function in Python (an imaginary fee rule)"),
            CODE("""
#include <stdio.h>

int transfer_fee(int amount)       /* function: returns an int */
{
    int fee = amount / 100;        /* integer division */
    if (fee < 50)
        fee = 50;
    return fee;
}

void print_receipt(int amount)     /* procedure: returns nothing */
{
    printf("Sent %d FCFA, fee %d FCFA\\n", amount, transfer_fee(amount));
}

int main(void)
{
    print_receipt(25000);          /* Sent 25000 FCFA, fee 250 FCFA */
    return 0;
}
""", "c", title="Listing 2. The same function in C, called from a procedure"),
            KEY("Passing parameters", "There are two ways an argument can be passed.", cards=[
                ["By value", "A copy of the argument is passed. Changes inside the subroutine do not affect the caller's variable. C passes all arguments by value."],
                ["By reference", "The address of the caller's variable is passed, so changes inside the subroutine change the original. In C this is done by passing a pointer (see the next lesson)."],
            ]),
            H("Scope and lifetime"),
            D("The **scope** of a variable is the part of the program in which it can be used. A **local variable** is declared inside a "
              "subroutine: it can only be used there and exists only while the subroutine is running. A **global variable** is declared "
              "outside all subroutines and can be used anywhere. If a local variable has the same name as a global one, the local one "
              "hides the global one inside that subroutine.", title="Definition: scope"),
            EX("Worked example 1: predicting output with local and global variables", intro=(
                "Predict the four lines printed by Listing 3."), steps=[
                S("Line 1: fee(5000)", text="Inside fee, rate = 3 creates a new local variable that hides the global. 5000 times 3, integer-divided by 100, is 150. Prints 150."),
                S("Line 2: print(rate)", text="The local rate disappeared when fee returned. The global rate is still 2. Prints 2."),
                S("Line 3: after bonus()", text="bonus declares global rate, so rate = rate + 1 changes the global variable to 3. Prints 3."),
                S("Line 4: fee(5000) again", text="fee still uses its own local rate of 3, so it prints 150. Output: 150, 2, 3, 150."),
            ]),
            CODE("""
rate = 2                     # global variable

def fee(amount):
    rate = 3                 # local variable: hides the global
    return amount * rate // 100

def bonus():
    global rate              # use the global variable
    rate = rate + 1

print(fee(5000))
print(rate)
bonus()
print(rate)
print(fee(5000))
""", "python", title="Listing 3. Local and global scope in Python"),
            H("Recursion and stack frames"),
            D("A **recursive** subroutine is one that calls itself. It must have a **base case**, which returns without a recursive call, "
              "and a **general (recursive) case**, which calls itself with a smaller problem that moves towards the base case.",
              title="Definition: recursion"),
            D("Each time a subroutine is called, a **stack frame** (activation record) is pushed onto the **call stack**. It holds the "
              "**return address**, the **parameters** and the **local variables** of that call. When the call returns, its frame is "
              "popped and execution continues at the return address. If recursion goes too deep (for example, no base case), the stack "
              "runs out of memory: a **stack overflow**.", title="Definition: stack frame and call stack"),
            CODE("""
int factorial(int n)
{
    if (n <= 1)                    /* base case */
        return 1;
    return n * factorial(n - 1);   /* general case */
}
""", "c", title="Listing 4. Recursive factorial in C"),
            EX("Worked example 2: tracing factorial(4) on the call stack", intro=(
                "main calls factorial(4). Show the stack frames and the value returned at each stage."), steps=[
                S("Winding: factorial(4)", text="n = 4 is not the base case. The frame for n = 4 is pushed and waits for factorial(3)."),
                S("Winding: factorial(3) and factorial(2)", text="Frames for n = 3 and n = 2 are pushed, each waiting for the next call."),
                S("Base case: factorial(1)", text="n = 1, so it returns 1. The stack is now 5 frames deep (main and four factorial frames). Its frame is popped."),
                S("Unwinding", text="The n = 2 frame computes 2 times 1 = 2 and is popped; n = 3 computes 3 times 2 = 6; n = 4 computes 4 times 6 = 24."),
                S("Result", text="factorial(4) returns 24 to main. Every frame has been popped. See Figure 1."),
            ]),
            IMG("cs-factorial-call-stack.svg",
                "Call stack at its deepest, top to bottom: factorial n = 1, n = 2, n = 3, n = 4, main. While unwinding the frames return 1, then 2 x 1 = 2, then 3 x 2 = 6, then 4 x 6 = 24, and main receives 24.",
                caption="Figure 1. The call stack for factorial(4). Each frame holds the return address, the parameter n and local data."),
            EX("Worked example 3: work done before and after the recursive call", intro=(
                "State the output of show(3) for the Python function in Listing 5."), steps=[
                S("Winding", text="show(3) prints 3, then calls show(2), which prints 2, then calls show(1), which prints 1, then calls show(0)."),
                S("Base case", text="show(0) returns immediately without printing."),
                S("Unwinding", text="Control returns to show(1), which runs its second print: 1. Then show(2) prints 2, then show(3) prints 3."),
                S("Output", text="3 2 1 1 2 3. Statements after the recursive call run in reverse order, as the frames are popped."),
            ]),
            CODE("""
def show(n):
    if n == 0:               # base case
        return
    print(n, end=" ")        # before the recursive call
    show(n - 1)
    print(n, end=" ")        # after the recursive call

show(3)                      # output: 3 2 1 1 2 3
""", "python", title="Listing 5. A recursive procedure"),
            H("Common mistakes"),
            MISTAKE("No base case, or a general case that does not move towards it", "factorial(n) calling factorial(n) again never stops and causes a stack overflow. Check that every recursive call uses a smaller value."),
            MISTAKE("Forgetting to return the recursive result", "Writing factorial(n - 1) on its own, without using its value, throws the answer away. Write: return n times factorial(n - 1)."),
            MISTAKE("Thinking an assignment inside a Python function changes the global", "Without the global keyword, assignment creates a new local variable. The global keeps its old value."),
            QUIZ("Which of these is NOT normally stored in a stack frame?",
                 ["The return address", "The values of the parameters", "The local variables", "The compiled code of the subroutine"], 3,
                 "The code of a subroutine is stored once, in the code area of memory. Each call gets its own frame holding the return address, parameters and locals.",
                 feedback=["The return address is needed so execution can continue after the call.",
                           "Each call has its own parameter values, so they are kept in the frame.",
                           "Each call has its own local variables, so they live in the frame.", ""]),
            QUIZ("A recursive function is called with a value that never reaches the base case. What is the most likely result?",
                 ["A syntax error", "A stack overflow at run time", "The function returns 0", "The compiler removes the recursion"], 1,
                 "Each call pushes a new frame. With no base case the stack keeps growing until memory runs out: a stack overflow (in Python, a RecursionError).",
                 feedback=["The code is syntactically valid; the problem appears only when it runs.", "",
                           "Nothing makes the function return; it keeps calling itself.",
                           "A compiler cannot generally know that the recursion will not stop."]),
            H("Practice questions"),
            PQ("Explain the difference between a local and a global variable, and give two advantages of using local variables. [4 marks]",
               "A local variable is declared inside a subroutine; it can be used only there and exists only while the subroutine runs. "
               "A global variable is declared outside all subroutines and can be accessed anywhere in the program for the whole run. "
               "Advantages of locals: the subroutine is self-contained, so it can be tested and reused separately; the same name can be "
               "used in different subroutines without clashes; memory is freed when the subroutine ends; other code cannot change them by accident."),
            PQ("The C function f is defined by: if n is at most 1 return n, otherwise return f(n - 1) + f(n - 2). (a) Find the value of f(4). "
               "(b) How many times is f called in total when f(4) is evaluated? (c) What is the greatest number of f frames on the stack at one time? [5 marks]",
               "(a) f(0) = 0, f(1) = 1, f(2) = 1 + 0 = 1, f(3) = 1 + 1 = 2, f(4) = 2 + 1 = 3. "
               "(b) f(4) calls f(3) and f(2); f(3) calls f(2) and f(1); each f(2) calls f(1) and f(0). Calls: f(4), f(3), f(2), f(1), f(0), f(1), f(2), f(1), f(0): 9 calls. "
               "(c) The deepest chain is f(4), f(3), f(2), f(1) (or f(0)): 4 frames."),
            PQ("Write a recursive Python function power(x, n) that returns x to the power n for any whole number n of at least 0. Identify the base case and trace power(2, 3). [5 marks]",
               "def power(x, n): if n == 0: return 1, otherwise return x times power(x, n - 1). "
               "Base case: n == 0 returns 1. Trace: power(2, 3) calls power(2, 2), which calls power(2, 1), which calls power(2, 0), which returns 1. "
               "Unwinding: power(2, 1) = 2 times 1 = 2; power(2, 2) = 2 times 2 = 4; power(2, 3) = 2 times 4 = 8."),
            SUM("Structured programming uses sequence, selection and iteration inside subroutines, designed top-down.",
                "Functions return a value; procedures do not. Parameters are in the heading; arguments are the values passed.",
                "By value passes a copy; by reference passes the address so the original can change.",
                "Local variables exist only inside their subroutine; global variables are visible everywhere. Prefer locals.",
                "A recursive subroutine needs a base case and a general case that moves towards it.",
                "Each call pushes a stack frame (return address, parameters, locals); returns pop it; endless recursion causes a stack overflow."),
        ],
    ),
    # ------------------------------------------------------------------ Files and pointers
    lesson(
        module=PROC,
        topic="Files and pointers",
        title="File handling and pointers in C",
        slug="file-handling-and-pointers",
        minutes=30,
        summary="Store data permanently by reading and writing text files in Python and C, and manage memory in C with pointers, pass-by-reference and dynamic allocation with malloc and free.",
        objectives=[
            "Explain why files are needed and describe text files, binary files and file modes",
            "Write programs that open, write, read and close files in Python and C",
            "Declare pointers in C and use the address-of and dereference operators",
            "Use pointers to pass parameters by reference",
            "Allocate and free memory dynamically and avoid memory leaks and dangling pointers",
        ],
        key_concepts=["File", "Text file", "Binary file", "File mode", "End of file", "Pointer", "Address-of operator",
                      "Dereference operator", "NULL pointer", "Dynamic memory allocation", "Memory leak"],
        blocks=[
            H("Introduction"),
            T("Variables live in RAM, and RAM is **volatile**: when a program ends, or when the power goes off, which still happens often in "
              "many Cameroonian towns, everything in RAM is lost. A mobile payment app must keep every transaction, and a school must keep "
              "every student's marks, so data is written to **files** on secondary storage.\n\n"
              "The second half of this lesson is about **pointers** in C. A pointer holds a memory address. Pointers let a function change "
              "the caller's variables, let programs ask for memory while they run, and are how C handles files (the FILE pointer)."),
            D("A **file** is a named collection of data on secondary storage. A **text file** stores characters (for example ASCII or UTF-8) "
              "arranged in lines and can be read in a text editor. A **binary file** stores data in the same form as in memory, which is more "
              "compact and faster but not human-readable. Every program follows the same pattern: **open** the file in a mode, **read** or "
              "**write**, detect **end of file (EOF)** when reading, then **close** the file so buffered data is saved.",
              title="Definition: file, text file and binary file"),
            KEY("File modes", "The mode is given when the file is opened (the same letters are used in Python and C).", cards=[
                ["r (read)", "Opens an existing file for reading. Fails if the file does not exist."],
                ["w (write)", "Creates the file, or empties it if it already exists, then writes from the start."],
                ["a (append)", "Writes new data at the end, keeping the existing contents. Creates the file if needed."],
            ], note="Add b for binary files, for example rb or wb."),
            EX("Worked example 1: a transaction log in Python", intro=(
                "A mobile payment app keeps a log of transfers in a text file, one transfer per line in the form account,amount. "
                "Write the three transfers in Listing 1 to the file, then read it back and total the transfers for account ACC101."), steps=[
                S("Open for writing", text="open with mode w creates transactions.txt. The with statement closes the file automatically at the end of the block."),
                S("Write one line per record", text="Each record is turned into text, for example ACC101,5000, followed by a newline character so the next record starts a new line."),
                S("Open for reading and loop over the lines", text="The for loop reads one line at a time and stops at end of file."),
                S("Split each line", text="strip removes the newline; split at the comma gives the account and the amount as strings. int converts the amount to a number."),
                S("Result", text="The ACC101 lines hold 5000 and 2000, so the program prints Total for ACC101: 7000."),
            ]),
            CODE("""
transactions = [("ACC101", 5000), ("ACC102", 12500), ("ACC101", 2000)]

with open("transactions.txt", "w") as f:            # create / empty the file
    for account, amount in transactions:
        f.write(account + "," + str(amount) + "\\n")

total = 0
with open("transactions.txt", "r") as f:            # read it back
    for line in f:                                   # stops at end of file
        account, amount = line.strip().split(",")
        if account == "ACC101":
            total = total + int(amount)

print("Total for ACC101:", total)                    # Total for ACC101: 7000
""", "python", title="Listing 1. Writing and reading a text file in Python"),
            EX("Worked example 2: averaging marks from a file in C", intro=(
                "The file marks.txt contains the marks 12 15 9 18 for one student. Write a C program that reads all the marks and prints their average."),
                steps=[
                S("Declare a FILE pointer and open the file", text="fopen returns a pointer to a FILE structure, or NULL if the file cannot be opened."),
                S("Check for NULL", text="If the file is missing, print a message and stop, instead of crashing later."),
                S("Read until end of file", text="fscanf returns the number of values it read. The loop continues while it returns 1, so it stops at end of file or at bad data."),
                S("Close the file and compute", text="total = 12 + 15 + 9 + 18 = 54 and count = 4. Casting to double avoids integer division: 54 divided by 4 = 13.50."),
            ]),
            CODE("""
#include <stdio.h>

int main(void)
{
    FILE *fp;
    int mark, count = 0, total = 0;

    fp = fopen("marks.txt", "r");
    if (fp == NULL) {
        printf("Cannot open marks.txt\\n");
        return 1;
    }
    while (fscanf(fp, "%d", &mark) == 1) {   /* stops at end of file */
        total = total + mark;
        count++;
    }
    fclose(fp);

    if (count > 0)
        printf("Average = %.2f\\n", (double) total / count);   /* Average = 13.50 */
    return 0;
}
""", "c", title="Listing 2. Reading numbers from a text file in C"),
            H("Pointers"),
            D("A **pointer** is a variable that stores the memory **address** of another variable. In C a pointer is declared with a star "
              "before its name, as in Listing 3. The **address-of operator** (the ampersand) gives the address of a variable. The "
              "**dereference operator** (the star placed before a pointer in an expression) gives the value stored at the address the "
              "pointer holds. A pointer that points nowhere should be set to **NULL**.", title="Definition: pointer"),
            CODE("""
#include <stdio.h>

int main(void)
{
    int x = 10;
    int y = 7;
    int *p = &x;          /* p holds the address of x          */

    *p = 25;              /* change x through p: x is now 25    */
    printf("%d %d\\n", x, *p);      /* prints: 25 25             */

    p = &y;               /* p now holds the address of y       */
    *p = *p + x;          /* y = 7 + 25 = 32                    */
    printf("%d %d\\n", x, y);       /* prints: 25 32             */
    return 0;
}
""", "c", title="Listing 3. Declaring and using a pointer"),
            EX("Worked example 3: tracing Listing 3 with a memory table", intro=(
                "Suppose x is stored at address 1000, y at 1004 and p at 1008 (illustrative addresses). Trace the program."), steps=[
                S("After the declarations", text="x = 10, y = 7, and p holds 1000, the address of x."),
                S("Assign through p", text="Dereferencing p means the variable at address 1000, which is x. So x becomes 25. Both x and the dereferenced p print 25."),
                S("Point p at y", text="p now holds 1004. x is unchanged."),
                S("Use the dereferenced p on both sides", text="The value at 1004 is 7; 7 + 25 = 32 is stored at 1004, so y = 32. The program prints 25 32 (Figure 1)."),
            ]),
            CODE("""
 Address   Variable   After line p = &x   After *p = 25   After p = &y   After *p = *p + x
 -------   --------   -----------------   -------------   ------------   -----------------
  1000        x              10                25              25               25
  1004        y               7                 7               7               32
  1008        p             1000              1000            1004             1004
""", "text", title="Figure 1. Memory table for Listing 3"),
            EX("Worked example 4: swapping two values by reference", intro=(
                "Two school accounts in a payment app have balances m = 3000 and n = 8000. Explain why swap_wrong in Listing 4 does not swap them, "
                "and why swap does."), steps=[
                S("swap_wrong receives copies", text="C passes arguments by value. a and b are local copies of m and n in swap_wrong's stack frame. Swapping the copies leaves m and n unchanged."),
                S("swap receives addresses", text="The call swap(&m, &n) passes the addresses of m and n. Inside swap, dereferencing a and b reaches the caller's actual variables."),
                S("Result", text="After swap, m = 8000 and n = 3000. Pointers give C the effect of pass-by-reference."),
            ]),
            CODE("""
#include <stdio.h>

void swap_wrong(int a, int b)     /* receives copies */
{
    int t = a;
    a = b;
    b = t;                        /* only the copies are swapped */
}

void swap(int *a, int *b)         /* receives addresses */
{
    int t = *a;
    *a = *b;
    *b = t;                       /* the caller's variables are swapped */
}

int main(void)
{
    int m = 3000, n = 8000;
    swap_wrong(m, n);
    printf("%d %d\\n", m, n);      /* 3000 8000 */
    swap(&m, &n);
    printf("%d %d\\n", m, n);      /* 8000 3000 */
    return 0;
}
""", "c", title="Listing 4. Pass by value and pass by reference with pointers"),
            D("**Dynamic memory allocation** requests memory from the **heap** while the program runs. In C, malloc returns a pointer to a "
              "block of the requested number of bytes, or NULL if there is not enough memory. The block must be released with free when it is "
              "no longer needed. Forgetting to free memory causes a **memory leak**. Using a pointer after its memory has been freed is a "
              "**dangling pointer** error, so set the pointer to NULL after freeing it. Adding 1 to a pointer moves it on by the size of "
              "one element (**pointer arithmetic**), so marks[i] and the dereferenced marks + i mean the same element.",
              title="Definition: dynamic memory allocation"),
            CODE("""
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n = 5, i;
    int *marks = malloc(n * sizeof(int));   /* room for 5 ints on the heap */

    if (marks == NULL) {
        printf("Out of memory\\n");
        return 1;
    }
    for (i = 0; i < n; i++)
        *(marks + i) = (i + 1) * 10;        /* same as marks[i] = ... */
    for (i = 0; i < n; i++)
        printf("%d ", marks[i]);            /* 10 20 30 40 50 */
    printf("\\n");

    free(marks);                            /* give the memory back */
    marks = NULL;                           /* avoid a dangling pointer */
    return 0;
}
""", "c", title="Listing 5. Allocating, using and freeing an array on the heap"),
            H("Common mistakes"),
            MISTAKE("Opening a file with w when you meant a", "Mode w empties an existing file. A transaction log opened with w each day loses all earlier records. Use a to add to the end."),
            MISTAKE("Not checking for NULL", "fopen and malloc both return NULL on failure. Using the result without checking crashes the program."),
            MISTAKE("Using an uninitialised pointer", "A pointer declared without a value holds a random address; writing through it can corrupt memory. Initialise every pointer to a valid address or to NULL."),
            MISTAKE("Confusing the pointer with the value it points to", "p is an address; the dereferenced p is the value at that address. Assigning to p changes where it points; assigning to the dereferenced p changes the data."),
            QUIZ("A program must add today's transactions to the end of an existing log file without losing the old records. Which mode should it use?",
                 ["r", "w", "a", "rb"], 2,
                 "Append mode writes at the end of the file and keeps what is already there.",
                 feedback=["r opens the file for reading only; it cannot write.",
                           "w empties the existing file first, so all old records would be lost.", "",
                           "rb opens a binary file for reading only."]),
            QUIZ("The pointer p holds the address of the integer variable x, which contains 5. What does the dereference operator applied to p give?",
                 ["The address of p", "The value 5 stored in x", "The address of x", "The number of bytes in x"], 1,
                 "Dereferencing follows the address held in p to the variable x and gives its value, 5.",
                 feedback=["The address of p is given by applying the address-of operator to p.", "",
                           "The address of x is the value of p itself, not of the dereferenced p.",
                           "The size of x is given by sizeof, not by dereferencing."]),
            H("Practice questions"),
            PQ("(a) Explain the difference between opening a file in mode w and in mode a. (b) Explain why a program should check the value returned by fopen before using it. [4 marks]",
               "(a) Mode w creates the file or, if it exists, deletes its contents and writes from the beginning. Mode a keeps the existing contents and adds new data at the end (creating the file if it does not exist). "
               "(b) fopen returns NULL if the file cannot be opened (for example it does not exist, or there is no permission). Reading or writing through a NULL FILE pointer causes a run-time crash, so the program should test for NULL and report the error."),
            CODE("""
int a = 4, b = 9;
int *p = &a;
int *q = &b;
*p = *q - 1;
q = p;
*q = *q * 2;
printf("%d %d\\n", a, b);
""", "c", title="Listing 6. Code for the next practice question"),
            PQ("Trace the C code in Listing 6 and state its output. [4 marks]",
               "p points to a and q points to b. Line 4: the value at q is 9, so the value at p (which is a) becomes 9 minus 1 = 8. "
               "Line 5: q now holds the same address as p, so q points to a. Line 6: the value at q (a = 8) is doubled, so a = 16. b was never changed, so b = 9. Output: 16 9."),
            PQ("Explain what is meant by a memory leak and a dangling pointer in C, and state how each can be avoided. [4 marks]",
               "A memory leak happens when memory allocated with malloc is never released, for example because the only pointer to it is overwritten or goes out of scope; the program uses more and more memory. Avoid it by calling free on every allocated block once it is no longer needed. "
               "A dangling pointer is a pointer that still holds the address of memory that has been freed (or of a local variable whose function has returned); using it gives unpredictable results. Avoid it by setting the pointer to NULL immediately after free and never returning the address of a local variable."),
            SUM("Files keep data on secondary storage after the program ends; text files hold characters, binary files hold raw memory data.",
                "Open the file in a mode (r, w or a), read or write, detect end of file, then close it. Mode w erases existing contents.",
                "In C, fopen returns a FILE pointer or NULL; always check it before use.",
                "A pointer stores an address: the ampersand gives an address, the dereference operator gives the value stored there.",
                "Passing addresses lets a C function change the caller's variables (pass by reference).",
                "malloc allocates heap memory and free releases it; avoid memory leaks, NULL dereferences and dangling pointers."),
        ],
    ),
]
