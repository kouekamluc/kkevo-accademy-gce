"""Upper Sixth Computer Science (A Level): draft lessons for every syllabus topic."""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "upper-sixth")

LESSONS = []

# ---------------------------------------------------------------------------
# Data Structures & Algorithms / Abstract data types
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Data Structures & Algorithms",
    topic="Abstract data types",
    title="Stacks, queues, linked lists and binary search trees",
    slug="abstract-data-types-stacks-queues-lists-trees",
    minutes=30,
    summary="Define the stack, queue, linked list and binary search tree, trace their operations step by step and choose the right structure for a problem.",
    objectives=[
        "Explain what an abstract data type is",
        "Trace push and pop on a stack, and enqueue and dequeue on a circular queue",
        "Describe singly and doubly linked lists and insert a node",
        "Build a binary search tree and give its in-order, pre-order and post-order traversals",
    ],
    key_concepts=["Abstract data type", "Stack", "Queue", "Circular queue", "Linked list", "Binary search tree", "Tree traversal"],
    blocks=[
        H("Introduction"),
        T("A secondary school in Bafoussam keeps hundreds of records: students waiting to pay fees, pages of a report that can be undone, a sorted list of matriculation numbers. Each job needs data stored in a particular order and accessed in a particular way.\n\n"
          "An **abstract data type** (ADT) describes the data and the operations allowed on it, without saying how they are programmed. A stack can be built with an array or with a linked list. The user of the stack only sees push and pop."),
        D("An **abstract data type** is a logical description of a collection of data together with the operations that can be performed on it, independent of any implementation.",
          note="A **data structure** is a concrete implementation of an ADT, for example an array with a top pointer."),
        KEY("The four ADTs in this lesson", "Each one fixes where data enters and where it leaves.", cards=[
            ["Stack", "LIFO: last in, first out. Operations: push, pop, peek, isEmpty, isFull."],
            ["Queue", "FIFO: first in, first out. Operations: enqueue, dequeue, isEmpty, isFull."],
            ["Linked list", "Nodes joined by pointers. Each node holds data and the address of the next node (and of the previous node in a doubly linked list)."],
            ["Binary search tree", "Each node has at most two children. Every key in the left subtree is smaller, every key in the right subtree is larger."],
        ]),
        H("Stacks"),
        T("A stack is like a pile of plates at a restaurant in Douala: you add and remove plates only at the top. In an array implementation a variable **top** holds the index of the top item. It starts at -1 for an empty stack. Stacks are used for undo features, subroutine return addresses and evaluating postfix expressions."),
        EX("Worked example 1: tracing a stack", intro="An empty stack is stored in an array of size 5 with top = -1. Trace the operations push(5), push(8), pop(), push(3), push(9), pop(), peek().", steps=[
            S("push(5), push(8)", text="top becomes 0, then 1. Stack (bottom to top): 5, 8."),
            S("pop()", text="Returns 8 and top becomes 0. Stack: 5."),
            S("push(3), push(9)", text="top becomes 1, then 2. Stack: 5, 3, 9."),
            S("pop()", text="Returns 9 and top becomes 1. Stack: 5, 3."),
            S("peek()", text="Returns 3 without removing it. Final stack: 5, 3 with top = 1."),
        ]),
        CODE('''
class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == len(self.items) - 1:
            raise OverflowError("stack is full")
        self.top += 1
        self.items[self.top] = value

    def pop(self):
        if self.top == -1:
            raise IndexError("stack is empty")
        value = self.items[self.top]
        self.top -= 1
        return value
''', "python", title="Listing 1: an array-based stack"),
        H("Queues and the circular queue"),
        T("A queue works like students lining up at the bursar's office: the first to arrive is served first. Items join at the **rear** and leave from the **front**. In a simple linear array, space at the front is wasted after items leave. A **circular queue** fixes this by wrapping the rear pointer back to index 0 using the remainder operator: rear = (rear + 1) mod size."),
        EX("Worked example 2: tracing a circular queue", intro="A circular queue has 4 slots (indices 0 to 3), front = 0, rear = -1, count = 0. Trace: enqueue A, B, C; dequeue twice; enqueue D, E, F.", steps=[
            S("Enqueue A, B, C", text="rear moves 0, 1, 2. count = 3. Slots: A B C -."),
            S("Dequeue twice", text="Returns A then B. front moves to 1, then 2. count = 1."),
            S("Enqueue D", text="rear = 3, count = 2. The queue holds C (slot 2) and D (slot 3)."),
            S("Enqueue E", text="rear = (3 + 1) mod 4 = 0, so E goes in slot 0. count = 3."),
            S("Enqueue F", text="rear = 1, count = 4, so the queue is now full. Slots: E F C D with front = 2. The queue order is C, D, E, F."),
        ]),
        H("Linked lists"),
        T("A **singly linked list** is a chain of nodes. Each node stores data and a pointer to the next node. A **head** pointer gives the first node and the last node points to null. To insert, you only change pointers; no items are shifted as in an array.\n\n"
          "A **doubly linked list** also stores a pointer to the previous node, so it can be traversed in both directions and a node can be deleted when you only have a pointer to it, at the cost of extra memory."),
        CODE('''
head -> [Abega | o-]-> [Fon | o-]-> [Ngono | null]

Insert "Eto" in alphabetical order:
1. Create node N with data "Eto".
2. Walk from head and stop at the last node whose data comes
   before "Eto" (Abega, because the next node, Fon, comes after Eto).
3. N.next = Abega.next      (N now points to Fon)
4. Abega.next = N

head -> [Abega | o-]-> [Eto | o-]-> [Fon | o-]-> [Ngono | null]
''', "text", title="Inserting into a sorted singly linked list"),
        MISTAKE("Changing pointers in the wrong order", "If you set Abega.next = N first, the address of Fon is lost and the rest of the list is cut off. Always link the new node to its successor before redirecting the predecessor."),
        H("Binary search trees"),
        T("In a **binary search tree** (BST) each node has a key, a left child and a right child. To insert, start at the root: go left if the new key is smaller, right if it is larger, until you reach an empty position. A balanced BST lets you find a key in about $\\log_2 n$ comparisons."),
        EX("Worked example 3: BST insertion and traversals", intro="Insert the student numbers 45, 23, 67, 12, 34, 56, 89 in that order into an empty BST, then give the three depth-first traversals.", steps=[
            S("Insert 45, 23, 67", text="45 is the root. 23 < 45 goes left. 67 > 45 goes right."),
            S("Insert 12 and 34", text="12 < 45, then 12 < 23: left child of 23. 34 < 45, then 34 > 23: right child of 23."),
            S("Insert 56 and 89", text="56 > 45, then 56 < 67: left child of 67. 89 > 45, then 89 > 67: right child of 67."),
            S("In-order (left, root, right)", text="12, 23, 34, 45, 56, 67, 89. In-order always gives the keys in ascending order."),
            S("Pre-order (root, left, right) and post-order (left, right, root)", text="Pre-order: 45, 23, 12, 34, 67, 56, 89. Post-order: 12, 34, 23, 56, 89, 67, 45."),
        ]),
        IMG("cs-bst-worked-example.svg",
            "Binary search tree with root 45. Left child 23 has children 12 and 34. Right child 67 has children 56 and 89. In-order traversal: 12, 23, 34, 45, 56, 67, 89.",
            caption="Figure 1. The binary search tree from worked example 3."),
        MISTAKE("Mixing up pre-order and post-order", "Remember where the root goes: pre-order visits the root before its subtrees, post-order after them. The root of the whole tree is first in pre-order and last in post-order."),
        MISTAKE("Forgetting overflow and underflow checks", "Examiners expect push to test for a full stack and pop to test for an empty one. The same applies to enqueue and dequeue."),
        QUIZ("A word processor lets a user undo the most recent action first. Which ADT is the best choice for storing the actions?",
             ["Queue", "Stack", "Binary search tree", "Circular queue"], 1,
             "Undo removes the most recent action first, which is last in, first out: a stack.",
             hint="Which action is undone first: the oldest or the newest?",
             feedback=["A queue would undo the oldest action first.", "", "A BST orders data by key, not by time of arrival.", "A circular queue is still first in, first out."]),
        QUIZ("Which traversal of a binary search tree outputs the keys in ascending order?",
             ["Pre-order", "Post-order", "In-order", "Breadth-first"], 2,
             "In-order visits the left subtree (smaller keys), then the node, then the right subtree (larger keys).",
             feedback=["Pre-order outputs the root first, which is usually not the smallest key.", "Post-order outputs the root last, which is usually not the largest key.", "", "Breadth-first goes level by level, not by size."]),
        H("Practice questions"),
        PQ("A stack is used to evaluate the postfix expression 6 2 + 5 × (where × means multiply). Show the contents of the stack after each symbol is read and give the result.",
           "Read 6: stack 6. Read 2: stack 6, 2. Read +: pop 2 and 6, push 8, stack 8. Read 5: stack 8, 5. Read ×: pop 5 and 8, push 40, stack 40. Result: 40."),
        PQ("Write an algorithm for dequeue on a circular queue stored in an array Q of size N with variables front, rear and count.",
           "IF count = 0 THEN report \"queue empty\" ELSE item ← Q[front]; front ← (front + 1) MOD N; count ← count − 1; RETURN item ENDIF. The MOD makes front wrap to 0 after the last slot."),
        PQ("Insert the keys 50, 30, 70, 20, 40, 60 into an empty BST. (a) Describe the tree. (b) Give the post-order traversal. (c) How many comparisons are needed to find 40?",
           "(a) 50 is the root; 30 is left of 50; 70 is right of 50; 20 is left of 30; 40 is right of 30; 60 is left of 70. (b) Post-order: 20, 40, 30, 60, 70, 50. (c) Three comparisons: with 50 (go left), with 30 (go right), with 40 (found)."),
        PQ("State one advantage and one disadvantage of a doubly linked list compared with a singly linked list.",
           "Advantage: it can be traversed backwards, and a node can be deleted using only a pointer to that node because its predecessor is known. Disadvantage: each node needs extra memory for the previous pointer, and every insertion or deletion must update more pointers."),
        SUM("An ADT describes data and its operations; a data structure is one way to implement it.",
            "A stack is LIFO (push, pop, peek); a queue is FIFO (enqueue, dequeue).",
            "A circular queue reuses freed slots with pointer = (pointer + 1) mod size.",
            "Linked lists change pointers instead of shifting data; link the new node before redirecting the old one.",
            "In a BST smaller keys go left and larger keys go right; in-order traversal gives ascending order."),
    ],
))

# ---------------------------------------------------------------------------
# Data Structures & Algorithms / Searching and sorting
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Data Structures & Algorithms",
    topic="Searching and sorting",
    title="Searching and sorting algorithms",
    slug="searching-and-sorting-algorithms",
    minutes=30,
    summary="Trace linear and binary search, and bubble, insertion, selection, merge and quick sort pass by pass, and compare when each one is useful.",
    objectives=[
        "Trace linear search and binary search and count comparisons",
        "Trace bubble, insertion and selection sort pass by pass",
        "Explain how merge sort and quick sort use divide and conquer",
        "Choose a suitable search or sort for a given situation",
    ],
    key_concepts=["Linear search", "Binary search", "Bubble sort", "Insertion sort", "Selection sort", "Merge sort", "Quick sort", "Pivot"],
    blocks=[
        H("Introduction"),
        T("A cooperative in Kumba stores the weights of cocoa bags delivered by its farmers. Before paying, the secretary must find a farmer's record quickly and print a list sorted by weight. Searching and sorting are two of the most common jobs a program does, and the method chosen can make the difference between a fraction of a second and many minutes."),
        H("Searching"),
        D("**Linear search** checks each item in turn from the start until the target is found or the list ends. It works on unsorted data.\n\n"
          "**Binary search** works only on sorted data. It compares the target with the middle item and discards the half that cannot contain it, repeating until the target is found or the search range is empty.",
          title="Two searches"),
        CODE('''
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1      # not found
''', "python", title="Listing 1: iterative binary search"),
        EX("Worked example 1: binary search", intro="The sorted list [3, 9, 14, 21, 27, 33, 40, 46, 52, 61, 70] has indices 0 to 10. Trace a search for 46, then for 25.", steps=[
            S("Search for 46: first comparison", text="low = 0, high = 10, mid = 5. items[5] = 33 < 46, so low = 6."),
            S("Second and third comparisons", text="mid = (6 + 10) // 2 = 8. items[8] = 52 > 46, so high = 7. Then mid = (6 + 7) // 2 = 6. items[6] = 40 < 46, so low = 7."),
            S("Fourth comparison", text="mid = 7. items[7] = 46: found at index 7 after 4 comparisons. Linear search would need 8."),
            S("Search for 25", text="mid = 5 (33 > 25, high = 4); mid = 2 (14 < 25, low = 3); mid = 3 (21 < 25, low = 4); mid = 4 (27 > 25, high = 3)."),
            S("Stop condition", text="Now low = 4 > high = 3, so the range is empty and the function returns -1: 25 is not in the list."),
        ]),
        H("Simple sorts: bubble, insertion, selection"),
        KEY("How the three simple sorts work", "All three sort in place and take about $n^2$ comparisons in the worst case.", cards=[
            ["Bubble sort", "Compare neighbours and swap if out of order. After each pass the largest remaining item has bubbled to the end. Stop early if a pass makes no swaps."],
            ["Insertion sort", "Take the next item and insert it into its correct place in the sorted part on the left, shifting larger items right."],
            ["Selection sort", "Find the smallest item in the unsorted part and swap it into the first unsorted position."],
        ]),
        EX("Worked example 2: bubble sort pass by pass", intro="Sort the cocoa bag weights [29, 10, 14, 37, 13] (kg) into ascending order with bubble sort, using a flag to stop early.", steps=[
            S("Pass 1", text="29 and 10 swap; 29 and 14 swap; 29 and 37 stay; 37 and 13 swap. Result: [10, 14, 29, 13, 37]. 37 is now in place."),
            S("Pass 2", text="10 and 14 stay; 14 and 29 stay; 29 and 13 swap. Result: [10, 14, 13, 29, 37]."),
            S("Pass 3", text="10 and 14 stay; 14 and 13 swap. Result: [10, 13, 14, 29, 37]."),
            S("Pass 4", text="10 and 13 stay. No swaps were made, so the flag stays false and the algorithm stops. Sorted: [10, 13, 14, 29, 37]."),
        ]),
        CODE('''
Insertion sort on [29, 10, 14, 37, 13]
  insert 10 : [10, 29, 14, 37, 13]
  insert 14 : [10, 14, 29, 37, 13]
  insert 37 : [10, 14, 29, 37, 13]   (already in place)
  insert 13 : [10, 13, 14, 29, 37]

Selection sort on [29, 10, 14, 37, 13]
  pass 1 : smallest is 10, swap with 29 -> [10, 29, 14, 37, 13]
  pass 2 : smallest is 13, swap with 29 -> [10, 13, 14, 37, 29]
  pass 3 : smallest is 14, already in place
  pass 4 : smallest is 29, swap with 37 -> [10, 13, 14, 29, 37]
''', "text", title="The same list sorted by insertion and selection sort"),
        CODE('''
static void insertionSort(int[] a) {
    for (int i = 1; i < a.length; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];   // shift larger item right
            j--;
        }
        a[j + 1] = key;
    }
}
''', "java", title="Listing 2: insertion sort in Java"),
        H("Divide and conquer: merge sort and quick sort"),
        T("**Merge sort** splits the list in half again and again until each part has one item, then merges neighbouring parts back together in order. Merging two sorted lists only needs one pass, always taking the smaller front item. Merge sort takes about $n \\log_2 n$ steps in every case but needs extra memory for the merged lists."),
        EX("Worked example 3: merge sort", intro="Sort [38, 27, 43, 3, 9, 82, 10] with merge sort.", steps=[
            S("Split", text="[38, 27, 43, 3] and [9, 82, 10]; then [38, 27], [43, 3], [9, 82], [10]; then single items."),
            S("Merge pairs", text="[27, 38], [3, 43], [9, 82], [10]."),
            S("Merge again", text="[27, 38] with [3, 43] gives [3, 27, 38, 43]. [9, 82] with [10] gives [9, 10, 82]."),
            S("Final merge", text="Compare front items each time: 3, 9, 10, 27, 38, 43, 82. Result: [3, 9, 10, 27, 38, 43, 82]."),
        ]),
        T("**Quick sort** chooses a **pivot**, then partitions the list so that items smaller than the pivot are on its left and larger items on its right. The pivot is then in its final place, and the two sides are sorted recursively. For example, with pivot 5, the list [7, 2, 9, 4, 3, 8, 5] can be partitioned into [2, 4, 3] 5 [9, 8, 7]; sorting each side gives [2, 3, 4, 5, 7, 8, 9]. Quick sort is usually very fast ($n \\log_2 n$ on average) but falls to $n^2$ if the pivot is always the smallest or largest item, for example when the list is already sorted and the last item is the pivot."),
        MISTAKE("Using binary search on unsorted data", "Binary search assumes the list is sorted. On unsorted data it can discard the half that contains the target and wrongly report \"not found\"."),
        MISTAKE("Showing only the final list", "When a question asks for the list after each pass, write the whole list after every pass. Marks are given for the intermediate states, not just the answer."),
        MISTAKE("Mixing up insertion and selection sort", "Insertion sort takes the next item and shifts it into place in the sorted part. Selection sort searches the unsorted part for the minimum and makes one swap per pass."),
        QUIZ("What is the maximum number of comparisons binary search needs to search a sorted list of 1000 items?",
             ["10", "500", "1000", "100"], 0,
             "Each comparison halves the range: $2^{10} = 1024 \\ge 1000$, so at most 10 comparisons are needed.",
             hint="How many times can you halve 1000 before reaching 1?",
             feedback=["", "500 is the average for linear search, not binary search.", "1000 is the worst case for linear search.", "Halving 1000 needs far fewer than 100 steps."]),
        QUIZ("After the first pass of bubble sort (ascending) on [5, 1, 4, 2, 8], what is the list?",
             ["[1, 4, 2, 5, 8]", "[1, 2, 4, 5, 8]", "[1, 5, 4, 2, 8]", "[5, 1, 4, 2, 8]"], 0,
             "5 and 1 swap, 5 and 4 swap, 5 and 2 swap, 5 and 8 stay: [1, 4, 2, 5, 8].",
             feedback=["", "That is the fully sorted list; one pass is not enough here.", "That is the list after only the first comparison.", "The first comparison already swaps 5 and 1."]),
        H("Practice questions"),
        PQ("Show the list after each pass of selection sort (ascending) on [64, 25, 12, 22, 11].",
           "Pass 1: swap 11 and 64 giving [11, 25, 12, 22, 64]. Pass 2: smallest of the rest is 12, swap with 25 giving [11, 12, 25, 22, 64]. Pass 3: smallest is 22, swap with 25 giving [11, 12, 22, 25, 64]. Pass 4: 25 is already in place. Final: [11, 12, 22, 25, 64]."),
        PQ("The sorted list [4, 8, 15, 16, 23, 42, 50] is searched for 23 with binary search. Give the value of mid at each step and the number of comparisons.",
           "Indices 0 to 6. mid = 3 (16 < 23, so low = 4). mid = (4 + 6) // 2 = 5 (42 > 23, so high = 4). mid = 4 (23 found). Three comparisons."),
        PQ("State two differences between merge sort and quick sort.",
           "Merge sort always splits the list in the middle and does its work when merging; quick sort splits around a pivot and does its work when partitioning. Merge sort is about $n \\log_2 n$ in every case but needs extra memory; quick sort sorts in place but can degrade to $n^2$ with a poor pivot."),
        PQ("A list is already nearly sorted. Explain why insertion sort is a good choice.",
           "Each item is compared with its left neighbour and, if it is already in place, the inner loop stops immediately. For a nearly sorted list very few shifts are needed, so insertion sort runs in close to linear time."),
        SUM("Linear search works on any list; binary search needs a sorted list and halves the range each time.",
            "Bubble sort swaps neighbours; insertion sort shifts items into a sorted part; selection sort swaps in the minimum.",
            "A flag lets bubble sort stop after a pass with no swaps.",
            "Merge sort splits then merges; quick sort partitions around a pivot.",
            "Always show the full list after each pass when tracing a sort."),
    ],
))

# ---------------------------------------------------------------------------
# Data Structures & Algorithms / Complexity
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Data Structures & Algorithms",
    topic="Complexity",
    title="Time and space complexity with Big-O notation",
    slug="algorithm-complexity-big-o",
    minutes=25,
    summary="Measure how the running time and memory of an algorithm grow with input size, derive Big-O from code, and compare O(1), O(log n), O(n), O(n log n) and O(n²).",
    objectives=[
        "Explain time complexity and space complexity",
        "Derive the Big-O order of a piece of code by counting basic operations",
        "Rank the common orders from O(1) to O(n²)",
        "Give the best, average and worst case complexity of standard searches and sorts",
    ],
    key_concepts=["Time complexity", "Space complexity", "Big-O notation", "Constant time", "Logarithmic time", "Linear time", "Quadratic time", "Worst case"],
    blocks=[
        H("Introduction"),
        T("Imagine the GCE Board's results system. A method that works well for 50 candidates in one centre might be far too slow for over 100 000 candidates across Cameroon. Timing a program with a stopwatch is not reliable, because the result depends on the computer, the language and what else is running.\n\n"
          "Instead we ask: **how does the number of steps grow as the input size $n$ grows?** That is what complexity measures."),
        D("**Time complexity** describes how the number of basic operations an algorithm performs grows with the input size $n$. **Space complexity** describes how the extra memory it needs grows with $n$.", title="Definitions"),
        D("**Big-O notation** gives an upper bound on the growth rate. To find it, count the operations as a function of $n$, keep only the fastest-growing term and drop its constant coefficient.",
          title="Big-O notation", formula=r"T(n) = 3n^2 + 2n + 5 \;\Rightarrow\; O(n^2)",
          note="For large $n$ the $n^2$ term dominates: at $n = 1000$ it contributes 3 000 000 while $2n + 5$ adds only 2005."),
        KEY("The common orders, fastest first", "Each row grows faster than the one before it.", cards=[
            ["O(1) constant", "Steps do not depend on $n$: reading an array element by index, push and pop on a stack."],
            ["O(log n) logarithmic", "The problem is halved each step: binary search, search in a balanced BST."],
            ["O(n) linear", "Each item is visited a fixed number of times: linear search, finding the maximum."],
            ["O(n log n)", "Divide and conquer with linear work per level: merge sort, quick sort on average."],
            ["O(n²) quadratic", "A loop inside a loop over the data: bubble, insertion and selection sort in the worst case."],
        ]),
        CODE('''
     n    log2 n    n log2 n          n^2
     8         3          24           64
    16         4          64          256
  1024        10      10 240    1 048 576
''', "text", title="Table 1: how the orders grow"),
        H("Deriving Big-O from code"),
        EX("Worked example 1: a single loop", intro="Find the time complexity of this function, which totals the daily sales of a market stall over n days.", steps=[
            S("Count the statements outside the loop", text="total = 0 and return total run once each: 2 operations."),
            S("Count the loop", text="The body total = total + sales[i] runs n times: n operations."),
            S("Write T(n)", math=r"T(n) = n + 2"),
            S("Keep the dominant term", text="Drop the constant 2. The function is O(n): linear time. It uses only one extra variable, so its space complexity is O(1)."),
        ]),
        CODE('''
def total_sales(sales):
    total = 0
    for i in range(len(sales)):
        total = total + sales[i]
    return total
''', "python", title="Listing 1: code for worked example 1"),
        EX("Worked example 2: nested loops in bubble sort", intro="Show that bubble sort without the early-stop flag makes n(n − 1)/2 comparisons on a list of n items, and give its Big-O order.", steps=[
            S("Count comparisons in each pass", text="Pass 1 compares n − 1 pairs, pass 2 compares n − 2 pairs, and so on until the last pass compares 1 pair."),
            S("Add them up", math=r"(n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2}"),
            S("Expand", math=r"\frac{n(n-1)}{2} = \frac{1}{2}n^2 - \frac{1}{2}n"),
            S("Keep the dominant term and drop the constant", text="The dominant term is the n² term, so bubble sort is O(n²). For n = 10 it makes 45 comparisons; for n = 100 it makes 4950."),
        ]),
        EX("Worked example 3: a halving loop", intro="How many times does the body of this loop run, and what is its order? i = n; WHILE i > 1: i = i DIV 2.", steps=[
            S("Trace for n = 16", text="i takes the values 16, 8, 4, 2, 1. The body runs 4 times."),
            S("Generalise", math=r"16 = 2^4 \;\Rightarrow\; \text{runs} = \log_2 16 = 4"),
            S("State the order", text="The body runs about log2 n times, so the loop is O(log n). This is why binary search is so fast."),
        ]),
        H("Best, average and worst case"),
        T("The same algorithm can take different numbers of steps on different inputs of the same size. Linear search finds the target at position 1 in the best case (O(1)) but checks all n items in the worst case (O(n)). Examiners usually want the **worst case** unless they say otherwise, because it is a guarantee."),
        CODE('''
Algorithm         Best         Average      Worst        Extra space
Linear search     O(1)         O(n)         O(n)         O(1)
Binary search     O(1)         O(log n)     O(log n)     O(1)
Bubble sort*      O(n)         O(n^2)       O(n^2)       O(1)
Insertion sort    O(n)         O(n^2)       O(n^2)       O(1)
Selection sort    O(n^2)       O(n^2)       O(n^2)       O(1)
Merge sort        O(n log n)   O(n log n)   O(n log n)   O(n)
Quick sort        O(n log n)   O(n log n)   O(n^2)       O(log n)

* with the early-stop flag
''', "text", title="Table 2: complexity of standard algorithms"),
        TIP("To predict running time, use the ratio. If an O(n²) program takes 2 seconds for n = 1000, tripling n multiplies the time by 3² = 9, so n = 3000 takes about 18 seconds. An O(n) program would take only about 6 seconds."),
        MISTAKE("Keeping constants and lower terms", "Writing O(3n² + 2n) or O(n/2) is wrong. Big-O keeps only the dominant term without its coefficient: O(n²) and O(n)."),
        MISTAKE("Assuming two loops always means O(n²)", "Two loops one after the other give n + n = 2n, which is O(n). Only nested loops that each run about n times give O(n²)."),
        QUIZ("An algorithm performs $5n + 4n^2 + 100$ operations. What is its time complexity?",
             ["O(n²)", "O(n)", "O(4n²)", "O(100)"], 0,
             "The $4n^2$ term grows fastest; dropping the coefficient gives O(n²).",
             feedback=["", "The n² term grows faster than the 5n term, so it dominates.", "Big-O drops constant coefficients.", "Constants are the least important part for large n."]),
        QUIZ("Which algorithm has O(log n) worst-case time complexity?",
             ["Linear search", "Binary search on a sorted array", "Merge sort", "Selection sort"], 1,
             "Binary search halves the remaining range at every comparison.",
             feedback=["Linear search may check every item: O(n).", "", "Merge sort is O(n log n).", "Selection sort is O(n²)."]),
        H("Practice questions"),
        PQ("Give the Big-O time complexity of: (a) accessing the 50th element of an array; (b) printing every element of an n by n table using two nested loops; (c) finding the largest value in an unsorted list.",
           "(a) O(1): the address is calculated directly from the index. (b) O(n²): the inner loop runs n times for each of the n outer iterations. (c) O(n): every item must be examined once."),
        PQ("A sorting program takes 4 seconds to sort 2000 records. Estimate the time for 8000 records if the algorithm is (a) O(n²) (b) O(n).",
           "The input is 4 times larger. (a) Time grows by 4² = 16, so about 64 seconds. (b) Time grows by 4, so about 16 seconds."),
        PQ("Explain why merge sort has space complexity O(n) while selection sort has O(1).",
           "Merge sort copies items into temporary lists while merging, and these lists can hold all n items. Selection sort only swaps items inside the original array and needs a few extra variables whatever the size of n."),
        PQ("Count the comparisons made by selection sort on a list of 6 items, and hence state its order.",
           "The passes make 5 + 4 + 3 + 2 + 1 = 15 comparisons, which is n(n − 1)/2 with n = 6. Selection sort always does this many comparisons, so it is O(n²) in every case."),
        SUM("Complexity measures how steps (time) or memory (space) grow with input size n.",
            "For Big-O, keep the dominant term and drop its coefficient.",
            "Order from fastest to slowest: O(1), O(log n), O(n), O(n log n), O(n²).",
            "Nested loops over the data usually give O(n²); halving gives O(log n).",
            "Unless told otherwise, quote the worst case."),
    ],
))

# ---------------------------------------------------------------------------
# Relational Databases / Relational algebra
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Relational algebra",
    title="Relational algebra: select, project, product, join and set operations",
    slug="relational-algebra-operations",
    minutes=25,
    summary="Use the relational algebra operators select, project, Cartesian product, join, union, intersection and difference to query a school records database.",
    objectives=[
        "State the effect of select, project, product and join on a relation",
        "Apply union, intersection and difference to union-compatible relations",
        "Write and evaluate a relational algebra expression that combines several operators",
        "Relate relational algebra expressions to equivalent SQL queries",
    ],
    key_concepts=["Relation", "Tuple", "Attribute", "Selection", "Projection", "Cartesian product", "Natural join", "Union compatibility"],
    blocks=[
        H("Introduction"),
        T("A school in Buea stores its records in a relational database. Before writing SQL, it helps to know the small set of operations that every query is built from. **Relational algebra** is that set: each operator takes one or two relations (tables) as input and produces a new relation as output, so operators can be combined like arithmetic."),
        D("A **relation** is a table with a fixed set of named columns called **attributes**. Each row is a **tuple**. No two tuples in a relation are identical, and the order of rows does not matter.", title="Definition"),
        CODE('''
STUDENT                                   RESULT
StudentID  Name    Class  Town            StudentID  Subject  Grade
S1         Abena   L6     Buea            S1         Maths    A
S2         Bih     U6     Bamenda         S2         Maths    C
S3         Nkeng   U6     Buea            S3         CompSci  B
S4         Tchoua  L6     Dschang         S3         Maths    A
''', "text", title="Table 1: the relations used in this lesson"),
        H("The unary operators: select and project"),
        D(r"**Selection** $\sigma_{\text{condition}}(R)$ keeps the tuples (rows) of $R$ that satisfy the condition. All attributes are kept.", title="Select",
          formula=r"\sigma_{\text{Town} = \text{'Buea'}}(\text{STUDENT})"),
        D(r"**Projection** $\pi_{\text{attributes}}(R)$ keeps only the listed attributes (columns). Duplicate tuples in the result are removed.", title="Project",
          formula=r"\pi_{\text{Name, Town}}(\text{STUDENT})"),
        EX("Worked example 1: select then project", intro=r"Evaluate $\pi_{\text{Name}}(\sigma_{\text{Class} = \text{'U6'}}(\text{STUDENT}))$ and say what it means.", steps=[
            S("Work from the inside out", text="First evaluate the selection on STUDENT."),
            S("Selection", text="Rows with Class = U6: (S2, Bih, U6, Bamenda) and (S3, Nkeng, U6, Buea)."),
            S("Projection", text="Keep only the Name attribute: Bih and Nkeng."),
            S("Interpret", text="The expression lists the names of all Upper Sixth students: {Bih, Nkeng}."),
        ]),
        H("Combining two relations: product and join"),
        D(r"The **Cartesian product** $R \times S$ pairs every tuple of $R$ with every tuple of $S$. If $R$ has $m$ tuples and $S$ has $n$ tuples, the product has $m \times n$ tuples, and its attributes are those of $R$ followed by those of $S$.", title="Cartesian product"),
        T(r"STUDENT $\times$ RESULT has $4 \times 4 = 16$ tuples and $4 + 3 = 7$ attributes. Most of these pairs are meaningless, for example Abena paired with Bih's Maths result. A **join** fixes this by keeping only the pairs that match."),
        D(r"A **theta join** $R \bowtie_{\text{condition}} S$ is a product followed by a selection: $R \bowtie_{c} S = \sigma_{c}(R \times S)$. A **natural join** $R \bowtie S$ matches tuples on all attributes with the same name and shows each common attribute once.", title="Join",
          formula=r"\text{STUDENT} \bowtie \text{RESULT} = \pi_{\ldots}(\sigma_{\text{STUDENT.StudentID} = \text{RESULT.StudentID}}(\text{STUDENT} \times \text{RESULT}))"),
        EX("Worked example 2: a natural join", intro=r"Find the names of students who scored grade A, using $\pi_{\text{Name}}(\sigma_{\text{Grade} = \text{'A'}}(\text{STUDENT} \bowtie \text{RESULT}))$.", steps=[
            S("Join on StudentID", text="S1 matches one result, S2 matches one, S3 matches two. S4 has no result, so S4 does not appear. The join has 4 tuples and 6 attributes: StudentID, Name, Class, Town, Subject, Grade."),
            S("Select Grade = A", text="(S1, Abena, L6, Buea, Maths, A) and (S3, Nkeng, U6, Buea, Maths, A)."),
            S("Project Name", text="Result: {Abena, Nkeng}."),
        ]),
        CODE('''
StudentID  Name   Class  Town     Subject  Grade
S1         Abena  L6     Buea     Maths    A
S2         Bih    U6     Bamenda  Maths    C
S3         Nkeng  U6     Buea     CompSci  B
S3         Nkeng  U6     Buea     Maths    A
''', "text", title="Table 2: STUDENT natural join RESULT"),
        H("Set operations"),
        T(r"**Union** $R \cup S$ contains tuples in $R$ or $S$ or both. **Intersection** $R \cap S$ contains tuples in both. **Difference** $R - S$ contains tuples in $R$ but not in $S$. These three only work on **union-compatible** relations: same number of attributes, with matching domains."),
        EX("Worked example 3: union, intersection and difference", intro="CHOIR(Name) = {Abena, Bih, Nkeng} and FOOTBALL(Name) = {Bih, Tchoua}. Find the union, the intersection and CHOIR − FOOTBALL. Then find the IDs of students with no result.", steps=[
            S("Union", math=r"\text{CHOIR} \cup \text{FOOTBALL} = \{\text{Abena, Bih, Nkeng, Tchoua}\}", text="Bih appears only once."),
            S("Intersection", math=r"\text{CHOIR} \cap \text{FOOTBALL} = \{\text{Bih}\}"),
            S("Difference", math=r"\text{CHOIR} - \text{FOOTBALL} = \{\text{Abena, Nkeng}\}"),
            S("Students with no result", math=r"\pi_{\text{StudentID}}(\text{STUDENT}) - \pi_{\text{StudentID}}(\text{RESULT}) = \{\text{S4}\}",
              text="Both projections have one attribute, StudentID, so they are union-compatible."),
        ]),
        CODE('''
-- pi Name ( sigma Grade = 'A' ( STUDENT join RESULT ) )
SELECT DISTINCT S.Name
FROM STUDENT S
JOIN RESULT R ON S.StudentID = R.StudentID
WHERE R.Grade = 'A';

-- pi StudentID (STUDENT) - pi StudentID (RESULT)
SELECT StudentID FROM STUDENT
EXCEPT
SELECT StudentID FROM RESULT;
''', "sql", title="Listing 1: the same queries in SQL"),
        TIP("SELECT in SQL corresponds to projection, not selection. The relational algebra selection is the WHERE clause."),
        MISTAKE("Confusing select and project", r"$\sigma$ chooses rows; $\pi$ chooses columns. A quick memory aid: sigma for sieving rows, pi for picking columns."),
        MISTAKE("Applying union to incompatible relations", "STUDENT ∪ RESULT is not allowed: the relations have different numbers of attributes. Project both onto matching attributes first."),
        QUIZ(r"Relation R has 5 tuples and 3 attributes; relation S has 4 tuples and 2 attributes. How many tuples and attributes does $R \times S$ have?",
             ["20 tuples, 5 attributes", "9 tuples, 5 attributes", "20 tuples, 6 attributes", "9 tuples, 6 attributes"], 0,
             r"The product pairs every tuple: $5 \times 4 = 20$. The attributes are placed side by side: $3 + 2 = 5$.",
             feedback=["", "Tuples are multiplied, not added.", "Attributes are added, not multiplied.", "Tuples are multiplied and attributes are added."]),
        H("Practice questions"),
        PQ(r"Using Table 1, evaluate $\pi_{\text{Name}}(\sigma_{\text{Town} = \text{'Buea'} \wedge \text{Class} = \text{'L6'}}(\text{STUDENT}))$.",
           "Only S1 lives in Buea and is in L6, so the result is {Abena}."),
        PQ("Write a relational algebra expression for the subjects taken by Nkeng, and evaluate it.",
           r"$\pi_{\text{Subject}}(\sigma_{\text{Name} = \text{'Nkeng'}}(\text{STUDENT} \bowtie \text{RESULT}))$. The join gives two tuples for Nkeng, so the result is {CompSci, Maths}."),
        PQ("Explain the difference between a Cartesian product and a natural join, and state which one is usually wanted in a query.",
           r"A Cartesian product pairs every tuple of one relation with every tuple of the other, including pairs that are unrelated. A natural join keeps only pairs whose common attributes have equal values and shows each common attribute once. A join is almost always what is wanted; it equals a product followed by a selection on the matching attributes."),
        PQ(r"Using Table 1, find $\pi_{\text{StudentID}}(\sigma_{\text{Subject} = \text{'Maths'}}(\text{RESULT})) \cap \pi_{\text{StudentID}}(\sigma_{\text{Town} = \text{'Buea'}}(\text{STUDENT}))$ and say what it means.",
           "The left side gives {S1, S2, S3}; the right side gives {S1, S3}. The intersection is {S1, S3}: the students from Buea who took Maths."),
        SUM(r"Selection $\sigma$ keeps rows that meet a condition; projection $\pi$ keeps chosen columns.",
            r"The product $R \times S$ has $m \times n$ tuples; a join is a product followed by a selection.",
            "A natural join matches tuples on attributes with the same name.",
            "Union, intersection and difference need union-compatible relations.",
            "Evaluate nested expressions from the inside out."),
    ],
))

# ---------------------------------------------------------------------------
# Relational Databases / Normalization
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Normalization",
    title="Functional dependencies and normalization to 3NF and BCNF",
    slug="normalization-1nf-2nf-3nf-bcnf",
    minutes=30,
    summary="Identify functional dependencies and update anomalies, then normalize a wholesaler's order table step by step through 1NF, 2NF and 3NF, and test for BCNF.",
    objectives=[
        "Define a functional dependency and identify the dependencies in a table",
        "Explain insertion, update and deletion anomalies",
        "Normalize an unnormalized table to 1NF, 2NF and 3NF",
        "Test whether a relation is in BCNF and decompose it if not",
    ],
    key_concepts=["Functional dependency", "Determinant", "Candidate key", "Partial dependency", "Transitive dependency", "1NF", "2NF", "3NF", "BCNF", "Anomaly"],
    blocks=[
        H("Introduction"),
        T("A rice and oil wholesaler at Mokolo market in Yaoundé keeps every order in one big spreadsheet. Each row repeats the customer's name and town and the product's description and price. When the price of a 50 kg bag of rice changes, someone must edit dozens of rows, and one missed row makes the data inconsistent.\n\n"
          "**Normalization** is a step-by-step method for splitting such a table into smaller, well-structured relations so that each fact is stored once."),
        D("Attribute B is **functionally dependent** on attribute A, written A → B, if each value of A is associated with exactly one value of B. A is called the **determinant**.",
          title="Functional dependency", note="Example: ProductCode → UnitPrice, because each product code has one price. But UnitPrice → ProductCode is false: two products can cost the same."),
        KEY("The normal forms", "Each normal form includes all the rules of the one before it.", cards=[
            ["1NF", "Every attribute holds a single (atomic) value and there are no repeating groups. A primary key is identified."],
            ["2NF", "1NF, and no partial dependency: no non-key attribute depends on only part of a composite key."],
            ["3NF", "2NF, and no transitive dependency: no non-key attribute depends on another non-key attribute."],
            ["BCNF", "Every determinant is a candidate key."],
        ]),
        CODE('''
OrderNo  Date        CustID  CustName     Town     | ProdCode  Description    Price  Qty
101      02/03/2026  C7      Mama Ngozi   Yaounde  | P1        Rice 50 kg     22000  2
                                                   | P4        Palm oil 20 L  18000  1
102      02/03/2026  C9      Ets Fomba    Bafia    | P1        Rice 50 kg     22000  5
103      03/03/2026  C7      Mama Ngozi   Yaounde  | P4        Palm oil 20 L  18000  3
                                                   | P6        Sugar 25 kg    15500  2
''', "text", title="Table 1: unnormalized orders (prices in FCFA)"),
        H("Why normalize: anomalies"),
        EX("Worked example 1: dependencies and anomalies", intro="For the data in Table 1, list the functional dependencies and give one example of each type of anomaly.", steps=[
            S("Order details", text="OrderNo → Date, CustID. Each order has one date and one customer."),
            S("Customer and product details", text="CustID → CustName, Town. ProdCode → Description, Price."),
            S("Order line", text="(OrderNo, ProdCode) → Qty. The quantity depends on both the order and the product."),
            S("Update anomaly", text="Mama Ngozi's town is stored twice. If she moves and only one row is changed, the data contradicts itself."),
            S("Insertion and deletion anomalies", text="A new product cannot be recorded until someone orders it (insertion). Deleting order 102 also deletes the only record of customer Ets Fomba (deletion)."),
        ]),
        H("From UNF to 3NF"),
        EX("Worked example 2: normalizing the orders table", intro="Normalize Table 1 to third normal form. Primary key attributes are marked KEY.", steps=[
            S("1NF: remove the repeating group", text="Write one row per product per order, repeating the order details. The primary key must identify a row, so it becomes the composite key (OrderNo, ProdCode)."),
            S("Check for partial dependencies", text="Date, CustID, CustName and Town depend only on OrderNo. Description and Price depend only on ProdCode. Only Qty depends on the whole key."),
            S("2NF: remove partial dependencies", text="ORDER(OrderNo KEY, Date, CustID, CustName, Town); PRODUCT(ProdCode KEY, Description, Price); ORDER_LINE(OrderNo KEY, ProdCode KEY, Qty)."),
            S("Check for transitive dependencies", text="In ORDER, OrderNo → CustID and CustID → CustName, Town. So CustName and Town depend on the key only through the non-key attribute CustID."),
            S("3NF: remove the transitive dependency", text="CUSTOMER(CustID KEY, CustName, Town); ORDER(OrderNo KEY, Date, CustID); PRODUCT and ORDER_LINE stay as they are. CustID in ORDER is now a foreign key to CUSTOMER."),
        ]),
        CODE('''
CUSTOMER(CustID, CustName, Town)                 key: CustID
ORDER(OrderNo, Date, CustID)                     key: OrderNo;  CustID -> CUSTOMER
PRODUCT(ProdCode, Description, Price)            key: ProdCode
ORDER_LINE(OrderNo, ProdCode, Qty)               key: (OrderNo, ProdCode)
                                                 OrderNo -> ORDER, ProdCode -> PRODUCT
''', "text", title="Table 2: the 3NF design"),
        TIP("A quick test for 3NF: every non-key attribute must depend on the key, the whole key, and nothing but the key."),
        H("Boyce-Codd normal form"),
        T("Most 3NF relations are also in BCNF. The difference appears only when a relation has overlapping candidate keys, so that a determinant is not a candidate key even though every non-key attribute is fine."),
        EX("Worked example 3: a 3NF table that is not in BCNF", intro="A school records extra lessons in TUTORING(Student, Subject, Teacher). Each student has one teacher per subject, and each teacher teaches only one subject. Is the relation in BCNF?", steps=[
            S("List the dependencies", text="(Student, Subject) → Teacher, and Teacher → Subject."),
            S("Find the candidate keys", text="(Student, Subject) and (Student, Teacher) are both candidate keys. Every attribute is part of some key, so there are no non-key attributes and the relation is in 3NF."),
            S("Apply the BCNF test", text="The determinant Teacher is not a candidate key on its own, so the relation is not in BCNF. If a teacher changes subject, many rows must change."),
            S("Decompose", text="TEACHES(Teacher KEY, Subject) and TUTORED(Student KEY, Teacher KEY). Every determinant is now a candidate key, so both relations are in BCNF."),
        ]),
        MISTAKE("Stopping at 1NF with the wrong key", "After removing a repeating group, the key usually becomes composite. Keeping OrderNo alone as the key is wrong, because OrderNo no longer identifies a single row."),
        MISTAKE("Losing the link between tables", "When a table is split, the determinant must stay behind as a foreign key. If CustID is not kept in ORDER, you can no longer tell who placed an order."),
        MISTAKE("Treating calculated values as stored data", "A column like LineTotal = Price × Qty should normally not be stored at all, because it can be calculated and may become inconsistent."),
        QUIZ("A relation in 2NF still has the dependencies StudentID → ClassID and ClassID → ClassTeacher, with StudentID as the key. What is wrong with it?",
             ["It has a transitive dependency, so it is not in 3NF", "It has a partial dependency, so it is not in 2NF", "It has a repeating group, so it is not in 1NF", "Nothing: it is in BCNF"], 0,
             "ClassTeacher depends on the key only through the non-key attribute ClassID. That is a transitive dependency, which 3NF removes.",
             feedback=["", "The key StudentID is a single attribute, so there cannot be a partial dependency.", "Nothing suggests multi-valued attributes.", "ClassID is a determinant but not a candidate key, so it is not in BCNF."]),
        QUIZ("A relation is in 1NF and its primary key is a single attribute. Which statement must be true?",
             ["It is in 2NF", "It is in 3NF", "It is in BCNF", "It has no functional dependencies"], 0,
             "A partial dependency needs a composite key. With a single-attribute key, 1NF implies 2NF.",
             feedback=["", "It may still contain a transitive dependency.", "It may still contain a determinant that is not a key.", "The key itself determines every other attribute."]),
        H("Practice questions"),
        PQ("Define (a) a partial dependency (b) a transitive dependency, giving an example of each from a school database.",
           "(a) A non-key attribute that depends on only part of a composite key. In ENTRY(StudentID, SubjectCode, StudentName, Grade), StudentName depends on StudentID alone. (b) A non-key attribute that depends on another non-key attribute. In STUDENT(StudentID, ClassID, ClassTeacher), ClassTeacher depends on ClassID, which depends on StudentID."),
        PQ("Normalize RESULT(StudentID, StudentName, SubjectCode, SubjectName, TeacherID, TeacherName, Grade) to 3NF. Assume each subject has exactly one teacher and the key is (StudentID, SubjectCode).",
           "Partial dependencies: StudentID → StudentName; SubjectCode → SubjectName, TeacherID, TeacherName. 2NF: STUDENT(StudentID, StudentName); SUBJECT(SubjectCode, SubjectName, TeacherID, TeacherName); RESULT(StudentID, SubjectCode, Grade). In SUBJECT, TeacherID → TeacherName is transitive. 3NF: TEACHER(TeacherID, TeacherName); SUBJECT(SubjectCode, SubjectName, TeacherID); STUDENT and RESULT unchanged."),
        PQ("Give two advantages and one disadvantage of normalizing a database to 3NF.",
           "Advantages: each fact is stored once, which saves space and removes update anomalies; data can be inserted and deleted without losing unrelated facts. Disadvantage: queries need more joins, which can make them slower and harder to write."),
        SUM("A → B means each value of A determines exactly one value of B.",
            "1NF: atomic values, no repeating groups, a key identified.",
            "2NF: remove partial dependencies on part of a composite key.",
            "3NF: remove transitive dependencies between non-key attributes.",
            "BCNF: every determinant must be a candidate key.",
            "Keep the determinant as a foreign key when you split a table."),
    ],
))

# ---------------------------------------------------------------------------
# Relational Databases / SQL
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="SQL",
    title="SQL: DDL, DML, joins and nested subqueries",
    slug="sql-ddl-dml-joins-subqueries",
    minutes=30,
    summary="Create tables with keys and constraints, insert, update and delete data, and write SELECT queries with joins, grouping and nested subqueries on a school results database.",
    objectives=[
        "Write DDL statements to create, alter and drop tables with primary and foreign keys",
        "Write DML statements to insert, update, delete and select data",
        "Join two or more tables with INNER JOIN and LEFT JOIN",
        "Use aggregate functions with GROUP BY and HAVING, and write nested subqueries",
    ],
    key_concepts=["DDL", "DML", "Primary key", "Foreign key", "INNER JOIN", "LEFT JOIN", "GROUP BY", "Subquery"],
    blocks=[
        H("Introduction"),
        T("In the last lesson we designed a school results database in 3NF. **SQL** (Structured Query Language) is the language used to build that database and ask it questions, such as \"Which Upper Sixth students scored above the average?\" SQL statements fall into two main groups."),
        KEY("Two parts of SQL", "Both are written as statements ending with a semicolon.", cards=[
            ["DDL: Data Definition Language", "Defines the structure: CREATE TABLE, ALTER TABLE, DROP TABLE. Sets keys and constraints."],
            ["DML: Data Manipulation Language", "Works with the data: INSERT, UPDATE, DELETE and SELECT."],
        ]),
        H("DDL: creating the tables"),
        CODE('''
CREATE TABLE Student (
    StudentID  CHAR(4)      PRIMARY KEY,
    Name       VARCHAR(30)  NOT NULL,
    Class      CHAR(2)      NOT NULL,
    Town       VARCHAR(20)
);

CREATE TABLE Subject (
    SubjectCode  CHAR(3)      PRIMARY KEY,
    Title        VARCHAR(30)  NOT NULL
);

CREATE TABLE Result (
    StudentID    CHAR(4),
    SubjectCode  CHAR(3),
    Mark         INTEGER CHECK (Mark BETWEEN 0 AND 100),
    PRIMARY KEY (StudentID, SubjectCode),
    FOREIGN KEY (StudentID)   REFERENCES Student(StudentID),
    FOREIGN KEY (SubjectCode) REFERENCES Subject(SubjectCode)
);

ALTER TABLE Student ADD Phone VARCHAR(15);
''', "sql", title="Listing 1: DDL for the school database"),
        D("A **foreign key** is an attribute in one table that refers to the primary key of another table. The DBMS enforces **referential integrity**: a Result row cannot refer to a student who does not exist.", title="Foreign key"),
        H("DML: changing the data"),
        CODE('''
INSERT INTO Student VALUES ('S1', 'Abena', 'L6', 'Buea', NULL);
INSERT INTO Result (StudentID, SubjectCode, Mark) VALUES ('S1', 'MAT', 72);

UPDATE Result SET Mark = Mark + 5 WHERE SubjectCode = 'PHY';

DELETE FROM Result WHERE Mark IS NULL;
''', "sql", title="Listing 2: INSERT, UPDATE and DELETE"),
        MISTAKE("UPDATE or DELETE without WHERE", "DELETE FROM Result; removes every row in the table. Always check the WHERE clause before running UPDATE or DELETE."),
        CODE('''
Student                              Subject                   Result
StudentID Name   Class Town          SubjectCode Title         StudentID SubjectCode Mark
S1        Abena  L6    Buea          MAT  Mathematics          S1        MAT         72
S2        Bih    U6    Bamenda       CSC  Computer Science     S1        CSC         65
S3        Nkeng  U6    Buea          PHY  Physics              S2        MAT         48
S4        Tchoua L6    Dschang                                 S3        CSC         81
S5        Manga  U6    Kribi                                   S3        MAT         77
                                                               S4        PHY         55
''', "text", title="Table 1: sample data used in the queries"),
        H("Joins"),
        EX("Worked example 1: a three-table INNER JOIN", intro="List the name, subject title and mark of every Upper Sixth student who has a result, highest mark first.", steps=[
            S("Choose the tables", text="Name is in Student, Title is in Subject, Mark is in Result. Result links the other two."),
            S("Write the joins", text="FROM Student S INNER JOIN Result R ON S.StudentID = R.StudentID INNER JOIN Subject J ON R.SubjectCode = J.SubjectCode."),
            S("Filter and sort", text="WHERE S.Class = 'U6' ORDER BY R.Mark DESC."),
            S("Result", text="Nkeng, Computer Science, 81; Nkeng, Mathematics, 77; Bih, Mathematics, 48. Manga is in U6 but has no result, so an inner join leaves Manga out."),
        ]),
        CODE('''
SELECT S.Name, J.Title, R.Mark
FROM Student S
INNER JOIN Result R  ON S.StudentID   = R.StudentID
INNER JOIN Subject J ON R.SubjectCode = J.SubjectCode
WHERE S.Class = 'U6'
ORDER BY R.Mark DESC;

-- LEFT JOIN keeps every student, even without a Maths mark
SELECT S.Name, R.Mark
FROM Student S
LEFT JOIN Result R ON S.StudentID = R.StudentID AND R.SubjectCode = 'MAT';
''', "sql", title="Listing 3: inner and left joins"),
        T("The LEFT JOIN in Listing 3 returns all five students: Abena 72, Bih 48, Nkeng 77, and NULL for Tchoua and Manga, who have no Maths mark. Use a LEFT JOIN when rows without a match must still appear."),
        H("Grouping and nested subqueries"),
        T("**Aggregate functions** (COUNT, SUM, AVG, MAX, MIN) summarise many rows. **GROUP BY** makes one group per value, and **HAVING** filters groups after they are formed, while WHERE filters rows before grouping. A **subquery** is a SELECT inside another statement; the inner query runs first and its result is used by the outer query."),
        EX("Worked example 2: subqueries", intro="(a) Find the results above the overall average mark. (b) Find students with no result at all.", steps=[
            S("Inner query for (a)", text="SELECT AVG(Mark) FROM Result gives (72 + 65 + 48 + 81 + 77 + 55) / 6 = 398 / 6, about 66.3."),
            S("Outer query for (a)", text="Keep rows with Mark > 66.3: Abena MAT 72, Nkeng CSC 81, Nkeng MAT 77."),
            S("Inner query for (b)", text="SELECT StudentID FROM Result gives S1, S2, S3, S4 (with repeats)."),
            S("Outer query for (b)", text="Students whose StudentID is NOT IN that list: Manga."),
        ]),
        CODE('''
SELECT S.Name, R.SubjectCode, R.Mark
FROM Student S JOIN Result R ON S.StudentID = R.StudentID
WHERE R.Mark > (SELECT AVG(Mark) FROM Result);

SELECT Name FROM Student
WHERE StudentID NOT IN (SELECT StudentID FROM Result);

SELECT SubjectCode, COUNT(*) AS Entries, AVG(Mark) AS Average
FROM Result
GROUP BY SubjectCode
HAVING COUNT(*) >= 2;
''', "sql", title="Listing 4: subqueries and grouping"),
        T("The last query in Listing 4 returns CSC with 2 entries and average 73, and MAT with 3 entries and average about 65.7. PHY has only 1 entry, so HAVING removes it."),
        MISTAKE("Using WHERE with an aggregate", "WHERE AVG(Mark) > 60 is an error, because WHERE works on single rows before grouping. Use HAVING AVG(Mark) > 60 after GROUP BY."),
        MISTAKE("Ambiguous column names", "StudentID exists in both Student and Result. In a join, write S.StudentID or R.StudentID, otherwise the query fails."),
        QUIZ("Which statement is part of the Data Definition Language?",
             ["ALTER TABLE", "INSERT INTO", "UPDATE", "SELECT"], 0,
             "ALTER TABLE changes the structure of a table, so it is DDL.",
             feedback=["", "INSERT adds data rows: DML.", "UPDATE changes data values: DML.", "SELECT retrieves data: DML."]),
        QUIZ("Using Table 1, how many rows does SELECT S.Name FROM Student S INNER JOIN Result R ON S.StudentID = R.StudentID return?",
             ["6", "5", "4", "30"], 0,
             "An inner join gives one row per matching pair. Every one of the 6 Result rows matches a student, so 6 rows are returned (Abena and Nkeng appear twice).",
             feedback=["", "That is the number of students; S1 and S3 each match two results, and S5 matches none.", "That is the number of different students who have results.", "That would be the Cartesian product of 5 students and 6 results."]),
        H("Practice questions"),
        PQ("Write an SQL statement to create a table Teacher with TeacherID (4 characters, primary key), Name (up to 30 characters, required) and Salary (whole number in FCFA, must be positive).",
           "CREATE TABLE Teacher ( TeacherID CHAR(4) PRIMARY KEY, Name VARCHAR(30) NOT NULL, Salary INTEGER CHECK (Salary > 0) );"),
        PQ("Using Table 1, write a query to show the name of every student who takes Computer Science, using a nested subquery, and give its output.",
           "SELECT Name FROM Student WHERE StudentID IN (SELECT StudentID FROM Result WHERE SubjectCode = 'CSC'); The subquery returns S1 and S3, so the output is Abena and Nkeng."),
        PQ("Write a query to count the number of students from each town, and give its output for Table 1.",
           "SELECT Town, COUNT(StudentID) AS Total FROM Student GROUP BY Town; Output: Bamenda 1, Buea 2, Dschang 1, Kribi 1 (the order of groups may vary unless ORDER BY Town is added)."),
        PQ("Explain what happens if the statement INSERT INTO Result VALUES ('S9', 'MAT', 50); is run, and why.",
           "It is rejected. StudentID is a foreign key that references Student, and there is no student S9. The DBMS enforces referential integrity and refuses to create a result for a student who does not exist."),
        SUM("DDL (CREATE, ALTER, DROP) defines structure; DML (INSERT, UPDATE, DELETE, SELECT) handles data.",
            "Primary keys identify rows; foreign keys enforce referential integrity.",
            "INNER JOIN keeps matching rows only; LEFT JOIN keeps every row of the left table.",
            "WHERE filters rows before grouping; HAVING filters groups after GROUP BY.",
            "A subquery runs first and passes its result to the outer query."),
    ],
))

# ---------------------------------------------------------------------------
# Object-Oriented Programming / OOP principles
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Object-Oriented Programming",
    topic="OOP principles",
    title="The four principles of object-oriented programming",
    slug="oop-principles",
    minutes=25,
    summary="Understand classes and objects and the four OOP principles of abstraction, encapsulation, inheritance and polymorphism, with Python and Java examples from a market stock system and a school payroll.",
    objectives=[
        "Distinguish between a class and an object",
        "Explain abstraction, encapsulation, inheritance and polymorphism with examples",
        "Write a class with private attributes and public methods",
        "Use inheritance and method overriding to achieve polymorphism",
    ],
    key_concepts=["Class", "Object", "Attribute", "Method", "Abstraction", "Encapsulation", "Inheritance", "Polymorphism", "Overriding", "Overloading"],
    blocks=[
        H("Introduction"),
        T("A shop at Marché Central in Douala sells hundreds of items: rice, palm oil, phone credit, soap. In a procedural program the data (names, prices, quantities) and the code that changes it are kept apart, and any part of the program can change a quantity by mistake.\n\n"
          "**Object-oriented programming** (OOP) groups data and the code that acts on it into **objects**. Large programs become easier to build, test and maintain."),
        D("A **class** is a blueprint that defines the attributes (data) and methods (behaviour) shared by a type of object. An **object** is one instance of a class, with its own attribute values.",
          title="Class and object", note="StockItem is a class. The object rice, with name \"Rice 50 kg\", price 22000 and quantity 10, is an instance of it."),
        KEY("The four principles", "Examiners often ask you to define each one and give an example.", cards=[
            ["Abstraction", "Show only the essential features and hide unnecessary detail. A Staff class says every staff member can be paid, without saying how."],
            ["Encapsulation", "Bundle data with its methods and hide the data (make it private), so it can only be changed through methods that check it."],
            ["Inheritance", "A subclass gets the attributes and methods of a superclass and can add or change them. This is an \"is a\" relationship."],
            ["Polymorphism", "The same method call behaves differently depending on the class of the object. pay() works differently for full-time and part-time teachers."],
        ]),
        H("Encapsulation"),
        EX("Worked example 1: an encapsulated stock item", intro="Design a StockItem class in which the price and quantity cannot be changed directly, and a sale is refused if there is not enough stock. Trace rice = StockItem(\"Rice 50 kg\", 22000, 10), then rice.sell(3).", steps=[
            S("Make the data private", text="In Python, a name starting with two underscores (such as __quantity) is hidden from outside code. Trying to read rice.__quantity raises an AttributeError."),
            S("Provide public methods", text="get_quantity() reads the quantity; sell(n) and restock(n) change it, but only after checking that n is valid."),
            S("Trace the constructor", text="The object stores name = Rice 50 kg, price = 22000, quantity = 10."),
            S("Trace rice.sell(3)", text="3 is positive and not more than 10, so quantity becomes 7 and the method returns 3 × 22000 = 66000 FCFA."),
        ]),
        CODE('''
class StockItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price          # private attribute
        self.__quantity = quantity    # private attribute

    def get_quantity(self):           # getter
        return self.__quantity

    def sell(self, n):
        if n <= 0 or n > self.__quantity:
            raise ValueError("invalid quantity")
        self.__quantity -= n
        return n * self.__price       # amount to pay in FCFA

    def restock(self, n):
        if n <= 0:
            raise ValueError("invalid quantity")
        self.__quantity += n


rice = StockItem("Rice 50 kg", 22000, 10)
print(rice.sell(3))           # 66000
print(rice.get_quantity())    # 7
''', "python", title="Listing 1: encapsulation in Python"),
        TIP("Encapsulation protects data integrity: because every change goes through sell or restock, the quantity can never become negative."),
        H("Inheritance, abstraction and polymorphism"),
        EX("Worked example 2: a school payroll", intro="A school pays full-time teachers a fixed monthly salary and part-time teachers by the hour. Design classes so that one loop can pay everyone, then trace the output for Mr Atangana (salary 250 000 FCFA) and Mrs Eyong (40 hours at 3500 FCFA).", steps=[
            S("Abstraction", text="Create an abstract superclass Staff with a name attribute and an abstract method pay(). Staff itself cannot be instantiated."),
            S("Inheritance", text="FullTimeTeacher and PartTimeTeacher inherit from Staff. Each constructor calls super().__init__(name) to set the inherited name."),
            S("Overriding", text="Each subclass overrides pay(): FullTimeTeacher returns its salary; PartTimeTeacher returns hours × rate."),
            S("Polymorphism in the loop", text="for s in staff: print(s.name, s.pay()) calls the correct pay() for each object."),
            S("Output", text="Mr Atangana 250000, then Mrs Eyong 140000 (because 40 × 3500 = 140 000)."),
        ]),
        CODE('''
from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def pay(self):
        pass

class FullTimeTeacher(Staff):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def pay(self):
        return self.salary

class PartTimeTeacher(Staff):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate

staff = [FullTimeTeacher("Mr Atangana", 250000),
         PartTimeTeacher("Mrs Eyong", 40, 3500)]
for s in staff:
    print(s.name, s.pay())
''', "python", title="Listing 2: inheritance and polymorphism in Python"),
        T("Adding a new kind of staff, such as a Bursar paid a salary plus an allowance, needs only a new subclass with its own pay(). The loop does not change. This is the main practical benefit of polymorphism."),
        H("Overriding and overloading"),
        T("**Overriding** happens when a subclass gives a new version of a method with the same name and parameters as in its superclass; the version used is chosen at run time from the object's class. **Overloading** means several methods in the same class share a name but have different parameter lists; the version is chosen at compile time from the arguments. Java supports both. Python does not support overloading in the same way, but default parameter values give a similar effect."),
        CODE('''
class Shape {
    double area() { return 0; }
}

class Rectangle extends Shape {
    double w, h;
    Rectangle(double w, double h) { this.w = w; this.h = h; }
    @Override
    double area() { return w * h; }             // overriding
}

class Calculator {
    int add(int a, int b)          { return a + b; }       // overloading:
    int add(int a, int b, int c)   { return a + b + c; }   // same name,
    double add(double a, double b) { return a + b; }       // different parameters
}
''', "java", title="Listing 3: overriding and overloading in Java"),
        MISTAKE("Confusing encapsulation with abstraction", "Encapsulation is about hiding data inside an object and controlling access to it. Abstraction is about hiding complexity by showing only what is essential. A private attribute is encapsulation; an abstract method is abstraction."),
        MISTAKE("Using inheritance for a \"has a\" relationship", "A Classroom has a Teacher, but a Classroom is not a Teacher, so Classroom must not inherit from Teacher. Use an attribute (composition) instead."),
        QUIZ("A program stores a list of Staff objects and calls pay() on each one. Each subclass gives a different result. Which principle does this show most directly?",
             ["Polymorphism", "Encapsulation", "Overloading", "Abstraction"], 0,
             "The same call, pay(), behaves differently depending on the object's class: that is polymorphism.",
             feedback=["", "Encapsulation is about hiding data, not about the same call behaving differently.", "Overloading uses different parameter lists in one class; here the method is overridden in subclasses.", "Abstraction is shown by the abstract Staff class, but the different behaviour is polymorphism."]),
        QUIZ("In Python, what happens when outside code runs print(rice.__quantity) for the class in Listing 1?",
             ["An AttributeError is raised", "It prints 7", "It prints None", "It prints 0"], 0,
             "Names starting with two underscores are name-mangled inside the class, so outside code cannot reach them by that name.",
             feedback=["", "The attribute is private; use rice.get_quantity() to read it.", "No new attribute is created when reading.", "There is no default value of 0."]),
        H("Practice questions"),
        PQ("Explain the difference between a class and an object, using a school example.",
           "A class is a template that defines the attributes and methods of a type of thing; an object is a single instance created from it with its own values. Student is a class with attributes name and class and a method enrol(); the student Ngono in U6 is an object of that class."),
        PQ("State two advantages of inheritance in a large program.",
           "Code is reused: common attributes and methods are written once in the superclass, so there is less code to write and test. Maintenance is easier: a correction made in the superclass applies automatically to every subclass. It also models real \"is a\" relationships clearly."),
        PQ("A Vehicle class has a method fare(distance). Taxi and Bus are subclasses. A taxi charges 300 FCFA per km and a bus charges a flat 500 FCFA. (a) Which principle allows one call v.fare(10) to work for both? (b) Give the result for each.",
           "(a) Polymorphism through method overriding: each subclass overrides fare. (b) Taxi: 10 × 300 = 3000 FCFA. Bus: 500 FCFA, whatever the distance."),
        PQ("Why should the quantity attribute of a StockItem be private? What should be provided instead?",
           "If it were public, any code could set it to a negative or impossible value, breaking data integrity. It should be private, with public methods such as get_quantity(), sell(n) and restock(n) that validate every change."),
        SUM("A class is a blueprint; an object is an instance with its own attribute values.",
            "Abstraction hides unnecessary detail; encapsulation hides data behind methods.",
            "Inheritance lets a subclass reuse and extend a superclass (an \"is a\" relationship).",
            "Polymorphism lets one method call behave differently for different classes.",
            "Overriding replaces a superclass method; overloading reuses a name with different parameters."),
    ],
))

# ---------------------------------------------------------------------------
# Object-Oriented Programming / Classes in practice
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Object-Oriented Programming",
    topic="Classes in practice",
    title="UML class diagrams, access modifiers, constructors, destructors and exceptions",
    slug="classes-in-practice-uml-constructors-exceptions",
    minutes=30,
    summary="Draw and read UML class diagrams, use public, private and protected access, write constructors and destructors, and handle errors with exceptions, using a school fees system.",
    objectives=[
        "Draw a UML class diagram showing attributes, methods, visibility, inheritance and associations",
        "Explain public, private and protected access modifiers",
        "Write constructors and explain when destructors run",
        "Throw and handle exceptions with try, catch and finally",
    ],
    key_concepts=["UML class diagram", "Visibility", "Access modifier", "Constructor", "Destructor", "Exception", "try-catch-finally", "Association", "Multiplicity"],
    blocks=[
        H("Introduction"),
        T("A school in Limbe wants software to track fees paid by each student. Before coding, the developer draws a **UML class diagram** to agree the design with the bursar. Then the classes are written with careful access control, constructors that set up valid objects, and exceptions that deal with bad input, such as a payment larger than the amount owed."),
        D("A **UML class diagram** shows each class as a box with three parts: the class name, the attributes, and the methods. Lines between boxes show relationships such as inheritance and association.", title="UML class diagram"),
        KEY("Visibility symbols and access modifiers", "The symbol before a member in UML matches the access modifier in code.", cards=[
            ["+ public", "Accessible from any class."],
            ["- private", "Accessible only inside the class itself. Normal for attributes."],
            ["# protected", "Accessible inside the class and its subclasses (in Java, also within the same package)."],
        ]),
        IMG("cs-uml-feeaccount.svg",
            "UML class box FeeAccount. Attributes: private studentId : String, private balance : Integer. Methods: public FeeAccount(studentId : String, fees : Integer), public pay(amount : Integer) : void, public getBalance() : Integer.",
            caption="Figure 1. The FeeAccount class in UML."),
        EX("Worked example 1: drawing a class hierarchy", intro="Every person in the school has a name and a phone number. A student also has a class and a fee account; a teacher also has a staff number and teaches several classes. Draw the class diagram.", steps=[
            S("Find the superclass", text="Person holds what is common: - name : String, - phone : String, + getName() : String."),
            S("Find the subclasses", text="Student adds - form : String; Teacher adds - staffNo : String. Both inherit from Person."),
            S("Show inheritance", text="Draw a line from each subclass to Person ending in a hollow triangle pointing at Person."),
            S("Show associations with multiplicity", text="Each Student has exactly 1 FeeAccount (1 to 1). A Teacher teaches one or more (1..many) SchoolClass objects, and each SchoolClass has 1 class teacher."),
        ]),
        IMG("cs-uml-person-hierarchy.svg",
            "Person (private name, phone; public getName() : String) is the superclass of Student (private form) and Teacher (private staffNo), shown by a hollow triangle. Each Student owns 1 FeeAccount. Each Teacher teaches 1..* SchoolClass objects.",
            caption="Figure 2. The class diagram from worked example 1."),
        H("Constructors and destructors"),
        D("A **constructor** is a special method that runs automatically when an object is created. It has the same name as the class in Java and C++ (__init__ in Python) and sets the initial attribute values. A **destructor** runs when an object is destroyed and releases resources such as files or memory.",
          title="Constructor and destructor", note="C++ has explicit destructors (~ClassName). Java and Python free memory automatically with a garbage collector, so destructors are rarely written there."),
        EX("Worked example 2: tracing constructors and destructors in C++", intro="Give the output of the C++ program in Listing 1.", steps=[
            S("Object a is created", text="Its constructor prints Open A."),
            S("The inner block starts", text="Object b is created: Open B. When the closing brace is reached, b goes out of scope and its destructor prints Close B."),
            S("Object c is created", text="Open C."),
            S("main ends", text="Local objects are destroyed in reverse order of creation: Close C, then Close A."),
            S("Full output", text="Open A, Open B, Close B, Open C, Close C, Close A (one per line)."),
        ]),
        CODE('''
#include <iostream>
#include <string>
using namespace std;

class Logger {
    string name;
public:
    Logger(string n) : name(n) { cout << "Open " << name << endl; }
    ~Logger()                  { cout << "Close " << name << endl; }
};

int main() {
    Logger a("A");
    {
        Logger b("B");
    }                  // b is destroyed here
    Logger c("C");
    return 0;          // c, then a, are destroyed here
}
''', "cpp", title="Listing 1: constructor and destructor order"),
        H("Exceptions"),
        T("An **exception** is an object that signals an error at run time, such as dividing by zero, opening a missing file or receiving an invalid payment. A method **throws** an exception; the calling code **catches** it in a try block and handles it, instead of letting the program crash. Code in a **finally** block runs whether or not an exception occurred, so it is used for clean-up."),
        EX("Worked example 3: throwing and catching an exception in Java", intro="A student owes 75 000 FCFA. Trace the main method in Listing 2, which pays 50 000 FCFA and then 30 000 FCFA.", steps=[
            S("Constructor", text="fees = 75000 is not negative, so balance = 75000."),
            S("acc.pay(50000)", text="50000 is positive and not more than 75000, so balance = 25000."),
            S("acc.pay(30000)", text="30000 > 25000, so pay throws an IllegalArgumentException. The rest of the try block, including Paid in full, is skipped."),
            S("catch and finally", text="The catch block prints Error: invalid payment: 30000. The finally block then prints Balance: 25000."),
        ]),
        CODE('''
public class FeeAccount {
    private String studentId;
    private int balance;                      // fees still owed, in FCFA

    public FeeAccount(String studentId, int fees) {
        if (fees < 0) {
            throw new IllegalArgumentException("fees cannot be negative");
        }
        this.studentId = studentId;
        this.balance = fees;
    }

    public void pay(int amount) {
        if (amount <= 0 || amount > balance) {
            throw new IllegalArgumentException("invalid payment: " + amount);
        }
        balance -= amount;
    }

    public int getBalance() { return balance; }

    public static void main(String[] args) {
        FeeAccount acc = new FeeAccount("U6-014", 75000);
        try {
            acc.pay(50000);
            acc.pay(30000);
            System.out.println("Paid in full");
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Balance: " + acc.getBalance());
        }
    }
}
''', "java", title="Listing 2: the FeeAccount class with exceptions"),
        MISTAKE("Making every attribute public", "Public attributes let any code set balance to a negative number. Make attributes private (-) and give public (+) methods that check the values."),
        MISTAKE("Giving a constructor a return type", "In Java and C++, a constructor has no return type, not even void. Writing public void FeeAccount(...) creates an ordinary method, and the constructor is never called."),
        MISTAKE("Catching an exception and doing nothing", "An empty catch block hides the error, so the program continues with wrong data. At least report the error or take a sensible recovery action."),
        QUIZ("In a UML class diagram, what does # before an attribute mean?",
             ["Protected", "Private", "Public", "Static"], 0,
             "# means protected: visible in the class and its subclasses.",
             feedback=["", "Private is shown with a minus sign.", "Public is shown with a plus sign.", "Static members are shown underlined."]),
        QUIZ("In Listing 2, which line is never printed?",
             ["Paid in full", "Error: invalid payment: 30000", "Balance: 25000", "All three lines are printed"], 0,
             "The exception from acc.pay(30000) jumps straight to the catch block, so the next line in the try block is skipped.",
             feedback=["", "The catch block runs because an exception was thrown.", "The finally block always runs.", "The exception skips the rest of the try block."]),
        H("Practice questions"),
        PQ("Draw a UML class box for a class Product with private attributes code (String), price (Integer) and quantity (Integer), a public constructor taking all three, and public methods sell(n : Integer) : Integer and getQuantity() : Integer.",
           "Top section: Product. Middle section: - code : String, - price : Integer, - quantity : Integer. Bottom section: + Product(code : String, price : Integer, quantity : Integer), + sell(n : Integer) : Integer, + getQuantity() : Integer."),
        PQ("State the difference between a constructor and a destructor, and explain why Java programmers rarely write destructors.",
           "A constructor runs when an object is created and initialises its attributes; a destructor runs when the object is destroyed and releases its resources. Java uses a garbage collector that frees unused memory automatically, so there is usually no need to write a destructor; other resources are closed explicitly, for example in a finally block."),
        PQ("Rewrite this Python function so that it handles a non-numeric input with an exception: def read_mark(text): return int(text).",
           "def read_mark(text): then, inside, try: mark = int(text), except ValueError: print(\"Mark must be a whole number\") and return None, else: return mark. Converting a string such as \"abc\" with int raises ValueError, which is now caught instead of stopping the program."),
        PQ("Explain why the attributes of FeeAccount are private while its methods are public.",
           "Private attributes enforce encapsulation: outside code cannot set balance to an invalid value directly. The public methods form the class interface and check every change, for example pay refuses amounts that are negative or greater than the balance."),
        SUM("A UML class box has three parts: name, attributes and methods; + public, - private, # protected.",
            "A hollow triangle shows inheritance; numbers such as 1 and 1..many show multiplicity.",
            "A constructor initialises a new object and has no return type.",
            "C++ destructors run when an object goes out of scope, in reverse order of creation.",
            "Throw an exception for an error; handle it with try and catch; use finally for clean-up."),
    ],
))

# ---------------------------------------------------------------------------
# Software Project / Individual project
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Software Project",
    topic="Individual project",
    title="Planning, building, testing and reporting your individual project",
    slug="individual-software-project-guide",
    minutes=30,
    summary="A practical guide to the stages of an individual software project: choosing a problem, analysis, design, coding, unit and integration testing, evaluation and writing the technical report.",
    objectives=[
        "Choose a realistic project with a real user and write measurable objectives",
        "Plan the analysis, design, implementation, testing and evaluation stages",
        "Write a test plan using normal, boundary and erroneous data, and write unit and integration tests",
        "Structure a clear technical report",
    ],
    key_concepts=["Requirements", "SMART objectives", "Design", "Implementation", "Unit testing", "Integration testing", "Test plan", "Boundary data", "Technical report", "Evaluation"],
    blocks=[
        H("Introduction"),
        T("The individual project is your chance to solve a real problem with software from start to finish. Good projects come from real users close to you: a provision store in Nkongsamba that loses track of stock, a njangi group whose secretary records contributions in an exercise book, or a school library that cannot tell which books are overdue.\n\n"
          "This lesson is a practical guide to the stages and the report. It is not the official marking scheme. Always check the current GCE Board regulations and your teacher's instructions for deadlines, length and what must be submitted."),
        KEY("The stages of a software project", "Most projects follow these stages in order, returning to earlier ones when problems appear.", cards=[
            ["1. Analysis", "Understand the current system and the user's needs. Interview the user, collect sample documents, and write measurable objectives."],
            ["2. Design", "Plan data structures and database tables, class or structure diagrams, algorithms in pseudocode, screen layouts and the test plan."],
            ["3. Implementation", "Write the code in small, tested pieces, with meaningful names, comments and regular backups or version control."],
            ["4. Testing", "Unit test each module, integration test modules together, then test the whole system with the user."],
            ["5. Evaluation", "Compare the finished system with each objective, collect user feedback, and describe limitations and improvements."],
        ]),
        H("Choosing a project and writing objectives"),
        TIP("Choose a problem that is big enough to need a database or several modules, but small enough to finish. A system with 3 to 5 main features, done well, is better than 15 features half finished. Make sure the user will be available to answer questions and test your system."),
        EX("Worked example 1: turning a vague idea into measurable objectives", intro="A student wants to build \"a system for the njangi group\". Turn this into objectives that can be tested at the end.", steps=[
            S("Interview the user", text="The secretary explains: 20 members each contribute every month; she must know who has paid, who owes, and who receives the pot each month."),
            S("Avoid vague objectives", text="\"The system should be easy to use\" cannot be tested. Ask: what exactly must it do, and how will we know?"),
            S("Write specific objectives", text="1. Store each member's ID, name and phone number. 2. Record a contribution of 1000 to 50 000 FCFA with the date. 3. List the members who have not paid in a chosen month."),
            S("Add measurable targets", text="4. Show the total collected for a month. 5. The secretary can record a payment in under one minute after a short demonstration."),
            S("Link to testing", text="Each objective will have at least one test in the test plan, and the evaluation will discuss each one in turn."),
        ]),
        H("Design"),
        T("Your design should let another programmer build the system without asking you questions. For a database project, show normalized tables with keys (for example MEMBER, CONTRIBUTION and PAYOUT). For an object-oriented project, include a UML class diagram. Write the main algorithms in pseudocode, sketch every screen or menu, and describe how data will be validated."),
        CODE('''
MEMBER(MemberID, Name, Phone)                       key: MemberID
CONTRIBUTION(MemberID, Month, Amount, DatePaid)     key: (MemberID, Month)
                                                    MemberID -> MEMBER
PAYOUT(Month, MemberID, Total)                      key: Month
                                                    MemberID -> MEMBER

Validation: Amount is a whole number from 1000 to 50000
            Month is in the form YYYY-MM
''', "text", title="Figure 1: part of a design for the njangi system"),
        H("Testing"),
        D("**Unit testing** checks one module (a function, method or class) on its own. **Integration testing** checks that modules work correctly together, for example that the payment screen saves to the database and the report then shows the new total. **System** and **acceptance testing** check the whole program, the last with the real user.",
          title="Levels of testing"),
        KEY("Choosing test data", "For each input, test all three kinds of data.", cards=[
            ["Normal", "Typical valid data that should be accepted, such as 10 000 FCFA."],
            ["Boundary", "Values at the edges of the valid range and just outside: 1000 and 50 000 (accepted), 999 and 50 001 (rejected)."],
            ["Erroneous", "Data of the wrong type or clearly invalid, which should be rejected with a clear message: \"ten thousand\" or -500."],
        ]),
        EX("Worked example 2: a test plan for one input", intro="Write test plan rows for the contribution amount, which must be a whole number from 1000 to 50 000 FCFA.", steps=[
            S("Columns of the plan", text="Test number, purpose, test data, type of data, expected result, actual result, and evidence (screenshot reference)."),
            S("Normal and boundary rows", text="10000 (normal, accept); 1000 and 50000 (boundary, accept); 999 and 50001 (boundary, reject)."),
            S("Erroneous rows", text="\"ten thousand\" and -500 (erroneous, reject with the message \"Enter a whole number from 1000 to 50000\")."),
            S("Run and record", text="Fill in the actual result after running each test. If it differs from the expected result, fix the code, re-run the test and record both runs as evidence."),
        ]),
        CODE('''
No  Purpose                   Data            Type        Expected           Actual
1   Accept a typical amount   10000           Normal      Accepted           Accepted
2   Lowest valid amount       1000            Boundary    Accepted           Accepted
3   Just below the minimum    999             Boundary    Error message      Error message
4   Highest valid amount      50000           Boundary    Accepted           Accepted
5   Just above the maximum    50001           Boundary    Error message      Error message
6   Text instead of a number  ten thousand    Erroneous   Error message      Error message
''', "text", title="Table 1: a test plan extract"),
        T("Automated tests save time, because they can be re-run after every change. Listing 1 uses Python's built-in unittest module: the first class unit tests the validation function, and the second integration tests the Ledger class together with that function."),
        CODE('''
import unittest

def valid_contribution(amount):
    """A monthly contribution must be a whole number from 1000 to 50000 FCFA."""
    return isinstance(amount, int) and 1000 <= amount <= 50000

class Ledger:
    def __init__(self):
        self.payments = {}

    def record(self, member_id, amount):
        if not valid_contribution(amount):
            raise ValueError("invalid amount")
        self.payments[member_id] = self.payments.get(member_id, 0) + amount

    def total(self):
        return sum(self.payments.values())

class TestValidContribution(unittest.TestCase):        # unit tests
    def test_normal(self):
        self.assertTrue(valid_contribution(10000))

    def test_boundaries(self):
        self.assertTrue(valid_contribution(1000))
        self.assertTrue(valid_contribution(50000))
        self.assertFalse(valid_contribution(999))
        self.assertFalse(valid_contribution(50001))

    def test_erroneous(self):
        self.assertFalse(valid_contribution("ten thousand"))
        self.assertFalse(valid_contribution(-500))

class TestLedger(unittest.TestCase):                    # integration tests
    def test_record_and_total(self):
        book = Ledger()
        book.record("M01", 10000)
        book.record("M02", 5000)
        book.record("M01", 2000)
        self.assertEqual(book.payments["M01"], 12000)
        self.assertEqual(book.total(), 17000)

    def test_invalid_amount_rejected(self):
        book = Ledger()
        with self.assertRaises(ValueError):
            book.record("M03", 500)
        self.assertEqual(book.total(), 0)

if __name__ == "__main__":
    unittest.main()        # runs all 5 tests
''', "python", title="Listing 1: unit and integration tests with unittest"),
        H("The technical report"),
        CODE('''
Title page and contents
1. Analysis       problem, user, current system, interview notes,
                  requirements and numbered objectives
2. Design         data design (tables or classes), diagrams,
                  pseudocode, screen designs, validation, test plan
3. Implementation key code with explanations, how problems were solved,
                  annotated screenshots of the working system
4. Testing        completed test plan with evidence for each test,
                  unit and integration test results, user testing
5. Evaluation     each objective met / partly met / not met with evidence,
                  user feedback, limitations, possible improvements
6. User guide     installing and using the system
Appendices        full code listing, interview records, references
''', "text", title="Figure 2: a sensible report structure"),
        MISTAKE("Writing the report at the end", "Students who write everything in the last week forget why they made decisions and lose evidence. Keep a log and write each section while you work on that stage."),
        MISTAKE("Testing only with normal data", "A test plan with only valid data shows nothing about validation. Include boundary and erroneous data for every input, and show screenshots of the results."),
        MISTAKE("Evaluating without evidence", "\"The system works well\" is not an evaluation. Go through each objective, refer to the tests that show it is met, and be honest about anything not finished."),
        QUIZ("A contribution must be from 1000 to 50 000 FCFA. Which value is boundary data that should be rejected?",
             ["50 001", "50 000", "25 000", "\"fifty\""], 0,
             "50 001 is just outside the upper limit, so it is boundary data that should be rejected.",
             feedback=["", "50 000 is boundary data, but it is valid and should be accepted.", "25 000 is normal data.", "Text is erroneous data, not boundary data."]),
        QUIZ("A student tests that the payment form saves to the database and that the monthly report then shows the new total. What kind of testing is this?",
             ["Integration testing", "Unit testing", "Boundary testing", "Dry run"], 0,
             "Two or more modules are being tested working together, which is integration testing.",
             feedback=["", "Unit testing checks one module on its own.", "Boundary testing is about choosing data at the edges of a range.", "A dry run is tracing code by hand, not running the system."]),
        H("Practice questions"),
        PQ("Explain the difference between unit testing and integration testing, with an example from a library system.",
           "Unit testing checks a single module in isolation, for example testing that the function that calculates an overdue fine returns the right value for 0, 1 and 10 days late. Integration testing checks that modules work together, for example that returning a book through the loans screen updates the database and removes it from the overdue report."),
        PQ("A field for a student's age must accept whole numbers from 15 to 21. Give two items of normal, boundary and erroneous test data, with expected results.",
           "Normal: 17 and 19, accepted. Boundary: 15 and 21 accepted; 14 and 22 rejected. Erroneous: \"seventeen\" and -3, rejected with an error message."),
        PQ("Rewrite the objective \"The system must be fast and user friendly\" as two measurable objectives.",
           "For example: 1. A search for a member by name returns results in under 2 seconds with 500 members stored. 2. After a 10-minute demonstration, the secretary can record a new payment without help in under one minute. Both can be checked in testing and discussed in the evaluation."),
        PQ("State what should be included in the evaluation section of a project report.",
           "A review of each objective stating whether it was fully, partly or not met, with reference to test evidence; feedback from the user; the limitations of the system; and realistic improvements or extensions for the future."),
        SUM("Pick a real problem with a real user, and write specific, measurable objectives.",
            "Follow the stages: analysis, design, implementation, testing, evaluation.",
            "Test every input with normal, boundary and erroneous data, and keep evidence.",
            "Unit tests check one module; integration tests check modules working together.",
            "Write the report as you go, and evaluate against each objective with evidence.",
            "Check the current official GCE Board regulations for exact submission requirements."),
    ],
))
