"""A Level Computer Science (795), Lower Sixth: deeper lessons for Operating Systems & Translators,
Networks & Software Engineering and Procedural Programming, plus the Lower Sixth practice paper lesson.

KKEVO draft material for review. Every trace table, Gantt chart, page-fault count, subnet and CRC
calculation was produced or checked by running a program. Check the real syllabus for the exact
scope of each topic.
"""
from .dsl import *  # noqa: F403

COURSE = ("computer-science", "lower-sixth")

OS = "Operating Systems & Translators"
NET = "Networks & Software Engineering"
PROC = "Procedural Programming"
EXAM = "Examination"

LESSONS = []


# ================================================================== Process management
LESSONS.append(lesson(
    module=OS, topic="Process management",
    title="FCFS and SJF scheduling with arrival times",
    slug="csb-fcfs-sjf-scheduling",
    minutes=22,
    summary="Draw Gantt charts for first come first served, shortest job first and shortest remaining time first when processes arrive at different times, and compare their waiting and turnaround times.",
    objectives=[
        "Explain why an operating system needs a scheduler and define burst, arrival, waiting and turnaround time",
        "Draw a Gantt chart for FCFS and non-preemptive SJF with different arrival times",
        "Calculate average waiting time and average turnaround time",
        "Describe the convoy effect, starvation and how preemptive SRTF differs from SJF",
    ],
    key_concepts=["Scheduler", "Burst time", "Waiting time", "Turnaround time", "FCFS", "SJF", "SRTF", "Convoy effect", "Starvation"],
    blocks=[
        H("Introduction"),
        T("At a busy mobile money kiosk in Bafoussam one agent serves many customers. She must decide who is served next. "
          "A computer has the same problem: many programs want the CPU, but one core can run only one at a time. "
          "The part of the operating system that chooses is the **scheduler**."),
        T("The overview lesson showed basic Gantt charts. Here we go deeper: processes that **arrive at different times**, "
          "a preemptive version of SJF, and the weaknesses of each rule."),
        H("Terms you must use exactly"),
        D("**Arrival time**: when the process enters the ready queue. **Burst time**: the CPU time the process needs. "
          "**Completion time**: when it finishes. For each process:", title="Definitions",
          formula=r"\text{turnaround} = \text{completion} - \text{arrival} \qquad \text{waiting} = \text{turnaround} - \text{burst}"),
        T("Waiting time is the time spent in the ready queue, not running. Turnaround time is the whole time in the system. "
          "Lower averages mean a better experience for the users."),
        KEY("Three rules", "Each rule chooses the next process from the ready queue in a different way.",
            cards=[["FCFS", "Run in order of arrival. Never preempts. Simple, but one long job makes short ones wait."],
                   ["SJF", "Run the ready process with the smallest burst. Non-preemptive: a running job always finishes."],
                   ["SRTF", "Preemptive SJF: a new process whose burst is smaller than the time the running process still needs takes the CPU."]]),
        H("The data"),
        CODE("""
Process   Arrival   Burst (ms)
P1        0         6
P2        1         8
P3        2         2
P4        3         4
""", "text", title="Data used in all three examples"),
        EX("Worked example 1: FCFS", intro="Draw the Gantt chart and find the average waiting and turnaround times.", steps=[
            S("Order by arrival", text="P1, P2, P3, P4. Each starts when the CPU is free and the process has arrived."),
            S("Gantt chart", text="P1 runs 0 to 6, P2 6 to 14, P3 14 to 16, P4 16 to 20."),
            S("Turnaround = completion - arrival", text="P1: 6 - 0 = 6. P2: 14 - 1 = 13. P3: 16 - 2 = 14. P4: 20 - 3 = 17. Average = 50 / 4 = 12.5 ms."),
            S("Waiting = turnaround - burst", text="P1: 0. P2: 13 - 8 = 5. P3: 14 - 2 = 12. P4: 17 - 4 = 13. Average = 30 / 4 = 7.5 ms."),
        ]),
        IMG("al-csb-gantt-compare.svg",
            "Three Gantt charts on a time axis from 0 to 20 ms. FCFS: P1 0-6, P2 6-14, P3 14-16, P4 16-20. SJF: P1 0-6, P3 6-8, P4 8-12, P2 12-20. SRTF: P1 0-2, P3 2-4, P1 4-8, P4 8-12, P2 12-20.",
            caption="Figure 1. The same four processes under FCFS, SJF and SRTF."),
        CODE("""
FCFS
| P1          | P2                | P3  | P4      |
0             6                   14    16        20
Waiting:    P1 0, P2 5, P3 12, P4 13    average 30/4 = 7.5
Turnaround: 6, 13, 14, 17               average 50/4 = 12.5

SJF (non-preemptive)
| P1          | P3  | P4      | P2                |
0             6     8         12                  20
Waiting:    P1 0, P2 11, P3 4, P4 5     average 20/4 = 5.0
Turnaround: 6, 19, 6, 9                 average 40/4 = 10.0

SRTF (preemptive)
| P1  | P3  | P1      | P4      | P2                |
0     2     4         8         12                  20
Waiting:    P1 2, P2 11, P3 0, P4 5     average 18/4 = 4.5
Turnaround: 8, 19, 2, 9                 average 38/4 = 9.5
""", "text", title="Results (each checked with a short program)"),
        EX("Worked example 2: SJF, step by step", intro="Why does P3 run at time 6 and not P2?", steps=[
            S("Time 0", text="Only P1 has arrived, so P1 starts. Non-preemptive: nobody can stop it, even though shorter jobs arrive at times 2 and 3."),
            S("Time 6", text="P1 finishes. The ready queue holds P2 (8), P3 (2) and P4 (4). The smallest burst is P3, so P3 runs 6 to 8."),
            S("Time 8", text="Ready: P2 (8) and P4 (4). P4 is shorter, so it runs 8 to 12. Last, P2 runs 12 to 20."),
            S("Result", text="P2 has the longest burst, so it waits 11 ms. Average waiting time falls from 7.5 ms (FCFS) to 5.0 ms."),
        ]),
        EX("Worked example 3: SRTF preempts", intro="Explain the decisions at times 1, 2 and 4 under SRTF.", steps=[
            S("Time 1", text="P2 arrives with burst 8. P1 still needs 5. Since 8 is more than 5, P1 continues."),
            S("Time 2", text="P3 arrives with burst 2. P1 still needs 4. Since 2 is less than 4, P3 **preempts** P1 and runs 2 to 4."),
            S("Time 4", text="P3 is done. P1 needs 4, P4 needs 4 and P2 needs 8. P1 and P4 tie; a common tie-break is the earlier arrival, so P1 resumes."),
            S("Why the average is lowest", text="When burst times are known, SRTF gives the smallest possible average waiting time, because it always runs the shortest remaining work."),
        ]),
        H("Weaknesses"),
        T("**Convoy effect** (FCFS): one long process at the front makes many short processes wait behind it, like a lorry on a narrow road "
          "with taxis queuing behind. CPU and input/output devices end up idle in turn."),
        T("**Starvation** (SJF and SRTF): if short jobs keep arriving, a long job may wait for ever. A remedy is **ageing**: the longer a process waits, "
          "the more its priority is increased."),
        T("**Unknown burst time**: a real operating system cannot know how long a job will run. It estimates from history, for example "
          "next estimate = 0.5 × last real burst + 0.5 × last estimate. If the last estimate was 10 ms and the last real burst was 6 ms, "
          "the next estimate is 0.5 × 6 + 0.5 × 10 = 8 ms."),
        H("Common mistakes"),
        MISTAKE("Choosing a process that has not arrived", "A process cannot be chosen before its arrival time. If the CPU is free and nothing has arrived, the CPU is idle until the next arrival."),
        MISTAKE("Forgetting arrival time in waiting time", "Waiting time is completion - arrival - burst, not completion - burst. A process arriving at time 3 cannot have waited since time 0."),
        MISTAKE("Calling SJF preemptive", "Plain SJF never interrupts a running process. The preemptive version has its own name, SRTF (shortest remaining time first)."),
        QUIZ("In non-preemptive SJF, a process with burst 2 arrives while a process with 7 ms still to run is on the CPU. What happens?",
             ["The new process preempts at once", "The running process continues to completion, then the shorter one is chosen next",
              "The new process is rejected", "Both run at the same time on one core"], 1,
             "Non-preemptive means the running process is never interrupted. The scheduler compares burst times only when the CPU becomes free.",
             hint="Which version of the rule is allowed to interrupt?",
             feedback=["That is SRTF, the preemptive version.", "", "Nothing is rejected; it waits in the ready queue.", "One core runs one process at a time."]),
        QUIZ("Which problem is solved by ageing?",
             ["Convoy effect", "Starvation of long processes", "Deadlock", "Page faults"], 1,
             "Ageing raises the priority of a process the longer it waits, so a long job is not postponed for ever.",
             feedback=["The convoy effect is a FCFS weakness; ageing does not address it.", "", "Deadlock is about resources held in a cycle.", "Page faults belong to memory management."]),
        H("Practice questions"),
        PQ("Three processes: A (arrival 0, burst 3), B (arrival 1, burst 5), C (arrival 2, burst 1). Draw the FCFS Gantt chart and calculate the average waiting time. [4 marks]",
           "Chart: A 0-3, B 3-8, C 8-9. Waiting time = completion - arrival - burst: A = 3 - 0 - 3 = 0; B = 8 - 1 - 5 = 2; C = 9 - 2 - 1 = 6. Average = (0 + 2 + 6) / 3 = 8 / 3, which is 2.67 ms."),
        PQ("Using the same processes, apply non-preemptive SJF. Give the order of execution and the average waiting time. [4 marks]",
           "At time 0 only A has arrived, so A runs 0-3. At time 3, B (5) and C (1) are waiting; C is shorter so C runs 3-4, then B runs 4-9. Waiting: A 0; B = 9 - 1 - 5 = 3; C = 4 - 2 - 1 = 1. Average = 4 / 3 = 1.33 ms."),
        PQ("Explain the convoy effect and say which scheduling rule suffers from it. [3 marks]",
           "FCFS suffers (1). A long process at the front of the queue holds the CPU while many short processes wait behind it (1), so average waiting time rises and devices may sit idle (1)."),
        PQ("Give one advantage and one disadvantage of SRTF compared with FCFS. [2 marks]",
           "Advantage: gives the lowest average waiting time for known burst times and favours short jobs (1). Disadvantage: long processes may starve, burst times must be predicted, and preemption adds context-switch overhead (1)."),
        SUM("Waiting time = turnaround - burst; turnaround = completion - arrival.",
            "FCFS is simple but suffers from the convoy effect.",
            "SJF gives a lower average waiting time but needs burst times and can starve long jobs.",
            "SRTF is SJF with preemption: a new process with less work than the remaining time takes the CPU.",
            "Ageing prevents starvation. Always check which processes have arrived before choosing.",
            "Exam link: Paper 2 structured questions often ask for a Gantt chart and averages; Paper 1 may test definitions."),
    ],
))


LESSONS.append(lesson(
    module=OS, topic="Process management",
    title="Round Robin scheduling and the time quantum",
    slug="csb-round-robin-scheduling",
    minutes=22,
    summary="Trace Round Robin scheduling with arrival times, draw the ready queue and Gantt chart, and explain how the size of the time quantum affects response time, waiting time and context-switch overhead.",
    objectives=[
        "Explain how Round Robin shares the CPU using a time quantum and a circular ready queue",
        "Trace Round Robin for processes with different arrival times and draw the Gantt chart",
        "Calculate waiting, turnaround and response time",
        "Explain the effect of a very small and a very large quantum, including context-switch overhead",
    ],
    key_concepts=["Round Robin", "Time quantum", "Ready queue", "Context switch", "Response time", "Time sharing"],
    blocks=[
        H("Introduction"),
        T("A teacher in Limbe has four students who each need help with a program. If she helps one student for a full hour "
          "the others wait and may lose interest. Instead she gives each student five minutes, then moves to the next, and goes round again. "
          "Everyone gets quick attention. This is **Round Robin** scheduling, the basis of time-sharing systems."),
        H("How Round Robin works"),
        D("**Round Robin (RR)** is a preemptive scheduling rule. Each process runs for at most one **time quantum**. "
          "If it is not finished, it is preempted and placed at the back of the ready queue. The CPU then goes to the process at the front.",
          title="Definition: Round Robin"),
        D("A **context switch** saves the state of the running process (registers, program counter) and loads the state of the next one. "
          "It is useful work for nobody, so it is **overhead**.", title="Definition: context switch"),
        KEY("Rules to follow when tracing", "Do the same thing every time and state your convention.",
            cards=[["Queue order", "A process that arrives while another is running joins the back of the queue before the preempted process is put back (the convention used here)."],
                   ["Short bursts", "A process that needs less than a full quantum leaves the CPU early. The next process starts at once."],
                   ["Finished", "A finished process is not put back in the queue."]]),
        CODE("""
Process   Arrival   Burst (ms)
P1        0         5
P2        1         4
P3        2         2
P4        4         1
""", "text", title="Data for the worked examples"),
        EX("Worked example 1: quantum = 2 ms", intro="Trace the ready queue and draw the Gantt chart.", steps=[
            S("Time 0 to 2", text="Queue holds P1 only. P1 runs 2 ms (3 left). P2 (time 1) and P3 (time 2) have arrived, so the queue is P2, P3, P1."),
            S("Time 2 to 4", text="P2 runs 2 ms (2 left). P4 arrives at time 4 and joins before P2: queue P3, P1, P4, P2."),
            S("Time 4 to 9", text="P3 runs 4-6 and finishes. P1 runs 6-8 (1 left). P4 runs 8-9 and finishes (it needed only 1 ms). Queue: P2, P1."),
            S("Time 9 to 12", text="P2 runs 9-11 and finishes. P1 runs 11-12 and finishes."),
        ]),
        CODE("""
Quantum = 2 ms
| P1 | P2 | P3 | P1 | P4 | P2 | P1 |
0    2    4    6    8    9    11   12

Process  Finish  Turnaround  Waiting  First run  Response
P1       12      12          7        0          0
P2       11      10          6        2          1
P3       6       4           2        4          2
P4       9       5           4        8          4
Average waiting time    = 19 / 4 = 4.75 ms
Average turnaround time = 31 / 4 = 7.75 ms
Average response time   = 7 / 4 = 1.75 ms
""", "text", title="Round Robin, quantum 2 ms (checked with a program)"),
        T("**Response time** = the time from arrival to the first time the process gets the CPU. It matters most for interactive users."),
        EX("Worked example 2: quantum = 4 ms", intro="Repeat with a larger quantum and compare.", steps=[
            S("Gantt chart", text="P1 0-4 (1 left). Queue after: P2, P3, P4, P1. P2 runs 4-8 and finishes. P3 8-10 finishes. P4 10-11 finishes. P1 11-12 finishes."),
            S("Waiting times", text="P1 = 12 - 0 - 5 = 7. P2 = 8 - 1 - 4 = 3. P3 = 10 - 2 - 2 = 6. P4 = 11 - 4 - 1 = 6. Average = 22 / 4 = 5.5 ms."),
            S("Response times", text="P1 0, P2 3, P3 6, P4 6. Average = 15 / 4 = 3.75 ms."),
            S("Compare with FCFS", text="FCFS gives average waiting 4.5 ms and average response 4.5 ms for this data. With a quantum of 5 or more, RR behaves exactly like FCFS."),
        ]),
        IMG("al-csb-rr-quantum.svg",
            "Two Gantt charts for the same four processes. With quantum 2: P1, P2, P3, P1, P4, P2, P1 finishing at time 12. With quantum 4: P1, P2, P3, P4, P1 finishing at time 12.",
            caption="Figure 1. A smaller quantum means more switches between processes."),
        H("Choosing the quantum"),
        KEY("The quantum is a trade-off", "There is no best value for every system.",
            cards=[["Too large", "Each process runs to completion in its first turn. RR becomes FCFS. Short jobs wait behind long ones and response time is poor."],
                   ["Too small", "Responsive, but the CPU spends a large share of its time on context switches."],
                   ["Rule of thumb", "Most processes should finish their CPU burst within one or two quanta, but the quantum should be much longer than a context switch."]]),
        EX("Worked example 3: overhead", intro="A context switch takes 1 ms. Compare quantum = 2 ms with quantum = 20 ms for processes that always use their whole quantum.", steps=[
            S("Useful fraction", text="Each turn costs quantum + switch."),
            S("Quantum 2 ms", text="Overhead = 1 / (2 + 1) = 1 / 3, about 33 percent of CPU time wasted."),
            S("Quantum 20 ms", text="Overhead = 1 / (20 + 1) = 1 / 21, about 4.8 percent."),
            S("Conclusion", text="A bigger quantum wastes less time on switching but raises the waiting time for short jobs. The designer balances the two."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying RR always gives the lowest waiting time", "RR improves response time. In the example above FCFS had a lower average waiting time (4.5 ms) than RR with quantum 4 (5.5 ms). Always calculate."),
        MISTAKE("Putting a process back before the new arrival", "Decide the convention and apply it consistently. A process arriving exactly when another is preempted goes first in this lesson. Exam questions normally state a convention or give data that avoids a clash."),
        MISTAKE("Using the full quantum for a short process", "If a process needs 1 ms and the quantum is 4 ms, it runs 1 ms and the next process starts at once."),
        QUIZ("A very large time quantum makes Round Robin behave like which rule?",
             ["SJF", "FCFS", "SRTF", "Priority scheduling"], 1,
             "If every process finishes within its first quantum, no preemption ever happens and processes run in arrival order: FCFS.",
             feedback=["SJF chooses by burst time; RR never does.", "", "SRTF chooses by remaining time.", "RR has no priorities."]),
        QUIZ("A context switch takes 2 ms. The quantum is 8 ms. What fraction of the time is spent on switching, if every process uses its full quantum?",
             ["20 percent", "25 percent", "80 percent", "2 percent"], 0,
             "Each cycle is 8 + 2 = 10 ms, of which 2 ms is switching: 2 / 10 = 20 percent.",
             hint="The cycle length is quantum plus switch.",
             feedback=["", "2 / 8 divides by the quantum only, not by the whole cycle.", "That is the useful fraction, not the overhead.", "That is just the 2 ms, not a percentage."]),
        H("Practice questions"),
        PQ("Three processes arrive at time 0: A (burst 10), B (burst 4), C (burst 2). Draw the Round Robin Gantt chart with quantum 3 ms. At what time does each process finish? [4 marks]",
           "A 0-3, B 3-6, C 6-8 (C finishes at 8), A 8-11, B 11-12 (B finishes at 12), A 12-15, A 15-16 (A finishes at 16). Finish times: C 8, B 12, A 16."),
        PQ("Using the same processes, find the average waiting time for Round Robin (quantum 3 ms) and for FCFS (order A, B, C). Which is lower? [4 marks]",
           "RR waiting = finish - burst: A 16 - 10 = 6, B 12 - 4 = 8, C 8 - 2 = 6. Average = 20 / 3 = 6.67 ms. FCFS: A waits 0, B waits 10, C waits 14, average = 24 / 3 = 8 ms. RR is lower here because the short jobs B and C are no longer stuck behind A for its whole 10 ms."),
        PQ("Explain what happens to system performance if the time quantum is made very small. [3 marks]",
           "The CPU switches between processes very often (1). Each context switch takes time in which no user work is done, so overhead is high (1). Response time looks good but throughput falls (1)."),
        PQ("Why is Round Robin suitable for a multi-user time-sharing system? [2 marks]",
           "Every user's process gets a regular turn of the CPU (1), so no user waits long for a first response and no process can monopolise the CPU (1)."),
        SUM("Round Robin gives each process a time quantum, then sends it to the back of the ready queue.",
            "Trace the queue at every step; state which convention you use for a simultaneous arrival.",
            "Response time = first CPU time - arrival time; RR improves it, but not always the average waiting time.",
            "A huge quantum turns RR into FCFS; a tiny quantum wastes time on context switches.",
            "Overhead fraction = switch time / (quantum + switch time).",
            "Exam link: Paper 2 often asks for an RR Gantt chart and averages; Paper 1 asks about the quantum."),
    ],
))


LESSONS.append(lesson(
    module=OS, topic="Process management",
    title="Race conditions, critical sections and semaphores",
    slug="csb-semaphores-mutual-exclusion",
    minutes=24,
    summary="See how two processes updating shared data can lose an update (a race condition), and how binary and counting semaphores with wait and signal give mutual exclusion and solve the producer-consumer problem.",
    objectives=[
        "Explain a race condition and a critical section with an interleaving trace",
        "State the requirements for a correct solution: mutual exclusion, progress and bounded waiting",
        "Use wait and signal on a binary semaphore (mutex) and a counting semaphore",
        "Trace the bounded-buffer producer-consumer problem with empty, full and mutex semaphores",
    ],
    key_concepts=["Race condition", "Critical section", "Mutual exclusion", "Semaphore", "wait and signal", "Mutex", "Producer-consumer"],
    blocks=[
        H("Introduction"),
        T("Two cashiers at a cooperative bank in Ngaoundéré each serve a customer paying into the same account at the same moment. "
          "Each reads the balance, adds the deposit, and writes the new balance back. If both read before either writes, one deposit is lost."),
        T("Processes share data in the same way. The result must not depend on who happens to run first. "
          "This lesson shows the fault and the standard tool that prevents it."),
        H("The race condition"),
        D("A **race condition** is a fault in which the result depends on the exact order in which processes access shared data. "
          "The part of a program that accesses the shared data is the **critical section**.", title="Definition: race condition and critical section"),
        T("Adding to a variable is not one step for the CPU. It is three: LOAD the value into a register, ADD, then STORE the register back. "
          "A process can be preempted between any two of these steps."),
        CODE("""
Shared balance = 100. Cashier A and cashier B each deposit 50.
Bad interleaving (found by running a simulation):

step  who  action                 register  balance
1     A    LOAD balance           100       100
2     B    LOAD balance           100       100
3     A    ADD 50                 150       100
4     B    ADD 50                 150       100
5     A    STORE balance          150       150
6     B    STORE balance          150       150

Final balance = 150, but it should be 200. One deposit is lost.
""", "text", title="A lost update"),
        KEY("What a correct solution needs", "Any method for protecting a critical section must satisfy three requirements.",
            cards=[["Mutual exclusion", "At most one process is inside the critical section at a time."],
                   ["Progress", "If no process is inside and some want to enter, one of them must be allowed in without long delay. A process outside the section cannot block others."],
                   ["Bounded waiting", "A process that wants to enter must not be postponed for ever while others keep entering."]]),
        H("Semaphores"),
        D("A **semaphore** is a protected integer variable that can be changed only by two **atomic** operations (they cannot be interrupted part-way): "
          "**wait(S)**: if S is greater than 0, subtract 1 and carry on; otherwise the process blocks until S becomes positive. "
          "**signal(S)**: add 1 to S (waking a blocked process if there is one).", title="Definition: semaphore"),
        T("A **binary semaphore** (also called a **mutex** when used for locking) has values 0 or 1. A **counting semaphore** starts at the number of "
          "identical resources, such as 3 free parking bays or 5 slots in a buffer."),
        CODE("""
S = 1                      # binary semaphore, shared by A and B

process A:                 process B:
    wait(S)                    wait(S)
    LOAD balance               LOAD balance
    ADD 50                     ADD 50
    STORE balance              STORE balance
    signal(S)                  signal(S)
""", "text", title="Protecting the critical section"),
        EX("Worked example 1: the mutex in action", intro="A and B both try to deposit. Follow S.", steps=[
            S("A calls wait(S)", text="S is 1, so it becomes 0 and A enters the critical section."),
            S("B calls wait(S)", text="S is 0, so B **blocks**. It uses no CPU time while it waits."),
            S("A finishes and calls signal(S)", text="A blocked process exists, so B is woken and enters. S stays 0 for B."),
            S("B finishes and calls signal(S)", text="Nobody is waiting, so S becomes 1 again. The balance is 100 + 50 + 50 = 200."),
        ]),
        CODE("""
import threading

mutex = threading.Semaphore(1)
balance = 0

def deposit():
    global balance
    for _ in range(100000):
        mutex.acquire()        # wait(mutex)
        balance += 1           # critical section
        mutex.release()        # signal(mutex)

ts = [threading.Thread(target=deposit) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print("balance", balance)

# Output (run):
# balance 200000
""", "python", title="The same idea in Python threads"),
        H("Producer and consumer"),
        T("A **producer** puts items in a shared buffer; a **consumer** takes them out. The buffer holds at most N items. "
          "The producer must wait if the buffer is full; the consumer must wait if it is empty. Three semaphores solve it: "
          "**empty** (free slots, starts at N), **full** (filled slots, starts at 0) and **mutex** (protects the buffer, starts at 1)."),
        CODE("""
producer:                      consumer:
  wait(empty)                    wait(full)
  wait(mutex)                    wait(mutex)
  put item in buffer             take item from buffer
  signal(mutex)                  signal(mutex)
  signal(full)                   signal(empty)
""", "text", title="Bounded buffer"),
        EX("Worked example 2: buffer of 2 slots", intro="Trace empty, full and the buffer.", steps=[
            S("Start", text="empty = 2, full = 0, buffer empty."),
            S("Producer makes item 1 then item 2", text="empty goes 2 to 1 to 0; full goes 0 to 1 to 2; buffer holds 1, 2."),
            S("Producer wants item 3", text="wait(empty) with empty = 0: the producer **blocks**. The buffer is full."),
            S("Consumer takes item 1", text="wait(full) makes full = 1. signal(empty) wakes the producer. Buffer holds 2."),
            S("Producer adds item 3", text="empty back to 0, full to 2. The buffer holds 2, 3."),
            S("Check", text="empty + full = 2 = N whenever no process is in the middle of an operation. This invariant shows the counts are consistent."),
        ]),
        H("Common mistakes"),
        MISTAKE("Reversing wait and signal", "Using signal first makes the semaphore larger than it should be, so two processes can enter the critical section at once. Always wait before, signal after."),
        MISTAKE("Forgetting to signal", "If a process leaves the critical section without calling signal, every other process blocks for ever."),
        MISTAKE("Taking the mutex before empty in the producer", "If the producer holds mutex and then waits on empty, the consumer cannot get mutex to free a slot. Both stop: a deadlock. Wait on empty or full first, then mutex."),
        MISTAKE("Thinking a semaphore wait keeps the CPU busy", "A blocked process is moved out of the ready queue and uses no CPU. This is different from a busy-wait loop."),
        QUIZ("A binary semaphore S = 1. Process A calls wait(S), then process B calls wait(S). What is the state?",
             ["A and B are both in the critical section", "A is in; B is blocked; S = 0", "B is in; A is blocked; S = 1", "Both are blocked; S = 0"], 1,
             "A's wait changes S from 1 to 0 and A enters. B's wait finds S = 0 and blocks.",
             feedback=["That would break mutual exclusion; the semaphore prevents it.", "", "A called wait first.", "A is not blocked: it found S = 1."]),
        QUIZ("A counting semaphore starts at 3 for three free parking bays. Four cars arrive in turn and each does wait(S). What happens to the fourth?",
             ["It parks, and S becomes -1 in the display", "It blocks until a car leaves and does signal(S)", "It parks in a bay already used", "It is discarded"], 1,
             "After three waits S = 0. The fourth finds S = 0 and blocks until a signal.",
             feedback=["The value is not decreased when the process blocks.", "", "That would break the limit of three.", "Blocked processes are kept and woken, not discarded."]),
        H("Practice questions"),
        PQ("Explain what is meant by a race condition, using a bank balance as an example. [3 marks]",
           "Two processes read and update the same data and the result depends on the order of their steps (1). Example: both read a balance of 100 before either stores, each adds 50 and stores 150 (1). One update is lost; the correct balance 200 is not reached (1)."),
        PQ("State the three requirements for a solution to the critical section problem. [3 marks]",
           "Mutual exclusion: only one process in the critical section (1). Progress: if the section is free and processes want to enter, one is chosen without unnecessary delay (1). Bounded waiting: no process waits indefinitely (1)."),
        PQ("A buffer holds 3 items. Give the initial values of the semaphores empty, full and mutex for a producer-consumer solution, and say what each one is for. [3 marks]",
           "empty = 3: counts free slots, so the producer blocks when the buffer is full (1). full = 0: counts filled slots, so the consumer blocks when the buffer is empty (1). mutex = 1: ensures only one process changes the buffer at a time (1)."),
        PQ("Why must wait and signal be atomic? [2 marks]",
           "If they could be interrupted part-way, two processes might both read S = 1 before either changes it (1), so both would enter the critical section and mutual exclusion would fail (1)."),
        SUM("A race condition makes the result depend on the order of steps; a critical section is the code that touches shared data.",
            "Correct solutions give mutual exclusion, progress and bounded waiting.",
            "wait(S) decrements or blocks; signal(S) increments or wakes a waiter. Both are atomic.",
            "A mutex is a binary semaphore starting at 1; a counting semaphore starts at the number of resources.",
            "Producer-consumer uses empty = N, full = 0 and mutex = 1, with empty or full waited on before mutex.",
            "Exam link: Paper 2 may ask you to define terms and trace semaphore values; Paper 1 tests definitions."),
    ],
))


LESSONS.append(lesson(
    module=OS, topic="Process management",
    title="Deadlock: conditions, graphs, prevention and avoidance",
    slug="csb-deadlock-conditions-and-banker",
    minutes=24,
    summary="State the four conditions for deadlock, detect it with a resource allocation or wait-for graph, and explain prevention, avoidance (the safe-state idea of the Banker's algorithm), detection and recovery.",
    objectives=[
        "Define deadlock and state the four necessary conditions",
        "Read a resource allocation graph and find a cycle that shows deadlock",
        "Explain how breaking each condition prevents deadlock, including resource ordering",
        "Decide whether a state is safe and whether a request should be granted (single resource Banker's idea)",
    ],
    key_concepts=["Deadlock", "Mutual exclusion", "Hold and wait", "No preemption", "Circular wait", "Safe state", "Banker's algorithm", "Starvation"],
    blocks=[
        H("Introduction"),
        T("At a narrow bridge near Mamfe two lorries meet in the middle. Neither can reverse, and each waits for the other to move. "
          "Nobody moves for ever. In an operating system, this is **deadlock**."),
        T("Typical case: process P1 holds the scanner and waits for the printer; process P2 holds the printer and waits for the scanner."),
        D("A set of processes is in **deadlock** if every process in the set is waiting for a resource that is held by another process in the set, "
          "so none of them can ever continue.", title="Definition: deadlock"),
        H("The four necessary conditions"),
        T("Deadlock can happen only if **all four** of these hold at the same time."),
        KEY("Coffman conditions", "If you can remove any one of them, deadlock cannot occur.",
            cards=[["1. Mutual exclusion", "A resource can be used by only one process at a time (e.g. a printer)."],
                   ["2. Hold and wait", "A process holds at least one resource while waiting for another."],
                   ["3. No preemption", "A resource cannot be forcibly taken from the process holding it. It is released only voluntarily."],
                   ["4. Circular wait", "There is a cycle of processes: each waits for a resource held by the next, and the last waits for the first."]]),
        H("Resource allocation graphs"),
        T("Draw processes as circles and resources as squares. An arrow from a resource to a process means the resource is **allocated** to it. "
          "An arrow from a process to a resource means the process **requests** it. With one unit of each resource, a **cycle means deadlock**."),
        IMG("al-csb-deadlock-graph.svg",
            "Resource allocation graph. R1 is allocated to P1. R2 is allocated to P2. P1 requests R2. P2 requests R1. The four arrows form a cycle, which shows deadlock.",
            caption="Figure 1. A cycle: P1 holds R1 and wants R2, P2 holds R2 and wants R1."),
        T("A **wait-for graph** removes the resources: draw an arrow from P1 to P2 if P1 is waiting for something P2 holds. Deadlock exists if there is a cycle. "
          "This is easy to check with a program."),
        CODE("""
def find_cycle(graph):
    state, path = {}, []
    def dfs(p):
        state[p] = 1; path.append(p)
        for q in graph.get(p, []):
            if state.get(q) == 1:
                return path[path.index(q):] + [q]
            if q not in state:
                c = dfs(q)
                if c: return c
        state[p] = 2; path.pop()
    for p in graph:
        if p not in state:
            c = dfs(p)
            if c: return c

print(find_cycle({"P1": ["P2"], "P2": ["P1"]}))
print(find_cycle({"P1": ["P2"], "P2": ["P3"], "P3": []}))
print(find_cycle({"P1": ["P2"], "P2": ["P3"], "P3": ["P1"], "P4": ["P1"]}))

# Output (run):
# ['P1', 'P2', 'P1']
# None
# ['P1', 'P2', 'P3', 'P1']
""", "python", title="Detecting a cycle in a wait-for graph"),
        EX("Worked example 1: is there deadlock?", intro="P1 waits for P2, P2 waits for P3, P3 waits for P1, and P4 waits for P1. Which processes are deadlocked?", steps=[
            S("Draw the wait-for graph", text="P1 to P2 to P3 to P1 forms a cycle. P4 points into the cycle."),
            S("Deadlocked", text="P1, P2 and P3 are deadlocked: each waits for another member of the cycle."),
            S("P4", text="P4 is not in the cycle, but it is waiting for P1, which will never finish. It is blocked indefinitely, though not part of the cycle."),
        ]),
        H("Handling deadlock"),
        KEY("Four approaches", "Systems choose one or combine them.",
            cards=[["Prevention", "Design the system so that at least one of the four conditions can never hold."],
                   ["Avoidance", "Allow all four possible, but refuse any request that could lead to an unsafe state (Banker's algorithm)."],
                   ["Detection and recovery", "Let deadlock happen, detect it, then break it by terminating a process or taking resources away."],
                   ["Ignore it", "Used by many general-purpose systems when deadlock is rare: the user restarts the process."]]),
        H("Prevention by breaking a condition"),
        T("**Hold and wait**: require a process to request all its resources at once, or to release what it holds before asking for more. Cost: resources are held longer than needed, and starvation is possible."),
        T("**No preemption**: if a request cannot be satisfied, the process must release what it holds and try again later."),
        T("**Circular wait**: give every resource a number and require processes to request in increasing order only. A cycle would need some process to ask for a lower-numbered resource while holding a higher one, which is not allowed. "
          "This is the most practical method."),
        CODE("""
Resource numbers: scanner = 1, printer = 2

P1:  request scanner (1), then printer (2)   allowed
P2:  request scanner (1), then printer (2)   allowed (same order)
P2:  request printer (2), then scanner (1)   NOT allowed

With the same order for everyone, P1 and P2 can never hold one
resource each while waiting for the other's.
""", "text", title="Resource ordering"),
        H("Avoidance: safe states and the Banker's idea"),
        D("A state is **safe** if there is some order in which every process can be given the rest of what it needs and finish. "
          "That order is a **safe sequence**. An unsafe state does not mean deadlock has happened, only that it may.", title="Definition: safe state"),
        T("The **Banker's algorithm** works like a banker who never lends so much that he cannot satisfy every customer's maximum. "
          "For each request it pretends to grant it, then checks whether a safe sequence still exists. If not, the request waits."),
        EX("Worked example 2: single resource, 12 units", intro=(
            "There are 12 identical units. P0 holds 5 and may need up to 8. P1 holds 2 and may need up to 4. P2 holds 2 and may need up to 9. "
            "Is the state safe?"), steps=[
            S("Available and needs", text="Available = 12 - (5 + 2 + 2) = 3. Remaining need = maximum - held: P0 needs 3, P1 needs 2, P2 needs 7."),
            S("Find a process that can finish", text="P0 needs 3 and 3 are available. P0 runs to completion and returns its 5, so available = 8."),
            S("Continue", text="P1 needs 2 (8 available): finishes, available = 10. P2 needs 7 (10 available): finishes, available = 12."),
            S("Conclusion", text="The sequence P0, P1, P2 lets everyone finish, so the state is **safe**."),
        ]),
        EX("Worked example 3: should a request be granted?", intro="From the safe state above, P2 asks for 2 more units. Should the system grant it?", steps=[
            S("Pretend to grant", text="P2 now holds 4 and needs 5 more. Available = 3 - 2 = 1."),
            S("Look for a process that can finish", text="P0 needs 3 (only 1 available): no. P1 needs 2: no. P2 needs 5: no."),
            S("Conclusion", text="No process can finish, so the new state is unsafe. **Deny the request for now** and make P2 wait. (Asking for only 1 unit would leave a safe state: P1, then P0, then P2.)"),
        ]),
        H("Detection and recovery"),
        T("The system checks regularly for a cycle. To recover it can **terminate** one or all of the processes in the cycle, or **preempt** a resource and roll a process back. "
          "Choosing a victim may depend on priority, work done and the number of resources held."),
        H("Common mistakes"),
        MISTAKE("Saying a cycle always means deadlock", "With several units of a resource, a cycle only shows deadlock is possible. With a single unit of each resource, a cycle is deadlock."),
        MISTAKE("Confusing deadlock with starvation", "In deadlock, processes wait for each other in a cycle. In starvation, a process waits for ever because others are always chosen first, though the system is still making progress."),
        MISTAKE("Equating unsafe with deadlocked", "An unsafe state may still end well if processes happen not to ask for their maximum. Avoidance simply refuses to take the risk."),
        QUIZ("Which condition is broken by numbering resources and requiring requests in increasing order?",
             ["Mutual exclusion", "Hold and wait", "No preemption", "Circular wait"], 3,
             "A cycle would need a process holding a high-numbered resource to ask for a lower one, which the rule forbids.",
             feedback=["The resources are still used by one process at a time.", "Processes may still hold one resource while waiting for another.", "Resources are still not taken away.", ""]),
        QUIZ("A state is unsafe. What does this mean?",
             ["Deadlock has already occurred", "No safe sequence exists, so deadlock may occur", "At least one process has crashed", "Resources are available but unused"], 1,
             "An unsafe state has no order in which all processes can finish with certainty. Deadlock is possible but not certain.",
             feedback=["Unsafe is a warning, not a deadlock.", "", "Crashes are unrelated.", "Unused resources are a different matter."]),
        H("Practice questions"),
        PQ("List the four conditions that must hold for deadlock to occur. [4 marks]",
           "Mutual exclusion (1); hold and wait (1); no preemption (1); circular wait (1)."),
        PQ("Process P1 holds the printer and requests the scanner. Process P2 holds the scanner and requests the printer. Explain why this is a deadlock and suggest how it could be prevented. [4 marks]",
           "Each process holds a resource the other needs and waits for the other's resource (1), so there is a circular wait and neither can continue (1), given the printer and scanner cannot be shared or taken away (1). Prevention: require both processes to request resources in the same fixed order, for example scanner first then printer, which prevents a cycle (1)."),
        PQ("There are 10 identical units. P0 holds 3 and may need up to 7. P1 holds 3 and may need up to 6. P2 holds 2 and may need up to 9. Show whether the state is safe. [4 marks]",
           "Available = 10 - 8 = 2 (1). Remaining needs: P0 4, P1 3, P2 7 (1). No process has need 2 or less, so no process can finish (1). The state is not safe (1)."),
        PQ("Distinguish between deadlock avoidance and deadlock detection. [2 marks]",
           "Avoidance checks each request in advance and refuses it if it would lead to an unsafe state, so deadlock never occurs (1). Detection allows deadlock to happen, then finds it (for example by looking for a cycle) and recovers (1)."),
        SUM("Deadlock needs mutual exclusion, hold and wait, no preemption and circular wait all at once.",
            "A cycle in a resource allocation graph with one unit of each resource shows deadlock.",
            "Prevention removes one condition; resource ordering removes circular wait.",
            "Avoidance (Banker's algorithm) grants a request only if a safe sequence remains.",
            "Detection and recovery lets deadlock occur, then terminates or preempts to break it.",
            "Exam link: Paper 2 asks for the four conditions and graph reading; Paper 1 tests definitions and safe-state ideas."),
    ],
))


# ================================================================== Memory management
LESSONS.append(lesson(
    module=OS, topic="Memory management",
    title="Paging and segmentation: translating addresses",
    slug="csb-paging-segmentation-translation",
    minutes=25,
    summary="Translate logical addresses to physical addresses with a page table and with a segment table, calculate internal fragmentation, effective access time with a TLB, and compare first fit with best fit.",
    objectives=[
        "Split a logical address into page number and offset and use a page table to find the physical address",
        "Translate a segment-offset address using base and limit, and recognise an invalid address",
        "Calculate internal fragmentation and explain external fragmentation",
        "Calculate effective access time with a TLB and compare first fit and best fit",
    ],
    key_concepts=["Logical address", "Physical address", "Page", "Frame", "Page table", "Segment table", "TLB", "Internal fragmentation", "External fragmentation"],
    blocks=[
        H("Introduction"),
        T("In a student hostel in Buea, rooms are numbered the same way on each floor, but the real room is found by the floor key. "
          "A program also uses its own 'room numbers' (logical addresses). The hardware and operating system convert them to real places in the RAM (physical addresses). "
          "This lets many programs share memory safely and lets a program be placed anywhere."),
        H("Paging"),
        D("**Paging** divides the logical address space into fixed-size **pages** and the physical memory into frames of the **same size**. "
          "Any page can be put in any free frame. A **page table** records which frame holds each page.", title="Definition: paging"),
        T("A logical address is split into two parts: the **page number** (which page) and the **offset** (where inside the page). With a page size of 1024 bytes:"),
        F(r"\text{page} = \lfloor L / 1024 \rfloor \qquad \text{offset} = L \bmod 1024 \qquad P = \text{frame} \times 1024 + \text{offset}", title="Address translation"),
        T("The offset is not changed by translation. Only the page number is replaced by a frame number."),
        CODE("""
Page table:   page 0 -> frame 5
              page 1 -> frame 2
              page 2 -> frame 7
              page 3 -> frame 1
              page 4 -> frame 9
Page size 1024 bytes.
""", "text", title="The page table used in the examples"),
        EX("Worked example 1: logical address 3500", intro="Translate logical address 3500 using the page table above.", steps=[
            S("Find page and offset", math=r"3500 = 3 \times 1024 + 428", text="Page 3, offset 428."),
            S("Look up the page table", text="Page 3 is in frame 1."),
            S("Build the physical address", math=r"1 \times 1024 + 428 = 1452"),
        ], check=r"\text{Offset } 428 < 1024 \text{ and frame } 1 \text{ exists}"),
        EX("Worked example 2: logical address 2060", intro="Translate logical address 2060.", steps=[
            S("Page and offset", math=r"2060 = 2 \times 1024 + 12", text="Page 2, offset 12."),
            S("Frame", text="Page 2 is in frame 7."),
            S("Physical address", math=r"7 \times 1024 + 12 = 7180"),
        ]),
        IMG("al-csb-paging-translation.svg",
            "A logical address 3500 is split into page 3 and offset 428. Page 3 is looked up in the page table and gives frame 1. Frame 1 and offset 428 form physical address 1452.",
            caption="Figure 1. Translating logical address 3500 with a page table."),
        CODE("""
PAGE_SIZE = 1024
page_table = {0: 5, 1: 2, 2: 7, 3: 1, 4: 9}

def translate(logical):
    page, offset = divmod(logical, PAGE_SIZE)
    if page not in page_table:
        return "invalid page " + str(page)
    return page_table[page] * PAGE_SIZE + offset

for la in (3500, 2060, 100, 6000):
    print(la, translate(la))

# Output (run):
# 3500 1452
# 2060 7180
# 100 5220
# 6000 invalid page 5
""", "python", title="Page translation in Python"),
        H("Costs of paging"),
        T("**Internal fragmentation**: the last page of a process is rarely full, so some bytes in its frame are wasted. "
          "A process of 72 766 bytes with 2048-byte pages needs 36 pages (35.5 rounded up). It uses 36 x 2048 = 73 728 bytes, so 962 bytes are wasted."),
        T("**Extra memory access**: the page table is in memory, so every access needs two memory reads (table, then data). "
          "A small, fast cache called the **TLB** (translation lookaside buffer) keeps recent page-to-frame mappings."),
        EX("Worked example 3: effective access time", intro="Memory access takes 100 ns, a TLB lookup takes 10 ns, the TLB hit ratio is 80 percent. Find the effective access time.", steps=[
            S("On a hit", text="TLB lookup, then one memory access: 10 + 100 = 110 ns."),
            S("On a miss", text="TLB lookup, page-table read, data read: 10 + 100 + 100 = 210 ns."),
            S("Weighted average", math=r"0.8 \times 110 + 0.2 \times 210 = 88 + 42 = 130 \text{ ns}"),
            S("Improve the hit ratio", text="At 95 percent the result is 0.95 x 110 + 0.05 x 210 = 115 ns, so the TLB matters."),
        ]),
        H("Segmentation"),
        D("**Segmentation** divides a program into logical units of **different sizes**, called segments (for example code, data, stack). "
          "A logical address is a pair (segment number, offset). The **segment table** stores each segment's **base** (start in memory) and **limit** (length).",
          title="Definition: segmentation"),
        T("The hardware checks that the offset is **less than** the limit. If not, the address is invalid and the hardware raises a trap (a segmentation fault). "
          "Otherwise the physical address is base + offset."),
        CODE("""
Segment   Base    Limit
0         2000    1000
1         8000    500
2         3000    200
3         12000   1500
""", "text", title="Segment table"),
        EX("Worked example 4: segment addresses", intro="Translate (1, 53), (2, 200) and (3, 1499).", steps=[
            S("(1, 53)", text="53 is less than the limit 500. Physical address = 8000 + 53 = 8053."),
            S("(2, 200)", text="The limit of segment 2 is 200 and offsets run 0 to 199, so 200 is **not** less than the limit. Trap: invalid address."),
            S("(3, 1499)", text="1499 is less than 1500. Physical address = 12000 + 1499 = 13499."),
        ]),
        T("Segmentation matches the way programmers think and allows sharing and protection per segment. But because segments have different sizes, free memory breaks into many small holes: "
          "**external fragmentation**. The total free space may be enough, but no single hole is big enough."),
        EX("Worked example 5: first fit and best fit", intro="Free holes are 120, 300 and 200 KB (in that order in memory). Requests arrive: 100, 190, 280 KB.", steps=[
            S("First fit (first hole big enough)", text="100 goes in the 120 hole (20 left). 190 goes in the 300 hole (110 left). 280 finds holes of 20, 110, 200: **fails**."),
            S("Best fit (smallest hole big enough)", text="100 goes in 120 (20 left). 190 goes in 200 (10 left). 280 goes in 300 (20 left): **all succeed**."),
            S("Remember", text="Best fit is not always better; it leaves many tiny useless holes. The result depends on the sequence."),
        ]),
        H("Common mistakes"),
        MISTAKE("Changing the offset", "The offset is copied unchanged into the physical address. Only the page number is replaced by the frame number."),
        MISTAKE("Allowing offset equal to the limit", "If the limit is 200, valid offsets are 0 to 199. Offset 200 is a trap."),
        MISTAKE("Mixing the two fragmentations", "Paging wastes space inside the last frame (internal). Segmentation and variable-size allocation leave holes between blocks (external)."),
        QUIZ("Page size 1024. A logical address of 4500 is in which page and offset?",
             ["Page 4, offset 404", "Page 4, offset 500", "Page 5, offset 4", "Page 3, offset 428"], 0,
             "4500 = 4 x 1024 + 404.", feedback=["", "500 is the last digits of the address, not the remainder after dividing by 1024.", "Page 5 would start at 5120.", "428 is the offset of address 3500, not 4500."]),
        QUIZ("Which fragmentation is associated with fixed-size pages?",
             ["External fragmentation", "Internal fragmentation in the last page", "Neither, paging has no fragmentation", "Both equally"], 1,
             "Pages and frames are the same fixed size, so no external holes occur. The unused part of a process's last page is internal fragmentation.",
             feedback=["External holes come from variable-size blocks, such as segments.", "", "Paging avoids external fragmentation but not internal.", "Only internal fragmentation applies."]),
        H("Practice questions"),
        PQ("Using the page table in this lesson (page size 1024), translate logical address 4500 to a physical address. Show your working. [3 marks]",
           "4500 / 1024 = 4 remainder 404, so page 4 and offset 404 (1). Page 4 is in frame 9 (1). Physical address = 9 x 1024 + 404 = 9216 + 404 = 9620 (1)."),
        PQ("A segment has base 8000 and limit 500. State what happens for offsets 53 and 500. [3 marks]",
           "Offset 53 is below the limit, so the physical address is 8000 + 53 = 8053 (1+1). Offset 500 is not less than the limit, so it is invalid and the hardware traps (1)."),
        PQ("A process needs 10 000 bytes. The page size is 4096 bytes. How many pages are needed and how many bytes are wasted by internal fragmentation? [3 marks]",
           "10 000 / 4096 = 2.44, so 3 pages (1). 3 x 4096 = 12 288 bytes (1). Waste = 12 288 - 10 000 = 2288 bytes (1)."),
        PQ("Explain what a TLB is and why it speeds up memory access. [3 marks]",
           "A small, fast cache holding recent page-to-frame translations (1). If the page is found (a hit) the frame is known without reading the page table in memory (1), saving one memory access per reference (1)."),
        SUM("A logical address splits into page number and offset; the page table replaces the page number by a frame number; the offset is unchanged.",
            "Internal fragmentation is waste inside the last frame; the number of pages is rounded up.",
            "A TLB caches translations; effective access time = hit x (TLB + memory) + miss x (TLB + 2 x memory).",
            "A segment address (segment, offset) is valid only if offset is less than the limit; physical address = base + offset.",
            "Segmentation causes external fragmentation; first fit and best fit are placement strategies.",
            "Exam link: Paper 2 calculations of addresses and fragmentation; Paper 1 definitions."),
    ],
))


LESSONS.append(lesson(
    module=OS, topic="Memory management",
    title="Virtual memory, page faults and page replacement",
    slug="csb-virtual-memory-page-replacement",
    minutes=25,
    summary="Explain demand paging and the steps of a page fault, count page faults for FIFO, LRU and optimal replacement, recognise Belady's anomaly and thrashing, and calculate effective access time with page faults.",
    objectives=[
        "Explain how virtual memory lets a program use more memory than the RAM installed",
        "Describe the sequence of events in a page fault",
        "Count page faults with FIFO, LRU and optimal replacement for a reference string",
        "Explain Belady's anomaly, thrashing and the dirty bit, and calculate effective access time with faults",
    ],
    key_concepts=["Virtual memory", "Demand paging", "Page fault", "Page replacement", "FIFO", "LRU", "Belady's anomaly", "Thrashing", "Dirty bit"],
    blocks=[
        H("Introduction"),
        T("A student in Yaoundé opens a game, a video, a browser with ten tabs and a document on a phone with 2 GB of RAM. "
          "The programs together seem to need more than 2 GB, yet the phone copes. The trick is **virtual memory**: only the pages being used "
          "need to be in RAM; the rest wait on the disk (or flash storage)."),
        D("**Virtual memory** gives each process a large logical address space by keeping only some of its pages in RAM and the rest in secondary storage. "
          "**Demand paging** loads a page only when it is first needed.", title="Definition: virtual memory and demand paging"),
        T("Each entry in the page table has a **valid bit**: 1 means the page is in a frame in RAM, 0 means it is not in RAM (or is not a legal page at all)."),
        H("What happens in a page fault"),
        D("A **page fault** happens when a process uses a page whose valid bit is 0. The hardware raises an interrupt and the operating system must bring the page into RAM.", title="Definition: page fault"),
        KEY("The steps of a page fault", "Learn them in order.", cards=[
            ["1. Trap", "The access to an invalid page raises an interrupt to the operating system."],
            ["2. Check", "The OS checks the address is legal. If not, the process is stopped. If legal, the page is on disk."],
            ["3. Find a frame", "Use a free frame. If none is free, a **replacement algorithm** picks a victim page to remove."],
            ["4. Read", "The disk reads the needed page into the frame. The process waits; the CPU runs another process."],
            ["5. Update and restart", "The page table is updated (valid bit = 1) and the interrupted instruction is run again."]]),
        T("If the victim page has been changed since it was loaded, its **dirty bit** is 1 and it must be written back to disk first. A clean page can simply be overwritten, which saves a disk write."),
        H("Page replacement algorithms"),
        T("A **reference string** lists the pages a program uses in order. With a fixed number of frames, the algorithm decides which page to evict."),
        KEY("Three algorithms", "Each chooses a different victim.", cards=[
            ["FIFO", "Evict the page that has been in memory longest. Simple, but it may remove a page still in heavy use."],
            ["LRU", "Evict the page not used for the longest time. Uses the past to predict the future. Good results, costly to implement exactly."],
            ["Optimal", "Evict the page that will not be used for the longest time in the future. Gives the fewest faults, but needs to see the future: used only as a yardstick."]]),
        CODE("""
Reference string: 2 3 2 1 5 2 4 5 3 2 5 2     3 frames

FIFO
Reference  2  3  2  1  5  2  4  5  3  2  5  2
Frame 0    2  2  2  2  5  5  5  5  3  3  3  3
Frame 1    -  3  3  3  3  2  2  2  2  2  5  5
Frame 2    -  -  -  1  1  1  4  4  4  4  4  2
Fault      F  F  .  F  F  F  F  .  F  .  F  F
Page faults = 9, hits = 3

LRU
Reference  2  3  2  1  5  2  4  5  3  2  5  2
Frame 0    2  2  2  2  2  2  2  2  3  3  3  3
Frame 1    -  3  3  3  5  5  5  5  5  5  5  5
Frame 2    -  -  -  1  1  1  4  4  4  2  2  2
Fault      F  F  .  F  F  .  F  .  F  F  .  .
Page faults = 7, hits = 5

Optimal: 6 page faults (the minimum possible for this string)
""", "text", title="Worked tables (produced by a program)"),
        EX("Worked example 1: FIFO, the first replacement", intro="Why does page 5 replace page 2 in the FIFO table?", steps=[
            S("State before", text="After 2, 3, 2, 1 the frames hold 2, 3, 1. Page 2 was loaded first, then 3, then 1. The hit on 2 does not change its load time."),
            S("Page 5 arrives", text="It is not in memory (fault). FIFO removes the oldest loaded page, which is 2. The frames become 5, 3, 1."),
            S("Next reference is 2", text="Page 2 was just evicted, so it faults again. This is why FIFO may remove pages that are still in use."),
        ]),
        EX("Worked example 2: LRU at the same moment", intro="Why does page 5 replace page 3 under LRU?", steps=[
            S("Last use times", text="Page 2 used at reference 3, page 3 at reference 2, page 1 at reference 4."),
            S("Least recently used", text="Page 3 has gone unused for longest, so page 3 is evicted. Frames: 2, 5, 1."),
            S("Result", text="The next reference to 2 is now a hit. LRU gives 7 faults against 9 for FIFO."),
        ]),
        CODE("""
def faults(refs, nframes, policy):
    frames, count = [], 0
    last_used = {}
    for t, page in enumerate(refs):
        if page in frames:
            last_used[page] = t
            continue
        count += 1
        if len(frames) == nframes:
            if policy == "FIFO":
                frames.pop(0)
            else:                      # LRU
                victim = min(frames, key=lambda p: last_used[p])
                frames.remove(victim)
        frames.append(page)
        last_used[page] = t
    return count

refs = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
print("FIFO, 3 frames:", faults(refs, 3, "FIFO"))
print("LRU,  3 frames:", faults(refs, 3, "LRU"))
belady = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
for n in (3, 4):
    print("FIFO with", n, "frames:", faults(belady, n, "FIFO"))

# Output (run):
# FIFO, 3 frames: 9
# LRU,  3 frames: 7
# FIFO with 3 frames: 9
# FIFO with 4 frames: 10
""", "python", title="Counting page faults in Python"),
        H("Belady's anomaly"),
        T("Surprisingly, giving a process **more** frames can make FIFO cause **more** faults. For the reference string 1 2 3 4 1 2 5 1 2 3 4 5, FIFO gives 9 faults with 3 frames but 10 faults with 4 frames (confirmed by the program above). "
          "This is **Belady's anomaly**. LRU and Optimal never behave this way: more frames never means more faults."),
        H("Thrashing"),
        D("**Thrashing** happens when a process has too few frames for the pages it needs at once. It faults again and again, and the system spends most of its time moving pages between disk and RAM, so little useful work is done.", title="Definition: thrashing"),
        T("The cause is too many processes in memory (high degree of multiprogramming). The CPU appears idle while processes wait for the disk, and a poor scheduler may then admit even more processes. "
          "Remedies: reduce the number of processes, give each its **working set** (the pages it uses in a recent time window), or add RAM."),
        EX("Worked example 3: cost of page faults", intro="A memory access takes 100 ns. Servicing a page fault takes 8 ms. One reference in 1000 causes a fault. Find the effective access time.", steps=[
            S("Convert units", math=r"8 \text{ ms} = 8\,000\,000 \text{ ns}"),
            S("Weighted average", math=r"(1 - 0.001) \times 100 + 0.001 \times 8\,000\,000 = 99.9 + 8000"),
            S("Result", text="About 8100 ns, which is 81 times slower than 100 ns. Even a tiny fault rate dominates, because a disk is far slower than RAM."),
        ]),
        H("Common mistakes"),
        MISTAKE("Counting a hit as a fault", "A page fault happens only when the page is not in a frame. A page already present is a hit and changes nothing for FIFO."),
        MISTAKE("Updating FIFO order on a hit", "FIFO orders by loading time, so a hit does not move a page. LRU does update on a hit."),
        MISTAKE("Forgetting the initial faults", "Every page loaded into an empty frame is also a fault. Count them."),
        QUIZ("Which algorithm can suffer from Belady's anomaly?",
             ["Optimal", "LRU", "FIFO", "None of them"], 2,
             "FIFO is the standard example: 9 faults with 3 frames and 10 with 4 frames on one string.",
             feedback=["Optimal never has the anomaly.", "LRU is a stack algorithm: more frames never increase faults.", "", "FIFO does."]),
        QUIZ("What is thrashing?",
             ["A page that is modified and must be written back", "Constant paging because processes have too few frames, so little useful work is done",
              "A process using too much CPU time", "A hardware fault in the disk"], 1,
             "The system spends its time moving pages instead of running programs.",
             feedback=["That is a dirty page.", "", "Thrashing is a memory problem, not CPU hogging.", "It is a software and load issue, not a hardware failure."]),
        H("Practice questions"),
        PQ("List, in order, the steps the operating system takes when a page fault occurs. [4 marks]",
           "The access to an invalid page causes a trap to the operating system (1). The OS checks the address is legal and finds the page on disk (1). A free frame is found, or a victim page is chosen (and written back if dirty) (1). The page is read into the frame, the page table is updated and the instruction is restarted (1)."),
        PQ("A process has 3 frames and uses pages in the order 7 0 1 2 0 3 0 4. Using FIFO, state the number of page faults. [3 marks]",
           "7 F, 0 F, 1 F (frames 7 0 1); 2 F evicts 7 (frames 2 0 1); 0 hit; 3 F evicts 0 (frames 2 3 1); 0 F evicts 1 (frames 2 3 0); 4 F evicts 2 (frames 4 3 0). Faults: 7, 0, 1, 2, 3, 0, 4 = 7 faults, 1 hit."),
        PQ("Using the same string and 3 frames, count the faults with LRU. [3 marks]",
           "7 F, 0 F, 1 F; 2 F evicts 7 (LRU); 0 hit; 3 F evicts 1 (0 was used more recently); 0 hit; 4 F evicts 2. Faults = 6 (7, 0, 1, 2, 3, 4), hits = 2."),
        PQ("Explain what is meant by thrashing and suggest one way of stopping it. [3 marks]",
           "Thrashing is when a process spends more time paging than executing because it has too few frames (1). It faults continuously and the CPU is underused (1). Stop it by reducing the number of processes in memory or giving each process enough frames for its working set (1)."),
        SUM("Virtual memory keeps only the needed pages in RAM; demand paging loads a page when first used.",
            "A page fault is an interrupt for a page not in RAM: find a frame, read the page, update the table, restart the instruction.",
            "FIFO evicts the oldest loaded page, LRU the least recently used, Optimal the one needed furthest in the future.",
            "Belady's anomaly: FIFO can fault more with more frames.",
            "Thrashing = constant paging; cure with fewer processes or working-set sizing.",
            "Exam link: Paper 2 usually has a reference string to trace; Paper 1 tests the definitions."),
    ],
))


# ================================================================== Translators
LESSONS.append(lesson(
    module=OS, topic="Translators",
    title="Assemblers, compilers and interpreters compared",
    slug="csb-translators-assembler-compiler-interpreter",
    minutes=22,
    summary="Compare assemblers, compilers and interpreters, explain object code, linking, loading and bytecode, and follow a two-pass assembler turning a small assembly program into machine code.",
    objectives=[
        "Define source code, object code and translator, and name the three kinds of translator",
        "Compare a compiler and an interpreter for speed, error reporting and distribution",
        "Explain the roles of the linker and loader and the idea of bytecode",
        "Follow the two passes of an assembler using a symbol table",
    ],
    key_concepts=["Translator", "Assembler", "Compiler", "Interpreter", "Object code", "Linker", "Loader", "Bytecode", "Symbol table"],
    blocks=[
        H("Introduction"),
        T("A developer in Douala writes a mobile app in a language like Python or Java. The phone's processor understands only **machine code**, patterns of 0s and 1s. "
          "A **translator** converts the program from the language it is written in (the **source code**) into machine code (the **object code**), or runs it directly."),
        D("A **translator** is a program that converts source code written in one language into another language, or executes it. "
          "The three kinds are the **assembler** (assembly language to machine code), the **compiler** (a high-level language to machine code in one go) "
          "and the **interpreter** (a high-level language, run one statement at a time).", title="Definition: translator"),
        H("The assembler"),
        T("Assembly language uses short mnemonics such as LDA, ADD and STA instead of binary. One assembly instruction normally becomes one machine instruction (a **one-to-one** relationship). "
          "Labels such as X or START let the programmer avoid writing addresses. The assembler works out the addresses in **two passes**."),
        KEY("Two-pass assembler", "A label can be used before it is defined, so one pass is not enough.", cards=[
            ["Pass 1", "Read every line, count addresses, and store each label with its address in the **symbol table**."],
            ["Pass 2", "Translate each mnemonic to its opcode and each label to its address from the symbol table. Produce the machine code."]]),
        CODE("""
Instruction set (8-bit word: 4-bit opcode, 4-bit address)
HLT = 0   LDA = 1   ADD = 2   STA = 3   JMP = 4

Source                      Address
START LDA X                 0
      ADD Y                 1
      STA Z                 2
      HLT                   3
X     DAT 5                 4
Y     DAT 7                 5
Z     DAT 0                 6
""", "text", title="A small assembly program"),
        EX("Worked example 1: the two passes", intro="Translate the program above into hexadecimal machine code.", steps=[
            S("Pass 1: symbol table", text="Count lines from 0. START is at 0, X at 4, Y at 5, Z at 6."),
            S("Pass 2: LDA X", math=r"1 \times 16 + 4 = 20 = \text{14 (hex)}", text="Opcode 1 in the top four bits, address 4 in the bottom four."),
            S("Pass 2: ADD Y, STA Z, HLT", text="ADD Y = 2 x 16 + 5 = 37 = 25 hex. STA Z = 3 x 16 + 6 = 54 = 36 hex. HLT = 00."),
            S("Data words", text="DAT 5, DAT 7, DAT 0 are stored as 05, 07, 00."),
            S("Machine code", text="14 25 36 00 05 07 00"),
        ]),
        CODE("""
OPCODES = {"HLT": 0, "LDA": 1, "ADD": 2, "STA": 3, "JMP": 4}
source = '''
START LDA X
      ADD Y
      STA Z
      HLT
X     DAT 5
Y     DAT 7
Z     DAT 0
'''
lines = [l.split() for l in source.strip().splitlines()]
symbols, address = {}, 0
for parts in lines:                       # pass 1
    if parts[0] not in OPCODES and parts[0] != "DAT":
        symbols[parts[0]] = address
    address += 1
print("Symbol table:", symbols)
code = []
for parts in lines:                       # pass 2
    if parts[0] in OPCODES or parts[0] == "DAT":
        op, rest = parts[0], parts[1:]
    else:
        op, rest = parts[1], parts[2:]
    if op == "DAT":
        code.append(int(rest[0]))
    else:
        operand = symbols[rest[0]] if rest else 0
        code.append(OPCODES[op] * 16 + operand)
print("Machine code:", " ".join(format(c, "02X") for c in code))

# Output (run):
# Symbol table: {'START': 0, 'X': 4, 'Y': 5, 'Z': 6}
# Machine code: 14 25 36 00 05 07 00
""", "python", title="A two-pass assembler in Python"),
        H("Compiler and interpreter"),
        D("A **compiler** translates the whole source program into object code before it runs. The object code can then be run many times without the compiler or the source.", title="Definition: compiler"),
        D("An **interpreter** reads, translates and executes the program **one statement at a time**. It translates again every time the statement is run, and no object code file is kept.", title="Definition: interpreter"),
        KEY("Comparison", "Examiners like clear contrasts.", cards=[
            ["Speed of running", "Compiled code runs faster: translation is done once. Interpreted code is slower because each statement is translated as it runs."],
            ["Errors", "A compiler reports many syntax errors together, after reading the whole program. An interpreter stops at the first error it reaches, which helps beginners find faults."],
            ["Development", "An interpreter lets you test a change at once. A compiler needs a recompile each time."],
            ["Distribution", "You can give users the object code without the source. Interpreted programs usually need the source and the interpreter on the user's machine."]]),
        H("Linker, loader and bytecode"),
        T("Big programs are written in several files and use library routines (such as maths or file functions). A compiler produces **object modules** with unresolved references. "
          "The **linker** joins the modules and libraries into one executable file, resolving those references. The **loader** copies the executable into memory and starts it."),
        T("Some languages use both ideas. The compiler translates source into **bytecode**, a compact code for an imaginary machine. A **virtual machine** then interprets the bytecode, or a **just-in-time (JIT) compiler** "
          "translates hot parts to machine code while the program runs. The same bytecode runs on any device with the virtual machine, which helps with the many kinds of phones in Cameroon."),
        EX("Worked example 2: choosing a translator", intro="Choose a translator for each situation and give a reason.", steps=[
            S("A game for phones that must run fast and be sold without its source", text="Compiler: the object code is fast and hides the source."),
            S("A student learning to program who changes one line and retries many times", text="Interpreter: no recompile, and it stops at the first error line."),
            S("A firmware routine written in assembly for a tiny sensor board", text="Assembler: one instruction per machine instruction, giving the programmer exact control of size and timing."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying an interpreter produces an object file", "An interpreter runs the code directly and normally keeps no object code. A compiler produces object code."),
        MISTAKE("Saying a compiler reports only one error", "A compiler analyses the whole program and can list many errors. It is the interpreter that stops at the first one it meets."),
        MISTAKE("Calling an assembler a compiler", "An assembler translates assembly language (low-level, mostly one-to-one). A compiler translates a high-level language, and one statement becomes many machine instructions."),
        QUIZ("What is the main job of the symbol table in an assembler?",
             ["To store the machine code", "To store each label with its address", "To store error messages", "To store the program output"], 1,
             "Pass 1 fills the symbol table with label addresses. Pass 2 uses it to replace labels with addresses.",
             feedback=["Machine code is generated in pass 2 and stored separately.", "", "Errors are reported, not stored in the symbol table.", "The assembler does not run the program."]),
        QUIZ("Why does an assembler need two passes?",
             ["Because machine code needs checking twice", "Because a label may be used before the line that defines it", "Because there are two kinds of memory", "Because opcodes must be sorted"], 1,
             "A jump to a label later in the program needs the label's address, which is not known until the whole source has been read.",
             feedback=["The passes are for addresses, not checking.", "", "Memory types are irrelevant here.", "Opcodes need no sorting."]),
        H("Practice questions"),
        PQ("Give three differences between a compiler and an interpreter. [3 marks]",
           "A compiler translates the whole program before it runs; an interpreter translates and runs one statement at a time (1). Compiled code runs faster as translation is done once; interpreted code is slower (1). A compiler produces object code that can be distributed without source; an interpreter keeps no object code and needs the source each time (1). Other valid points: error reporting, testing."),
        PQ("Explain why an assembler normally makes two passes through the source code. [3 marks]",
           "In the first pass it records the address of every label in a symbol table (1). A label may be referred to before it is defined (a forward reference) (1). In the second pass it replaces mnemonics by opcodes and labels by addresses using the table (1)."),
        PQ("Translate the assembly instruction ADD Y into hexadecimal, using the program in this lesson (ADD = 2, Y at address 5). [2 marks]",
           "Opcode 2 in the high four bits and address 5 in the low four bits give binary 0010 0101 (1), which is 25 in hexadecimal (1)."),
        PQ("State the roles of the linker and the loader. [2 marks]",
           "The linker combines object modules and library routines into one executable file and resolves references between them (1). The loader copies the executable into memory and starts it (1)."),
        SUM("An assembler translates assembly to machine code (mostly one to one) in two passes using a symbol table.",
            "A compiler translates the whole program first; an interpreter translates and runs statement by statement.",
            "Compiled programs run faster and can be distributed as object code; interpreters give fast testing and stop at the first error.",
            "The linker joins modules and libraries; the loader puts the executable in memory.",
            "Bytecode with a virtual machine or JIT combines portability with speed.",
            "Exam link: Paper 2 asks for comparisons and the roles of each translator; Paper 1 tests definitions."),
    ],
))


LESSONS.append(lesson(
    module=OS, topic="Translators",
    title="Lexical analysis: tokens, patterns and finite automata",
    slug="csb-lexical-analysis-tokens",
    minutes=22,
    summary="Explain the first stage of a compiler: turning source text into tokens, using patterns written as regular expressions and finite automata, building the symbol table and reporting lexical errors.",
    objectives=[
        "Distinguish lexeme, token and pattern and list the usual token types",
        "Break a source statement into tokens by hand, using longest match",
        "Trace a finite automaton that recognises identifiers and integers",
        "Explain what the lexical analyser removes, what it records and which errors it reports",
    ],
    key_concepts=["Lexical analysis", "Token", "Lexeme", "Pattern", "Regular expression", "Finite automaton", "Symbol table", "Longest match"],
    blocks=[
        H("Introduction"),
        T("Read the sentence 'Tchamba sells yams.' without thinking: your brain splits it into words before it looks at meaning. "
          "A compiler does the same with a program. The first stage, **lexical analysis** (also called scanning), reads the characters of the source "
          "and groups them into meaningful units called **tokens**. The part of the compiler that does this is the **lexical analyser** or lexer."),
        D("A **lexeme** is the actual text matched in the source, such as rate or 1.5. A **token** is the category it belongs to, such as IDENTIFIER or NUMBER, "
          "together with its value. A **pattern** is the rule that describes which lexemes belong to a token type.", title="Definition: lexeme, token and pattern"),
        T("The lexer also does housekeeping: it **removes** white space and comments (the parser does not need them), it keeps track of line numbers for error messages, "
          "and it enters identifiers into the **symbol table**."),
        KEY("Usual token types", "Names differ between languages, but the kinds are the same.", cards=[
            ["Keyword", "Reserved words with a fixed meaning: if, else, while, print."],
            ["Identifier", "Names chosen by the programmer: rate, x1, total_2."],
            ["Literal", "Fixed values: the numbers 20 and 1.5, text such as 'hello'."],
            ["Operator and punctuation", "Symbols: + - * / = <= == and ( ) { } ; ,"]]),
        H("Patterns and finite automata"),
        T("Patterns are written as **regular expressions**. An identifier is a letter or underscore followed by any number of letters, digits or underscores. "
          "In words: one letter or underscore, then zero or more letters, digits or underscores. An integer is one or more digits."),
        T("A pattern can be recognised by a **finite automaton**: a machine with a few states that reads one character at a time. "
          "If, after the last character, it is in an **accepting state**, the text matches."),
        CODE("""
Automaton for IDENTIFIER
State  letter or _   digit   other
S0     S1            DEAD    DEAD      (start)
S1     S1            S1      DEAD      (accepting)
DEAD   DEAD          DEAD    DEAD

Automaton for INTEGER
State  digit   other
S0     S1      DEAD      (start)
S1     S1      DEAD      (accepting)
""", "text", title="Transition tables"),
        EX("Worked example 1: trace the identifier automaton", intro="Is x1 an identifier? Is 2x?", steps=[
            S("x1", text="Start S0. Read x (a letter): S1. Read 1 (a digit): stay in S1. End of input in S1 (accepting): **valid identifier**."),
            S("2x", text="Start S0. Read 2 (a digit): the table gives DEAD. Once dead, always dead. **Not an identifier.**"),
            S("Why this rule", text="An identifier cannot start with a digit. Otherwise 2x would be confused with a number followed by a name."),
        ]),
        CODE("""
def is_identifier(s):
    state = 0                      # 0 start, 1 identifier (accepting), 2 dead
    for ch in s:
        if state == 0:
            state = 1 if ch.isalpha() or ch == "_" else 2
        elif state == 1:
            state = 1 if ch.isalnum() or ch == "_" else 2
        else:
            break
    return state == 1

for s in ("rate", "x1", "2x", "total_2", "a-b", ""):
    print(repr(s), is_identifier(s))

# Output (run):
# 'rate' True
# 'x1' True
# '2x' False
# 'total_2' True
# 'a-b' False
# '' False
""", "python", title="The automaton as a program"),
        H("Longest match and keywords"),
        T("When several tokens could start at the same place, the lexer takes the **longest match**. So <= is one operator token, not < followed by =, and rate2 is one identifier, not rate followed by 2."),
        T("Keywords look like identifiers. The lexer checks each identifier against the list of keywords: **if** is a keyword, but **iffy** is an identifier because the longest match is iffy."),
        H("A working lexer"),
        CODE("""
import re

TOKEN_SPEC = [
    ("KEYWORD", r"\\b(?:if|else|while|print)\\b"),
    ("NUMBER",  r"\\d+(?:\\.\\d+)?"),
    ("IDENT",   r"[A-Za-z_]\\w*"),
    ("OP",      r"==|<=|>=|[+\\-*/=<>]"),
    ("PUNCT",   r"[(){};,]"),
    ("SKIP",    r"[ \\t]+"),
    ("BAD",     r"."),
]
PATTERN = re.compile("|".join(f"(?P<{n}>{p})" for n, p in TOKEN_SPEC))

def tokenize(text):
    for m in PATTERN.finditer(text):
        if m.lastgroup != "SKIP":
            yield (m.lastgroup, m.group())

for source in ("rate = rate * 1.5 + 20;", "total = 5 # 2"):
    print(source)
    print("  ", list(tokenize(source)))

# Output (run):
# rate = rate * 1.5 + 20;
#    [('IDENT', 'rate'), ('OP', '='), ('IDENT', 'rate'), ('OP', '*'), ('NUMBER', '1.5'), ('OP', '+'), ('NUMBER', '20'), ('PUNCT', ';')]
# total = 5 # 2
#    [('IDENT', 'total'), ('OP', '='), ('NUMBER', '5'), ('BAD', '#'), ('NUMBER', '2')]
""", "python", title="A small lexer using regular expressions"),
        EX("Worked example 2: tokens of a statement", intro="Write the tokens of: if (x1 <= 10) print(x1);", steps=[
            S("Split by longest match", text="if, (, x1, <=, 10, ), print, (, x1, ), ;"),
            S("Classify", text="if = KEYWORD; ( = PUNCT; x1 = IDENT; <= = OP; 10 = NUMBER; ) = PUNCT; print = KEYWORD; ( = PUNCT; x1 = IDENT; ) = PUNCT; ; = PUNCT."),
            S("Count", text="11 tokens. White space was discarded. The symbol table now holds one new name, x1 (entered once)."),
        ]),
        EX("Worked example 3: a lexical error", intro="What does the lexer do with total = 5 # 2, if # is not part of the language?", steps=[
            S("Scan", text="total, =, 5 are fine."),
            S("The # character", text="No pattern matches #. The lexer reports a **lexical error** with the line number and the unrecognised character."),
            S("Recover", text="It may skip the character and carry on to find further errors in one run."),
        ]),
        H("The symbol table"),
        T("The **symbol table** stores one entry per identifier: its name, and later its type and where it lives in memory. Lexical analysis creates the entries; "
          "later stages add the type and address. When the same name appears again, the lexer finds the existing entry instead of making a new one."),
        H("Common mistakes"),
        MISTAKE("Mixing lexical and syntax errors", "A character that belongs to no token (such as #) is a lexical error. Tokens in the wrong order, such as 2 + * 3, are a syntax error found by the next stage."),
        MISTAKE("Forgetting that white space is removed", "Spaces and comments produce no tokens. They matter only where they separate two tokens."),
        MISTAKE("Splitting a multi-character operator", "<= is a single token. Treating it as < and = changes the meaning."),
        QUIZ("How many tokens are in the statement total = price * 3; (ignoring spaces)?",
             ["4", "5", "6", "7"], 2,
             "total, =, price, the multiplication sign, 3 and the semicolon are six tokens.", hint="Count each identifier, operator, number and punctuation mark.",
             feedback=["That misses two tokens.", "One token is missing; do not forget the semicolon.", "", "Seven would count something twice."]),
        QUIZ("Which stage reports the error in the line x = 4 @ 5 where @ is not in the language?",
             ["Lexical analysis", "Syntax analysis", "Semantic analysis", "Code generation"], 0,
             "No pattern matches the character @, so the lexer cannot form a token.",
             feedback=["", "Syntax analysis sees the tokens; the @ never becomes one.", "Semantic analysis checks meaning of valid structures.", "Code generation happens much later."]),
        H("Practice questions"),
        PQ("Define the terms lexeme and token. [2 marks]",
           "A lexeme is the actual sequence of characters in the source that matches a pattern, for example rate (1). A token is the category of the lexeme, for example IDENTIFIER, with its value (1)."),
        PQ("List the tokens in the statement while (n < 10) n = n + 1; and give the type of each. [4 marks]",
           "while KEYWORD, ( PUNCT, n IDENT, < OP, 10 NUMBER, ) PUNCT, n IDENT, = OP, n IDENT, + OP, 1 NUMBER, ; PUNCT. (1 mark for splitting correctly, up to 3 for types.)"),
        PQ("State two things the lexical analyser removes or ignores, and one thing it records. [3 marks]",
           "It removes white space (1) and comments (1). It records identifiers in the symbol table (1). It may also record line numbers."),
        PQ("Using the identifier automaton in this lesson, explain whether 9lives and lives9 are valid identifiers. [3 marks]",
           "9lives: from S0 the first character 9 is a digit, giving the dead state, so it is not valid (1+1). lives9: the first character is a letter (S1), and the digit keeps it in S1, which is accepting, so it is valid (1)."),
        SUM("Lexical analysis turns characters into tokens: keywords, identifiers, literals, operators and punctuation.",
            "A lexeme is the text; a token is its category; a pattern is the rule (a regular expression).",
            "Finite automata recognise patterns: an accepting state at the end means a match.",
            "The lexer uses longest match, removes white space and comments, and fills the symbol table.",
            "A character that matches no pattern is a lexical error.",
            "Exam link: Paper 2 may ask for the tokens of a statement; Paper 1 tests the terms."),
    ],
))


LESSONS.append(lesson(
    module=OS, topic="Translators",
    title="Syntax analysis, semantic analysis and code generation",
    slug="csb-syntax-semantic-analysis",
    minutes=25,
    summary="Describe a language with BNF rules, build derivations and parse trees, tell syntax errors from semantic errors, and follow the later compiler stages: intermediate code, optimisation and code generation.",
    objectives=[
        "Read and use BNF production rules to derive a sentence",
        "Draw a parse tree and show how the grammar gives operator precedence",
        "Distinguish syntax errors from semantic errors with examples",
        "Describe intermediate code, optimisation (such as constant folding) and code generation",
    ],
    key_concepts=["Syntax analysis", "BNF", "Grammar", "Parse tree", "Derivation", "Semantic analysis", "Intermediate code", "Optimisation", "Code generation"],
    blocks=[
        H("Introduction"),
        T("In English, 'Eat the yams' is a correct sentence and 'yams the eat' is not. The first test is **grammar**: are the words in an allowed order? "
          "A second test is meaning: 'The yams ate the farmer' is grammatical but makes little sense. A compiler makes these two tests separately: "
          "**syntax analysis** (grammar) then **semantic analysis** (meaning)."),
        T("The input to syntax analysis is the stream of tokens from the lexical analyser. The output is a **parse tree** (or syntax tree) that shows how the tokens fit the grammar."),
        H("Describing syntax with BNF"),
        D("**Backus-Naur Form (BNF)** is a notation for the grammar of a language. A rule has the form <name> ::= alternatives. "
          "Angle brackets enclose a **non-terminal** (something defined by other rules), the sign ::= means 'is defined as', the bar | separates alternatives, "
          "and symbols written plainly are **terminals** (actual tokens).", title="Definition: BNF"),
        CODE("""
<expr>   ::= <term>   | <expr> + <term>   | <expr> - <term>
<term>   ::= <factor> | <term> * <factor> | <term> / <factor>
<factor> ::= <number> | ( <expr> )
<number> ::= <digit> | <number> <digit>
<digit>  ::= 0|1|2|3|4|5|6|7|8|9
""", "text", title="A grammar for arithmetic expressions"),
        T("These rules are **recursive**: an <expr> can contain an <expr>. This is how a finite grammar describes expressions of any length. "
          "Notice that <term> (which handles * and /) sits **below** <expr> (which handles + and -). This builds operator precedence into the grammar."),
        EX("Worked example 1: derive 2 + 3 * 4", intro="Show that 2 + 3 * 4 is a valid <expr>. Always replace the leftmost non-terminal.", steps=[
            S("Start", text="<expr>"),
            S("Rule 2", text="<expr> + <term>   (using <expr> ::= <expr> + <term>)"),
            S("Expand left side", text="<term> + <term>  then  <factor> + <term>  then  2 + <term>"),
            S("Expand the right term", text="2 + <term> * <factor>  then  2 + <factor> * <factor>"),
            S("Finish", text="2 + 3 * <factor>  then  2 + 3 * 4. Every step used a rule, so the expression is valid."),
        ]),
        CODE("""
Parse tree for 2 + 3 * 4 (numbers shown directly)

<expr>
|-- <expr>
|     `-- <term>
|           `-- <factor> -- 2
|-- +
`-- <term>
      |-- <term>
      |     `-- <factor> -- 3
      |-- *
      `-- <factor> -- 4

The * is lower in the tree than the +, so 3 * 4 is worked out first:
2 + (3 * 4) = 14, not (2 + 3) * 4 = 20.
""", "text", title="A parse tree gives the structure"),
        EX("Worked example 2: use brackets", intro="How does (2 + 3) * 4 fit the grammar?", steps=[
            S("Top level", text="The whole expression is a <term>: <term> * <factor>, with <factor> = 4."),
            S("The left <term>", text="It becomes <factor> ::= ( <expr> ), and the inner <expr> is 2 + 3."),
            S("Meaning", text="The addition is deeper in the tree, so it is done first: 5 * 4 = 20. Brackets override the usual precedence by changing the tree."),
        ]),
        T("A grammar is **ambiguous** if one sentence has two different parse trees. A simple rule such as <expr> ::= <expr> + <expr> | <expr> * <expr> is ambiguous for 2 + 3 * 4. "
          "Compiler writers avoid ambiguity, as the layered grammar above does."),
        H("A parser in code"),
        T("A **recursive descent parser** has one function for each non-terminal. The code below parses the grammar (with loops in place of left recursion) and also produces **three-address code**, the intermediate form met next."),
        CODE("""
import re
def tokens(text):
    return re.findall(r"\\d+|[()+\\-*/]", text)

class Parser:
    def __init__(self, toks): self.t, self.i, self.tac, self.n = toks, 0, [], 0
    def peek(self): return self.t[self.i] if self.i < len(self.t) else None
    def eat(self, x=None):
        tok = self.peek()
        if tok is None or (x and tok != x):
            raise SyntaxError(f"expected {x or 'a token'} but found {tok}")
        self.i += 1; return tok
    def new(self): self.n += 1; return f"t{self.n}"
    def expr(self):
        left = self.term()
        while self.peek() in ("+", "-"):
            op = self.eat(); right = self.term(); t = self.new()
            self.tac.append(f"{t} = {left} {op} {right}"); left = t
        return left
    def term(self):
        left = self.factor()
        while self.peek() in ("*", "/"):
            op = self.eat(); right = self.factor(); t = self.new()
            self.tac.append(f"{t} = {left} {op} {right}"); left = t
        return left
    def factor(self):
        tok = self.peek()
        if tok == "(":
            self.eat("("); v = self.expr(); self.eat(")"); return v
        if tok and tok.isdigit(): return self.eat()
        raise SyntaxError(f"unexpected {tok}")

for src in ("2 + 3 * 4", "(2 + 3) * 4", "2 + * 3", "(2 + 3"):
    p = Parser(tokens(src))
    try:
        p.expr()
        if p.peek() is not None: raise SyntaxError("extra token " + p.peek())
        print(src, "->", p.tac)
    except SyntaxError as e:
        print(src, "-> syntax error:", e)

# Output (run):
# 2 + 3 * 4 -> ['t1 = 3 * 4', 't2 = 2 + t1']
# (2 + 3) * 4 -> ['t1 = 2 + 3', 't2 = t1 * 4']
# 2 + * 3 -> syntax error: unexpected *
# (2 + 3 -> syntax error: expected ) but found None
""", "python", title="Recursive descent parser with three-address code"),
        H("Semantic analysis"),
        D("**Semantic analysis** checks that a program that is correct in form also makes sense. It uses the symbol table and the parse tree to check types, declarations and the use of names.", title="Definition: semantic analysis"),
        KEY("Syntax error or semantic error?", "Ask: is the grammar broken, or is the meaning wrong?", cards=[
            ["Syntax errors", "Missing bracket, missing semicolon, two operators together (2 + * 3), a keyword in the wrong place. Found by the parser."],
            ["Semantic errors", "Using a variable that was never declared, adding a number to a string, calling a function with the wrong number of arguments, assigning a real number where an integer is required. Found by semantic analysis."],
            ["Logic errors", "The program is valid but gives wrong results, such as using + instead of -. No compiler can find these."]]),
        H("The later stages"),
        T("**Intermediate code generation** converts the tree into a simple, machine-independent form such as three-address code (at most one operator per line, as in the output above). "
          "This lets one compiler front end work with several back ends."),
        T("**Optimisation** improves the intermediate code without changing its result. Example: **constant folding** replaces 2 * 3.14 by 6.28 at compile time, so the multiplication is not done every time the program runs. "
          "Another example is removing code that can never be reached."),
        T("**Code generation** produces the target machine code or assembly, choosing registers and instructions. The result is the object code."),
        CODE("""
Source:  area = 3 * 4 + width

Three-address code        After constant folding
t1 = 3 * 4                t1 = 12
t2 = t1 + width           t2 = t1 + width
area = t2                 area = t2
""", "text", title="Constant folding"),
        H("Common mistakes"),
        MISTAKE("Saying a missing semicolon is a semantic error", "It breaks the grammar, so it is a syntax error. Semantic errors concern meaning, such as types and declarations."),
        MISTAKE("Thinking terminals are in angle brackets", "Non-terminals are written in angle brackets, like <expr>. Terminals are the actual symbols, like + and 7."),
        MISTAKE("Placing + and * at the same grammar level", "Putting them in one rule loses precedence. The operator with higher precedence must be defined lower down (in <term>)."),
        QUIZ("Which is a semantic error?",
             ["Writing x = (3 + 4;", "Writing 5 + * 2", "Using a variable total that was never declared", "Using @ in a language with no @"], 2,
             "The structure of the statement is fine, but the name has no declaration. This is found by semantic analysis.",
             feedback=["The missing bracket breaks the grammar: syntax error.", "Two operators together: syntax error.", "", "An invalid character is a lexical error."]),
        QUIZ("What does the rule <number> ::= <digit> | <number> <digit> describe?",
             ["A single digit only", "One or more digits", "Exactly two digits", "A decimal number"], 1,
             "A number is either one digit or a number followed by another digit, so it can be any length of 1 or more digits.",
             feedback=["The second alternative allows more digits.", "", "Nothing limits it to two.", "There is no decimal point in the rule."]),
        H("Practice questions"),
        PQ("Using the grammar in this lesson, show a derivation of 7 * 2 from <expr>. [3 marks]",
           "<expr> => <term> => <term> * <factor> => <factor> * <factor> => 7 * <factor> => 7 * 2. (1 mark for <expr> to <term>, 1 for <term> * <factor>, 1 for finishing with the factors and numbers.)"),
        PQ("Draw the parse tree for 2 * 3 + 4 and state its value. [4 marks]",
           "The root <expr> has three children: <expr>, +, <term> (1). The left <expr> becomes <term> with children <term> * <factor> giving 2 * 3 (1). The right <term> is <factor> 4 (1). Value = (2 * 3) + 4 = 10 (1)."),
        PQ("Give one example each of a syntax error and a semantic error, and say which compiler stage finds each. [4 marks]",
           "Syntax error: for example a missing closing bracket (1); found by syntax analysis (1). Semantic error: for example adding a number to a string, or using an undeclared variable (1); found by semantic analysis (1)."),
        PQ("Explain what constant folding is and why it is useful. [2 marks]",
           "The compiler works out an expression whose operands are constants at compile time, for example replacing 3 * 4 by 12 (1). The program then does less work each time it runs (1)."),
        SUM("Syntax analysis checks that tokens fit the grammar and builds a parse tree.",
            "BNF: non-terminals in angle brackets, ::= for 'is defined as', | for alternatives; rules may be recursive.",
            "Layered rules (expression, term, factor) give operator precedence; brackets change the tree.",
            "Syntax errors break the grammar; semantic errors break the meaning (types, declarations).",
            "Intermediate code, optimisation (such as constant folding) and code generation finish the job.",
            "Exam link: Paper 2 may ask for a BNF derivation or parse tree; Paper 1 asks which stage finds which error."),
    ],
))


# ================================================================== Network models
LESSONS.append(lesson(
    module=NET, topic="Network models",
    title="The seven OSI layers: functions, units and devices",
    slug="csb-osi-layers-in-detail",
    minutes=24,
    summary="Study each OSI layer's job, its data unit and typical protocols and devices, follow one web request down the layers with header sizes, and use the layers to locate network faults.",
    objectives=[
        "State the function, data unit (PDU) and an example protocol or device for each of the seven layers",
        "Explain encapsulation using header sizes and calculate overhead",
        "Match devices (hub, switch, router) to the layer at which they work",
        "Use the layered model to locate a fault",
    ],
    key_concepts=["OSI model", "Layer", "PDU", "Segment, packet and frame", "Hub, switch and router", "Encapsulation", "Overhead"],
    blocks=[
        H("Introduction"),
        T("When you send a photo from your phone in Garoua to a friend in Limbe, thousands of different devices and rules are involved, made by many companies. "
          "They work together because each rule handles one small job. The OSI model splits the job into **seven layers**. The overview lesson introduced the model; "
          "here we study what each layer does, what unit of data it uses, and which devices work at each level."),
        D("A **protocol data unit (PDU)** is the name for the block of data at a given layer. "
          "As data moves down, each layer adds its own header (and the data link layer a trailer), a process called **encapsulation**.", title="Definition: PDU and encapsulation"),
        H("The layers, from the top"),
        KEY("Layers 7, 6 and 5: working with the data", "These layers are about the program and its dialogue.", cards=[
            ["7 Application", "Gives network services to the user's program: web (HTTP), email (SMTP), names (DNS). The PDU is **data**."],
            ["6 Presentation", "Formats the data: character coding, compression, encryption, so that both sides understand it."],
            ["5 Session", "Starts, manages and ends a dialogue between two programs, including checkpoints."]]),
        KEY("Layers 4, 3, 2 and 1: moving the data", "These layers are about delivery.", cards=[
            ["4 Transport", "End-to-end delivery between programs using **port numbers**. TCP (reliable) or UDP (fast). PDU: **segment** (TCP) or datagram (UDP)."],
            ["3 Network", "Logical addressing (IP) and **routing** across networks. PDU: **packet**. Device: **router**."],
            ["2 Data link", "Delivery between two devices on the same link using MAC addresses, framing and error detection. PDU: **frame**. Device: **switch**."],
            ["1 Physical", "Sends raw **bits** as signals over cable, radio or fibre. Devices: hub, cable, repeater, network card connectors."]]),
        IMG("al-csb-osi-encapsulation.svg",
            "Seven stacked layers from application at top to physical at bottom, with the data unit beside each: data, data, data, segment, packet, frame, bits. An arrow shows headers being added going down.",
            caption="Figure 1. The seven layers and the data unit at each."),
        T("A memory aid, from layer 7 down to layer 1: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing."),
        H("Devices and layers"),
        T("A **hub** works at layer 1: it repeats bits to all ports and knows nothing about addresses. A **switch** works at layer 2: it reads the destination MAC address and sends the frame only out of the right port. "
          "A **router** works at layer 3: it reads the destination IP address and chooses the next network on the path. A **firewall** can work at several layers."),
        H("Encapsulation with numbers"),
        EX("Worked example 1: frame size", intro=(
            "A program sends 100 bytes of data. TCP adds a 20-byte header, IP adds a 20-byte header and Ethernet adds a 14-byte header and a 4-byte trailer. "
            "Find the size of each unit and the overhead."), steps=[
            S("Transport layer", math=r"100 + 20 = 120 \text{ bytes (segment)}"),
            S("Network layer", math=r"120 + 20 = 140 \text{ bytes (packet)}"),
            S("Data link layer", math=r"140 + 14 + 4 = 158 \text{ bytes (frame)}"),
            S("Overhead", math=r"158 - 100 = 58 \text{ bytes}", text="58 / 158 is 36.7 percent of the frame. Small messages carry a high proportion of headers."),
        ]),
        EX("Worked example 2: splitting a big message", intro="A 4000-byte message is sent by TCP. The largest data piece in one segment (MSS) is 1460 bytes. How many segments are needed?", steps=[
            S("Divide", math=r"4000 / 1460 = 2.74 \to 3 \text{ segments}"),
            S("Sizes", text="1460, 1460 and the remainder 4000 - 2920 = 1080 bytes."),
            S("At the receiver", text="TCP uses sequence numbers to put the segments back in order and rebuild the 4000 bytes."),
        ]),
        CODE("""
import math
TCP, IP, ETH_H, ETH_T = 20, 20, 14, 4
data = 100
segment = data + TCP
packet = segment + IP
frame = packet + ETH_H + ETH_T
print("data", data, "segment", segment, "packet", packet, "frame", frame)
overhead = frame - data
print("overhead", overhead, "bytes =", round(100 * overhead / frame, 1), "percent of the frame")
MSS, msg = 1460, 4000
n = math.ceil(msg / MSS)
sizes = [min(MSS, msg - i * MSS) for i in range(n)]
print("segments:", n, sizes, sum(sizes))

# Output (run):
# data 100 segment 120 packet 140 frame 158
# overhead 58 bytes = 36.7 percent of the frame
# segments: 3 [1460, 1460, 1080] 4000
""", "python", title="Checking the arithmetic"),
        H("Using layers to find faults"),
        EX("Worked example 3: which layer?", intro="Match each symptom to the most likely layer.", steps=[
            S("The cable is unplugged and the link light is off", text="Layer 1 (physical)."),
            S("Two computers on the same switch have the same MAC address", text="Layer 2 (data link)."),
            S("A computer cannot reach a server in another network but can reach local computers; the default gateway address is wrong", text="Layer 3 (network): routing and addressing."),
            S("A web page does not load but ping to the server works, and the server's port 80 is closed", text="Layer 4 (transport): the port is not reachable."),
            S("The page loads but characters appear as strange symbols", text="Layer 6 (presentation): coding of characters."),
        ]),
        T("Fault finding usually starts at layer 1 and works upward, or splits the problem in half. Each working layer rules out the layers below."),
        H("Common mistakes"),
        MISTAKE("Mixing up PDU names", "Segment belongs to layer 4, packet to layer 3, frame to layer 2. A router works with packets, a switch with frames."),
        MISTAKE("Saying a switch uses IP addresses", "A normal switch uses MAC addresses (layer 2). IP addresses are used by routers (layer 3)."),
        MISTAKE("Saying the physical layer adds a header", "The physical layer sends bits. Headers are added by layers 7 to 2, and a trailer by layer 2."),
        QUIZ("A device reads the destination IP address and sends the packet to the next network. At which layer does it work?",
             ["Layer 1", "Layer 2", "Layer 3", "Layer 4"], 2,
             "Reading the IP address and choosing a path is routing, a layer 3 job. The device is a router.",
             feedback=["Layer 1 only sends bits.", "Layer 2 devices use MAC addresses.", "", "Layer 4 uses port numbers, not routes."]),
        QUIZ("Which layer provides port numbers so that data reaches the right program?",
             ["Network", "Transport", "Session", "Data link"], 1,
             "Ports are used by TCP and UDP, which belong to the transport layer.",
             feedback=["The network layer uses IP addresses.", "", "The session layer manages dialogues, not port numbers.", "The data link layer uses MAC addresses."]),
        H("Practice questions"),
        PQ("State the layer that is responsible for each of: (a) routing, (b) MAC addresses and framing, (c) encryption and compression, (d) port numbers. [4 marks]",
           "(a) Network layer (1). (b) Data link layer (1). (c) Presentation layer (1). (d) Transport layer (1)."),
        PQ("Name the data unit at the transport layer, the network layer and the data link layer. [3 marks]",
           "Transport: segment (TCP) or datagram (UDP) (1). Network: packet (1). Data link: frame (1)."),
        PQ("Data of 200 bytes is sent. TCP adds a 20-byte header, IP a 20-byte header and the data link layer a 14-byte header and 4-byte trailer. Find the size of the frame and the overhead as a percentage of the frame (to 1 decimal place). [4 marks]",
           "Frame = 200 + 20 + 20 + 14 + 4 = 258 bytes (2). Overhead = 258 - 200 = 58 bytes (1). 58 / 258 = 22.5 percent (1)."),
        PQ("Explain the difference between a hub, a switch and a router in terms of the OSI model. [3 marks]",
           "A hub works at layer 1 and repeats bits to every port (1). A switch works at layer 2 and forwards frames using MAC addresses to the correct port (1). A router works at layer 3 and forwards packets between networks using IP addresses (1)."),
        SUM("Layers 7-5 deal with the application's data; 4-1 deal with delivery.",
            "PDUs: data, segment, packet, frame, bits.",
            "Transport: ports, TCP or UDP. Network: IP addressing and routing. Data link: MAC addresses and framing.",
            "Hub = layer 1, switch = layer 2, router = layer 3.",
            "Encapsulation adds headers going down; frame size = data + all headers + trailer.",
            "Exam link: Paper 1 asks for the layer of a function or device; Paper 2 asks for explanations and header calculations."),
    ],
))


LESSONS.append(lesson(
    module=NET, topic="Network models",
    title="The TCP/IP model: TCP, UDP, ports and the handshake",
    slug="csb-tcp-ip-tcp-udp-handshake",
    minutes=24,
    summary="Map the TCP/IP model to the OSI model, compare TCP and UDP, follow the three-way handshake and acknowledgements with sequence numbers, and trace what happens when a browser opens a web page.",
    objectives=[
        "Name the four TCP/IP layers and map them to OSI layers",
        "Compare TCP and UDP and choose the right one for an application",
        "Trace a TCP three-way handshake and acknowledged data transfer with sequence numbers",
        "Explain the roles of DNS, ARP and well-known ports when a web page is requested",
    ],
    key_concepts=["TCP/IP model", "TCP", "UDP", "Port number", "Socket", "Three-way handshake", "Acknowledgement", "DNS", "ARP"],
    blocks=[
        H("Introduction"),
        T("The internet runs on the **TCP/IP model**, which has four layers instead of seven. The OSI model is mainly a teaching reference; TCP/IP is what real networks use. "
          "This lesson goes further than the overview: you will see how TCP guarantees delivery, how UDP differs, and what your phone does in the first moments after you type a web address."),
        KEY("The four TCP/IP layers", "Learn the mapping to OSI.", cards=[
            ["Application", "OSI layers 7, 6 and 5 combined. Protocols: HTTP, HTTPS, DNS, SMTP, FTP."],
            ["Transport", "OSI layer 4. TCP and UDP. Ports."],
            ["Internet", "OSI layer 3. IP, ICMP (ping). Addressing and routing."],
            ["Link (network access)", "OSI layers 2 and 1. Ethernet, Wi-Fi. MAC addresses, framing and signals."]]),
        H("Ports and sockets"),
        D("A **port number** (0 to 65535) identifies a program on a computer. An IP address finds the computer; the port finds the program. "
          "The pair IP address plus port is a **socket**.", title="Definition: port and socket"),
        CODE("""
Well-known server ports (standard)
80   HTTP        web pages
443  HTTPS       secure web pages
53   DNS         names to IP addresses (usually UDP)
25   SMTP        sending email between servers
21   FTP         file transfer control
22   SSH         secure remote login
67/68 DHCP       automatic IP addresses
""", "text", title="Common ports"),
        T("A client such as your browser uses a temporary high port (for example 51234) as its source port, and the server's well-known port (443 for HTTPS) as the destination."),
        H("TCP and UDP"),
        KEY("Two transport protocols", "Choose by what the application needs.", cards=[
            ["TCP", "Transmission Control Protocol. **Connection-oriented**: set up first. Reliable: acknowledgements, retransmission of lost data, sequence numbers to restore order, flow control. Slower, more overhead. Used for web, email, file transfer."],
            ["UDP", "User Datagram Protocol. **Connectionless**: just send. No acknowledgement, no ordering, no retransmission. Small header, very fast. Used for DNS queries, live video and voice calls, online games, where a late packet is worse than a lost one."]]),
        H("The TCP three-way handshake"),
        T("Before data flows, the two sides agree on starting sequence numbers. A **sequence number** counts the bytes sent; an **acknowledgement number** says which byte the receiver expects next."),
        CODE("""
Client (port 51234)                      Server (port 80)

1  SYN, seq = 1000            ---->
2                             <----      SYN+ACK, seq = 5000, ack = 1001
3  ACK, seq = 1001, ack = 5001 ---->
   (connection open)

4  DATA 100 bytes, seq = 1001 ---->
5                             <----      ACK, ack = 1101
6  DATA 100 bytes, seq = 1101 ----X      (segment lost)
7  (no ACK arrives; timer expires)
8  DATA 100 bytes, seq = 1101 ---->      (retransmitted)
9                             <----      ACK, ack = 1201
""", "text", title="Handshake and acknowledged data"),
        EX("Worked example 1: reading the numbers", intro="Explain steps 2, 5 and 9 in the trace.", steps=[
            S("Step 2", text="The server's SYN+ACK has ack = 1001: it received the client's SYN (seq 1000, which uses one number) and expects byte 1001 next. It also gives its own starting number, 5000."),
            S("Step 5", text="The client's 100 bytes start at 1001, so the next byte it will send is 1101. The server acknowledges with ack = 1101."),
            S("Step 9", text="Byte 1101 to 1200 arrived after retransmission, so the server expects 1201 next. The ack number always means 'the next byte I need'."),
        ]),
        T("To close, each side sends a **FIN** and the other acknowledges. TCP also uses a **window**: the receiver tells the sender how much data it can accept, so a fast sender does not overwhelm a slow receiver (flow control). "
          "TCP slows down when it detects loss, to avoid overloading the network (congestion control)."),
        CODE("""
import socket, threading

def tcp_server(ready, out):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0)); s.listen(1)
    out.append(s.getsockname()[1]); ready.set()
    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.sendall(b"ACK:" + data)
    conn.close(); s.close()

ready, port = threading.Event(), []
threading.Thread(target=tcp_server, args=(ready, port), daemon=True).start()
ready.wait()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port[0]))       # three-way handshake happens here
c.sendall(b"hello")
print("TCP reply:", c.recv(1024))
c.close()

u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       # UDP: no handshake
u.bind(("127.0.0.1", 0))
addr = u.getsockname()
t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t.sendto(b"ping", addr)
data, _ = u.recvfrom(1024)
print("UDP datagram:", data)

# Output (run):
# TCP reply: b'ACK:hello'
# UDP datagram: b'ping'
""", "python", title="TCP and UDP sockets on one computer"),
        H("Opening a web page"),
        EX("Worked example 2: what happens when you type www.example.cm?", intro="Put the main events in order.", steps=[
            S("1. DNS lookup", text="The browser asks a DNS server (UDP port 53) for the IP address of the name. The reply gives, say, 203.0.113.10."),
            S("2. ARP", text="On the local network the phone needs the MAC address of the gateway (the router). ARP broadcasts 'who has this IP?' and the router replies with its MAC address."),
            S("3. TCP handshake", text="The browser connects to port 443 (or 80) on the server: SYN, SYN+ACK, ACK. For HTTPS, encryption is then set up."),
            S("4. HTTP request", text="The browser sends GET for the page. Large replies are split into several TCP segments, each acknowledged."),
            S("5. Display and close", text="The browser displays the page; the connection is closed with FIN, or kept open for further requests."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying UDP is always bad", "UDP is the right choice for live voice and video and for DNS queries: a lost packet is better ignored than delayed by retransmission."),
        MISTAKE("Saying TCP is faster because it is reliable", "TCP is reliable but has more overhead (handshake, acknowledgements). UDP is faster per message."),
        MISTAKE("Reading an acknowledgement as the last byte received", "ack = 1101 means bytes up to 1100 arrived and the receiver now expects 1101."),
        MISTAKE("Confusing IP address and port", "The IP address identifies the machine on the network; the port identifies the program on that machine."),
        QUIZ("A client sends 200 bytes starting at sequence number 3001, and all arrive. What acknowledgement number does the server send?",
             ["3001", "3200", "3201", "200"], 2,
             "Bytes 3001 to 3200 arrived, so the next byte expected is 3201.",
             hint="The acknowledgement is the next byte expected, not the last byte received.",
             feedback=["That is where the data started.", "3200 is the last byte received, not the next expected.", "", "200 is the amount of data, not a sequence position."]),
        QUIZ("Which protocol suits a live voice call where speed matters more than perfect delivery?",
             ["TCP", "UDP", "FTP", "SMTP"], 1,
             "UDP has no retransmission delay. A late voice packet is useless, so it is better to skip it.",
             feedback=["TCP's retransmission delays the stream.", "", "FTP is an application protocol for files, using TCP.", "SMTP is for email, using TCP."]),
        H("Practice questions"),
        PQ("Give three differences between TCP and UDP. [3 marks]",
           "TCP is connection-oriented (handshake first); UDP is connectionless (1). TCP is reliable with acknowledgements, retransmission and ordering; UDP is not (1). TCP has larger headers and more overhead and is slower; UDP is lighter and faster (1)."),
        PQ("A client opens a TCP connection with initial sequence number 700. Write the three segments of the handshake, with the server's starting number 2000. [3 marks]",
           "1: client to server, SYN, seq = 700 (1). 2: server to client, SYN+ACK, seq = 2000, ack = 701 (1). 3: client to server, ACK, seq = 701, ack = 2001 (1)."),
        PQ("Explain the purpose of DNS when a user opens a website, and say which transport protocol it normally uses. [3 marks]",
           "DNS converts the domain name typed by the user into an IP address (1), because routers need the IP address to deliver packets (1). It normally uses UDP (port 53) because queries are short (1)."),
        PQ("Explain what a port number is and why it is needed in addition to an IP address. [2 marks]",
           "A port number identifies a particular program or service on a computer (1). An IP address only identifies the computer, so the port is needed to deliver data to the right program, for example a browser or a mail client (1)."),
        SUM("TCP/IP has four layers: application, transport, internet and link.",
            "A port identifies a program; an IP address plus port is a socket.",
            "TCP is connection-oriented and reliable (handshake, sequence numbers, acknowledgements, retransmission); UDP is connectionless and light.",
            "Handshake: SYN, SYN+ACK, ACK. An acknowledgement number is the next byte expected.",
            "Opening a web page: DNS, ARP, TCP handshake, HTTP request and reply.",
            "Exam link: Paper 1 asks protocol-to-layer matching; Paper 2 asks for comparisons and traces."),
    ],
))


LESSONS.append(lesson(
    module=NET, topic="Addressing and errors",
    title="IPv4 and IPv6 addresses: formats, private ranges and compression",
    slug="csb-ipv4-ipv6-addresses",
    minutes=22,
    summary="Convert IPv4 addresses between dotted decimal and binary, identify private, loopback and link-local ranges, explain address exhaustion and NAT, and write IPv6 addresses in full and compressed form.",
    objectives=[
        "Convert an IPv4 address between dotted-decimal and binary",
        "Recognise private, loopback and link-local IPv4 addresses and explain NAT",
        "Explain why IPv6 was introduced and state its size and notation",
        "Compress and expand IPv6 addresses using the two compression rules",
    ],
    key_concepts=["IPv4", "Dotted decimal", "Private address", "NAT", "Loopback", "IPv6", "Hexadecimal groups", "Address compression"],
    blocks=[
        H("Introduction"),
        T("Every phone or computer on the internet needs an address so that replies find their way back. In Cameroon, the number of devices has grown very quickly "
          "with cheap smartphones. The older addressing system, IPv4, is nearly used up, and the newer one, IPv6, is slowly replacing it. "
          "This lesson looks at the two address formats. The next lesson uses IPv4 in subnetting."),
        H("IPv4 addresses"),
        D("An **IPv4 address** is a 32-bit number, written as four 8-bit parts called **octets**, each in decimal (0 to 255) and separated by dots. This is **dotted-decimal notation**.", title="Definition: IPv4 address"),
        T("There are 2 to the power 32, which is 4 294 967 296 possible addresses, fewer than the number of internet-connected devices in the world today."),
        EX("Worked example 1: decimal to binary", intro="Write 192.168.14.77 in binary.", steps=[
            S("192", math=r"192 = 128 + 64 \to 11000000"),
            S("168", math=r"168 = 128 + 32 + 8 \to 10101000"),
            S("14", math=r"14 = 8 + 4 + 2 \to 00001110"),
            S("77", math=r"77 = 64 + 8 + 4 + 1 \to 01001101"),
            S("Join", text="11000000.10101000.00001110.01001101. Each octet must have all 8 bits, with leading zeros."),
        ]),
        EX("Worked example 2: binary to decimal", intro="Convert 00101001.11001010.00010001.10000010 to dotted decimal.", steps=[
            S("First octet", math=r"00101001 = 32 + 8 + 1 = 41"),
            S("Second octet", math=r"11001010 = 128 + 64 + 8 + 2 = 202"),
            S("Third and fourth", math=r"00010001 = 17 \qquad 10000010 = 128 + 2 = 130"),
            S("Result", text="41.202.17.130"),
        ]),
        CODE("""
import ipaddress

def to_binary(dotted):
    return ".".join(format(int(p), "08b") for p in dotted.split("."))

print(to_binary("192.168.14.77"))
print(to_binary("41.202.17.130"))
for a in ("10.4.5.6", "172.15.1.1", "172.16.1.1", "172.32.0.1", "192.168.0.1", "8.8.8.8"):
    print(a, "private" if ipaddress.ip_address(a).is_private else "public")

# Output (run):
# 11000000.10101000.00001110.01001101
# 00101001.11001010.00010001.10000010
# 10.4.5.6 private
# 172.15.1.1 public
# 172.16.1.1 private
# 172.32.0.1 public
# 192.168.0.1 private
# 8.8.8.8 public
""", "python", title="Conversion and private ranges, checked by a program"),
        H("Special IPv4 ranges"),
        KEY("Learn these", "Standard reserved ranges.", cards=[
            ["Private (not routed on the internet)", "10.0.0.0 to 10.255.255.255 (10.0.0.0/8); 172.16.0.0 to 172.31.255.255 (172.16.0.0/12); 192.168.0.0 to 192.168.255.255 (192.168.0.0/16). Used inside homes, schools and companies."],
            ["Loopback", "127.0.0.1 (the whole 127.0.0.0/8 block). A computer talking to itself; useful for testing."],
            ["Link-local", "169.254.x.x. Self-assigned when no DHCP server answers: a sign that the network is not giving addresses."],
            ["Public", "All other addresses, which are unique on the internet and given out by registries and ISPs."]]),
        T("Notice the edge cases: 172.15.1.1 and 172.32.0.1 are **public** because the private block is only 172.16 to 172.31."),
        D("**NAT (network address translation)** lets many devices with private addresses share one public address. The router changes the source address and port of outgoing packets and keeps a table so replies are sent back to the right device. "
          "NAT slowed down address exhaustion but it breaks the simple end-to-end idea of the internet.", title="Definition: NAT"),
        H("IPv6 addresses"),
        D("An **IPv6 address** is 128 bits long, written as eight groups of four hexadecimal digits separated by colons.", title="Definition: IPv6 address"),
        T("2 to the power 128 is about 3.4 x 10 to the power 38 addresses: enough to give every device a unique public address. IPv6 also simplifies the header and was designed with auto-configuration. "
          "Both IPv4 and IPv6 are used together at present (dual stack)."),
        KEY("Two compression rules", "Make long addresses shorter. Apply them in this order.", cards=[
            ["Rule 1: leading zeros", "In each group, leading zeros may be dropped: 0db8 becomes db8, 0042 becomes 42, 0000 becomes 0."],
            ["Rule 2: one double colon", "One run of consecutive all-zero groups may be replaced by ::. Use it **once only**, for the longest run (the first if equal)."]]),
        EX("Worked example 3: compress", intro="Compress 2001:0db8:0000:0000:0000:ff00:0042:8329.", steps=[
            S("Rule 1", text="2001:db8:0:0:0:ff00:42:8329"),
            S("Rule 2", text="The three groups 0:0:0 form the longest zero run. Replace with ::"),
            S("Result", text="2001:db8::ff00:42:8329"),
        ]),
        EX("Worked example 4: expand", intro="Expand 2001:db8::1 to full form.", steps=[
            S("Count groups", text="Written: 2001, db8, then :: , then 1. That is 3 groups, so :: stands for 8 - 3 = 5 groups of zeros."),
            S("Insert and pad", text="2001:0db8:0000:0000:0000:0000:0000:0001"),
        ]),
        CODE("""
import ipaddress
print(ipaddress.ip_address("2001:0db8:0000:0000:0000:ff00:0042:8329").compressed)
print(ipaddress.ip_address("fe80:0000:0000:0000:0202:b3ff:fe1e:8329").compressed)
print(ipaddress.ip_address("2001:db8::1").exploded)

# Output (run):
# 2001:db8::ff00:42:8329
# fe80::202:b3ff:fe1e:8329
# 2001:0db8:0000:0000:0000:0000:0000:0001
""", "python", title="Compression and expansion"),
        T("Useful IPv6 addresses: **::1** is the loopback address; addresses beginning **fe80** are link-local (used on one network segment only). IPv6 has no broadcast; it uses multicast instead."),
        H("Common mistakes"),
        MISTAKE("Using :: twice", "If :: appeared twice you could not tell how many groups each stands for. Use it once."),
        MISTAKE("Dropping trailing zeros", "Only leading zeros may be dropped. In the group 0db8 the 0 at the front can go; in 0d80 you cannot remove the final 0."),
        MISTAKE("Writing octets above 255", "Each octet is 8 bits, so the largest value is 255. 192.168.300.1 is not a valid IPv4 address."),
        QUIZ("Which address is a private IPv4 address?",
             ["172.32.5.5", "172.20.5.5", "192.169.1.1", "11.0.0.1"], 1,
             "The private block is 172.16.0.0 to 172.31.255.255, which contains 172.20.5.5.",
             feedback=["172.32 is outside the 172.16 to 172.31 block.", "", "Only 192.168.x.x is private.", "Only 10.x.x.x is private; 11.x.x.x is public."]),
        QUIZ("Which is the correct compression of 2001:0000:0000:0000:0000:0000:0000:0005?",
             ["2001:0:0:0:0:0:0:5", "2001::5", "2001::0005", "2001::5::"], 1,
             "All seven groups after 2001 except the last form a run of six zero groups, so :: replaces them and 0005 becomes 5.",
             hint="Drop leading zeros, then use :: for the zero run.",
             feedback=["That applies rule 1 only and is correct but not fully compressed.", "", "The leading zeros of 0005 should be dropped.", "The :: appears at the end twice."]),
        H("Practice questions"),
        PQ("Convert the IPv4 address 10.20.30.40 to binary. [3 marks]",
           "10 = 00001010 (1); 20 = 00010100 (1); 30 = 00011110 and 40 = 00101000 (1). Answer: 00001010.00010100.00011110.00101000."),
        PQ("Explain why IPv6 was introduced and give the size of an IPv6 address. [3 marks]",
           "IPv4 has only about 4.3 billion addresses (2 to the power 32), which is not enough for the growing number of devices (1). IPv6 addresses are 128 bits long (1), giving a vastly larger address space (1)."),
        PQ("Write 2001:0db8:0000:0000:0000:0000:0000:0001 in its shortest form. [2 marks]",
           "Drop leading zeros (1) and replace the longest run of zero groups with :: giving 2001:db8::1 (1)."),
        PQ("State what NAT does and why a home router uses it. [3 marks]",
           "NAT translates private addresses into the router's public address (1) and keeps a table of connections so replies reach the right device (1). It lets many devices share one public IPv4 address, which saves scarce addresses (1)."),
        SUM("IPv4 is 32 bits in four octets (0-255); there are 2 to the power 32 addresses.",
            "Private ranges: 10/8, 172.16/12 (172.16 to 172.31), 192.168/16. Loopback 127.0.0.1. Link-local 169.254.x.x.",
            "NAT lets many private devices share one public address.",
            "IPv6 is 128 bits in eight hexadecimal groups.",
            "Compress by dropping leading zeros and using :: once for the longest zero run.",
            "Exam link: Paper 2 conversions and compression; Paper 1 identifies address types."),
    ],
))


LESSONS.append(lesson(
    module=NET, topic="Addressing and errors",
    title="CIDR subnetting: masks, subnets and VLSM",
    slug="csb-cidr-subnetting",
    minutes=26,
    summary="Use CIDR prefix lengths and subnet masks to find network, broadcast and host ranges, split a network into equal subnets, plan variable-length subnets (VLSM) and summarise routes.",
    objectives=[
        "Convert between a CIDR prefix length and a dotted-decimal subnet mask",
        "Find the network address, broadcast address and usable host range for an address and prefix",
        "Divide a network into equal subnets and into subnets of different sizes (VLSM)",
        "Check results with Python and summarise contiguous networks into one route",
    ],
    key_concepts=["CIDR", "Prefix length", "Subnet mask", "Network address", "Broadcast address", "Usable hosts", "Subnetting", "VLSM", "Route summarisation"],
    blocks=[
        H("Introduction"),
        T("A school in Bamenda is given one block of addresses, 200.10.5.0/24. It has a library with 100 computers, a lab with 50, an office with 20 and a link to the ISP. "
          "Putting everything in one big network wastes addresses and lets any fault spread. **Subnetting** splits the block into smaller networks sized to fit. "
          "The overview showed one worked case. Here you will learn the method and practise it on several."),
        D("**CIDR (Classless Inter-Domain Routing)** writes an address with a **prefix length**, such as 192.168.14.77/27, meaning the first 27 bits identify the network and the remaining 5 bits identify the host. "
          "The **subnet mask** has 1s for the network bits and 0s for the host bits.", title="Definition: CIDR and subnet mask"),
        KEY("Four formulas", "With h host bits (h = 32 minus the prefix length).", cards=[
            ["Usable hosts", "2 to the power h, minus 2. One address is the network address (all host bits 0) and one is the broadcast address (all host bits 1)."],
            ["Block size", "2 to the power h. The subnets start at multiples of this size in the interesting octet."],
            ["Network address", "Address AND mask (bit by bit)."],
            ["Broadcast address", "Network address plus block size, minus 1 (in the interesting octet)."]]),
        H("The mask from the prefix"),
        T("For /27: 27 ones then 5 zeros: 11111111.11111111.11111111.11100000. The last octet 11100000 = 128 + 64 + 32 = 224. So the mask is 255.255.255.224. "
          "Useful last-octet values: /25 = 128, /26 = 192, /27 = 224, /28 = 240, /29 = 248, /30 = 252."),
        EX("Worked example 1: network and broadcast for 192.168.14.77/27", intro="Find the mask, network address, broadcast address and usable host range.", steps=[
            S("Mask and host bits", text="/27 gives mask 255.255.255.224. Host bits h = 32 - 27 = 5, so the block size is 2^5 = 32."),
            S("Find the block", text="The interesting octet is the last: 77. The multiples of 32 are 0, 32, 64, 96. The largest not above 77 is 64, so the network address is 192.168.14.64."),
            S("Check by AND", text="77 = 01001101 and mask 224 = 11100000. AND = 01000000 = 64."),
            S("Broadcast", math=r"64 + 32 - 1 = 95", text="Broadcast address: 192.168.14.95."),
            S("Hosts", text="First usable 192.168.14.65, last usable 192.168.14.94. Count = 2^5 - 2 = 30."),
        ]),
        EX("Worked example 2: a /20 across two octets", intro="Find the network and broadcast addresses of 172.16.45.200/20.", steps=[
            S("Mask", text="/20 = 20 ones: 255.255.240.0. Host bits = 12; block size in the third octet = 256 - 240 = 16."),
            S("Third octet", text="45: multiples of 16 are 32, 48. The largest not above 45 is 32. Network = 172.16.32.0."),
            S("Broadcast", text="Next network starts at third octet 48, so broadcast = 172.16.47.255."),
            S("Hosts", text="172.16.32.1 to 172.16.47.254, which is 2^12 - 2 = 4094 hosts."),
        ]),
        CODE("""
import ipaddress

def describe(cidr):
    i = ipaddress.ip_interface(cidr)
    n = i.network
    hosts = list(n.hosts())
    print(cidr, "-> mask", n.netmask, "| network", n.network_address,
          "| broadcast", n.broadcast_address,
          "| hosts", hosts[0], "to", hosts[-1], f"({len(hosts)})")

describe("192.168.14.77/27")
describe("172.16.45.200/20")

# Output (run):
# 192.168.14.77/27 -> mask 255.255.255.224 | network 192.168.14.64 | broadcast 192.168.14.95 | hosts 192.168.14.65 to 192.168.14.94 (30)
# 172.16.45.200/20 -> mask 255.255.240.0 | network 172.16.32.0 | broadcast 172.16.47.255 | hosts 172.16.32.1 to 172.16.47.254 (4094)
""", "python", title="Checking the two examples"),
        H("Splitting into equal subnets"),
        EX("Worked example 3: four equal subnets", intro="Divide 192.168.10.0/24 into 4 equal subnets.", steps=[
            S("Bits to borrow", text="4 subnets need 2 bits (2^2 = 4). New prefix = 24 + 2 = 26."),
            S("Block size", text="Host bits = 6, so block size = 64. Mask = 255.255.255.192."),
            S("List", text="192.168.10.0/26, 192.168.10.64/26, 192.168.10.128/26, 192.168.10.192/26."),
            S("Hosts per subnet", text="2^6 - 2 = 62. The first subnet runs from .1 to .62, with broadcast .63."),
        ]),
        H("Different sizes: VLSM"),
        D("**Variable-length subnet masking (VLSM)** uses different prefix lengths inside one block, so each subnet is just big enough. "
          "Method: sort the requirements from the largest to the smallest, give each the smallest block that fits (hosts + 2 addresses), and allocate one after another without overlap.", title="Definition: VLSM"),
        EX("Worked example 4: the school at 200.10.5.0/24", intro="Library 100 hosts, lab 50 hosts, office 20 hosts, ISP link 2 hosts. Plan the subnets.", steps=[
            S("Library, 100 hosts", text="Need at least 102 addresses. 2^7 = 128 fits. Prefix /25 (126 hosts): 200.10.5.0/25, range .0 to .127."),
            S("Lab, 50 hosts", text="52 addresses needed. 2^6 = 64. Prefix /26 (62 hosts): 200.10.5.128/26, range .128 to .191."),
            S("Office, 20 hosts", text="22 needed. 2^5 = 32. Prefix /27 (30 hosts): 200.10.5.192/27, range .192 to .223."),
            S("ISP link, 2 hosts", text="4 addresses. Prefix /30 (2 hosts): 200.10.5.224/30, range .224 to .227."),
            S("Check", text="128 + 64 + 32 + 4 = 228, less than 256, so everything fits. Addresses from .228 to .255 are left for future use."),
        ]),
        CODE("""
for c in ("200.10.5.0/25", "200.10.5.128/26", "200.10.5.192/27", "200.10.5.224/30"):
    describe(c)

# Output (run, using describe from above):
# 200.10.5.0/25 -> mask 255.255.255.128 | network 200.10.5.0 | broadcast 200.10.5.127 | hosts 200.10.5.1 to 200.10.5.126 (126)
# 200.10.5.128/26 -> mask 255.255.255.192 | network 200.10.5.128 | broadcast 200.10.5.191 | hosts 200.10.5.129 to 200.10.5.190 (62)
# 200.10.5.192/27 -> mask 255.255.255.224 | network 200.10.5.192 | broadcast 200.10.5.223 | hosts 200.10.5.193 to 200.10.5.222 (30)
# 200.10.5.224/30 -> mask 255.255.255.252 | network 200.10.5.224 | broadcast 200.10.5.227 | hosts 200.10.5.225 to 200.10.5.226 (2)
""", "python", title="Verifying the VLSM plan"),
        H("Route summarisation and testing membership"),
        T("The reverse of subnetting is **summarisation**: combining contiguous networks into one route. 192.168.4.0/24, 192.168.5.0/24, 192.168.6.0/24 and 192.168.7.0/24 are four blocks of 256 starting at a multiple of 4 in the third octet, "
          "so they combine into **192.168.4.0/22** (mask 255.255.252.0). Python's collapse_addresses confirms it."),
        T("To test whether a host is in a subnet, find the subnet's range. 172.16.50.1 is not in 172.16.32.0/20 because the third octet 50 is above the broadcast value 47 (confirmed with Python: False)."),
        H("Common mistakes"),
        MISTAKE("Forgetting the minus 2", "Usable hosts = 2^h - 2. The network address and broadcast address cannot be given to a host."),
        MISTAKE("Starting a subnet at an address that is not a multiple of the block size", "A /26 subnet must begin at 0, 64, 128 or 192. 192.168.10.50/26 is a host inside the 0 subnet, not a network address."),
        MISTAKE("Allocating small subnets first in VLSM", "Start with the largest block. Small blocks first can leave awkward gaps that waste space or cause overlaps."),
        MISTAKE("Counting hosts needed without the two extra addresses", "For 30 hosts you need 30 + 2 = 32 addresses, which is exactly a /27. For 31 hosts you need 33 addresses, so the next size up, 64 addresses (a /26)."),
        QUIZ("What is the subnet mask for /28?",
             ["255.255.255.192", "255.255.255.224", "255.255.255.240", "255.255.255.248"], 2,
             "/28 has 4 host bits. The last octet has 4 ones: 11110000 = 240.",
             feedback=["That is /26.", "That is /27.", "", "That is /29."]),
        QUIZ("How many usable host addresses are there in a /29 subnet?",
             ["8", "6", "5", "2"], 1,
             "3 host bits give 2^3 = 8 addresses, minus network and broadcast = 6.",
             feedback=["8 counts the network and broadcast addresses too.", "", "Subtract only the two reserved addresses, not three.", "2 hosts is a /30 subnet."]),
        H("Practice questions"),
        PQ("For the address 192.168.14.77/27, state the network address, the broadcast address and the number of usable hosts. [3 marks]",
           "Block size 32; 77 lies in the block starting at 64, so network address 192.168.14.64 (1). Broadcast = 64 + 32 - 1 = 95: 192.168.14.95 (1). Usable hosts = 32 - 2 = 30 (1)."),
        PQ("A company is given 10.1.1.0/24 and needs 8 equal subnets. State the new prefix length, the subnet mask and the number of usable hosts in each subnet. [3 marks]",
           "8 subnets need 3 bits, so the prefix is /27 (1). Mask 255.255.255.224 (1). Host bits 5 so 2^5 - 2 = 30 usable hosts (1)."),
        PQ("An office network needs 60 hosts. State the smallest suitable prefix length and explain your choice. [3 marks]",
           "60 hosts plus network and broadcast addresses need 62 addresses (1). 2^6 = 64 is the smallest power of two that is large enough (1), so 6 host bits are needed and the prefix is /26 (1)."),
        PQ("Combine the networks 192.168.8.0/24, 192.168.9.0/24, 192.168.10.0/24 and 192.168.11.0/24 into one summary route. [3 marks]",
           "The third octets 8, 9, 10, 11 cover a block of 4 starting at a multiple of 4 (1). Four /24 networks need 2 fewer prefix bits: 24 - 2 = 22 (1). Summary route 192.168.8.0/22 (1)."),
        SUM("Prefix length n means n network bits; host bits h = 32 - n; usable hosts = 2^h - 2.",
            "Network address = address AND mask; broadcast = network + block size - 1.",
            "Borrowing k bits makes 2^k subnets, each with a prefix k bits longer.",
            "VLSM: allocate the largest requirement first, with the smallest block that fits hosts + 2.",
            "Summarise contiguous networks by shortening the prefix.",
            "Exam link: Paper 2 subnetting calculations; Paper 1 mask and host-count questions."),
    ],
))


LESSONS.append(lesson(
    module=NET, topic="Addressing and errors",
    title="Error detection: parity, checksum and CRC",
    slug="csb-crc-error-detection",
    minutes=26,
    summary="Detect transmission errors with a parity bit, a checksum and a cyclic redundancy check: calculate a CRC by modulo-2 division, verify a received frame and understand what CRC can and cannot detect.",
    objectives=[
        "Explain why errors occur in transmission and why detection is needed",
        "Calculate an even parity bit and a simple checksum",
        "Calculate a CRC remainder by modulo-2 division and build the transmitted frame",
        "Check a received frame, and state which errors a CRC detects",
    ],
    key_concepts=["Transmission error", "Parity bit", "Checksum", "CRC", "Generator polynomial", "Modulo-2 division", "Burst error"],
    blocks=[
        H("Introduction"),
        T("When you send mobile money data over a weak signal near a hill in the North-West Region, noise can change a 1 into a 0. If the amount 5 000 became 1 000, or the receiving account changed, the result would be serious. "
          "The receiver needs a cheap way to notice that something went wrong. The sender adds a few extra bits calculated from the data. The receiver repeats the calculation and compares."),
        D("**Error detection** adds redundant bits to data so that the receiver can tell that the data was changed in transmission. If an error is found, the receiver asks for the data to be sent again (retransmission).", title="Definition: error detection"),
        H("Parity bit"),
        T("A **parity bit** is one extra bit that makes the number of 1s in the data even (**even parity**) or odd (**odd parity**). For the 7-bit data 1011011 there are five 1s, so the even parity bit is 1, and the sent byte is 10110111 (six 1s). "
          "If the receiver counts an odd number of 1s, an error occurred."),
        T("Parity detects any **single-bit** error, but if two bits flip, the count is still even and the error goes unnoticed. It cannot say which bit is wrong."),
        H("Checksum"),
        T("A **checksum** adds up the data bytes and sends the total (kept to one byte by taking the remainder after dividing by 256) as an extra byte. "
          "Bytes 69, 26, 243 and 8 sum to 346, and 346 - 256 = 90. The receiver adds the data bytes again and compares with the checksum 90. "
          "Checksums are simple but can miss some errors, for example two changes that cancel each other out (one byte up by 5 and another down by 5)."),
        H("Cyclic redundancy check (CRC)"),
        D("A **cyclic redundancy check (CRC)** treats the data as a long binary number and divides it by an agreed **generator** (also written as a polynomial) using modulo-2 arithmetic. "
          "The **remainder** is sent after the data. The receiver divides the whole received frame by the same generator: if the remainder is zero, no error is detected.", title="Definition: CRC"),
        KEY("Modulo-2 arithmetic", "No carrying or borrowing: addition and subtraction are both XOR.", cards=[
            ["Rules", "0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, 1 XOR 1 = 0."],
            ["Division step", "If the leading bit of the current window is 1, XOR the window with the generator. If it is 0, skip (XOR with zeros) and slide on by one bit."],
            ["Check bits", "A generator of n bits (degree n - 1) gives n - 1 check bits. Generator 1101 is x^3 + x^2 + 1 and gives 3 check bits."]]),
        EX("Worked example 1: calculate the CRC", intro="Data = 101101, generator = 1101. Find the check bits and the transmitted frame.", steps=[
            S("Append zeros", text="Generator has 4 bits, so append 3 zeros: 101101000."),
            S("Position 1: 1011 XOR 1101", math=r"1011 \oplus 1101 = 0110", text="The string becomes 011001000."),
            S("Position 2: 1100 XOR 1101", math=r"1100 \oplus 1101 = 0001", text="The string becomes 000011000."),
            S("Positions 3 and 4", text="Leading bit is 0, so nothing to do."),
            S("Position 5: 1100 XOR 1101", math=r"1100 \oplus 1101 = 0001", text="The string becomes 000000010."),
            S("Remainder", text="The last three bits are 010. CRC = 010."),
            S("Frame", text="Data followed by remainder: 101101010."),
        ]),
        CODE("""
Dividend  101101000   generator 1101

start     101101000
pos 1     1011 xor 1101 = 0110     ->  011001000
pos 2      1100 xor 1101 = 0001    ->  000011000
pos 3, 4   leading bit 0, skip
pos 5          1100 xor 1101 = 0001 ->  000000010
remainder (last 3 bits) = 010
transmitted frame = 101101 010
""", "text", title="Division layout"),
        EX("Worked example 2: the receiver checks", intro="The frame 101101010 arrives. Then repeat with 100101010 (bit 3 changed).", steps=[
            S("First frame", text="Divide 101101010 by 1101 in the same way. The remainder is 000, so no error is detected."),
            S("Second frame", text="Divide 100101010 by 1101. The remainder is 110, which is not zero. **Error detected**; the receiver rejects the frame and requests it again."),
            S("Check by program", text="See the program below, which gives the same results."),
        ]),
        CODE("""
def crc_remainder(bits, gen):
    work = list(bits)
    n = len(gen)
    for i in range(len(work) - n + 1):
        if work[i] == "1":
            for j in range(n):
                work[i + j] = "0" if work[i + j] == gen[j] else "1"
    return "".join(work[-(n - 1):])

def make_frame(data, gen):
    return data + crc_remainder(data + "0" * (len(gen) - 1), gen)

def check(frame, gen):
    return crc_remainder(frame, gen) == "0" * (len(gen) - 1)

gen = "1101"
frame = make_frame("101101", gen)
print("frame:", frame)
print("receiver, no error:", check(frame, gen))
bad = frame[:2] + ("1" if frame[2] == "0" else "0") + frame[3:]
print("bit 3 flipped:", bad, check(bad, gen), crc_remainder(bad, gen))
multiple = "000001101"
undetected = "".join("1" if a != b else "0" for a, b in zip(frame, multiple))
print("error equal to a multiple of the generator:", undetected, check(undetected, gen))
print("second example:", make_frame("1101011", "1011"))

# Output (run):
# frame: 101101010
# receiver, no error: True
# bit 3 flipped: 100101010 False 110
# error equal to a multiple of the generator: 101100111 True
# second example: 1101011110
""", "python", title="CRC in Python"),
        H("What can a CRC detect?"),
        T("The error pattern is the XOR of the sent and received frames. A CRC fails to notice an error only if the error pattern is exactly divisible by the generator. In the program above, changing the bits marked by the pattern 000001101 (which is the generator itself) "
          "gives the frame 101100111. The check still returns **True**, so this changed frame passes. Such errors are very rare with real, long generators."),
        KEY("Strengths of a CRC with r check bits", "Reasons it is used on Ethernet frames, disks and files.", cards=[
            ["Single-bit errors", "All detected (when the generator has at least two terms, including the constant 1)."],
            ["Burst errors", "All burst errors up to r bits long are detected. Bursts are typical of noise on cables and radio."],
            ["Longer errors", "Most are detected. The chance of missing a random error is very small, about 1 in 2 to the power r."],
            ["Limits", "A CRC detects errors only; it does not correct them. It does not protect against deliberate tampering, because an attacker can recalculate it."]]),
        H("Common mistakes"),
        MISTAKE("Forgetting to append the zeros", "Append n - 1 zeros to the data before dividing. Without them the division gives the wrong remainder."),
        MISTAKE("Subtracting normally", "Modulo-2 subtraction is XOR, with no borrowing. 1 - 1 = 0 and 0 - 1 = 1 in modulo-2."),
        MISTAKE("Sending the quotient", "The quotient is discarded. Only the remainder is attached to the data."),
        MISTAKE("Thinking a zero remainder proves the data is correct", "It means no error was detected. A rare error pattern that is a multiple of the generator would also give zero."),
        QUIZ("A generator has 5 bits. How many check bits does the CRC add?",
             ["5", "4", "6", "1"], 1,
             "The remainder is one bit shorter than the generator, so 4 check bits.",
             feedback=["The remainder has one bit fewer than the generator.", "", "More than the generator length is impossible.", "One bit is a parity bit, not a CRC."]),
        QUIZ("The receiver divides a received frame by the generator and gets a non-zero remainder. What does it do?",
             ["Accepts the frame", "Rejects the frame and requests retransmission", "Corrects the wrong bit automatically", "Adds more check bits"], 1,
             "A non-zero remainder means an error was detected. A CRC cannot correct; the frame is discarded and sent again.",
             feedback=["That would accept bad data.", "", "CRC detects but cannot correct.", "Adding bits would not fix the data."]),
        H("Practice questions"),
        PQ("Calculate the even parity bit for the 7-bit data 1100101 and write the byte sent. [2 marks]",
           "The data has four 1s (1100101: 1+1+0+0+1+0+1 = 4), already even, so the parity bit is 0 (1). The byte sent is 11001010 (1)."),
        PQ("Use modulo-2 division to find the CRC for the data 1101011 with generator 1011. State the transmitted frame. [4 marks]",
           "Append three zeros: 1101011000 (1). Divide by 1011 using XOR; the remainder is 110 (2). The transmitted frame is 1101011110 (1)."),
        PQ("The frame 1101011110 is received with the generator 1011, and the remainder after division is 000. What does the receiver conclude? Give one reason why this is not a guarantee. [3 marks]",
           "No error is detected, so the frame is accepted (1). An error pattern that is an exact multiple of the generator would also give a remainder of 000 (1), so some very rare errors go unnoticed (1)."),
        PQ("Explain two advantages of CRC compared with a single parity bit. [2 marks]",
           "A CRC detects burst errors and multiple-bit errors that parity misses (when an even number of bits change) (1). It uses several check bits, giving a far lower chance of missing an error (1)."),
        SUM("Transmission errors are detected by sending redundant bits; the receiver recalculates and compares.",
            "Parity detects odd numbers of bit errors; a checksum adds up bytes.",
            "CRC: append n - 1 zeros, divide by the generator with XOR (no borrow), send the remainder after the data.",
            "The receiver divides the whole frame: remainder 000 means no error detected.",
            "CRC catches all single-bit and short burst errors but only detects, never corrects.",
            "Exam link: Paper 2 asks for a CRC calculation; Paper 1 asks for definitions and what CRC detects."),
    ],
))


# ================================================================== Software development
LESSONS.append(lesson(
    module=NET, topic="Software development",
    title="Development models: Waterfall, Spiral and Agile Scrum",
    slug="csb-sdlc-waterfall-spiral-agile",
    minutes=24,
    summary="Describe the stages of the software development life cycle, compare the Waterfall, Spiral and Agile Scrum models, name the Scrum roles, events and artefacts, and choose a model for a given project.",
    objectives=[
        "List the stages of the software development life cycle",
        "Explain the Waterfall and Spiral models with advantages and disadvantages",
        "Describe Agile values and the Scrum roles, events and artefacts",
        "Choose and justify a development model for a described project; track progress with story points",
    ],
    key_concepts=["SDLC", "Waterfall", "Spiral", "Risk analysis", "Agile", "Scrum", "Sprint", "Product backlog", "Velocity"],
    blocks=[
        H("Introduction"),
        T("A team in Douala is asked to build a mobile app that lets market traders record daily sales. Questions come at once. What exactly should it do? Who will test it? What if the traders want changes after seeing the first version? "
          "A **development model** is a plan for how the team will answer these questions and organise the work."),
        D("The **software development life cycle (SDLC)** is the series of stages through which software passes: **requirements**, **design**, **implementation** (coding), **testing**, **deployment** and **maintenance**. "
          "A development model decides the order in which these stages are done and how often they are repeated.", title="Definition: SDLC"),
        H("The Waterfall model"),
        T("In the **Waterfall model** each stage is finished completely, signed off, and only then the next one starts. Progress flows downward like water over steps. There is little going back."),
        CODE("""
Requirements -> Design -> Implementation -> Testing -> Deployment -> Maintenance
(each stage complete and approved before the next begins)
""", "text", title="Waterfall"),
        KEY("Waterfall: when it fits", "Compare strengths and weaknesses.", cards=[
            ["Advantages", "Simple to manage. Clear stages, documents and deadlines. Good when requirements are well understood and unlikely to change (e.g. a payroll system following fixed law, or safety-critical equipment)."],
            ["Disadvantages", "Working software appears only at the end. Changes are costly. Mistakes in the requirements are discovered late, at testing or after delivery. The client sees nothing until the end."]]),
        H("The Spiral model"),
        T("The **Spiral model** repeats four activities in loops, each loop producing a more complete version. It puts **risk analysis** at the centre of every loop."),
        KEY("Four activities in each loop", "Each cycle of the spiral does all four.", cards=[
            ["1. Objectives", "Decide goals, alternatives and constraints for this loop."],
            ["2. Risk analysis", "Identify and reduce the biggest risks, for example by building a prototype."],
            ["3. Develop and test", "Build and test the next version of the product."],
            ["4. Plan the next loop", "Review with the client and plan the next cycle."]]),
        T("Spiral suits large, expensive or risky projects where risks must be managed early. Its drawbacks are the cost of repeated risk analysis, the need for skilled risk assessors, and the difficulty of fixing an end date."),
        H("Agile and Scrum"),
        D("**Agile** development builds software in short cycles, delivering a working version each time, and welcomes changing requirements. It values individuals and teamwork, working software, customer collaboration and responding to change more than rigid plans and heavy documents.", title="Definition: Agile"),
        D("**Scrum** is the most common Agile framework. Work is done in fixed periods of 1 to 4 weeks called **sprints**. At the end of each sprint the team has a usable **increment** of the product.", title="Definition: Scrum"),
        KEY("Scrum: roles, events, artefacts", "Learn all three groups.", cards=[
            ["Roles", "**Product Owner**: speaks for the users and decides priorities in the backlog. **Scrum Master**: helps the team follow Scrum and removes obstacles. **Development Team**: designs, builds and tests; organises itself."],
            ["Events", "**Sprint planning** (choose items for the sprint). **Daily scrum** (a 15-minute meeting: what I did, what I will do, any blockers). **Sprint review** (show the increment to stakeholders). **Sprint retrospective** (the team looks at how to improve)."],
            ["Artefacts", "**Product backlog**: ordered list of everything wanted. **Sprint backlog**: the items chosen for the current sprint. **Increment**: the working product at the end of the sprint."]]),
        EX("Worked example 1: tracking progress with story points", intro=(
            "A product backlog totals 60 story points. The team completes 14, 10 and 12 points in sprints 1 to 3. How many points remain, what is the average velocity and how many more sprints are needed?"), steps=[
            S("Points remaining", math=r"60 - 14 - 10 - 12 = 24"),
            S("Velocity", math=r"(14 + 10 + 12) / 3 = 12 \text{ points per sprint}", text="Velocity is the average work completed per sprint."),
            S("Sprints needed", math=r"24 / 12 = 2", text="Two more sprints, if the velocity stays the same. Backlogs and velocity are estimates, so the forecast may change."),
        ]),
        CODE("""
backlog = 60
done = [14, 10, 12]
remaining = backlog
for i, d in enumerate(done, 1):
    remaining -= d
    print("after sprint", i, "completed", d, "remaining", remaining)
velocity = sum(done) / len(done)
print("average velocity", velocity)

# Output (run):
# after sprint 1 completed 14 remaining 46
# after sprint 2 completed 10 remaining 36
# after sprint 3 completed 12 remaining 24
# average velocity 12.0
""", "python", title="Velocity check"),
        H("Choosing a model"),
        EX("Worked example 2: choose and justify", intro="Choose Waterfall, Spiral or Agile Scrum for each project.", steps=[
            S("A mobile money app for a start-up, with ideas that will change as customers try it", text="Agile Scrum: frequent working releases and feedback; the requirements will change."),
            S("A flight-control system for a new aircraft, expensive, with serious risks and strict rules", text="Spiral (or Waterfall with heavy documentation): risks must be analysed early and carefully."),
            S("A school timetable program for a fixed set of rules written down by the ministry, to be built once", text="Waterfall: requirements are fixed and well understood, so a plan-driven approach is efficient."),
        ]),
        KEY("Quick comparison", "Use this as a revision summary.", cards=[
            ["Waterfall", "Plan-driven, linear, late delivery, changes costly."],
            ["Spiral", "Iterative, risk-driven, suits large risky projects."],
            ["Agile Scrum", "Iterative, time-boxed sprints, frequent delivery, welcomes change."]]),
        H("Common mistakes"),
        MISTAKE("Saying Agile means no planning or no documents", "Agile plans in short cycles and still documents what is needed. It prefers working software to heavy documents."),
        MISTAKE("Saying Waterfall can never go back", "In practice teams sometimes return, but the model itself treats stages as complete. Going back is expensive."),
        MISTAKE("Confusing the Scrum Master with a manager", "The Scrum Master serves the team by removing obstacles. The Product Owner sets priorities; the team decides how to do the work."),
        QUIZ("Which model puts risk analysis in every cycle?",
             ["Waterfall", "Spiral", "Agile Scrum", "None of them"], 1,
             "In the Spiral model each loop includes a risk analysis step.",
             feedback=["Waterfall has no repeating risk step.", "", "Scrum focuses on short sprints and feedback, not formal risk analysis loops.", "Spiral does."]),
        QUIZ("Who decides the order of items in the product backlog?",
             ["The Scrum Master", "The Product Owner", "Each developer alone", "The testers"], 1,
             "The Product Owner represents the users and sets the priority order.",
             feedback=["The Scrum Master helps with the process, not the priorities.", "", "The team chooses how to build, but priorities come from the Product Owner.", "Testers are part of the development team."]),
        H("Practice questions"),
        PQ("List the stages of the software development life cycle in order. [3 marks]",
           "Requirements, design, implementation (coding), testing, deployment, maintenance. (1 mark for at least three correct stages in order, 2 marks for five, 3 marks for all six.)"),
        PQ("Give two advantages and two disadvantages of the Waterfall model. [4 marks]",
           "Advantages: simple and easy to manage with clear stages (1); full documentation is produced, and it suits fixed requirements (1). Disadvantages: working software appears only at the end (1); changes and late-found errors are costly (1)."),
        PQ("A team uses Scrum. Describe the purpose of the daily scrum and the sprint review. [4 marks]",
           "Daily scrum: a short (about 15 minutes) meeting where each member says what was done, what is planned and what blocks them (2). Sprint review: at the end of a sprint the team shows the working increment to the stakeholders and gets feedback (2)."),
        PQ("A company will build a banking system with high security risks and a large budget. Recommend a development model and justify the choice. [3 marks]",
           "Spiral model (1). It analyses risk in each loop, which is important for security (1). Prototypes are built and reviewed by the client in each cycle, reducing the chance of costly mistakes (1). (An answer for Waterfall or Agile could also gain marks if well justified.)"),
        SUM("SDLC stages: requirements, design, implementation, testing, deployment, maintenance.",
            "Waterfall is linear and plan-driven; changes are costly.",
            "Spiral repeats loops with risk analysis in each; suits large risky projects.",
            "Agile Scrum works in short sprints with a Product Owner, Scrum Master and team; artefacts are the product backlog, sprint backlog and increment.",
            "Velocity = average story points completed per sprint; use it to forecast.",
            "Exam link: Paper 2 asks for comparisons and recommendations; Paper 1 asks for definitions."),
    ],
))


LESSONS.append(lesson(
    module=NET, topic="Software development",
    title="Data flow diagrams and entity-relationship diagrams",
    slug="csb-dfd-and-erd",
    minutes=26,
    summary="Draw and read data flow diagrams (context and level 1) with their rules, and entity-relationship diagrams with entities, attributes, keys and one-to-many and many-to-many relationships turned into database tables.",
    objectives=[
        "Name the four DFD symbols and apply the rules for drawing a correct DFD",
        "Draw a context diagram and a level 1 DFD for a simple system",
        "Draw an ERD with entities, attributes, primary keys and cardinality",
        "Resolve a many-to-many relationship with a link entity and write the tables in SQL",
    ],
    key_concepts=["Data flow diagram", "External entity", "Process", "Data store", "Data flow", "ERD", "Primary key", "Foreign key", "Cardinality", "Link entity"],
    blocks=[
        H("Introduction"),
        T("Before building a system, analysts draw pictures so that clients and programmers agree on what it will do. Two common pictures answer different questions. "
          "A **data flow diagram (DFD)** shows how data moves through the system: who sends it, what happens to it, where it is stored. "
          "An **entity-relationship diagram (ERD)** shows what data is kept and how the items are connected. The example in this lesson is a fee system for a school in Bafoussam."),
        H("Data flow diagrams"),
        KEY("The four DFD elements", "Every DFD is made from these four.", cards=[
            ["External entity", "A person or system outside the one being studied that sends or receives data (parent, ministry, bank). Drawn as a square."],
            ["Process", "An action that changes data: input becomes output. Name it with a verb and number it. Drawn as a circle or rounded rectangle."],
            ["Data store", "A place where data rests: a file or database table. Drawn between two lines, labelled D1, D2."],
            ["Data flow", "An arrow showing data moving. Label every arrow with the name of the data."]]),
        KEY("Rules for a correct DFD", "Examiners check these.", cards=[
            ["Rule 1", "Data flows only through a process. Never directly entity to entity, entity to store or store to store."],
            ["Rule 2", "Every process has at least one input and one output."],
            ["Rule 3", "Label every flow, with a noun that describes the data. No control or sequence is shown."],
            ["Rule 4", "Levels must balance: the inputs and outputs of a process at level 1 must match the flows in the parent diagram."]]),
        T("A **context diagram** (level 0) shows the whole system as a single process in the middle, with the external entities and the data flows to and from them. "
          "A **level 1 DFD** splits that process into its main sub-processes and shows the data stores."),
        CODE("""
Context diagram: School fee system

Parent --- payment details --->  [ 0  Fee system ] --- receipt ---> Parent
Bursar --- fee rates --------->  [              ] --- fee report -> Bursar
""", "text", title="Level 0"),
        IMG("al-csb-dfd-fees.svg",
            "Level 1 DFD of a school fee system: Parent sends payment details to process 1 Record payment, which writes to store D1 Payments and returns a receipt. Process 2 Update balance reads D1 and updates D2 Accounts. Process 3 Produce report reads D2 and sends a fee report to Bursar.",
            caption="Figure 1. Level 1 DFD for the school fee system."),
        EX("Worked example 1: checking a DFD", intro="A student draws an arrow labelled 'fees' from Parent directly to the data store D2 Accounts. What is wrong and how is it fixed?", steps=[
            S("Spot the rule", text="Data flows from an external entity directly to a store, with no process between them. This breaks rule 1."),
            S("Fix", text="Add a process (for example 1 Record payment). The flow becomes Parent to process 1 (payment details), then process 1 to D2 (payment record)."),
            S("Recheck", text="Process 1 now has an input and an output, and all arrows are labelled."),
        ]),
        H("Entity-relationship diagrams"),
        D("An **entity** is a thing about which data is stored (Student, Class). Its **attributes** are the facts stored (name, date of birth). A **relationship** is a link between entities (a student **belongs to** a class). "
          "Each entity has a **primary key**, an attribute (or group) whose value is unique for every record, such as student_id.", title="Definition: entity, attribute, relationship"),
        D("**Cardinality** states how many of one entity can be linked to the other: **one-to-one (1:1)**, **one-to-many (1:M)** or **many-to-many (M:N)**. A **foreign key** is an attribute in one table that holds the primary key of another table, creating the link.", title="Definition: cardinality and foreign key"),
        CODE("""
CLASS (1) ----< STUDENT (M)       one class has many students
STUDENT (M) >----< SUBJECT (M)    a student takes many subjects and a subject has many students

Resolve M:N with a link entity ENROLMENT:

CLASS (1) ----< STUDENT (1) ----< ENROLMENT >---- (1) SUBJECT
   (the crow's foot < is on the 'many' side)

CLASS     (class_id PK, class_name)
STUDENT   (student_id PK, name, class_id FK)
SUBJECT   (subject_id PK, title)
ENROLMENT (student_id FK, subject_id FK)   PK = both together
""", "text", title="From many-to-many to tables"),
        T("A many-to-many relationship cannot be stored directly in a relational database. A **link entity** (also called a junction or associative entity) sits between the two, turning it into two one-to-many relationships. "
          "Its primary key is the pair of foreign keys together."),
        EX("Worked example 2: from the diagram to SQL", intro="Create the tables, insert data and query who studies which subject.", steps=[
            S("Create tables", text="The foreign key in STUDENT refers to CLASS. ENROLMENT has a composite primary key, which prevents the same student being enrolled twice in a subject."),
            S("Insert and join", text="A join through ENROLMENT lists each student with each subject taken."),
            S("Test the rules", text="Inserting a duplicate enrolment pair fails, and so does a student with a class that does not exist (foreign key check)."),
        ]),
        CODE("""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript('''
CREATE TABLE class   (class_id TEXT PRIMARY KEY, class_name TEXT);
CREATE TABLE student (student_id INTEGER PRIMARY KEY, name TEXT,
                      class_id TEXT REFERENCES class(class_id));
CREATE TABLE subject (subject_id TEXT PRIMARY KEY, title TEXT);
CREATE TABLE enrolment (student_id INTEGER REFERENCES student(student_id),
                        subject_id TEXT REFERENCES subject(subject_id),
                        PRIMARY KEY (student_id, subject_id));
INSERT INTO class VALUES ('L6S', 'Lower Sixth Science'), ('U6A', 'Upper Sixth Arts');
INSERT INTO student VALUES (1, 'Ngu', 'L6S'), (2, 'Fanta', 'L6S'), (3, 'Eto', 'U6A');
INSERT INTO subject VALUES ('CS', 'Computer Science'), ('MA', 'Mathematics');
INSERT INTO enrolment VALUES (1, 'CS'), (1, 'MA'), (2, 'CS'), (3, 'MA');
''')
print(db.execute("SELECT class_id, COUNT(*) FROM student GROUP BY class_id ORDER BY class_id").fetchall())
print(db.execute('''SELECT s.name, sub.title FROM student s
                    JOIN enrolment e ON e.student_id = s.student_id
                    JOIN subject sub ON sub.subject_id = e.subject_id
                    ORDER BY s.name, sub.title''').fetchall())
try:
    db.execute("INSERT INTO enrolment VALUES (1, 'CS')")
except sqlite3.IntegrityError as e:
    print("duplicate pair rejected:", e)
try:
    db.execute("INSERT INTO student VALUES (4, 'Mbah', 'XXX')")
except sqlite3.IntegrityError as e:
    print("bad foreign key rejected:", e)

# Output (run):
# [('L6S', 2), ('U6A', 1)]
# [('Eto', 'Mathematics'), ('Fanta', 'Computer Science'), ('Ngu', 'Computer Science'), ('Ngu', 'Mathematics')]
# duplicate pair rejected: UNIQUE constraint failed: enrolment.student_id, enrolment.subject_id
# bad foreign key rejected: FOREIGN KEY constraint failed
""", "python", title="The ERD as tables, checked with sqlite3"),
        H("DFD or ERD?"),
        KEY("Which diagram answers which question", "Do not mix them up.", cards=[
            ["DFD", "Shows the movement and processing of data: sources, processes, stores, destinations. Does not show data types or relationships between records."],
            ["ERD", "Shows the structure of the stored data: entities, attributes, keys and relationships. Does not show processing or the order of events."]]),
        H("Common mistakes"),
        MISTAKE("Joining two external entities with an arrow", "Everything happens inside the system. Draw a process between them. Data flows between outside entities are outside the system boundary."),
        MISTAKE("Naming a process with a noun", "Processes do something: 'Record payment', not 'Payment'. Flows and stores take noun names."),
        MISTAKE("Leaving a many-to-many relationship unresolved", "Add a link entity. Otherwise the tables would need repeating groups."),
        MISTAKE("Putting the foreign key on the wrong side", "In a one-to-many link, the foreign key goes in the table on the 'many' side (student holds class_id)."),
        QUIZ("A teacher teaches many classes and each class has many teachers. How is this stored in a relational database?",
             ["One table with a repeated list of classes in each teacher row", "A link table holding the teacher id and class id, with both together as the primary key",
              "A foreign key in the teacher table only", "One table with two primary keys"], 1,
             "A many-to-many relationship is resolved with a link entity that has two one-to-many relationships.",
             feedback=["Repeating groups break relational design.", "", "A single foreign key would allow only one class per teacher.", "A table has one primary key (possibly a combination of attributes)."]),
        QUIZ("Which rule does the DFD flow Customer to Data store D1 break?",
             ["Every process needs an output", "Data must pass through a process", "Flows must be labelled", "Stores need a number"], 1,
             "Data flows must go through a process, never directly from an external entity to a data store.",
             feedback=["No process is involved in that flow.", "", "Labelling is a separate rule.", "The numbering is not the problem here."]),
        H("Practice questions"),
        PQ("List the four elements of a data flow diagram and say what each shows. [4 marks]",
           "External entity: a person or system outside the system that sends or receives data (1). Process: an activity that transforms input data into output data (1). Data store: where data is kept (1). Data flow: an arrow showing data moving, labelled with the data name (1)."),
        PQ("A library lends books to members. Draw a context diagram described in words: give the external entities, the single process and at least three data flows. [4 marks]",
           "External entities: Member and Librarian (1). Single process: Library system (1). Flows: Member to system: book request or membership details; system to Member: loan receipt or due date; Librarian to system: new book details; system to Librarian: overdue list (any three flows, 2)."),
        PQ("Each lecturer teaches many modules and each module is taught by one lecturer. Give the cardinality and say where the foreign key is placed. [3 marks]",
           "One-to-many from lecturer to module (1). The foreign key lecturer_id is in the module table, the 'many' side (1) and refers to the primary key of lecturer (1)."),
        PQ("Students and clubs have a many-to-many relationship. Describe how you would store it and give the primary key of the new table. [3 marks]",
           "Create a link table Membership (1) with the foreign keys student_id and club_id (1). The primary key is the two together (a composite key) (1)."),
        SUM("DFD: external entity, process, data store, data flow; data flows only through processes; every process has input and output.",
            "Context diagram = one process; level 1 = its sub-processes and stores.",
            "ERD: entities, attributes, primary key, relationships and cardinality (1:1, 1:M, M:N).",
            "Foreign key goes on the 'many' side; a many-to-many relation needs a link entity.",
            "DFD shows data movement; ERD shows data structure.",
            "Exam link: Paper 2 asks for a DFD or ERD to be drawn or corrected; Paper 1 asks for definitions."),
    ],
))


LESSONS.append(lesson(
    module=NET, topic="Software development",
    title="UML: use case, class and sequence diagrams",
    slug="csb-uml-diagrams",
    minutes=26,
    summary="Read and draw the three most-used UML diagrams: use case diagrams (actors and use cases), class diagrams (attributes, operations, visibility, inheritance, association and multiplicity) and sequence diagrams (lifelines and messages), and turn a class diagram into code.",
    objectives=[
        "Draw a use case diagram with actors, a system boundary and include or extend relationships",
        "Draw a class diagram with attributes, operations, visibility, inheritance, association and multiplicity",
        "Read a sequence diagram showing messages between objects in time order",
        "Translate a class diagram into Python code",
    ],
    key_concepts=["UML", "Actor", "Use case", "Class", "Attribute", "Operation", "Inheritance", "Association", "Multiplicity", "Sequence diagram"],
    blocks=[
        H("Introduction"),
        T("When a team of programmers in different towns builds one system, they need a common language of pictures. **UML (Unified Modeling Language)** is a standard set of diagrams for describing software. "
          "In this lesson we use a mobile money savings service. We study three diagrams that answer three questions: "
          "what does the system do for its users (use case), what things does it contain (class), and what happens in what order (sequence)."),
        H("Use case diagrams"),
        D("A **use case diagram** shows the **actors** (people or other systems that use the system) as stick figures, the **use cases** (things the system does for them) as ovals, and a rectangle called the **system boundary** around the use cases.", title="Definition: use case diagram"),
        CODE("""
 +----------------------- Mobile money system -----------------------+
 |                                                                   |
 |   (Check balance)                                                 |
 |        |                                                          |
 | Customer ---- (Send money) ......<<include>>......> (Verify PIN)  |
 |        |                                                          |
 |   (Deposit cash) <---- Agent                                      |
 |        .                                                          |
 |        . <<extend>>                                               |
 |   (Report fault)                                                  |
 +-------------------------------------------------------------------+
""", "text", title="Use case diagram (text form)"),
        KEY("Relationships between use cases", "Two special arrows.", cards=[
            ["include", "The base use case always uses the included one. Send money always includes Verify PIN."],
            ["extend", "Adds optional behaviour in some cases. Report fault extends Deposit cash only when something goes wrong."]]),
        T("Use case diagrams show **what** the system offers, not how. Each use case is a verb phrase: 'Send money'."),
        H("Class diagrams"),
        D("A **class diagram** shows the classes, their contents and their relationships. A class is drawn as a box with three compartments: the **name**, the **attributes** (data) and the **operations** (methods).", title="Definition: class diagram"),
        KEY("Symbols to learn", "Visibility, relationships and multiplicity.", cards=[
            ["Visibility", "+ public (visible everywhere); - private (only inside the class); # protected (the class and its subclasses)."],
            ["Inheritance", "An arrow with a hollow triangle head from the subclass to the superclass (SavingsAccount is an Account). The subclass inherits attributes and operations."],
            ["Association", "A plain line between classes that know each other. A diamond marks a stronger whole-part link: aggregation (hollow diamond: parts can exist alone) and composition (solid diamond: parts die with the whole)."],
            ["Multiplicity", "Numbers at the ends of a line: 1, 0..1, or 1 to many. A customer has 1 to many accounts; each account belongs to exactly 1 customer."]]),
        IMG("al-csb-uml-class.svg",
            "UML class diagram: Customer (name, openAccount) is linked, 1 to many, with Account (owner, balance, deposit, withdraw, getBalance). SavingsAccount (rate, addInterest) is joined to Account by an inheritance arrow.",
            caption="Figure 1. A class diagram for the savings service."),
        EX("Worked example 1: from diagram to code", intro="Write Python for Account, SavingsAccount and Customer from the diagram.", steps=[
            S("Account", text="Attributes owner (public) and balance (private, written _balance). Operations deposit, withdraw and get_balance."),
            S("SavingsAccount inherits Account", text="class SavingsAccount(Account). It adds the attribute rate and the operation add_interest, and calls super().__init__ for the inherited attributes."),
            S("Customer has 1 to many accounts", text="An association becomes an attribute: a list accounts in Customer, plus open_account to add one."),
            S("Test", text="Run the code and check the results by hand: a savings account of 1000 at 5 percent interest has 1050 after add_interest."),
        ]),
        CODE("""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if amount > self._balance:
            return False
        self._balance -= amount
        return True
    def get_balance(self):
        return self._balance

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate
    def add_interest(self):
        self.deposit(self._balance * self.rate)

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    def open_account(self, account):
        self.accounts.append(account)

c = Customer("Ngu")
s = SavingsAccount("Ngu", 1000, 0.05)
c.open_account(s)
s.add_interest()
print(s.get_balance())
print(s.withdraw(5000), s.withdraw(50), s.get_balance())
print(isinstance(s, Account), len(c.accounts))

# Output (run):
# 1050.0
# False True 1000.0
# True 1
""", "python", title="The class diagram as code"),
        H("Sequence diagrams"),
        D("A **sequence diagram** shows how objects interact over time. Each object has a vertical dashed **lifeline**; horizontal arrows are **messages** sent from one object to another. Time runs from top to bottom.", title="Definition: sequence diagram"),
        CODE("""
Customer          Phone app           Server            Bank
   |  enter amount     |                 |                |
   |------------------>|                 |                |
   |                   | sendMoney(amt)  |                |
   |                   |---------------->|                |
   |                   |                 | checkBalance() |
   |                   |                 |--------------->|
   |                   |                 |   balance OK   |
   |                   |                 |<- - - - - - - -|
   |                   |  confirmation   |                |
   |                   |<- - - - - - - - |                |
   |  "Money sent"     |                 |                |
   |<- - - - - - - - - |                 |                |
""", "text", title="Sequence diagram: sending money"),
        T("Solid arrows are calls; dashed arrows are returns or replies. The order of the arrows from top to bottom is the order of events."),
        EX("Worked example 2: reading the sequence diagram", intro="State the order of events and which object checks the balance.", steps=[
            S("Step 1", text="The customer enters an amount in the phone app."),
            S("Step 2", text="The app sends sendMoney(amt) to the server."),
            S("Step 3", text="The server asks the bank to checkBalance(); the bank replies 'balance OK'."),
            S("Step 4", text="The server confirms to the app, and the app shows 'Money sent' to the customer. The **bank** checks the balance."),
        ]),
        H("Which diagram?"),
        KEY("Use the right diagram", "A choice you may be asked to make.", cards=[
            ["Use case", "What the system does for each type of user (requirements)."],
            ["Class", "The static structure: classes, data, methods, relationships."],
            ["Sequence", "The dynamic behaviour: messages between objects in time order for one scenario."]]),
        H("Common mistakes"),
        MISTAKE("Drawing the inheritance arrow the wrong way", "The arrow points from the subclass to the superclass (SavingsAccount to Account)."),
        MISTAKE("Putting attributes in the use case diagram", "A use case diagram has actors and use cases only. Data and methods belong to the class diagram."),
        MISTAKE("Mixing include and extend", "Include is always done as part of the base use case. Extend is optional and conditional."),
        MISTAKE("Showing every attribute as public", "Data attributes are normally private (-) and reached through public operations (+)."),
        QUIZ("Which UML diagram would you draw to show the messages exchanged between a phone app, a server and a bank in time order?",
             ["Use case diagram", "Class diagram", "Sequence diagram", "Entity-relationship diagram"], 2,
             "A sequence diagram shows messages between objects over time.",
             feedback=["A use case diagram shows what users can do, not the message order.", "A class diagram shows structure, not behaviour in time.", "", "An ERD is not UML; it shows stored data."]),
        QUIZ("In a class diagram, SavingsAccount is joined to Account by an arrow with a hollow triangle. What does this mean?",
             ["SavingsAccount contains Account", "SavingsAccount inherits from Account", "Account uses SavingsAccount once", "The two classes are the same"], 1,
             "A hollow triangle arrow shows inheritance: SavingsAccount is a kind of Account.",
             feedback=["Containment is shown with a diamond.", "", "A plain association line shows use.", "They are two classes in an is-a relationship."]),
        H("Practice questions"),
        PQ("Draw (describe) a use case diagram for an online school registration system with the actors Student and Administrator. Give at least four use cases. [4 marks]",
           "Actors Student and Administrator outside a system boundary rectangle (1). Use cases such as: Register for classes, View timetable (Student); Approve registration, Manage courses (Administrator) (2 for any four, in ovals). Lines join each actor to the use cases they take part in (1)."),
        PQ("A class Teacher has the private attribute name and the public operation getName(). Show the class box and explain the visibility symbols. [3 marks]",
           "Box with three compartments: Teacher / - name / + getName() (1). The minus sign means private: only the class can access the attribute (1). The plus sign means public: other classes can call the operation (1)."),
        PQ("Class Vehicle has subclasses Bus and Taxi. State two things that Bus inherits and how inheritance is drawn. [3 marks]",
           "Bus inherits the attributes and operations of Vehicle (1+1, for example registration number and move()). Inheritance is drawn as an arrow with a hollow triangle head from Bus (and Taxi) to Vehicle (1)."),
        PQ("Explain the difference between a class diagram and a sequence diagram. [2 marks]",
           "A class diagram shows the static structure of the system: classes, attributes, operations and relationships (1). A sequence diagram shows how objects interact in time order through messages for one scenario (1)."),
        SUM("UML gives standard diagrams: use case (what), class (structure), sequence (behaviour in time).",
            "Use case diagram: actors, use cases, system boundary, include and extend.",
            "Class diagram: name, attributes, operations; + public, - private; inheritance arrow to the superclass; multiplicity such as 1 to many.",
            "A class diagram converts into code: attributes become variables, associations become references or lists.",
            "Sequence diagram: lifelines, solid call arrows, dashed returns, time downward.",
            "Exam link: Paper 2 asks for UML diagrams to be drawn or interpreted; Paper 1 asks which diagram to use."),
    ],
))


# ================================================================== Procedural Programming
LESSONS.append(lesson(
    module=PROC, topic="Structured programming",
    title="Functions, parameters, return values and scope",
    slug="csb-functions-parameters-scope",
    minutes=24,
    summary="Design a program as small functions, pass information with parameters and return values (including defaults and keyword arguments), see how Python passes references to mutable and immutable objects, and predict local, global and enclosing scope.",
    objectives=[
        "Break a problem into functions using top-down decomposition",
        "Use parameters, arguments, default and keyword arguments and return several values",
        "Explain why a function changes a list passed to it but not an integer",
        "Predict scope with the local, enclosing, global and built-in rule and use global correctly",
    ],
    key_concepts=["Structured programming", "Function", "Parameter and argument", "Return value", "Default argument", "Mutable and immutable", "Local scope", "Global scope", "Side effect"],
    blocks=[
        H("Introduction"),
        T("A shopkeeper in Mokolo keeps accounts on a long sheet. When the shop grows, one long sheet becomes impossible to check. She splits it: one page for stock, one for sales, one for debts. "
          "**Structured programming** does the same with code. A big problem is divided into small, named parts, each doing one job, called **subroutines** (functions or procedures). "
          "The overview lesson introduced these. Here we look at how information goes into and out of functions and where names are visible."),
        D("**Top-down decomposition** means starting with the whole task and repeatedly splitting it into smaller tasks until each can be written as one short function. "
          "A good function has one clear job, a descriptive name, and does not depend on hidden global data.", title="Definition: top-down decomposition"),
        CODE("""
Task: print a customer's bill
  1 get the prices                 read_prices()
  2 add up the prices              total(prices)
  3 apply a discount               apply_discount(total, rate)
  4 print the bill                 show_bill(final)
""", "text", title="Decomposition of one task"),
        H("Parameters, arguments and return values"),
        D("A **parameter** is a name in the function definition. An **argument** is the value given when the function is called. A function sends a result back with **return**; a function with no return gives back None.", title="Definition: parameter, argument, return"),
        T("Python allows **default arguments** (used when the caller gives no value) and **keyword arguments** (the caller names the parameter, so order does not matter). A function can return several values at once as a tuple."),
        CODE("""
def apply_discount(price, rate=0.1):
    return price * (1 - rate)

def stats(marks):
    return min(marks), max(marks), sum(marks) / len(marks)

print(apply_discount(5000))
print(apply_discount(5000, 0.25))
print(apply_discount(rate=0.5, price=800))
lo, hi, avg = stats([12, 15, 9, 18])
print(lo, hi, avg)

# Output (run):
# 4500.0
# 3750.0
# 400.0
# 9 18 13.5
""", "python", title="Defaults, keywords and multiple return values"),
        EX("Worked example 1: trace the calls", intro="Explain each output of the program above.", steps=[
            S("apply_discount(5000)", text="rate takes the default 0.1: 5000 x (1 - 0.1) = 4500.0."),
            S("apply_discount(5000, 0.25)", text="5000 x 0.75 = 3750.0."),
            S("apply_discount(rate=0.5, price=800)", text="Names make the order irrelevant: 800 x 0.5 = 400.0."),
            S("stats([12, 15, 9, 18])", text="min is 9, max is 18, sum is 54 and 54 / 4 = 13.5. The tuple is unpacked into lo, hi, avg."),
        ]),
        H("What does a function change?"),
        T("Python passes **a reference to the object**. If the object is **mutable** (a list, a dictionary), the function can change it and the caller sees the change. "
          "If the object is **immutable** (an integer, a string, a tuple), 'changing' it creates a new object and the caller's variable is unchanged."),
        CODE("""
def add_item(basket, item):
    basket.append(item)           # changes the caller's list
    return len(basket)

def rebind(n):
    n = n + 1                     # new local object
    return n

b = ["yam"]
print(add_item(b, "plantain"), b)
n = 7
print(rebind(n), n)

# Output (run):
# 2 ['yam', 'plantain']
# 8 7
""", "python", title="Mutable and immutable arguments"),
        T("A change made to something outside the function is a **side effect**. Side effects make programs harder to understand. Prefer functions that take inputs and return results."),
        H("Scope"),
        D("The **scope** of a name is the part of the program where it can be used. A **local** variable is created inside a function and exists only while it runs. A **global** variable is created at the top level and can be read anywhere. "
          "Python looks names up in this order: **L**ocal, **E**nclosing function, **G**lobal, **B**uilt-in (LEGB).", title="Definition: scope"),
        CODE("""
counter = 0
def bad():
    try:
        counter = counter + 1       # counter is local here, but has no value yet
    except UnboundLocalError:
        return "UnboundLocalError"

def good():
    global counter                  # use the global name
    counter = counter + 1
    return counter

print(bad())
print(good(), counter)

x = "global"
def outer():
    x = "outer"
    def inner():
        return x                    # found in the enclosing function
    return inner()
def shadow():
    x = "local"                     # hides the global x inside the function
    return x
print(outer(), x)
print(shadow(), x)

# Output (run):
# UnboundLocalError
# 1 1
# outer global
# local global
""", "python", title="Scope in action"),
        EX("Worked example 2: why does bad() fail?", intro="Explain the UnboundLocalError.", steps=[
            S("Assignment makes a name local", text="Because counter is assigned inside bad(), Python treats it as a local variable for the whole function."),
            S("Read before write", text="On the right-hand side, counter + 1 reads the local counter before it has a value, so Python raises UnboundLocalError."),
            S("Fix", text="Declare global counter as in good(), or better, pass counter in as a parameter and return the new value."),
        ]),
        H("Common mistakes"),
        MISTAKE("Printing instead of returning", "A function that prints a result gives nothing back, so its value cannot be used in later calculations. Return the value and print outside."),
        MISTAKE("Expecting an integer argument to change", "The function gets its own name for the same integer; n = n + 1 makes a new integer and the caller keeps the old one."),
        MISTAKE("Using a mutable default argument", "def f(x, acc=[]) creates the list once, so every call without acc shares it. Use acc=None and create a new list inside."),
        MISTAKE("Relying on globals", "A function that quietly reads or writes globals is hard to test and reuse. Pass values in as parameters instead."),
        QUIZ("A function is def f(n): n = n + 1; return n. The caller runs k = 5 and then print(f(k), k). What is printed?",
             ["5 5", "6 5", "6 6", "5 6"], 1,
             "The function builds a new local value, 5 + 1 = 6, and returns it. The caller's variable is not changed, so it prints 6 then 5.",
             hint="Is the argument an integer, and is it mutable?",
             feedback=["The returned value is 6.", "", "The caller's own n is unchanged.", "The order is returned value first, then n."]),
        QUIZ("Which kind of variable exists only while its function is running?",
             ["Global", "Local", "Built-in", "Constant"], 1,
             "A local variable is created when the function starts and disappears when it returns.",
             feedback=["Global variables exist for the whole run.", "", "Built-ins like len are always available.", "A constant is a value that does not change; it can be global or local."]),
        H("Practice questions"),
        PQ("Distinguish between a parameter and an argument. [2 marks]",
           "A parameter is the name listed in the function definition (1). An argument is the actual value passed when the function is called (1)."),
        PQ("Write a Python function total_with_tax(price, rate=0.19) that returns the price with tax added. State the results of total_with_tax(1000) and total_with_tax(1000, 0.1). [3 marks]",
           "def total_with_tax(price, rate=0.19): return price * (1 + rate) (1). total_with_tax(1000) = 1190 using the default rate (1). total_with_tax(1000, 0.1) = 1100 (1). (Floating point may print 1190.0 and 1100.0.)"),
        PQ("Explain why a function that appends to a list parameter changes the caller's list, but a function that adds 1 to an integer parameter does not change the caller's integer. [3 marks]",
           "Python passes a reference to the object (1). A list is mutable, so append changes the same object that the caller sees (1). An integer is immutable, so n + 1 creates a new integer bound to the local name only (1)."),
        PQ("Give two reasons why using global variables inside functions is poor practice. [2 marks]",
           "Functions become dependent on hidden data and are hard to reuse or test on their own (1). Any part of the program may change a global, so errors are difficult to trace (1)."),
        SUM("Structured programming splits a task into small functions, each with one job (top-down decomposition).",
            "Parameters are names in the definition; arguments are the values passed; return sends a value back.",
            "Python passes references: mutable arguments can be changed by the function; immutable ones cannot.",
            "Scope: local, enclosing, global, built-in (LEGB). Assigning to a name inside a function makes it local unless declared global.",
            "Prefer parameters and return values to globals and side effects.",
            "Exam link: Paper 2 asks you to write and trace functions and explain scope; Paper 1 tests the terms."),
    ],
))


LESSONS.append(lesson(
    module=PROC, topic="Structured programming",
    title="Recursion and the call stack",
    slug="csb-recursion-call-stack",
    minutes=26,
    summary="Write and trace recursive functions with a base case and a recursive case, draw the call stack frame by frame, count calls (Fibonacci), understand stack overflow, and compare recursion with iteration and memoisation.",
    objectives=[
        "Identify the base case and recursive case of a recursive function",
        "Trace a recursive call, showing each stack frame as it is pushed and popped",
        "Count the calls made by a recursive function and explain why naive Fibonacci is slow",
        "Explain stack overflow and compare recursion with iteration",
    ],
    key_concepts=["Recursion", "Base case", "Recursive case", "Stack frame", "Call stack", "Stack overflow", "Memoisation", "Iteration"],
    blocks=[
        H("Introduction"),
        T("Stand between two mirrors and you see a picture inside a picture inside a picture. A recursive function is like that: it solves a problem by calling itself on a smaller copy of the same problem, until the problem is so small that the answer is obvious. "
          "Counting the pages of a thick notebook can be done this way: the number of pages is one more than the number of pages left after turning one over, and a notebook with no pages left has none."),
        D("A **recursive function** is a function that calls itself. It needs a **base case**, an input for which it returns an answer directly without calling itself, and a **recursive case**, which calls itself on a smaller or simpler input that moves towards the base case.", title="Definition: recursion"),
        CODE("""
def factorial(n):
    if n == 0:                 # base case
        return 1
    return n * factorial(n - 1)    # recursive case

print(factorial(4), factorial(10))

# Output (run):
# 24 3628800
""", "python", title="Factorial: n! = n x (n-1)!, with 0! = 1"),
        H("The call stack"),
        D("Each time a function is called, the system creates a **stack frame** holding its parameters, local variables and the address to return to. Frames are kept on the **call stack**, a last-in first-out structure. "
          "A call **pushes** a new frame on the top; a return **pops** it and gives control back to the caller.", title="Definition: stack frame and call stack"),
        IMG("al-csb-stack-frames.svg",
            "The call stack when factorial(4) reaches its base case: five frames from bottom to top, factorial(4) with n=4, factorial(3) with n=3, factorial(2) with n=2, factorial(1) with n=1 and factorial(0) with n=0 on top. The top frame returns 1.",
            caption="Figure 1. The stack at the deepest point of factorial(4): five frames."),
        EX("Worked example 1: trace factorial(4)", intro="Show the calls going down and the values returned coming back up.", steps=[
            S("Going down (frames pushed)", text="factorial(4) calls factorial(3), which calls factorial(2), then factorial(1), then factorial(0). Five frames are on the stack, each waiting."),
            S("Base case", text="factorial(0) returns 1 and its frame is popped."),
            S("Coming back (frames popped)", text="factorial(1) computes 1 x 1 = 1. factorial(2) computes 2 x 1 = 2. factorial(3) computes 3 x 2 = 6. factorial(4) computes 4 x 6 = 24."),
            S("Result", text="The first call returns 24. The stack is empty again."),
        ]),
        CODE("""
factorial(4)
 -> 4 * factorial(3)
     -> 3 * factorial(2)
         -> 2 * factorial(1)
             -> 1 * factorial(0)
                 -> returns 1
             <- returns 1 * 1 = 1
         <- returns 2 * 1 = 2
     <- returns 3 * 2 = 6
 <- returns 4 * 6 = 24
""", "text", title="Trace of factorial(4)"),
        H("Thinking recursively"),
        T("To write a recursive function, ask three questions. What is the simplest case, with an obvious answer? How can I reduce the problem by one step? How do I combine the answer of the smaller problem with the current step?"),
        EX("Worked example 2: sum of the digits", intro="Write a recursive function digit_sum(n) and trace digit_sum(2749).", steps=[
            S("Base case", text="If n is below 10 it has one digit, so return n."),
            S("Recursive case", text="The last digit is n % 10. The other digits form n // 10. Return n % 10 + digit_sum(n // 10)."),
            S("Trace", text="digit_sum(2749) = 9 + digit_sum(274) = 9 + 4 + digit_sum(27) = 9 + 4 + 7 + digit_sum(2) = 9 + 4 + 7 + 2 = 22."),
        ]),
        EX("Worked example 3: recursive binary search", intro="Search for 31 in the sorted list [3, 8, 15, 22, 31, 40, 52] (indexes 0 to 6).", steps=[
            S("Call 1: lo=0, hi=6", text="mid = 3, a[3] = 22. 22 is less than 31, so search the right half: lo=4."),
            S("Call 2: lo=4, hi=6", text="mid = 5, a[5] = 40. 40 is more than 31, so search the left half: hi=4."),
            S("Call 3: lo=4, hi=4", text="mid = 4, a[4] = 31. Found: return index 4. The base case 'lo > hi' returns -1 for a missing value."),
            S("Depth", text="Three calls, so three frames at the deepest point. Each call halves the range, so for n items the depth is about log2 of n."),
        ]),
        CODE("""
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def bsearch(a, x, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == x:
        return mid
    if a[mid] < x:
        return bsearch(a, x, mid + 1, hi)
    return bsearch(a, x, lo, mid - 1)

a = [3, 8, 15, 22, 31, 40, 52]
print(digit_sum(2749))
print(bsearch(a, 31, 0, 6), bsearch(a, 10, 0, 6))

# Output (run):
# 22
# 4 -1
""", "python", title="Two more recursive functions"),
        H("Counting calls: Fibonacci"),
        T("The Fibonacci numbers are defined by fib(0) = 0, fib(1) = 1 and fib(n) = fib(n-1) + fib(n-2). The direct recursive version makes **two** calls each time and repeats the same work again and again."),
        CODE("""
calls = 0
def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

for n in (5, 10, 20):
    calls = 0
    print(n, fib(n), calls)

memo = {}
calls = 0
def fibm(n):
    global calls
    calls += 1
    if n in memo:
        return memo[n]
    r = n if n < 2 else fibm(n - 1) + fibm(n - 2)
    memo[n] = r
    return r
print("memoised", fibm(20), calls)

# Output (run):
# 5 5 15
# 10 55 177
# 20 6765 21891
# memoised 6765 39
""", "python", title="Number of calls: plain and memoised Fibonacci"),
        T("fib(20) makes 21 891 calls, but only 39 when answers are saved in a dictionary. Saving answers already computed is **memoisation**. The plain version's work roughly multiplies by 1.6 each time n goes up by one, so it becomes impractical for n near 50."),
        H("Stack overflow"),
        D("A **stack overflow** happens when recursion goes too deep, because there is no base case or it is never reached, and the call stack runs out of space. Python stops the program with a RecursionError (the default limit is about 1000 nested calls).", title="Definition: stack overflow"),
        CODE("""
def count_down(n):
    return count_down(n + 1)       # no base case, and n moves away from one

try:
    count_down(0)
except RecursionError:
    print("RecursionError")

# Output (run):
# RecursionError
""", "python", title="A missing base case"),
        H("Recursion or iteration?"),
        KEY("Choosing", "Every recursive function can be rewritten with a loop, and the reverse.", cards=[
            ["Recursion", "Shorter, clearer for naturally recursive problems (trees, divide and conquer, searching). Costs a stack frame per call and risks overflow."],
            ["Iteration", "Uses a loop and a few variables. Faster and uses constant memory. Can be longer to write for tree-shaped problems."]]),
        H("Common mistakes"),
        MISTAKE("Forgetting the base case", "Without it the function never stops and the stack overflows."),
        MISTAKE("A recursive call that does not get closer to the base case", "factorial(n + 1) or a call with the same value repeats for ever. Each call must make the input smaller."),
        MISTAKE("Forgetting to return the recursive result", "Writing factorial(n - 1) without return or without using the result loses the answer and gives None."),
        MISTAKE("Counting frames wrongly", "factorial(4) has frames for n = 4, 3, 2, 1 and 0: five, not four."),
        QUIZ("What is the base case in def power(b, e): if e == 0: return 1 else return b * power(b, e - 1)?",
             ["e == 0, which returns 1", "b * power(b, e - 1)", "e - 1", "return 1 whenever b is 1"], 0,
             "The base case is the branch that returns without a further call: e == 0 gives 1.",
             feedback=["", "That is the recursive case.", "That is the way the problem is made smaller.", "The test is on e, not b."]),
        QUIZ("How many stack frames exist at the deepest point of factorial(6)?",
             ["6", "7", "5", "1"], 1,
             "Frames for n = 6, 5, 4, 3, 2, 1 and 0: seven.",
             feedback=["That forgets the frame for n = 0.", "", "That is one too few.", "Only the final frame is on top; the others are still waiting below."]),
        H("Practice questions"),
        PQ("Define the terms base case and recursive case. [2 marks]",
           "Base case: an input for which the function returns a result without calling itself (1). Recursive case: the part where the function calls itself with a smaller or simpler input (1)."),
        PQ("Trace the function f(n) that returns 1 if n is 0 and otherwise n + f(n - 1) for f(3). Show the calls and the value returned by each. [4 marks]",
           "f(3) calls f(2), which calls f(1), which calls f(0) (1). f(0) returns 1 (1). f(1) returns 1 + 1 = 2 and f(2) returns 2 + 2 = 4 (1). f(3) returns 3 + 4 = 7 (1)."),
        PQ("Explain what a stack frame is and what happens to the call stack when a function returns. [3 marks]",
           "A stack frame stores the parameters, local variables and return address of one function call (1). When the function returns, its frame is popped from the top of the stack (1) and control returns to the caller using the stored address (1)."),
        PQ("Give one advantage and one disadvantage of recursion compared with iteration. [2 marks]",
           "Advantage: clear and short code for problems that are naturally recursive, such as trees or divide and conquer (1). Disadvantage: each call uses stack space, so deep recursion can overflow, and it is usually slower (1)."),
        SUM("A recursive function needs a base case and a recursive case that moves towards it.",
            "Each call pushes a stack frame (parameters, locals, return address); each return pops one. The stack is last-in first-out.",
            "factorial(n) uses n + 1 frames at its deepest.",
            "Plain Fibonacci repeats work (21 891 calls for fib(20)); memoisation reduces it to 39.",
            "No base case, or a call that does not get closer, causes stack overflow.",
            "Exam link: Paper 2 asks you to trace recursive functions and describe the stack; Paper 1 tests the terms."),
    ],
))


LESSONS.append(lesson(
    module=PROC, topic="Files and pointers",
    title="File handling: text and binary files, modes and errors",
    slug="csb-file-handling",
    minutes=24,
    summary="Open, read, write and append text files with the right mode, process a file line by line, move around a binary file with seek and tell, and handle missing files and bad data with exceptions.",
    objectives=[
        "Choose the correct file mode (r, w, a, b) and explain what each does to existing data",
        "Read a text file line by line and write or append records",
        "Use seek and tell on a binary file",
        "Handle FileNotFoundError and bad lines with try and except, and close files safely with with",
    ],
    key_concepts=["Text file", "Binary file", "File mode", "Open and close", "with statement", "Append", "File pointer", "Exception handling"],
    blocks=[
        H("Introduction"),
        T("Variables disappear when a program ends. A teacher in Kumba who types 200 marks into a program would lose them all at the end of the run, unless the program saves them in a **file** on the disk. "
          "File handling lets a program keep data between runs, read data prepared by someone else, and exchange data with other programs."),
        D("A **text file** stores characters, so a person can read it in a simple editor; lines end with a newline. A **binary file** stores raw bytes in any format (images, programs, packed numbers) and is not meant to be read as text.", title="Definition: text and binary files"),
        H("Opening a file"),
        T("Before use, a file must be **opened**. This links a file on the disk to a variable in the program (a file object) and chooses a **mode**. When finished, it must be **closed**, which saves buffered data. "
          "The **with** statement closes the file automatically, even if an error occurs, so always use it."),
        KEY("File modes", "Add b for binary: rb, wb, ab.", cards=[
            ["r", "Read. The file must already exist, or FileNotFoundError is raised."],
            ["w", "Write. Creates the file, or **erases** all existing contents. A very common cause of lost data."],
            ["a", "Append. Creates the file if needed and adds to the end without erasing."],
            ["r+", "Read and write an existing file without erasing it."]]),
        CODE("""
with open("marks.txt", "w") as f:
    f.write("Ngu,72\\n")
    f.write("Fanta,65\\n")
    f.write("Eto,88\\n")

with open("marks.txt", "a") as f:       # append, nothing is erased
    f.write("Mbah,54\\n")

total = 0
count = 0
with open("marks.txt", "r") as f:       # read one line at a time
    for line in f:
        name, mark = line.strip().split(",")
        total += int(mark)
        count += 1
        print(name, mark)
print("average", total / count)

# Output (run):
# Ngu 72
# Fanta 65
# Eto 88
# Mbah 54
# average 69.75
""", "python", title="Writing, appending and reading a text file"),
        EX("Worked example 1: follow the file", intro="Describe the contents of marks.txt after each step and explain the average.", steps=[
            S("After mode w", text="The file holds three lines: Ngu,72 / Fanta,65 / Eto,88. Each write ends with a newline character."),
            S("After mode a", text="A fourth line Mbah,54 is added at the end. The first three lines are unchanged."),
            S("Reading", text="The loop gives one line at a time. strip() removes the newline, split(',') makes [name, mark], int() converts the mark."),
            S("Average", math=r"(72 + 65 + 88 + 54) / 4 = 279 / 4 = 69.75"),
        ]),
        H("Reading in different ways"),
        T("f.read() returns the whole file as one string. f.readline() returns one line. A for loop over the file reads one line at a time and is best for large files because only one line is in memory. "
          "f.read().splitlines() returns a list of lines without newline characters."),
        H("Binary files and the file pointer"),
        T("An open file has a **file pointer**: the position of the next byte to be read or written. After opening, it is at byte 0. Reading moves it forward. f.tell() reports the position and f.seek(n) moves it to byte n."),
        CODE("""
data = bytes([72, 101, 108, 108, 111])     # the bytes for the letters H e l l o
with open("data.bin", "wb") as f:
    f.write(data)
with open("data.bin", "rb") as f:
    f.seek(1)                              # skip byte 0
    print(f.read(2), f.tell())

# Output (run):
# b'el' 3
""", "python", title="Binary file with seek and tell"),
        T("After seek(1), the pointer is at byte 1. Reading 2 bytes returns bytes 1 and 2, which are 101 and 108, the letters e and l. The pointer is then at byte 3. This random access is what makes binary files useful for records of a fixed size."),
        H("Errors and exceptions"),
        T("Files cause errors that are not the programmer's fault: the file is missing, the disk is full, or a line has the wrong format. An **exception** is an error raised at run time. "
          "The **try / except** structure lets the program react instead of crashing."),
        CODE("""
try:
    open("missing.txt")
except FileNotFoundError:
    print("file not found")

lines = ["Ngu,72", "bad line", "Eto,88"]
good = []
for line in lines:
    try:
        name, mark = line.split(",")
        good.append((name, int(mark)))
    except ValueError:
        print("skipped:", line)
print(good)

# Output (run):
# file not found
# skipped: bad line
# [('Ngu', 72), ('Eto', 88)]
""", "python", title="Handling errors"),
        EX("Worked example 2: why was 'bad line' skipped?", intro="Explain the ValueError.", steps=[
            S("split(',')", text="'bad line' has no comma, so split returns a list of one item: ['bad line']."),
            S("Unpacking", text="name, mark = ['bad line'] needs two items but there is one, so Python raises ValueError."),
            S("except ValueError", text="The handler prints a message and the loop goes on to the next line, so one bad record does not stop the whole run."),
        ]),
        EX("Worked example 3: the danger of w", intro="A program opens marks.txt with mode w to add one more mark. What happens?", steps=[
            S("Mode w erases", text="The existing four records are deleted when the file is opened."),
            S("Result", text="Only the new line remains. In the lesson's test, the file then contained just one line, ['new']."),
            S("Fix", text="Use mode a to add to the end, or read the file into a list, change the list, and write the whole list back."),
        ]),
        H("Common mistakes"),
        MISTAKE("Opening with w when you meant a", "Write mode erases the old contents. Use append mode to keep them."),
        MISTAKE("Forgetting the newline", "write() does not add a newline. Without \\n, all your records run together on one line."),
        MISTAKE("Not closing the file", "Data may stay in a buffer and never reach the disk. Use with so the file is always closed."),
        MISTAKE("Forgetting to convert text to numbers", "Everything read from a text file is a string. '72' + '65' is '7265'. Use int() or float() before calculating."),
        QUIZ("Which mode adds new data at the end of an existing text file without erasing it?",
             ["r", "w", "a", "rb"], 2,
             "Append mode a keeps the old data and writes at the end.",
             feedback=["Mode r only reads.", "Mode w erases the old contents.", "", "rb reads a binary file."]),
        QUIZ("After f.seek(2) on a binary file, f.read(3) is called. At what position is the pointer afterwards?",
             ["3", "5", "2", "0"], 1,
             "seek(2) puts the pointer at byte 2. Reading 3 bytes moves it to byte 5.",
             feedback=["It moved from 2, not from 0.", "", "That is where it started before the read.", "Seek moved it away from 0."]),
        H("Practice questions"),
        PQ("Explain the difference between opening a file in mode w and in mode a. [2 marks]",
           "Mode w creates the file or erases existing contents before writing (1). Mode a keeps the existing contents and adds new data at the end (1)."),
        PQ("Write Python code to read a file scores.txt, which has one whole number on each line, and print their total. [4 marks]",
           "total = 0 (1); with open('scores.txt', 'r') as f: (1); for line in f: total += int(line) (1, int() converts the string; a trailing newline is accepted by int); print(total) (1)."),
        PQ("Describe two things that could go wrong when a program reads a data file, and how try and except helps. [3 marks]",
           "The file may not exist (FileNotFoundError) (1). A line may have the wrong format, such as text where a number is expected (ValueError) (1). try/except catches the exception, prints a message or skips the line, and the program continues instead of crashing (1)."),
        PQ("A binary file contains the bytes 10, 20, 30, 40, 50 in that order. After f.seek(1) and f.read(2), which bytes are returned and what does f.tell() give? [3 marks]",
           "seek(1) moves to byte index 1, the second byte (1). The bytes returned are 20 and 30 (1). tell() returns 3 (1)."),
        SUM("Text files hold characters in lines; binary files hold raw bytes.",
            "Modes: r reads, w writes and erases, a appends; add b for binary.",
            "Use with open(...) as f so the file is closed automatically.",
            "Everything read from a text file is a string: convert it before calculating.",
            "The file pointer marks the next byte; seek moves it and tell reports it.",
            "try/except handles missing files and bad data. Exam link: Paper 2 asks you to write file-processing code; Paper 1 tests modes and terms."),
    ],
))


LESSONS.append(lesson(
    module=PROC, topic="Files and pointers",
    title="Pointers and memory management: addresses, dereferencing, heap",
    slug="csb-pointers-and-memory",
    minutes=26,
    summary="Understand pointers as variables that hold memory addresses: declare, take an address, dereference, do pointer arithmetic, pass by pointer, allocate and free heap memory, and avoid NULL, dangling and leak errors. Hand-traced in C; Python references compared.",
    objectives=[
        "Explain what a pointer is and read the address-of and dereference operators",
        "Hand-trace a C program using pointers with a memory table",
        "Explain pass by value versus pass by pointer using a swap function",
        "Describe dynamic allocation with malloc and free and the errors NULL pointers, dangling pointers and memory leaks",
    ],
    key_concepts=["Pointer", "Address-of operator", "Dereference", "Pointer arithmetic", "Pass by pointer", "malloc and free", "NULL pointer", "Dangling pointer", "Memory leak"],
    blocks=[
        H("Introduction"),
        T("Every house in a town has a street number, and a letter is delivered to the number, not to a description of the family. The memory of a computer is similar: each byte has a number, its **address**. "
          "A variable is a named place at some address. A **pointer** is a variable whose value is the address of another variable. Languages such as C let programmers work with addresses directly; "
          "this gives control and speed, and allows mistakes that Python protects you from."),
        D("A **pointer** is a variable that stores a memory address. In C, the **address-of operator** (the ampersand, as in &x) gives the address of x. If p holds an address, the **dereference operator** (a star written in front of p, as in Listing 1) gives the value stored at that address. Reading or writing the value through the pointer is called **dereferencing**.", title="Definition: pointer"),
        CODE("""
int x = 10;        /* an integer variable            */
int *p = &x;       /* p is a pointer to int; p holds the address of x */
*p = 99;           /* write 99 at the address in p: x is now 99       */
""", "c", title="Declaring and using a pointer"),
        T("The star has two jobs. In a declaration it means 'this variable is a pointer', so the declaration in Listing 1 says p is a pointer to an int. In an expression, a star in front of a pointer means 'the thing the pointer points to'."),
        H("A complete example, hand-traced"),
        CODE("""
#include <stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void) {
    int x = 10, y = 20;
    int *p = &x;
    *p = *p + 5;            /* line A */
    swap(&x, &y);           /* line B */
    int arr[3] = {4, 8, 12};
    int *q = arr;           /* q holds the address of arr[0] */
    q = q + 2;              /* line C */
    *q = *q - 1;            /* line D */
    printf("%d %d %d\\n", x, y, arr[2]);
    return 0;
}
""", "c", title="Listing 1. Pointers, swap and arrays"),
        T("We trace by hand. Use these made-up addresses: ints take 4 bytes; x is at 1000, y at 1004, p at 1008, arr[0] at 1012, arr[1] at 1016, arr[2] at 1020 and q at 1024. "
          "(Real addresses differ, and a pointer occupies 8 bytes on a 64-bit machine; the table is simplified to show the idea.)"),
        CODE("""
After                         x     y     p     arr[0] arr[1] arr[2]  q
int x=10,y=20                 10    20    -     -      -      -       -
int *p = &x                   10    20    1000  -      -      -       -
line A  *p = *p + 5           15    20    1000  -      -      -       -
line B  swap(&x,&y):
   a=1000, b=1004, t=*a=15
   *a = *b  -> x = 20         20    20    1000
   *b = t   -> y = 15         20    15    1000
arr = {4,8,12}                20    15    1000  4      8      12      -
int *q = arr                  20    15    1000  4      8      12      1012
line C  q = q + 2             20    15    1000  4      8      12      1020
line D  *q = *q - 1           20    15    1000  4      8      11      1020

printf prints:  20 15 11
""", "text", title="Memory table for Listing 1 (hand trace, checked with a program that models memory)"),
        EX("Worked example 1: explain lines C and D", intro="Why does q = q + 2 move the pointer by 8 bytes and not 2?", steps=[
            S("Pointer arithmetic", text="Adding 2 to a pointer to int moves it by 2 elements, that is 2 x 4 = 8 bytes. So q goes from 1012 to 1020."),
            S("Where it points", text="1020 is the address of arr[2]. In C, the value at address arr + 2 is the same thing as arr[2]."),
            S("Line D", text="Line D reads the value q points to (12, at address 1020), subtracts 1 and writes 11 back to that address, so arr[2] becomes 11."),
        ]),
        H("Pass by value and pass by pointer"),
        T("C passes arguments **by value**: the function receives a copy. A function swap(int a, int b) would swap only its own copies. To change the caller's variables, the caller passes their **addresses** (&x, &y) and the function writes through the pointers. "
          "This is called **pass by pointer** (pass by reference). It is also how a function can return more than one result."),
        H("Dynamic memory: the heap"),
        D("**Dynamic allocation** asks the system for memory while the program runs. malloc(n) reserves n bytes on the **heap** and returns a pointer to it (or NULL if there is no room). free(p) gives the memory back.", title="Definition: malloc and free"),
        CODE("""
int *a = malloc(3 * sizeof(int));   /* room for 3 ints on the heap */
if (a == NULL) {                    /* always check            */
    return 1;
}
for (int i = 0; i < 3; i++)
    a[i] = (i + 1) * 10;            /* 10, 20, 30              */
int sum = 0;
for (int i = 0; i < 3; i++)
    sum += *(a + i);                /* sum = 10 + 20 + 30 = 60 */
free(a);                            /* return the memory       */
a = NULL;                           /* a no longer points to freed memory */
""", "c", title="Listing 2. Allocate, use, free"),
        KEY("Three classic pointer errors", "These cause crashes and security holes.", cards=[
            ["NULL pointer dereference", "NULL means 'points to nothing'. Dereferencing a pointer that is NULL crashes the program. Always check malloc's result and set unused pointers to NULL."],
            ["Dangling pointer", "A pointer to memory that has been freed (or to a local variable whose function has returned). Using it reads or writes memory that is no longer yours."],
            ["Memory leak", "Memory is allocated but never freed, and the pointer is lost. Over time the program uses more and more memory."]]),
        H("What about Python?"),
        T("Python has no pointer syntax, and the interpreter manages memory and frees unused objects automatically. But every Python name is, in effect, a **reference** to an object, so aliasing exists."),
        CODE("""
a = [1, 2]
b = a              # b refers to the same list
b.append(3)
print(a, a is b)
c = a.copy()       # a new list with equal contents
print(c is a, c == a)

# Output (run):
# [1, 2, 3] True
# False True
""", "python", title="References in Python"),
        T("The first line shows aliasing: changing b changes a, as two pointers to the same memory would. The copy c is a separate object, equal in value but not identical (is gives False)."),
        H("Common mistakes"),
        MISTAKE("Confusing a pointer with the value it points to", "The pointer p is the address. The dereferenced pointer (a star in front of p) is the value at that address. Assigning to p changes where it points; assigning through the star changes the value stored there."),
        MISTAKE("Using a pointer before it points anywhere", "An uninitialised pointer holds a garbage address. Initialise to NULL or to a valid address."),
        MISTAKE("Forgetting free, or freeing twice", "Missing free leaks memory. Freeing the same block twice corrupts the heap. Set the pointer to NULL after free."),
        MISTAKE("Forgetting that pointer arithmetic counts elements", "p + 1 moves by the size of the type, not by one byte."),
        QUIZ("In C, x is 5 and p points to x. A statement adds 1 to the value that p points to. What is x now?",
             ["5", "6", "The address of x", "1"], 1,
             "The value p points to is x itself. Adding 1 through the pointer makes x equal to 6.",
             feedback=["x was changed through the pointer.", "", "x is the value, not an address.", "1 is the amount added, not the new value."]),
        QUIZ("Which is a dangling pointer?",
             ["A pointer set to NULL", "A pointer to memory that has been freed", "A pointer to a variable still in scope", "A pointer returned by a successful malloc"], 1,
             "The memory was released, but the pointer still holds its old address.",
             feedback=["NULL is a safe 'points to nothing' value.", "", "That points to valid memory.", "A fresh block is valid."]),
        H("Practice questions"),
        PQ("In the C declaration that makes the pointer p hold the address of x (see Listing 1), explain the meaning of the ampersand and of the star. [2 marks]",
           "The ampersand is the address-of operator: &x is the address of variable x (1). The star in the declaration means p is a pointer to int, which can store an address; so p is set to hold the address of x (1)."),
        PQ("p points to a (a = 3) and q points to b (b = 8). The program first copies the value q points to into the place p points to, then sets the place q points to equal to the value p points to plus 1. State the final values of a and b. [3 marks]",
           "The first step copies 8 into a, so a = 8 (1). The second step sets b to the new value of a plus 1, which is 9 (1). Final values: a = 8 and b = 9 (1)."),
        PQ("An int array arr is at address 2000 and an int takes 4 bytes. If q = arr and then q = q + 3, what address does q hold and which element does it point to? [2 marks]",
           "q holds 2000 + 3 x 4 = 2012 (1) and points to arr[3] (1)."),
        PQ("Describe two errors that can occur when a program uses dynamic memory. [4 marks]",
           "Memory leak: memory is allocated but never freed, so the program's memory use keeps growing (1+1 for explanation). Dangling pointer: a pointer still holds the address of memory that has been freed, so using it may read or corrupt data (1+1). (A NULL pointer dereference or a double free also gains marks.)"),
        SUM("A pointer stores a memory address. &x is the address of x; a star in front of the pointer gives the value at that address.",
            "Pass by pointer lets a function change the caller's variables; C normally passes copies.",
            "Pointer arithmetic moves by whole elements: p + 1 adds the size of the type.",
            "malloc reserves heap memory and may return NULL; free releases it; set the pointer to NULL afterwards.",
            "Errors: NULL dereference, dangling pointer, memory leak, double free.",
            "Python hides pointers behind references, but aliasing still exists. Exam link: Paper 2 asks you to trace pointer code or explain dynamic memory; Paper 1 tests the terms."),
    ],
))


# ================================================================== Examination
LESSONS.append(lesson(
    module=EXAM, topic="Practice paper",
    title="Approaching the Lower Sixth practice paper",
    slug="csb-exam-lower-sixth-practice-paper",
    minutes=20,
    summary="Plan your time, read multiple-choice stems carefully, eliminate wrong options, check calculations and revise by topic before the KKEVO Lower Sixth Computer Science practice paper of 40 questions.",
    objectives=[
        "Explain the format and purpose of the KKEVO practice paper and what to check with your teacher",
        "Make a time plan for 40 questions in 90 minutes, using KKEVO's suggested timings",
        "Use reading, elimination and checking techniques on multiple-choice questions",
        "Use the topic results to choose what to revise next",
    ],
    key_concepts=["Exam technique", "Time planning", "Elimination", "Checking calculations", "Revision by topic"],
    blocks=[
        H("Introduction"),
        T("You have now studied the whole of Lower Sixth Computer Science: machine models and the CPU, digital logic, operating systems, translators, networks, software development and procedural programming. "
          "The KKEVO practice paper is a chance to test all of it in one sitting, under time, before the real examinations."),
        D("The **KKEVO practice paper** is practice material written by KKEVO. It has **40 four-option multiple-choice questions** and a **90-minute** time limit in timed mode. "
          "Both the question count and the timing are KKEVO practice settings, **not** official ones. The real paper may be built differently (for example with structured questions or calculations to write out). "
          "Ask your Computer Science teacher for the real format, the number of papers and what you may bring.", title="About this paper"),
        T("The practice paper does not count towards topic mastery. It is a mirror: its results page shows your score for each topic, with links back to the lessons."),
        H("Planning your time (KKEVO advice)"),
        T("Ninety minutes for forty questions is **2 minutes 15 seconds** per question on average (90 divided by 40 = 2.25 minutes). That is a lot of time for a recall question and not much for a trace or a subnetting calculation. A plan helps you give the time where it is needed."),
        KEY("A three-pass plan", "This is a suggestion, not a rule.", cards=[
            ["Pass 1 (about 60 minutes)", "Go through all 40 questions. Answer at once those you know (about 1 minute each). Do the short calculations. If a question needs more than 3 minutes, mark it and move on."],
            ["Pass 2 (about 20 minutes)", "Return to the marked questions: traces, subnetting, page-fault tables. Work them on paper."],
            ["Pass 3 (about 10 minutes)", "Make sure every question has an answer. Re-check calculations and any question with NOT, EXCEPT or ALWAYS in the stem."]]),
        T("Never leave a question blank: with four options a guess has a one in four chance, and an elimination of one or two options improves it."),
        H("Techniques for multiple-choice questions"),
        KEY("Read, eliminate, check", "Do these three things on every question.", cards=[
            ["Read the stem twice", "Underline words such as NOT, ONLY, FIRST, MAXIMUM. Many wrong answers are correct statements that answer a different question."],
            ["Eliminate", "Cross out options that are impossible: a mask that is not valid, a probability above 1, a value that has the wrong units or sign. Usually two options can go quickly."],
            ["Check", "Put your answer back into the question. A calculation can be repeated in a different order, or checked by estimating."]]),
        EX("Worked example 1: eliminating options", intro="Which of these is the subnet mask for a /27 prefix? A 255.255.255.128  B 255.255.255.192  C 255.255.255.224  D 255.255.255.240", steps=[
            S("Count bits", text="/27 means 27 ones: 24 in the first three octets and 3 in the last."),
            S("Eliminate", text="A has 1 bit in the last octet (/25) and B has 2 (/26). D has 4 (/28). Only C has 3 ones: 11100000 = 224."),
            S("Check", text="Block size = 256 - 224 = 32 = 2 to the power 5, and 5 host bits fit /27 (32 - 27 = 5). Answer C."),
        ]),
        EX("Worked example 2: a NOT question", intro="Which of the following is NOT a necessary condition for deadlock? A mutual exclusion  B hold and wait  C preemption of resources  D circular wait", steps=[
            S("Circle NOT", text="The stem asks for the option that is wrong, so three options are true statements."),
            S("Test each", text="Mutual exclusion, hold and wait and circular wait are three of the four conditions. The fourth is NO preemption."),
            S("Answer", text="C: if resources could be preempted, deadlock could be broken. Preemption is not a condition for deadlock."),
        ]),
        EX("Worked example 3: a calculation with a check", intro="A 5-stage pipeline processes 12 instructions with one cycle per stage and no hazards. How many cycles? A 60  B 17  C 16  D 12", steps=[
            S("Formula", math=r"\text{cycles} = k + (n - 1) = 5 + 11 = 16"),
            S("Check", text="The first instruction needs 5 cycles; each of the other 11 finishes one cycle later: 5 + 11 = 16."),
            S("Why not the others", text="60 is the unpipelined time (5 x 12). 17 adds n instead of n - 1. 12 forgets the time to fill the pipeline. Answer C."),
        ]),
        H("A revision map by topic"),
        KEY("What to revise for each part", "Use your results page to find your weakest topic first.", cards=[
            ["Computer Organization & Architecture", "Von Neumann and Harvard, buses and address width (2 to the power n); registers PC, MAR, MDR, CIR, ACC; the fetch-decode-execute cycle; pipeline cycles k + n - 1."],
            ["Digital Logic", "Half and full adder results, multiplexers and decoders; SR, D, JK and T flip-flop behaviour; De Morgan, absorption and Karnaugh map groups."],
            ["Operating Systems & Translators", "Gantt charts and averages for FCFS, SJF and Round Robin; semaphores; four deadlock conditions; page translation and FIFO or LRU fault counts; compiler stages and translator comparison."],
            ["Networks & Software Engineering", "OSI and TCP/IP layers, TCP and UDP; subnet masks and host counts; CRC; SDLC models; DFD, ERD and UML."],
            ["Procedural Programming", "Parameters and scope; recursion and the stack; file modes; pointers, dereferencing, dynamic memory errors."]]),
        H("Common mistakes in exams"),
        MISTAKE("Spending five minutes on one question", "A single question is worth the same as any other. Mark it, move on and return if time remains."),
        MISTAKE("Answering a question you half-read", "The wrong options are written from real mistakes. Reading only the first line makes them attractive."),
        MISTAKE("Trusting the first calculation", "Redo it a different way (for example by working backwards), especially for binary, subnet and CRC questions."),
        MISTAKE("Changing answers without a reason", "Change an answer only if you find a clear mistake. A hunch is usually less reliable than your first careful reasoning."),
        QUIZ("A multiple-choice paper has 40 questions and 90 minutes. You plan a first pass of 60 minutes. How many minutes remain for the second and third passes?",
             ["20", "30", "45", "60"], 1,
             "90 - 60 = 30 minutes, which can be split as 20 for the marked questions and 10 for final checks.",
             feedback=["20 minutes is only the second pass.", "", "45 would leave only 45 for the first pass.", "60 is the first pass itself."]),
        QUIZ("A question says: Which of the following is NOT a feature of TCP? You find that three options are true of TCP. What should you do?",
             ["Choose the first option anyway", "Choose the remaining option, because it is the one that is not a feature of TCP", "Skip the question for ever", "Choose the longest option"], 1,
             "In a NOT question the three true statements are the distractors; the false one is the answer.",
             feedback=["There is no reason to pick the first option.", "", "Never leave a question unanswered.", "Option length is not a reliable clue."]),
        H("Practice questions"),
        PQ("Explain three things that you will do in the practice paper to avoid losing marks on questions you find difficult. [3 marks]",
           "Mark the question and move on after about 3 minutes (1). Eliminate options that cannot be right and guess among the rest rather than leaving it blank (1). Return in the second pass with the working done on paper (1)."),
        PQ("A student has 20 minutes left and 6 marked questions. Suggest how to use the time. [2 marks]",
           "Spend about 2 to 3 minutes on each, attempting the quickest first (1). Leave the last few minutes to ensure every question has an answer (1)."),
        PQ("State why you should look at the results by topic after the practice paper, and what you will do next. [2 marks]",
           "The results by topic show which parts of the course are weakest (1). Next, go back to the lessons and practice sets for the lowest-scoring topics and repeat the questions you missed (1)."),
        SUM("The practice paper has 40 four-option questions and 90 minutes in KKEVO timed mode; these are not official figures.",
            "Check the real paper format with your teacher.",
            "Plan three passes: answer quickly (about 60 minutes), work marked questions (about 20), check (about 10).",
            "Read twice, eliminate, check; take care with NOT, ONLY and MAXIMUM.",
            "Never leave a question blank; change an answer only for a clear reason.",
            "Use the results by topic to choose what to revise next."),
    ],
))

