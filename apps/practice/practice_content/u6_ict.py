"""ICT (A Level) Upper Sixth: draft practice sets, one per lesson topic."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "upper-sixth")

SETS = []

# ---------------------------------------------------------------------------
# Network Engineering / Cabling and switching
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Network Engineering", topic="Cabling and switching",
    title="RJ-45 termination, VLANs and DHCP scopes", lesson="rj45-termination-vlans-and-dhcp-scopes",
    questions=[
        MC("A technician terminates a cable to the T568B standard. Which wire goes to pin 6?", [
            C("Green", correct=True),
            C("Orange", why="Orange is on pin 6 in T568A. T568B swaps the orange and green pairs, so pin 6 becomes Green."),
            C("Blue", why="Blue is on pin 4 in both standards."),
            C("White-Green", why="White-Green is on pin 3 in T568B; its partner, solid Green, is on pin 6."),
        ], steps=[
            S("Recall T568B", text="White-Orange, Orange, White-Green, Blue, White-Blue, Green, White-Brown, Brown."),
            S("Read pin 6", text="The sixth wire is Green."),
        ], concept="T568A and T568B pin orders", skill="Recall",
           hint="Write out the T568B order from pin 1 and count along to the sixth wire.",
           feedback="T568A and T568B differ only by swapping the orange and green pairs."),
        MC("Two old switches that do not support Auto-MDI/MDI-X must be connected directly. Which cable is needed?", [
            C("A crossover cable: T568A at one end and T568B at the other", correct=True),
            C("A straight-through cable: T568B at both ends", why="Straight-through is for unlike devices such as PC to switch. Two switches are like devices."),
            C("A straight-through cable: T568A at both ends", why="Using the same standard at both ends, A or B, still gives a straight-through cable."),
            C("A rollover (console) cable", why="A console cable is for configuring a device from a PC, not for carrying network traffic between switches."),
        ], steps=[
            S("Classify the devices", text="Switch to switch means like devices."),
            S("Choose the cable", text="Like devices traditionally need a crossover cable: T568A at one end and T568B at the other."),
        ], concept="Straight-through versus crossover cables", skill="Application",
           hint="Are the two devices alike or unlike?",
           feedback="Auto-MDI/MDI-X hides this on modern switches, but the traditional rule is still examined."),
        MC("A frame arrives at switch port 5 with source MAC address A and destination MAC address B. B is already in the MAC address table on port 9. What does the switch do?", [
            C("Records A against port 5 and forwards the frame out of port 9 only", correct=True),
            C("Floods the frame out of every port except port 5", why="Flooding is only for unknown or broadcast destinations. B is already known on port 9."),
            C("Records B against port 5 and forwards the frame out of port 9", why="The switch learns from the source address, so it records A on port 5, not B."),
            C("Forwards the frame out of every port, like a hub", why="A hub repeats every signal; a switch uses its table to send a known destination to one port."),
        ], steps=[
            S("Learn", text="The switch records the source MAC address A against the incoming port 5."),
            S("Forward", text="The destination B is in the table on port 9, so the frame goes out of port 9 only."),
        ], concept="How a switch learns and forwards frames", skill="Application",
           hint="A switch learns from one address in the frame and forwards using the other.",
           feedback="Learn the source, forward by the destination."),
        MC("A lab PC in VLAN 20 and an admin printer in VLAN 10 are plugged into the same switch. Why can the PC not print to it?", [
            C("Each VLAN is a separate broadcast domain, so traffic between them needs a router or layer 3 switch", correct=True),
            C("The cable to the printer must be a crossover cable", why="The cable type affects the physical link, not which VLAN the ports are in."),
            C("The switch has not yet learned the printer's MAC address", why="An unknown address is flooded, but only within the same VLAN; learning it would not cross VLANs."),
            C("The printer needs a trunk port", why="A trunk carries several VLANs between switches or to a router; it does not route between VLANs on its own."),
        ], steps=[
            S("VLANs are separate networks", text="Ports in different VLANs form different broadcast domains even on one switch."),
            S("What is needed", text="A router or layer 3 switch must route between VLAN 10 and VLAN 20, where traffic can also be filtered."),
        ], concept="VLANs as separate broadcast domains", skill="Reasoning",
           hint="What device is normally needed to move traffic between two different networks?",
           feedback="VLANs separate traffic until something routes between them."),
        NUM("The IEEE 802.1Q tag added to frames on a trunk port contains a 12-bit VLAN ID field. How many different values can this field hold?", 4096, steps=[
            S("Count the bit patterns", math=r"2^{12} = 4096"),
            S("Note", text="A few of these values are reserved, so slightly fewer are usable as VLANs."),
        ], concept="Trunk ports and 802.1Q tagging", skill="Calculation",
           hint="How many different patterns can n bits make?"),
        NUM("A DHCP scope is planned for the network 192.168.40.0/24. The addresses 192.168.40.1 to 192.168.40.30 are excluded, and the pool runs from 192.168.40.31 to 192.168.40.254. How many addresses can be leased?", 224, steps=[
            S("Count an inclusive range", math=r"254 - 31 + 1 = 224"),
        ], concept="Planning a DHCP pool with exclusions", skill="Calculation",
           hint="When counting from one number to another inclusive, remember to add one."),
        MC("In what order are the four DHCP messages exchanged when a client obtains an address?", [
            C("Discover, Offer, Request, Acknowledge", correct=True),
            C("Request, Offer, Discover, Acknowledge", why="The client cannot request an address before it has discovered a server and received an offer."),
            C("Discover, Request, Offer, Acknowledge", why="The server offers an address first; the client then requests the offered address."),
            C("Offer, Discover, Acknowledge, Request", why="The client starts the exchange with a broadcast Discover; the server cannot offer before that."),
        ], steps=[
            S("Remember DORA", text="The client broadcasts Discover, the server replies with an Offer, the client sends a Request and the server confirms with an Acknowledge."),
        ], concept="DHCP DORA process", skill="Recall",
           hint="The four initials spell a short word.",
           feedback="DORA: Discover, Offer, Request, Acknowledge."),
        MC("A lab printer has the fixed address 192.168.20.10, but that address was not excluded from the DHCP pool. What problem is likely?", [
            C("The DHCP server may lease 192.168.20.10 to a PC, causing an IP address conflict", correct=True),
            C("The printer will be moved to a different VLAN", why="DHCP does not change VLAN membership; VLANs are set on the switch ports."),
            C("The lease time will be shortened to zero", why="Exclusions do not affect the lease time option."),
            C("The switch will flood all frames for the printer", why="Flooding depends on the MAC address table, not on the DHCP pool."),
        ], steps=[
            S("Why exclusions matter", text="The server only avoids addresses it is told about. If .10 stays in the pool it may be leased to another device."),
            S("Fix", text="Exclude every static address, for example 192.168.20.1 to 192.168.20.20."),
        ], concept="DHCP exclusions for static devices", skill="Reasoning",
           hint="What happens if two devices end up with the same IP address?",
           feedback="Always exclude addresses used by statically configured devices."),
    ]))

# ---------------------------------------------------------------------------
# Cybersecurity / Security principles
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Cybersecurity", topic="Security principles",
    title="The CIA triad", lesson="the-cia-triad",
    questions=[
        MC("A list of every student's fee balance at a school in Limbe is posted on a public WhatsApp group by mistake. Which property of the CIA triad is broken?", [
            C("Confidentiality", correct=True),
            C("Integrity", why="The balances were not changed; they were read by people who should not see them."),
            C("Availability", why="The bursar can still use the records; nothing was made unusable."),
            C("Non-repudiation", why="Non-repudiation is about proving who performed an action; it is not part of the triad and not the issue here."),
        ], steps=[
            S("What happened to the data?", text="It was disclosed to unauthorised people, not changed or made unavailable."),
            S("Name the property", text="Unauthorised disclosure breaks confidentiality."),
        ], concept="Confidentiality", skill="Application",
           hint="Was the data read, changed or made unusable?",
           feedback="A leaked list is confidentiality; an edited list would be integrity."),
        MC("During a bank transfer, an attacker intercepts the message and changes the amount from 50 000 FCFA to 500 000 FCFA. Which property is mainly broken?", [
            C("Integrity", correct=True),
            C("Confidentiality", why="The main harm is that the data was altered, not merely read."),
            C("Availability", why="The transfer service still works; the problem is that the data in it is wrong."),
            C("Authentication of the server", why="Authentication proves who someone is; the attack described modifies data in transit."),
        ], steps=[
            S("Identify the harm", text="The amount is no longer accurate: an unauthorised change."),
            S("Name the property", text="Unauthorised modification breaks integrity."),
        ], concept="Integrity", skill="Application",
           hint="Ask whether the data was disclosed, changed or blocked.",
           feedback="Integrity means data is accurate and not changed without authorisation."),
        MC("A long power cut shuts down the server of a microfinance office in Bamenda, so cashiers cannot record deposits for a whole day. Which property is broken, and which control would best protect it?", [
            C("Availability; install a UPS with a generator", correct=True),
            C("Integrity; keep an audit log", why="The data is not altered; the service is unusable. Audit logs protect integrity, not availability."),
            C("Confidentiality; encrypt the server disk", why="Nobody read the data without permission, and encryption does not keep a server running."),
            C("Availability; give each cashier a stronger password", why="Availability is the right property, but passwords protect confidentiality and do nothing during a power cut."),
        ], steps=[
            S("Identify the property", text="Authorised users cannot use the system when they need it: availability."),
            S("Choose a matching control", text="A UPS with a generator keeps the server running through power cuts."),
        ], concept="Availability and matching controls", skill="Application",
           hint="First name the property, then check that the control actually stops this threat.",
           feedback="A justified control names the property it protects and the threat it stops."),
        MC("A teacher's password for the marks database is written on a sticky note on the monitor. How is this best described?", [
            C("A vulnerability", correct=True),
            C("A threat", why="A threat is something that could cause harm, such as a student wanting to change marks. The sticky note is the weakness the threat could use."),
            C("A risk", why="Risk combines how likely harm is and how bad it would be; the sticky note itself is a weakness."),
            C("A control", why="A control reduces risk. This note increases it."),
        ], steps=[
            S("Threat or weakness?", text="The note does not cause harm by itself; it is a weakness that a threat could exploit."),
            S("Name it", text="A weakness is a vulnerability."),
        ], concept="Threats, vulnerabilities and risk", skill="Concept",
           hint="Is the sticky note the attacker, or the weakness an attacker could use?",
           feedback="A threat exploits a vulnerability; risk depends on likelihood and impact."),
        MC("A customer receives an SMS: \"Your MoMo account is blocked. Send your PIN to unblock it.\" What is the most effective defence against this kind of attack?", [
            C("Awareness: a genuine operator never asks for a PIN, so the customer should not reply", correct=True),
            C("Installing a firewall on the customer's phone", why="This is social engineering: it attacks the person, not the network, so a firewall does not stop the customer typing the PIN."),
            C("Making a daily backup of the phone", why="Backups protect availability; they do not stop a PIN being given away."),
            C("Using a longer PIN", why="A longer PIN does not help if the customer sends it to the attacker."),
        ], steps=[
            S("Classify the attack", text="It tricks a person into revealing a secret: social engineering (smishing)."),
            S("Choose the defence", text="Social engineering is defeated mainly by awareness and procedures."),
        ], concept="Social engineering", skill="Reasoning",
           hint="Does this attack target a machine or a person?",
           feedback="Awareness is the main defence against phishing and fake calls."),
        MC("Which control is used mainly to detect unauthorised changes to data, protecting integrity?", [
            C("Storing a hash of each record and checking it when the record is read", correct=True),
            C("A UPS and generator", why="These keep systems running, which protects availability."),
            C("Encrypting the data so that outsiders cannot read it", why="Encryption mainly protects confidentiality; on its own it is not the usual way to detect a change."),
            C("A redundant server that takes over on failure", why="Failover protects availability, not the accuracy of the data."),
        ], steps=[
            S("How a hash helps", text="Any change to the data changes its hash, so a mismatch reveals tampering."),
        ], concept="Controls for integrity", skill="Concept",
           hint="Which control would show that even one character had been changed?",
           feedback="Hashes, digital signatures, validation and audit logs support integrity."),
        MC("A microfinance office gives each cashier an account that can record deposits and withdrawals but cannot change interest rates or delete customers. What is this principle called?", [
            C("Least privilege", correct=True),
            C("Social engineering", why="Social engineering is an attack that tricks people; this is a control."),
            C("Redundancy", why="Redundancy means spare equipment or links to protect availability."),
            C("Avalanche effect", why="The avalanche effect is a property of hash functions."),
        ], steps=[
            S("Name the principle", text="Giving each user only the access needed for their job is least privilege. It protects confidentiality and integrity."),
        ], concept="Least privilege", skill="Recall",
           hint="Each user gets only the permissions their job needs. What is that called?",
           feedback="Least privilege limits the damage a mistake or a stolen account can do."),
        MC("A school locks its results server so tightly that teachers can enter marks only from one office computer during two hours a week. Which problem does this create?", [
            C("Availability suffers, because authorised users cannot reach the system when they need it", correct=True),
            C("Confidentiality suffers, because more people can read the marks", why="Fewer people can reach the system, so confidentiality is if anything stronger."),
            C("Integrity suffers, because marks are changed without authorisation", why="Restricting access does not cause unauthorised changes."),
            C("There is no problem: tighter security is always better", why="Security must balance all three properties; locking everything down destroys availability."),
        ], steps=[
            S("Check all three properties", text="Confidentiality and integrity are well protected, but authorised teachers cannot use the system when needed."),
            S("Conclusion", text="Availability is lost. Good security balances the three properties."),
        ], concept="Balancing the three properties", skill="Reasoning",
           hint="Can the people who are allowed to use the system actually use it?",
           feedback="Security that nobody can use has failed on availability."),
    ]))

# ---------------------------------------------------------------------------
# Cybersecurity / Cryptography
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Cybersecurity", topic="Cryptography",
    title="AES, RSA, hashing and digital signatures", lesson="cryptography-aes-rsa-pki-and-hashing",
    questions=[
        MC(r"For a toy RSA key with $p = 7$ and $q = 11$, the totient is $\varphi(n) = 60$. Which public exponent $e$ is valid?", [
            C("$e = 7$", correct=True),
            C("$e = 5$", why="5 divides 60, so gcd(5, 60) = 5 and e has no inverse; decryption would be impossible."),
            C("$e = 9$", why="9 and 60 share the factor 3, so e = 9 has no inverse modulo 60."),
            C("$e = 4$", why="4 and 60 are both even, so they share a factor and e = 4 cannot be used."),
        ], steps=[
            S("Condition on e", math=r"\gcd(e, \varphi(n)) = 1"),
            S("Factor the totient", math=r"60 = 2^2 \times 3 \times 5", text="e must not be divisible by 2, 3 or 5. Of the options only 7 qualifies."),
        ], concept="Choosing a valid RSA public exponent", skill="Reasoning",
           hint="e must share no factor with the totient. What are the prime factors of 60?",
           feedback="Always check gcd(e, totient) = 1 before using e."),
        NUM(r"Toy RSA: $p = 7$, $q = 11$, so $n = 77$ and $\varphi(n) = 60$, with $e = 7$. Find the private exponent $d$, the inverse of $e$ modulo 60 (with $0 < d < 60$).", 43, steps=[
            S("Condition", math=r"7d \equiv 1 \pmod{60}"),
            S("Search multiples of 60 plus 1", math=r"61, 121, 181, 241, 301 = 7 \times 43"),
            S("Check", math=r"7 \times 43 = 301 = 5 \times 60 + 1"),
        ], concept="RSA key generation: finding d", skill="Calculation",
           hint="Look for a number of the form 60k + 1 that is divisible by 7."),
        NUM(r"Using the public key $(e, n) = (7, 77)$, encrypt the message $m = 5$. What is the ciphertext $c = m^e \bmod n$?", 47, steps=[
            S("Square and multiply", math=r"5^2 = 25,\quad 5^4 = 625 \equiv 9 \pmod{77}"),
            S("Combine", math=r"5^7 = 5^4 \times 5^2 \times 5 \equiv 9 \times 25 \times 5 = 1125 \equiv 47 \pmod{77}"),
            S("Check", math=r"1125 = 14 \times 77 + 47"),
        ], concept="RSA encryption with the public key", skill="Calculation",
           hint="Reduce modulo 77 after each multiplication so the numbers stay small."),
        MC("A bank wants to sign a message so customers can check that it really came from the bank and was not altered. How is the digital signature created?", [
            C("Hash the message, then encrypt the hash with the bank's private key", correct=True),
            C("Hash the message, then encrypt the hash with the bank's public key", why="Anyone can use the bank's public key, so anyone could create such a signature; it proves nothing about the sender."),
            C("Encrypt the whole message with the customer's public key", why="That gives confidentiality for the customer, not proof that the bank sent it."),
            C("Encrypt the message with AES using a shared key", why="A shared key does not prove which party created the message, so it gives no non-repudiation."),
        ], steps=[
            S("Sign", text="Only the bank holds its private key, so encrypting the hash with it proves the bank made the signature."),
            S("Verify", text="The customer decrypts the signature with the bank's public key and compares it with a fresh hash of the message."),
        ], concept="Digital signatures", skill="Concept",
           hint="Which key does only the sender have?",
           feedback="Signing uses the sender's private key; verifying uses the sender's public key."),
        NUM("A SHA-256 digest is written in hexadecimal. How many hexadecimal characters does it contain?", 64, steps=[
            S("Bits per hex character", text="Each hexadecimal digit represents 4 bits."),
            S("Divide", math=r"256 \div 4 = 64"),
        ], concept="Hash functions: fixed-length SHA-256 digest", skill="Calculation",
           hint="How many bits does one hexadecimal digit represent?"),
        MC("Why does an HTTPS session use public-key cryptography and AES together?", [
            C("Public-key cryptography safely agrees a session key; AES then encrypts the bulk data quickly", correct=True),
            C("AES is used to exchange the keys and RSA encrypts the page data", why="This is the wrong way round: RSA is slow, so it is used for the key exchange, and fast AES for the data."),
            C("Using two ciphers makes the encryption twice as long, so it is twice as strong", why="The reason is speed and key distribution, not doubling the encryption."),
            C("AES cannot encrypt web pages, so RSA is needed for text", why="AES encrypts any binary data, including web pages; it is the main cipher for the traffic."),
        ], steps=[
            S("Strength of each", text="RSA solves the key distribution problem but is slow; AES is fast but needs a shared key."),
            S("Combine", text="Hybrid encryption uses public-key methods to agree the AES session key, then AES for the traffic."),
        ], concept="Symmetric versus asymmetric encryption", skill="Reasoning",
           hint="Which method is fast, and which one solves the problem of sharing a key?",
           feedback="This combination is called hybrid encryption."),
        MC("What does a digital certificate issued by a certificate authority (CA) allow a browser to check?", [
            C("That the public key in the certificate really belongs to the named website", correct=True),
            C("That the website's private key is stored inside the certificate", why="The private key is never put in a certificate; it stays secret with the owner."),
            C("That the website contains no viruses", why="A certificate proves identity, not that the content is safe."),
            C("That the connection will never be intercepted", why="A certificate lets the browser authenticate the server; it does not stop someone capturing packets."),
        ], steps=[
            S("Contents of a certificate", text="Owner's name, owner's public key, expiry date and the CA's digital signature."),
            S("What the browser checks", text="It verifies the CA's signature with a trusted CA public key, which links the public key to the website's identity."),
        ], concept="PKI and digital certificates", skill="Concept",
           hint="A certificate links two things together. What are they?",
           feedback="PKI links public keys to real identities through CA signatures."),
        MC("A school stores teachers' passwords as SHA-256 hashes, each with a random salt. What is the main purpose of the salt?", [
            C("To make identical passwords give different hashes and defeat precomputed tables of common hashes", correct=True),
            C("To allow the system to decrypt the hash back to the password", why="Hashing is one-way; a salt does not make it reversible."),
            C("To make the digest shorter so it takes less storage", why="SHA-256 always outputs 256 bits, salted or not."),
            C("To encrypt the password with AES before hashing", why="A salt is random data added to the input, not an encryption key."),
        ], steps=[
            S("Without a salt", text="Two teachers with the same password would have the same hash, and attackers could look up common hashes in a table."),
            S("With a salt", text="Each password gets different random data added before hashing, so precomputed tables no longer work."),
        ], concept="Salted password hashing", skill="Concept",
           hint="What could an attacker do if everyone with the password 123456 had the same stored hash?",
           feedback="Store salted hashes of passwords, never the passwords."),
    ]))

# ---------------------------------------------------------------------------
# Cybersecurity / Defence and recovery
# ---------------------------------------------------------------------------
_RULES = ("A stateful firewall uses these rules, checked top to bottom: "
          "1 ALLOW TCP from 192.168.10.0/24 to any, port 443; "
          "2 ALLOW UDP from 192.168.10.0/24 to 192.168.10.53, port 53; "
          "3 ALLOW TCP from any to 192.168.50.10, port 443; "
          "4 DENY TCP from any to any, port 23; "
          "5 DENY anything else. ")

SETS.append(practice_set(
    module="Cybersecurity", topic="Defence and recovery",
    title="Firewalls, IDS/IPS and disaster recovery", lesson="firewalls-ids-ips-and-disaster-recovery",
    questions=[
        MC(_RULES + "What happens to a packet from 192.168.10.25 to 41.202.0.10 on TCP port 80?", [
            C("Denied by rule 5, the default deny", correct=True),
            C("Allowed by rule 1", why="Rule 1 only allows port 443 (HTTPS). Port 80 does not match it."),
            C("Denied by rule 4", why="Rule 4 only matches port 23 (Telnet)."),
            C("Allowed, because the source is inside the LAN", why="A firewall allows only what a rule explicitly permits; being inside the LAN is not enough."),
        ], steps=[
            S("Check rules in order", text="Rule 1 needs port 443; rule 2 needs UDP 53; rule 3 needs destination 192.168.50.10; rule 4 needs port 23. None match."),
            S("Default deny", text="The packet reaches rule 5 and is denied."),
        ], concept="Applying a firewall rule set", skill="Application",
           hint="Go down the rules one by one; the first rule that matches every field decides.",
           feedback="Anything not explicitly allowed falls through to the default deny."),
        MC(_RULES + "What happens to a packet from 102.244.0.7 (on the internet) to 192.168.50.10 on TCP port 443?", [
            C("Allowed by rule 3", correct=True),
            C("Allowed by rule 1", why="Rule 1 needs a source inside 192.168.10.0/24; 102.244.0.7 is on the internet."),
            C("Denied by rule 5", why="Rule 3 matches first (any source, the DMZ server, port 443), so rule 5 is never reached."),
            C("Denied, because traffic from the internet is never allowed in", why="Rule 3 deliberately allows HTTPS to the public web server in the DMZ."),
        ], steps=[
            S("Rules 1 and 2", text="Both need a LAN source, so they do not match."),
            S("Rule 3", text="Any source, destination 192.168.50.10, TCP 443: match. The packet is allowed."),
        ], concept="Firewall rules and the DMZ", skill="Application",
           hint="Check the source address against rules 1 and 2 first.",
           feedback="Public servers sit in a DMZ so outside access to them does not expose the LAN."),
        MC("An administrator adds the rule ALLOW any any any at the TOP of a rule set that ends with several DENY rules. What is the effect?", [
            C("Every packet matches the new rule first, so all traffic is allowed and the DENY rules are useless", correct=True),
            C("Nothing changes, because DENY rules always take priority", why="Rules are checked top to bottom and the first match wins; DENY has no special priority."),
            C("All traffic is blocked", why="The new rule allows, not denies. All traffic would be blocked if a DENY any rule were at the top."),
            C("Only traffic not covered by the DENY rules is allowed", why="That would be true if the ALLOW rule were at the bottom, not the top."),
        ], steps=[
            S("First match wins", text="Every packet matches ALLOW any any any, so no later rule is checked."),
            S("Lesson", text="Put specific rules first and the default deny last."),
        ], concept="Rule order and first match", skill="Reasoning",
           hint="Which rule does every packet meet first?",
           feedback="Because the first match wins, rule order matters."),
        MC("Which statement correctly compares an IDS with an IPS?", [
            C("An IDS detects and raises alerts; an IPS sits inline and can block suspicious traffic", correct=True),
            C("An IDS blocks attacks; an IPS only logs them", why="This is reversed. Only the IPS, which sits in the traffic path, can block."),
            C("Both block traffic, but an IPS is host-based and an IDS is network-based", why="Both can be network- or host-based; the difference is alerting versus blocking."),
            C("An IDS checks only IP addresses and ports, like a packet filter", why="An IDS inspects traffic for attack signatures or anomalies, not just addresses and ports."),
        ], steps=[
            S("Detection versus prevention", text="Detection systems watch and alert. Prevention systems are in the path of traffic and can drop packets."),
        ], concept="IDS versus IPS", skill="Recall",
           hint="The D stands for detection and the P for prevention.",
           feedback="An IDS alerts; only an IPS or firewall blocks."),
        MC("A new attack that has never been seen before (a zero-day attack) hits a network. Which detection method is more likely to notice it, and what is its main drawback?", [
            C("Anomaly-based detection; it produces more false positives", correct=True),
            C("Signature-based detection; it needs frequent updates", why="Signature-based detection needs a known pattern, so it misses a never-seen attack."),
            C("Anomaly-based detection; it can only find known attacks", why="Finding only known attacks is the limitation of signature-based detection."),
            C("Signature-based detection; it produces many false negatives on known attacks", why="Signature matching is accurate for known attacks; its weakness is new attacks."),
        ], steps=[
            S("New attack", text="There is no signature yet, but its behaviour differs from normal, which anomaly detection can flag."),
            S("Drawback", text="Unusual but legitimate activity is also flagged, giving false positives."),
        ], concept="Signature-based versus anomaly-based detection", skill="Reasoning",
           hint="Which method needs a database of known patterns?",
           feedback="Most products combine both methods."),
        NUM("An office makes a full backup every Sunday at 22:00 and an incremental backup Monday to Friday at 22:00. The server disk fails on Friday at 10:00. "
            "How many backup sets must be restored, in total, to recover the most recent data?", 5, steps=[
            S("Last full backup", text="Sunday 22:00: 1 set."),
            S("Incrementals since then", text="Monday, Tuesday, Wednesday and Thursday at 22:00 (Friday's has not run): 4 sets."),
            S("Total", math=r"1 + 4 = 5"),
        ], concept="Restoring from incremental backups", skill="Calculation",
           hint="An incremental restore needs the last full backup plus every incremental after it, in order."),
        NUM("In the same office (full backup Sunday 22:00, incrementals Monday to Friday at 22:00), the disk fails on Friday at 10:00. "
            "How many hours of data are lost?", 12, unit="hours", steps=[
            S("Last backup", text="Thursday 22:00."),
            S("Time to the failure", math=r"\text{Thursday 22:00 to Friday 10:00} = 12\ \text{hours}"),
        ], concept="Data loss and the recovery point objective", skill="Calculation",
           hint="Find the most recent backup before the failure, then count the hours."),
        MC("A school makes a full backup every Friday evening and a differential backup every other evening. The server is destroyed on Wednesday afternoon. Which backups are needed?", [
            C("Friday's full backup and Tuesday's differential", correct=True),
            C("Friday's full backup and the differentials from Saturday to Tuesday", why="Each differential contains everything changed since the full backup, so only the latest one is needed."),
            C("Tuesday's differential only", why="A differential holds only the changes since the full backup; the full backup is still needed."),
            C("Friday's full backup only", why="That would lose every change made from Saturday to Tuesday."),
        ], steps=[
            S("What a differential holds", text="Everything changed since the last full backup."),
            S("Restore", text="Restore Friday's full backup, then the most recent differential, Tuesday's."),
        ], concept="Full, incremental and differential backups", skill="Application",
           hint="Does a differential contain changes since the last backup, or since the last full backup?",
           feedback="Differential restores need only the full backup plus the latest differential."),
    ]))

# ---------------------------------------------------------------------------
# Productivity & Project Management / Advanced Excel
# ---------------------------------------------------------------------------
_FEES = ("The sheet Fees holds IDs in A2:A5 (S101, S102, S103, S104), names in B2:B5 (Ngwa Paul, Fon Mary, Tabi Eric, Ewane Joy), "
         "classes in C2:C5 (L6A, L6B, U6A, U6A) and fees paid in D2:D5 (75000, 50000, 90000, 60000). ")

SETS.append(practice_set(
    module="Productivity & Project Management", topic="Advanced Excel",
    title="Lookups, pivot tables, Solver and VBA", lesson="advanced-excel-lookups-pivots-solver-vba",
    questions=[
        MC(_FEES + "What does =XLOOKUP(\"S104\", A2:A5, D2:D5) return?", [
            C("60000", correct=True),
            C("Ewane Joy", why="Ewane Joy is in B2:B5, but the return_array here is D2:D5, the fees column."),
            C("4", why="4 is the position of S104, which MATCH would return. XLOOKUP returns the matching value."),
            C("#N/A", why="S104 is in A2:A5, so the lookup succeeds."),
        ], steps=[
            S("Find the value", text="S104 is the 4th item in A2:A5."),
            S("Return the matching item", text="The 4th item of D2:D5 is 60000."),
        ], concept="XLOOKUP basics", skill="Application",
           hint="Find S104 in the lookup array, then read the item in the same position of the return array.",
           feedback="XLOOKUP returns from the return_array at the matching position."),
        MC(_FEES + "Cell G2 contains S999. What does =XLOOKUP(G2, A2:A5, B2:B5, \"Not found\") display?", [
            C("Not found", correct=True),
            C("#N/A", why="#N/A appears only when the if_not_found argument is left out. Here it is given as \"Not found\"."),
            C("Ewane Joy", why="XLOOKUP uses an exact match by default; it does not return the last or nearest item."),
            C("0", why="A failed lookup does not return zero; it returns the if_not_found value."),
        ], steps=[
            S("Search", text="S999 is not in A2:A5."),
            S("if_not_found", text="The fourth argument is shown instead of the #N/A error: Not found."),
        ], concept="XLOOKUP if_not_found argument", skill="Application",
           hint="What is the purpose of the fourth argument of XLOOKUP?",
           feedback="The if_not_found argument replaces the #N/A error with a friendly message."),
        NUM(_FEES + "What does =MATCH(\"S103\", A2:A5, 0) return?", 3, steps=[
            S("Count positions in the range", text="S101 is 1, S102 is 2, S103 is 3."),
            S("Result", text="MATCH returns the position 3, not the row number 4."),
        ], concept="MATCH returns a position", skill="Application",
           hint="MATCH counts from the first cell of the range given, not from row 1 of the sheet."),
        MC("Monthly sales are in A1:D4: months Jan, Feb, Mar in B1:D1 and branches Bafoussam, Dschang, Mbouda in A2:A4. Which cell does =INDEX(B2:D4, 3, 2) return?", [
            C("C4 (Mbouda, Feb)", correct=True),
            C("D3 (Dschang, Mar)", why="This swaps the row and column numbers. The second argument is the row, the third is the column."),
            C("B3", why="This counts row 3 and column 2 from A1 instead of from the first cell of the array, B2."),
            C("C3 (Dschang, Feb)", why="Row 3 of B2:D4 is sheet row 4 (Mbouda), not sheet row 3."),
        ], steps=[
            S("Row 3 of B2:D4", text="B2:D4 starts at row 2, so its 3rd row is sheet row 4: Mbouda."),
            S("Column 2 of B2:D4", text="Its 2nd column is column C: Feb."),
            S("Cell", text="C4."),
        ], concept="Two-way INDEX and MATCH", skill="Interpretation",
           hint="Count rows and columns from the top-left cell of the array, B2.",
           feedback="INDEX positions are relative to the array, not to the sheet."),
        MC("In H2 a bursar types =XLOOKUP(G2, A2:A401, D2:D401, \"Not found\") with ordinary relative references, then copies it down to H40. What goes wrong, and what is the fix?", [
            C("The ranges shift down as the formula is copied, so some records are missed; lock both ranges with absolute references (F4)", correct=True),
            C("Nothing goes wrong: XLOOKUP adjusts its ranges automatically", why="All relative references shift when copied, including XLOOKUP ranges. In H3 the lookup range becomes A3:A402."),
            C("G2 should be made absolute so every row looks up the same ID", why="Each row needs its own ID (G3, G4, ...), so G2 must stay relative. It is the ranges that must be locked."),
            C("The formula must be changed to VLOOKUP before it can be copied", why="VLOOKUP has the same problem with relative ranges; the fix is absolute references."),
        ], steps=[
            S("What happens when copied", text="Relative references move with the formula: one row down, A2:A401 becomes A3:A402, so S101 is no longer searched."),
            S("Fix", text="Make the lookup and return ranges absolute (dollar signs before the column letters and row numbers, added with F4), and keep G2 relative."),
        ], concept="Absolute references in copied formulas", skill="Reasoning",
           hint="Which parts of the formula should change from row to row, and which should stay fixed?",
           feedback="Lock the ranges; leave the lookup value relative."),
        MC("A store's sales list has the fields Date, Branch, Product, Category, Quantity and Amount. The manager wants total sales for each category in each branch, one month at a time. Which pivot table layout is right?", [
            C("Category in Rows, Branch in Columns, Sum of Amount in Values, Date (grouped by month) in Filters", correct=True),
            C("Category in Rows, Branch in Columns, Count of Amount in Values, Date in Filters", why="Count gives the number of sales, not the total amount. Values should use Sum."),
            C("Amount in Rows, Category in Columns, Sum of Branch in Values", why="Branch is text and cannot be summed; Amount is the field to total in Values."),
            C("Date in Rows, Product in Columns, Sum of Quantity in Values", why="This shows quantities by product and date, not total amounts by category and branch."),
        ], steps=[
            S("Group by", text="Category down the side (Rows) and Branch across the top (Columns)."),
            S("Calculate", text="Sum of Amount in Values."),
            S("Select a month", text="Date in Filters, grouped by months, or a slicer."),
        ], concept="Planning a pivot table", skill="Application",
           hint="Decide what goes down the side, what goes across, what is totalled and what is used to pick a month.",
           feedback="Remember to refresh the pivot table when new data is added."),
        NUM("A carpenter makes chairs (profit 4000 FCFA) and tables (profit 9000 FCFA). A chair needs 1 hour and 2 m² of wood; a table needs 3 hours and 2 m² of wood. "
            "Each week there are 30 hours and 36 m² of wood. Solver maximises profit with whole-number variable cells. What is the maximum weekly profit in FCFA?", 102000, unit="FCFA", steps=[
            S("Constraints", math=r"x + 3y \le 30,\quad 2x + 2y \le 36,\quad x, y \ge 0"),
            S("Corner where both constraints are tight", math=r"x + 3y = 30,\ x + y = 18 \Rightarrow y = 6,\ x = 12"),
            S("Compare corner points", math=r"(0, 10): 90\,000;\ (18, 0): 72\,000;\ (12, 6): 4000 \times 12 + 9000 \times 6 = 102\,000"),
        ], concept="Solver: objective, variable cells and constraints", skill="Calculation",
           hint="Write the two constraints, find where they cross, and test the profit at each corner point."),
        MC("The macro FlagWeakMarks from the lesson colours a cell light red if it is numeric and below 10, clears the colour of other numeric cells, and skips empty or text cells. C2:C5 hold 12, 7, \"abs\" and 10. Which cells end up light red?", [
            C("C3 only", correct=True),
            C("C3 and C5", why="The test is cell.Value < 10. 10 is not less than 10, so C5 is cleared, not coloured."),
            C("C3 and C4", why="\"abs\" is text; the IsNumeric test skips it before the comparison."),
            C("None, because the macro stops at the text cell", why="The If statement skips non-numeric cells and the For Each loop carries on to the next cell."),
        ], steps=[
            S("Check each cell", text="12: not below 10, cleared. 7: below 10, light red. \"abs\": not numeric, skipped. 10: not below 10, cleared."),
        ], concept="Reading a VBA macro", skill="Interpretation",
           hint="Apply the two If tests to each cell in turn: is it numeric, and is it less than 10?",
           feedback="For Each visits every cell; the If statements decide what happens to each one."),
    ]))

# ---------------------------------------------------------------------------
# Productivity & Project Management / IT project management
# ---------------------------------------------------------------------------
_ACTS = ("A network project for a cyber café in Garoua has these activities (durations in days): A 2, no predecessor; "
         "B 3, after A; C 4, after A; D 2, after B; E 5, after B and C; F 3, after D and E; G 1, after C. ")

SETS.append(practice_set(
    module="Productivity & Project Management", topic="IT project management",
    title="WBS, critical path and Gantt charts", lesson="it-project-management-wbs-cpm-gantt",
    questions=[
        MC("Which statement best describes a work breakdown structure (WBS)?", [
            C("A hierarchy that splits the project into deliverables and work packages small enough to estimate and assign", correct=True),
            C("A timeline showing when each activity starts and finishes", why="That is a Gantt chart. A WBS lists what must be delivered, not when."),
            C("The longest chain of dependent activities through the project", why="That is the critical path, found with the critical path method."),
            C("A table of earliest and latest start times", why="That is the result of a CPM forward and backward pass."),
        ], steps=[
            S("Purpose of a WBS", text="It breaks the whole project into smaller deliverables until each work package can be estimated, assigned and tracked. The order of work comes from the dependencies, not the WBS."),
        ], concept="Work breakdown structure", skill="Recall",
           hint="A WBS answers the question \"what must be done?\", not \"when?\".",
           feedback="WBS for what, CPM for the order and timing, Gantt chart for the timeline."),
        NUM(_ACTS + "What is the minimum project duration in days?", 14, steps=[
            S("Forward pass", text="A: 0 to 2. B: 2 to 5. C: 2 to 6. D: 5 to 7. E: starts at max(5, 6) = 6, ends 11. G: 6 to 7."),
            S("F", text="F starts at max(7, 11) = 11 and ends at 14."),
            S("Duration", text="The largest earliest finish is 14 days."),
        ], concept="Forward pass and project duration", skill="Calculation",
           hint="Work through the activities in order. An activity with several predecessors must wait for the last of them to finish."),
        MC(_ACTS + "Which activities form the critical path?", [
            C("A, C, E, F", correct=True),
            C("A, B, E, F", why="Path A, B, E, F takes 2 + 3 + 5 + 3 = 13 days, shorter than 14; B has 1 day of float."),
            C("A, C, G", why="This path takes only 7 days. G has 7 days of float."),
            C("E only, because it is the longest activity", why="The critical path is the longest chain of dependent activities, not the single longest activity."),
        ], steps=[
            S("Compare paths", text="A-B-D-F 10, A-B-E-F 13, A-C-E-F 14, A-C-G 7 days."),
            S("Longest path", text="A, C, E, F takes 14 days, equal to the project duration, so those activities have zero float."),
        ], concept="Identifying the critical path", skill="Application",
           hint="Add up the durations along each route from start to finish. Which route is longest?",
           feedback="Zero-float activities form the critical path."),
        NUM(_ACTS + "What is the float, in days, of activity D?", 4, unit="days", steps=[
            S("Earliest start", text="D follows B, which finishes at day 5, so ES = 5."),
            S("Latest start", text="D must finish before F starts at day 11, so LF = 11 and LS = 11 − 2 = 9."),
            S("Float", math=r"\text{Float} = LS - ES = 9 - 5 = 4"),
        ], concept="Float from a backward pass", skill="Calculation",
           hint="Float = latest start − earliest start. Work backwards from F to find D's latest finish."),
        MC(_ACTS + "What is the earliest start of activity E?", [
            C("Day 6", correct=True),
            C("Day 5", why="That takes the smaller earliest finish (B at 5). E must wait for both B and C, so take the larger, C at 6."),
            C("Day 2", why="E cannot start when A finishes; it must wait for both B and C."),
            C("Day 11", why="11 is E's earliest finish (6 + 5), not its earliest start."),
        ], steps=[
            S("Predecessors of E", text="B finishes at day 5 and C at day 6."),
            S("Take the largest", math=r"ES_E = \max(5, 6) = 6"),
        ], concept="Earliest start with several predecessors", skill="Application",
           hint="E needs both B and C finished. Which of them finishes later?",
           feedback="In the forward pass, take the largest earliest finish of the predecessors."),
        MC(_ACTS + "Activity B is delayed so that it takes 6 days instead of 3. What is the new project duration?", [
            C("16 days", correct=True),
            C("14 days", why="B has only 1 day of float, so a 3-day delay cannot be absorbed completely."),
            C("17 days", why="Only the part of the delay beyond B's float (3 − 1 = 2 days) moves the end date, not all 3 days."),
            C("15 days", why="This subtracts the float twice. B's float of 1 day absorbs 1 day of the delay, leaving 2 days."),
        ], steps=[
            S("New forward pass", text="B now ends at day 8, so E starts at max(8, 6) = 8 and ends at 13. D ends at 10."),
            S("End of project", text="F starts at max(10, 13) = 13 and ends at 16."),
        ], concept="Effect of delays on the critical path", skill="Reasoning",
           hint="Compare the delay with B's float. Only the excess delays the project.",
           feedback="B becomes critical and the critical path changes to A, B, E, F."),
        MC("On a Gantt chart, the official handover of a new computer lab is shown as a diamond with no length. What does this represent?", [
            C("A milestone: a zero-duration event marking an important point", correct=True),
            C("Float: the time an activity can be delayed", why="Float is usually shown as a dotted extension of a bar, not a diamond."),
            C("A critical activity lasting one day", why="A one-day activity is drawn as a short bar; a diamond has no duration."),
            C("A dependency between two activities", why="Dependencies are shown as arrows or links between bars, not diamonds."),
        ], steps=[
            S("Gantt chart symbols", text="Bars show activities, dotted extensions show float and diamonds show milestones."),
        ], concept="Reading a Gantt chart", skill="Interpretation",
           hint="Which project item has no duration but marks an important moment?",
           feedback="Milestones such as handover are events, not activities."),
        MC("Midway through a lab project, the school asks for 20 extra computers to be installed. According to the scope, time and cost constraints, what is the most likely effect?", [
            C("The project will need more time, more money, or both", correct=True),
            C("Nothing changes, because scope is separate from time and cost", why="The three constraints are linked: increasing scope affects time and cost."),
            C("The project will finish sooner, because more computers can be set up in parallel", why="Extra work without extra resources cannot shorten the project."),
            C("Only the WBS changes; the schedule and budget stay fixed", why="Adding work packages to the WBS adds activities to the schedule and items to the budget."),
        ], steps=[
            S("Scope increases", text="More computers mean more work packages."),
            S("Effect", text="The extra work needs more time, more cost, or both, unless something else is cut."),
        ], concept="Scope, time and cost constraints", skill="Reasoning",
           hint="If one corner of the scope-time-cost triangle grows, what happens to the others?",
           feedback="Changing one constraint affects the other two."),
    ]))
