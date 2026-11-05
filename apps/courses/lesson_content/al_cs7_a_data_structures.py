"""Upper Sixth Computer Science (A Level): Data Structures & Algorithms, deepened (12 focused lessons).

REVIEW: scope is stacks, circular queues, singly and doubly linked lists, binary search trees (insertion,
search, three traversals, deletion), linear and binary search, bubble, insertion, selection, merge and quick
sort, and time and space complexity with Big-O. Every trace, comparison count and listing was run in Python.
Pseudocode style, pivot choice for quick sort (last item, Lomuto partition) and the way comparisons are
counted are KKEVO choices stated in each lesson; check them against the teacher's or Board's own convention.
"""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "upper-sixth")

MODULE = "Data Structures & Algorithms"
ADT = "Abstract data types"
SS = "Searching and sorting"
CX = "Complexity"

LESSONS = []

# ============================================================== 1. Stacks
LESSONS.append(lesson(
    module=MODULE, topic=ADT,
    title="The stack: push, pop and the top pointer",
    slug="csc-stack-push-pop",
    minutes=22,
    summary="Build a stack in an array with a top pointer, trace push and pop, detect overflow and underflow, and use a stack to evaluate postfix expressions and check brackets.",
    objectives=[
        "Describe a stack and its operations push, pop, peek, isEmpty and isFull",
        "Trace push and pop on an array-based stack using a top pointer",
        "Distinguish stack overflow from stack underflow",
        "Use a stack to evaluate a postfix expression and to check brackets",
    ],
    key_concepts=["Stack", "LIFO", "Push and pop", "Top pointer", "Overflow and underflow", "Postfix expression"],
    blocks=[
        H("Introduction"),
        T("At a canteen in Buea the cleaner puts clean plates on a pile. The next student takes the plate from the top, not from the bottom. The last plate placed is the first plate taken.\n\n"
          "A **stack** works in the same way. Your phone's *back* button, the *undo* key in a word processor and the way a program remembers where to return after a function call all use stacks."),
        D("A **stack** is an abstract data type in which items are added and removed at one end only, called the **top**. The last item added is the first item removed: **LIFO** (last in, first out).",
          title="Definition: stack"),
        KEY("The operations of a stack", "Every stack offers the same small set of operations, whatever it is built from.", cards=[
            ["push(item)", "Add an item at the top. Fails with overflow if the stack is full."],
            ["pop()", "Remove and return the top item. Fails with underflow if the stack is empty."],
            ["peek()", "Return the top item without removing it."],
            ["isEmpty() / isFull()", "Tests used before pop and push to avoid an error."],
        ]),
        T("A stack can be stored in an array of fixed size. A variable called **top** holds the index of the top item. An empty stack has top = -1, because index 0 is the first real position."),
        CODE('''
SIZE = 4
items = [None] * SIZE
top = -1

def push(x):
    global top
    if top == SIZE - 1:
        return "overflow"
    top = top + 1
    items[top] = x

def pop():
    global top
    if top == -1:
        return "underflow"
    x = items[top]
    top = top - 1
    return x
''', "python", title="Listing 1: an array stack of size 4"),
        IMG("al-csc-stack.svg", alt="A stack of four cells indexed 0 to 3 holding 15, 8, 40 and 6 with the top pointer at index 3", caption="Figure 1. A full stack of size 4. The top pointer is 3, so the next push fails."),
        EX("Worked example 1: tracing push and pop", intro="Start with an empty stack of size 4. Carry out: push 15, push 8, push 23, pop, push 40, push 6, push 9. Show the contents and top after each operation.", steps=[
            S("Three pushes", text="push 15 gives top = 0. push 8 gives top = 1. push 23 gives top = 2. The array holds 15, 8, 23."),
            S("Pop", text="pop returns 23 and top becomes 1. The value 23 may still sit in the array, but it is outside the stack because only positions 0 to top count."),
            S("Two more pushes", text="push 40 overwrites index 2 and top = 2. push 6 goes to index 3 and top = 3. The stack is now full: 15, 8, 40, 6."),
            S("The last push", text="push 9 finds top = SIZE - 1, so it returns overflow. Nothing changes."),
        ]),
        CODE('''
operation   returns     items               top
push 15                 15 . . .            0
push 8                  15 8 . .            1
push 23                 15 8 23 .           2
pop         23          15 8 (23) .         1
push 40                 15 8 40 .           2
push 6                  15 8 40 6           3
push 9      overflow    15 8 40 6           3
''', "text", title="Trace table for worked example 1"),
        D("**Overflow** happens when you push onto a full stack. **Underflow** happens when you pop from an empty stack. A good program tests isFull before push and isEmpty before pop.", title="Overflow and underflow"),
        H("Postfix evaluation with a stack"),
        T("Normal (infix) writing puts the operator between its numbers: 5 + 3. **Postfix** (reverse Polish) writing puts it after: 5 3 +. Postfix needs no brackets, so a computer evaluates it simply with a stack.\n\n"
          "Rule: read left to right. If the item is a number, push it. If it is an operator, pop twice, apply the operator and push the result. The first item popped is the *right-hand* operand."),
        EX("Worked example 2: evaluate 5 3 + 4 *", intro="The postfix expression 5 3 + 4 * means (5 + 3) * 4. Evaluate it with a stack.", steps=[
            S("Read 5 and 3", text="Push 5, then push 3. Stack from bottom to top: 5, 3."),
            S("Read +", text="Pop 3, pop 5, compute 5 + 3 = 8 and push 8. Stack: 8."),
            S("Read 4", text="Push 4. Stack: 8, 4."),
            S("Read *", text="Pop 4, pop 8, compute 8 * 4 = 32 and push 32. Stack: 32."),
            S("End of input", text="One value remains. The answer is 32."),
        ]),
        EX("Worked example 3: order matters for minus", intro="Evaluate 8 2 3 * -.", steps=[
            S("Push the numbers", text="Push 8, 2, 3. Stack: 8, 2, 3."),
            S("Read *", text="Pop 3, pop 2, compute 2 * 3 = 6, push 6. Stack: 8, 6."),
            S("Read -", text="Pop 6 first (right operand), then pop 8 (left operand). Compute 8 - 6 = 2. Push 2."),
            S("Answer", text="The result is 2. Computing 6 - 8 = -2 would be the mistake of swapping the operands."),
        ]),
        H("Where stacks are used"),
        KEY("Typical uses", "Anything that must be undone in reverse order uses a stack.", cards=[
            ["Undo and back", "Each action or page is pushed. Undo pops the latest one."],
            ["Function calls", "The return address and local variables of each call are pushed. The most recent call finishes first."],
            ["Bracket checking", "Push each opening bracket. When a closing bracket appears, pop and compare. The expression is valid only if every pop matches and the stack ends empty."],
        ]),
        EX("Worked example 4: bracket check", intro="Is the text (a + [b * c)] correctly bracketed?", steps=[
            S("Read ( then [", text="Push ( and push [. Stack: (, [."),
            S("Read )", text="Pop gives [. A ) needs a ( on top, so [ and ) do not match."),
            S("Conclusion", text="The text is not valid. A correct nesting such as (a + [b * c]) would pop [ for ] and ( for ) and finish with an empty stack."),
        ]),
        MISTAKE("Counting the pop as a deletion", "Pop only moves top down. The old value may remain in the array. Describe the stack by the items from index 0 to top, not by everything left in memory."),
        MISTAKE("Starting top at 0", "If an empty stack has top = 0, the first push would overwrite or skip index 0. With top = -1, push does top + 1 first, so the first item lands in index 0."),
        QUIZ("A stack of size 5 has top = 4. What happens when push is called?", [
            "The item is stored at index 5",
            "The item replaces the item at the top",
            "An overflow is reported and the stack is unchanged",
            "The oldest item is removed to make space",
        ], 2, "top = SIZE - 1 means the stack is full. A push on a full stack is an overflow.", hint="Compare top with SIZE - 1.",
             feedback=["Index 5 does not exist in an array of size 5.", "Push never overwrites an existing stack item.", "", "A stack only removes from the top, never the oldest item."]),
        QUIZ("Evaluate the postfix expression 6 2 / 5 +.", ["8", "5.33", "3", "13"], 0,
             "6 2 / is 6 / 2 = 3. Then 3 5 + is 8. The first popped item (2) is the divisor.", hint="Evaluate the first operator on the first two numbers.",
             feedback=["", "This swaps the operands in the division (2 / 6, then + 5). The first item popped is the divisor.", "This is only the value of 6 2 /; the + 5 still has to be applied.", "This adds all the numbers and ignores the division."]),
        TIP("In Paper 2 style questions you are often asked to show the stack after each operation. Draw the array, mark top, and cross out popped values lightly. Check your syllabus paper format with your teacher."),
        PQ("A stack of size 3 starts empty. Show the items and top after: push 7, push 2, pop, push 9, push 4, push 1.",
           "push 7: items 7, top 0. push 2: 7, 2, top 1. pop returns 2: items 7, top 0. push 9: 7, 9, top 1. push 4: 7, 9, 4, top 2 (full). push 1: overflow, so the stack stays 7, 9, 4 with top 2."),
        PQ("State two differences between a stack overflow and a stack underflow, and say which test prevents each.",
           "Overflow is pushing onto a full stack; underflow is popping from an empty stack. isFull (top = SIZE - 1) is checked before push; isEmpty (top = -1) is checked before pop."),
        PQ("Evaluate 4 6 2 / + using a stack. Show the stack after each token.",
           "Push 4: 4. Push 6: 4, 6. Push 2: 4, 6, 2. Read /: pop 2, pop 6, 6 / 2 = 3, push 3: 4, 3. Read +: pop 3, pop 4, 4 + 3 = 7, push 7. Answer: 7."),
        PQ("Give one reason why a stack suits the undo feature of an editor.",
           "Undo must reverse the most recent action first. A stack is LIFO: each action is pushed, and undo pops the last one pushed."),
        SUM("A stack is LIFO: items are added and removed at the top only.",
            "push adds, pop removes, peek reads; top = -1 means empty and top = SIZE - 1 means full in an array of that size.",
            "Overflow is a push on a full stack; underflow is a pop on an empty stack.",
            "Postfix expressions are evaluated by pushing numbers and popping two for each operator; the first pop is the right operand.",
            "Stacks support undo, function calls and bracket checking."),
    ],
))

# ============================================================== 2. Circular queue
LESSONS.append(lesson(
    module=MODULE, topic=ADT,
    title="Queues and the circular queue",
    slug="csc-queue-circular",
    minutes=22,
    summary="Describe the queue ADT, see why a simple array queue wastes space, and trace a circular queue with front and rear pointers and the mod operator.",
    objectives=[
        "Describe a queue and its operations enqueue and dequeue",
        "Explain why a linear array queue wastes space",
        "Trace a circular queue using front, rear and a count",
        "Use the mod operator to wrap a pointer round the array",
    ],
    key_concepts=["Queue", "FIFO", "Enqueue and dequeue", "Circular queue", "Front and rear pointers", "Mod operator"],
    blocks=[
        H("Introduction"),
        T("At a mobile money agent's kiosk in Garoua, people stand in a line. The person who arrived first is served first, and new customers join at the back. This fairness rule is **FIFO**: first in, first out.\n\n"
          "Computers use queues for print jobs, for messages waiting to be sent and for tasks waiting for the processor."),
        D("A **queue** is an abstract data type in which items are added at the **rear** and removed from the **front**. The first item added is the first item removed (FIFO).", title="Definition: queue"),
        KEY("Operations", "Compare with the stack: here the two ends have different jobs.", cards=[
            ["enqueue(item)", "Add at the rear. Fails (queue full) if there is no space."],
            ["dequeue()", "Remove and return the item at the front. Fails (queue empty) if there are no items."],
            ["isEmpty() / isFull()", "Tests used before dequeue and enqueue."],
        ]),
        H("The problem with a simple array queue"),
        T("Suppose a queue is stored in an array of size 4 with front and rear pointers that only ever move right. Enqueue A, B, C, D fills indexes 0 to 3. Dequeue twice removes A and B, so front is 2. Indexes 0 and 1 are free, but rear is already at index 3. The queue reports *full* although half of the array is empty. Space is wasted."),
        D("A **circular queue** treats the array as a ring. When a pointer moves past the last index it wraps round to index 0. The new index is found with the mod operator: (pointer + 1) mod SIZE.", title="Definition: circular queue"),
        IMG("al-csc-circular-queue.svg", alt="A ring of five slots holding F, G, C, D and E with front at index 2, rear at index 1 and a count of 5", caption="Figure 1. A circular queue of size 5 after enqueue G. The queue is full: count = 5."),
        T("We keep three variables. **front** is the index of the first item. **rear** is the index of the last item. **count** is the number of items. Using count makes the full and empty tests easy: empty means count = 0 and full means count = SIZE."),
        CODE('''
SIZE = 5
items = [None] * SIZE
front = 0
rear = -1
count = 0

def enqueue(x):
    global rear, count
    if count == SIZE:
        return "full"
    rear = (rear + 1) % SIZE
    items[rear] = x
    count = count + 1

def dequeue():
    global front, count
    if count == 0:
        return "empty"
    x = items[front]
    front = (front + 1) % SIZE
    count = count - 1
    return x
''', "python", title="Listing 1: circular queue of size 5"),
        EX("Worked example 1: tracing a circular queue", intro="Size 5, empty at the start. Carry out: enqueue A, B, C, D; dequeue; dequeue; enqueue E; enqueue F; enqueue G; enqueue H. Give front, rear and count after each operation.", steps=[
            S("Four enqueues", text="rear goes 0, 1, 2, 3. front stays 0. After D: front = 0, rear = 3, count = 4."),
            S("Two dequeues", text="dequeue returns A and front becomes 1. dequeue returns B and front becomes 2. count = 2. The queue holds C, D."),
            S("Enqueue E", text="rear becomes (3 + 1) mod 5 = 4. E goes in index 4. count = 3."),
            S("Enqueue F: the wrap", text="rear becomes (4 + 1) mod 5 = 0. F goes in index 0, which A used before. count = 4."),
            S("Enqueue G, then H", text="G goes in index 1 (rear = 1, count = 5), so the queue is full. H finds count = SIZE and returns full."),
        ]),
        CODE('''
operation    returns  array (index 0..4)   front rear count
enqueue A             A . . . .             0     0    1
enqueue B             A B . . .             0     1    2
enqueue C             A B C . .             0     2    3
enqueue D             A B C D .             0     3    4
dequeue      A        (A) B C D .           1     3    3
dequeue      B        (A)(B) C D .          2     3    2
enqueue E             (A)(B) C D E          2     4    3
enqueue F             F (B) C D E           2     0    4
enqueue G             F G C D E             2     1    5
enqueue H    full     F G C D E             2     1    5
''', "text", title="Trace table (brackets show dequeued values still in the array)"),
        EX("Worked example 2: finding rear from front and count", intro="A circular queue of size 6 has front = 4 and count = 3. Where is the rear, and where will the next item go?", steps=[
            S("The three items", text="They sit at indexes 4, 5 and then wrap to 0."),
            S("Rear", text="rear = (front + count - 1) mod SIZE = (4 + 3 - 1) mod 6 = 6 mod 6 = 0."),
            S("Next item", text="The next item goes to index (0 + 1) mod 6 = 1."),
        ]),
        TIP("When tracing, write the index next to every move. If a pointer reaches SIZE, replace it by 0. This is exactly what mod does."),
        MISTAKE("Using + 1 without mod", "rear = rear + 1 eventually gives an index outside the array. Always write (rear + 1) mod SIZE, and the same for front."),
        MISTAKE("Testing full with rear = SIZE - 1", "In a circular queue the rear can be at the last index while the front has moved on, so the queue is not full. Test count = SIZE (or compare front and rear using mod)."),
        QUIZ("A circular queue has SIZE = 8 and rear = 7. After one enqueue, what is rear?", ["8", "0", "7", "1"], 1,
             "(7 + 1) mod 8 = 0, so the pointer wraps to the start of the array.", hint="Apply (rear + 1) mod SIZE.",
             feedback=["Index 8 does not exist. The pointer must wrap.", "", "The pointer must move on by one place.", "This would happen after two enqueues, not one."]),
        QUIZ("Why is a circular queue better than a simple array queue?", [
            "It makes dequeue faster",
            "It reuses the space freed at the front of the array",
            "It can grow without limit",
            "It keeps the items sorted",
        ], 1, "Wrapping lets new items use the slots freed by dequeues, so space is not wasted.", hint="Think about what happens to the slots at the start after dequeue.",
             feedback=["Dequeue costs the same in both designs.", "", "A circular queue still has a fixed size.", "Queues keep arrival order, not sorted order."]),
        PQ("A circular queue of size 4 is empty. Show front, rear and count after: enqueue P, enqueue Q, enqueue R, dequeue, enqueue S, enqueue T, enqueue U.",
           "P: front 0, rear 0, count 1. Q: rear 1, count 2. R: rear 2, count 3. dequeue returns P: front 1, count 2. S: rear 3, count 3. T: rear (3 + 1) mod 4 = 0, count 4, queue full. U: full, no change. Final: front 1, rear 0, count 4."),
        PQ("A circular queue of size 10 has front = 8 and count = 4. State the indexes of the four items and the index where the next item will be stored.",
           "The items are at 8, 9, 0 and 1. rear = (8 + 4 - 1) mod 10 = 1. The next item goes to (1 + 1) mod 10 = 2."),
        PQ("Explain, with an example, why a linear array queue of size 4 can report full when only two items are in it.",
           "Enqueue A, B, C, D then dequeue A and B. Front is 2 and rear is 3 (the last index). The rear cannot move right, so the queue reports full although indexes 0 and 1 are empty."),
        SUM("A queue is FIFO: enqueue at the rear, dequeue from the front.",
            "A simple array queue wastes the space freed at the front.",
            "A circular queue wraps pointers with (pointer + 1) mod SIZE.",
            "A count variable makes the empty (count = 0) and full (count = SIZE) tests simple.",
            "In a trace, record front, rear and count after every operation."),
    ],
))

# ============================================================== 3. Linked lists
LESSONS.append(lesson(
    module=MODULE, topic=ADT,
    title="Singly and doubly linked lists",
    slug="csc-linked-lists",
    minutes=24,
    summary="Build singly and doubly linked lists from nodes and pointers, traverse them, and insert and delete nodes by changing pointers in the right order.",
    objectives=[
        "Describe a node, the start pointer and the null pointer",
        "Traverse a singly linked list and insert and delete a node",
        "Explain how a doubly linked list differs and update both pointers",
        "Compare a linked list with an array",
    ],
    key_concepts=["Node", "Pointer", "Singly linked list", "Doubly linked list", "Insertion and deletion", "Linked list versus array"],
    blocks=[
        H("Introduction"),
        T("A treasure hunt in a school compound in Bafoussam has clues on paper. Each clue says where the next clue is hidden. You must follow them in order from the first clue; you cannot jump to clue 7 without visiting the earlier ones.\n\n"
          "A **linked list** stores data like this. The items need not be next to each other in memory. Each item knows where the next one is."),
        D("A **linked list** is a collection of **nodes**. Each node holds a data value and a **pointer** to the next node. A **start** (head) pointer holds the first node. The last node holds **null** (no next node).", title="Definition: singly linked list"),
        IMG("al-csc-linked-list.svg", alt="A singly linked list 10, 25, 40, 60 ending in null above a doubly linked list 10, 25, 40 with next and previous arrows", caption="Figure 1. A singly linked list (top) and a doubly linked list (bottom)."),
        T("In an A Level exam the list is often stored in two parallel arrays: one for the data and one for the next pointer, with -1 as null. A third variable, the **free list pointer**, gives the next unused node."),
        CODE('''
index      0    1    2    3    4    5
data      10   25   40   60    -    -
next       1    2    3   -1    5   -1
start = 0        free = 4
''', "text", title="A list stored in arrays (free nodes are linked together too)"),
        T("Follow the pointers: start is 0, data[0] = 10, next[0] = 1, data[1] = 25, next[1] = 2, and so on until next = -1. The list is 10, 25, 40, 60."),
        CODE('''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(start):
    current = start
    while current is not None:
        print(current.data)
        current = current.next

def insert_after(node, value):
    new = Node(value)
    new.next = node.next      # step 1: new node points to the rest
    node.next = new           # step 2: previous node points to new
''', "python", title="Listing 1: node, traverse and insert after a node"),
        KEY("Order of the pointer changes", "Set the new node's pointer first, then change the existing pointer. If you do it the other way round, the rest of the list is lost.", cards=[
            ["Insert", "new.next = node.next, then node.next = new."],
            ["Delete", "Find the node before the one to remove, then predecessor.next = target.next."],
        ]),
        EX("Worked example 1: insert 30 into the list 10, 25, 40, 60 (kept in order)", intro="Use the array list above. Free node is index 4.", steps=[
            S("Store the data", text="data[4] = 30. The new node is index 4."),
            S("Find the position", text="30 goes after 25 (index 1), because 25 < 30 < 40."),
            S("Link the new node to the rest", text="next[4] = next[1] = 2, so 30 points to 40."),
            S("Link the previous node to the new one", text="next[1] = 4, so 25 points to 30."),
            S("Check by traversing", text="Start 0, then 1, then 4, then 2, then 3: 10, 25, 30, 40, 60."),
        ]),
        EX("Worked example 2: delete 25 from the list 10, 25, 30, 40, 60", intro="Index 0 holds 10 and index 1 holds 25.", steps=[
            S("Find the predecessor", text="25 is at index 1. Its predecessor holds 10 at index 0."),
            S("Bypass the node", text="next[0] = next[1] = 4, so 10 now points straight to 30."),
            S("Free the node", text="Add index 1 to the free list so it can be reused."),
            S("Check", text="Start 0, then 4, then 2, then 3: 10, 30, 40, 60."),
        ]),
        H("Doubly linked lists"),
        D("In a **doubly linked list** each node has two pointers: **next** and **previous**. The list can be traversed forwards from the start and backwards from the end.", title="Definition: doubly linked list"),
        EX("Worked example 3: insert a new node N after node A in a doubly linked list", intro="B is the node currently after A.", steps=[
            S("N.next = B", text="The new node points forward to B."),
            S("N.prev = A", text="The new node points back to A."),
            S("B.prev = N", text="B now points back to N (do this before changing A.next if you used A.next to find B)."),
            S("A.next = N", text="A points forward to N. Four pointer changes in all, compared with two in a singly linked list."),
        ]),
        KEY("Linked list or array?", "Neither is always better.", cards=[
            ["Linked list strengths", "Insert and delete need no shifting of other items once the position is known. Size can grow and shrink as needed."],
            ["Array strengths", "Direct access by index. Less memory per item, because there are no pointers."],
            ["Linked list weakness", "No direct access: to reach the nth node you follow n pointers from the start."],
        ]),
        MISTAKE("Changing node.next first", "If you write node.next = new before new.next = node.next, the address of the old next node is lost and the rest of the list cannot be reached."),
        MISTAKE("Forgetting the start pointer", "Deleting or inserting before the first node changes the start pointer itself. Deleting the first node means start = start.next."),
        QUIZ("In a singly linked list a node X holds next = null. What does this mean?", [
            "X is the first node",
            "X is the last node",
            "X has been deleted",
            "X holds the value zero",
        ], 1, "A null next pointer marks the end of the list, so X is the last node.", hint="What follows the last node?",
             feedback=["The first node is identified by the start pointer.", "", "A deleted node is removed by bypassing it, not by a null pointer.", "null is an empty pointer, not a data value."]),
        QUIZ("Which is a real advantage of a doubly linked list over a singly linked list?", [
            "It uses less memory",
            "It can be traversed backwards",
            "It gives direct access by index",
            "It needs fewer pointer changes to insert",
        ], 1, "The previous pointer lets you move backwards. The cost is an extra pointer per node and more updates.", hint="What does the previous pointer allow?",
             feedback=["It uses more memory, one extra pointer per node.", "", "Neither type gives direct access by index.", "Insertion needs more pointer changes, not fewer."]),
        PQ("A list stored in arrays has data = [8, 15, 22, 40], next = [1, 2, 3, -1] and start = 0. Write out the list and then show the changes to insert 19 (stored at free index 4) in the correct sorted place.",
           "The list is 8, 15, 22, 40. 19 goes after 15 (index 1). Set data[4] = 19, next[4] = next[1] = 2, then next[1] = 4. Traversal: 0, 1, 4, 2, 3 gives 8, 15, 19, 22, 40."),
        PQ("Describe how to delete the node holding 22 from the list 8, 15, 22, 40 (indexes 0, 1, 2, 3).",
           "Find the predecessor of 22, which is the node holding 15 at index 1. Set next[1] = next[2] = 3 so 15 points to 40. Return index 2 to the free list. The list is 8, 15, 40."),
        PQ("State two advantages and one disadvantage of a linked list compared with an array.",
           "Advantages: insertion and deletion do not shift other items; the list can grow or shrink easily. Disadvantage: items cannot be reached directly by index, so reaching the nth item means following n pointers."),
        PQ("Give the pointer assignments to insert node N between A and B in a doubly linked list.",
           "N.next = B; N.prev = A; B.prev = N; A.next = N."),
        SUM("A linked list is nodes joined by pointers; start gives the first node and null ends the list.",
            "To insert, point the new node at the rest of the list first, then point the earlier node at the new node.",
            "To delete, make the predecessor's next pointer skip the removed node.",
            "A doubly linked list adds a previous pointer so it can be traversed both ways, at the cost of more memory and more pointer updates.",
            "Linked lists suit frequent insertion and deletion; arrays suit direct access."),
    ],
))

# ============================================================== 4. BST insertion and search
LESSONS.append(lesson(
    module=MODULE, topic=ADT,
    title="Binary search trees: building and searching",
    slug="csc-bst-insert-search",
    minutes=24,
    summary="Define a binary search tree, build one by inserting keys in order, search it, and see why the order of insertion decides how tall and how fast the tree is.",
    objectives=[
        "Define a binary tree, root, leaf, subtree and height",
        "State the binary search tree rule and build a tree by insertion",
        "Search a binary search tree and count the comparisons",
        "Explain how insertion order changes the shape of the tree",
    ],
    key_concepts=["Binary tree", "Root, leaf and subtree", "Binary search tree", "Insertion", "Searching a BST", "Height of a tree"],
    blocks=[
        H("Introduction"),
        T("A university in Yaounde keeps 20,000 matriculation numbers. A list in arrival order must be searched one number at a time. A list kept sorted can be searched fast by binary search, but inserting a new number means shifting many others.\n\n"
          "A **binary search tree** (BST) keeps data ordered *and* lets you insert without shifting. Each decision at a node throws away half of what is left, if the tree is well shaped."),
        D("A **binary tree** is a tree in which each node has at most two children, called the **left child** and the **right child**. The top node is the **root**. A node with no children is a **leaf**. Every node is the root of a **subtree**. The **height** is the number of nodes on the longest path from the root down to a leaf.",
          title="Definition: binary tree"),
        D("A **binary search tree** is a binary tree in which, for every node, all keys in its left subtree are smaller than the node's key and all keys in its right subtree are larger. (This lesson does not allow duplicate keys.)",
          title="Definition: binary search tree"),
        T("The rule means every comparison tells you which way to go. At a node, a smaller target goes left, a larger target goes right, and an equal target is found."),
        CODE('''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    comparisons = 0
    while root is not None:
        comparisons = comparisons + 1
        if key == root.key:
            return True, comparisons
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return False, comparisons
''', "python", title="Listing 1: insert and search in a binary search tree"),
        EX("Worked example 1: build a BST", intro="Insert the keys 50, 30, 70, 20, 40, 60, 80, 35 in that order into an empty tree.", steps=[
            S("50", text="The tree is empty, so 50 becomes the root."),
            S("30 and 70", text="30 < 50 goes left. 70 > 50 goes right."),
            S("20 and 40", text="20 < 50, go left to 30, 20 < 30, so 20 is the left child of 30. 40 < 50, go left to 30, 40 > 30, so 40 is the right child of 30."),
            S("60 and 80", text="60 > 50, go right to 70, 60 < 70, so 60 is the left child of 70. 80 is the right child of 70."),
            S("35", text="35 < 50, left to 30; 35 > 30, right to 40; 35 < 40, so 35 is the left child of 40. The tree has height 4."),
        ]),
        IMG("al-csc-bst.svg", alt="A binary search tree with root 50, children 30 and 70, grandchildren 20, 40, 60 and 80, and 35 below 40", caption="Figure 1. The tree built in worked example 1."),
        EX("Worked example 2: search the tree", intro="Search the tree in Figure 1 for 35, then for 65.", steps=[
            S("Search for 35", text="Compare with 50: less, go left. Compare with 30: more, go right. Compare with 40: less, go left. Compare with 35: equal, found. 4 comparisons."),
            S("Search for 65", text="Compare with 50: more, go right. Compare with 70: less, go left. Compare with 60: more, go right. The right child of 60 is empty, so the search stops."),
            S("Result", text="65 is not in the tree after 3 comparisons. The empty place is exactly where 65 would be inserted."),
        ]),
        KEY("Insert is search plus one step", "To insert, search for the key. When the search reaches an empty place, put the new node there. A new key always becomes a leaf; existing nodes never move.", cards=[
            ["Search cost", "At most the height of the tree, because each step moves down one level."],
            ["Insert cost", "Also at most the height of the tree."],
        ]),
        H("Order of insertion decides the shape"),
        EX("Worked example 3: the same keys in a different order", intro="Insert 10, 20, 30, 40 in that order. Then compare with inserting 20, 10, 30, 40.", steps=[
            S("Sorted order", text="10 is the root. 20 > 10 goes right. 30 > 10 and > 20 goes right of 20. 40 goes right of 30. Every node has only a right child: a long chain of height 4."),
            S("Order 20, 10, 30, 40", text="20 is the root. 10 goes left. 30 goes right. 40 > 20 and > 30 goes right of 30. Height 3."),
            S("Why it matters", text="Searching for 40 takes 4 comparisons in the chain but 3 in the second tree. With thousands of keys the chain behaves like a linked list, while a balanced tree needs only about log base 2 of n comparisons."),
        ]),
        D("A tree is **balanced** if its left and right subtrees have almost the same height at every node. A balanced tree with n nodes has height about log2(n). A tree built from already sorted data is a chain with height n.", title="Balanced and degenerate trees"),
        MISTAKE("Comparing only with the parent", "Every key must be compared from the root downwards. 35 is smaller than 40 but also must be on the left of 50 and the right of 30. Following the path from the root keeps all these conditions true."),
        MISTAKE("Counting the missing node", "When a search fails, count only the nodes you compared with. The empty place is not a comparison."),
        QUIZ("Keys 45, 20, 60, 10, 30 are inserted into an empty BST in that order. Which node is the right child of 20?", ["10", "30", "45", "60"], 1,
             "20 is left of 45. 10 < 20 goes left of 20. 30 > 20 goes right of 20.", hint="Compare each key with 45 first, then with 20.",
             feedback=["10 is smaller than 20, so it is the left child.", "", "45 is the root, the parent of 20.", "60 is larger than 45, so it is in the right subtree of the root."]),
        QUIZ("Why is inserting keys that are already sorted a poor way to build a BST?", [
            "The tree cannot store sorted keys",
            "Every node becomes a leaf",
            "The tree becomes a chain, so searches take as long as in a list",
            "The root has to be deleted",
        ], 2, "Each new key is larger than all before it, so it always goes right, and the tree has height n.", hint="Where does each new larger key go?",
             feedback=["A BST can store any keys.", "Only the last node is a leaf in a chain.", "", "Insertion never deletes the root."]),
        TIP("In Paper 2 style questions, draw the tree after every insertion if the question asks for the order of nodes. A quick sketch avoids errors. Check the format with your teacher."),
        PQ("Draw (describe) the BST formed by inserting 14, 8, 20, 5, 11, 17, 25 in order and state its height.",
           "14 is the root. 8 is left of 14. 20 is right of 14. 5 is left of 8. 11 is right of 8. 17 is left of 20. 25 is right of 20. The tree is perfectly balanced: three levels, height 3."),
        PQ("In the tree of the previous question, list the keys compared when searching for 17 and for 12, and say how many comparisons each needs.",
           "17: 14, 20, 17 (3 comparisons, found). 12: 14, 8, 11 (3 comparisons; 12 is larger than 11 and 11 has no right child, so 12 is not in the tree)."),
        PQ("Insert 3, 1, 2, 5, 4 into an empty BST. State the root, the right child of 3 and the height.",
           "3 is the root. 1 is left of 3. 2 is right of 1. 5 is right of 3. 4 is left of 5. The right child of 3 is 5. Longest path: 3, 1, 2 or 3, 5, 4, so the height is 3."),
        PQ("Explain why the order in which keys are inserted affects how quickly the tree can be searched.",
           "Each key goes down from the root until a free place is found, so the order decides which keys are near the root. Sorted keys give a chain of height n and about n comparisons per search. Mixed keys give a short balanced tree with about log2 n comparisons."),
        SUM("A BST keeps smaller keys on the left and larger keys on the right of every node.",
            "Search and insert both start at the root and move down, comparing at each node.",
            "A new key always becomes a leaf; no existing node moves.",
            "Search and insert cost at most the height of the tree.",
            "Sorted input gives a chain of height n; random input gives a tree of height close to log2 n."),
    ],
))

# ============================================================== 5. BST traversal and deletion
LESSONS.append(lesson(
    module=MODULE, topic=ADT,
    title="Binary search trees: traversals and deletion",
    slug="csc-bst-traversal-deletion",
    minutes=25,
    summary="Produce the in-order, pre-order and post-order traversals of a binary search tree and delete a leaf, a node with one child and a node with two children.",
    objectives=[
        "Write the in-order, pre-order and post-order traversals of a tree",
        "Explain why the in-order traversal of a BST gives sorted keys",
        "Delete a leaf, a node with one child and a node with two children",
        "Use the in-order successor to delete a node with two children",
    ],
    key_concepts=["In-order traversal", "Pre-order traversal", "Post-order traversal", "Deleting a leaf", "Deleting with one child", "In-order successor"],
    blocks=[
        H("Introduction"),
        T("The registry of a school in Bamenda wants to print all matriculation numbers stored in a tree, in order, and also to remove the record of a student who has left. Printing visits every node once: this is a **traversal**. Removing a record must keep the BST rule true.\n\n"
          "We use the same tree as before, built by inserting 50, 30, 70, 20, 40, 60, 80, 35."),
        IMG("al-csc-bst.svg", alt="A binary search tree with root 50, children 30 and 70, grandchildren 20, 40, 60 and 80, and 35 below 40", caption="Figure 1. The tree used in this lesson."),
        D("A **traversal** visits every node of a tree exactly once. The three depth-first traversals differ in *when* the node itself is visited compared with its left and right subtrees.", title="Definition: tree traversal"),
        KEY("Three traversals", "Each is defined recursively on a node.", cards=[
            ["In-order", "Left subtree, then node, then right subtree."],
            ["Pre-order", "Node, then left subtree, then right subtree."],
            ["Post-order", "Left subtree, then right subtree, then node."],
        ]),
        CODE('''
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.key)
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(node.key)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.key)
''', "python", title="Listing 1: the three traversals"),
        EX("Worked example 1: the three traversals of the tree in Figure 1", intro="Give the in-order, pre-order and post-order output.", steps=[
            S("In-order", text="Go left as far as possible: 20, then its parent 30, then 30's right subtree (which gives 35, 40), then 50, then the right subtree 60, 70, 80. Output: 20, 30, 35, 40, 50, 60, 70, 80."),
            S("Pre-order", text="Visit the node first: 50, then the left subtree (30, 20, 40, 35), then the right subtree (70, 60, 80). Output: 50, 30, 20, 40, 35, 70, 60, 80."),
            S("Post-order", text="Visit the children first: 20, then 35, 40, then 30 (left subtree done), then 60, 80, 70, then the root. Output: 20, 35, 40, 30, 60, 80, 70, 50."),
        ]),
        KEY("What each traversal is used for", "The in-order result is the sorted list of keys, which follows from the BST rule: everything on the left is smaller and everything on the right is larger.", cards=[
            ["In-order", "Prints the keys in ascending order."],
            ["Pre-order", "Gives an order that rebuilds the same tree when the keys are inserted again."],
            ["Post-order", "Visits children before parents: used to delete a whole tree and to evaluate an expression tree (it gives postfix)."],
        ]),
        H("Deleting a node"),
        T("After a deletion the tree must still be a BST. There are three cases, depending on how many children the node has."),
        KEY("Three deletion cases", "Find the node with a search first.", cards=[
            ["No children (leaf)", "Remove it: set the parent's pointer to null."],
            ["One child", "Replace the node by its only child: the parent now points to that child."],
            ["Two children", "Replace the key by its in-order successor (the smallest key in the right subtree), then delete the successor from the right subtree. It has no left child, so this is an easy case."],
        ]),
        EX("Worked example 2: leaf and one child", intro="Starting from the tree in Figure 1, delete 20, and (in a separate copy) delete 40.", steps=[
            S("Delete 20", text="20 is a leaf, the left child of 30. Set 30's left pointer to null. Pre-order is now 50, 30, 40, 35, 70, 60, 80."),
            S("Delete 40", text="40 has one child, 35. Make 35 the right child of 30 in place of 40. Pre-order is now 50, 30, 20, 35, 70, 60, 80."),
            S("Check", text="In-order after deleting 40 is 20, 30, 35, 50, 60, 70, 80: still sorted, so the BST rule holds."),
        ]),
        EX("Worked example 3: two children", intro="Starting from the tree in Figure 1, delete the root 50.", steps=[
            S("Find the successor", text="Go to the right subtree (root 70) and then left as far as possible: 70, then 60. 60 has no left child, so 60 is the in-order successor."),
            S("Copy it", text="Replace the key 50 at the root by 60."),
            S("Delete the successor", text="Delete the old node 60 from the right subtree. It is a leaf, so 70's left pointer becomes null."),
            S("Check", text="Pre-order is now 60, 30, 20, 40, 35, 70, 80. In-order is 20, 30, 35, 40, 60, 70, 80: sorted."),
        ]),
        IMG("al-csc-bst-delete.svg", alt="Before and after deleting the root 50, which has two children: 60 replaces it and the old leaf 60 is removed", caption="Figure 2. Deleting a node with two children (simplified tree)."),
        TIP("The in-order predecessor (largest key in the left subtree) works equally well. State which one you use. The sorted order is the same either way."),
        MISTAKE("Using the left child as the replacement", "The left child may be smaller than other keys in the left subtree or may leave the right subtree out of order. Only the in-order successor or predecessor keeps the BST rule true."),
        MISTAKE("Mixing up pre-order and post-order", "Pre means the node comes before its subtrees. Post means after. In-order has the node in the middle."),
        QUIZ("A BST contains 8, 3, 10, 1, 6, 14 (inserted in that order). What is the in-order traversal?", [
            "8, 3, 1, 6, 10, 14",
            "1, 3, 6, 8, 10, 14",
            "1, 6, 3, 14, 10, 8",
            "8, 3, 10, 1, 6, 14",
        ], 1, "In-order on a BST always gives ascending order: 1, 3, 6, 8, 10, 14.", hint="What does the BST rule say about the order of an in-order walk?",
             feedback=["This is the pre-order traversal of the tree.", "", "This is the post-order traversal.", "This is the insertion order, not a traversal."]),
        QUIZ("Which node replaces the deleted node 50 when 50 has two children and the in-order successor is used?", [
            "The largest key in the left subtree",
            "The smallest key in the right subtree",
            "The right child of 50",
            "The parent of 50",
        ], 1, "The in-order successor is the smallest key larger than 50, which is the leftmost node of the right subtree.", hint="Successor means the next larger key.",
             feedback=["That is the in-order predecessor, a valid alternative but not the successor.", "", "The right child may have its own left subtree with smaller keys.", "50 is the root here and has no parent."]),
        PQ("Give the in-order, pre-order and post-order traversals of the BST formed from 40, 20, 60, 10, 30, 50, 70.",
           "The tree is balanced: root 40, children 20 and 60, leaves 10, 30, 50, 70. In-order: 10, 20, 30, 40, 50, 60, 70. Pre-order: 40, 20, 10, 30, 60, 50, 70. Post-order: 10, 30, 20, 50, 70, 60, 40."),
        PQ("In the tree of the previous question delete 20 (two children) using the in-order successor. Give the new pre-order traversal.",
           "The successor of 20 is 30 (leftmost of the right subtree, which is just 30). Replace 20 by 30 and delete the old leaf 30. The tree is root 40, left child 30 with left child 10, right child 60 with children 50 and 70. Pre-order: 40, 30, 10, 60, 50, 70."),
        PQ("Explain why the in-order traversal of a binary search tree produces its keys in ascending order.",
           "At every node the left subtree holds smaller keys and the right subtree holds larger keys. In-order visits the left subtree first, then the node, then the right subtree, so smaller keys always come out before the node and larger keys after it."),
        PQ("Describe the three cases when deleting a node from a BST.",
           "Leaf: remove it by setting the parent's pointer to null. One child: the parent points to that child instead. Two children: replace the node's key by the in-order successor (smallest in the right subtree) and delete the successor from the right subtree."),
        SUM("In-order is left, node, right; pre-order is node, left, right; post-order is left, right, node.",
            "The in-order traversal of a BST lists the keys in ascending order.",
            "Delete a leaf by removing it, a one-child node by promoting the child.",
            "Delete a two-child node by copying the in-order successor into it and deleting the successor.",
            "After any deletion the in-order traversal must still be sorted."),
    ],
))

# ============================================================== 6. Linear and binary search
LESSONS.append(lesson(
    module=MODULE, topic=SS,
    title="Linear search and binary search in depth",
    slug="csc-linear-binary-search",
    minutes=24,
    summary="Write and trace linear and binary search, count comparisons in the best and worst cases, and explain why binary search needs sorted data but needs only about log2 n comparisons.",
    objectives=[
        "Write and trace linear search and binary search",
        "Count comparisons in the best, worst and not-found cases",
        "Explain why binary search needs sorted data",
        "Compare the two searches for lists of different sizes",
    ],
    key_concepts=["Linear search", "Binary search", "Sorted data", "Comparisons", "Best and worst case", "Halving the search range"],
    blocks=[
        H("Introduction"),
        T("A cooperative in Bamenda keeps the weights of 15 coffee deliveries on a sheet. To find a delivery of 22 kg the secretary reads down the sheet from the top. If the sheet were sorted from lightest to heaviest, she could open it in the middle and know at once which half to read next.\n\n"
          "These are the two basic searches. In this lesson we count exactly how many items each one examines."),
        D("**Linear search** examines the items one after another from the start until the target is found or the end is reached. It works on any list.", title="Definition: linear search"),
        D("**Binary search** works only on a **sorted** list. It compares the target with the middle item. If it is equal, the search ends. If the target is smaller, the search continues in the lower half; if larger, in the upper half. The range is halved each time until the target is found or the range is empty.", title="Definition: binary search"),
        CODE('''
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def binary_search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
''', "python", title="Listing 1: the two searches (return -1 when not found)"),
        T("In this lesson we **count one comparison each time an item is examined** and tested for equality with the target. Some books count the less-than test too; always say what you count."),
        CODE('''
index  0  1  2   3   4   5   6   7   8   9  10  11  12   13   14
value  4  9 15  22  31  38  45  53  60  72  81  90  97  104  120
''', "text", title="The sorted list used in the examples (15 weights in kg)"),
        EX("Worked example 1: find 22", intro="Search the list above for 22 with both searches.", steps=[
            S("Linear search", text="Examine 4, 9, 15, then 22 at index 3: found after 4 comparisons."),
            S("Binary search, first step", text="low = 0, high = 14, mid = 7. items[7] = 53. 22 < 53, so high = 6. 1 comparison."),
            S("Binary search, second step", text="mid = (0 + 6) // 2 = 3. items[3] = 22: found. 2 comparisons in all."),
        ]),
        EX("Worked example 2: search for 100, which is not in the list", intro="Trace binary search and compare with linear search.", steps=[
            S("mid = 7", text="low = 0, high = 14. items[7] = 53 < 100, so low = 8. (1)"),
            S("mid = 11", text="low = 8, high = 14. items[11] = 90 < 100, so low = 12. (2)"),
            S("mid = 13", text="low = 12, high = 14. items[13] = 104 > 100, so high = 12. (3)"),
            S("mid = 12", text="low = 12, high = 12. items[12] = 97 < 100, so low = 13. (4)"),
            S("Stop", text="Now low = 13 is greater than high = 12, so the range is empty and the function returns -1 after 4 comparisons. Linear search would examine all 15 items."),
        ]),
        CODE('''
step  low  high  mid  items[mid]  decision
1      0    14    7      53       100 > 53, low = 8
2      8    14   11      90       100 > 90, low = 12
3     12    14   13     104       100 < 104, high = 12
4     12    12   12      97       100 > 97, low = 13
      13 > 12: range empty, not found
''', "text", title="Trace table for worked example 2"),
        KEY("Best, worst and not found", "The number of comparisons depends on where the target is.", cards=[
            ["Linear search", "Best: 1 (first item). Worst: n (last item or not present). On average about n / 2 if the target is present."],
            ["Binary search", "Best: 1 (the middle item). Worst: floor(log2 n) + 1, because the range can be halved only that many times."],
        ]),
        EX("Worked example 3: how many comparisons for large lists?", intro="Use the worst-case rule floor(log2 n) + 1 for binary search.", steps=[
            S("n = 15", text="log2 15 is about 3.9, so floor is 3 and the worst case is 4 comparisons. This matches the trace above."),
            S("n = 100", text="floor(log2 100) = 6, so at most 7 comparisons. Linear search may need 100."),
            S("n = 1000", text="floor(log2 1000) = 9, so at most 10 comparisons."),
            S("n = 1 000 000", text="floor(log2 1 000 000) = 19, so at most 20 comparisons. Linear search may need a million. Doubling the list adds only one more comparison for binary search."),
        ]),
        D("Binary search relies on the fact that the items are in order. If the list is not sorted, discarding half of it can throw away the target. The list must be sorted first (and sorting itself costs time).", title="The precondition"),
        TIP("Use linear search for short lists, unsorted data, or a single search. Use binary search for a large sorted list that is searched many times. The cost of sorting is paid once and every search afterwards is fast."),
        MISTAKE("Using binary search on unsorted data", "For 9, 3, 7, 1 searching for 1: mid = 3 gives items[1] = 3 > 1, so the search goes left to 9 and wrongly ends. The result is wrong, not just slow."),
        MISTAKE("Writing mid = (low + high) / 2", "Index must be a whole number. Use integer division: mid = (low + high) // 2 (DIV in many exam pseudo-codes)."),
        MISTAKE("Stopping when low = high", "When low equals high there is still one item to check. The loop must continue while low <= high."),
        QUIZ("A sorted list holds 200 items. What is the largest number of comparisons binary search needs?", ["8", "100", "200", "7"], 0,
             "floor(log2 200) + 1 = 7 + 1 = 8, because 2^7 = 128 is below 200 and 2^8 = 256 is above it.", hint="How many times can 200 be halved before the range is empty?",
             feedback=["", "100 is the average of linear search, not binary.", "200 is the worst case of linear search.", "7 is floor(log2 200); add one for the final item."]),
        QUIZ("Why can binary search not be used on the unsorted list 9, 3, 7, 1?", [
            "The list is too short",
            "Comparing with the middle item does not tell which half contains the target",
            "Binary search only works with numbers",
            "The list has an even number of items",
        ], 1, "Binary search discards a half using the ordering. Without sorted data that decision is meaningless.", hint="What does a smaller middle value tell you in a sorted list?",
             feedback=["Length is not the issue.", "", "Binary search works for any ordered type, such as names.", "Even or odd length only changes how mid is rounded."]),
        PQ("Trace binary search for 72 in the list 4, 9, 15, 22, 31, 38, 45, 53, 60, 72, 81, 90, 97, 104, 120 (indexes 0 to 14). State the mid values and the number of comparisons.",
           "low 0, high 14, mid 7 (53 < 72, low 8). low 8, high 14, mid 11 (90 > 72, high 10). low 8, high 10, mid 9 (72 = 72). Found at index 9 after 3 comparisons."),
        PQ("Search for 4 in the same list with binary search and give the number of comparisons.",
           "mid 7 (53 > 4, high 6), mid 3 (22 > 4, high 2), mid 1 (9 > 4, high 0), mid 0 (4, found). 4 comparisons."),
        PQ("A sorted list has 1000 items. State the maximum number of comparisons for binary search and for linear search, and explain the difference.",
           "Binary search: floor(log2 1000) + 1 = 10. Linear search: 1000. Binary search halves the range each step, so the work grows with log2 n instead of n."),
        PQ("State two conditions in which linear search is a better choice than binary search.",
           "The data is not sorted (and sorting would cost more than one search), or the list is very short, or it is searched only once."),
        SUM("Linear search checks items in turn; it works on unsorted data and needs up to n comparisons.",
            "Binary search needs sorted data and halves the range each step.",
            "Binary search needs at most floor(log2 n) + 1 comparisons.",
            "Continue the loop while low <= high; use integer division for mid.",
            "Always say what you count as a comparison when giving a number."),
    ],
))

# ============================================================== 7. Bubble sort
LESSONS.append(lesson(
    module=MODULE, topic=SS,
    title="Bubble sort: passes, swaps and the early exit",
    slug="csc-bubble-sort",
    minutes=22,
    summary="Trace bubble sort pass by pass with comparisons and swaps, add the swapped flag that stops early on sorted data, and see why the worst case is about n squared over 2 comparisons.",
    objectives=[
        "Trace bubble sort pass by pass",
        "Count comparisons and swaps",
        "Explain the swapped flag and the shrinking range",
        "State the best-case and worst-case behaviour",
    ],
    key_concepts=["Bubble sort", "Pass", "Swap", "Swapped flag", "Best and worst case", "In-place sort"],
    blocks=[
        H("Introduction"),
        T("A teacher in Limbe has six test marks on a board and must arrange them from lowest to highest by swapping two *neighbouring* marks at a time. She walks along the row, swaps any pair that is the wrong way round, and repeats until nothing needs swapping.\n\n"
          "That is **bubble sort**: large values drift (bubble) to the end of the list like air bubbles rising."),
        D("**Bubble sort** repeatedly passes through the list, comparing each pair of adjacent items and swapping them if they are in the wrong order. After pass 1 the largest item is in its final place at the end, after pass 2 the second largest, and so on.", title="Definition: bubble sort"),
        CODE('''
def bubble_sort(a):
    n = len(a)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
''', "python", title="Listing 1: bubble sort with early exit"),
        T("Two details save work. The inner loop gets shorter on each pass (n - 1 - p), because the last p items are already in place. The **swapped flag** stops the sort as soon as a whole pass makes no swap: then the list is sorted."),
        EX("Worked example 1: trace bubble sort on 7, 3, 9, 1, 5, 2", intro="Show the list after each pass, with the comparisons and swaps in the pass.", steps=[
            S("Pass 1 (5 comparisons)", text="7 and 3 swap; 7 and 9 stay; 9 and 1 swap; 9 and 5 swap; 9 and 2 swap. Result: 3, 7, 1, 5, 2, 9. 4 swaps. 9 is in place."),
            S("Pass 2 (4 comparisons)", text="3 and 7 stay; 7 and 1 swap; 7 and 5 swap; 7 and 2 swap. Result: 3, 1, 5, 2, 7, 9. 3 swaps."),
            S("Pass 3 (3 comparisons)", text="3 and 1 swap; 3 and 5 stay; 5 and 2 swap. Result: 1, 3, 2, 5, 7, 9. 2 swaps."),
            S("Pass 4 (2 comparisons)", text="1 and 3 stay; 3 and 2 swap. Result: 1, 2, 3, 5, 7, 9. 1 swap."),
            S("Pass 5 (1 comparison)", text="1 and 2 stay. No swap, so swapped is False and the sort stops."),
            S("Totals", text="5 + 4 + 3 + 2 + 1 = 15 comparisons and 4 + 3 + 2 + 1 = 10 swaps."),
        ]),
        CODE('''
start    7 3 9 1 5 2
pass 1   3 7 1 5 2 | 9      comparisons 5, swaps 4
pass 2   3 1 5 2 | 7 9      comparisons 4, swaps 3
pass 3   1 3 2 | 5 7 9      comparisons 3, swaps 2
pass 4   1 2 | 3 5 7 9      comparisons 2, swaps 1
pass 5   1 | 2 3 5 7 9      comparisons 1, swaps 0  -> stop
''', "text", title="Trace table (the bar marks the part already in final place)"),
        EX("Worked example 2: the early exit on sorted data", intro="Sort 2, 3, 5, 7 with the listing above.", steps=[
            S("Pass 1", text="Compare 2 and 3, 3 and 5, 5 and 7: 3 comparisons and no swaps. swapped stays False."),
            S("Stop", text="The loop breaks. Total: 3 comparisons, 0 swaps. The best case is n - 1 comparisons, about n."),
        ]),
        EX("Worked example 3: the worst case", intro="Sort 9, 7, 5, 3, 1.", steps=[
            S("Pass 1", text="4 comparisons, 4 swaps: 7, 5, 3, 1, 9."),
            S("Pass 2", text="3 comparisons, 3 swaps: 5, 3, 1, 7, 9."),
            S("Pass 3", text="2 comparisons, 2 swaps: 3, 1, 5, 7, 9."),
            S("Pass 4", text="1 comparison, 1 swap: 1, 3, 5, 7, 9. Total: 10 comparisons and 10 swaps."),
            S("General rule", text="For a reversed list of n items: (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 comparisons. For n = 5 this is 10. The work grows like n squared."),
        ]),
        KEY("Bubble sort facts", "Useful for exam answers.", cards=[
            ["Best case", "Already sorted data with the early exit: n - 1 comparisons, no swaps."],
            ["Worst case", "Reversed data: n(n - 1) / 2 comparisons and as many swaps."],
            ["Space", "In place: only a temporary variable for swapping."],
        ]),
        MISTAKE("Forgetting that a pass can end the sort early", "If a pass makes no swap, the list is sorted. Without the flag, bubble sort carries on with useless passes."),
        MISTAKE("Comparing every pair on every pass", "The last p items are already in place after p passes. Counting full-length passes gives too many comparisons."),
        MISTAKE("Swapping three items at once", "Bubble sort only ever swaps two adjacent items. A trace table should show one swap at a time."),
        QUIZ("After the first pass of bubble sort on 4, 8, 2, 6, which list results?", ["4, 2, 6, 8", "2, 4, 6, 8", "4, 8, 2, 6", "2, 8, 4, 6"], 0,
             "4 and 8 stay; 8 and 2 swap; 8 and 6 swap. The largest item, 8, is now last: 4, 2, 6, 8.", hint="Move 8 to the end by comparing neighbours only.",
             feedback=["", "This is the finished list; one pass does not fully sort it.", "This is the unchanged list. Several adjacent pairs are out of order.", "This is what selection sort does on its first pass, not bubble sort."]),
        QUIZ("What is the purpose of the swapped flag?", [
            "To count the swaps",
            "To stop the sort when a pass makes no swap",
            "To make the sort stable",
            "To reverse the list",
        ], 1, "A pass with no swap proves every neighbouring pair is in order, so the list is sorted and the sort can stop.", hint="What does a pass with no swaps tell you?",
             feedback=["The flag only records whether any swap happened; it is not a counter.", "", "Stability is decided by whether equal items are moved past each other.", "The flag has nothing to do with order direction."]),
        PQ("Show the list after each pass of bubble sort on 5, 1, 4, 2 and give the total comparisons and swaps (with shrinking passes and early exit).",
           "Pass 1: 1, 4, 2, 5 (3 comparisons, 3 swaps). Pass 2: 1, 2, 4, 5 (2 comparisons, 1 swap). Pass 3: 1, 2, 4, 5 (1 comparison, 0 swaps, stop). Totals: 6 comparisons, 4 swaps."),
        PQ("How many comparisons does bubble sort (with early exit) make on an already sorted list of 8 items? Explain.",
           "7. The first pass compares each of the 7 neighbouring pairs and finds no swap, so the sort stops after one pass."),
        PQ("State the number of comparisons needed to sort a reversed list of 6 items with bubble sort and give the general formula.",
           "5 + 4 + 3 + 2 + 1 = 15, which is n(n - 1) / 2 with n = 6."),
        PQ("Explain why, after pass 2, the two largest items are in their final positions.",
           "Pass 1 carries the largest item to the end. Pass 2 starts again and carries the largest of the remaining items to the position before it. Neither moves again."),
        SUM("Bubble sort compares and swaps adjacent items; each pass puts the next largest item in place.",
            "The inner loop shortens each pass because the end of the list is already sorted.",
            "The swapped flag stops the sort when a pass makes no swaps.",
            "Best case about n comparisons (sorted data); worst case n(n - 1) / 2 comparisons (reversed data).",
            "It sorts in place using only a temporary variable."),
    ],
))

# ============================================================== 8. Insertion and selection sort
LESSONS.append(lesson(
    module=MODULE, topic=SS,
    title="Insertion sort and selection sort",
    slug="csc-insertion-selection-sort",
    minutes=24,
    summary="Trace insertion sort and selection sort on the same list, count comparisons and moves, and compare their behaviour on sorted, reversed and random data.",
    objectives=[
        "Trace insertion sort and selection sort step by step",
        "Count comparisons and swaps or shifts for each",
        "Explain which one adapts to nearly sorted data",
        "Define a stable sort and say which of these two is stable",
    ],
    key_concepts=["Insertion sort", "Selection sort", "Sorted part and unsorted part", "Comparisons and shifts", "Stable sort"],
    blocks=[
        H("Introduction"),
        T("A card player in Douala sorts a hand of cards in two natural ways. She may take each new card and slide it into the right place among the cards she already holds (**insertion**). Or she may look through the cards, pick out the lowest and put it first, then the next lowest, and so on (**selection**).\n\n"
          "Both keep the list in two parts: a sorted part and an unsorted part. They differ in how they grow the sorted part."),
        KEY("Two ways to grow the sorted part", "Both sort in place.", cards=[
            ["Insertion sort", "Take the first unsorted item and insert it into its correct place in the sorted part on the left, shifting larger items one place to the right."],
            ["Selection sort", "Find the smallest item in the unsorted part and swap it with the first unsorted item."],
        ]),
        CODE('''
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
''', "python", title="Listing 1: insertion sort and selection sort"),
        EX("Worked example 1: insertion sort on 7, 3, 9, 1, 5, 2", intro="Show the list after each insertion. The bar marks the sorted part.", steps=[
            S("Insert 3", text="3 < 7, so 7 shifts right and 3 goes first: 3, 7 | 9, 1, 5, 2. (1 comparison with a larger item, 1 shift.)"),
            S("Insert 9", text="9 > 7, so it stays: 3, 7, 9 | 1, 5, 2. (1 comparison, 0 shifts.)"),
            S("Insert 1", text="1 is smaller than 9, 7 and 3, so all three shift: 1, 3, 7, 9 | 5, 2. (3 comparisons, 3 shifts.)"),
            S("Insert 5", text="5 < 9 and 5 < 7 shift; 5 > 3 stops: 1, 3, 5, 7, 9 | 2. (3 comparisons, 2 shifts.)"),
            S("Insert 2", text="2 shifts past 9, 7, 5 and 3, stops at 1: 1, 2, 3, 5, 7, 9. (5 comparisons, 4 shifts.)"),
            S("Totals", text="Comparisons: 1 + 1 + 3 + 3 + 5 = 13. Shifts: 1 + 0 + 3 + 2 + 4 = 10. Here a comparison is counted each time the key is compared with an item on its left."),
        ]),
        T("*Note on counting:* when 2 is inserted it is compared with 9, 7, 5 and 3 (four shifts) and then with 1, which is smaller, so the loop stops: 5 comparisons. When 1 is inserted it moves to the left end, so j reaches -1 and there is no final comparison. Exam answers should state what is counted."),
        EX("Worked example 2: selection sort on 7, 3, 9, 1, 5, 2", intro="Show the list after each pass.", steps=[
            S("Pass 1", text="The smallest of all six is 1 (index 3). Swap with index 0: 1, 3, 9, 7, 5, 2."),
            S("Pass 2", text="The smallest of 3, 9, 7, 5, 2 is 2 (index 5). Swap with index 1: 1, 2, 9, 7, 5, 3."),
            S("Pass 3", text="The smallest of 9, 7, 5, 3 is 3 (index 5). Swap with index 2: 1, 2, 3, 7, 5, 9."),
            S("Pass 4", text="The smallest of 7, 5, 9 is 5 (index 4). Swap with index 3: 1, 2, 3, 5, 7, 9."),
            S("Pass 5", text="The smallest of 7, 9 is 7, already in place: no swap. Sorted."),
            S("Totals", text="Comparisons: 5 + 4 + 3 + 2 + 1 = 15. Swaps: 4. Selection sort makes the same number of comparisons whatever the data."),
        ]),
        CODE('''
Insertion sort                          Selection sort
start     7 3 9 1 5 2                   start   7 3 9 1 5 2
insert 3  3 7 | 9 1 5 2                 pass 1  1 | 3 9 7 5 2
insert 9  3 7 9 | 1 5 2                 pass 2  1 2 | 9 7 5 3
insert 1  1 3 7 9 | 5 2                 pass 3  1 2 3 | 7 5 9
insert 5  1 3 5 7 9 | 2                 pass 4  1 2 3 5 | 7 9
insert 2  1 2 3 5 7 9                   pass 5  1 2 3 5 7 | 9
''', "text", title="The two sorts side by side on the same list"),
        EX("Worked example 3: sorted and reversed data", intro="Compare the sorts on 1, 2, 3, 4, 5 and on 5, 4, 3, 2, 1.", steps=[
            S("Insertion sort, sorted data", text="Each new item is larger than the one before it: 1 comparison per item, no shifts. Total: 4 comparisons. Insertion sort is quick on sorted or nearly sorted data."),
            S("Insertion sort, reversed data", text="Each new item moves to the front: 1 + 2 + 3 + 4 = 10 comparisons and 10 shifts."),
            S("Selection sort, either order", text="5 items always give 4 + 3 + 2 + 1 = 10 comparisons. It does not notice that the data is already sorted."),
        ]),
        D("A sort is **stable** if items with equal keys stay in their original order. Insertion sort (as written, shifting only items strictly greater) is stable. Selection sort with a long-distance swap is not stable: sorting 2a, 2b, 1 swaps 2a with 1 and gives 1, 2b, 2a.", title="Definition: stable sort"),
        KEY("Comparison of the three simple sorts", "All three are in place and take about n squared steps on average.", cards=[
            ["Bubble", "Best about n (with early exit), worst n(n - 1) / 2. Many swaps."],
            ["Insertion", "Best about n (sorted data), worst about n(n - 1) / 2. Good for small or nearly sorted lists."],
            ["Selection", "Always n(n - 1) / 2 comparisons but at most n - 1 swaps: useful when a swap is expensive."],
        ]),
        MISTAKE("Mixing up the two sorts", "Insertion sort *shifts* many items to open a gap. Selection sort *swaps* once per pass. A trace that shows several items moving in one step is insertion sort."),
        MISTAKE("Swapping instead of shifting in insertion sort", "Insertion sort places the key once at the end of the loop. Swapping at every step gives the right answer but changes the operation count."),
        QUIZ("Which sort makes exactly the same number of comparisons for 1, 2, 3, 4, 5 as for 5, 4, 3, 2, 1?", ["Insertion sort", "Selection sort", "Bubble sort with early exit", "Binary search"], 1,
             "Selection sort always scans the whole unsorted part: 10 comparisons for five items in both orders.", hint="Which sort never notices that the data is sorted?",
             feedback=["Insertion sort needs 4 comparisons on sorted data and 10 on reversed data.", "", "Bubble sort with early exit needs 4 comparisons on sorted data and 10 on reversed data.", "Binary search is a search, not a sort."]),
        QUIZ("Which statement about insertion sort is correct?", [
            "It always makes n(n - 1) / 2 comparisons",
            "It selects the smallest item in each pass",
            "It is fast when the data is already almost sorted",
            "It needs a second array as large as the first",
        ], 2, "With nearly sorted data each new item is only a little out of place, so there are few shifts.", hint="How far must each item move in nearly sorted data?",
             feedback=["That is selection sort. Insertion sort needs far fewer on sorted data.", "That describes selection sort.", "", "Insertion sort works in place."]),
        PQ("Sort 6, 2, 8, 4 by selection sort. Give the list after each pass and the number of swaps.",
           "Pass 1: smallest is 2, swap with 6: 2, 6, 8, 4. Pass 2: smallest of 6, 8, 4 is 4, swap with 6: 2, 4, 8, 6. Pass 3: smallest of 8, 6 is 6, swap with 8: 2, 4, 6, 8. Swaps: 3."),
        PQ("Sort 6, 2, 8, 4 by insertion sort. Give the list after each insertion.",
           "Insert 2: 2, 6, 8, 4. Insert 8: 2, 6, 8, 4 (no change). Insert 4: 4 shifts 8 and 6 and stops after 2: 2, 4, 6, 8."),
        PQ("Why does selection sort make the same number of comparisons whatever the data, while insertion sort does not?",
           "Selection sort scans the whole unsorted part to find the smallest item, so the scan length never depends on the order. Insertion sort stops comparing as soon as the item reaches its place, so ordered data stops early."),
        PQ("Define a stable sort and say whether selection sort (swapping the minimum into place) is stable, with an example.",
           "A stable sort keeps equal items in their original order. Selection sort is not stable: for 2a, 2b, 1 the first swap exchanges 2a and 1 and gives 1, 2b, 2a, so the equal items change order."),
        SUM("Insertion sort inserts each new item into the sorted part by shifting larger items right.",
            "Selection sort swaps the smallest unsorted item to the front of the unsorted part, once per pass.",
            "Selection sort always makes n(n - 1) / 2 comparisons; insertion sort can finish in about n comparisons on sorted data.",
            "Insertion sort is stable; selection sort by long-distance swap is not.",
            "All three simple sorts take about n squared steps in the worst case."),
    ],
))

# ============================================================== 9. Merge sort
LESSONS.append(lesson(
    module=MODULE, topic=SS,
    title="Merge sort: divide, sort and merge",
    slug="csc-merge-sort",
    minutes=24,
    summary="Trace merge sort by splitting a list into halves and merging sorted halves, count the comparisons in each merge, and explain why it takes about n log n steps but needs extra memory.",
    objectives=[
        "Explain divide and conquer as used by merge sort",
        "Merge two sorted lists and count the comparisons",
        "Trace a complete merge sort on eight items",
        "State the time complexity, space cost and stability of merge sort",
    ],
    key_concepts=["Divide and conquer", "Merge", "Recursion", "n log n", "Extra memory", "Stable sort"],
    blocks=[
        H("Introduction"),
        T("Two examiners in Bertoua each mark half of the scripts and sort their own pile by candidate number. To produce one sorted list they sit together and take the lower top script from either pile again and again. This is far quicker than sorting the whole heap by one person with simple sorts.\n\n"
          "**Merge sort** does exactly this. It splits a list in two, sorts each half the same way, and merges the two sorted halves."),
        D("**Merge sort** is a *divide and conquer* algorithm. It (1) divides the list into two halves, (2) sorts each half by calling itself, and (3) merges the two sorted halves into one sorted list. A list of 0 or 1 item is already sorted: this is the base case.", title="Definition: merge sort"),
        T("The key step is **merging**. Two sorted lists are merged by comparing their front items, moving the smaller one to the result, and repeating. When one list is empty, the rest of the other list is copied over."),
        CODE('''
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result = result + left[i:] + right[j:]
    return result

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)
''', "python", title="Listing 1: merge and merge sort"),
        EX("Worked example 1: merge 3, 27, 38, 43 with 9, 10, 15, 82", intro="Show each comparison and the result so far.", steps=[
            S("3 against 9", text="3 is smaller: result 3."),
            S("27 against 9", text="9 is smaller: result 3, 9."),
            S("27 against 10", text="10 is smaller: result 3, 9, 10."),
            S("27 against 15", text="15 is smaller: result 3, 9, 10, 15."),
            S("27 against 82", text="27 is smaller: result 3, 9, 10, 15, 27."),
            S("38 against 82, then 43 against 82", text="38 and then 43 are smaller: result 3, 9, 10, 15, 27, 38, 43."),
            S("Copy the rest", text="The left list is empty, so copy 82. The result is 3, 9, 10, 15, 27, 38, 43, 82 after 7 comparisons."),
        ]),
        EX("Worked example 2: a complete merge sort", intro="Sort 38, 27, 43, 3, 9, 82, 10, 15.", steps=[
            S("Divide", text="Split into 38, 27, 43, 3 and 9, 82, 10, 15. Split again into pairs: 38, 27 | 43, 3 | 9, 82 | 10, 15. Split again into single items."),
            S("Merge the single items into pairs", text="27, 38 | 3, 43 | 9, 82 | 10, 15. Each merge needs 1 comparison: 4 comparisons."),
            S("Merge the pairs into fours", text="27, 38 with 3, 43 gives 3, 27, 38, 43 (3 comparisons). 9, 82 with 10, 15 gives 9, 10, 15, 82 (3 comparisons). Total 6."),
            S("Final merge", text="The two lists of four merge into 3, 9, 10, 15, 27, 38, 43, 82 using 7 comparisons (worked example 1)."),
            S("Total", text="4 + 6 + 7 = 17 comparisons for 8 items."),
        ]),
        IMG("al-csc-merge-sort.svg", alt="Eight numbers split down to single items then merged back up through pairs and fours into one sorted list", caption="Figure 1. Merge sort on eight items: three levels of splitting and three levels of merging."),
        KEY("Why n log n?", "Count the levels and the work per level.", cards=[
            ["Levels", "Halving 8 items gives 3 levels of merging, because 2 x 2 x 2 = 8. For n items there are about log2 n levels."],
            ["Work per level", "Each level merges items once in total, so it handles about n items and needs at most n comparisons."],
            ["Total", "About n x log2 n comparisons: 8 x 3 = 24 at most. The trace needed 17."],
        ]),
        D("Merge sort takes about n log n steps in the **best, average and worst** cases. It is **stable** when merge takes the left item on ties (the listing uses <=). It needs **extra memory** of about n items for the merged lists, so it is not an in-place sort.", title="Properties of merge sort"),
        TIP("The usual weakness to mention is the extra memory. The usual strength is that its speed does not depend on the data: sorted, reversed or random lists all take about n log n steps."),
        MISTAKE("Merging by joining the lists", "Joining two sorted lists end to end does not give a sorted list. You must compare the front items repeatedly."),
        MISTAKE("Forgetting to copy the leftover items", "When one list runs out, the remaining items of the other list are already in order and are added to the end."),
        MISTAKE("Counting the splits as comparisons", "Only the comparisons inside the merge step count. Dividing the list needs no comparisons."),
        QUIZ("Merge the sorted lists 2, 9, 14 and 5, 6, 20. How many comparisons does the merge make?", ["3", "5", "6", "9"], 1,
             "2 v 5, 9 v 5, 9 v 6, 9 v 20, 14 v 20 make 5 comparisons; then 20 is copied. Result: 2, 5, 6, 9, 14, 20.", hint="Count each comparison of two front items until one list is empty.",
             feedback=["This stops before the lists are used up.", "", "The last item (20) is copied without a comparison, so the count is one less.", "There are only 6 items and each comparison places one of them, with the last one copied, so 9 is impossible."]),
        QUIZ("Which statement about merge sort is true?", [
            "It sorts in place without extra memory",
            "It is slower on already sorted data",
            "It takes about n log n steps in every case but uses extra memory",
            "It needs the list to be sorted first",
        ], 2, "Every level merges all n items and there are about log2 n levels, whatever the order of the data. The merged lists need about n extra places.", hint="Think about the number of levels and the work per level.",
             feedback=["Merging builds new lists, so extra memory is needed.", "Its time does not depend on the order of the data.", "", "It is the algorithm that sorts the list."]),
        PQ("Trace merge sort on 6, 2, 8, 4, giving the lists at each stage and the total number of comparisons.",
           "Split: 6, 2 | 8, 4, then 6 | 2 | 8 | 4. Merge: 2, 6 (1 comparison) and 4, 8 (1 comparison). Final merge of 2, 6 with 4, 8: 2 v 4, 6 v 4, 6 v 8, then 8 is copied: 3 comparisons. Result 2, 4, 6, 8. Total 5 comparisons."),
        PQ("Explain why merge sort takes about n log2 n steps. Use n = 16.",
           "16 items are halved 4 times (16, 8, 4, 2, 1), so there are 4 levels of merging. Each level handles all 16 items with at most 16 comparisons, so at most 16 x 4 = 64 steps."),
        PQ("State one advantage and one disadvantage of merge sort compared with insertion sort.",
           "Advantage: about n log n steps even in the worst case, much faster than insertion sort's n squared for large lists. Disadvantage: it needs extra memory of about n items, whereas insertion sort works in place (and is faster on nearly sorted small lists)."),
        PQ("Merge sort is called a divide and conquer algorithm. Describe the three stages.",
           "Divide: split the list into two halves. Conquer: sort each half by applying the same method (recursion) until a list has 0 or 1 item. Combine: merge the two sorted halves into one sorted list."),
        SUM("Merge sort divides the list, sorts the halves recursively and merges them.",
            "Merging two sorted lists compares the two front items and takes the smaller; leftovers are copied.",
            "There are about log2 n levels and each level handles n items: about n log n steps in every case.",
            "It is stable but needs extra memory of about n items.",
            "Only comparisons in the merge step are counted."),
    ],
))

# ============================================================== 10. Quick sort
LESSONS.append(lesson(
    module=MODULE, topic=SS,
    title="Quick sort: pivot and partition",
    slug="csc-quick-sort",
    minutes=25,
    summary="Trace quick sort with a last-item pivot: partition the list so smaller items are left of the pivot and larger items right, then sort each side, and see why a bad pivot gives the n squared worst case.",
    objectives=[
        "Explain the role of the pivot and of partitioning",
        "Trace a partition step by step",
        "Trace a complete quick sort and count comparisons",
        "Explain the best, average and worst cases",
    ],
    key_concepts=["Pivot", "Partition", "Divide and conquer", "Recursion", "Worst case", "In-place sort"],
    blocks=[
        H("Introduction"),
        T("A teacher in Ngaoundere has a pile of exam scripts. She picks one script and divides the pile: scripts with lower marks on the left, higher marks on the right. That one script is now in its final place. She then does the same for each smaller pile.\n\n"
          "This is **quick sort**. The chosen script is the **pivot**."),
        D("**Quick sort** is a divide and conquer algorithm. It chooses a **pivot**, **partitions** the list so that items not greater than the pivot are on its left and larger items on its right, which puts the pivot in its final position, and then sorts the left part and the right part in the same way.", title="Definition: quick sort"),
        T("There are several ways to choose a pivot and to partition. **In this lesson the pivot is the last item of the part and we use this partition method** (often called the Lomuto scheme). Other methods give different intermediate lists but the same final sorted list, so always follow the method your teacher or paper uses."),
        CODE('''
def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quick_sort(a, low, p - 1)
        quick_sort(a, p + 1, high)
''', "python", title="Listing 1: quick sort with the last item as pivot"),
        T("In **partition**, the variable i marks the end of the group of items not greater than the pivot. Each item at j that is not greater than the pivot is swapped into that group. At the end the pivot is swapped into the place just after the group."),
        EX("Worked example 1: one partition", intro="Partition 4, 9, 2, 7, 5 (indexes 0 to 4). The pivot is the last item, 5.", steps=[
            S("Set up", text="pivot = 5, i = -1."),
            S("j = 0: item 4", text="4 <= 5, so i = 0 and swap a[0] with itself: 4, 9, 2, 7, 5."),
            S("j = 1: item 9", text="9 > 5: nothing happens."),
            S("j = 2: item 2", text="2 <= 5, so i = 1 and swap a[1] with a[2]: 4, 2, 9, 7, 5."),
            S("j = 3: item 7", text="7 > 5: nothing happens."),
            S("Place the pivot", text="Swap a[i + 1] = a[2] with the pivot: 4, 2, 5, 7, 9. The pivot 5 is at index 2 in its final place; 4 and 2 are on its left, 7 and 9 on its right. 4 comparisons were made."),
        ]),
        EX("Worked example 2: a complete quick sort of 7, 3, 9, 1, 5, 2", intro="Always take the last item of each part as the pivot.", steps=[
            S("Partition 1: pivot 2", text="Only 1 is not greater than 2, so the group is 1; place the pivot: 1, 2, 9, 7, 5, 3. Pivot 2 is final at index 1. (5 comparisons.)"),
            S("Left part", text="The left part is the single item 1: nothing to do."),
            S("Partition 2: 9, 7, 5, 3 with pivot 3", text="No item is not greater than 3, so the pivot goes to the front of this part: 3, 7, 5, 9. The list is 1, 2, 3, 7, 5, 9. Pivot 3 is final at index 2. (3 comparisons.)"),
            S("Partition 3: 7, 5, 9 with pivot 9", text="Both 7 and 5 are not greater than 9, so the pivot stays last: 7, 5, 9. Pivot 9 is final at index 5. (2 comparisons.)"),
            S("Partition 4: 7, 5 with pivot 5", text="7 > 5, so the pivot swaps with 7: 5, 7. The list is 1, 2, 3, 5, 7, 9. (1 comparison.)"),
            S("Total", text="5 + 3 + 2 + 1 = 11 comparisons. Compare: bubble sort needed 15, insertion sort 13 and merge sort 9 on this same list."),
        ]),
        CODE('''
start (indexes 0 to 5)         7 3 9 1 5 2
partition (0-5), pivot 2   ->  1 2 9 7 5 3     pivot at index 1, 5 comparisons
partition (2-5), pivot 3   ->  1 2 3 7 5 9     pivot at index 2, 3 comparisons
partition (3-5), pivot 9   ->  1 2 3 7 5 9     pivot at index 5, 2 comparisons
partition (3-4), pivot 5   ->  1 2 3 5 7 9     pivot at index 3, 1 comparison
''', "text", title="Trace of worked example 2"),
        KEY("Best, average and worst cases", "The speed depends on how evenly the pivot splits the part.", cards=[
            ["Good pivot", "If the pivot splits the part into two nearly equal halves, there are about log2 n levels, each needing about n comparisons: about n log n."],
            ["Bad pivot", "If the pivot is always the smallest or largest item (for example the last item of an already sorted list), each part shrinks by only one item: (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 comparisons, about n squared."],
            ["Memory", "Quick sort sorts in place. The recursive calls use stack space: about log2 n deep on a good split, up to n on the worst."],
        ]),
        EX("Worked example 3: the worst case", intro="Quick sort 1, 2, 3, 4, 5, 6 with the last item as pivot.", steps=[
            S("First partition", text="The pivot is 6. Every other item is smaller, so all 5 comparisons put them left of the pivot. The pivot stays at index 5. The part is now 1 to 5."),
            S("Next partitions", text="The pivot 5 takes 4 comparisons, then 4 takes 3, then 3 takes 2, then 2 takes 1."),
            S("Total", text="5 + 4 + 3 + 2 + 1 = 15 comparisons, the same as bubble sort. Choosing the middle item (or a random item, or the median of three) as pivot avoids this case on sorted data."),
        ]),
        TIP("A short exam answer: quick sort is fast on average (n log n), in place, but slow (n squared) when the pivot is repeatedly the smallest or largest item, such as the last item of sorted data."),
        MISTAKE("Thinking the pivot ends up in the middle", "The pivot ends up in its final sorted position, which can be anywhere from the first to the last index of the part."),
        MISTAKE("Sorting the pivot again", "After partition the pivot is in place. The two recursive calls cover only the items on either side (low to p - 1 and p + 1 to high)."),
        QUIZ("Partition 6, 1, 8, 3 using the last item (3) as pivot. Which list results?", ["1, 3, 8, 6", "1, 3, 6, 8", "3, 1, 8, 6", "6, 1, 3, 8"], 0,
             "pivot = 3. 6 > 3: no. 1 <= 3: i = 0, swap a[0] and a[1]: 1, 6, 8, 3. 8 > 3: no. Place the pivot: swap a[1] with the pivot: 1, 3, 8, 6.", hint="Move items not greater than 3 to the left, then swap the pivot into place.",
             feedback=["", "This is the fully sorted list. One partition does not sort the right part.", "The pivot must end with all smaller items to its left.", "The pivot 3 is not at its final place here: 6 is on its left."]),
        QUIZ("When does quick sort (last item as pivot) take about n squared steps?", [
            "When the list is in random order",
            "When the list is already sorted",
            "When the list has exactly two items",
            "It never takes n squared steps",
        ], 1, "On sorted data the last item is the largest, so each partition removes only one item.", hint="What happens if the pivot is always the largest item?",
             feedback=["Random order gives fairly even splits: about n log n on average.", "", "Two items need one comparison.", "It does, in the worst case."]),
        PQ("Partition 10, 15, 5, 8, 12 using the last item as pivot. Show the final list and the pivot index.",
           "pivot 12. 10 <= 12: i = 0 (swap with itself). 15 > 12. 5 <= 12: i = 1, swap a[1] and a[2]: 10, 5, 15, 8, 12. 8 <= 12: i = 2, swap a[2] and a[3]: 10, 5, 8, 15, 12. Place the pivot: swap a[3] and a[4]: 10, 5, 8, 12, 15. The pivot 12 is at index 3."),
        PQ("Quick sort the list 3, 1, 2 (pivot the last item) and say how many comparisons are made.",
           "Partition with pivot 2: 3 > 2, 1 <= 2 (i = 0, swap a[0] and a[1]: 1, 3, 2). Place the pivot: 1, 2, 3 (2 comparisons). Left part 1 and right part 3 are single items. Total: 2 comparisons."),
        PQ("Explain why quick sort with the last item as pivot is slow on a sorted list of 1000 items. How many comparisons does it make?",
           "The last item is the largest, so every partition leaves all the other items on one side and shrinks the part by one. The comparisons are 999 + 998 + ... + 1 = 1000 x 999 / 2 = 499 500."),
        PQ("Give two ways to reduce the chance of the worst case.",
           "Choose the pivot as the middle item, a random item, or the median of the first, middle and last items, instead of always using the last item."),
        SUM("Quick sort picks a pivot, partitions the part around it, and then sorts the left and right parts.",
            "After a partition the pivot is in its final position.",
            "On a good split quick sort takes about n log n steps; on repeated bad splits it takes about n squared.",
            "It sorts in place, with recursion stack space.",
            "State the pivot rule you use; other rules give different intermediate lists but the same sorted result."),
    ],
))

# ============================================================== 11. Time complexity and Big-O
LESSONS.append(lesson(
    module=MODULE, topic=CX,
    title="Time complexity and Big-O notation",
    slug="csc-time-complexity-big-o",
    minutes=24,
    summary="Measure an algorithm by how its number of steps grows with the input size, simplify the count to Big-O by dropping constants and smaller terms, and know the classes from O(1) to O(n squared) and beyond.",
    objectives=[
        "Explain what time complexity measures and why seconds are not used",
        "Simplify a step count to Big-O by dropping constants and lower terms",
        "Place algorithms in the classes O(1), O(log n), O(n), O(n log n), O(n squared), O(2 to the n) and O(n!)",
        "Compare how the classes grow when n doubles",
    ],
    key_concepts=["Time complexity", "Big-O notation", "Input size n", "Worst case", "Growth rate", "Polynomial and exponential growth"],
    blocks=[
        H("Introduction"),
        T("A transport agency in Douala sells 100 tickets a day, and its ticket program works well. A year later a new scheme brings 100,000 tickets a day. One program still answers instantly. Another takes hours. Both were correct; they differ in how their work *grows* as the data grows.\n\n"
          "Computer scientists compare algorithms by that growth. They do not time them in seconds, because seconds depend on the machine, the language and what else is running."),
        D("The **time complexity** of an algorithm describes how the number of basic steps it needs grows as the size of the input, **n**, grows. A basic step is one simple operation such as a comparison, an assignment or an addition.", title="Definition: time complexity"),
        D("**Big-O notation** gives an upper bound on the growth of the step count. Write O(f(n)) where f(n) is the dominant term with its constant factor removed. Unless told otherwise we quote the **worst case**.", title="Definition: Big-O"),
        KEY("Two simplification rules", "Big-O keeps only what matters when n is large.", cards=[
            ["Drop constants", "3n and 100n are both O(n). A constant factor changes the speed by a fixed multiple, not the way it grows."],
            ["Drop smaller terms", "n squared + 5n + 2 is O(n squared). When n is large the n squared term dwarfs the rest."],
        ]),
        EX("Worked example 1: simplify 3n squared + 5n + 2", intro="Count the steps of an algorithm as 3n^2 + 5n + 2 and give its Big-O.", steps=[
            S("n = 10", text="3 x 100 + 50 + 2 = 352. The n squared part is 300 of 352."),
            S("n = 100", text="3 x 10 000 + 500 + 2 = 30 502. The n squared part is nearly all of it."),
            S("n = 1000", text="3 x 1 000 000 + 5000 + 2 = 3 005 002. The total is only 0.17 percent above 3n squared."),
            S("Conclusion", text="Drop the constant 3 and the smaller terms: the algorithm is O(n squared)."),
        ]),
        H("The common classes"),
        KEY("From fastest to slowest growth", "Learn an example of each.", cards=[
            ["O(1) constant", "The steps do not depend on n. Reading items[5], push and pop on a stack."],
            ["O(log n) logarithmic", "The work is cut in half each step. Binary search; searching a balanced binary search tree."],
            ["O(n) linear", "One step per item. Linear search, adding up a list, traversing a linked list."],
            ["O(n log n)", "Merge sort, and quick sort on average."],
            ["O(n squared) quadratic", "A loop inside a loop over n items. Bubble, insertion and selection sort."],
            ["O(2 to the n) exponential", "Work doubles when n grows by 1. Trying every subset of n items; naive recursive Fibonacci."],
            ["O(n!) factorial", "Trying every ordering of n items, as in brute-force route planning."],
        ]),
        CODE('''
def first_item(a):          # O(1): one step whatever the length
    return a[0]

def total(a):               # O(n): one pass
    s = 0
    for x in a:
        s = s + x
    return s

def count_pairs(a):         # O(n squared): loop inside loop
    c = 0
    for x in a:
        for y in a:
            c = c + 1
    return c

def halvings(n):            # O(log n): n is halved each time
    c = 0
    while n > 1:
        n = n // 2
        c = c + 1
    return c
''', "python", title="Listing 1: four growth rates"),
        EX("Worked example 2: count the steps", intro="Run the functions of Listing 1 for a list of n = 1024 items (halvings(1024) too).", steps=[
            S("first_item", text="1 step, however long the list is: O(1)."),
            S("total", text="The loop body runs 1024 times: O(n)."),
            S("count_pairs", text="The inner loop runs 1024 times for each of 1024 outer passes: 1024 x 1024 = 1 048 576 steps: O(n squared)."),
            S("halvings(1024)", text="1024 becomes 512, 256, 128, 64, 32, 16, 8, 4, 2, 1: 10 steps, which is log2 1024: O(log n)."),
        ]),
        CODE('''
n       log2 n    n log2 n      n squared      2 to the n
10      3.3       33            100            1 024
100     6.6       664           10 000         about 1.3 x 10^30
1000    10.0      9 966         1 000 000      far too large to write
''', "text", title="How the classes grow (values rounded)"),
        IMG("al-csc-big-o-growth.svg", alt="Curves of steps against n for O(1), O(log n), O(n), O(n log n) and O(n squared), with n squared rising fastest", caption="Figure 1. The shapes of the common growth rates for small n."),
        EX("Worked example 3: what happens when n doubles?", intro="A job takes 1000 steps for n = 100. How many steps for n = 200 for each class?", steps=[
            S("O(n)", text="Steps double: 2000."),
            S("O(n squared)", text="Steps grow by 2 x 2 = 4: 4000."),
            S("O(log n)", text="Only one more halving is needed. The steps rise by a fixed amount (about 1 in log2 n)."),
            S("O(2 to the n)", text="Adding just one item doubles the work, so doubling n squares it. Exponential algorithms are only practical for small n."),
        ]),
        D("An algorithm is called **tractable** if its time is bounded by a polynomial such as n, n log n or n squared. Exponential and factorial algorithms are not practical for large n, however fast the computer.", title="Tractable growth"),
        TIP("In a Paper 2 style answer, say what n is, what you count, and give the Big-O with a reason: for example, binary search is O(log n) because the search range is halved each comparison. Check the paper format with your teacher."),
        MISTAKE("Keeping the constants", "Writing O(5n) or O(n squared + n) is not wrong in meaning but is not simplified. Write O(n) and O(n squared)."),
        MISTAKE("Thinking O(n squared) is always slower than O(n) on every input", "Big-O is about growth for large n. For very small n, a program with a small constant factor in O(n squared) may beat a large-constant O(n) one. Big-O tells you who wins as n gets big."),
        MISTAKE("Confusing log n with n", "log2 1,000,000 is about 20, not 1,000,000. A logarithmic algorithm barely slows down as the data grows."),
        QUIZ("An algorithm takes 2n squared + 7n + 40 steps. What is its Big-O?", ["O(n)", "O(2n squared)", "O(n squared)", "O(n cubed)"], 2,
             "Drop the smaller terms 7n and 40, then drop the constant 2. The dominant term is n squared.", hint="Which term grows fastest, and what is left after removing its constant?",
             feedback=["n is the next term in size, not the dominant one.", "The constant 2 is dropped in Big-O.", "", "There is no n cubed term."]),
        QUIZ("Which algorithm is O(log n)?", ["Linear search", "Binary search on a sorted array", "Bubble sort", "Adding all items in a list"], 1,
             "Binary search halves the remaining range at each comparison.", hint="Which one halves the problem each step?",
             feedback=["Linear search is O(n).", "", "Bubble sort is O(n squared).", "Adding up the items is O(n)."]),
        PQ("State the Big-O of each: (a) 5n + 20, (b) n squared / 2, (c) 7, (d) 4n log n + 3n.",
           "(a) O(n). (b) O(n squared), because the factor 1/2 is dropped. (c) O(1). (d) O(n log n), because n log n is larger than n."),
        PQ("A program makes 1 step for n = 1 and every step count is exactly n squared. How many steps does it make for n = 50 and for n = 100? What is the ratio?",
           "50 squared = 2500 steps. 100 squared = 10 000 steps. The ratio is 4: doubling n multiplies the steps by 4."),
        PQ("Match each algorithm to its Big-O: merge sort, linear search, selection sort, reading the first element of an array.",
           "Merge sort: O(n log n). Linear search: O(n). Selection sort: O(n squared). Reading the first element: O(1)."),
        PQ("Explain why exponential algorithms are impractical. Use n = 30 and n = 40 for an algorithm that needs 2 to the n steps.",
           "2 to the 30 is about 1.07 billion steps and 2 to the 40 is about 1.1 trillion: adding ten items multiplies the work by 1024. The work soon exceeds what any computer can do in a reasonable time."),
        SUM("Time complexity counts how the number of basic steps grows with the input size n, not seconds.",
            "Big-O keeps the dominant term and drops constants and smaller terms; it usually describes the worst case.",
            "In order of growth: O(1), O(log n), O(n), O(n log n), O(n squared), O(2 to the n), O(n!).",
            "Doubling n doubles an O(n) cost, quadruples an O(n squared) cost and adds one step to an O(log n) cost.",
            "Polynomial algorithms are tractable; exponential and factorial ones are not for large n."),
    ],
))

# ============================================================== 12. Analysing code, space complexity
LESSONS.append(lesson(
    module=MODULE, topic=CX,
    title="Analysing algorithms, space complexity and choosing between sorts",
    slug="csc-analysing-space-comparing",
    minutes=25,
    summary="Work out the Big-O of code from its loops and recursion, define space complexity, and compare searching and sorting algorithms by time, memory and stability to choose the right one.",
    objectives=[
        "Find the Big-O of code from sequential, nested and halving loops",
        "Define space complexity and give O(1) and O(n) examples",
        "Explain the time and stack cost of recursion",
        "Compare the searches and sorts and choose one for a given situation",
    ],
    key_concepts=["Analysing loops", "Space complexity", "Auxiliary space", "Recursion cost", "Best, average and worst case", "Choosing an algorithm"],
    blocks=[
        H("Introduction"),
        T("A mobile money company in Yaounde must sort one million transactions every night. A programmer chooses an algorithm that is fine for the 100 test records, then the real run takes all night and never finishes. Choosing well needs two skills: reading the Big-O from code, and knowing what each standard algorithm costs in time *and* memory."),
        KEY("Rules for reading Big-O from code", "Work from the inside out.", cards=[
            ["Sequential parts add", "A loop over n followed by another loop over n costs n + n = 2n, which is O(n). The slowest part dominates."],
            ["Nested loops multiply", "An outer loop of n and an inner loop of n gives n x n = O(n squared)."],
            ["Halving gives log n", "A loop that halves (or doubles) a variable each time runs about log2 n times."],
        ]),
        CODE('''
def A(a):                         # two loops one after the other
    c = 0
    for x in a:
        c = c + 1
    for x in a:
        c = c + 1
    return c

def B(n):                         # inner loop starts after the outer index
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            c = c + 1
    return c

def C(n):                         # loop that halves
    c = 0
    while n > 1:
        n = n // 2
        c = c + 1
    return c
''', "python", title="Listing 1: three loop patterns"),
        EX("Worked example 1: analyse Listing 1", intro="Find the Big-O of A, B and C and check with n = 100 (a list of 100 items for A).", steps=[
            S("A", text="Two loops of n steps added: 2n = 200 steps for n = 100. Big-O: O(n)."),
            S("B", text="The inner loop runs n - 1, then n - 2, then down to 0 times: n(n - 1) / 2 = 100 x 99 / 2 = 4950 steps for n = 100. Dropping the constant 1/2 and the smaller term gives O(n squared)."),
            S("C", text="n is halved each time. For n = 1024 it takes 10 halvings, for n = 1 000 000 it takes 19. Big-O: O(log n)."),
        ]),
        H("Space complexity"),
        D("The **space complexity** of an algorithm describes how the amount of extra memory it needs grows with n. We usually count the **auxiliary space**: memory beyond the input itself.", title="Definition: space complexity"),
        KEY("Examples", "Counting what the algorithm creates, not what it is given.", cards=[
            ["O(1) space", "Adding up a list uses one extra variable. Bubble, insertion and selection sort work in place with only a temporary variable."],
            ["O(n) space", "Copying a list, or merge sort, which builds new lists totalling about n items."],
            ["Recursion uses stack space", "Each unfinished call keeps a stack frame. A recursion n levels deep uses O(n) stack space."],
        ]),
        CODE('''
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
''', "python", title="Listing 2: two recursive functions"),
        EX("Worked example 2: cost of recursion", intro="Analyse factorial and fib.", steps=[
            S("factorial(n)", text="It makes one call for each of n, n - 1, ..., 1: n calls, so time O(n). The calls wait on the stack until the base case returns, so the stack space is O(n) as well."),
            S("fib(n)", text="Each call makes two more calls. fib(10) makes 177 calls, fib(20) makes 21 891 and fib(30) makes 2 692 537. The count grows exponentially (O(2 to the n) is an upper bound). The same values are recomputed again and again."),
            S("Lesson", text="A recursive definition that matches the mathematics can still be very slow. Saving earlier results (memoisation) or using a loop fixes fib."),
        ]),
        H("Comparing the standard algorithms"),
        CODE('''
algorithm        best        average     worst       extra space   stable
bubble (flag)    O(n)        O(n^2)      O(n^2)      O(1)          yes
insertion        O(n)        O(n^2)      O(n^2)      O(1)          yes
selection        O(n^2)      O(n^2)      O(n^2)      O(1)          no
merge            O(n log n)  O(n log n)  O(n log n)  O(n)          yes
quick (last)     O(n log n)  O(n log n)  O(n^2)      O(log n) stack  no

linear search    O(1)        O(n)        O(n)        O(1)
binary search    O(1)        O(log n)    O(log n)    O(1)   (needs sorted data)
BST search       O(1)        O(log n)    O(n)        O(1)   (O(n) if the tree is a chain)
''', "text", title="Summary table (the quick sort stack depth is for a good split; it can reach n)"),
        EX("Worked example 3: which algorithm?", intro="Choose a sort for each case and give a reason.", steps=[
            S("One million records, time matters", text="Merge sort or quick sort: O(n log n). For n = 1 000 000 that is about 20 million steps against 1 000 000 000 000 for O(n squared). At 100 million steps per second (an illustrative speed) that is about 0.2 second against nearly 3 hours."),
            S("A list of 20 items that is almost sorted", text="Insertion sort. It needs about n steps when little must move, uses no extra memory and is simple."),
            S("A phone with very little free memory and a large list", text="Quick sort (in place, small stack) rather than merge sort, which needs about n extra memory."),
            S("Records must stay in their original order when keys are equal", text="Merge sort (or insertion sort for small lists): both are stable."),
        ]),
        TIP("When asked to compare, give a reason in terms of time, memory and the data (size, nearly sorted or not). Naming only the algorithm earns little."),
        MISTAKE("Counting the input as extra space", "The input list is given. Space complexity counts the extra memory the algorithm needs. Bubble sort on a list of a million items is O(1) extra space."),
        MISTAKE("Forgetting hidden loops", "Slicing a list, using the in keyword on a list, or sorting inside a loop each hide a loop of n steps. Count them."),
        QUIZ("What is the time complexity of this code?   for i in range(n): for j in range(n): for k in range(3): count = count + 1", ["O(n)", "O(n squared)", "O(n cubed)", "O(3n)"], 1,
             "The inner loop of 3 is a constant. n x n x 3 = 3n squared, which is O(n squared).", hint="Is the third loop's length linked to n?",
             feedback=["There are two loops of n nested inside each other.", "", "The third loop always runs 3 times, not n times.", "O(3n) is not what the nesting gives; and constants are dropped anyway."]),
        QUIZ("Which sorting algorithm needs O(n) extra space?", ["Bubble sort", "Insertion sort", "Merge sort", "Selection sort"], 2,
             "Merge sort builds new lists while merging, totalling about n items of extra memory. The other three work in place.", hint="Which sort copies items into new lists?",
             feedback=["Bubble sort swaps in place.", "Insertion sort shifts items in place.", "", "Selection sort swaps in place."]),
        PQ("State the time complexity of each: (a) a loop from 1 to n containing a loop from 1 to n; (b) a loop from 1 to n followed by another loop from 1 to n; (c) while n > 1: n = n // 2.",
           "(a) O(n squared). (b) O(n), because n + n = 2n and constants are dropped. (c) O(log n)."),
        PQ("Define space complexity and give one algorithm with O(1) and one with O(n) auxiliary space.",
           "Space complexity is how the extra memory an algorithm needs grows with the input size n. Bubble sort uses O(1) (one temporary variable). Merge sort uses O(n) (new lists of total size about n)."),
        PQ("The recursive function fib(n) calls itself twice. Explain why it is much slower than a loop that adds the last two values, and give the number of calls for fib(20).",
           "Each call makes two more calls and the same values are recomputed many times, so the number of calls grows exponentially: fib(20) makes 21 891 calls. A loop needs about n steps and O(1) space."),
        PQ("A school keeps 50 student records almost sorted and re-sorts them every day. Which of insertion sort and merge sort would you choose, and why?",
           "Insertion sort. On almost sorted data it takes about n steps, uses O(1) extra space and is simple, while merge sort still takes about n log n steps and needs O(n) extra space. For only 50 records the difference in speed is small either way."),
        SUM("Sequential code adds, nested loops multiply, a loop that halves is O(log n).",
            "Space complexity counts the extra memory an algorithm needs, including the stack used by recursion.",
            "Merge sort is O(n log n) in every case but needs O(n) extra space; quick sort is in place but O(n squared) in its worst case.",
            "Bubble, insertion and selection sort are O(n squared) in the worst case; insertion and bubble (with a flag) are O(n) on sorted data.",
            "Choose an algorithm using the data size, how sorted the data already is, memory limits and whether stability matters."),
    ],
))
