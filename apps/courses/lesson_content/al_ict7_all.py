"""ICT (A Level) Upper Sixth: focused depth lessons (KKEVO draft material for review).

Topics: Network Engineering, Cybersecurity, Productivity & Project Management, Examination.
These lessons go deeper than the overview lessons in u6_ict.py and do not repeat their slugs.
"""

from .dsl import *  # noqa: F403

COURSE = ("ict", "upper-sixth")

LESSONS = []

NE = "Network Engineering"
CS = "Cybersecurity"
PP = "Productivity & Project Management"

# ---------------------------------------------------------------------------
# Cabling and switching 1: UTP and T568
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=NE, topic="Cabling and switching",
    title="UTP cable categories, pairs and T568A/T568B wiring",
    slug="ic7-utp-cabling-and-t568-wiring",
    minutes=22,
    summary="Choose a cable category and length, say which wire goes on which pin in T568A and T568B, work out the pin mapping of a crossover cable, and read a cable tester.",
    objectives=[
        "Compare Cat5e, Cat6 and Cat6a by speed and distance and state the 100 m limit",
        "Write the T568A and T568B pin orders and name the four pairs",
        "Work out the pin-to-pin mapping of straight-through and crossover cables",
        "Diagnose a faulty patch cable from the order of lights on a cable tester",
    ],
    key_concepts=["UTP", "Cat5e", "Cat6", "Twisted pair", "T568A", "T568B", "Straight-through", "Crossover", "Cable tester"],
    blocks=[
        H("Introduction"),
        T("A cybercafe in Garoua has 12 computers. Its Wi-Fi is slow when everyone downloads at the same time, so the owner decides "
          "to wire the machines to a switch. A technician arrives with a roll of cable, a pack of RJ-45 plugs and a crimping tool. "
          "Which cable should he buy? How long can each run be? Which wire goes on which pin? A small mistake in the order of "
          "the colours gives a cable that looks perfect but does not work, or works only at slow speed."),
        H("Choosing the cable"),
        T("Office networks use **UTP (unshielded twisted pair)** cable. It holds eight copper wires twisted into four pairs. "
          "Each pair carries a signal and its mirror image, and the twists cancel most of the interference picked up from "
          "power cables, motors and neighbouring pairs (**crosstalk**)."),
        KEY("Common categories", "A higher category has more twists per metre and tighter rules, so it carries faster signals.",
            cards=[["Cat5e", "Supports 1 Gbps Ethernet (1000BASE-T) over 100 m. Still common in small offices."],
                   ["Cat6", "Supports 1 Gbps over 100 m and 10 Gbps over short runs (about 55 m)."],
                   ["Cat6a", "Supports 10 Gbps over the full 100 m. Thicker and dearer."]],
            note="Check the category printed on the cable jacket. The weakest part of a link (cable, plug or socket) limits its speed."),
        D("The maximum length of a twisted-pair Ethernet run is **100 m** in total: up to 90 m of fixed cable inside the walls plus short patch cables at each end (10 m together).",
          title="The 100 m rule",
          note="Beyond 100 m the signal becomes too weak and late. Use a switch or fibre link to go further."),
        H("Pairs and pin order"),
        T("An RJ-45 plug has eight pins numbered 1 to 8, counted from the left when you hold the plug with the contacts facing you "
          "and the clip pointing away from you. The standard TIA/EIA-568 gives two colour orders for the eight wires. Both are "
          "valid; a building should use one of them consistently."),
        CODE("""
Pin  T568A         T568B         Pair (T568B)
 1   white-green   white-orange  2 (orange)
 2   green         orange        2 (orange)
 3   white-orange  white-green   3 (green)
 4   blue          blue          1 (blue)
 5   white-blue    white-blue    1 (blue)
 6   orange        green         3 (green)
 7   white-brown   white-brown   4 (brown)
 8   brown         brown         4 (brown)
""", "text", title="Listing 1: the two pin orders",
             caption="Only the orange and green pairs change places. Memory aid: in T568B the first wire is white-orange; in T568A it is white-green."),
        IMG("al-ic7-t568-pins.svg", alt="The eight pins of an RJ-45 plug with the wire colours of T568A above and T568B below; the green and orange wires swap places",
            caption="Figure 1. T568A and T568B side by side. Pins 4, 5, 7 and 8 are the same; pins 1, 2, 3 and 6 swap."),
        T("Notice that the green pair is split: one green wire goes to pin 3 and the other to pin 6, with pins 4 and 5 (blue) between "
          "them. This is deliberate. Fast Ethernet (100 Mbps) uses only pins 1, 2, 3 and 6. Gigabit Ethernet uses all four pairs."),
        EX("Worked example 1: terminating a patch cable to T568B", intro=(
            "A technician must make a 2 m patch cable from a lab PC to a wall socket, using T568B at both ends. Give the wire order and the order of work."),
           steps=[
               S("Choose the standard", text="Same standard at both ends gives a straight-through cable. PC to wall socket is unlike devices, so straight-through is right."),
               S("Prepare the cable", text="Strip about 2.5 cm of the outer jacket without cutting the wires. Untwist the pairs and straighten them."),
               S("Order the wires, pin 1 to pin 8", text="white-orange, orange, white-green, blue, white-blue, green, white-brown, brown."),
               S("Trim and insert", text="Cut the ends level about 1.3 cm from the jacket, slide them into the plug with the clip underneath until every copper end touches the front, and check the colours again through the clear plastic."),
               S("Crimp and test", text="Crimp the plug, repeat at the other end in the same order, and test with a cable tester."),
           ]),
        EX("Worked example 2: the pin mapping of a crossover cable", intro=(
            "A crossover cable has T568A at one end and T568B at the other. Which pin at end B receives the signal from pin 1 and from pin 2 at end A?"),
           steps=[
               S("Find the wire on pin 1 at end A (T568A)", text="Pin 1 is white-green."),
               S("Find where white-green is at end B (T568B)", text="In T568B white-green is on pin 3. So pin 1 at A connects to pin 3 at B."),
               S("Repeat for pin 2", text="Pin 2 at A is green. In T568B green is on pin 6. So pin 2 connects to pin 6."),
               S("Finish the mapping", text="By the same method pin 3 goes to pin 1 and pin 6 goes to pin 2. Pins 4, 5, 7 and 8 go straight across. In short: 1 to 3, 2 to 6, 3 to 1, 6 to 2."),
               S("Why it works", text="A PC sends on pins 1 and 2 and listens on 3 and 6. A crossover joins one device's transmit pins to the other's receive pins. A PC-to-switch link does not need this because the switch port already has transmit and receive swapped."),
           ]),
        EX("Worked example 3: reading a cable tester", intro=(
            "A tester has eight numbered lights on the main unit and eight on the remote unit. For a good straight-through cable the lights flash 1 to 8 in order on both units. "
            "On the remote unit the lights flash 1, 2, 3, 4, 6, 5, 7, 8. What is wrong?"),
           steps=[
               S("Compare the two sequences", text="The main unit flashes in order but the remote unit shows pins 5 and 6 swapped."),
               S("Name the fault", text="Two wires are crossed (a miswire) at one end: the wires for pins 5 and 6 are in each other's place."),
               S("Fix", text="Cut off the plug at the faulty end, re-order the wires and crimp a new plug. Then test again."),
               S("Other results", text="A light that does not come on means an open wire (not pushed in or broken). Two lights on together mean a short. A cable can pass a continuity test and still be a split pair, which causes crosstalk; only a better tester or a speed problem reveals it."),
           ]),
        TIP("In the exam, write the eight pin positions in a row, then check that pins 4, 5, 7, 8 are blue, white-blue, white-brown, brown in both standards. That check catches most slips."),
        MISTAKE("Wiring the pairs by colour instead of by pin", "Pairing white-green with green on pins 1 and 2 looks tidy, but in both standards the green pair is split across pins 3 and 6. Follow the pin order, not the pairs."),
        MISTAKE("Calling a cable crossover because the colours look different", "The colour of the outer jacket means nothing. Only the pin order at each end decides: same at both ends is straight-through, A at one end and B at the other is crossover."),
        QUIZ("Which wire is on pin 3 in T568B?",
             ["white-orange", "white-green", "green", "blue"], 1,
             "In T568B the order is white-orange, orange, white-green, blue, white-blue, green, white-brown, brown, so pin 3 is white-green.",
             hint="Write the T568B order from pin 1 and count to the third wire.",
             feedback=["White-orange is on pin 3 in T568A but on pin 1 in T568B.", "",
                       "Solid green is on pin 6 in T568B and on pin 2 in T568A.", "Blue is on pin 4 in both standards."]),
        QUIZ("A cable run in a building is 120 m long from the switch to a PC. What is the correct engineering response?",
             ["Use Cat6a, which works over any length", "Add a switch or use fibre so no copper segment is over 100 m",
              "Crimp the plugs more tightly", "Use T568A instead of T568B"], 1,
             "The 100 m limit applies to every twisted-pair category. Place an intermediate switch within range or use fibre.",
             hint="Does a higher category change the length limit?",
             feedback=["Cat6a carries 10 Gbps over 100 m; it does not extend the limit.", "",
                       "Tight crimping does not change signal loss over distance.",
                       "The wiring standard does not affect the maximum length."]),
        H("Practice questions"),
        PQ("List the T568A wire order from pin 1 to pin 8.",
           "white-green, green, white-orange, blue, white-blue, orange, white-brown, brown."),
        PQ("A technician crimps white-orange, orange, white-green, blue, white-blue, green, white-brown, brown on one end and white-green, green, white-orange, blue, white-blue, orange, white-brown, brown on the other end. (a) Name the standard at each end. (b) What kind of cable is it? (c) Give one use.",
           "(a) The first end is T568B and the second end is T568A. (b) A crossover cable. (c) Joining two like devices directly, for example two older switches or two PCs, when the devices do not have automatic crossover (Auto-MDI/MDI-X)."),
        PQ("State two differences between Cat5e and Cat6 and one thing they share.",
           "Cat6 supports 10 Gbps over short runs (about 55 m) while Cat5e is meant for 1 Gbps; Cat6 has tighter specifications and less crosstalk. They share the 100 m maximum for a twisted-pair run and the same RJ-45 plug and pin orders."),
        PQ("A tester shows lights 1, 2, 3 and 6 on both units and nothing for 4, 5, 7, 8. What will still work, and what will not?",
           "Pins 1, 2, 3 and 6 are good, which is all that Fast Ethernet (100 Mbps) needs, so the link may work at 100 Mbps. Gigabit Ethernet needs all four pairs, so it will fail or fall back to 100 Mbps. The open wires on pins 4, 5, 7 and 8 must be repaired."),
        H("Summary"),
        SUM("UTP has four twisted pairs; the 100 m limit applies to every category.",
            "T568A and T568B differ only by swapping the green and orange pairs (pins 1, 2, 3, 6).",
            "Same standard at both ends gives straight-through; A at one end and B at the other gives crossover (1 to 3, 2 to 6).",
            "Fast Ethernet uses pins 1, 2, 3, 6; gigabit uses all eight.",
            "Read a tester by comparing the light order on both units: a missing light is open, a swap is a miswire."),
    ],
))

# ---------------------------------------------------------------------------
# Cabling and switching 2: switch learning and forwarding
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=NE, topic="Cabling and switching",
    title="How a switch learns, forwards and floods frames",
    slug="ic7-switch-mac-table-and-forwarding",
    minutes=22,
    summary="Trace frames through a switch, build its MAC address table step by step, and explain collision and broadcast domains.",
    objectives=[
        "Describe the address fields of an Ethernet frame",
        "Trace a series of frames through a switch and write the MAC address table after each",
        "Decide whether a frame is forwarded, flooded or filtered",
        "Distinguish collision domains from broadcast domains for hubs, switches and routers",
    ],
    key_concepts=["MAC address", "Frame", "MAC address table", "Flooding", "Filtering", "Broadcast", "Collision domain", "Broadcast domain"],
    blocks=[
        H("Introduction"),
        T("A school in Kumba replaced its old hub with a switch and the lab became much faster. Nothing changed in the cables or the PCs. "
          "The difference is in how the device decides where to send data. A hub repeats every signal out of every port. A switch "
          "sends a frame only where it needs to go. To do this a switch has a small memory that it fills by itself, the "
          "**MAC address table**. In this lesson you build that table by hand."),
        H("Frames and MAC addresses"),
        D("A **MAC address** is a 48-bit hardware address written as six pairs of hexadecimal digits, for example 3C:52:82:1A:9F:07. It identifies a network interface on the local network. The first half identifies the manufacturer and the second half the individual card.",
          title="MAC address"),
        D("A **frame** is the unit of data at the data link layer (layer 2). Its header holds the **destination MAC address**, the **source MAC address** and a type field, followed by the data and an error-check value at the end. The all-ones address FF:FF:FF:FF:FF:FF is the **broadcast** address: every device on the LAN receives that frame.",
          title="Frame"),
        T("A switch never needs to read IP addresses. It works only with the two MAC addresses in the frame header."),
        H("The learn, forward, flood rules"),
        KEY("What a switch does with every frame", "Two jobs, in this order.",
            cards=[["1. Learn", "Read the source MAC address. Record it in the table against the port the frame arrived on (update the entry if it was already there)."],
                   ["2. Decide", "Read the destination MAC. Known and on another port: forward to that port only. Known and on the same port as the arrival port: filter (drop). Unknown, or broadcast: flood out of every port except the arrival port."]],
            note="Entries are removed after a time without traffic (aging, often a few minutes), so the table stays correct when devices are moved."),
        EX("Worked example 1: building the table", intro=(
            "A four-port switch starts with an empty table. Computers A, B, C, D (MACs AA, BB, CC, DD) are on ports 1, 2, 3, 4. "
            "Trace these frames in order: (1) A to B, (2) B to A, (3) C to B, (4) D to broadcast, (5) A to D."),
           steps=[
               S("Frame 1: A to B arrives on port 1", text="Learn AA on port 1. BB is unknown, so flood to ports 2, 3, 4. Table: AA=1."),
               S("Frame 2: B to A arrives on port 2", text="Learn BB on port 2. AA is known on port 1, so forward to port 1 only. Table: AA=1, BB=2."),
               S("Frame 3: C to B arrives on port 3", text="Learn CC on port 3. BB is known on port 2: forward to port 2 only. Table: AA=1, BB=2, CC=3."),
               S("Frame 4: D to broadcast arrives on port 4", text="Learn DD on port 4. A broadcast is always flooded to ports 1, 2, 3. Table: AA=1, BB=2, CC=3, DD=4."),
               S("Frame 5: A to D arrives on port 1", text="AA is already on port 1. DD is known on port 4, so forward to port 4 only. The table does not change."),
           ]),
        CODE("""
Frame  In  Src  Dst  Action               Table afterwards
1      1   AA   BB   flood to 2,3,4       AA=1
2      2   BB   AA   forward to 1         AA=1 BB=2
3      3   CC   BB   forward to 2         AA=1 BB=2 CC=3
4      4   DD   FF   flood to 1,2,3       AA=1 BB=2 CC=3 DD=4
5      1   AA   DD   forward to 4         unchanged
""", "text", title="Listing 1: the trace table for Worked example 1",
             caption="Only frames 1 and 4 reached ports they did not need to. Once the table is full, most frames go to one port only."),
        QUIZ("In the trace above, C then sends a frame to A. Which port(s) does the switch send it out of?",
             ["All ports except port 3", "Port 1 only", "Port 3 only", "Ports 1 and 2"], 1,
             "AA is already in the table on port 1, so the frame is forwarded to port 1 only.",
             hint="Is AA still unknown?",
             feedback=["That is flooding, used only for unknown or broadcast destinations.", "",
                       "Port 3 is where C is; the switch never returns a frame to its arrival port.",
                       "Only A is the destination, so only A's port is used."]),
        H("Collision and broadcast domains"),
        D("A **collision domain** is a group of devices whose signals can collide because they share the same medium. A **broadcast domain** is the set of devices that receive a broadcast frame sent by any one of them.",
          title="Domains"),
        CODE("""
Device   Collision domains         Broadcast domains
Hub      1 for all its ports       1 (all ports)
Switch   1 per port                1 (all ports, unless VLANs)
Router   1 per port                1 per port (it blocks broadcasts)
""", "text", title="Listing 2: how devices divide the network"),
        EX("Worked example 2: counting domains", intro=(
            "A lab has one 24-port switch with 20 PCs connected, which is connected by one cable to a router. Count the collision domains on the switch and the broadcast domains of the lab LAN if there are no VLANs."),
           steps=[
               S("Collision domains on the switch", text="One per connected port. 20 PCs plus 1 link to the router use 21 ports, so 21 collision domains (an unused port has no link to collide on)."),
               S("Broadcast domains", text="All switch ports are in one broadcast domain. The router port is the edge of it. So the lab LAN is 1 broadcast domain."),
               S("What would change with a hub", text="A hub would put all the PCs in one collision domain, so busy times would cause many collisions and retransmissions."),
           ]),
        MISTAKE("Learning from the destination address", "The switch learns from the SOURCE address, because that tells it which port leads to that device. The destination is used only to decide where to send."),
        MISTAKE("Saying a switch stops broadcasts", "A switch floods broadcasts. Only a router (or a VLAN boundary) stops them."),
        MISTAKE("Thinking flooding is a fault", "Flooding of unknown destinations is normal and happens mostly at the start, until the table is filled."),
        QUIZ("What happens when a switch receives a frame whose destination MAC address is on the same port the frame arrived on?",
             ["It floods the frame", "It sends the frame back", "It filters (drops) the frame", "It updates the source address to the destination"], 2,
             "The destination is reachable through the port the frame came from, so the switch does not forward it (it filters it). This happens when a hub or another switch is behind that port.",
             hint="Would sending it out of the same port help anyone?",
             feedback=["Flooding is for unknown or broadcast destinations.", "A switch never returns a frame to its arrival port.", "",
                       "Source addresses are learned from the source field only."]),
        H("Practice questions"),
        PQ("State the two actions a switch performs on every frame and which header field each uses.",
           "Learn: record the source MAC address against the arrival port. Forward: use the destination MAC address to look in the table and send to the matching port; flood if unknown or broadcast."),
        PQ("A switch has an empty table. Host P (port 5) sends a frame to host Q (port 7). Then Q replies to P. State the action and the table after each frame.",
           "Frame 1: learn P=5; Q unknown so flood out of every port except 5. Table: P=5. Frame 2: learn Q=7; P is known on port 5 so forward to port 5 only. Table: P=5, Q=7."),
        PQ("Explain why a switch gives better performance than a hub in a busy computer lab.",
           "A hub repeats each signal out of all ports, so all machines share one collision domain and must wait and retransmit after collisions. A switch forwards a known frame only to the destination port, each port is its own collision domain, so several pairs of computers can communicate at the same time."),
        PQ("A student asks: \"If the switch floods a frame to an unknown destination, does that frame reach every computer in the school?\" Answer using the idea of a broadcast domain.",
           "The switch floods to every port except the arrival port, but only within the same broadcast domain. If the school uses VLANs, the frame reaches only the ports in the same VLAN. If all ports are in one VLAN, it reaches all of them."),
        H("Summary"),
        SUM("A switch learns the source MAC address and forwards by the destination MAC address.",
            "Known destination on another port: forward. Same port: filter. Unknown or broadcast: flood out of all other ports.",
            "A trace table lists frame, arrival port, source, destination, action and the table after each frame.",
            "Each switch port is a collision domain; all ports are one broadcast domain until VLANs or a router divide it."),
    ],
))

# ---------------------------------------------------------------------------
# Cabling and switching 3: VLANs
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=NE, topic="Cabling and switching",
    title="VLANs, 802.1Q trunks and routing between VLANs",
    slug="ic7-vlans-trunks-and-inter-vlan-routing",
    minutes=24,
    summary="Group switch ports into VLANs, explain access and trunk ports and the 802.1Q tag, and trace a packet that must cross from one VLAN to another through a router.",
    objectives=[
        "Explain why VLANs are used and how they limit broadcasts",
        "Distinguish access ports from trunk ports and describe the 802.1Q tag",
        "Trace a packet between two VLANs through a router on a stick",
        "Find the cause of a VLAN fault from a short symptom description",
    ],
    key_concepts=["VLAN", "Access port", "Trunk port", "802.1Q", "VLAN ID", "Native VLAN", "Router on a stick", "Layer 3 switch"],
    blocks=[
        H("Introduction"),
        T("A teaching hospital in Yaounde has doctors, nurses, administrators and visitors using the same building. "
          "It would be costly to run four separate sets of switches. It would also be unsafe to put everyone on one flat network, "
          "because a visitor's laptop could then reach the patient-records server. A **VLAN** solves both problems: one set of "
          "switches carries several separate logical networks."),
        H("What a VLAN is"),
        D("A **VLAN (virtual local area network)** is a logical network defined inside a switch. Ports in the same VLAN share one broadcast domain. Ports in different VLANs cannot exchange frames at layer 2, even on the same physical switch.",
          title="VLAN",
          note="A VLAN is identified by a number, the VLAN ID. 802.1Q uses 12 bits, so IDs run from 0 to 4095, and IDs 1 to 4094 are usable on a switch (0 and 4095 are reserved)."),
        KEY("Why use VLANs", "Four benefits that are asked in exams.",
            cards=[["Security", "Visitors cannot reach clinical servers. Traffic between VLANs passes a router where rules (ACLs) can filter it."],
                   ["Performance", "Each VLAN is a smaller broadcast domain, so fewer broadcasts reach each device."],
                   ["Flexibility", "Move a user by changing a port setting, not by moving cables."],
                   ["Cost", "One switch carries several networks, so fewer devices to buy and power."]]),
        H("Access and trunk ports"),
        D("An **access port** belongs to one VLAN and connects an end device such as a PC. Frames leave it without any tag, so the PC knows nothing about VLANs.",
          title="Access port"),
        D("A **trunk port** carries traffic of many VLANs over one link between two switches, or between a switch and a router. Each frame is marked with an **IEEE 802.1Q tag** so the other end knows which VLAN it belongs to.",
          title="Trunk port",
          note="The tag adds 4 bytes to the frame: a tag identifier (0x8100), 3 bits of priority, 1 bit drop eligibility and the 12-bit VLAN ID. Frames of the **native VLAN** are sent untagged on a trunk; both ends must agree on which VLAN is native."),
        IMG("al-ic7-vlan-school.svg", alt="Two switches joined by a trunk. Ports in VLAN 10 (green) and VLAN 20 (blue) are on each switch, and a router connected by a trunk routes between the VLANs",
            caption="Figure 1. Two VLANs spread over two switches. The trunk between the switches and the trunk to the router carry both VLANs."),
        EX("Worked example 1: planning ports for a clinic", intro=(
            "A clinic in Limbe has one 24-port switch. Reception and administration use ports 1 to 6 (VLAN 10), doctors use ports 7 to 14 (VLAN 20), the guest Wi-Fi access point uses port 15 (VLAN 30), and port 24 goes to the router. Write the port plan and count the broadcast domains."),
           steps=[
               S("Assign the access ports", text="Ports 1-6: access, VLAN 10. Ports 7-14: access, VLAN 20. Port 15: access, VLAN 30."),
               S("Make the router link a trunk", text="Port 24: trunk, carrying VLANs 10, 20 and 30 to the router."),
               S("Count the broadcast domains", text="One per VLAN: VLAN 10, 20 and 30, so 3 broadcast domains. Unused ports 16 to 23 should be shut down or put in an unused VLAN."),
               S("Number of ports used", text="6 + 8 + 1 + 1 trunk = 16 ports."),
           ]),
        CODE("""
Port    Mode     VLAN
1-6     access   10  (ADMIN)
7-14    access   20  (DOCTORS)
15      access   30  (GUEST)
16-23   shutdown -
24      trunk    10,20,30
""", "text", title="Listing 1: the port plan"),
        H("Routing between VLANs"),
        T("Different VLANs are different IP networks, so a router is needed to join them. In a **router on a stick** one physical router "
          "port connects to a trunk on the switch. The router divides this port into **sub-interfaces**, one per VLAN, each with its own "
          "IP address (the default gateway for that VLAN). A **layer 3 switch** does the same job inside the switch using virtual "
          "interfaces, which is faster."),
        EX("Worked example 2: a packet from VLAN 20 to VLAN 10", intro=(
            "A doctor's PC in VLAN 20 (network 192.168.20.0/24, gateway 192.168.20.1) sends a packet to the records server in VLAN 10 (192.168.10.0/24, gateway 192.168.10.1). Follow the packet."),
           steps=[
               S("Does the PC need a gateway?", text="The destination 192.168.10.5 is not in 192.168.20.0/24, so the PC sends the frame to its default gateway, 192.168.20.1 (the MAC address of the router sub-interface)."),
               S("PC to switch", text="The frame enters an access port in VLAN 20 untagged. The switch adds an 802.1Q tag with VLAN ID 20 and sends it out of the trunk."),
               S("Router receives it", text="The router reads the tag, hands the packet to sub-interface VLAN 20, removes the old frame header, and looks up 192.168.10.0/24 in its routing table. This network is on sub-interface VLAN 10."),
               S("Router back to switch", text="The router builds a new frame addressed to the server's MAC, tagged with VLAN ID 10, and sends it down the same trunk."),
               S("Switch to server", text="The switch removes the tag and delivers the frame out of the access port in VLAN 10. The server receives it as a normal frame."),
           ]),
        T("Notice that the packet crossed the trunk twice. The router can also apply an access control list on the way, which is where the "
          "security benefit of VLANs comes from."),
        MISTAKE("Thinking VLANs alone give security", "A VLAN is a separation at layer 2 only. If a router joins the VLANs and allows all traffic, they are connected. Security comes from VLANs together with filtering rules on the router or firewall."),
        MISTAKE("Putting an end device on a trunk", "A PC does not understand 802.1Q tags. Connect PCs to access ports and use trunks only between switches and routers."),
        MISTAKE("Forgetting to allow the VLAN on the trunk", "If VLAN 30 is created on both switches but is not allowed on the trunk between them, PCs in VLAN 30 on different switches cannot talk even though the ports are correct."),
        QUIZ("A PC in VLAN 10 on switch 1 cannot reach a printer in VLAN 10 on switch 2. Both access ports are correct. What should the technician check first?",
             ["The cable categories of the PCs", "Whether VLAN 10 is allowed on the trunk between the switches",
              "The colour of the cables", "Whether the router has a DHCP scope"], 1,
             "Same VLAN on two switches depends on the trunk carrying that VLAN. If it is not allowed (or not created on both switches), the frames never cross.",
             hint="What carries frames of several VLANs between two switches?",
             feedback=["The PC cable type affects speed, not which VLAN a frame is in.", "",
                       "The cable colour has no effect on VLANs.",
                       "A DHCP scope gives addresses; the printer is already unreachable at layer 2."]),
        QUIZ("How many different VLAN IDs can the 802.1Q tag carry, counting all values of its VLAN ID field?",
             ["12", "256", "4096", "65536"], 2,
             "The VLAN ID field is 12 bits long, giving 2 to the power 12 = 4096 values (1 to 4094 are usable for normal VLANs).",
             hint="The field is 12 bits. What does 2 to the power 12 equal?",
             feedback=["12 is the number of bits, not the number of values.", "256 is 2 to the power 8.", "",
                       "65536 would need a 16-bit field."]),
        H("Practice questions"),
        PQ("Distinguish between an access port and a trunk port.",
           "An access port belongs to one VLAN, connects an end device and sends untagged frames. A trunk port carries frames of several VLANs between switches or to a router, and marks each frame with an 802.1Q tag holding the VLAN ID (except the native VLAN, which may be untagged)."),
        PQ("State three advantages of dividing a school network into VLANs.",
           "Security: groups can be separated and traffic between them filtered at the router. Performance: smaller broadcast domains reduce broadcast traffic. Flexibility and cost: users are moved by a port setting and several networks share the same switches."),
        PQ("Explain why two VLANs on the same switch cannot communicate without a router or layer 3 switch.",
           "Each VLAN is a separate broadcast domain and a separate IP network. The switch forwards frames only within a VLAN. To go from one IP network to another a device must send the packet to a default gateway, which must be a router or layer 3 switch that routes between the networks."),
        PQ("A router on a stick has sub-interfaces for VLAN 10 and VLAN 20. A PC in VLAN 20 cannot reach VLAN 10, but can reach other PCs in VLAN 20. Give two possible causes.",
           "The VLAN 10 sub-interface may be missing or shut down, or VLAN 10 may not be allowed on the trunk to the router. The PC may also have the wrong default gateway, or a router access list may block the traffic. Within VLAN 20 the switch alone is enough, which is why those PCs still work."),
        H("Summary"),
        SUM("A VLAN is a separate broadcast domain and IP network defined by switch ports.",
            "Access ports carry one untagged VLAN; trunk ports carry many VLANs using 802.1Q tags (12-bit VLAN ID).",
            "Traffic between VLANs must pass a router (router on a stick) or a layer 3 switch, where filtering can be applied.",
            "Faults: wrong port VLAN, VLAN not allowed on the trunk, wrong gateway, missing sub-interface."),
    ],
))

# ---------------------------------------------------------------------------
# Cabling and switching 4: DHCP scope arithmetic
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=NE, topic="Cabling and switching",
    title="DHCP scopes: subnet arithmetic, exclusions and lease times",
    slug="ic7-dhcp-scopes-subnets-and-leases",
    minutes=25,
    summary="Divide an address block into subnets, work out network, broadcast and usable host addresses, size a DHCP pool with exclusions, and choose a lease time.",
    objectives=[
        "List the DORA steps and what each message carries",
        "Calculate the network address, broadcast address and number of usable hosts of a subnet",
        "Design a DHCP scope with exclusions, a gateway and a lease time",
        "Explain address exhaustion, relay agents and the 169.254 fallback address",
    ],
    key_concepts=["DHCP", "DORA", "Scope", "Lease", "Exclusion", "Reservation", "Subnet mask", "Broadcast address", "Relay agent"],
    blocks=[
        H("Introduction"),
        T("A university in Dschang opens a new wireless network for its students. Hundreds of phones and laptops arrive each morning. "
          "Nobody can type an address into each one. **DHCP (Dynamic Host Configuration Protocol)** gives each device an address, "
          "mask, gateway and DNS server automatically. The network engineer's job is to decide how large the pool is, which "
          "addresses to keep back, and how long a device may keep an address."),
        H("DORA and lease timers"),
        KEY("The four messages (DORA)", "A new client has no address, so the first messages are broadcasts.",
            cards=[["Discover", "Client broadcasts: is there a DHCP server?"],
                   ["Offer", "Server offers an address from its scope with mask, gateway, DNS and lease time."],
                   ["Request", "Client broadcasts that it accepts that offer (other servers see it and withdraw theirs)."],
                   ["Acknowledge", "Server confirms the lease. The client can now use the address."]]),
        D("A **lease** is the length of time a client may use an address. At 50 percent of the lease (T1) the client asks the same server to renew. If that fails, at 87.5 percent (T2) it asks any server. If the lease ends with no answer the client must stop using the address.",
          title="Lease and renewal"),
        T("Check with a lease of 8 hours: T1 = 4 hours and T2 = 7 hours. A lease of 24 hours gives T1 = 12 hours and T2 = 21 hours."),
        H("Subnet arithmetic"),
        D("A **subnet mask** such as 255.255.255.192 (/26) splits an address into a network part and a host part. With n host bits a subnet has 2 to the power n addresses. The first is the **network address**, the last is the **broadcast address**, and neither can be given to a host, so there are 2 to the power n minus 2 **usable hosts**.",
          title="Subnet rules"),
        CODE("""
Prefix  Mask             Host bits  Addresses  Usable hosts
/24     255.255.255.0    8          256        254
/25     255.255.255.128  7          128        126
/26     255.255.255.192  6          64         62
/27     255.255.255.224  5          32         30
/28     255.255.255.240  4          16         14
/30     255.255.255.252  2          4          2
""", "text", title="Listing 1: subnet sizes",
             caption="Each extra prefix bit halves the subnet. A /30 is the usual size for a router-to-router link."),
        EX("Worked example 1: splitting a /24 into four /26 subnets", intro=(
            "A business centre in Bamenda has the block 10.20.0.0/24 and needs four departments, each with up to 50 devices. Give each subnet's network address, usable range and broadcast address."),
           steps=[
               S("How many host bits are needed?", text="50 devices need at least 50 usable addresses. 6 host bits give 62 usable, 5 host bits only 30. So the prefix is /26 and the mask is 255.255.255.192."),
               S("Block size", text="2 to the power 6 = 64 addresses per subnet, so the networks start at 0, 64, 128 and 192 in the last number."),
               S("Write the four subnets", text="10.20.0.0/26: hosts .1 to .62, broadcast .63. 10.20.0.64/26: hosts .65 to .126, broadcast .127. 10.20.0.128/26: hosts .129 to .190, broadcast .191. 10.20.0.192/26: hosts .193 to .254, broadcast .255."),
               S("Check", text="Each subnet has 64 addresses, 62 of them usable, and 4 x 64 = 256 uses the whole /24."),
           ]),
        H("Sizing a scope"),
        D("A **scope** is the range of addresses a DHCP server may hand out for one subnet, with its options (mask, gateway, DNS, lease). An **exclusion** removes addresses from the pool for devices with fixed addresses. A **reservation** always gives the same address to one MAC address, which suits printers.",
          title="Scope, exclusion, reservation"),
        EX("Worked example 2: the DHCP scope for the lab subnet", intro=(
            "The lab VLAN uses 10.20.0.64/26. The router takes the first usable address as gateway. A printer is at .66 and a file server at .67. Design the scope, and check that 40 PCs and 10 phones fit."),
           steps=[
               S("Subnet facts", text="Network 10.20.0.64, broadcast 10.20.0.127, usable .65 to .126, which is 62 addresses."),
               S("Exclude static addresses", text="Gateway .65, printer .66, file server .67; keep a few spare for future fixed devices. Exclude .65 to .70, which is 6 addresses."),
               S("Define the pool", text="Pool from 10.20.0.71 to 10.20.0.126. Count: 126 - 71 + 1 = 56 addresses."),
               S("Check capacity", text="40 PCs + 10 phones = 50 devices, and 50 is less than 56, so everyone can have an address, with 6 spare."),
               S("Set the options", text="Mask 255.255.255.192, default gateway 10.20.0.65, DNS server of the school, lease time 8 hours."),
           ]),
        EX("Worked example 3: running out of addresses", intro=(
            "The wireless network uses 192.168.50.0/24 with the pool .21 to .254 (234 addresses) and a lease of 24 hours. During a day 300 different phones connect, but never more than 150 at the same time. Do users get errors? What should the engineer change?"),
           steps=[
               S("Count the addresses", text="The pool is 254 - 21 + 1 = 234."),
               S("Find the problem", text="With a 24-hour lease each phone keeps its address for a day even after it leaves. 300 phones need 300 leases, which is more than 234, so late arrivals get no address."),
               S("Fix 1: shorten the lease", text="Use a lease of 1 hour. Addresses of phones that have left come back quickly, and 150 simultaneous devices fit easily in 234."),
               S("Fix 2: enlarge the subnet", text="Change to /23 (510 usable hosts) if long leases are needed. This needs the router and DHCP scope to be updated together."),
           ]),
        T("Two further ideas. A **relay agent** (on the router) forwards DHCP broadcasts to a central server on another subnet, so one server can serve many VLANs. "
          "If no server answers, a Windows client gives itself an address in 169.254.0.0/16 (APIPA). Seeing a 169.254 address means DHCP failed."),
        MISTAKE("Counting the network and broadcast addresses as usable", "In a /26 there are 64 addresses but only 62 usable. The first and last are not given to hosts."),
        MISTAKE("Leaving static devices in the pool", "If the printer is at .66 and .66 is still in the pool, the server may give .66 to a phone and both stop working (an address conflict). Exclude or reserve it."),
        QUIZ("What is the broadcast address of 10.20.0.64/26?",
             ["10.20.0.63", "10.20.0.127", "10.20.0.126", "10.20.0.255"], 1,
             "The subnet runs from .64 to .127 (64 addresses). The last one, .127, is the broadcast address.",
             hint="Add the block size, 64, to the network address and subtract 1.",
             feedback=["10.20.0.63 is the broadcast address of the subnet before this one.", "",
                       "10.20.0.126 is the last usable host, one before the broadcast address.",
                       "10.20.0.255 is the broadcast address of the last /26 in the block."]),
        QUIZ("A laptop shows the address 169.254.17.9 and cannot reach the internet. What is the most likely cause?",
             ["The lease is too long", "The laptop could not reach a DHCP server", "The subnet mask is /30", "The gateway is a layer 3 switch"], 1,
             "A 169.254.x.x address is the automatic fallback. It means that Discover received no Offer.",
             hint="Where does an address in 169.254.0.0/16 come from?",
             feedback=["A lease that is too long would give an old valid address, not 169.254.", "",
                       "A /30 mask is a different problem and would not give a 169.254 address.",
                       "A layer 3 switch is a normal gateway; it does not cause the fallback address."]),
        H("Practice questions"),
        PQ("Name the four DHCP messages in order and say which two are sent by the client.",
           "Discover, Offer, Request, Acknowledge. The client sends Discover and Request; the server sends Offer and Acknowledge."),
        PQ("Calculate the number of usable host addresses in 172.16.5.0/27 and give its network, broadcast and first and last usable addresses.",
           "A /27 has 5 host bits, 32 addresses, so 30 usable. Network 172.16.5.0, usable 172.16.5.1 to 172.16.5.30, broadcast 172.16.5.31."),
        PQ("An office uses 192.168.1.0/24. The router is .1, a server .2, printers .3 and .4. Write a DHCP scope for the PCs and state a sensible lease for an office where PCs stay all day.",
           "Exclude 192.168.1.1 to 192.168.1.10 (leaving spare fixed addresses). Pool: 192.168.1.11 to 192.168.1.254 (244 addresses). Mask 255.255.255.0, gateway 192.168.1.1, a DNS server. Since PCs stay all day, a lease of 8 hours to 1 day is suitable."),
           PQ("Explain why a public Wi-Fi hotspot should use a short lease time.",
           "Many different devices come and go. With a long lease each departed device still holds an address, so the pool can be used up even though few devices are connected. A short lease returns the addresses quickly so new users can be served."),
        H("Summary"),
        SUM("DORA: Discover and Request come from the client, Offer and Acknowledge from the server.",
            "Usable hosts = 2 to the power (host bits) minus 2; the network and broadcast addresses are not usable.",
            "Exclude or reserve fixed-address devices; set mask, gateway, DNS and lease in the scope.",
            "Short leases suit busy public networks; a 169.254 address means DHCP failed; a relay agent lets one server serve many subnets."),
    ],
))

# ---------------------------------------------------------------------------
# Security principles 1: AAA, non-repudiation, least privilege
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Security principles",
    title="Authentication, authorisation, accounting and least privilege",
    slug="ic7-authentication-authorisation-and-least-privilege",
    minutes=22,
    summary="Go beyond the triad: prove who a user is, decide what that user may do, record what was done, and apply least privilege and defence in depth to a school or mobile-money system.",
    objectives=[
        "Distinguish authentication, authorisation and accounting",
        "Classify authentication factors and explain why multi-factor authentication is stronger",
        "Build a simple access control matrix from roles and apply least privilege",
        "Explain non-repudiation and defence in depth with examples",
    ],
    key_concepts=["Authentication", "Authorisation", "Accounting", "Multi-factor authentication", "Least privilege", "Separation of duties", "Non-repudiation", "Defence in depth"],
    blocks=[
        H("Introduction"),
        T("When you withdraw money at a Mobile Money kiosk, three things happen. The agent checks that you own the account (your SIM and "
          "your PIN). The system checks that you are allowed to withdraw that amount. Then the transaction is written to a log with the "
          "time, the agent and the amount. These are three different security jobs, and the CIA triad does not name them. "
          "Security engineers call them **authentication, authorisation and accounting**, often written **AAA**."),
        H("AAA: three questions"),
        KEY("Who, what, and what happened", "Each step depends on the one before it.",
            cards=[["Authentication", "Who are you? Prove your identity with a password, PIN, token or fingerprint."],
                   ["Authorisation", "What may you do? The system grants rights to the proven identity: read, write, approve, delete."],
                   ["Accounting", "What did you do? Logs record who did what and when, so that misuse can be found and users held responsible."]]),
        D("Authentication factors are of three kinds: something you **know** (password, PIN), something you **have** (SIM card, bank token, phone), "
          "something you **are** (fingerprint, face). **Multi-factor authentication (MFA)** uses factors from at least two different kinds.",
          title="Authentication factors",
          note="A password plus a security question is NOT multi-factor: both are things you know. A PIN plus a SIM card is multi-factor."),
        EX("Worked example 1: classifying the controls in a Mobile Money withdrawal", intro=(
            "Agent Ngwa serves a customer. The customer must (1) insert the SIM in the phone, (2) type a 4-digit PIN, (3) show a national ID card. The agent's screen shows only the amount requested, and every withdrawal is stored with the agent's number. Name the AAA step and factor for each."),
           steps=[
               S("SIM card", text="Authentication, factor: something you have."),
               S("PIN", text="Authentication, factor: something you know. SIM and PIN together are multi-factor authentication."),
               S("ID card", text="A further identity check by a person: something you have (a document)."),
               S("Screen shows only the amount", text="Authorisation and least privilege: the agent sees only what the job needs, not the balance or the PIN."),
               S("Each withdrawal stored with the agent number", text="Accounting: the action is traced to a person, so disputes can be investigated."),
           ]),
        H("Authorisation and least privilege"),
        D("**Least privilege** means giving a user only the rights needed for the job, no more. **Separation of duties** means that no single person can complete a sensitive process alone, for example one person enters a payment and another approves it. **Role-based access control (RBAC)** gives rights to roles, and users receive rights through their roles.",
          title="Least privilege, separation of duties, RBAC"),
        EX("Worked example 2: an access control matrix for a school marks system", intro=(
            "A school has three roles: Teacher, Head of department (HOD) and Student. The marks system has the objects: own class marks, other classes' marks, and the final transcript. Teachers enter marks of their own class. The HOD approves marks and prints transcripts. Students view only their own transcript. Draw the matrix and check separation of duties."),
           steps=[
               S("List rights per role", text="Teacher: enter and view own class marks. HOD: view all marks, approve marks, print transcripts. Student: view own transcript."),
               S("Write the matrix", text="Use R for read, W for write (enter or change), A for approve, P for print, and a dash for no access."),
               S("Check least privilege", text="A teacher cannot approve or see other classes. A student cannot change anything. Each role has only what it needs."),
               S("Check separation of duties", text="Marks are entered by the teacher but approved by the HOD, so no single person can enter and approve a mark."),
           ]),
        CODE("""
Object                  Teacher   HOD     Student
Own class marks         R, W      R, A    -
Other classes' marks    -         R, A    -
Final transcript        -         R, P    R (own only)
""", "text", title="Listing 1: access control matrix",
             caption="Reading across a row shows who can do what to an object. Reading down a column shows everything one role can do."),
        QUIZ("A bank requires an ATM card and a PIN. Which statement is correct?",
             ["It is single-factor because both are used at the same machine",
              "It is multi-factor: the card is something you have and the PIN is something you know",
              "It is multi-factor: both are something you know", "It is accounting, not authentication"], 1,
             "Two different kinds of factor (have and know) make it multi-factor authentication.",
             hint="Put each item into know, have or are.",
             feedback=["Using one machine does not matter. What counts is the number of different factor kinds.", "",
                       "A card is something you hold, not something you remember.",
                       "Proving identity is authentication; accounting is recording actions."]),
        H("Accounting, non-repudiation and defence in depth"),
        D("**Non-repudiation** means that a person cannot later deny an action, because there is reliable evidence: a log entry, a digital signature, a signed receipt. It needs good authentication (so the log really names that person) and tamper-proof records (integrity).",
          title="Non-repudiation"),
        D("**Defence in depth** means using several independent layers of protection so that if one fails the next still stops the attacker: for example a fence and guard (physical), a firewall (network), a patched system, an account with least privilege, encrypted data, and backups.",
          title="Defence in depth"),
        EX("Worked example 3: layers for a microfinance office", intro=(
            "An office in Bafoussam stores savings records. List one control in each of four layers: physical, network, system and data."),
           steps=[
               S("Physical layer", text="A locked server room with a visitor book, so a thief cannot walk to the machine."),
               S("Network layer", text="A firewall that allows only the application port from the cashiers' computers."),
               S("System layer", text="Patches installed monthly, antivirus, and individual accounts with least privilege."),
               S("Data layer", text="Encrypted disk and encrypted off-site backup, so a stolen machine or tape gives nothing away."),
               S("Why layers", text="If a cashier is tricked into opening a malicious attachment (system layer), the firewall and least privilege still limit what the attacker can reach."),
           ]),
        MISTAKE("Thinking a longer password makes a system multi-factor", "Two passwords are still two things you know. MFA needs factors of different kinds."),
        MISTAKE("Sharing one login for the whole office", "A shared account destroys accounting and non-repudiation: the log cannot say who did a transaction. Give each user their own account."),
        MISTAKE("Giving administrator rights to make work easy", "An administrator account used for everyday work lets a single mistake or malware infection damage the whole system. Use least privilege."),
        H("Practice questions"),
        PQ("Define authentication, authorisation and accounting, with one example of each from a school computer lab.",
           "Authentication: proving identity, for example logging in with a username and password. Authorisation: deciding what the logged-in user may do, for example students can open their own folder but not install software. Accounting: recording what happened, for example a log of logins and file changes."),
        PQ("State three factors a customer could use for a bank transfer by phone and say which kind each is.",
           "A PIN or password (something you know), a one-time code sent to the registered SIM or generated by a token (something you have), a fingerprint scan (something you are)."),
        PQ("Explain how separation of duties helps stop fraud in a school bursary office.",
           "If one clerk records payments and a different person approves and banks them, a fraudster would need the cooperation of both. This makes secret theft harder and makes errors more likely to be noticed."),
        PQ("Using the matrix in this lesson, a teacher asks for the right to approve marks 'to save time'. Give two reasons why the school should refuse.",
           "It would break least privilege (approval is not needed for entering marks) and separation of duties (the same person could enter and approve any mark, so errors or cheating would not be caught). It would also reduce non-repudiation because the approval would no longer be an independent check."),
        H("Summary"),
        SUM("AAA: authenticate (who), authorise (what allowed), account (what was done).",
            "Factors: know, have, are. Multi-factor means at least two different kinds.",
            "Least privilege, role-based access and separation of duties limit the damage one person or account can do.",
            "Accounting needs personal accounts; together with integrity it gives non-repudiation.",
            "Defence in depth uses independent layers: physical, network, system and data."),
    ],
))

# ---------------------------------------------------------------------------
# Security principles 2: threats, vulnerabilities and risk assessment
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Security principles",
    title="Threats, vulnerabilities and risk assessment",
    slug="ic7-threats-vulnerabilities-and-risk-assessment",
    minutes=24,
    summary="List common threats, link each to the CIA property it attacks, score risks by likelihood and impact, calculate annual loss, and decide whether a control is worth its cost.",
    objectives=[
        "Name common attacks and the CIA property each one attacks",
        "Score and rank risks with a likelihood and impact matrix",
        "Calculate single loss expectancy and annualised loss expectancy",
        "Estimate password search spaces and judge whether a control is cost-effective",
    ],
    key_concepts=["Threat", "Vulnerability", "Risk", "Likelihood", "Impact", "Risk matrix", "ALE", "Brute force", "Phishing", "Ransomware", "Denial of service", "SQL injection"],
    blocks=[
        H("Introduction"),
        T("A cooperative bank in Bamenda has a budget of 500 000 FCFA for security this year. It cannot buy everything. Should it buy a "
          "generator, an antivirus licence, a staff training course or a second server? **Risk assessment** is the method for choosing: "
          "find what can go wrong, estimate how likely and how costly it is, then spend the money where it reduces the most risk."),
        H("Common threats and what they attack"),
        CODE("""
Threat                 How it works                                  CIA property
Phishing               Fake email or SMS tricks a user into giving   Confidentiality
                       a password or PIN
Malware (virus, worm)  Harmful code copies itself or damages files   Integrity, availability
Ransomware             Encrypts the files and demands payment        Availability
Denial of service      Floods a server with requests so real users   Availability
(DoS, DDoS)            cannot get in
SQL injection          Attacker types SQL code into a web form so    Confidentiality, integrity
                       the database runs it
Brute force            Tries many passwords until one works           Confidentiality
Insider misuse         A trusted user reads or edits data wrongly     Confidentiality, integrity
Power cut, fire,       Hardware stops or is destroyed                 Availability
flood
""", "text", title="Listing 1: threats mapped to the CIA triad",
             caption="Most real incidents touch more than one property. The table shows the main one."),
        D("A **threat** can cause harm. A **vulnerability** is a weakness it can exploit. **Risk** is the chance that a threat uses a vulnerability, combined with the harm that would follow.",
          title="Threat, vulnerability, risk",
          note="Without a vulnerability a threat is harmless: a ransomware infection cannot encrypt a file backup that is offline."),
        H("Scoring risk with a matrix"),
        T("In a qualitative risk assessment each risk gets a **likelihood** score and an **impact** score, usually from 1 (very low) to 5 "
          "(very high). The **risk score** is likelihood multiplied by impact, so it runs from 1 to 25. A common KKEVO-style banding is "
          "1 to 5 low, 6 to 12 medium and 13 to 25 high. Banding is a policy choice: each organisation sets its own."),
        EX("Worked example 1: ranking the risks of the cooperative bank", intro=(
            "The manager scores five risks (likelihood, impact): power cut (5, 3), phishing (4, 4), ransomware (3, 5), stolen laptop (2, 3), server fire (1, 5). Work out each score, band it, and rank the risks."),
           steps=[
               S("Multiply likelihood by impact", text="Power cut 5 x 3 = 15. Phishing 4 x 4 = 16. Ransomware 3 x 5 = 15. Stolen laptop 2 x 3 = 6. Server fire 1 x 5 = 5."),
               S("Band them", text="15, 16, 15 are high (13 to 25). 6 is medium (6 to 12). 5 is low (1 to 5)."),
               S("Rank", text="Phishing (16), then power cut and ransomware (15 each), then stolen laptop (6), then server fire (5)."),
               S("Choose actions", text="The three high risks come first: staff training and email filtering for phishing, a UPS and generator for power, offline backups for ransomware. A server fire has a high impact but is so unlikely that insurance and an off-site backup may be enough."),
           ]),
        H("Putting a value on risk"),
        D("**Single loss expectancy (SLE)** is the cost of one incident: asset value multiplied by the exposure factor (the fraction of the asset lost). **Annual rate of occurrence (ARO)** is how many times per year the incident is expected. **Annualised loss expectancy (ALE)** is the expected yearly loss.",
          title="Quantitative risk", formula=r"\text{ALE} = \text{SLE}\times\text{ARO},\qquad \text{SLE} = \text{asset value}\times\text{exposure factor}"),
        EX("Worked example 2: is the control worth buying?", intro=(
            "The bank server is worth 2 000 000 FCFA. A power surge would damage 40 percent of its value and is expected once every two years. A UPS with surge protection costs 250 000 FCFA per year (purchase spread over its life, plus upkeep) and cuts the rate to once every ten years. Is it worth it?"),
           steps=[
               S("SLE", text="2 000 000 x 0.40 = 800 000 FCFA per incident.", math=r"2\,000\,000\times 0.40 = 800\,000"),
               S("ALE before the control", text="ARO = 1/2 = 0.5, so ALE = 800 000 x 0.5 = 400 000 FCFA per year.", math=r"800\,000\times 0.5 = 400\,000"),
               S("ALE after the control", text="ARO = 1/10 = 0.1, so ALE = 800 000 x 0.1 = 80 000 FCFA per year.", math=r"800\,000\times 0.1 = 80\,000"),
               S("Value of the control", text="Risk reduced = 400 000 - 80 000 = 320 000 per year. Cost 250 000. Net benefit = 320 000 - 250 000 = 70 000 FCFA per year.", math=r"320\,000 - 250\,000 = 70\,000"),
               S("Decision", text="The net benefit is positive, so buy it. If the cost were more than 320 000, the control would cost more than the loss it prevents."),
           ]),
        H("Password search spaces"),
        T("A **brute-force** attack tries every possible password. The number of possibilities is the size of the character set raised to the "
          "length. Suppose an attacker's computer can test 1 000 000 000 (one billion) passwords per second against a stolen list of hashes."),
        CODE("""
Password type                       Possibilities       Time at 1 billion per second
4-digit PIN (10^4)                  10 000              0.00001 s
6-digit PIN (10^6)                  1 000 000           0.001 s
8 lower-case letters (26^8)         208 827 064 576     about 209 s (3.5 minutes)
8 letters and digits, both cases    218 340 105 584 896 about 2.5 days
(62^8)
12 letters and digits (62^12)       3.2 x 10^21         about 100 000 years
""", "text", title="Listing 2: how length and variety change the search",
             caption="Length matters more than special characters: each added character multiplies the work by the size of the character set."),
        QUIZ("A risk has likelihood 4 and impact 5 on the 1 to 5 scales. Using the bands in this lesson, what is its rating?",
             ["Low, score 9", "Medium, score 9", "High, score 20", "High, score 9"], 2,
             "4 x 5 = 20, which is in the high band (13 to 25).",
             hint="Multiply the two scores first.",
             feedback=["Adding 4 + 5 gives 9, but risk uses multiplication.", "Adding gives 9 again; multiply instead.", "",
                       "The score is 20, not 9."]),
        MISTAKE("Adding likelihood and impact", "The risk score is a product. A very unlikely, very costly event and a likely, trivial one should not look the same as a likely and costly one."),
        MISTAKE("Treating the ALE as a prediction for next year", "ALE is an average. A server fire expected once in 50 years can still happen next week. Use ALE to compare options, not to promise outcomes."),
        MISTAKE("Using one control for every risk", "A firewall does not stop a power cut and a UPS does not stop phishing. Match each control to the threat and vulnerability it addresses."),
        H("Practice questions"),
        PQ("Name the CIA property mainly attacked by ransomware, by phishing, and by a denial-of-service attack.",
           "Ransomware: availability (files cannot be used). Phishing: confidentiality (credentials are disclosed). Denial of service: availability (the service is unreachable)."),
        PQ("A lab has these risks, each as (likelihood, impact): virus on USB sticks (4, 3), theft of a PC (2, 4), flood (1, 5). Calculate the scores and say which should be handled first.",
           "Virus 4 x 3 = 12, theft 2 x 4 = 8, flood 1 x 5 = 5. The virus risk has the highest score (12) so it is handled first, for example with antivirus, scanning of USB drives and training."),
        PQ("A printing shop's computer is worth 600 000 FCFA. Theft would lose all of it (exposure factor 1) and is expected once every four years. Calculate the SLE and ALE. A lock and alarm costing 40 000 FCFA per year would cut theft to once in twenty years. Is it worth buying?",
           "SLE = 600 000. ALE before = 600 000 x 0.25 = 150 000. ALE after = 600 000 x 0.05 = 30 000. Reduction 120 000 per year, cost 40 000, net benefit 80 000 per year. Yes, worth buying."),
        PQ("Compare the number of possible 6-digit PINs with the number of possible 8-letter lower-case passwords and say which is easier to brute force.",
           "6-digit PINs: 10^6 = 1 000 000. 8 lower-case letters: 26^8 = 208 827 064 576. The PIN has far fewer possibilities, so it is far easier to brute force, which is why PINs are safe only when the system limits the number of attempts."),
        H("Summary"),
        SUM("Match threats to the CIA property they attack: phishing and brute force to confidentiality, ransomware and DoS to availability, malware and SQL injection to integrity as well.",
            "Risk score = likelihood x impact, then band as low, medium or high.",
            "SLE = asset value x exposure factor; ALE = SLE x ARO; a control is worth buying if the ALE it removes is more than its cost.",
            "Search space = characters to the power length; length defeats brute force."),
    ],
))

# ---------------------------------------------------------------------------
# Cryptography 1: symmetric encryption and AES
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Cryptography",
    title="Symmetric encryption: from the Caesar cipher to AES",
    slug="ic7-symmetric-encryption-and-aes",
    minutes=22,
    summary="Encrypt and decrypt with a Caesar shift and XOR, see why simple ciphers fail, then describe AES block size, key lengths and modes, and count the keys needed by a group.",
    objectives=[
        "Apply a Caesar shift and a bitwise XOR key to encrypt and decrypt",
        "Explain why a small key space or simple substitution is insecure",
        "State the block size, key lengths and rounds of AES and the weakness of ECB mode",
        "Calculate how many secret keys a group needs with symmetric encryption",
    ],
    key_concepts=["Plaintext", "Ciphertext", "Key", "Caesar cipher", "XOR", "Symmetric encryption", "AES", "Block cipher", "Key distribution", "Brute force"],
    blocks=[
        H("Introduction"),
        T("Every time a phone sends a Mobile Money request, a school uploads results over Wi-Fi, or a bank shows a padlock in the browser, "
          "**encryption** protects the data. Encryption turns readable **plaintext** into unreadable **ciphertext** using an algorithm and a "
          "**key**. In **symmetric encryption** the same secret key encrypts and decrypts. This lesson starts with a cipher you can do by hand, "
          "learns why it is weak, and then studies AES, the standard used today."),
        H("A cipher by hand: Caesar"),
        D("The **Caesar cipher** moves each letter a fixed number of places along the alphabet. The shift is the key. To decrypt, shift back by the same amount.",
          title="Caesar cipher"),
        EX("Worked example 1: encrypting CAMEROON with shift 3", intro=("Encrypt CAMEROON with key 3, then decrypt the result."),
           steps=[
               S("Shift each letter 3 places forward", text="C goes to F, A to D, M to P, E to H, R to U, O to R, O to R, N to Q."),
               S("Write the ciphertext", text="FDPHURRQ."),
               S("Decrypt by shifting back 3", text="F to C, D to A, P to M, H to E, U to R, R to O, R to O, Q to N: CAMEROON."),
           ]),
        T("The Caesar cipher has only 25 useful keys, so an attacker can try them all (**brute force**) in a minute. Even a general "
          "substitution cipher, with any letter replaced by any other (more than 400 000 000 000 000 000 000 000 000 keys), falls to "
          "**frequency analysis**: in English the letter E is the most common, and the most common letter in the ciphertext is probably E. "
          "The lessons: the key space must be huge, and the cipher must hide the pattern of the language."),
        H("XOR: the building block"),
        D("**XOR** (exclusive OR) gives 1 when its two input bits differ and 0 when they are equal. XORing with the same key twice restores the original: (P XOR K) XOR K = P.",
          title="XOR"),
        EX("Worked example 2: XOR with a one-byte key", intro=(
            "Encrypt the letter K (ASCII 75, binary 01001011) with the key 01011010, then decrypt it."),
           steps=[
               S("Write both bytes", text="Plaintext 01001011, key 01011010."),
               S("XOR bit by bit", text="Pair the bits from the left: 0,0 gives 0; 1,1 gives 0; 0,0 gives 0; 0,1 gives 1; 1,1 gives 0; 0,0 gives 0; 1,1 gives 0; 1,0 gives 1. The result is 00010001."),
               S("Decrypt", text="XOR 00010001 with the same key 01011010 and you get 01001011 again, which is K."),
           ], check=r"01001011 \oplus 01011010 = 00010001"),
        T("XOR with a short repeating key is weak, but XOR is used inside modern ciphers, combined with substitution and shuffling steps."),
        H("AES"),
        D("**AES (Advanced Encryption Standard)** is a symmetric **block cipher**. It works on blocks of **128 bits** (16 bytes) and uses a key of **128, 192 or 256 bits**, with 10, 12 or 14 rounds respectively. Each round substitutes bytes, shifts rows, mixes columns and adds a round key (the last round omits the column mixing).",
          title="AES"),
        T("With a 128-bit key there are 2 to the power 128 keys, about 3.4 followed by 38 zeros. Even a machine trying a million million "
          "(10 to the power 12) keys per second would need about 10 billion billion years to try them all. So AES is not broken by brute force. "
          "Real attacks target weak passwords, stolen keys, or mistakes in how AES is used."),
        KEY("Modes of operation", "A block cipher encrypts one block. A mode says how to handle a long message.",
            cards=[["ECB", "Each block is encrypted alone. Equal plaintext blocks give equal ciphertext blocks, so patterns in a picture or table remain visible. Avoid it."],
                   ["CBC", "Each block is mixed with the previous ciphertext block, using a random starting value (IV). Hides patterns."],
                   ["GCM", "A counter-based mode that also produces an authentication tag, so changes to the ciphertext are detected (confidentiality and integrity)."]]),
        H("The key distribution problem"),
        T("With symmetric encryption every pair of people who want private communication needs its own shared key, and the keys must be "
          "delivered secretly. For n people the number of pair keys is n(n - 1) / 2."),
        EX("Worked example 3: keys in a growing network", intro=("A bank links 10 branches so that every pair of branches shares a different symmetric key. How many keys are needed? What if there are 100 branches?"),
           steps=[
               S("Use the formula for 10 branches", text="10 x 9 / 2 = 45 keys.", math=r"\frac{10\times 9}{2}=45"),
               S("Use it for 100 branches", text="100 x 99 / 2 = 4950 keys.", math=r"\frac{100\times 99}{2}=4950"),
               S("Comment", text="The number grows with the square of the group size, and each key must be sent to two places in secret. This is the key distribution problem, which asymmetric encryption (next lesson) helps to solve."),
           ]),
        QUIZ("Which statement about AES is correct?",
             ["It is an asymmetric cipher with a public and a private key", "It encrypts blocks of 128 bits with a 128, 192 or 256-bit key",
              "It can only use 56-bit keys", "It is a hashing algorithm"], 1,
             "AES is a symmetric block cipher: 128-bit blocks, keys of 128, 192 or 256 bits.",
             hint="Is the same key used for both directions?",
             feedback=["Asymmetric ciphers such as RSA use key pairs. AES uses one shared key.", "",
                       "56 bits was the key size of the older DES, which is now too small.",
                       "Hash functions have no key and cannot be reversed; AES is reversible with the key."]),
        MISTAKE("Thinking a secret algorithm is more secure", "Strong systems assume the attacker knows the algorithm. Security must come from the key alone."),
        MISTAKE("Using ECB mode for files", "Equal blocks give equal ciphertext, so patterns leak. Use CBC or GCM with a fresh random IV."),
        MISTAKE("Sending the key with the message", "If the key travels with the ciphertext, the attacker has both. The key must be shared by a separate secure route."),
        H("Practice questions"),
        PQ("Encrypt the word DOUALA with a Caesar shift of 5, and show how to decrypt it.",
           "D to I, O to T, U to Z, A to F, L to Q, A to F, so the ciphertext is ITZFQF. To decrypt, shift each letter back 5 places: I to D, T to O, Z to U, F to A, Q to L, F to A, giving DOUALA."),
        PQ("Give two reasons why a Caesar cipher is insecure.",
           "There are only 25 possible keys, so all can be tried quickly (brute force). Each letter always maps to the same letter, so frequency analysis of the ciphertext reveals the pattern of the language."),
        PQ("State the block size and the three key lengths of AES.",
           "Block size 128 bits. Key lengths 128, 192 and 256 bits."),
        PQ("Twenty teachers in a school want to exchange confidential messages, each pair using its own secret AES key. How many keys are needed? State one difficulty.",
           "20 x 19 / 2 = 190 keys. The difficulty is distributing and storing so many keys securely, because every key must reach both people secretly."),
        H("Summary"),
        SUM("Symmetric encryption uses one shared secret key; the key, not the algorithm, must be secret.",
            "Caesar and simple substitution fail to brute force and frequency analysis; XOR with the same key twice restores the data.",
            "AES: 128-bit blocks, 128/192/256-bit keys, 10/12/14 rounds; avoid ECB mode and prefer CBC or GCM.",
            "n people need n(n - 1) / 2 pair keys: the key distribution problem."),
    ],
))

# ---------------------------------------------------------------------------
# Cryptography 2: RSA with small primes
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Cryptography",
    title="Asymmetric encryption and RSA with small primes",
    slug="ic7-asymmetric-encryption-and-toy-rsa",
    minutes=25,
    summary="Generate an RSA key pair from two small primes, encrypt and decrypt a number by hand with modular arithmetic, and explain why real RSA is safe and how it is combined with AES.",
    objectives=[
        "Explain public and private keys and which one encrypts and which one decrypts",
        "Generate an RSA key pair from two small primes",
        "Encrypt and decrypt a message number using modular exponentiation",
        "Describe why RSA is secure and how hybrid encryption combines RSA and AES",
    ],
    key_concepts=["Asymmetric encryption", "Public key", "Private key", "RSA", "Modulus", "Euler totient", "Modular exponentiation", "Hybrid encryption"],
    blocks=[
        H("Introduction"),
        T("You want a farmer in Ndop to send you his bank details without anyone listening. You cannot meet him to share a secret key. "
          "**Asymmetric encryption** solves this. Everyone has a **pair** of keys. The **public key** can be given to the whole world and is "
          "used to encrypt. The matching **private key** is kept secret and is the only key that can decrypt. "
          "Anyone can lock the box, only the owner has the key to open it."),
        D("In **asymmetric encryption** a message encrypted with a public key can be decrypted only with the matching private key. The reverse is used for signatures: something produced with the private key can be checked by anyone with the public key.",
          title="Asymmetric encryption"),
        H("The RSA recipe"),
        T("RSA (named after Rivest, Shamir and Adleman) relies on a fact: multiplying two large primes is easy, but finding them from the "
          "product is extremely hard. Here is the recipe, with small primes so you can do it by hand."),
        KEY("Generating an RSA key pair", "Five steps.",
            cards=[["1. Choose two primes", "p and q. Real keys use primes of about 1000 bits each."],
                   ["2. Modulus", "n = p x q. This number is public."],
                   ["3. Totient", "phi = (p - 1)(q - 1). Keep it secret (it needs the factors)."],
                   ["4. Public exponent e", "Choose e with 1 < e < phi and no common factor with phi."],
                   ["5. Private exponent d", "Find d with (e x d) mod phi = 1. Public key is (n, e); private key is (n, d)."]]),
        F(r"c = m^{e} \bmod n \qquad m = c^{d} \bmod n", title="Encryption and decryption"),
        T("The message must be a number m smaller than n. Real software converts text to numbers and adds padding."),
        EX("Worked example 1: a key pair from p = 5 and q = 11", intro=("Generate a key pair using p = 5, q = 11 and e = 3. Then encrypt m = 9 and decrypt the result."),
           steps=[
               S("Modulus", text="n = 5 x 11 = 55.", math=r"n = 55"),
               S("Totient", text="phi = (5 - 1)(11 - 1) = 4 x 10 = 40.", math=r"\varphi = 40"),
               S("Check e", text="e = 3 has no common factor with 40 (gcd = 1), and 1 < 3 < 40. Good."),
               S("Find d", text="We need 3 x d to leave remainder 1 when divided by 40. Try d = 27: 3 x 27 = 81 = 2 x 40 + 1. So d = 27.", math=r"3\times 27 = 81 = 2\times 40 + 1"),
               S("Keys", text="Public key (55, 3). Private key (55, 27)."),
               S("Encrypt m = 9", text="9 cubed is 729. Divide by 55: 13 x 55 = 715, remainder 14. So c = 14.", math=r"9^3 = 729,\ 729 - 13\times 55 = 14"),
               S("Decrypt c = 14", text="Compute 14 to the power 27 mod 55 (see the table next). The result is 9, the original message.", math=r"14^{27} \bmod 55 = 9"),
           ]),
        T("The hard part by hand is 14 to the power 27, a huge number. Use **repeated squaring**: write the exponent as a sum of powers of two, "
          "27 = 16 + 8 + 2 + 1. Square the base again and again, reducing mod 55 each time, and multiply together only the powers you need."),
        CODE("""
Power of 14    Working                    Result mod 55
14^1           14                         14
14^2           14 x 14 = 196              31   (196 - 3 x 55)
14^4           31 x 31 = 961              26   (961 - 17 x 55)
14^8           26 x 26 = 676              16   (676 - 12 x 55)
14^16          16 x 16 = 256              36   (256 - 4 x 55)

14^27 = 14^16 x 14^8 x 14^2 x 14^1
36 x 16 = 576  -> 26 (mod 55)
26 x 31 = 806  -> 36 (mod 55)
36 x 14 = 504  -> 9  (mod 55)
""", "text", title="Listing 1: repeated squaring for 14^27 mod 55",
             caption="Every number stays below 55 x 55, so the arithmetic is easy. Computers use the same idea for 2048-bit numbers."),
        EX("Worked example 2: another key pair, p = 7 and q = 11", intro=("Use p = 7, q = 11, e = 7. Find d, then encrypt m = 5."),
           steps=[
               S("n and phi", text="n = 77 and phi = 6 x 10 = 60.", math=r"n = 77,\ \varphi = 60"),
               S("Check e", text="gcd(7, 60) = 1, so e = 7 is allowed."),
               S("Find d", text="7 x 43 = 301 = 5 x 60 + 1, so d = 43. Public key (77, 7); private key (77, 43)."),
               S("Encrypt m = 5", text="5 to the power 7 = 78 125. 77 x 1014 = 78 078, and 78 125 - 78 078 = 47. So c = 47.", math=r"5^7 = 78125 \equiv 47 \pmod{77}"),
               S("Decrypt", text="47 to the power 43 mod 77 = 5 (done by repeated squaring or by a calculator program). The message is recovered."),
           ]),
        MISTAKE("Choosing e with a common factor", "If e = 2 and phi = 40, the numbers share the factor 2 and no d exists. Always check gcd(e, phi) = 1."),
        MISTAKE("Using a message larger than n", "With n = 55, a message of 60 would be reduced mod 55 and decrypt to 5. Real systems split messages and add padding."),
        MISTAKE("Mixing up the keys", "Encrypt for someone with THEIR public key. Decrypt with YOUR private key. If you encrypt with your own private key, anyone can open it, which is useful for signatures but not for secrecy."),
        QUIZ("Sara wants to send Pierre a secret message with RSA. Which key does she use to encrypt it?",
             ["Sara's private key", "Pierre's private key", "Pierre's public key", "Sara's public key"], 2,
             "A secret message is encrypted with the receiver's public key so that only the receiver's private key can decrypt it.",
             hint="Who must be able to read the message?",
             feedback=["If Sara encrypted with her private key, anyone with her public key could decrypt it.",
                       "Pierre's private key must stay secret and Sara should not have it.", "",
                       "Only Sara's private key could decrypt that, and Pierre does not have it."]),
        H("Why RSA is safe, and why we still need AES"),
        T("With n = 55 anyone can find that 55 = 5 x 11 and compute d. With a 2048-bit n there is no known fast way to factor it with ordinary "
          "computers, so the private key cannot be found from the public key. (Large quantum computers could change this, so research on "
          "new algorithms is under way.) RSA is also far slower than AES. So real systems use **hybrid encryption**: choose a random AES "
          "key, encrypt the message with AES, then encrypt only the short AES key with RSA. This is how secure web connections start."),
        EX("Worked example 3: hybrid encryption of a school report", intro=("A school in Kribi sends a 5 MB report to the regional office. Explain the steps."),
           steps=[
               S("Sender makes a session key", text="The sender's software generates a random 256-bit AES key."),
               S("Encrypt the report", text="The 5 MB file is encrypted with AES, which is fast."),
               S("Protect the key", text="The 256-bit AES key is encrypted with the regional office's RSA public key. This is small and quick."),
               S("Send both", text="The encrypted report and the encrypted key travel to the office."),
               S("Receiver decrypts", text="The office decrypts the AES key with its private RSA key, then decrypts the report with AES."),
           ]),
        H("Practice questions"),
        PQ("Using p = 3, q = 11 and e = 3, find n, phi and d. Then encrypt m = 4.",
           "n = 33, phi = 2 x 10 = 20. d satisfies 3 x d mod 20 = 1; d = 7 because 21 = 20 + 1. Encrypt: 4 cubed = 64; 64 - 33 = 31, so c = 31. Check: 31 to the power 7 mod 33 = 4."),
        PQ("Why is it a problem if the private key is stored on the same server as the encrypted data and the server is stolen?",
           "The thief obtains both the ciphertext and the key that decrypts it, so encryption gives no protection. Private keys should be protected separately, for example on a hardware device or password-protected store."),
        PQ("Explain why systems use RSA to send an AES key instead of using RSA to encrypt a whole large file.",
           "RSA is much slower than AES and can only encrypt data smaller than its modulus. AES is fast for large data. Using RSA only for the short AES key gives both the easy key exchange of asymmetric encryption and the speed of symmetric encryption."),
        PQ("An attacker knows the public key (55, 3). Explain how she could find the private key, and why this is not possible for real RSA keys.",
           "She factors 55 into 5 and 11, computes phi = 40 and then finds d = 27. For a real key n has about 600 digits and no known method factors it in a reasonable time on ordinary computers, so this attack fails."),
        H("Summary"),
        SUM("Public key encrypts, private key decrypts; the public key can be shared openly.",
            "RSA: n = p x q, phi = (p - 1)(q - 1), choose e coprime with phi, find d with e x d mod phi = 1.",
            "Encrypt c = m^e mod n; decrypt m = c^d mod n; use repeated squaring by hand.",
            "Security relies on the difficulty of factoring n; hybrid encryption pairs RSA with AES."),
    ],
))

# ---------------------------------------------------------------------------
# Cryptography 3: SHA-256 hashing
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Cryptography",
    title="SHA-256 hashing: integrity checks and password storage",
    slug="ic7-sha256-hashing-and-password-storage",
    minutes=22,
    summary="Explain what a cryptographic hash is, see the avalanche effect on real SHA-256 outputs, check a download, and store passwords safely with a salt.",
    objectives=[
        "State the properties of a cryptographic hash function",
        "Describe SHA-256 output size and the avalanche effect",
        "Use hashes to check file integrity and to store passwords",
        "Explain why salting defeats precomputed tables and identical hashes",
    ],
    key_concepts=["Hash function", "SHA-256", "Digest", "Avalanche effect", "Collision", "Integrity check", "Salt", "Pre-image"],
    blocks=[
        H("Introduction"),
        T("A teacher in Maroua downloads a 3 GB software package over a slow connection. Halfway, the connection drops and resumes. "
          "Is the file on his disk exactly the one the publisher made? He cannot read 3 GB to check. The publisher gives a short "
          "string of 64 characters, a **hash**. The teacher computes the hash of his copy; if the two strings are equal, the file is "
          "identical. This is the use of a hash function."),
        D("A **cryptographic hash function** turns input of any size into a fixed-size output called the **digest**. It is **deterministic** (same input, same digest), **one-way** (you cannot work backwards from digest to input), and **collision resistant** (it is infeasible to find two different inputs with the same digest). A tiny change in the input changes the digest completely: the **avalanche effect**.",
          title="Cryptographic hash function"),
        D("**SHA-256** (from the SHA-2 family) produces a digest of **256 bits**, shown as **64 hexadecimal characters**. For comparison, MD5 gives 128 bits (32 hex digits) and SHA-1 gives 160 bits (40 hex digits). MD5 and SHA-1 have known collision attacks and should not be used for security.",
          title="SHA-256"),
        H("Seeing a hash"),
        CODE("""
import hashlib

def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

print(sha256("abc"))
print(len(sha256("abc")))
print(sha256("Pay Ngu 5000")[:16])
print(sha256("Pay Ngu 50000")[:16])
""", "python", title="Listing 1: computing SHA-256 in Python"),
        CODE("""
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
64
bfd1246cdb118f24
de8b6f71c59456a9
""", "text", title="Listing 2: the output",
             caption="The hash of abc is a well-known test value. The two payment messages differ by one extra zero, but their digests share nothing."),
        T("When these two digests are compared bit by bit, 130 of the 256 bits are different, about half. That is what the avalanche "
          "effect means: a one-character change flips about half of the output bits, so you cannot tell from the digest how close two inputs are."),
        EX("Worked example 1: detecting a tampered payment", intro=(
            "A treasurer stores the SHA-256 digest of each approved payment instruction on a separate paper sheet. The instruction \"Pay Ngu 5000\" has digest starting bfd1246c. Later the file shows \"Pay Ngu 50000\". How does the treasurer detect the change?"),
           steps=[
               S("Recompute", text="Compute the SHA-256 of the text now in the file. It starts de8b6f71."),
               S("Compare", text="de8b6f71 does not equal bfd1246c, so the text is not the approved one."),
               S("Conclusion", text="The change is detected although the file looks almost the same to a human. A hash protects integrity, but the stored digest must itself be safe from change (here it is on paper), otherwise an attacker could update both."),
           ]),
        H("Storing passwords"),
        T("A website must never store passwords as plain text. If its database leaks, every user is exposed. Instead it stores the "
          "hash of the password. At login it hashes what the user types and compares digests."),
        T("A simple hash has a problem: two users with the same password have the same hash, and attackers keep huge tables of hashes of "
          "common passwords. The fix is a **salt**: a random string stored beside the hash and added to the password before hashing. "
          "The salt is not secret, but every user has a different one."),
        CODE("""
Password: mango123
Unsalted SHA-256 (first 16 digits):           02f4ac0310b7b6c2
Salt x9Q2 + password, SHA-256 (first 16):     d3bf13e16cab7117
Same password, a different salt gives a different digest.
""", "text", title="Listing 3: the effect of a salt",
             caption="Real systems also use a deliberately slow password-hashing function so that each guess costs the attacker time."),
        EX("Worked example 2: why a salt helps", intro=(
            "A leaked database holds unsalted SHA-256 hashes. Two users, Ama and Bello, have the same hash. What does the attacker learn, and what changes if every password has its own salt?"),
           steps=[
               S("Unsalted", text="Equal hashes mean equal passwords. If the attacker cracks one, he has both. A prepared table of common passwords and their hashes can be looked up instantly."),
               S("Salted", text="Each user has a different random salt, so identical passwords give different hashes. The attacker cannot see who shares a password and cannot use a ready-made table."),
               S("What is still needed", text="Strong passwords. A salt does not help if a user's password is 1234 and the attacker can guess it."),
           ]),
        QUIZ("Which of these is NOT a property of a cryptographic hash function?",
             ["Same input always gives the same digest", "A digest can be decrypted to recover the input with a key",
              "Output has a fixed length", "A one-character change alters the digest greatly"], 1,
             "A hash is one-way and has no key. It cannot be decrypted. (That is why it is suitable for password storage.)",
             hint="Which statement describes encryption instead of hashing?",
             feedback=["This is the deterministic property.", "",
                       "SHA-256 always gives 256 bits whatever the input size.",
                       "This is the avalanche effect."]),
        MISTAKE("Calling hashing a type of encryption", "Encryption can be reversed with a key. A hash has no key and cannot be reversed, which makes it right for integrity checks and password storage but wrong for hiding data that must be read later."),
        MISTAKE("Storing the digest next to the data it protects without protection", "An attacker who can change the file can also recompute and replace the digest. The digest must be kept or sent by a separate trusted route, or signed."),
        MISTAKE("Using MD5 or SHA-1 for security", "Both have practical collision attacks. Use SHA-256 or better."),
        H("Practice questions"),
        PQ("State four properties of a cryptographic hash function.",
           "Deterministic (same input gives same digest); fixed-length output; one-way (cannot recover the input from the digest); collision resistant; and the avalanche effect (a small change gives a very different digest). Any four."),
        PQ("How many hexadecimal characters does a SHA-256 digest have, and why?",
           "64. The digest is 256 bits and each hexadecimal digit represents 4 bits, so 256 / 4 = 64."),
        PQ("A software site publishes the SHA-256 digest of a download on its web page. Explain how a user checks the download, and what a mismatch means.",
           "The user computes the SHA-256 digest of the downloaded file and compares it with the published digest. If they are the same, the file is unchanged. A mismatch means the file was corrupted during download or has been altered, so it must not be installed."),
        PQ("Explain why a school's student portal should store a salted hash of each password instead of the password itself.",
           "If the database is stolen the attacker does not get the passwords. Hashing makes passwords unreadable, and a different salt for each user means that identical passwords give different hashes and prepared hash tables cannot be used, so each password must be attacked separately."),
        H("Summary"),
        SUM("A hash maps any input to a fixed-size digest; SHA-256 gives 256 bits, 64 hexadecimal digits.",
            "Properties: deterministic, one-way, collision resistant, avalanche effect.",
            "Integrity: compare the digest of the received file with a trusted published digest.",
            "Passwords: store salted hashes, never plain text; a salt makes every stored hash different."),
    ],
))

# ---------------------------------------------------------------------------
# Cryptography 4: digital signatures, certificates and PKI
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Cryptography",
    title="Digital signatures, certificates and PKI",
    slug="ic7-digital-signatures-certificates-and-pki",
    minutes=24,
    summary="Sign and verify a document with a private and public key (with a toy RSA example), and follow how certificates and certificate authorities let a browser trust a bank's website.",
    objectives=[
        "Describe how a digital signature is created and verified",
        "Say which security properties a signature provides",
        "Explain what a digital certificate contains and how a chain of trust works",
        "Outline how a browser uses a certificate to start a secure connection",
    ],
    key_concepts=["Digital signature", "Certificate", "Certificate authority", "Chain of trust", "PKI", "Non-repudiation", "TLS"],
    blocks=[
        H("Introduction"),
        T("A regional delegate in Bamenda receives a PDF that says: \"Approved: transfer of 20 million FCFA to the new school project.\" It "
          "appears to come from the minister's office. How can she be sure that the document was really sent by the minister and "
          "that nobody changed the amount? On paper, a signature and a stamp do this job. In digital form, we use a **digital signature**."),
        H("How a signature works"),
        D("A **digital signature** is made by computing the hash of the document and then transforming that hash with the signer's **private key**. Anyone can **verify** it with the signer's **public key**: the verifier computes the hash of the received document, recovers the hash from the signature with the public key, and checks that the two are equal.",
          title="Digital signature"),
        IMG("al-ic7-rsa-signature.svg", alt="Flow chart: the sender hashes the document and signs the hash with the private key; the receiver hashes the document, uses the public key on the signature, and compares the two hashes",
            caption="Figure 1. Signing (left) and verifying (right). A match means the document is unchanged and was signed by the owner of the private key."),
        KEY("What a signature gives you", "Three properties.",
            cards=[["Authentication", "Only the owner of the private key could have produced it."],
                   ["Integrity", "Any change to the document changes the hash, so verification fails."],
                   ["Non-repudiation", "The signer cannot deny signing, because only he holds the private key."]],
            note="A signature does NOT hide the document. If secrecy is also needed, the document is encrypted as well."),
        EX("Worked example 1: sign and verify with the toy key (n = 55, e = 3, d = 27)", intro=(
            "The hash of a document is the small number 9 (a real SHA-256 digest has 256 bits; we use a tiny value to calculate by hand). Sign it with the private key (55, 27) and verify with the public key (55, 3)."),
           steps=[
               S("Sign: raise the hash to the power d", text="s = 9 to the power 27 mod 55. By repeated squaring this equals 4.", math=r"s = 9^{27} \bmod 55 = 4"),
               S("Send", text="The document and the signature 4 are sent."),
               S("Verify: raise the signature to the power e", text="4 cubed = 64. 64 - 55 = 9.", math=r"4^3 = 64 \equiv 9 \pmod{55}"),
               S("Compare", text="The receiver also computes the hash of the document received and gets 9. The two are equal, so the signature is valid."),
           ]),
        EX("Worked example 2: a tampered document", intro=(
            "An attacker changes the amount in the document, so that its hash is now 10, but keeps the signature 4. What does the receiver find?"),
           steps=[
               S("Recover the signed hash", text="4 cubed mod 55 = 9."),
               S("Hash the document received", text="The altered document hashes to 10."),
               S("Compare", text="9 is not 10, so verification fails and the document is rejected."),
               S("Why the attacker cannot fix it", text="To produce a signature for hash 10 he would need the private key d = 27, which he does not have."),
           ]),
        H("Certificates and PKI"),
        T("There is one gap. The receiver verifies with a public key, but how does she know that the public key truly belongs to the minister "
          "and not to an impostor? A **digital certificate** closes the gap. It is a small file that binds a public key to an identity, and it is "
          "itself digitally signed by a trusted organisation, a **certificate authority (CA)**."),
        D("A **digital certificate** contains the owner's name (for example the domain name of a bank), the owner's **public key**, the **issuer** (the CA), the **validity dates**, and the **CA's digital signature** over all of this.",
          title="Digital certificate"),
        D("**PKI (public key infrastructure)** is the whole system of CAs, certificates, policies and software that creates, distributes, checks and revokes certificates.",
          title="PKI"),
        T("CAs form a **chain of trust**. A website certificate is signed by an intermediate CA, whose certificate is signed by a root CA. "
          "Browsers and operating systems ship with a list of trusted root certificates, so the chain ends at something the device already trusts."),
        EX("Worked example 3: what the browser checks at a banking site", intro=(
            "A customer opens the website of a bank. The server sends its certificate. List the checks the browser makes."),
           steps=[
               S("Name", text="The domain name in the certificate must match the address in the browser."),
               S("Dates", text="Today's date must be between the start and end dates of the certificate."),
               S("Chain", text="Check the signature on the certificate with the intermediate CA's public key, then the intermediate with the root, and see that the root is in the trusted list."),
               S("Revocation", text="Check that the CA has not cancelled the certificate (a revocation list or an online status check)."),
               S("Use the key", text="If all checks pass, the browser and server use the public key in the certificate to agree on a fresh symmetric session key. After that, all data is encrypted with it (for example AES). This is the TLS handshake in outline."),
           ]),
        QUIZ("Which key does a sender use to create a digital signature, and which key does a receiver use to verify it?",
             ["Sign with the public key, verify with the private key", "Sign with the sender's private key, verify with the sender's public key",
              "Sign and verify with the receiver's keys", "Sign and verify with a shared AES key"], 1,
             "The signer's private key creates the signature; anyone can check it with the signer's public key.",
             hint="Only one person must be able to sign, but everyone must be able to verify.",
             feedback=["If the public key signed, everyone could sign.", "",
                       "The receiver's keys have nothing to do with the sender's identity.",
                       "A shared key would let either side forge a signature, so there would be no non-repudiation."]),
        MISTAKE("Thinking the signature encrypts the message", "A signature proves origin and integrity; the message itself can still be read by anyone. Use encryption for confidentiality."),
        MISTAKE("Trusting a public key without a certificate", "An attacker can publish a key under someone else's name. Only a certificate signed by a trusted CA ties a name to a key."),
        MISTAKE("Ignoring a certificate warning", "A warning means a name, date or chain check failed. Do not continue to enter a password."),
        H("Practice questions"),
        PQ("Describe, in order, how a digital signature is created and verified.",
           "Creation: hash the document with a hash function, then transform the hash with the sender's private key to give the signature; send document and signature. Verification: hash the received document, recover the hash from the signature with the sender's public key, and compare. If equal the signature is valid."),
        PQ("List three security properties provided by a digital signature.",
           "Authentication of the sender, integrity of the document, and non-repudiation (the sender cannot deny signing)."),
        PQ("State four items found in a digital certificate and explain the role of the certificate authority.",
           "Owner's name or domain, owner's public key, issuer, validity dates and the CA's signature. The CA checks the owner's identity and signs the certificate so that others can trust that the public key belongs to that owner."),
        PQ("With the toy key n = 55, e = 3, d = 27, a hash value 14 is to be signed. Find the signature, given that 14 to the power 27 mod 55 = 9. Then verify it.",
           "Signature s = 14^27 mod 55 = 9. Verify: 9^3 = 729, 729 mod 55 = 14, which equals the hash, so the signature is valid."),
        H("Summary"),
        SUM("A signature is a hash transformed with the sender's private key and checked with the sender's public key.",
            "It gives authentication, integrity and non-repudiation, but not secrecy.",
            "A certificate binds a public key to an identity and is signed by a certificate authority; PKI is the system around it.",
            "A browser checks name, dates, chain and revocation before using a site's key to set up an encrypted session."),
    ],
))

# ---------------------------------------------------------------------------
# Defence and recovery 1: firewalls
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Defence and recovery",
    title="Firewall rules, stateful inspection and the DMZ",
    slug="ic7-firewall-rules-state-and-dmz",
    minutes=25,
    summary="Read and write ordered firewall rules, trace packets through them (first match wins, implicit deny), compare stateless, stateful and application firewalls, and place public servers in a DMZ.",
    objectives=[
        "Explain what a firewall does and where it sits",
        "Write an ordered rule list and trace packets through it",
        "Compare packet-filter, stateful and application-layer firewalls",
        "Describe how a DMZ protects an internal network",
    ],
    key_concepts=["Firewall", "Rule", "First match", "Implicit deny", "Stateless filter", "Stateful inspection", "Application firewall", "DMZ", "Port"],
    blocks=[
        H("Introduction"),
        T("A secondary school in Ebolowa has a student lab, an administration office with fee records, and a small web server for the school website. "
          "All of them connect to the internet through one router. Without protection, anyone on the internet could try to log in "
          "to the fee records, and a virus on a student's laptop could reach the bursar's computer. A **firewall** is the device or software that "
          "decides which network traffic is allowed to pass and which is blocked."),
        D("A **firewall** examines packets passing between two networks and permits or blocks each one according to a list of **rules**. A rule usually names a protocol (TCP, UDP or any), a source address, a destination address, a destination **port** and an **action** (permit or deny).",
          title="Firewall"),
        CODE("""
Port  Service               Port  Service
22    SSH (secure shell)    80    HTTP (web)
25    SMTP (sending mail)   443   HTTPS (secure web)
53    DNS (names)           3389  Remote Desktop
""", "text", title="Listing 1: ports used in this lesson",
             caption="A port number tells the server which service the packet is meant for."),
        H("Rules are read in order"),
        KEY("Two rules for every rule list", "Learn these before you trace a packet.",
            cards=[["First match wins", "The firewall tests the rules from the top. The first rule that matches the packet decides the action. The rest are ignored."],
                   ["Implicit deny", "If no rule matches, the packet is denied. Security teams add an explicit deny-all rule at the end so that this is visible in the logs."]],
            note="Specific rules must come before general ones. A broad permit placed too high can hide a deny placed below it."),
        IMG("al-ic7-firewall-dmz.svg", alt="A firewall with three zones: the internet on the left, a DMZ with a web server and DNS server at the top right, and the internal LAN with admin and lab networks at the bottom right",
            caption="Figure 1. One firewall with three zones. The public web server sits in the DMZ, not in the internal LAN."),
        EX("Worked example 1: tracing packets through a school firewall", intro=(
            "The firewall between the zones has these rules, from the top. Lab = 10.0.20.0/24, Admin = 10.0.10.0/24, web server in the DMZ = 10.0.30.10, DNS server in the DMZ = 10.0.30.53. Trace the six packets listed after the rules."),
           steps=[
               S("Read the rules", text="Rule 1: deny any from Lab to Admin. Rule 2: permit TCP from Lab to any on port 80. Rule 3: permit TCP from Lab to any on port 443. Rule 4: permit UDP from Lab to 10.0.30.53 on port 53. Rule 5: permit TCP from any to 10.0.30.10 on port 443. Rule 6: deny any from any to any."),
               S("Packet 1: lab PC 10.0.20.15 to an internet site, TCP 443", text="Rule 1 no (destination is not Admin), rule 2 no (port 443), rule 3 yes. PERMIT."),
               S("Packet 2: lab PC to the fee server 10.0.10.7, TCP 80", text="Rule 1 matches (Lab to Admin). DENY. Rule 2 would have allowed it, but rule 1 is first."),
               S("Packet 3: lab PC to 10.0.30.53, UDP 53", text="Rules 1 to 3 do not match; rule 4 matches. PERMIT."),
               S("Packet 4: internet host 41.202.1.9 to 10.0.30.10, TCP 443", text="Rules 1 to 4 do not match; rule 5 matches. PERMIT. The public can read the school website."),
               S("Packet 5: internet host to lab PC 10.0.20.15, TCP 3389", text="No rule from 1 to 5 matches; rule 6 matches. DENY."),
               S("Packet 6: internet host to the web server, TCP 22", text="Rule 5 needs port 443, not 22. Rule 6 matches. DENY. Only the web service is exposed."),
           ]),
        CODE("""
Pkt  From          To            Proto  Port   Rule matched   Action
1    10.0.20.15    93.184.216.34 TCP    443    3              PERMIT
2    10.0.20.15    10.0.10.7     TCP    80     1              DENY
3    10.0.20.15    10.0.30.53    UDP    53     4              PERMIT
4    41.202.1.9    10.0.30.10    TCP    443    5              PERMIT
5    41.202.1.9    10.0.20.15    TCP    3389   6              DENY
6    41.202.1.9    10.0.30.10    TCP    22     6              DENY
""", "text", title="Listing 2: the trace table"),
        H("Types of firewall"),
        KEY("Three generations", "Each looks deeper into the traffic.",
            cards=[["Packet filter (stateless)", "Judges every packet alone using addresses, protocol and ports. Fast, but has no memory, so replies need their own rules."],
                   ["Stateful inspection", "Keeps a table of connections. A packet that is part of a connection started from inside is allowed back in automatically; unsolicited packets are dropped."],
                   ["Application firewall / proxy", "Understands protocols such as HTTP. Can block a harmful web request or a banned site by looking at the content. Slower but more precise."]]),
        EX("Worked example 2: stateful inspection", intro=(
            "A lab PC 10.0.20.15 opens a web page on server 93.184.216.34 port 443. The server's answer comes back from port 443 to the PC. Why is a rule for the reply not needed in a stateful firewall?"),
           steps=[
               S("Outgoing packet", text="The PC sends a connection request. Rule 3 permits it, and the firewall records the connection in its state table: source 10.0.20.15, destination 93.184.216.34:443."),
               S("Reply arrives", text="The reply matches the entry in the state table (same addresses and ports, reversed), so it is allowed without checking the rule list."),
               S("Unsolicited packet", text="Another packet from 93.184.216.34 aimed at port 3389 on the PC does not match a recorded connection, so it is dropped."),
               S("Stateless comparison", text="A stateless filter would need a rule to permit all traffic from port 443 to the lab, which attackers could abuse by faking their source port."),
           ]),
        H("The DMZ"),
        D("A **DMZ (demilitarised zone)** is a separate network segment for servers that must be reachable from the internet, such as web, mail and DNS servers. The firewall allows the internet to reach the DMZ only on the needed ports and allows the DMZ almost nothing towards the internal LAN.",
          title="DMZ",
          note="If the web server is hacked, the attacker is still outside the internal network and must pass the firewall again to reach it."),
        MISTAKE("Putting a broad permit above a specific deny", "In the trace, if rule 2 were above rule 1, the lab could reach the fee server on port 80. The order of the rules is part of the security."),
        MISTAKE("Forgetting the implicit deny", "A packet that matches nothing is dropped. If a service stops working after a rule change, check that a permit rule exists for it."),
        MISTAKE("Thinking a firewall stops all attacks", "A firewall cannot stop an attack carried inside traffic it allows, for example a phishing email on port 25 or malware in an allowed web download. It is one layer of defence in depth."),
        QUIZ("A firewall has rule 1: permit TCP any to any port 80, and rule 2: deny TCP from 10.0.20.0/24 to any port 80. A lab PC in 10.0.20.0/24 browses a site on port 80. What happens?",
             ["It is denied by rule 2", "It is permitted by rule 1", "It is denied by the implicit deny", "It is logged and then permitted by rule 2"], 1,
             "Rule 1 is first and matches every TCP port 80 packet, so the lab PC is permitted. Rule 2 is never reached.",
             hint="Which rule is tested first, and does it match?",
             feedback=["Rule 2 is never reached because rule 1 already matched.", "",
                       "Implicit deny applies only if no rule matches.", "Matching is first-match; the second rule is not combined with the first."]),
        H("Practice questions"),
        PQ("State the two rules that decide the outcome when a packet is tested against an ordered firewall rule list.",
           "The first matching rule, reading from the top, decides the action. If no rule matches, the packet is denied by the implicit deny."),
        PQ("Write firewall rules (in order) that let the Admin network 10.0.10.0/24 browse the web (ports 80 and 443) but block everything else.",
           "Rule 1: permit TCP from 10.0.10.0/24 to any port 80. Rule 2: permit TCP from 10.0.10.0/24 to any port 443. Rule 3: deny any from any to any. (DNS from Admin would also need a permit rule if the DNS server is outside the Admin network.)"),
        PQ("Explain the difference between a stateless packet filter and a stateful firewall, using returning web traffic as the example.",
           "A stateless filter judges each packet on its own, so replies to a web request need an explicit rule. A stateful firewall remembers the outgoing connection in a state table and automatically allows the matching reply, while dropping unsolicited packets."),
        PQ("Explain why a school should put its public website server in a DMZ and not in the same network as the fee records.",
           "The website must accept connections from the internet and is more likely to be attacked. In a DMZ, if it is compromised the attacker is still separated from the internal network by the firewall, which blocks traffic from the DMZ to the fee records. In the same network the attacker could reach the fee records directly."),
        H("Summary"),
        SUM("A firewall permits or denies packets using rules: protocol, source, destination, port, action.",
            "The first matching rule wins; no match means deny. Put specific rules first.",
            "Stateless filters judge packets alone; stateful firewalls track connections; application firewalls inspect content.",
            "A DMZ holds public servers so that a compromise does not give direct access to the internal LAN."),
    ],
))

# ---------------------------------------------------------------------------
# Defence and recovery 2: IDS and IPS
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Defence and recovery",
    title="Intrusion detection and prevention: IDS, IPS and alert quality",
    slug="ic7-ids-ips-detection-methods-and-alerts",
    minutes=24,
    summary="Compare IDS and IPS, network-based and host-based systems, and signature and anomaly detection, then calculate detection rate, false positives and the share of alerts that are real.",
    objectives=[
        "Distinguish an intrusion detection system from an intrusion prevention system",
        "Compare signature-based and anomaly-based detection",
        "Distinguish network-based and host-based sensors",
        "Calculate detection rate and alert precision and explain false positives and false negatives",
    ],
    key_concepts=["IDS", "IPS", "NIDS", "HIDS", "Signature", "Anomaly", "Baseline", "False positive", "False negative"],
    blocks=[
        H("Introduction"),
        T("A firewall decides at the door. But what if an attacker uses an allowed door, for example a normal web request that contains a hidden SQL command? Or a "
          "laptop inside the network starts sending thousands of messages at midnight? Security teams add systems that watch the traffic and the machines "
          "for signs of attack. An **intrusion detection system (IDS)** raises an alarm. An **intrusion prevention system (IPS)** raises an alarm and also acts."),
        KEY("IDS and IPS", "Same detection, different reaction.",
            cards=[["IDS", "Sits beside the traffic (it receives a copy, for example from a mirror port) and only alerts staff. If it fails, traffic is not affected."],
                   ["IPS", "Sits in line, so traffic passes through it. It can drop packets, block an address or reset a connection automatically. If it fails or makes a mistake, it can block real users."]]),
        H("Where the sensor sits"),
        D("A **network-based IDS (NIDS)** watches traffic on a network segment and can see attacks against many machines. A **host-based IDS (HIDS)** runs on one computer and watches its logs, system files and processes, so it can see what happens after encrypted traffic is decrypted.",
          title="NIDS and HIDS"),
        H("How attacks are recognised"),
        KEY("Two detection methods", "Most products use both.",
            cards=[["Signature-based", "Compares traffic or files with a database of known attack patterns. Accurate for known attacks, few false alarms, but blind to new attacks and needs frequent updates."],
                   ["Anomaly-based", "Learns what is normal (a baseline) and alerts on large deviations. Can find new attacks but produces more false alarms and needs time to learn."]]),
        CODE("""
Signature rule (idea, not a product's syntax):
IF the web request to 10.0.30.10 port 80 contains the text  ' OR '1'='1
THEN raise alert "possible SQL injection" and (IPS only) drop the packet

Anomaly rule (idea):
Baseline  : failed logins per hour on the portal, mean 20, standard deviation 5
Threshold : mean + 3 x standard deviation = 20 + 15 = 35
IF failed logins in the last hour > 35 THEN raise alert "possible brute force"
""", "text", title="Listing 1: a signature rule and an anomaly rule"),
        EX("Worked example 1: applying the anomaly rule", intro=("Using the baseline in Listing 1, decide which hours cause an alert: 22, 31, 38, 52 failed logins."),
           steps=[
               S("Threshold", text="mean + 3 x standard deviation = 20 + 3 x 5 = 35.", math=r"20 + 3\times 5 = 35"),
               S("Compare", text="22 and 31 are not above 35. 38 and 52 are above 35."),
               S("Result", text="Alerts for 38 and 52. An analyst should check the source addresses; 38 might be a class forgetting passwords after a holiday, 52 more likely an attack."),
           ]),
        H("Measuring alert quality"),
        D("A **false positive** is an alert for harmless activity. A **false negative** is a real attack that raised no alert. A **true positive** is a correct alert; a **true negative** is correct silence.",
          title="Outcomes"),
        F(r"\text{Detection rate} = \frac{TP}{TP+FN} \qquad \text{Precision} = \frac{TP}{TP+FP}", title="Two useful measures"),
        EX("Worked example 2: why most alerts can be false", intro=(
            "In one week a university network has 10 000 events. 100 are real attacks. The IDS detects 90 of them and also raises a false alarm on 1 percent of the 9900 harmless events. Calculate the figures."),
           steps=[
               S("True positives and false negatives", text="TP = 90 and FN = 100 - 90 = 10."),
               S("False positives", text="1 percent of 9900 = 99 false alarms."),
               S("Detection rate", text="90 / (90 + 10) = 0.90, so 90 percent of attacks are detected.", math=r"\frac{90}{90+10} = 0.90"),
               S("Total alerts and precision", text="Alerts = 90 + 99 = 189. Precision = 90 / 189 = 0.476, so only about 48 percent of alerts are real.", math=r"\frac{90}{189} \approx 0.476"),
               S("Meaning", text="The analysts see 189 alerts and more than half are false, even though the IDS looks accurate. This is why tuning rules and ranking alerts matter. An IPS with these figures would block 99 harmless connections."),
           ]),
        TIP("In an exam, say which mistake is more serious in the context. For an IDS, missing an attack (false negative) is usually worse. For an IPS that blocks automatically, false positives are costly because real users are cut off."),
        QUIZ("A new attack uses a pattern that is in no database. Which method is more likely to detect it?",
             ["Signature-based detection", "Anomaly-based detection", "Neither can detect new attacks", "A router access list"], 1,
             "Anomaly detection looks for unusual behaviour, so it can catch unknown attacks, at the cost of more false alarms. Signature detection recognises only known patterns.",
             hint="Which method needs a database of known attacks?",
             feedback=["A signature must already exist for the attack.", "",
                       "Anomaly detection was designed for this case.", "An access list matches fixed addresses and ports and does not judge behaviour."]),
        MISTAKE("Thinking an IDS blocks attacks", "An IDS only alerts. An IPS in line can block. Check which word the question uses."),
        MISTAKE("Equating a high detection rate with good quality", "A system can detect 99 percent of attacks and still produce so many false alarms that staff ignore it. Quote precision as well."),
        MISTAKE("Installing an IPS without testing", "An IPS with a bad rule can block a bank's own customers. Run it in detection-only mode first, tune it, then switch to blocking."),
        H("Practice questions"),
        PQ("State two differences between an IDS and an IPS.",
           "An IDS monitors a copy of the traffic and only raises alerts; an IPS sits in line and can block traffic automatically. An IDS failure does not stop traffic; an IPS failure or false alarm can interrupt normal traffic."),
        PQ("Give one advantage and one disadvantage of signature-based detection.",
           "Advantage: accurate with few false positives for known attacks. Disadvantage: it cannot detect new attacks that are not in the signature database, and it needs regular updates."),
        PQ("A bank's IPS saw 5000 events. 50 were real attacks, 40 were detected, and 60 harmless events were wrongly flagged. Calculate the detection rate and the precision.",
           "Detection rate = 40 / 50 = 0.80, which is 80 percent. Alerts = 40 + 60 = 100, so precision = 40 / 100 = 0.40, which is 40 percent."),
        PQ("Why is a host-based IDS useful in addition to a network-based IDS on a server that uses encrypted connections?",
           "A network sensor cannot read encrypted traffic. A host-based IDS runs on the server and sees the decrypted requests, the logs and changes to important files, so it can detect attacks that the network sensor cannot see."),
        H("Summary"),
        SUM("IDS detects and alerts; IPS sits in line and can also block.",
            "NIDS watches a network segment; HIDS watches one host.",
            "Signature detection finds known attacks; anomaly detection compares with a baseline and can find new ones with more false alarms.",
            "Detection rate = TP / (TP + FN); precision = TP / (TP + FP). Tune rules to reduce false positives."),
    ],
))

# ---------------------------------------------------------------------------
# Defence and recovery 3: backups and disaster recovery
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=CS, topic="Defence and recovery",
    title="Disaster recovery planning: backups, RPO, RTO and availability",
    slug="ic7-disaster-recovery-backups-rpo-rto",
    minutes=25,
    summary="Plan recovery from a disaster: run a business impact analysis, set RPO and RTO, compare full, incremental and differential backups, choose a recovery site, and convert availability percentages to downtime.",
    objectives=[
        "Define disaster recovery, RPO and RTO and apply them to a scenario",
        "Compare full, incremental and differential backups and work out restore sets and storage",
        "Describe the 3-2-1 backup rule and hot, warm and cold recovery sites",
        "Convert an availability percentage into hours of downtime per year",
    ],
    key_concepts=["Disaster recovery plan", "Business impact analysis", "RPO", "RTO", "Full backup", "Incremental backup", "Differential backup", "3-2-1 rule", "Hot site", "Availability"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian towns a fire in a market, a flood in the rainy season or a long power cut can stop a business for days. "
          "Suppose a pharmacy's only computer holds its stock and customer records on one hard disk in the shop. If that disk fails on a Friday, "
          "what happens on Monday? A **disaster recovery plan (DRP)** is a written plan, prepared and tested in advance, that says how to restore IT systems and data after a serious incident."),
        H("Business impact analysis, RPO and RTO"),
        D("A **business impact analysis (BIA)** lists the business functions, the systems they need, and the cost of losing them for an hour, a day, a week. It ranks systems so that the most important are recovered first.",
          title="Business impact analysis"),
        KEY("Two numbers every plan needs", "They come from the BIA and decide the cost of the solution.",
            cards=[["RPO: recovery point objective", "The most data the business can afford to lose, measured in time. RPO of 4 hours means backups must be at most 4 hours apart."],
                   ["RTO: recovery time objective", "The longest time the system may be down before the damage is unacceptable. RTO of 4 hours means the system must be working again within 4 hours of the failure."]]),
        EX("Worked example 1: testing a plan against RPO and RTO", intro=(
            "A supermarket in Douala backs up its sales database every night at 22:00. A disk fails at 15:00 the next day. Restoring takes 6 hours to buy and install a disk and 2 hours to copy the data. The manager set RPO = 4 hours and RTO = 4 hours. Does the plan meet them?"),
           steps=[
               S("Data lost", text="The last backup was at 22:00 the day before, so data from 22:00 to 15:00 is lost: 17 hours."),
               S("Compare with the RPO", text="17 hours is more than the RPO of 4 hours. RPO is NOT met."),
               S("Recovery time", text="6 hours + 2 hours = 8 hours of downtime."),
               S("Compare with the RTO", text="8 hours is more than the RTO of 4 hours. RTO is NOT met."),
               S("Improvements", text="To meet an RPO of 4 hours the backups must run at least every 4 hours (or the data must be copied to a second disk continuously). To meet an RTO of 4 hours keep a spare disk or computer on site and test the restore so that it takes less than 4 hours."),
           ]),
        H("Types of backup"),
        KEY("Full, incremental and differential", "They differ in what is copied and what is needed to restore.",
            cards=[["Full", "Copies everything. Largest and slowest, but one set restores everything."],
                   ["Incremental", "Copies only what changed since the LAST backup of any kind. Smallest and fastest, but a restore needs the last full backup and every incremental after it."],
                   ["Differential", "Copies everything changed since the last FULL backup. Grows each day, but a restore needs only the last full backup and the latest differential."]]),
        EX("Worked example 2: a week of backups", intro=(
            "A server holds 100 GB. A full backup is made on Sunday. Every day from Monday to Saturday 5 GB of new or changed data appears (different data each day). Compare incremental and differential schemes: how much is stored by the end of Saturday, and what is needed to restore on Thursday evening?"),
           steps=[
               S("Incremental storage", text="Each day copies 5 GB. Total = 100 + 6 x 5 = 130 GB.", math=r"100 + 6\times 5 = 130"),
               S("Differential storage", text="Monday 5, Tuesday 10, Wednesday 15, Thursday 20, Friday 25, Saturday 30. Sum = 105, so total = 100 + 105 = 205 GB.", math=r"100 + (5+10+15+20+25+30) = 205"),
               S("Restore on Thursday, incremental", text="Full (Sunday) + Monday + Tuesday + Wednesday + Thursday increments: 5 backup sets, 100 + 4 x 5 = 120 GB."),
               S("Restore on Thursday, differential", text="Full (Sunday) + Thursday differential: 2 sets, 100 + 20 = 120 GB."),
               S("Compare", text="Incremental uses less storage (130 against 205 GB) but needs more sets, and one damaged set breaks the chain. Differential uses more storage and is faster and safer to restore."),
           ]),
        T("The **3-2-1 rule**: keep at least **3** copies of important data, on **2** different kinds of media, with **1** copy off-site "
          "(another building or town). A fire that destroys the office also destroys a backup stored next to the computer."),
        H("Recovery sites and availability"),
        KEY("Alternative sites", "Cost rises as recovery time falls.",
            cards=[["Hot site", "Fully equipped and running, with data copied continuously. Recovery in minutes. Most expensive."],
                   ["Warm site", "Has hardware and connectivity, but data must be restored from backups. Recovery in hours to a day."],
                   ["Cold site", "Only space, power and a network connection. Equipment is brought in after the disaster. Recovery in days. Cheapest."]]),
        D("**Availability** is the percentage of time a system is working. Downtime per year = (100 minus availability) percent of the hours in a year (8760).",
          title="Availability", formula=r"\text{Downtime} = (1 - A)\times 8760\ \text{hours per year}"),
        CODE("""
Availability   Downtime per year
99%            87.6 hours   (about 3.65 days)
99.9%          8.76 hours
99.99%         52.6 minutes
""", "text", title="Listing 1: what the nines mean",
             caption="Each extra nine cuts the downtime by ten, but costs much more."),
        QUIZ("A hospital can afford to lose at most 15 minutes of patient data. What does this define?",
             ["RTO = 15 minutes", "RPO = 15 minutes", "Availability = 15 percent", "A cold site"], 1,
             "The maximum acceptable data loss, measured in time, is the RPO.",
             hint="Is the figure about lost data or about time to restore service?",
             feedback=["RTO is how long the system may be down, not how much data may be lost.", "",
                       "Availability is a percentage of time the system is working.",
                       "A cold site is a type of recovery location."]),
        MISTAKE("Never testing the restore", "A backup that cannot be restored is worthless. Test restores regularly and time them against the RTO."),
        MISTAKE("Keeping the only backup next to the computer", "Fire, flood and theft take both. Follow the 3-2-1 rule with one copy off-site."),
        MISTAKE("Confusing RPO and RTO", "RPO is about DATA lost (time since the last good copy). RTO is about SERVICE downtime (time to be working again)."),
        H("Practice questions"),
        PQ("Define RPO and RTO.",
           "RPO (recovery point objective) is the maximum amount of data, measured as time, that the organisation can accept losing. RTO (recovery time objective) is the maximum time the system may be unavailable after a failure."),
        PQ("A school makes a full backup on Sunday and a differential backup each evening. The server fails on Wednesday morning. Which backups are needed for the restore?",
           "The Sunday full backup and the Tuesday evening differential (the latest differential before the failure). Monday's differential is not needed because Tuesday's contains all changes since Sunday."),
        PQ("Explain the 3-2-1 backup rule and why the off-site copy matters.",
           "Keep 3 copies of the data, on 2 different types of media, with 1 copy stored off-site. The off-site copy survives a local disaster such as a fire, flood or theft that destroys the computer and any backup in the same place."),
        PQ("A web shop promises 99.9 percent availability. Calculate the maximum downtime per year, and compare it with 99 percent.",
           "99.9 percent leaves 0.1 percent of 8760 hours, which is 8.76 hours of downtime. 99 percent leaves 1 percent, which is 87.6 hours. The higher target allows ten times less downtime."),
        H("Summary"),
        SUM("A disaster recovery plan is written, tested and based on a business impact analysis.",
            "RPO is the maximum data loss in time; RTO is the maximum downtime.",
            "Full copies everything; incremental copies changes since the last backup; differential copies changes since the last full backup.",
            "3-2-1 rule; hot, warm and cold sites trade cost against recovery time.",
            "Downtime per year = (1 minus availability) x 8760 hours."),
    ],
))

# ---------------------------------------------------------------------------
# Advanced Excel 1: XLOOKUP and INDEX/MATCH
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=PP, topic="Advanced Excel",
    title="Lookups: XLOOKUP and INDEX/MATCH",
    slug="ic7-xlookup-and-index-match",
    minutes=25,
    summary="Retrieve data from a table with XLOOKUP and INDEX/MATCH: exact and approximate matches, left lookups, two-way lookups, not-found messages, and the errors to avoid.",
    objectives=[
        "Write XLOOKUP formulas with the arguments in the right order, including not-found and match-mode options",
        "Write INDEX/MATCH formulas for one-way, left and two-way lookups",
        "Use an approximate match to convert scores to grades",
        "Explain why XLOOKUP and INDEX/MATCH are preferred to VLOOKUP",
    ],
    key_concepts=["XLOOKUP", "INDEX", "MATCH", "Exact match", "Approximate match", "Absolute reference", "#N/A", "Spill"],
    blocks=[
        H("Introduction"),
        T("A shopkeeper in Mokolo keeps her prices on one sheet and writes each customer's order on another sheet using only the product code. "
          "She wants the item name, the price and the total to appear by themselves. This job, finding a value in a table from a key, is the "
          "most common task in a spreadsheet. Excel has older functions (VLOOKUP, HLOOKUP) and newer, more flexible ones: "
          "**XLOOKUP** and the pair **INDEX** and **MATCH**."),
        T("All the examples in this lesson use the table below. The formulas appear in code blocks so that you can see the exact symbols, "
          "including dollar signs for absolute references."),
        CODE("""
Sheet: Prices                         Sheet: Orders (columns F to J, same sheet)
     A      B             C           D          F      G    H      I       J
1    Code   Item          Category    Price      Code   Qty  Item   Price   Total
2    P101   Rice          Staples     800        P103   4
3    P102   Oil           Oils        1200       P101   10
4    P103   Sugar         Staples     900        P107   2
5    P104   Salt          Condiments  250        P104   6
6    P105   Tomato paste  Condiments  600
7    P106   Spaghetti     Staples     500
""", "text", title="Listing 1: the data"),
        H("XLOOKUP"),
        D("**XLOOKUP** searches one range for a value and returns the matching item from another range. Only the first three arguments are required.",
          title="XLOOKUP syntax"),
        CODE("""
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])

match_mode :  0 exact match (the default)
             -1 exact, or the next smaller item
              1 exact, or the next larger item
              2 wildcard match (* and ?)
search_mode:  1 first to last (the default)   -1 last to first
""", "text", title="Listing 2: arguments of XLOOKUP",
             caption="Square brackets mark optional arguments. XLOOKUP is available in Microsoft 365 and Excel 2021 and later."),
        EX("Worked example 1: filling the order sheet", intro=("Write formulas for H2 (item), I2 (price) and J2 (total) for the first order, copy them down, and give the results for all four rows."),
           steps=[
               S("Item name in H2", text="Look for the code in F2 inside the Code column and return the item from the Item column. If the code is not found, show a message."),
               S("Price in I2", text="Same lookup, returning the Price column. If not found, use 0 so that the total still works."),
               S("Total in J2", text="Quantity multiplied by price."),
               S("Copy down", text="The dollar signs fix the table ranges, so when the formula is copied to rows 3 to 5 only F2 changes to F3, F4, F5."),
               S("Results", text="Row 2: Sugar, 900, 3600. Row 3: Rice, 800, 8000. Row 4: code P107 is not in the table, so Unknown code, 0, 0. Row 5: Salt, 250, 1500. The sum of the totals is 13 100."),
           ]),
        CODE("""
H2:  =XLOOKUP(F2,$A$2:$A$7,$B$2:$B$7,"Unknown code")
I2:  =XLOOKUP(F2,$A$2:$A$7,$D$2:$D$7,0)
J2:  =G2*I2
J6:  =SUM(J2:J5)          result 13100
""", "text", title="Listing 3: the formulas"),
        T("XLOOKUP can also return several columns at once. =XLOOKUP(\"P104\",A2:A7,B2:D7) returns Salt, Condiments and 250 in three neighbouring cells (the "
          "result **spills** into the cells to the right). With search mode -1 it finds the last match: asking for the last item of category Staples "
          "(Staples are Rice, Sugar and Spaghetti) returns Spaghetti. A wildcard search with match mode 2, with a pattern that ends in a star after Ric (see Listing 4), returns the price of Rice, 800."),
        CODE("""
=XLOOKUP("P104",A2:A7,B2:D7)                  returns Salt | Condiments | 250
=XLOOKUP("Staples",C2:C7,B2:B7,,0,-1)         returns Spaghetti  (last match)
=XLOOKUP("Ric*",B2:B7,D2:D7,"none",2)         returns 800        (wildcard)
""", "text", title="Listing 4: more XLOOKUP forms"),
        H("INDEX and MATCH"),
        D("**MATCH(value, range, type)** returns the position of the value in the range (1 for the first cell). **INDEX(range, row, column)** returns the item at that position. Together they do the work of a lookup, and they work in every version of Excel.",
          title="INDEX and MATCH",
          note="Use match type 0 for an exact match. Type 1 (the default if omitted!) finds the largest value less than or equal to the lookup value and needs the range sorted ascending."),
        EX("Worked example 2: a left lookup and a two-way lookup", intro=(
            "(a) Find the code of Sugar. (b) Using the quarterly sales table in Listing 5, find Bamenda's sales in Q3, and the quarter in which Douala sold the most."),
           steps=[
               S("(a) Left lookup", text="MATCH(\"Sugar\",B2:B7,0) gives 3 because Sugar is the third item. INDEX(A2:A7,3) returns the code in the third row, P103. VLOOKUP cannot do this, because it only returns values to the right of the lookup column."),
               S("(b) Row position", text="MATCH(\"Bamenda\",A2:A5,0) = 3."),
               S("(b) Column position", text="MATCH(\"Q3\",B1:E1,0) = 3."),
               S("(b) Combine", text="INDEX(B2:E5,3,3) returns the value in the third row and third column of the data block: 80."),
               S("(b) Best quarter for Douala", text="MAX(B2:E2) = 170. MATCH(170,B2:E2,0) = 4. INDEX(B1:E1,4) returns Q4."),
           ]),
        CODE("""
        A         B     C     D     E        (sales in thousand FCFA)
1       Town      Q1    Q2    Q3    Q4
2       Douala    120   135   150   170
3       Yaounde   100   110   105   125
4       Bamenda   60    65    80    70
5       Garoua    45    50    40    55
""", "text", title="Listing 5: quarterly sales"),
        CODE("""
Code of Sugar:        =INDEX($A$2:$A$7,MATCH("Sugar",$B$2:$B$7,0))              P103
Bamenda in Q3:        =INDEX(B2:E5,MATCH("Bamenda",A2:A5,0),MATCH("Q3",B1:E1,0)) 80
Best quarter, Douala: =INDEX(B1:E1,MATCH(MAX(B2:E2),B2:E2,0))                    Q4
""", "text", title="Listing 6: INDEX/MATCH formulas"),
        H("Approximate match: scores to grades"),
        T("A grade table lists the lowest score for each grade, sorted ascending: 0 is F, 40 is D, 50 is C, 60 is B, 70 is A. A score is given the grade of "
          "the largest threshold that does not exceed it. This is an **approximate match**: the score 65 is not in the table, but it falls between 60 and 70, so it earns B."),
        EX("Worked example 3: grading", intro=("The thresholds are in F2:F6 (0, 40, 50, 60, 70) and the grades in G2:G6 (F, D, C, B, A). Write a formula for a score in B2 and give the grade for 35, 40, 59, 65 and 82."),
           steps=[
               S("XLOOKUP version", text="Match mode -1 means exact match or the next smaller value. This works even if the table is not sorted."),
               S("INDEX/MATCH version", text="MATCH with type 1 finds the position of the largest threshold not above the score. The thresholds must be sorted ascending."),
               S("Results", text="35 gives F. 40 gives D (exact). 59 gives C. 65 gives B. 82 gives A."),
           ]),
        CODE("""
=XLOOKUP(B2,$F$2:$F$6,$G$2:$G$6,,-1)
=INDEX($G$2:$G$6,MATCH(B2,$F$2:$F$6,1))
""", "text", title="Listing 7: two ways to grade"),
        MISTAKE("Forgetting the dollar signs", "If the table range is written as A2:A7 and the formula is copied down, the range slides to A3:A8 and rows are missed. Use $A$2:$A$7 for ranges that must not move."),
        MISTAKE("Leaving out the 0 in MATCH", "MATCH(value, range) without a third argument does an approximate match and can return a wrong position with no error message if the range is not sorted. Always type ,0 for an exact lookup."),
        MISTAKE("Using ranges of different size", "In XLOOKUP the lookup array and return array must have the same number of rows (or columns). Otherwise Excel returns #VALUE!."),
        TIP("The error #N/A means the value was not found. Do not hide it with a blank. Give a clear message, as in the Unknown code example, so users notice wrong codes."),
        QUIZ("In =XLOOKUP(\"P104\",A2:A7,D2:D7), what is returned for the table in Listing 1?",
             ["Salt", "250", "P104", "600"], 1,
             "P104 is in row 5 of the table. The return array is the Price column D, so the result is 250.",
             hint="Which column is the return array?",
             feedback=["Salt is in column B, which is not the return array.", "",
                       "The lookup value is returned only if it is also the return array.", "600 is the price of P105, the next row."]),
        H("Practice questions"),
        PQ("List the first three arguments of XLOOKUP and say what each is.",
           "lookup_value: the value to find. lookup_array: the range to search. return_array: the range from which the matching item is returned."),
        PQ("Write a formula that returns the price of Tomato paste from the table in Listing 1, and a message \"not stocked\" if the item is missing.",
           "=XLOOKUP(\"Tomato paste\",B2:B7,D2:D7,\"not stocked\"). It returns 600. The equivalent with INDEX/MATCH is =IFERROR(INDEX(D2:D7,MATCH(\"Tomato paste\",B2:B7,0)),\"not stocked\")."),
        PQ("Using Listing 5, write one formula that returns Yaounde's Q2 sales and say what it returns.",
           "=INDEX(B2:E5,MATCH(\"Yaounde\",A2:A5,0),MATCH(\"Q2\",B1:E1,0)). MATCH gives row 2 and column 2 of the data block, so it returns 110."),
        PQ("Give two advantages of XLOOKUP over VLOOKUP.",
           "It looks in any direction, including to the left of the lookup column; it uses exact match by default; it has a built-in not-found argument; it uses a return range, so inserting a column does not break it as a column number can."),
        H("Summary"),
        SUM("XLOOKUP(value, lookup range, return range, not found, match mode, search mode): exact by default, can look left, can return several columns.",
            "INDEX(range, row, column) with MATCH(value, range, 0) works in every version and gives left and two-way lookups.",
            "Approximate matches need thresholds: XLOOKUP with mode -1, or MATCH with type 1 on sorted data.",
            "Lock ranges with absolute references and give not-found messages instead of hiding errors."),
    ],
))

# ---------------------------------------------------------------------------
# Advanced Excel 2: pivot tables
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=PP, topic="Advanced Excel",
    title="Pivot tables: summarising data by town, product and month",
    slug="ic7-pivot-tables-summarising-data",
    minutes=24,
    summary="Prepare a table, build a pivot table with rows, columns, values and filters, change the summary function, show percentages, and explain why a pivot must be refreshed.",
    objectives=[
        "Prepare a source table that a pivot table can use",
        "Place fields in the Rows, Columns, Values and Filters areas to get a required summary",
        "Choose between Sum, Count and Average and show values as a percentage of the total",
        "Read a pivot table and explain when and why to refresh it",
    ],
    key_concepts=["Pivot table", "Field", "Rows area", "Columns area", "Values area", "Filter", "Sum", "Count", "Average", "Refresh", "Grand total"],
    blocks=[
        H("Introduction"),
        T("The owner of three grocery shops in Douala, Yaounde and Bamenda has a list of sales with hundreds of lines. She wants to know: how much "
          "did each town sell, which category sells best, and how did February compare with January? Writing a formula for every question "
          "is slow. A **pivot table** answers these questions in a few clicks by grouping and summarising the rows of a table."),
        D("A **pivot table** is an interactive summary of a table of data. You drag fields into four areas: **Rows**, **Columns**, **Values** and **Filters**. Excel groups the data by the fields in Rows and Columns and calculates the field in Values for each group.",
          title="Pivot table"),
        KEY("The four areas", "Think of a report with a title, row labels, column labels and a body.",
            cards=[["Rows", "Each different value of the field becomes a row (for example each town)."],
                   ["Columns", "Each different value becomes a column (for example each category)."],
                   ["Values", "The number that is calculated in each cell: sum, count, average, maximum..."],
                   ["Filters", "A field that limits the whole report to some values (for example only January)."]]),
        H("Preparing the data"),
        T("Pivot tables need a clean table. Rules: one header row with a unique name for each column; no blank rows or blank columns inside; "
          "no merged cells; no total rows inside the data; one value per cell (do not put the month and the town in the same cell). "
          "Converting the range to an Excel Table (Insert, Table) lets the pivot table grow with new rows."),
        CODE("""
     Town      Category    Month  Amount (thousand FCFA)
1    Douala    Staples     Jan    120
2    Douala    Oils        Jan    80
3    Douala    Staples     Feb    140
4    Yaounde   Staples     Jan    100
5    Yaounde   Condiments  Feb    40
6    Bamenda   Oils        Jan    60
7    Bamenda   Staples     Feb    90
8    Bamenda   Condiments  Jan    30
9    Douala    Condiments  Feb    50
10   Yaounde   Oils        Feb    70
11   Yaounde   Staples     Feb    110
12   Bamenda   Oils        Feb    55
""", "text", title="Listing 1: the source data (12 sales lines)"),
        EX("Worked example 1: total sales by town and category", intro=(
            "Create a pivot table with Town in Rows, Category in Columns and Sum of Amount in Values. Give the result."),
           steps=[
               S("Insert the pivot table", text="Click inside the data, choose Insert, PivotTable, and accept the range and a new sheet."),
               S("Drag the fields", text="Town to Rows. Category to Columns. Amount to Values (Excel proposes Sum for numbers)."),
               S("Bamenda row", text="Condiments 30, Oils 60 + 55 = 115, Staples 90. Row total 235."),
               S("Douala row", text="Condiments 50, Oils 80, Staples 120 + 140 = 260. Row total 390."),
               S("Yaounde row", text="Condiments 40, Oils 70, Staples 100 + 110 = 210. Row total 320."),
               S("Column and grand totals", text="Condiments 120, Oils 265, Staples 560. Grand total 945 thousand FCFA, which is the sum of all twelve lines."),
           ]),
        CODE("""
Sum of Amount   Condiments   Oils   Staples   Grand Total
Bamenda         30           115    90        235
Douala          50           80     260       390
Yaounde         40           70     210       320
Grand Total     120          265    560       945
""", "text", title="Listing 2: the pivot table"),
        H("Changing what is calculated"),
        EX("Worked example 2: filter, count, average and percentage", intro=(
            "Using the same data, answer: (a) sales in February only, (b) how many sales lines Douala has, (c) Douala's average line, (d) each town's share of the grand total."),
           steps=[
               S("(a) Filter", text="Drag Month to Filters and choose Feb. Rows with Feb: lines 3, 5, 7, 9, 10, 11, 12 give 140 + 40 + 90 + 50 + 70 + 110 + 55 = 555. (January gives 390; 390 + 555 = 945.)"),
               S("(b) Count", text="Right-click the Values field, Summarize Values By, Count. Douala has 4 lines (rows 1, 2, 3 and 9)."),
               S("(c) Average", text="Summarize by Average. Douala: (120 + 80 + 140 + 50) / 4 = 390 / 4 = 97.5."),
               S("(d) Percentage of total", text="Show Values As, % of Grand Total. Bamenda 235 / 945 = 24.9 percent, Douala 390 / 945 = 41.3 percent, Yaounde 320 / 945 = 33.9 percent. They add to 100 percent."),
           ]),
        TIP("Drag Town to Rows and Category to Rows below it to get a two-level list. Use Month in Columns and Sum of Amount in Values to see a trend. The same data can answer many questions by moving fields."),
        H("Refresh, formulas and charts"),
        T("A pivot table is a copy of a summary taken from the source data. If you change a cell or add lines to the source, the pivot table does NOT update by itself. "
          "Right-click it and choose **Refresh**, or use Data, Refresh All. If new lines were added below an ordinary range, the pivot table's range must also be extended. An Excel Table does this automatically."),
        CODE("""
=GETPIVOTDATA("Amount",$A$3,"Town","Douala")        reads Douala's total from the pivot
""", "text", title="Listing 3: reading a value from a pivot table", caption="Cell A3 is the top-left cell of the pivot table. Clicking a pivot cell while typing = creates this formula automatically."),
        MISTAKE("Summarising a number stored as text", "If the Amount column holds text, the field is counted instead of summed and shows Count of Amount. Convert the column to numbers first."),
        MISTAKE("Expecting the pivot table to update on its own", "After the source changes, refresh the pivot table. Otherwise reports are out of date."),
        MISTAKE("Leaving a blank row in the data", "The pivot table may stop at the blank row and ignore the lines below it. Delete blank rows or use an Excel Table."),
        QUIZ("A pivot table shows Count of Amount for Douala = 4 and Sum of Amount for Douala = 390. What is the average sale line for Douala?",
             ["4", "390", "97.5", "1560"], 2,
             "Average = sum / count = 390 / 4 = 97.5.",
             hint="Average equals total divided by number of lines.",
             feedback=["4 is the number of lines, not the average.", "390 is the total.", "", "1560 comes from multiplying 390 by 4 instead of dividing."]),
        H("Practice questions"),
        PQ("Name the four areas of the PivotTable Fields pane and say what each does.",
           "Rows: fields whose values form row labels. Columns: fields whose values form column labels. Values: the number calculated for each group, such as a sum. Filters: a field used to limit the whole table to chosen values."),
        PQ("Using Listing 1, what does a pivot table with Category in Rows and Sum of Amount in Values give?",
           "Condiments 120 (30 + 40 + 50), Oils 265 (80 + 60 + 70 + 55), Staples 560 (120 + 140 + 100 + 90 + 110), grand total 945."),
        PQ("The shop adds three new lines at the bottom of the data. The pivot table does not show them. Give two possible reasons and the fix.",
           "The pivot table was not refreshed, or its source range does not include the new rows. Refresh it after extending the source range, or convert the data to an Excel Table so that the range grows automatically."),
        PQ("List three rules for preparing data for a pivot table.",
           "One header row with unique names; no blank rows or columns in the data; no merged cells; no total rows inside the data; one kind of value per column (numbers stored as numbers). Any three."),
        H("Summary"),
        SUM("A pivot table summarises a table by dragging fields to Rows, Columns, Values and Filters.",
            "The source must be clean: one header row, no blanks, no merged cells, numbers stored as numbers.",
            "Values can be Sum, Count or Average and can be shown as a percentage of the grand total.",
            "A pivot table is not live: refresh it after the data changes."),
    ],
))

# ---------------------------------------------------------------------------
# Advanced Excel 3: Solver
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=PP, topic="Advanced Excel",
    title="Solver: choosing the best product mix",
    slug="ic7-solver-optimisation-product-mix",
    minutes=24,
    summary="Model a business decision with changing cells, an objective and constraints, set up Excel Solver, read the answer, and explain binding constraints and what happens when the problem has no solution.",
    objectives=[
        "Identify the objective, the changing cells and the constraints in a decision problem",
        "Lay out a spreadsheet model with SUMPRODUCT formulas ready for Solver",
        "Fill in the Solver dialog and interpret the result",
        "Explain binding constraints, shadow prices and infeasible problems",
    ],
    key_concepts=["Solver", "Objective cell", "Changing cells", "Constraint", "Simplex LP", "Feasible solution", "Binding constraint", "SUMPRODUCT", "Shadow price"],
    blocks=[
        H("Introduction"),
        T("A bakery in Bafoussam makes bread loaves and cakes. Loaves earn little profit but are quick; cakes earn more but use more flour and more "
          "labour. Flour and labour are limited each day. How many of each should the baker make to earn the most profit? This is an "
          "**optimisation problem**. You could try numbers by hand, but Excel's **Solver** add-in finds the best answer for you."),
        D("An optimisation problem has three parts. The **objective** is the quantity to maximise or minimise (profit, cost). The **changing cells** (decision variables) are the values you can choose. The **constraints** are the limits the choices must respect.",
          title="Optimisation"),
        H("Step 1: write the problem"),
        CODE("""
Product     Profit per unit   Flour per unit   Labour per unit
Loaf        100 FCFA          0.5 kg           4 minutes
Cake        250 FCFA          1 kg             12 minutes

Available each day: 120 kg of flour, 1200 minutes of labour.
Maximise profit = 100 x loaves + 250 x cakes
Subject to   0.5 x loaves + 1 x cakes   <= 120   (flour)
             4 x loaves + 12 x cakes    <= 1200  (labour)
             loaves, cakes >= 0 and whole numbers
""", "text", title="Listing 1: the problem"),
        H("Step 2: build the model on the sheet"),
        CODE("""
     A                      B        C        D       E
1    Item                   Loaves   Cakes    Used    Limit
2    Quantity (changing)    0        0
3    Profit per unit        100      250
4    Flour per unit (kg)    0.5      1        =SUMPRODUCT($B$2:$C$2,B4:C4)   120
5    Labour per unit (min)  4        12       =SUMPRODUCT($B$2:$C$2,B5:C5)   1200
6
7    Total profit           =SUMPRODUCT(B2:C2,B3:C3)
""", "text", title="Listing 2: the spreadsheet model",
             caption="SUMPRODUCT multiplies matching cells in two rows and adds the results. For example, D4 equals 0.5 x loaves + 1 x cakes. The formulas react to B2 and C2, which Solver will change."),
        T("Check the model by typing trial values in B2 and C2 before using Solver. With 100 loaves and 50 cakes: flour used = 0.5 x 100 + 50 = 100 kg, labour = 400 + 600 = 1000 minutes, profit = 10 000 + 12 500 = 22 500 FCFA. Both limits are respected."),
        H("Step 3: the Solver dialog"),
        CODE("""
Set Objective:                 $B$7
To:                            Max
By Changing Variable Cells:    $B$2:$C$2
Subject to the Constraints:    $D$4 <= $E$4
                               $D$5 <= $E$5
                               $B$2:$C$2 = integer
[x] Make Unconstrained Variables Non-Negative
Select a Solving Method:       Simplex LP
""", "text", title="Listing 3: Solver settings",
             caption="Solver is on the Data tab. If you cannot see it, enable it in File, Options, Add-ins, Excel Add-ins, Go, tick Solver Add-in."),
        T("**Simplex LP** is for models where every formula is a sum of variables multiplied by constants (linear models) such as this one. "
          "**GRG Nonlinear** handles smooth curves, and **Evolutionary** handles models with jumps; they are slower and may stop at a good but not the best answer."),
        EX("Worked example 1: reading the answer", intro=("Solver finishes and reports that it found a solution. B2 = 120, C2 = 60. Check that the answer is feasible and find the profit and the unused resources."),
           steps=[
               S("Flour", text="0.5 x 120 + 1 x 60 = 60 + 60 = 120 kg. The limit is 120, so all the flour is used."),
               S("Labour", text="4 x 120 + 12 x 60 = 480 + 720 = 1200 minutes. The limit is 1200, so all the labour is used."),
               S("Profit", text="100 x 120 + 250 x 60 = 12 000 + 15 000 = 27 000 FCFA per day.", math=r"100\times 120 + 250\times 60 = 27\,000"),
               S("Compare with simple choices", text="Only loaves: the limits allow 240 loaves (flour) and 300 (labour), so 240 loaves give 24 000. Only cakes: the limits allow 120 (flour) and 100 (labour), so 100 cakes give 25 000. The mixed plan is better than either."),
           ]),
        D("A constraint is **binding** when it is used up exactly (slack = 0). Here flour and labour are both binding. The **shadow price** of a binding resource is the extra profit from one more unit of it.",
          title="Binding constraints and shadow price"),
        EX("Worked example 2: what is one more kilogram of flour worth?", intro=("The baker can buy 1 extra kg of flour (121 kg). What happens to the best plan and the profit?"),
           steps=[
               S("Re-solve", text="Change E4 to 121 and run Solver again. The best whole-number plan becomes 126 loaves and 58 cakes."),
               S("Check", text="Flour: 0.5 x 126 + 58 = 63 + 58 = 121. Labour: 4 x 126 + 12 x 58 = 504 + 696 = 1200."),
               S("Profit", text="100 x 126 + 250 x 58 = 12 600 + 14 500 = 27 100. The profit rises by 100 FCFA."),
               S("Decision", text="One extra kg of flour is worth 100 FCFA per day to the baker (its shadow price). If flour costs less than 100 FCFA more per kg than usual, buying it pays; if it costs more, do not."),
           ]),
        EX("Worked example 3: when there is no solution", intro=("The baker adds two conditions: at least 150 loaves and at least 80 cakes must be made each day for regular customers. What does Solver report?"),
           steps=[
               S("Flour needed", text="0.5 x 150 + 1 x 80 = 75 + 80 = 155 kg."),
               S("Compare with the limit", text="155 kg is more than the 120 kg available, so no plan can meet all the conditions."),
               S("Solver message", text="Solver reports that it could not find a feasible solution. The model is infeasible: the constraints contradict each other."),
               S("Fix", text="Relax a condition (lower the minimum orders), buy more flour, or decide which customers to serve."),
           ]),
        MISTAKE("Typing numbers instead of formulas in the Used cells", "If D4 is a typed number, Solver changes B2 and C2 but D4 never reacts, so the constraint is meaningless. The objective and the Used cells must be formulas that depend on the changing cells."),
        MISTAKE("Forgetting non-negativity", "Without it Solver may choose a negative number of cakes to \"free\" flour. Tick Make Unconstrained Variables Non-Negative."),
        MISTAKE("Wrong direction in a constraint", "Resources are limited above (used <= limit). Minimum orders are limited below (made >= minimum). Check the sign for each constraint."),
        QUIZ("In a Solver model, which cell must contain a formula that depends on the changing cells?",
             ["The limit cell E4", "The objective cell", "The profit-per-unit cells", "The cell with the label Loaves"], 1,
             "The objective cell is the result Solver maximises or minimises, so it must be a formula using the changing cells (the Used cells also depend on them).",
             hint="What does Solver try to make as large as possible?",
             feedback=["The limit is a fixed number such as 120.", "",
                       "Profit per unit is input data.", "Labels are text."]),
        H("Practice questions"),
        PQ("Name the three parts of an optimisation problem and identify them in the bakery problem.",
           "Objective: maximise total profit. Changing cells: number of loaves and number of cakes. Constraints: flour used no more than 120 kg, labour used no more than 1200 minutes, quantities not negative and whole numbers."),
        PQ("With 100 loaves and 50 cakes, calculate the flour used, the labour used and the profit in the bakery model.",
           "Flour: 0.5 x 100 + 1 x 50 = 100 kg. Labour: 4 x 100 + 12 x 50 = 1000 minutes. Profit: 100 x 100 + 250 x 50 = 22 500 FCFA. Both limits are respected."),
        PQ("Explain what \"binding constraint\" means and give an example from the solution (120 loaves, 60 cakes).",
           "A binding constraint is used up completely, with no slack. Flour is binding because 0.5 x 120 + 60 = 120 kg equals the limit. Labour is binding because 4 x 120 + 12 x 60 = 1200 minutes equals the limit."),
        PQ("Why does the Solver model use SUMPRODUCT instead of typing a long sum such as 0.5 times B2 plus 1 times C2 into each formula? Give one advantage.",
           "SUMPRODUCT multiplies two rows and adds them in a single, short formula, so it is easy to copy to other constraints and still correct when more products (columns) are added. It also keeps the numbers in cells where they can be changed, instead of inside formulas."),
        H("Summary"),
        SUM("Write the objective, changing cells and constraints before opening Solver.",
            "Build formulas with SUMPRODUCT so that the objective and the Used cells react to the changing cells.",
            "Solver settings: objective cell, Max or Min, changing cells, constraints, non-negative, Simplex LP for linear models.",
            "Binding constraints have no slack; shadow price is the gain from one more unit; contradictory limits make a problem infeasible."),
    ],
))

# ---------------------------------------------------------------------------
# Advanced Excel 4: VBA macros
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=PP, topic="Advanced Excel",
    title="VBA macros: loops, conditions and custom functions",
    slug="ic7-vba-macros-loops-conditions-functions",
    minutes=25,
    summary="Record and write VBA macros: use variables, a For loop over rows, an If test and a message box, trace the code, write a custom function, and handle macro security.",
    objectives=[
        "Explain what a macro is and the difference between recording and writing one",
        "Write and trace a Sub procedure with Dim, For...Next, If...Then...Else and MsgBox",
        "Write a Function that can be used in a worksheet formula",
        "State the safety rules for macro-enabled workbooks",
    ],
    key_concepts=["Macro", "VBA", "Sub", "Function", "Variable", "Loop", "Condition", "Macro-enabled workbook", "Macro security"],
    blocks=[
        H("Introduction"),
        T("A shop assistant in Limbe checks the stock list every morning. For each item she compares the quantity with the reorder level and writes "
          "REORDER in the next column when stock is low. It takes ten minutes and she sometimes makes mistakes. A **macro** does the same job "
          "in one click. A macro is a small program, written in **VBA (Visual Basic for Applications)**, that automates actions in Excel."),
        D("A **macro** is a saved set of instructions that Excel can run on demand. You can **record** one (Excel writes the code from your actions) or **write** it in the VBA editor (Alt + F11). A workbook that contains macros is saved as **.xlsm** (macro-enabled).",
          title="Macro"),
        KEY("Recording or writing?", "Each has a place.",
            cards=[["Recording", "Quick for repeated formatting or copying. Records exact cell positions, so it does not adapt to more rows. Use relative recording to avoid fixed cells."],
                   ["Writing", "Needed for loops, decisions and input checks. The code adapts to the data (for example any number of rows)."]]),
        H("The building blocks"),
        CODE("""
Sub Name()              starts a procedure that does something; End Sub finishes it
Function Name(x) As Double   returns a value and can be used in a cell formula
Dim n As Long           declares a variable (Integer, Long, Double, String, Boolean)
Cells(row, col).Value   the value of one cell, e.g. Cells(2, 3)
Range("A1:A5")          a block of cells
For r = 2 To 8 ... Next r       repeat for r = 2, 3, ..., 8
If test Then ... Else ... End If   choose between actions
MsgBox "text"           show a message
Option Explicit         (top of module) forces every variable to be declared
""", "vba", title="Listing 1: the VBA you need in this lesson"),
        H("A macro with a loop and a condition"),
        T("The stock sheet has item names in column A, quantity in B, reorder level in C, and column D is for the status. The data starts in row 2."),
        CODE("""
     A              B     C           D
1    Item           Qty   Reorder at  Status
2    Rice           40    50
3    Oil            120   60
4    Sugar          15    30
5    Salt           200   80
6    Tomato paste   25    25
7    Spaghetti      10    40
8    Tea            70    30
""", "text", title="Listing 2: the stock list"),
        CODE("""
Option Explicit

Sub MarkReorder()
    Dim lastRow As Long, r As Long, n As Long
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    n = 0
    For r = 2 To lastRow
        If Cells(r, 2).Value < Cells(r, 3).Value Then
            Cells(r, 4).Value = "REORDER"
            n = n + 1
        Else
            Cells(r, 4).Value = "OK"
        End If
    Next r
    MsgBox n & " item(s) need reordering."
End Sub
""", "vba", title="Listing 3: the MarkReorder macro",
             caption="lastRow finds the last filled row in column A, so the macro works for any number of items."),
        EX("Worked example 1: tracing the macro", intro=("Trace Listing 3 on the data in Listing 2 and state what appears in column D and in the message box."),
           steps=[
               S("Start", text="lastRow = 8 (the last item, Tea, is in row 8). n = 0."),
               S("r = 2 Rice", text="40 < 50 is true: D2 = REORDER; n = 1."),
               S("r = 3 Oil", text="120 < 60 is false: D3 = OK."),
               S("r = 4 Sugar", text="15 < 30 is true: D4 = REORDER; n = 2."),
               S("r = 5 Salt, r = 6 Tomato paste", text="200 < 80 false: OK. 25 < 25 false (equal is not less): OK."),
               S("r = 7 Spaghetti, r = 8 Tea", text="10 < 40 true: REORDER, n = 3. 70 < 30 false: OK."),
               S("Result", text="Column D reads REORDER, OK, REORDER, OK, OK, REORDER, OK. The message box says: 3 item(s) need reordering."),
           ]),
        CODE("""
r   Item          Qty  Level  Qty < Level   D          n
2   Rice          40   50     True          REORDER    1
3   Oil           120  60     False         OK         1
4   Sugar         15   30     True          REORDER    2
5   Salt          200  80     False         OK         2
6   Tomato paste  25   25     False         OK         2
7   Spaghetti     10   40     True          REORDER    3
8   Tea           70   30     False         OK         3
""", "text", title="Listing 4: trace table"),
        EX("Worked example 2: a small change and its effect", intro=("The manager says: \"Reorder when the quantity is at or below the level.\" Which change is needed, and how does the result change?"),
           steps=[
               S("Change the operator", text="Replace < by <= in the If line: If Cells(r, 2).Value <= Cells(r, 3).Value Then"),
               S("Re-trace the affected row", text="Tomato paste: 25 <= 25 is now true, so D6 = REORDER and n increases."),
               S("New message", text="4 item(s) need reordering. The other rows are unchanged."),
           ]),
        H("A custom function"),
        T("A **Function** returns a value, so you can type it in a cell like =SUM. The example calculates sales tax on an amount. The rate 19.25 percent is used here only as an example; always check the current rate."),
        CODE("""
Function TaxAmount(amount As Double, Optional rate As Double = 0.1925) As Double
    TaxAmount = Round(amount * rate, 0)
End Function

' In cells:   =TaxAmount(20000)       gives 3850
'             =TaxAmount(12500)       gives 2406   (2406.25 rounded)
'             =TaxAmount(4000, 0.1)   gives 400
""", "vba", title="Listing 5: a custom function with an optional argument"),
        EX("Worked example 3: checking the function", intro=("Calculate TaxAmount(20000) and TaxAmount(12500) by hand."),
           steps=[
               S("20 000", text="20 000 x 0.1925 = 3850. Round to 0 decimals: 3850."),
               S("12 500", text="12 500 x 0.1925 = 2406.25. Round to 0 decimals: 2406."),
               S("With a rate given", text="TaxAmount(4000, 0.1) = 4000 x 0.1 = 400. The optional rate overrides the default."),
           ]),
        H("Safe use of macros"),
        T("A macro can do anything the user can do: delete files, send data, install programs. So macros are a common way to spread malware. "
          "Excel disables macros by default and shows a security warning. Enable macros only in files from a source you trust. Do not enable macros in an "
          "attachment from an unknown sender. Keep your own macros in a trusted location, and sign them with a digital certificate if you share them."),
        MISTAKE("Saving a macro workbook as .xlsx", "The macros are deleted. Use Save As, Excel Macro-Enabled Workbook (.xlsm)."),
        MISTAKE("Hard-coding the last row", "Writing For r = 2 To 8 works today, but the macro skips new items tomorrow. Find the last row with End(xlUp) or use the used range."),
        MISTAKE("Confusing = and <> in tests", "In VBA, = tests equality inside an If, and <> means \"not equal\". An off-by-one error between < and <= changes the result, as the Tomato paste example shows."),
        QUIZ("What does the macro in Listing 3 show in the message box if only Rice and Sugar are below their reorder levels?",
             ["2 item(s) need reordering.", "7 item(s) need reordering.", "n item(s) need reordering.", "Nothing, because MsgBox needs a Function"], 0,
             "n counts the REORDER rows, so with two low items it is 2. The & joins the number to the text.",
             hint="What does n count?",
             feedback=["", "7 is the number of items, but only low ones are counted.", "n is a variable; & puts its value into the text, not the letter n.",
                       "MsgBox is a statement and works in a Sub."]),
        H("Practice questions"),
        PQ("State two differences between recording a macro and writing one in the VBA editor.",
           "A recorded macro repeats the exact actions and cell positions, so it does not adapt to different amounts of data and cannot make decisions. A written macro can use variables, loops and If statements, so it adapts to the data and can check conditions."),
        PQ("Explain what each of these lines does: lastRow = Cells(Rows.Count, 1).End(xlUp).Row, and For r = 2 To lastRow.",
           "The first finds the last used row in column 1 (A) by going up from the bottom of the sheet, and stores the row number in lastRow. The second repeats the following instructions for r equal to 2, 3, up to lastRow, so every item row is processed."),
        PQ("Write VBA that puts the word LOW in column D when the value in column B is less than 10, for rows 2 to 20.",
           "Sub MarkLow()\n    Dim r As Long\n    For r = 2 To 20\n        If Cells(r, 2).Value < 10 Then Cells(r, 4).Value = \"LOW\"\n    Next r\nEnd Sub"),
        PQ("Give three precautions to take before running macros in a workbook received by email.",
           "Do not enable macros unless the sender is known and trusted and the file was expected; scan the file with antivirus software; open it first with macros disabled and inspect the code; keep macro security at the default setting that disables macros with notification."),
        H("Summary"),
        SUM("A macro automates Excel; record it for simple repeated actions, write it for loops and decisions.",
            "Sub does a job; Function returns a value to a cell formula; declare variables with Dim.",
            "For r = 2 To lastRow with an If test processes every row; trace with a table of r, test and result.",
            "Save as .xlsm; enable macros only from trusted sources."),
    ],
))

# ---------------------------------------------------------------------------
# IT project management 1: WBS
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=PP, topic="IT project management",
    title="Work breakdown structures: from deliverables to work packages",
    slug="ic7-work-breakdown-structure-and-cost-rollup",
    minutes=22,
    summary="Break a project into deliverables and work packages, apply the 100 percent rule, number the levels, and add up costs from the bottom of the structure to the top.",
    objectives=[
        "Define a work breakdown structure and a work package",
        "Decompose a project into levels without gaps or overlaps (100 percent rule)",
        "Write a numbered WBS and recognise a poor one",
        "Roll costs up from work packages to the project total and add a contingency",
    ],
    key_concepts=["Project", "Deliverable", "Work breakdown structure", "Work package", "100 percent rule", "WBS dictionary", "Cost roll-up", "Contingency"],
    blocks=[
        H("Introduction"),
        T("A school in Bafoussam wins a grant to build a new computer lab: 15 PCs, a switch, cabling, software and training for the teachers. The head teacher asks "
          "the ICT coordinator: \"What exactly must be done, how much will it cost and when will it be ready?\" You cannot answer a question like that for a whole "
          "project at once. You first break the project into smaller and smaller parts until each part can be given a person, a cost and a time. "
          "The result is a **work breakdown structure (WBS)**."),
        D("A **project** is a temporary effort with a start and an end that produces a unique result. A **WBS** is a hierarchical breakdown of the whole scope of the project into **deliverables** (things produced) and finally into **work packages** (the smallest pieces, which can be estimated, assigned and tracked).",
          title="Project and WBS"),
        KEY("Rules of a good WBS", "Examiners often ask for these.",
            cards=[["100 percent rule", "The children of an item together cover 100 percent of the work of their parent, no less and no more. Nothing is forgotten and nothing is counted twice."],
                   ["Deliverable-oriented", "Items are things (Cabling installed) or results, not just verbs without an end product."],
                   ["Work packages", "The lowest level. Small enough to estimate and give to one person or team; a common rule of thumb is between about 8 and 80 hours of work, but each organisation decides."],
                   ["Numbering", "Each item has a code: 1, 1.1, 1.1.1... so that costs and progress can be rolled up."]]),
        H("A WBS for the school lab"),
        CODE("""
1     School computer lab
1.1   Planning and ordering
1.1.1   Site survey                          (A)
1.1.2   Order and pay for equipment          (B)
1.2   Room
1.2.1   Prepare room                         (C)
1.2.2   Install cabling                      (E)
1.3   Equipment
1.3.1   Equipment delivery                   (D)
1.3.2   Install PCs                          (F)
1.4   Software and network
1.4.1   Configure network and software       (G)
1.5   People
1.5.1   Train teachers                       (H)
1.6   Closure
1.6.1   Final testing and handover           (I)
""", "text", title="Listing 1: the WBS (letters are used in the next two lessons)",
             caption="Level 1 is the project. Level 2 groups deliverables. Level 3 holds the work packages."),
        T("Each work package also gets an entry in a **WBS dictionary**: a short description, the person responsible, the deliverable, the cost and the "
          "time. The WBS says WHAT is to be done. It does not say in what order; that comes from the dependencies, used in the Critical Path Method."),
        EX("Worked example 1: rolling up costs", intro=(
            "The work packages cost (in FCFA): A 50 000; B 3 500 000; C 400 000; D 150 000; E 300 000; F 200 000; G 250 000; H 120 000; I 100 000. Calculate the cost of each level 2 item and of the project. Then add a 10 percent contingency."),
           steps=[
               S("1.1 Planning and ordering (A + B)", text="50 000 + 3 500 000 = 3 550 000."),
               S("1.2 Room (C + E)", text="400 000 + 300 000 = 700 000."),
               S("1.3 Equipment (D + F)", text="150 000 + 200 000 = 350 000."),
               S("1.4, 1.5 and 1.6", text="1.4 = 250 000 (G). 1.5 = 120 000 (H). 1.6 = 100 000 (I)."),
               S("Project total", text="3 550 000 + 700 000 + 350 000 + 250 000 + 120 000 + 100 000 = 5 070 000 FCFA. Check by adding all nine packages: the same total."),
               S("Contingency", text="10 percent of 5 070 000 = 507 000. Budget = 5 070 000 + 507 000 = 5 577 000 FCFA.", math=r"5\,070\,000\times 0.10 = 507\,000"),
           ]),
        EX("Worked example 2: improving a poor WBS", intro=(
            "A student draws this WBS for a school website: 1 Website; 1.1 Design; 1.2 Build; 1.3 Test; 1.4 Make the site better. Criticise it and suggest improvements."),
           steps=[
               S("Check the 100 percent rule", text="Design, Build and Test leave out content writing, hosting and training. Something is missing, so the rule is broken."),
               S("Check deliverables", text="\"Make the site better\" is vague and overlaps with Design and Build. It should be removed or replaced with named deliverables."),
               S("Improve", text="1.1 Requirements and design (page plan, colour scheme). 1.2 Content (texts, photos). 1.3 Website build (pages, contact form). 1.4 Hosting and domain. 1.5 Testing on phones and computers. 1.6 Staff training and handover."),
               S("Decompose again", text="Break 1.3 into Home page, News page and Contact form so that each can be given to one person."),
           ]),
        QUIZ("Which statement describes the 100 percent rule?",
             ["A project must be finished with 100 percent of the budget spent", "The children of any WBS item must cover all of the parent's work, with no overlap",
              "Every work package must take exactly 100 hours", "100 percent of tasks must be critical"], 1,
             "The 100 percent rule is about scope: the sub-items together equal the parent, nothing missing and nothing repeated.",
             hint="It is about completeness of scope.",
             feedback=["Spending the whole budget is not the aim of a WBS.", "",
                       "The 8/80 rule of thumb is about size, and not a fixed 100 hours.",
                       "Critical tasks are found by the critical path method, not by the WBS."]),
        MISTAKE("Listing activities in time order instead of breaking down the scope", "A WBS is a tree of what must be delivered, not a to-do list in sequence. Sequence is added later."),
        MISTAKE("Breaking down unevenly", "One work package of 3 hours and another of 3 months cannot be managed in the same way. Decompose big items further."),
        MISTAKE("Forgetting management and closure work", "Planning, meetings, testing, handover and training are part of the scope and cost money. Include them."),
        H("Practice questions"),
        PQ("Define work package and explain why the WBS goes down to that level.",
           "A work package is the lowest-level item of the WBS. The structure continues down to work packages because at that level the work can be estimated for cost and time, assigned to one person or team, and tracked."),
        PQ("A WBS item 2.3 has three children: 2.3.1 costs 120 000, 2.3.2 costs 80 000 and 2.3.3 costs 45 000. Calculate the cost of 2.3, and then of the project if 2.1 is 300 000 and 2.2 is 150 000 and these are the only items.",
           "2.3 = 120 000 + 80 000 + 45 000 = 245 000. Project = 300 000 + 150 000 + 245 000 = 695 000 FCFA."),
        PQ("State the 100 percent rule and give an example of how it can be broken in a WBS for a cybercafe opening.",
           "The sub-items must add up to all the work of the parent, with nothing missing or repeated. In a cybercafe WBS that lists Buy computers, Install network and Hire staff but forgets Licences and Furniture, the scope is incomplete. If Install network also contains Buy cables while Buy computers also lists cables, the work is counted twice."),
        PQ("The budget is 8 000 000 FCFA with a contingency of 12 percent of the base cost. Find the total including contingency.",
           "Contingency = 12 percent of 8 000 000 = 960 000. Total = 8 000 000 + 960 000 = 8 960 000 FCFA."),
        H("Summary"),
        SUM("A WBS breaks the whole scope into deliverables and work packages; it says what, not when.",
            "100 percent rule: children together equal the parent; no gaps, no overlaps.",
            "Number the levels (1, 1.1, 1.1.1) and keep work packages small enough to estimate and assign.",
            "Costs roll up from work packages to the project total; add a contingency for risk."),
    ],
))

# ---------------------------------------------------------------------------
# IT project management 2: critical path method
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=PP, topic="IT project management",
    title="Critical path method: forward pass, backward pass and float",
    slug="ic7-critical-path-forward-backward-pass",
    minutes=28,
    summary="Draw an activity network, calculate earliest and latest start and finish times with a forward and a backward pass, find the float of each activity and identify the critical path.",
    objectives=[
        "Build an activity network from a table of durations and predecessors",
        "Carry out a forward pass to find earliest start and finish times and the project duration",
        "Carry out a backward pass to find latest start and finish times",
        "Calculate total float and identify the critical path",
    ],
    key_concepts=["Activity", "Predecessor", "Network diagram", "Earliest start", "Earliest finish", "Latest start", "Latest finish", "Float", "Critical path"],
    blocks=[
        H("Introduction"),
        T("The grant for the school lab in Bafoussam has a deadline: the lab must be handed over before examinations. The coordinator needs to know "
          "the shortest time in which the project can be completed, and which activities cannot be delayed by even a day. The **Critical Path "
          "Method (CPM)** gives both answers from a table of activities."),
        D("An **activity** is a piece of work with a duration. A **predecessor** is an activity that must finish before another can start. The **critical path** is the longest path of dependent activities through the network; it sets the minimum project duration. **Float** (slack) is the time an activity can be delayed without delaying the whole project.",
          title="CPM terms"),
        CODE("""
Activity                          Code  Days  Predecessors
Site survey                        A     2    -
Order and pay for equipment        B     3    A
Prepare room                       C     6    A
Equipment delivery                 D     5    B
Install cabling                    E     4    C
Install PCs                        F     3    D, E
Configure network and software     G     4    F
Train teachers                     H     2    F
Final testing and handover         I     3    G, H
""", "text", title="Listing 1: activities of the lab project",
             caption="Durations are working days. F needs both the delivery (D) and the cabling (E)."),
        IMG("al-ic7-cpm-network.svg", alt="Activity network with nine boxes A to I; the critical path A, C, E, F, G, I is drawn in amber and the boxes B, D and H are above it with 2 days of float",
            caption="Figure 1. The network. Each box shows the code and duration, and below it the earliest start and finish times."),
        H("Forward pass: earliest times"),
        KEY("Rules for the forward pass", "Work from the start to the end.",
            cards=[["Earliest start (ES)", "The largest earliest finish of all predecessors. An activity with no predecessor starts at 0."],
                   ["Earliest finish (EF)", "EF = ES + duration."],
                   ["Project duration", "The largest EF of the last activities."]]),
        EX("Worked example 1: the forward pass", intro=("Calculate ES and EF for every activity of Listing 1."),
           steps=[
               S("A", text="No predecessor: ES = 0, EF = 0 + 2 = 2."),
               S("B and C", text="Both follow A. B: ES = 2, EF = 5. C: ES = 2, EF = 8."),
               S("D and E", text="D follows B: ES = 5, EF = 10. E follows C: ES = 8, EF = 12."),
               S("F", text="F follows D (EF 10) and E (EF 12). ES is the larger, 12. EF = 15."),
               S("G and H", text="Both follow F. G: ES = 15, EF = 19. H: ES = 15, EF = 17."),
               S("I", text="I follows G (19) and H (17). ES = 19, EF = 22. Project duration = 22 days."),
           ]),
        H("Backward pass: latest times"),
        KEY("Rules for the backward pass", "Work from the end to the start.",
            cards=[["Latest finish (LF)", "The smallest latest start of all successors. The last activities take LF = project duration."],
                   ["Latest start (LS)", "LS = LF - duration."],
                   ["Total float", "Float = LS - ES (the same as LF - EF). An activity with float 0 is critical."]]),
        EX("Worked example 2: the backward pass and float", intro=("Using a project duration of 22 days, calculate LS, LF and float for every activity."),
           steps=[
               S("I", text="Last activity: LF = 22, LS = 22 - 3 = 19. Float = 19 - 19 = 0."),
               S("G and H", text="Their only successor is I with LS 19, so LF = 19 for both. G: LS = 15, float 0. H: LS = 19 - 2 = 17, float = 17 - 15 = 2."),
               S("F", text="Successors G (LS 15) and H (LS 17). LF = the smaller, 15. LS = 15 - 3 = 12. Float 0."),
               S("D and E", text="Their successor F has LS 12, so LF = 12 for both. E: LS = 12 - 4 = 8, float 0. D: LS = 12 - 5 = 7, float = 7 - 5 = 2."),
               S("B and C", text="B: LF = LS of D = 7, LS = 4, float = 4 - 2 = 2. C: LF = LS of E = 8, LS = 2, float 0."),
               S("A", text="Successors B (LS 4) and C (LS 2). LF = 2, LS = 0, float 0."),
               S("Critical path", text="Float 0 for A, C, E, F, G and I, so the critical path is A - C - E - F - G - I with duration 2 + 6 + 4 + 3 + 4 + 3 = 22 days."),
           ]),
        CODE("""
Act  Dur  ES  EF  LS  LF  Float
A    2    0   2   0   2   0   critical
B    3    2   5   4   7   2
C    6    2   8   2   8   0   critical
D    5    5   10  7   12  2
E    4    8   12  8   12  0   critical
F    3    12  15  12  15  0   critical
G    4    15  19  15  19  0   critical
H    2    15  17  17  19  2
I    3    19  22  19  22  0   critical
""", "text", title="Listing 2: the full CPM table", caption="Check: for every activity LS - ES equals LF - EF. B, D and H each have 2 days of float."),
        T("Meaning: if the room preparation (C) takes one extra day, the project ends a day late, because C is critical. But the delivery (D) can be "
          "two days late without any effect on the end date, because D has 2 days of float. The coordinator should put the best staff and the closest "
          "supervision on the critical activities."),
        EX("Worked example 3: another network", intro=("Activities: A 4 days (no predecessor); B 6 days (no predecessor); C 3 days (after A); D 5 days (after A and B); E 2 days (after C and D). Find the duration, the critical path and the float of A and C."),
           steps=[
               S("Forward pass", text="A: 0-4. B: 0-6. C: ES 4, EF 7. D: ES = larger of A's 4 and B's 6 = 6, EF 11. E: ES = larger of 7 and 11 = 11, EF 13. Duration 13 days."),
               S("Backward pass", text="E: LF 13, LS 11. D: LF 11, LS 6. C: LF 11, LS 8. B: LF 6, LS 0. A: LF = smaller of C's LS 8 and D's LS 6 = 6, LS 2."),
               S("Float", text="A: LS - ES = 2 - 0 = 2. B: 0. C: 8 - 4 = 4. D: 0. E: 0."),
               S("Critical path", text="B - D - E, duration 6 + 5 + 2 = 13 days. A has float 2 and C has float 4."),
           ]),
        QUIZ("An activity has ES = 8, duration 5 and LF = 18. What is its total float?",
             ["0", "5", "10", "18"], 1,
             "EF = 8 + 5 = 13. Float = LF - EF = 18 - 13 = 5.",
             hint="Find EF first, then compare with LF.",
             feedback=["That would need LF = 13.", "", "10 comes from 18 - 8 and forgets the duration.", "18 is the latest finish, not the float."]),
        MISTAKE("Using the smaller EF at a merge in the forward pass", "An activity cannot start until ALL predecessors have finished, so ES is the LARGEST EF."),
        MISTAKE("Using the larger LS at a split in the backward pass", "An activity must finish early enough for ALL its successors, so LF is the SMALLEST LS."),
        MISTAKE("Thinking there is only one critical path", "Several paths can have float 0. Delaying any critical activity on any of them delays the project."),
        H("Practice questions"),
        PQ("Activities: A 3 days (no predecessor); B 4 days (after A); C 2 days (after A); D 5 days (after B); E 6 days (after C); F 2 days (after D and E). Find the project duration, the critical path and the float of C and E.",
           "Forward pass: A 0-3, B 3-7, C 3-5, D 7-12, E 5-11, F ES = larger of 12 and 11 = 12, EF 14. Duration 14 days. Backward pass: F LS 12; D LF 12, LS 7; E LF 12, LS 6; B LS 3; C LF 6, LS 4; A LS 0. Critical path A - B - D - F (3 + 4 + 5 + 2 = 14). Float of C = 4 - 3 = 1; float of E = 6 - 5 = 1."),
        PQ("Define float and explain why critical activities have zero float.",
           "Float is the time an activity can be delayed without delaying the project end date. Critical activities lie on the longest path, so their earliest and latest times are equal; any delay moves the project end date by the same amount, so their float is zero."),
        PQ("In Worked example 1, the delivery (D) is delayed by 3 days. What is the new project duration? Explain.",
           "D has 2 days of float. A delay of 3 days uses the 2 days of float and exceeds it by 1, so D finishes on day 13 instead of 10. F can then start on day 13, which is one day later than before, and the project takes 23 days."),
        PQ("Why must the forward pass use the largest earliest finish of the predecessors?",
           "An activity can start only when all its predecessors have finished. The last predecessor to finish, the one with the largest EF, therefore decides the earliest start."),
        H("Summary"),
        SUM("Forward pass: ES = largest EF of predecessors; EF = ES + duration; project duration = largest EF.",
            "Backward pass: LF = smallest LS of successors; LS = LF - duration.",
            "Float = LS - ES = LF - EF. Zero float means critical.",
            "The critical path is the longest path; it fixes the project duration, and delaying it delays the project."),
    ],
))

# ---------------------------------------------------------------------------
# IT project management 3: Gantt charts, schedule and crashing
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=PP, topic="IT project management",
    title="Gantt charts: scheduling, tracking progress and shortening a project",
    slug="ic7-gantt-schedule-tracking-and-crashing",
    minutes=26,
    summary="Turn a CPM table into a dated Gantt chart, show float and the critical path, track progress against the plan, and shorten the project by crashing critical activities.",
    objectives=[
        "Draw a Gantt chart from a table of start times and durations and convert working days to dates",
        "Show the critical path, float and dependencies on a Gantt chart",
        "Track progress and forecast a new end date",
        "Explain crashing and decide whether it is worth its cost",
    ],
    key_concepts=["Gantt chart", "Bar", "Milestone", "Dependency", "Baseline", "Progress", "Crashing", "Slack", "Working days"],
    blocks=[
        H("Introduction"),
        T("The CPM table is accurate but hard for a head teacher, a donor or a builder to read. Most projects also publish a **Gantt chart**: "
          "a bar chart in which each activity is a horizontal bar on a time axis. The length of the bar is the duration and its position is the start date. "
          "A Gantt chart answers: what happens this week, who is busy, what is late?"),
        D("A **Gantt chart** lists the activities down the left and the time along the top. Each activity is a bar from its start to its finish. Arrows may show dependencies, a diamond shows a **milestone** (a point in time with zero duration, such as Handover), and a coloured part of the bar shows progress.",
          title="Gantt chart"),
        H("From CPM to calendar dates"),
        T("The lab project starts on Monday 1 March 2027. Work is done Monday to Friday, so a duration of days means working days. Earliest start (ES) 0 means the "
          "morning of working day 1. An activity with ES = 2 and duration 3 occupies working days 3, 4 and 5. (Public holidays are ignored in this example; a real plan marks them as non-working days.)"),
        CODE("""
Act  Task                         ES  EF  First day     Last day      Float
A    Site survey                   0   2  Mon 1 Mar     Tue 2 Mar     0
B    Order equipment               2   5  Wed 3 Mar     Fri 5 Mar     2
C    Prepare room                  2   8  Wed 3 Mar     Wed 10 Mar    0
D    Equipment delivery            5  10  Mon 8 Mar     Fri 12 Mar    2
E    Install cabling               8  12  Thu 11 Mar    Tue 16 Mar    0
F    Install PCs                  12  15  Wed 17 Mar    Fri 19 Mar    0
G    Configure network/software   15  19  Mon 22 Mar    Thu 25 Mar    0
H    Train teachers               15  17  Mon 22 Mar    Tue 23 Mar    2
I    Final testing and handover   19  22  Fri 26 Mar    Tue 30 Mar    0
""", "text", title="Listing 1: the dated schedule",
             caption="Working days only: C runs 6 working days from Wed 3 Mar to Wed 10 Mar, skipping the weekend. The project finishes on Tuesday 30 March 2027."),
        IMG("al-ic7-gantt-chart.svg", alt="Gantt chart of activities A to I over 22 working days. Critical activities are amber bars and non-critical activities are blue bars with a pale tail showing their float",
            caption="Figure 1. The Gantt chart for the lab project. Pale tails show float: B, D and H can slip by 2 days."),
        EX("Worked example 1: converting a working-day number to a date", intro=("Activity F has ES = 12 and EF = 15. Find its dates, given that working day 1 is Monday 1 March and weekends are not worked."),
           steps=[
               S("Count the days", text="F occupies working days 13, 14 and 15."),
               S("Find working day 13", text="Days 1 to 5 are 1 to 5 March (Mon to Fri). Days 6 to 10 are 8 to 12 March. Day 11 is Mon 15 March, day 12 is Tue 16 March, day 13 is Wed 17 March."),
               S("Find the last day", text="Day 14 is Thu 18 March and day 15 is Fri 19 March."),
               S("Result", text="F runs from Wednesday 17 March to Friday 19 March 2027, which agrees with Listing 1."),
           ]),
        KEY("Gantt chart or network diagram?", "They are used together.",
            cards=[["Gantt chart", "Shows when things happen, how long they last, progress and workload. Easy for everybody to read. Shows dependencies less clearly."],
                   ["Network diagram (CPM)", "Shows dependencies and critical path clearly, and allows float to be calculated. Harder to read for non-specialists."]]),
        H("Tracking progress"),
        EX("Worked example 2: a progress report at the end of day 10", intro=(
            "At the end of working day 10 (Friday 12 March) the coordinator reports: A, B and C are 100 percent complete. D (delivery, 5 days) is 60 percent complete. E (cabling, 4 days) is 25 percent complete. Compare with the plan and forecast the end date."),
           steps=[
               S("Plan at day 10", text="A, B, C and D should be finished. E should have run for 2 of its 4 days, so 50 percent."),
               S("Actual work", text="D has 60 percent of 5 days done: 3 days. Two days of work remain. E has 25 percent of 4 days done: 1 day, so 3 days remain."),
               S("Effect on D", text="D needs 2 more days, so it finishes at the end of day 12. Its planned latest finish is day 12, using up its 2 days of float. It is now critical, but not yet late."),
               S("Effect on E", text="E needs 3 more days: it finishes at day 13, one day later than planned (day 12). E is critical, so the project is affected."),
               S("Forecast", text="F cannot start until E and D have finished, so F starts on day 13 (not 12). F 13-16, G 16-20, I 20-23. The forecast duration is 23 days: the project will finish one day late, on Wednesday 31 March 2027, unless the delay is recovered."),
           ]),
        H("Crashing: shortening a project"),
        D("**Crashing** shortens the project by paying more to complete critical activities sooner, for example by adding workers or overtime. Only critical activities are worth crashing: shortening an activity with float does not shorten the project. After shortening, check whether a different path has become critical.",
          title="Crashing"),
        EX("Worked example 3: is crashing worth it?", intro=(
            "The donor charges a penalty of 100 000 FCFA for each day the lab is late beyond day 20. The room preparation (C, 6 days) can be shortened to 4 days with extra workers costing 40 000 FCFA per day saved. Should the coordinator do it, and can the project be shortened further by crashing D too?"),
           steps=[
               S("Cost of crashing C by 2 days", text="2 x 40 000 = 80 000 FCFA."),
               S("New duration", text="Path A-C-E-F-G-I = 2 + 4 + 4 + 3 + 4 + 3 = 20 days. The other path A-B-D-F-G-I = 2 + 3 + 5 + 3 + 4 + 3 = 20 days is now also critical. The project falls from 22 to 20 days."),
               S("Benefit", text="The project avoids a penalty on 2 days = 200 000 FCFA. Net gain = 200 000 - 80 000 = 120 000 FCFA. Crashing C is worthwhile."),
               S("Crash D as well?", text="Shortening D alone does not help, because the path through C and E is still 20 days. To go below 20 days both paths must be shortened, for example C-E path and B-D path, and the cost doubles for each further day saved."),
           ]),
        MISTAKE("Crashing a non-critical activity", "An activity with float does not control the end date. Shortening it spends money and gains nothing."),
        MISTAKE("Ignoring weekends when converting days to dates", "Twenty-two working days are not 22 calendar days. Count only working days, and add public holidays as non-working days."),
        MISTAKE("Reading the Gantt bars as the order of dependencies", "Two bars that overlap in time may still depend on each other with an offset (start-to-start). Use arrows and the dependency table, not only the bar positions."),
        QUIZ("Which activities should the manager watch most closely to keep the end date, using Listing 1?",
             ["B, D and H, because they have float", "A, C, E, F, G and I, because they have no float", "All activities equally", "Only the last activity, I"], 1,
             "Activities with zero float are critical. A delay on any of them delays the project.",
             hint="Look at the Float column.",
             feedback=["Activities with float can slip without harming the end date.", "",
                       "Equal attention wastes effort. Focus on the critical activities.",
                       "I is critical, but so are the activities before it."]),
        H("Practice questions"),
        PQ("List four items that can be shown on a Gantt chart.",
           "Activity names, bars showing start and duration, milestones, dependencies (arrows), progress (shading), the critical path (a different colour), float or slack, and resources. Any four."),
        PQ("Activity X has ES = 4 and duration 3, and working day 1 is Monday. Give the first and last working day numbers and their weekdays.",
           "It occupies working days 5, 6 and 7. Day 5 is Friday of the first week, day 6 is Monday of the second week (the weekend is skipped), and day 7 is Tuesday. So it runs from Friday to Tuesday."),
        PQ("Give two advantages of a Gantt chart over a table of activities, and one limitation.",
           "It shows the schedule visually, so overlaps, progress and workload are seen at once, and it is easy for non-specialists to read. Limitation: it does not show dependencies and float as clearly as a network diagram, and it does not calculate the critical path by itself."),
        PQ("In the progress report, E was 25 percent complete instead of 50 percent. Explain why the project end date is affected but a delay on H would not be.",
           "E is a critical activity (float 0), so one extra day on E delays F and everything after it by one day. H has 2 days of float, so H can be delayed by up to 2 days without changing the end date."),
        H("Summary"),
        SUM("A Gantt chart shows activities as bars on a calendar, with milestones, progress, dependencies and the critical path.",
            "Convert CPM times to dates by counting working days only.",
            "Compare actual progress with the plan; delays on critical activities move the end date, delays within float do not.",
            "Crash only critical activities and compare the cost with the benefit; check for new critical paths."),
    ],
))

# ---------------------------------------------------------------------------
# Examination / Practice paper
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Examination", topic="Practice paper",
    title="Approaching the Upper Sixth ICT practice paper",
    slug="ic7-exam-practice-paper-approach",
    minutes=22,
    summary="Plan your time for a 40-question multiple-choice practice paper, use a two-pass method, keep a calculation toolkit for each topic, and avoid the traps that cost marks in networking, security, Excel and project management.",
    objectives=[
        "Plan time for a multiple-choice practice paper (KKEVO practice settings)",
        "Use a two-pass method and elimination to improve accuracy",
        "Recall the key formulas and procedures from all six topics of the year",
        "Recognise the common traps in each topic",
    ],
    key_concepts=["Practice paper", "Time plan", "Two-pass method", "Elimination", "Calculation toolkit", "Distractor"],
    blocks=[
        H("Introduction"),
        T("This lesson prepares you for the KKEVO practice paper of the year. The mock has 40 multiple-choice questions and a 90-minute timer. "
          "Those figures are **KKEVO practice settings**, not the settings of the real examination. The real paper format, its length and its "
          "marking must be checked with your teacher and the current GCE Board instructions. The skills below help in any multiple-choice or structured paper."),
        D("The mock covers all six topics of the year: **Cabling and switching**, **Security principles**, **Cryptography**, **Defence and recovery**, **Advanced Excel** and **IT project management**. "
          "After the timed paper the results page shows your score by topic, with links to the lessons to revise.",
          title="What the practice paper covers"),
        H("Plan your time"),
        T("The average time per question is the minutes divided by the number of questions: 90 / 40 = 2.25 minutes, about two minutes and fifteen seconds. "
          "KKEVO advice is to use that average only as a guide: recall questions take less time, calculations take more."),
        CODE("""
Stage                 Suggested time     What to do
First pass            about 55 minutes   Answer every question you can do quickly. Mark the others.
Calculation pass      about 25 minutes   Return to the marked calculations (subnets, RSA, CPM, ALE).
Final check           about 10 minutes   Re-read marked answers, check you have answered all.
""", "text", title="Listing 1: a KKEVO time plan for 90 minutes",
             caption="These times are advice for practice, not official. Adjust them to your own speed."),
        EX("Worked example 1: choosing the order of work", intro=("You have 10 minutes left and 6 questions unanswered: two recall questions, two quick calculations, and two long CPM networks. What should you do?"),
           steps=[
               S("Pick the cheapest marks first", text="Answer the two recall questions (about 30 seconds each)."),
               S("Quick calculations next", text="Use the remaining time on the two quick calculations, for example a subnet size or an ALE."),
               S("Long networks last", text="Do the CPM networks only if time remains. If not, eliminate options that are clearly impossible and guess, because a blank cannot score."),
           ]),
        H("A calculation toolkit"),
        KEY("Formulas to know without looking", "Write them at the start of your rough work if the paper allows.",
            cards=[["Networks", "Usable hosts = 2 to the power (host bits) minus 2. Subnet block size = 2 to the power host bits. DHCP T1 = 50 percent and T2 = 87.5 percent of the lease. VLAN ID has 12 bits (4096 values)."],
                   ["Security", "Risk score = likelihood x impact. SLE = asset value x exposure factor. ALE = SLE x ARO. Search space = characters to the power length. Downtime per year = (1 minus availability) x 8760 hours."],
                   ["Cryptography", "n = p x q. phi = (p - 1)(q - 1). e x d leaves remainder 1 on division by phi. Encrypt c = m to the power e mod n; decrypt m = c to the power d mod n. SHA-256 = 256 bits = 64 hex digits. Pair keys = n(n - 1) / 2."],
                   ["Excel and projects", "XLOOKUP(value, lookup range, return range, if not found, mode). INDEX(range, row, column) with MATCH(value, range, 0). EF = ES + duration; float = LS - ES; critical path = longest path. Roll costs up from work packages."]]),
        EX("Worked example 2: a quick calculation under time pressure", intro=("A question gives a server worth 600 000 FCFA, a 50 percent loss when it fails and one failure every 4 years. Find the ALE."),
           steps=[
               S("SLE", text="600 000 x 0.5 = 300 000."),
               S("ARO", text="One failure every 4 years is 1 / 4 = 0.25 per year."),
               S("ALE", text="300 000 x 0.25 = 75 000 FCFA per year."),
               S("Check against the options", text="If an option shows 300 000, that is the SLE and a distractor. If an option shows 150 000, someone multiplied by 0.5 twice."),
           ]),
        H("Elimination and traps"),
        T("Each wrong option is built from a real mistake. Cross out options you know are wrong. Then compare the remaining ones with the key word of the question. "
          "Watch for words such as always, never, only and all: very few technical statements are absolute."),
        CODE("""
Topic                    Common trap
Cabling and switching    Mixing T568A and T568B; counting the network and broadcast addresses as usable;
                         thinking a switch stops broadcasts.
Security principles      Adding likelihood and impact instead of multiplying; confusing integrity and
                         confidentiality; calling two passwords multi-factor.
Cryptography             Encrypting with the wrong key; confusing hashing with encryption; forgetting that
                         a signature does not hide the message.
Defence and recovery     Reading firewall rules from the bottom; confusing RPO (data) with RTO (time);
                         saying an IDS blocks traffic.
Advanced Excel           Leaving out the 0 in MATCH; forgetting to refresh a pivot table; typing numbers
                         where Solver needs formulas.
IT project management    Using the smaller EF at a merge; crashing a non-critical activity; ignoring
                         weekends when turning days into dates.
""", "text", title="Listing 2: traps by topic"),
        EX("Worked example 3: eliminating options", intro=("Question: A firewall rule list reads (1) permit TCP any to the web server port 443, (2) deny any any. A packet for TCP port 25 arrives at the web server. What happens? The options are: permitted by rule 1; denied by rule 2; permitted because the web server is public; denied by rule 1."),
           steps=[
               S("Test rule 1", text="Port 25 is not port 443, so rule 1 does not match."),
               S("Eliminate", text="Permitted by rule 1 is wrong. Denied by rule 1 is wrong, because rule 1 is a permit rule."),
               S("Choose", text="Rule 2 matches everything, so the packet is denied by rule 2. The option \"permitted because the web server is public\" ignores the rules."),
           ]),
        QUIZ("You are unsure of a question and have eliminated two options. What is the best action in a practice paper with no negative marking?",
             ["Leave it blank", "Choose between the remaining two, mark it, and return if time allows", "Change all the other answers", "Spend 10 minutes on it now"], 1,
             "Narrowing to two gives a 50 percent chance. Mark the question and return to it after the first pass. (Check whether the real paper uses negative marking.)",
             hint="What can a blank answer score?",
             feedback=["A blank answer scores nothing.", "",
                       "Changing other answers without a reason lowers your score.",
                       "Ten minutes is about four questions' worth of time."]),
        MISTAKE("Rushing to start with question 1 in a calculation", "Read the question twice and underline the quantities and units before you calculate. Many errors are misread numbers."),
        MISTAKE("Changing a correct answer at the end", "Change an answer only if you have found a specific mistake. First instincts are often right when your revision is good."),
        MISTAKE("Revising only your favourite topic", "The results page shows your score by topic. Spend the next revision session on the lowest one."),
        H("Practice questions"),
        PQ("A practice paper has 60 questions in 75 minutes. Calculate the average time per question, and give the time you would plan for a first pass if you keep 10 minutes for checking.",
           "75 / 60 = 1.25 minutes per question on average. With 10 minutes for checking, 65 minutes remain for answering, which is about 1 minute 5 seconds per question for a first pass. Spend less on recall questions to leave time for calculations."),
        PQ("Describe the two-pass method and say why it helps.",
           "In the first pass answer all questions you can do quickly and mark the others. In the second pass return to the marked ones. It secures the easy marks first, avoids spending too long on one hard question, and often a later question reminds you of a fact that helps."),
        PQ("List two ways to use the topic scores after a mock to plan revision.",
           "Identify the topic with the lowest score and revise its lesson first; redo that topic's practice set. Review the questions you answered wrongly and read the explanation of each distractor to find the mistake behind your choice."),
        PQ("An option says \"A switch always stops broadcast traffic.\" Explain how to use the word always to reject it.",
           "Absolute words such as always are rarely correct in technical statements. Here a switch floods broadcasts to all ports in the same VLAN; only a router or a VLAN boundary stops them. One counter-example makes the statement false."),
        H("Summary"),
        SUM("KKEVO practice settings: 40 questions, 90 minutes, about 2.25 minutes each. Check the real paper format with your teacher.",
            "Use the two-pass method: easy marks first, calculations second, checking last.",
            "Keep a toolkit of formulas for subnets, ALE, RSA, CPM and Excel lookups.",
            "Eliminate options using the traps for each topic and watch absolute words.",
            "Use the topic scores on the results page to plan your revision."),
    ],
))
