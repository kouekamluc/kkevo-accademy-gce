"""Upper Sixth Computer Science (A Level): draft practice sets, one per lesson topic."""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "upper-sixth")

SETS = []

# ---------------------------------------------------------------------------
# Data Structures & Algorithms / Abstract data types
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Data Structures & Algorithms", topic="Abstract data types",
    title="Stacks, queues, linked lists and BSTs", lesson="abstract-data-types-stacks-queues-lists-trees",
    questions=[
        MC("An empty stack receives the operations push(4), push(7), pop(), push(2), push(6), pop(), pop(). "
           "In what order are the values returned by the three pop operations?", [
            C("7, 6, 2", correct=True),
            C("4, 7, 2", why="That is first in, first out, the order a queue would give. A stack always removes the most recently added item."),
            C("7, 2, 6", why="After push(2) and push(6), the top item is 6, so 6 must come out before 2."),
            C("6, 2, 4", why="The first pop happens straight after push(7), so it returns 7. Each pop must be traced at the moment it occurs."),
        ], steps=[
            S("push(4), push(7), pop()", text="Stack 4, 7. pop returns 7, leaving 4."),
            S("push(2), push(6), pop(), pop()", text="Stack 4, 2, 6. pop returns 6, then pop returns 2. Final stack: 4."),
        ], concept="Stack (LIFO) operations", skill="Application",
           hint="Write the stack from bottom to top after every operation; pop always takes the top item.",
           feedback="You traced the stack one operation at a time, removing from the top each time."),
        NUM("A circular queue has 5 slots (indices 0 to 4), with front = 0, rear = -1 and count = 0. "
            "The operations are: enqueue P, Q, R, S; dequeue three times; enqueue T, U, V. "
            "At which index is V stored?", 1, steps=[
            S("Enqueue P, Q, R, S", text="rear moves to 0, 1, 2, 3. count = 4."),
            S("Dequeue three times", text="P, Q and R leave; front moves to 3. count = 1."),
            S("Enqueue T and U", text="T goes to index 4. Then rear = (4 + 1) mod 5 = 0, so U goes to index 0."),
            S("Enqueue V", math=r"\text{rear} = (0 + 1) \bmod 5 = 1"),
        ], concept="Circular queue pointer wrap-around", skill="Application",
           hint="Each enqueue sets rear = (rear + 1) mod 5. Trace rear carefully once it passes index 4."),
        MC("A node N must be inserted into a singly linked list directly after node P. Which sequence of pointer updates is correct?", [
            C("N.next = P.next, then P.next = N", correct=True),
            C("P.next = N, then N.next = P.next", why="After the first step P.next already points to N, so N.next = P.next makes N point to itself and the rest of the list is lost."),
            C("N.next = P, then P.next = N", why="This makes N and P point to each other in a loop; the node that used to follow P is cut off."),
            C("P.next = N.next, then N.next = P", why="N.next is still null before insertion, so P loses its successor and the list is broken."),
        ], steps=[
            S("Link the new node to its successor first", text="N.next = P.next makes N point to the node that used to follow P."),
            S("Then redirect the predecessor", text="P.next = N completes the chain P → N → old successor without losing any address."),
        ], concept="Linked list insertion and pointer order", skill="Reasoning",
           hint="Which address would be lost if you changed P.next first?",
           feedback="Linking the new node before redirecting the old one keeps the rest of the list reachable."),
        MC("The keys 40, 25, 60, 10, 30, 50, 70, 27 are inserted in that order into an empty binary search tree. What is the post-order traversal?", [
            C("10, 27, 30, 25, 50, 70, 60, 40", correct=True),
            C("40, 25, 10, 30, 27, 60, 50, 70", why="This visits each root before its subtrees, which is pre-order. Post-order puts the root last."),
            C("10, 25, 27, 30, 40, 50, 60, 70", why="This is ascending order, which is what in-order traversal gives, not post-order."),
            C("40, 60, 70, 50, 25, 30, 27, 10", why="This is the post-order sequence written backwards: root first, then right subtree before left."),
        ], steps=[
            S("Build the tree", text="40 is the root. 25 and 60 are its children. 10 and 30 are children of 25; 27 is the left child of 30. 50 and 70 are children of 60."),
            S("Post-order: left, right, root", text="Left subtree of 40 gives 10, 27, 30, 25. Right subtree gives 50, 70, 60. Then the root 40."),
        ], concept="BST insertion and post-order traversal", skill="Application",
           hint="Draw the tree first. In post-order a node is written only after both of its subtrees.",
           feedback="You built the tree carefully and wrote every root after its subtrees."),
        NUM("The keys 50, 20, 80, 10, 30, 25, 27 are inserted in that order into an empty binary search tree. "
            "How many key comparisons are needed to find 27, counting the comparison where it is found?", 5, steps=[
            S("Build the path to 27", text="27 < 50 go left to 20; 27 > 20 go right to 30; 27 < 30 go left to 25; 27 > 25 go right to 27."),
            S("Count the nodes visited", text="50, 20, 30, 25, 27: 5 comparisons."),
        ], concept="Searching a binary search tree", skill="Calculation",
           hint="Insert the keys one by one, then follow the path from the root to 27, counting each node you compare with."),
        MC("A stack is used to evaluate the postfix expression 8 3 − 4 2 + × (× means multiply). What is the result?", [
            C("30", correct=True),
            C("−30", why="When − is read, 3 is popped first and 8 second; the operation is second-popped minus first-popped, 8 − 3 = 5, not 3 − 8."),
            C("22", why="This works left to right as (8 − 3) × 4 + 2. In postfix, + is applied to 4 and 2 before × is read."),
            C("11", why="11 is 5 + 6. The last operator is ×, so the two results must be multiplied."),
        ], steps=[
            S("Read 8, 3, −", text="Push 8, push 3. On − pop 3 and 8, push 8 − 3 = 5."),
            S("Read 4, 2, +", text="Stack 5, 4, 2. On + pop 2 and 4, push 6. Stack 5, 6."),
            S("Read ×", math=r"5 \times 6 = 30"),
        ], concept="Postfix evaluation with a stack", skill="Application",
           hint="Push numbers; when you meet an operator, pop two values, apply it and push the result.",
           feedback="You kept the operand order right: the second value popped is the left operand."),
        MC("Which statement best describes an abstract data type?", [
            C("A description of data and the operations allowed on it, independent of how it is programmed", correct=True),
            C("An array together with a pointer such as top or front", why="That is a data structure: one concrete way of implementing an ADT."),
            C("A data type that cannot hold any values until it is inherited", why="This confuses an ADT with an abstract class in object-oriented programming."),
            C("A built-in type such as integer or Boolean provided by the language", why="Primitive types are not ADTs; an ADT is defined by its operations, such as push and pop."),
        ], steps=[
            S("Separate the what from the how", text="An ADT says what operations exist (push, pop, peek). A data structure such as an array with a top pointer says how they are carried out."),
        ], concept="Abstract data type versus data structure", skill="Recall",
           hint="Think of a stack: you can use push and pop without knowing whether it is an array or a linked list.",
           feedback="An ADT is the logical view; the data structure is the implementation."),
        MC("In an array-based stack, pop() is called when top = -1. What should the pop operation do?", [
            C("Report that the stack is empty (underflow) and leave top unchanged", correct=True),
            C("Return the item at index -1 and set top to -2", why="Index -1 holds no valid item and top would become invalid. Pop must test for an empty stack first."),
            C("Report that the stack is full (overflow)", why="Overflow happens on push when top equals size − 1. An empty stack on pop is underflow."),
            C("Set top to 0 and return the item at index 0", why="Index 0 holds no item yet; returning it would give garbage data and corrupt the stack."),
        ], steps=[
            S("top = -1 means the stack is empty", text="There is no item to remove."),
            S("Check before removing", text="Pop must test top = -1 first and report underflow instead of reading the array."),
        ], concept="Stack underflow and overflow checks", skill="Concept",
           hint="What does top = -1 tell you about how many items the stack holds?",
           feedback="Examiners expect pop to test for an empty stack before reading the array."),
    ]))

# ---------------------------------------------------------------------------
# Data Structures & Algorithms / Searching and sorting
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Data Structures & Algorithms", topic="Searching and sorting",
    title="Searching and sorting algorithms", lesson="searching-and-sorting-algorithms",
    questions=[
        NUM("The sorted list [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91, 95] has indices 0 to 11. "
            "Binary search with mid = (low + high) DIV 2 is used to find 45. How many comparisons with list items are made?", 4, steps=[
            S("First comparison", text="low = 0, high = 11, mid = 5. items[5] = 23 < 45, so low = 6."),
            S("Second comparison", text="mid = (6 + 11) DIV 2 = 8. items[8] = 56 > 45, so high = 7."),
            S("Third comparison", text="mid = (6 + 7) DIV 2 = 6. items[6] = 38 < 45, so low = 7."),
            S("Fourth comparison", text="mid = 7. items[7] = 45: found after 4 comparisons."),
        ], concept="Tracing binary search", skill="Calculation",
           hint="Keep a table of low, high and mid. Remember DIV discards the fraction."),
        MC("Bubble sort (ascending) is applied to [34, 12, 45, 7, 23]. What is the list after the second pass?", [
            C("[12, 7, 23, 34, 45]", correct=True),
            C("[12, 34, 7, 23, 45]", why="This is the list after the first pass only. A second pass is needed to move 34 into place."),
            C("[7, 12, 23, 34, 45]", why="This is the list after the third pass. In pass 2, 7 moves only one place left, so it is not compared with 12 until pass 3."),
            C("[7, 12, 45, 34, 23]", why="This is selection sort after two passes: it swaps the minimum to the front instead of comparing neighbours."),
        ], steps=[
            S("Pass 1", text="34 and 12 swap; 34 and 45 stay; 45 and 7 swap; 45 and 23 swap. Result: [12, 34, 7, 23, 45]."),
            S("Pass 2", text="12 and 34 stay; 34 and 7 swap; 34 and 23 swap. Result: [12, 7, 23, 34, 45]."),
        ], concept="Bubble sort pass by pass", skill="Application",
           hint="In each pass compare neighbours from the left and swap any pair that is out of order.",
           feedback="You wrote out the whole list after each pass, as examiners expect."),
        NUM("Bubble sort with an early-stop flag sorts [6, 2, 3, 4, 5, 9] into ascending order. "
            "Each pass compares one fewer pair than the pass before. How many comparisons are made in total?", 9, steps=[
            S("Pass 1", text="5 comparisons. 6 moves past 2, 3, 4 and 5: [2, 3, 4, 5, 6, 9]. Swaps were made, so continue."),
            S("Pass 2", text="4 comparisons and no swaps, so the flag stays false and the algorithm stops."),
            S("Total", math=r"5 + 4 = 9", text="Without the flag it would make 5 + 4 + 3 + 2 + 1 = 15 comparisons."),
        ], concept="Bubble sort with an early-stop flag", skill="Calculation",
           hint="The algorithm only stops after a complete pass with no swaps. That pass still counts."),
        MC("Insertion sort (ascending) is applied to [52, 18, 35, 9, 41]. What is the list immediately after 35 has been inserted into the sorted part?", [
            C("[18, 35, 52, 9, 41]", correct=True),
            C("[18, 52, 35, 9, 41]", why="This is the list after 18 is inserted; 35 has not yet been moved into place."),
            C("[9, 18, 35, 52, 41]", why="This is the list one step later, after 9 is inserted at the front."),
            C("[18, 35, 9, 41, 52]", why="This is bubble sort after one pass, which moves the largest item to the end."),
        ], steps=[
            S("Insert 18", text="18 < 52, so 52 shifts right: [18, 52, 35, 9, 41]."),
            S("Insert 35", text="35 < 52 so 52 shifts right; 35 > 18 so it stops: [18, 35, 52, 9, 41]."),
        ], concept="Insertion sort tracing", skill="Application",
           hint="The sorted part starts as just 52. Each step takes the next item and shifts larger items right.",
           feedback="Insertion sort grows a sorted part on the left one item at a time."),
        MC("Selection sort (ascending) is applied to [40, 15, 32, 8, 27]. What is the list after the third pass?", [
            C("[8, 15, 27, 40, 32]", correct=True),
            C("[8, 15, 32, 40, 27]", why="This is the list after pass 2. Pass 2 makes no change because 15 is already in place, but it still counts as a pass."),
            C("[8, 15, 27, 32, 40]", why="This is the sorted list after the fourth pass, when 32 is swapped with 40."),
            C("[15, 32, 40, 8, 27]", why="This is insertion sort after inserting 15 and 32. Selection sort searches the unsorted part for the minimum each pass."),
        ], steps=[
            S("Pass 1", text="Minimum is 8; swap with 40: [8, 15, 32, 40, 27]."),
            S("Pass 2", text="Minimum of [15, 32, 40, 27] is 15, already in place: no change."),
            S("Pass 3", text="Minimum of [32, 40, 27] is 27; swap with 32: [8, 15, 27, 40, 32]."),
        ], concept="Selection sort tracing", skill="Application",
           hint="Each pass finds the smallest item in the unsorted part and swaps it into the first unsorted position.",
           feedback="Selection sort makes at most one swap per pass."),
        NUM("Merge sort merges the sorted lists [4, 19, 33] and [7, 12, 40] into one sorted list. "
            "How many comparisons between front items are made before one list is empty?", 5, steps=[
            S("Compare front items", text="4 v 7 take 4; 19 v 7 take 7; 19 v 12 take 12; 19 v 40 take 19; 33 v 40 take 33."),
            S("Copy the rest", text="The first list is now empty, so 40 is copied with no comparison. Total: 5 comparisons, giving [4, 7, 12, 19, 33, 40]."),
        ], concept="Merging in merge sort", skill="Calculation",
           hint="Each comparison places exactly one item. What happens when one list runs out?"),
        MC("Quick sort always chooses the last item as the pivot. Which input gives its worst-case performance?", [
            C("A list that is already sorted in ascending order", correct=True),
            C("A list in random order", why="Random data usually gives fairly balanced partitions, which is the average n log n case."),
            C("A list whose middle item is the median", why="The last item is the pivot, not the middle one, so the median position does not help here."),
            C("A list with an even number of items", why="Whether the number of items is even or odd does not affect how balanced the partitions are."),
        ], steps=[
            S("Look at each partition", text="If the list is sorted, the last item is the largest, so every other item goes to its left and the right side is empty."),
            S("Effect on the work", text="Each call places only the pivot, so there are about n levels of partitioning with up to n comparisons each: about n² steps."),
        ], concept="Quick sort pivot choice and worst case", skill="Reasoning",
           hint="What happens to the two sides of the partition if the pivot is always the largest item?",
           feedback="A pivot at an extreme gives one empty side, so quick sort falls to n² steps."),
        MC("A cooperative stores 5000 unsorted farmer records and needs to find one farmer's record just once. Which approach is most suitable?", [
            C("Linear search on the unsorted records", correct=True),
            C("Binary search directly on the unsorted records", why="Binary search assumes sorted data; on an unsorted list it can discard the half containing the record and wrongly report not found."),
            C("Bubble sort the records, then binary search", why="Sorting costs far more than one linear search of 5000 items, so it only pays off if many searches will follow."),
            C("Merge sort the records, then linear search", why="Linear search works on unsorted data, so the sort is wasted work."),
        ], steps=[
            S("Check the precondition", text="The data is unsorted, so binary search cannot be used directly."),
            S("Compare the costs", text="One linear search makes at most 5000 comparisons. Any sort costs more than that, so sorting first only pays off for many searches."),
        ], concept="Choosing a search for a situation", skill="Reasoning",
           hint="Binary search needs a sorted list. Is sorting worth it for a single search?",
           feedback="For a single search of unsorted data, linear search is the sensible choice."),
    ]))

# ---------------------------------------------------------------------------
# Data Structures & Algorithms / Complexity
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Data Structures & Algorithms", topic="Complexity",
    title="Time and space complexity with Big-O", lesson="algorithm-complexity-big-o",
    questions=[
        MC(r"An algorithm performs $T(n) = 6n\log_2 n + 3n + 40$ basic operations. What is its time complexity in Big-O notation?", [
            C("O(n log n)", correct=True),
            C("O(n)", why="For large n the n log n term grows faster than 3n, so it dominates."),
            C("O(6n log n)", why="Big-O drops the constant coefficient, so the 6 must be removed."),
            C("O(n²)", why="There is no n² term. n log n grows more slowly than n²."),
        ], steps=[
            S("Find the fastest-growing term", text="Compare n log n, n and the constant 40: n log n grows fastest."),
            S("Drop the coefficient", math=r"6n\log_2 n \;\Rightarrow\; O(n \log n)"),
        ], concept="Deriving Big-O from an operation count", skill="Concept",
           hint="Keep only the term that grows fastest as n becomes large, then remove its constant.",
           feedback="Big-O keeps the dominant term without its coefficient."),
        MC("A procedure has one loop that runs n times to read marks, followed by a second, separate loop that runs n times to print them. "
           "Each loop body is a constant number of operations. What is the time complexity?", [
            C("O(n)", correct=True),
            C("O(n²)", why="Only nested loops multiply. Two loops one after the other give n + n = 2n operations."),
            C("O(2n)", why="2n is the right count, but Big-O drops the coefficient 2."),
            C("O(log n)", why="Neither loop halves the problem; each visits every item once."),
        ], steps=[
            S("Add the loops", text="The loops run one after the other, so T(n) is about n + n = 2n."),
            S("Drop the constant", text="2n is O(n): linear time."),
        ], concept="Sequential versus nested loops", skill="Reasoning",
           hint="Are the loops inside each other, or one after the other?",
           feedback="Sequential loops add; only nested loops multiply."),
        NUM("Consider: i ← 200; WHILE i > 1: i ← i DIV 2; ENDWHILE. How many times does the loop body run?", 7, steps=[
            S("Trace i", text="200, 100, 50, 25, 12, 6, 3, 1."),
            S("Count the halvings", text="i is halved 7 times before the condition i > 1 fails. This is about log2 200 ≈ 7.6, so the loop is O(log n)."),
        ], concept="Logarithmic loops", skill="Calculation",
           hint="Write down the value of i after each halving, remembering that DIV drops the fraction."),
        NUM("Bubble sort without the early-stop flag is used on a list of 20 items. How many comparisons does it make?", 190, steps=[
            S("Comparisons per pass", text="19 + 18 + ... + 1."),
            S("Use the formula", math=r"\frac{n(n-1)}{2} = \frac{20 \times 19}{2} = 190"),
        ], concept="Counting comparisons in a quadratic sort", skill="Calculation",
           hint="Pass 1 compares n − 1 pairs, pass 2 compares n − 2 pairs, and so on."),
        NUM("A program with O(n²) time complexity takes 3 seconds to process 1500 records. "
            "Estimate the time in seconds for 6000 records.", 48, unit="s", steps=[
            S("Find the size ratio", math=r"6000 \div 1500 = 4"),
            S("Square it for O(n²)", math=r"4^2 = 16"),
            S("Scale the time", math=r"3 \times 16 = 48\ \text{s}"),
        ], concept="Predicting running time from Big-O", skill="Application",
           hint="How many times bigger is the input? For a quadratic algorithm, what happens to the time?"),
        MC("Which list puts the orders of growth from fastest-running (slowest-growing) to slowest-running?", [
            C("O(1), O(log n), O(n), O(n log n), O(n²)", correct=True),
            C("O(1), O(n), O(log n), O(n log n), O(n²)", why="log n grows more slowly than n: for n = 1024, log2 n is only 10."),
            C("O(log n), O(1), O(n), O(n²), O(n log n)", why="Constant time does not grow at all, so O(1) is fastest; and n log n grows more slowly than n²."),
            C("O(1), O(log n), O(n log n), O(n), O(n²)", why="n log n is n multiplied by log n, so it grows faster than n for n > 2."),
        ], steps=[
            S("Compare at n = 1024", text="1, 10, 1024, 10 240 and 1 048 576 operations respectively."),
        ], concept="Ranking common orders of growth", skill="Recall",
           hint="Substitute a large value such as n = 1024 into each expression and compare.",
           feedback="From fastest to slowest: constant, logarithmic, linear, n log n, quadratic."),
        MC("Which sorting algorithm makes the same number of comparisons whether the list is already sorted or in reverse order?", [
            C("Selection sort", correct=True),
            C("Insertion sort", why="On a sorted list each item is compared once with its left neighbour, so its best case is O(n)."),
            C("Bubble sort with an early-stop flag", why="On a sorted list the first pass makes no swaps and it stops: O(n) best case."),
            C("Quick sort with the last item as pivot", why="Its comparisons depend heavily on the input: n log n on average but n² on sorted data."),
        ], steps=[
            S("Look at selection sort", text="Each pass must scan the whole unsorted part to be sure it has the minimum, whatever the order."),
            S("Count", text="It always makes n(n − 1)/2 comparisons, so it is O(n²) in the best, average and worst case."),
        ], concept="Best, average and worst case", skill="Concept",
           hint="Which algorithm must always scan the whole unsorted part to be sure it has found the minimum?",
           feedback="Selection sort is O(n²) in every case."),
        MC("Which algorithm has O(n) extra space complexity, rather than O(1)?", [
            C("Merge sort", correct=True),
            C("Selection sort", why="Selection sort swaps items inside the original array and needs only a few variables: O(1)."),
            C("Binary search (iterative)", why="The iterative version stores only low, high and mid: O(1) extra space."),
            C("Bubble sort", why="Bubble sort swaps neighbours in place, using one temporary variable: O(1)."),
        ], steps=[
            S("Think about extra memory", text="Merge sort copies items into temporary lists while merging, and these can hold all n items."),
        ], concept="Space complexity", skill="Concept",
           hint="Which algorithm builds new lists instead of working inside the original array?",
           feedback="Merge sort trades extra memory for guaranteed n log n time."),
    ]))

# ---------------------------------------------------------------------------
# Relational Databases / Relational algebra
# ---------------------------------------------------------------------------
_RA_TABLES = ("STUDENT(StudentID, Name, Class, Town) holds (S1, Abena, L6, Buea), (S2, Bih, U6, Bamenda), "
              "(S3, Nkeng, U6, Buea), (S4, Tchoua, L6, Dschang). RESULT(StudentID, Subject, Grade) holds "
              "(S1, Maths, A), (S2, Maths, C), (S3, CompSci, B), (S3, Maths, A). ")

SETS.append(practice_set(
    module="Relational Databases", topic="Relational algebra",
    title="Relational algebra operations", lesson="relational-algebra-operations",
    questions=[
        MC(r"Which relational algebra operator returns some of the attributes (columns) of a relation and removes duplicate tuples from the result?", [
            C(r"Projection $\pi$", correct=True),
            C(r"Selection $\sigma$", why="Selection chooses rows that meet a condition and keeps all the attributes."),
            C(r"Cartesian product $\times$", why="The product combines two relations and increases the number of attributes."),
            C(r"Difference $-$", why="Difference removes tuples that appear in a second relation; it does not choose columns."),
        ], steps=[
            S("Rows or columns?", text="Choosing columns is projection (pi for picking columns); choosing rows is selection (sigma for sieving rows)."),
        ], concept="Selection versus projection", skill="Recall",
           hint="One Greek letter sieves rows, the other picks columns.",
           feedback="Projection picks columns and removes any duplicate tuples."),
        NUM(_RA_TABLES + r"How many tuples are in $\pi_{\text{Town}}(\text{STUDENT})$?", 3, steps=[
            S("Project onto Town", text="The Town values are Buea, Bamenda, Buea, Dschang."),
            S("Remove duplicates", text="A relation has no identical tuples, so Buea appears once: {Buea, Bamenda, Dschang}, 3 tuples."),
        ], concept="Projection removes duplicate tuples", skill="Application",
           hint="List the Town values, then remember that a relation cannot contain two identical tuples."),
        NUM(_RA_TABLES + r"How many tuples are in $\sigma_{\text{Town} = \text{'Buea'}}(\text{STUDENT}) \times \text{RESULT}$?", 8, steps=[
            S("Inner expression first", text="The selection keeps S1 and S3: 2 tuples."),
            S("Cartesian product", math=r"2 \times 4 = 8 \text{ tuples}", text="Every selected student is paired with every RESULT tuple."),
        ], concept="Cartesian product size", skill="Calculation",
           hint="Evaluate the selection first, then remember that a product pairs every tuple with every tuple."),
        MC(_RA_TABLES + r"What is $\pi_{\text{Name}}(\sigma_{\text{Subject} = \text{'Maths'}}(\text{STUDENT} \bowtie \text{RESULT}))$?", [
            C("{Abena, Bih, Nkeng}", correct=True),
            C("{Abena, Nkeng}", why="These are the students with grade A in Maths. The condition is only Subject = 'Maths', so Bih (grade C) is included."),
            C("{Abena, Bih, Nkeng, Nkeng}", why="Nkeng has only one Maths tuple, and in any case projection removes duplicate tuples."),
            C("{Abena, Bih, Nkeng, Tchoua}", why="Tchoua (S4) has no RESULT tuple, so S4 does not appear in the natural join."),
        ], steps=[
            S("Natural join on StudentID", text="4 tuples: S1 Maths A, S2 Maths C, S3 CompSci B, S3 Maths A. S4 has no match."),
            S("Select Subject = 'Maths'", text="S1, S2 and S3 (Maths row)."),
            S("Project Name", text="{Abena, Bih, Nkeng}."),
        ], concept="Evaluating select, project and natural join", skill="Application",
           hint="Work from the inside out: join first, then select, then project.",
           feedback="You evaluated the nested expression from the inside out."),
        MC(_RA_TABLES + r"What is $\pi_{\text{StudentID}}(\text{STUDENT}) - \pi_{\text{StudentID}}(\sigma_{\text{Grade} = \text{'A'}}(\text{RESULT}))$?", [
            C("{S2, S4}", correct=True),
            C("{S1, S3}", why="These are the students who did get an A: the right-hand side, not the difference."),
            C("{S4}", why="That would be students with no result at all. The right-hand side only contains students with an A, so S2 (grade C) stays."),
            C("{S2, S3, S4}", why="S3 has an A in Maths, so S3 is removed even though S3 also has a B."),
        ], steps=[
            S("Left side", text="All student IDs: {S1, S2, S3, S4}."),
            S("Right side", text="IDs with grade A: {S1, S3}."),
            S("Difference", math=r"\{S1, S2, S3, S4\} - \{S1, S3\} = \{S2, S4\}"),
        ], concept="Set difference on union-compatible relations", skill="Application",
           hint="Find each side separately, then keep the IDs that are on the left but not on the right.",
           feedback="Difference keeps tuples in the first relation that are not in the second."),
        MC(r"CHOIR has the single attribute Name. Which expression is valid relational algebra?", [
            C(r"$\text{CHOIR} \cup \pi_{\text{Name}}(\text{STUDENT})$", correct=True),
            C(r"$\text{STUDENT} \cup \text{RESULT}$", why="STUDENT has 4 attributes and RESULT has 3, so they are not union-compatible."),
            C(r"$\text{CHOIR} \cap \text{STUDENT}$", why="CHOIR has one attribute and STUDENT has four, so they are not union-compatible. Project STUDENT onto Name first."),
            C(r"$\pi_{\text{Name}}(\text{STUDENT}) - \pi_{\text{Subject}}(\text{RESULT})$", why="Both have one attribute, but Name and Subject come from different domains, so the relations are not union-compatible."),
        ], steps=[
            S("Union compatibility", text="Union, intersection and difference need the same number of attributes with matching domains."),
            S("Check the valid option", text="CHOIR(Name) and the projection onto Name both have one attribute holding student names."),
        ], concept="Union compatibility", skill="Concept",
           hint="For set operations, both relations need the same number of attributes holding the same kind of values.",
           feedback="Project relations onto matching attributes before using set operations."),
        MC(r"In an SQL query, which clause corresponds to the relational algebra selection $\sigma$?", [
            C("WHERE", correct=True),
            C("SELECT", why="SQL SELECT chooses columns, so it corresponds to projection, not selection."),
            C("FROM", why="FROM names the relations; listing two tables there forms a product or join."),
            C("ORDER BY", why="Relational algebra has no ordering of tuples; ORDER BY only sorts the output."),
        ], steps=[
            S("Match the meaning", text="Selection keeps rows that satisfy a condition, which is what WHERE does."),
        ], concept="Relational algebra and SQL equivalents", skill="Recall",
           hint="Which SQL clause keeps only the rows that satisfy a condition?",
           feedback="SQL SELECT is projection; SQL WHERE is selection."),
        MC(_RA_TABLES + "Which expression gives the names of Upper Sixth students who took Maths?", [
            C(r"$\pi_{\text{Name}}(\sigma_{\text{Class} = \text{'U6'} \wedge \text{Subject} = \text{'Maths'}}(\text{STUDENT} \bowtie \text{RESULT}))$", correct=True),
            C(r"$\pi_{\text{Name}}(\sigma_{\text{Class} = \text{'U6'} \vee \text{Subject} = \text{'Maths'}}(\text{STUDENT} \bowtie \text{RESULT}))$", why="With OR, Abena (L6, Maths) is also returned. Both conditions must hold, so AND is needed."),
            C(r"$\sigma_{\text{Name}}(\pi_{\text{Class} = \text{'U6'} \wedge \text{Subject} = \text{'Maths'}}(\text{STUDENT} \bowtie \text{RESULT}))$", why="The operators are swapped: sigma takes a condition and pi takes a list of attributes."),
            C(r"$\pi_{\text{Name}}(\sigma_{\text{Class} = \text{'U6'}}(\text{STUDENT})) \cap \pi_{\text{Subject}}(\sigma_{\text{Subject} = \text{'Maths'}}(\text{RESULT}))$", why="Names and subjects are different domains, so the intersection is not valid and would be empty anyway."),
        ], steps=[
            S("Join the relations", text="Class is in STUDENT and Subject is in RESULT, so join on StudentID."),
            S("Select with both conditions", text="Class = 'U6' AND Subject = 'Maths' keeps S2 (Bih) and S3 (Nkeng)."),
            S("Project Name", text="{Bih, Nkeng}."),
        ], concept="Writing a combined relational algebra query", skill="Reasoning",
           hint="Which relations hold Class and Subject? How must the two conditions be combined?",
           feedback="Join, select with both conditions, then project the attribute you need."),
    ]))

# ---------------------------------------------------------------------------
# Relational Databases / Normalization
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Relational Databases", topic="Normalization",
    title="Functional dependencies and normalization", lesson="normalization-1nf-2nf-3nf-bcnf",
    questions=[
        MC("A wholesaler's PRODUCT table has attributes ProdCode, Description and Price. Two different products can have the same price. Which functional dependency holds?", [
            C("ProdCode → Price", correct=True),
            C("Price → ProdCode", why="Two products can cost the same, so one price can be linked to several product codes."),
            C("Price → Description", why="A price of 18 000 FCFA could belong to several different products with different descriptions."),
            C("No dependency holds between ProdCode and Price", why="Each product code has exactly one price, so ProdCode → Price does hold, even though the reverse does not."),
        ], steps=[
            S("Apply the definition", text="A → B holds when each value of A is associated with exactly one value of B."),
            S("Test each direction", text="Each product code has one price, but one price can belong to many products. So ProdCode → Price only."),
        ], concept="Functional dependency", skill="Concept",
           hint="For A → B, ask: can one value of A ever go with two different values of B?",
           feedback="The determinant on the left must fix exactly one value on the right."),
        MC("In an unnormalized orders table, deleting the only order placed by customer Ets Fomba also removes every record of that customer's name and town. What is this called?", [
            C("A deletion anomaly", correct=True),
            C("An insertion anomaly", why="An insertion anomaly is being unable to add a fact (such as a new customer) without unrelated data, such as an order."),
            C("An update anomaly", why="An update anomaly is when a fact stored in several rows is changed in some but not all of them."),
            C("A referential integrity check", why="Referential integrity stops foreign keys pointing to missing rows; it is a protection, not an anomaly."),
        ], steps=[
            S("Identify the action", text="The problem appears when a row is deleted."),
            S("Name the anomaly", text="Losing an unrelated fact (the customer's details) because a row was deleted is a deletion anomaly."),
        ], concept="Insertion, update and deletion anomalies", skill="Recall",
           hint="Which action, insert, update or delete, causes the problem here?",
           feedback="Normalization stores customer details in their own table so this cannot happen."),
        MC("ENTRY(StudentID, SubjectCode, StudentName, Grade) has the composite key (StudentID, SubjectCode), and StudentID → StudentName. Which statement is correct?", [
            C("It is not in 2NF because StudentName depends on only part of the key", correct=True),
            C("It is not in 3NF because of a transitive dependency, but it is in 2NF", why="StudentName depends on StudentID, which is part of the key, not a non-key attribute. That is a partial dependency, which breaks 2NF."),
            C("It is not in 1NF because the key has two attributes", why="A composite key is allowed in 1NF. 1NF only requires atomic values and no repeating groups."),
            C("It is in 3NF because every attribute depends on StudentID", why="Grade depends on the whole key, and StudentName depends on only part of it, so the relation fails 2NF."),
        ], steps=[
            S("Check against the composite key", text="Grade needs both StudentID and SubjectCode. StudentName needs only StudentID."),
            S("Name the dependency", text="A non-key attribute depending on part of a composite key is a partial dependency, so the relation is in 1NF but not 2NF."),
        ], concept="Partial dependency and 2NF", skill="Reasoning",
           hint="Does every non-key attribute need the whole key, or only part of it?",
           feedback="Split it into STUDENT(StudentID, StudentName) and ENTRY(StudentID, SubjectCode, Grade)."),
        MC("BOOK(ISBN, Title, PublisherID, PublisherName) has key ISBN, with ISBN → PublisherID and PublisherID → PublisherName. What should be done to reach 3NF?", [
            C("Move PublisherName to a new table PUBLISHER(PublisherID, PublisherName), keeping PublisherID in BOOK", correct=True),
            C("Nothing: the key is a single attribute, so the relation is already in 3NF", why="A single-attribute key rules out partial dependencies (2NF), but a transitive dependency can still exist."),
            C("Make (ISBN, PublisherID) the composite key", why="Changing the key does not remove the dependency PublisherID → PublisherName between non-key attributes."),
            C("Move PublisherID and PublisherName to PUBLISHER and remove PublisherID from BOOK", why="Without PublisherID in BOOK as a foreign key, you can no longer tell who published each book."),
        ], steps=[
            S("Spot the transitive dependency", text="PublisherName depends on ISBN only through the non-key attribute PublisherID."),
            S("Decompose", text="PUBLISHER(PublisherID, PublisherName) and BOOK(ISBN, Title, PublisherID), with PublisherID as a foreign key."),
        ], concept="Transitive dependency and 3NF", skill="Application",
           hint="Which non-key attribute determines another non-key attribute?",
           feedback="Remove the transitive dependency and keep the determinant behind as a foreign key."),
        MC("An order table has a repeating group of products for each OrderNo. After writing one row per product per order (1NF), what should the primary key be?", [
            C("The composite key (OrderNo, ProdCode)", correct=True),
            C("OrderNo alone", why="After removing the repeating group, one order appears in several rows, so OrderNo no longer identifies a single row."),
            C("ProdCode alone", why="The same product appears in many orders, so ProdCode does not identify a single row."),
            C("Qty", why="Quantities repeat and do not identify an order line; a key must be unique for every row."),
        ], steps=[
            S("Check uniqueness", text="Each row is one product in one order, so both OrderNo and ProdCode are needed to identify it."),
        ], concept="Choosing the key in 1NF", skill="Concept",
           hint="After the split, which combination of values appears in exactly one row?",
           feedback="Removing a repeating group usually makes the key composite."),
        NUM("BORROWING(MemberID, BookID, DateBorrowed, MemberName, MemberTown, Title, PublisherID, PublisherName) has the key (MemberID, BookID). "
            "Each book has one publisher. How many relations are in the 3NF design?", 4, steps=[
            S("Remove partial dependencies (2NF)", text="MEMBER(MemberID, MemberName, MemberTown); BOOK(BookID, Title, PublisherID, PublisherName); BORROWING(MemberID, BookID, DateBorrowed)."),
            S("Remove the transitive dependency (3NF)", text="In BOOK, PublisherID → PublisherName, so split off PUBLISHER(PublisherID, PublisherName)."),
            S("Count", text="MEMBER, BOOK, PUBLISHER and BORROWING: 4 relations."),
        ], concept="Normalizing a relation to 3NF", skill="Application",
           hint="First find what depends on MemberID alone and on BookID alone, then look for a non-key attribute that determines another."),
        MC("TUTORING(Student, Subject, Teacher): each student has one teacher per subject, and each teacher teaches only one subject. The candidate keys are (Student, Subject) and (Student, Teacher). Which statement is true?", [
            C("It is in 3NF but not in BCNF, because the determinant Teacher is not a candidate key", correct=True),
            C("It is in BCNF, because every attribute is part of a candidate key", why="Being part of a key is enough for 3NF here, but BCNF requires every determinant to be a whole candidate key. Teacher alone is not."),
            C("It is not in 2NF, because Subject depends on part of a key", why="Subject is part of a candidate key, so it is not a non-key attribute; the 2NF and 3NF rules are about non-key attributes."),
            C("It is not in 1NF, because it has two candidate keys", why="A relation can have several candidate keys. 1NF is about atomic values and repeating groups."),
        ], steps=[
            S("List the dependencies", text="(Student, Subject) → Teacher and Teacher → Subject."),
            S("Apply the BCNF test", text="Teacher is a determinant but not a candidate key, so the relation is not in BCNF. There are no non-key attributes, so it is in 3NF."),
        ], concept="3NF versus BCNF", skill="Reasoning",
           hint="List every determinant. Is each one a candidate key on its own?",
           feedback="Decompose into TEACHES(Teacher, Subject) and TUTORED(Student, Teacher) to reach BCNF."),
        MC("Which is a genuine disadvantage of normalizing a database to 3NF?", [
            C("Queries need more joins, so they can be slower and harder to write", correct=True),
            C("Update anomalies become more likely", why="Normalization removes update anomalies by storing each fact once."),
            C("More data is duplicated across tables", why="Only foreign keys are repeated; normalization reduces duplication overall."),
            C("Tables can no longer have primary keys", why="Every normalized table has a primary key; keys are central to the process."),
        ], steps=[
            S("Think about the cost", text="Data is split across more tables, so answering a question often needs several joins."),
        ], concept="Advantages and disadvantages of normalization", skill="Concept",
           hint="What extra work does a query have to do once data is spread over several tables?",
           feedback="Normalization saves space and removes anomalies at the cost of more joins."),
    ]))

# ---------------------------------------------------------------------------
# Relational Databases / SQL
# ---------------------------------------------------------------------------
_SQL_TABLES = ("Student(StudentID, Name, Class, Town) holds S1 Abena L6 Buea, S2 Bih U6 Bamenda, S3 Nkeng U6 Buea, "
               "S4 Tchoua L6 Dschang, S5 Manga U6 Kribi. Subject(SubjectCode, Title) holds MAT Mathematics, "
               "CSC Computer Science, PHY Physics. Result(StudentID, SubjectCode, Mark) holds S1 MAT 72, S1 CSC 65, "
               "S2 MAT 48, S3 CSC 81, S3 MAT 77, S4 PHY 55. ")

SETS.append(practice_set(
    module="Relational Databases", topic="SQL",
    title="SQL: DDL, DML, joins and subqueries", lesson="sql-ddl-dml-joins-subqueries",
    questions=[
        MC("Which of these SQL statements belongs to the Data Manipulation Language (DML)?", [
            C("DELETE FROM Result WHERE Mark < 20;", correct=True),
            C("DROP TABLE Result;", why="DROP TABLE removes the table structure itself, so it is DDL."),
            C("ALTER TABLE Student ADD Phone VARCHAR(15);", why="ALTER TABLE changes the structure of a table, so it is DDL."),
            C("CREATE TABLE Teacher (TeacherID CHAR(4) PRIMARY KEY);", why="CREATE TABLE defines a new structure, so it is DDL."),
        ], steps=[
            S("Structure or data?", text="DDL (CREATE, ALTER, DROP) changes structure. DML (INSERT, UPDATE, DELETE, SELECT) works with the rows of data."),
            S("Classify", text="DELETE removes data rows but leaves the table, so it is DML."),
        ], concept="DDL versus DML", skill="Recall",
           hint="Does the statement change the shape of a table, or the rows stored in it?",
           feedback="DELETE removes rows; DROP removes the whole table."),
        NUM(_SQL_TABLES + "How many rows does SELECT S.Name, R.Mark FROM Student S LEFT JOIN Result R ON S.StudentID = R.StudentID; return?", 7, steps=[
            S("Matching rows", text="Each of the 6 Result rows matches a student, giving 6 rows (Abena and Nkeng twice)."),
            S("Unmatched left rows", text="Manga (S5) has no result. A LEFT JOIN still keeps Manga, with Mark NULL."),
            S("Total", math=r"6 + 1 = 7"),
        ], concept="LEFT JOIN keeps unmatched rows", skill="Application",
           hint="Count the matching pairs first, then add any student who has no match at all."),
        NUM(_SQL_TABLES + "How many rows does SELECT StudentID, AVG(Mark) FROM Result GROUP BY StudentID HAVING AVG(Mark) >= 60; return?", 2, steps=[
            S("Form the groups", text="S1: (72 + 65) / 2 = 68.5. S2: 48. S3: (81 + 77) / 2 = 79. S4: 55."),
            S("Apply HAVING", text="Only S1 and S3 have an average of at least 60: 2 rows."),
        ], concept="GROUP BY with HAVING", skill="Calculation",
           hint="Make one group per student, find each group's average, then filter the groups."),
        MC("A student writes SELECT SubjectCode, AVG(Mark) FROM Result WHERE AVG(Mark) > 60 GROUP BY SubjectCode; and gets an error. What is the correct fix?", [
            C("Remove the WHERE clause and add HAVING AVG(Mark) > 60 after GROUP BY SubjectCode", correct=True),
            C("Replace AVG(Mark) with Mark in the WHERE clause", why="That runs, but it filters individual marks before grouping, so it answers a different question."),
            C("Move WHERE AVG(Mark) > 60 to the end of the query", why="WHERE must come before GROUP BY and still cannot contain an aggregate function."),
            C("Replace GROUP BY with ORDER BY", why="Without GROUP BY there are no groups to average per subject; ORDER BY only sorts."),
        ], steps=[
            S("Why it fails", text="WHERE filters single rows before grouping, so an aggregate such as AVG cannot be used there."),
            S("Fix", text="Filter the groups after they are formed: GROUP BY SubjectCode HAVING AVG(Mark) > 60."),
        ], concept="WHERE versus HAVING", skill="Reasoning",
           hint="Which clause filters rows before grouping, and which filters groups after?",
           feedback="Aggregates belong in HAVING, not WHERE."),
        MC("The Result table was created with Mark INTEGER CHECK (Mark BETWEEN 0 AND 100). What happens when INSERT INTO Result VALUES ('S2', 'PHY', 120); is run?", [
            C("The row is rejected because it breaks the CHECK constraint", correct=True),
            C("The row is inserted with Mark set to 100", why="A DBMS does not silently correct values; a constraint violation rejects the whole statement."),
            C("The row is rejected because S2 does not exist in Student", why="S2 (Bih) does exist, so the foreign key is satisfied. The problem is the mark."),
            C("The row is inserted because the primary key (S2, PHY) is new", why="A new key is necessary but not enough: every constraint on every column must also be satisfied."),
        ], steps=[
            S("Check each constraint", text="(S2, PHY) is a new key, S2 and PHY both exist, but 120 is outside 0 to 100."),
            S("Result", text="The CHECK constraint fails, so the DBMS refuses the insertion."),
        ], concept="Constraints in DDL", skill="Application",
           hint="Look at every constraint on the Result table, not just the key.",
           feedback="Constraints let the DBMS reject invalid data automatically."),
        MC("What is the effect of running DELETE FROM Result; with no WHERE clause?", [
            C("Every row is removed but the empty Result table still exists", correct=True),
            C("The Result table and its structure are removed", why="That is DROP TABLE Result, a DDL statement. DELETE only removes rows."),
            C("Nothing happens because a WHERE clause is required", why="WHERE is optional; without it the statement applies to every row."),
            C("Only the last row inserted is removed", why="SQL has no idea of a last row here; DELETE without WHERE matches every row."),
        ], steps=[
            S("No condition", text="Without WHERE, every row satisfies the statement, so all rows are deleted."),
            S("Structure stays", text="The table definition remains and new rows can be inserted later."),
        ], concept="DELETE without WHERE", skill="Concept",
           hint="Which rows does a statement apply to when no condition is given?",
           feedback="Always check the WHERE clause before running UPDATE or DELETE."),
        MC(_SQL_TABLES + "Which query lists the names of students who have no result at all?", [
            C("SELECT Name FROM Student WHERE StudentID NOT IN (SELECT StudentID FROM Result);", correct=True),
            C("SELECT Name FROM Student WHERE StudentID IN (SELECT StudentID FROM Result);", why="IN returns the students who do have results: Abena, Bih, Nkeng and Tchoua."),
            C("SELECT S.Name FROM Student S INNER JOIN Result R ON S.StudentID = R.StudentID WHERE R.Mark IS NULL;", why="An inner join drops students with no result, so there are no NULL marks to find: the output is empty."),
            C("SELECT S.Name FROM Student S LEFT JOIN Result R ON S.StudentID = R.StudentID WHERE R.Mark = NULL;", why="Comparing with = NULL is never true in SQL, so this returns nothing. It needs IS NULL."),
        ], steps=[
            S("Inner query", text="SELECT StudentID FROM Result gives S1, S2, S3, S4."),
            S("Outer query", text="Keep students whose ID is NOT IN that list: Manga."),
        ], concept="Nested subqueries with NOT IN", skill="Application",
           hint="First find the IDs of students who do have results. Then which students are left?",
           feedback="The inner query runs first and the outer query uses its result."),
        MC(_SQL_TABLES + "What does this query output? SELECT J.Title, COUNT(R.StudentID) FROM Result R INNER JOIN Subject J ON R.SubjectCode = J.SubjectCode GROUP BY J.Title HAVING COUNT(R.StudentID) >= 2;", [
            C("Computer Science 2 and Mathematics 3", correct=True),
            C("Computer Science 2, Mathematics 3 and Physics 1", why="Physics has only one entry, so HAVING COUNT(R.StudentID) >= 2 removes that group."),
            C("Mathematics 3 only", why="Computer Science has two entries (S1 and S3), which satisfies >= 2."),
            C("Abena 2 and Nkeng 2", why="The query groups by subject title, not by student name."),
        ], steps=[
            S("Join and group", text="MAT has 3 results, CSC has 2, PHY has 1."),
            S("Filter the groups", text="HAVING keeps groups with at least 2 rows: Computer Science 2, Mathematics 3."),
        ], concept="Joins with aggregate functions", skill="Interpretation",
           hint="Count the results for each subject, then apply the HAVING condition.",
           feedback="GROUP BY forms the groups; HAVING then filters them."),
    ]))

# ---------------------------------------------------------------------------
# Object-Oriented Programming / OOP principles
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Object-Oriented Programming", topic="OOP principles",
    title="The four principles of OOP", lesson="oop-principles",
    questions=[
        MC("In the statement rice = StockItem(\"Rice 50 kg\", 22000, 10), what is rice?", [
            C("An object: an instance of the class StockItem", correct=True),
            C("A class", why="StockItem is the class (the blueprint); rice is one instance created from it."),
            C("A method of StockItem", why="Methods are behaviours such as sell and restock; rice is created by calling the constructor."),
            C("A private attribute", why="Attributes such as __price belong inside an object; rice is the object itself."),
        ], steps=[
            S("Class versus object", text="A class defines attributes and methods; calling it creates an object with its own attribute values."),
        ], concept="Class and object", skill="Recall",
           hint="Which is the blueprint and which is the thing built from it?",
           feedback="rice has its own values: name Rice 50 kg, price 22000 and quantity 10."),
        MC("StockItem stores its quantity in a private attribute __quantity, which can only be changed through sell(n) and restock(n), and both methods check n. Which principle does this show?", [
            C("Encapsulation", correct=True),
            C("Inheritance", why="No subclass is involved; inheritance is about a subclass reusing a superclass."),
            C("Polymorphism", why="Polymorphism is one method call behaving differently for different classes of object."),
            C("Overloading", why="Overloading means several methods with the same name but different parameters, which is not described here."),
        ], steps=[
            S("Identify the features", text="The data is hidden (private) and bundled with the methods that are allowed to change it."),
            S("Name the principle", text="Hiding data behind validating methods is encapsulation; it protects data integrity."),
        ], concept="Encapsulation", skill="Concept",
           hint="What is being hidden here, and who is allowed to change it?",
           feedback="Encapsulation means every change goes through methods that check it."),
        MC("An abstract class Staff declares an abstract method pay() without any code, and Staff objects cannot be created. Which principle does this show most directly?", [
            C("Abstraction", correct=True),
            C("Encapsulation", why="Encapsulation hides data behind methods. Here the focus is on showing only the essential idea, that staff can be paid, without the detail."),
            C("Overloading", why="There is only one pay() with one parameter list, so nothing is overloaded."),
            C("Composition", why="Composition is a \"has a\" relationship using attributes; no object here contains another."),
        ], steps=[
            S("What is hidden?", text="Staff says every staff member can be paid, but hides how pay is worked out."),
            S("Name the principle", text="Showing only essential features and hiding unnecessary detail is abstraction."),
        ], concept="Abstraction and abstract classes", skill="Concept",
           hint="Does Staff hide data, or hide how something is done?",
           feedback="A private attribute is encapsulation; an abstract method is abstraction."),
        NUM("FullTimeTeacher and PartTimeTeacher both inherit from Staff and override pay(). Full-time pay is the salary; part-time pay is hours × rate. "
            "The list staff holds FullTimeTeacher(\"Mr Ndi\", 180000) and PartTimeTeacher(\"Mrs Ayuk\", 25, 4000). "
            "What is the value of total after: total = 0, then for s in staff: total = total + s.pay()?", 280000, unit="FCFA", steps=[
            S("First object", text="FullTimeTeacher.pay() returns the salary: 180 000."),
            S("Second object", math=r"25 \times 4000 = 100\,000"),
            S("Add", math=r"180\,000 + 100\,000 = 280\,000"),
        ], concept="Polymorphism through overriding", skill="Application",
           hint="For each object, use the pay() of that object's own class."),
        MC("A Java class Calculator contains int add(int a, int b), int add(int a, int b, int c) and double add(double a, double b). What is this called?", [
            C("Overloading", correct=True),
            C("Overriding", why="Overriding is a subclass redefining a method with the same name and parameters. Here all three are in one class with different parameters."),
            C("Inheritance", why="There is only one class, so nothing is inherited."),
            C("Encapsulation", why="Encapsulation is about hiding data; these methods differ only in their parameter lists."),
        ], steps=[
            S("Same class, same name", text="All three methods are in Calculator and are called add."),
            S("Different parameters", text="The parameter lists differ, so the compiler picks the version from the arguments: overloading."),
        ], concept="Overloading versus overriding", skill="Concept",
           hint="Are the methods in one class or in a superclass and a subclass? Do their parameters match?",
           feedback="Overloading is chosen at compile time; overriding is chosen at run time."),
        MC("Which design is a correct use of inheritance?", [
            C("Teacher inherits from Person", correct=True),
            C("Classroom inherits from Teacher", why="A classroom has a teacher but is not a teacher. A \"has a\" relationship needs an attribute, not inheritance."),
            C("Person inherits from Teacher", why="The direction is reversed: every teacher is a person, but not every person is a teacher."),
            C("FeeAccount inherits from Student", why="A student owns a fee account (association); a fee account is not a kind of student."),
        ], steps=[
            S("Apply the \"is a\" test", text="A teacher is a person, so Teacher can inherit Person's name and phone."),
        ], concept="Inheritance and the is-a relationship", skill="Reasoning",
           hint="Read each design as \"A is a B\". Which one is true?",
           feedback="Inheritance models \"is a\"; composition models \"has a\"."),
        MC("For the StockItem class in the lesson, rice has quantity 10. What happens when rice.sell(12) is called?", [
            C("A ValueError is raised and the quantity stays 10", correct=True),
            C("The quantity becomes -2 and 264 000 is returned", why="sell checks n > quantity before changing anything, so it never subtracts 12 from 10."),
            C("All 10 bags are sold and 220 000 is returned", why="The method does not adjust the request; an invalid quantity is refused with an exception."),
            C("An AttributeError is raised because __quantity is private", why="sell is a method of the class, so it can read the private attribute; only outside code cannot."),
        ], steps=[
            S("Check the condition", text="12 > 10, so the test n <= 0 or n > quantity is true."),
            S("Effect", text="ValueError is raised before the quantity line runs, so the quantity stays 10."),
        ], concept="Encapsulation protects data integrity", skill="Application",
           hint="Look at what sell checks before it changes the quantity.",
           feedback="Because every change is checked, the quantity can never become negative."),
        NUM("For the StockItem class in the lesson: oil = StockItem(\"Palm oil 20 L\", 18000, 6); oil.sell(4); oil.restock(5). "
            "Then oil.sell(8) is called inside a try block that catches ValueError. What does oil.get_quantity() return afterwards?", 7, steps=[
            S("After sell(4)", math=r"6 - 4 = 2"),
            S("After restock(5)", math=r"2 + 5 = 7"),
            S("sell(8)", text="8 > 7, so ValueError is raised before the quantity changes. The quantity stays 7."),
        ], concept="Tracing method calls on an object", skill="Application",
           hint="Track the private quantity after each call, and check whether sell(8) passes its validation."),
    ]))

# ---------------------------------------------------------------------------
# Object-Oriented Programming / Classes in practice
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Object-Oriented Programming", topic="Classes in practice",
    title="UML, access, constructors and exceptions", lesson="classes-in-practice-uml-constructors-exceptions",
    questions=[
        MC("In a UML class box, the FeeAccount attribute is written as - balance : Integer. What does the minus sign mean?", [
            C("balance is private: only code inside FeeAccount can access it", correct=True),
            C("balance is public: any class can access it", why="Public is shown with a plus sign (+)."),
            C("balance is protected: FeeAccount and its subclasses can access it", why="Protected is shown with a hash sign (#)."),
            C("balance can never be negative", why="UML visibility symbols describe access, not the range of values. Validation belongs in the methods."),
        ], steps=[
            S("Recall the visibility symbols", text="+ public, - private, # protected."),
        ], concept="UML visibility symbols", skill="Recall",
           hint="There are three symbols: plus, minus and hash. Which one is normal for attributes?",
           feedback="Attributes are usually private, with public methods to access them."),
        MC("In a UML class diagram, Student and Teacher are each joined to Person by a line ending in a hollow triangle at Person. What does this show?", [
            C("Student and Teacher inherit from Person", correct=True),
            C("Person inherits from Student and Teacher", why="The triangle points at the superclass, so Person is the parent class."),
            C("Each Person owns one Student and one Teacher", why="Ownership (association) is shown by a plain line with multiplicities, not a hollow triangle."),
            C("Student and Teacher are private attributes of Person", why="Attributes are listed inside the class box, not drawn as lines."),
        ], steps=[
            S("Read the arrowhead", text="A hollow triangle means inheritance and points at the superclass."),
        ], concept="Inheritance in UML class diagrams", skill="Interpretation",
           hint="Which end of the line has the triangle, and what does that class represent?",
           feedback="Hollow triangle: inheritance, pointing to the superclass."),
        MC("A UML association between Teacher and SchoolClass has 1 at the Teacher end and 1..many at the SchoolClass end. What does this mean?", [
            C("Each teacher teaches one or more classes, and each class has exactly one class teacher", correct=True),
            C("Each teacher teaches exactly one class, and each class has one or more teachers", why="The multiplicity is read at the far end: 1..many beside SchoolClass tells how many classes one teacher has."),
            C("Each teacher teaches zero or more classes", why="1..many means at least one; zero or more would be written 0..many."),
            C("SchoolClass inherits from Teacher", why="Multiplicities label an association; inheritance is shown with a hollow triangle and has no multiplicities."),
        ], steps=[
            S("Read from Teacher", text="One teacher is linked to 1..many SchoolClass objects: one or more."),
            S("Read from SchoolClass", text="One class is linked to 1 Teacher: exactly one."),
        ], concept="Associations and multiplicity", skill="Interpretation",
           hint="To find how many classes one teacher has, read the number next to SchoolClass.",
           feedback="Read each multiplicity at the opposite end of the line from the object you start with."),
        MC("The C++ class Logger prints Open name in its constructor and Close name in its destructor. "
           "main() creates Logger a(\"X\"); then an inner block { Logger b(\"Y\"); Logger c(\"Z\"); }; then Logger d(\"W\"); and returns. What is the output order?", [
            C("Open X, Open Y, Open Z, Close Z, Close Y, Open W, Close W, Close X", correct=True),
            C("Open X, Open Y, Open Z, Close Y, Close Z, Open W, Close W, Close X", why="Objects in a scope are destroyed in reverse order of creation, so Z (created last) closes before Y."),
            C("Open X, Open Y, Open Z, Open W, Close W, Close Z, Close Y, Close X", why="b and c are destroyed at the closing brace of the inner block, before d is created."),
            C("Open X, Open Y, Open Z, Open W, Close X, Close Y, Close Z, Close W", why="Destructors run when objects go out of scope, in reverse order of creation, not in creation order at the end."),
        ], steps=[
            S("Inner block", text="Y and Z are created, then destroyed at the closing brace in reverse order: Close Z, Close Y."),
            S("End of main", text="W is created after the block. At return, W then X are destroyed: Close W, Close X."),
        ], concept="Constructor and destructor order", skill="Application",
           hint="An object is destroyed when its scope ends; within a scope, the last object created is the first destroyed.",
           feedback="C++ destructors run at the end of scope in reverse order of creation."),
        NUM("Using the FeeAccount class from the lesson: acc = new FeeAccount(\"U6-020\", 60000). Inside a try block the program calls acc.pay(20000), then acc.pay(-5000), then acc.pay(10000). "
            "The catch block prints the error and the finally block prints the balance. What balance is printed?", 40000, unit="FCFA", steps=[
            S("acc.pay(20000)", math=r"60\,000 - 20\,000 = 40\,000"),
            S("acc.pay(-5000)", text="The amount is not positive, so pay throws IllegalArgumentException. Control jumps to catch, so pay(10000) never runs."),
            S("finally", text="The finally block prints Balance: 40000."),
        ], concept="Throwing and catching exceptions", skill="Application",
           hint="After an exception is thrown, does the rest of the try block run?"),
        MC("A student writes public void FeeAccount(String studentId, int fees) { ... } inside the Java class FeeAccount. What is the effect?", [
            C("It becomes an ordinary method, so it does not run when an object is created", correct=True),
            C("It works as a constructor that returns nothing", why="A constructor has no return type, not even void. Adding void makes Java treat it as a normal method."),
            C("It works as a destructor", why="Java has no destructors of this form; memory is freed by the garbage collector."),
            C("It makes the attributes public", why="The modifiers on a method do not change the visibility of the attributes."),
        ], steps=[
            S("Constructor rule", text="A Java constructor has the class name and no return type."),
            S("Effect of void", text="With void it is an ordinary method, so new FeeAccount(...) does not call it and the attributes are not set."),
        ], concept="Writing constructors", skill="Concept",
           hint="What is special about the declaration of a constructor compared with a normal method?",
           feedback="Constructors never have a return type."),
        MC("In a try-catch-finally structure, when does the finally block run?", [
            C("Always, whether or not an exception was thrown in the try block", correct=True),
            C("Only when an exception is thrown", why="That describes the catch block. finally also runs when the try block completes normally."),
            C("Only when no exception is thrown", why="finally still runs after a catch block handles an exception; that is why it is used for clean-up."),
            C("Only when the catch block is empty", why="The contents of the catch block do not affect whether finally runs."),
        ], steps=[
            S("Purpose of finally", text="It holds clean-up code, such as closing a file, which must run in every case."),
        ], concept="try-catch-finally", skill="Recall",
           hint="Think about what finally is used for: clean-up that must always happen.",
           feedback="finally runs in every case, so it is used for clean-up."),
        MC("Person has an attribute # phone : String. Teacher is a subclass of Person; Bursar is an unrelated class in another package. Which code can access phone directly?", [
            C("Code in Person and in Teacher, but not in Bursar", correct=True),
            C("Only code in Person", why="That describes private (-). Protected also allows access from subclasses such as Teacher."),
            C("Code in Person, Teacher and Bursar", why="That describes public (+). An unrelated class in another package cannot access a protected member."),
            C("Only code in Teacher", why="The class that declares an attribute can always access it."),
        ], steps=[
            S("Read the symbol", text="# means protected."),
            S("Apply the rule", text="Protected members are accessible inside the class and its subclasses, so Person and Teacher can use phone; Bursar cannot."),
        ], concept="Access modifiers", skill="Reasoning",
           hint="What does # mean, and how is it different from + and -?",
           feedback="Protected sits between private and public."),
    ]))

# ---------------------------------------------------------------------------
# Software Project / Individual project
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module="Software Project", topic="Individual project",
    title="Planning, testing and reporting a project", lesson="individual-software-project-guide",
    questions=[
        MC("A student interviews the secretary of a njangi group, collects sample pages from her exercise book and writes numbered objectives. Which project stage is this?", [
            C("Analysis", correct=True),
            C("Design", why="Design comes after analysis: it plans tables, diagrams, pseudocode, screens and the test plan."),
            C("Implementation", why="Implementation is writing the code; no code is written here."),
            C("Evaluation", why="Evaluation happens at the end, comparing the finished system with the objectives written during analysis."),
        ], steps=[
            S("Match the activities", text="Understanding the current system and the user's needs, and writing objectives, is analysis."),
        ], concept="Stages of a software project", skill="Recall",
           hint="Which stage is about understanding the problem before planning a solution?",
           feedback="Analysis produces the objectives that the rest of the project is measured against."),
        MC("Which of these is a measurable objective for a njangi contributions system?", [
            C("The system lists the members who have not paid for a chosen month", correct=True),
            C("The system should be easy to use", why="\"Easy\" cannot be tested; there is no way to show at the end whether it was met."),
            C("The system should be modern and attractive", why="This is a matter of opinion and cannot be checked with a test."),
            C("The system should be better than the exercise book", why="\"Better\" is vague; it does not say what the system must do or how success is measured."),
        ], steps=[
            S("Test each objective", text="Ask: could a test show clearly whether this is met? Only the list of unpaid members can be checked directly."),
        ], concept="Writing measurable objectives", skill="Concept",
           hint="For each option, imagine writing a test. Which one gives a clear pass or fail?",
           feedback="Each objective should be specific enough to be tested and discussed in the evaluation."),
        MC("A field for a student's age must accept whole numbers from 15 to 21. Which value is boundary data that should be rejected?", [
            C("22", correct=True),
            C("21", why="21 is boundary data, but it is inside the valid range, so it should be accepted."),
            C("18", why="18 is typical valid data: normal data."),
            C("\"eighteen\"", why="Text is erroneous data (wrong type), not boundary data."),
        ], steps=[
            S("Find the edges", text="The limits are 15 and 21. Boundary data is at the edges and just outside: 14, 15, 21 and 22."),
            S("Choose the rejected one", text="22 is just outside the upper limit, so it is boundary data that should be rejected."),
        ], concept="Normal, boundary and erroneous test data", skill="Application",
           hint="Boundary data sits on the edges of the range and just beyond them.",
           feedback="Test both sides of every limit."),
        NUM("A contribution must be a whole number from 1000 to 50 000 FCFA. How many of these test values should be accepted: "
            "999, 1000, 25 000, 50 000, 50 001, \"ten thousand\", -500, 2500.5?", 3, steps=[
            S("Check the range", text="999, 50 001 and -500 are outside 1000 to 50 000."),
            S("Check the type", text="\"ten thousand\" is text and 2500.5 is not a whole number."),
            S("Count the valid values", text="1000, 25 000 and 50 000: 3 values."),
        ], concept="Validation rules and test data", skill="Application",
           hint="A value must pass both checks: is it a whole number, and is it inside the range?"),
        MC("A student runs tests that call valid_contribution() on its own with the values 1000, 999 and \"ten thousand\". What kind of testing is this?", [
            C("Unit testing", correct=True),
            C("Integration testing", why="Integration testing checks modules working together, such as the Ledger class using the validation function."),
            C("Acceptance testing", why="Acceptance testing is done with the real user on the whole system."),
            C("Evaluation", why="Evaluation is a report stage comparing the system with the objectives; it is not a kind of test run."),
        ], steps=[
            S("How much is being tested?", text="One function is tested in isolation, which is unit testing."),
        ], concept="Unit versus integration testing", skill="Concept",
           hint="Is one module being tested alone, or several modules together?",
           feedback="Unit tests check one module; integration tests check modules together."),
        NUM("The Ledger class in the lesson rejects invalid amounts with ValueError. A test calls book.record(\"M01\", 8000), book.record(\"M02\", 3000), "
            "book.record(\"M01\", 4000), then book.record(\"M03\", 500) inside assertRaises. What does book.total() return?", 15000, unit="FCFA", steps=[
            S("Valid payments", text="M01: 8000 + 4000 = 12 000. M02: 3000."),
            S("Invalid payment", text="500 is below 1000, so record raises ValueError and nothing is added for M03."),
            S("Total", math=r"12\,000 + 3000 = 15\,000"),
        ], concept="Reading an integration test", skill="Application",
           hint="Add up only the payments that pass the validation function."),
        MC("Which item belongs in the design section of the project report rather than the analysis section?", [
            C("Normalized tables with keys and pseudocode for the main algorithms", correct=True),
            C("Notes from the interview with the user", why="Interview notes record the user's needs, which is analysis."),
            C("A description of how the current paper system works", why="Studying the current system is part of analysis."),
            C("A judgement of whether each objective was met", why="That belongs in the evaluation, after testing."),
        ], steps=[
            S("Purpose of design", text="Design plans the solution in enough detail for another programmer to build it: data, diagrams, algorithms, screens, validation and the test plan."),
        ], concept="Structure of the technical report", skill="Concept",
           hint="Which item plans how the solution will be built?",
           feedback="Analysis says what is needed; design says how it will be built."),
        MC("Which is the best evaluation of one objective in a project report?", [
            C("Objective 3 is met: tests 7 to 9 show the unpaid-members list is correct, and the secretary confirmed it matched her records", correct=True),
            C("The system works well and the user is happy", why="This gives no link to a specific objective and no test evidence."),
            C("All objectives were met because the program runs without crashing", why="Not crashing does not show that each objective was achieved; each one needs its own evidence."),
            C("Objective 3 was difficult to code, so it took two weeks", why="This describes the effort, not whether the objective was achieved."),
        ], steps=[
            S("What an evaluation needs", text="For each objective: met, partly met or not met, with reference to test evidence and user feedback."),
        ], concept="Evaluating against objectives with evidence", skill="Interpretation",
           hint="A good evaluation refers to a specific objective and to evidence that it is met.",
           feedback="Evaluate each objective in turn, with evidence and honesty about limitations."),
    ]))
