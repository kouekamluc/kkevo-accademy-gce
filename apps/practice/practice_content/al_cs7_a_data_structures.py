"""Upper Sixth Computer Science (A Level): practice sets for Data Structures & Algorithms, one per lesson (12 sets)."""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "upper-sixth")

MODULE = "Data Structures & Algorithms"
ADT = "Abstract data types"
SS = "Searching and sorting"
CX = "Complexity"


def Q(prompt, answer, wrongs, pos, steps, concept, skill, hint, feedback=""):
    """Four-option multiple choice: `wrongs` is three (text, why) pairs; the right answer goes at index `pos` (0 = A)."""
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(pos, C(answer, correct=True))
    return MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint, feedback=feedback)


SETS = []

# ------------------------------------------------------------------ 1. Stack
SETS.append(practice_set(
    module=MODULE, topic=ADT,
    title="Stack operations and uses", lesson="csc-stack-push-pop",
    questions=[
        Q("Which rule describes a stack?", "Last in, first out", [
            ("First in, first out", "That is a queue: the first item added leaves first."),
            ("Smallest item out first", "A stack does not look at the values, only at the order of arrival."),
            ("Items can be removed from either end", "A stack has one open end, the top.")], 1,
          [S("Recall", text="Items are added and removed at the top only, so the latest item added is the first removed.")],
          "Stack (LIFO)", "Recall", "Think of a pile of plates."),
        Q("An array stack uses an index called top. What is the value of top when the stack is empty?", "-1", [
            ("0", "top = 0 means there is one item, at index 0."),
            ("1", "Index 1 is the second place in the array."),
            ("The size of the array", "top = SIZE - 1 means the stack is full, and SIZE is outside the array.")], 0,
          [S("Reason", text="The first push does top + 1 and stores at index 0, so top must start one place before index 0: -1.")],
          "Top pointer", "Concept", "What must top be so that the first push lands in index 0?"),
        Q("A stack is empty. What happens when pop is called?", "Underflow is reported", [
            ("Overflow is reported", "Overflow happens on a push to a full stack."),
            ("The stack becomes full", "Pop never adds items."),
            ("The bottom item is returned", "An empty stack has no items to return.")], 2,
          [S("Check the test", text="pop must test isEmpty first. top = -1 means no items, so the pop fails with underflow.")],
          "Overflow and underflow", "Concept", "There is nothing to remove."),
        NUM("A stack of size 6 starts empty. Operations: push 5, push 9, push 2, pop, push 7. What is the value of top (an array index) at the end?", 2,
            steps=[S("Three pushes", text="top goes 0, 1, 2."), S("Pop", text="top becomes 1."), S("Push 7", text="top becomes 2. The stack holds 5, 9, 7.")],
            concept="Tracing push and pop", skill="Calculation", hint="Count pushes up and pops down from -1."),
        Q("Operations on an empty stack: push 4, push 6, pop, push 8, pop, pop. What does the last pop return?", "4", [
            ("6", "6 was returned by the first pop. It is no longer in the stack."),
            ("8", "8 was returned by the second pop."),
            ("Underflow", "The stack still holds 4 at that point, so the pop succeeds.")], 3,
          [S("Trace", text="push 4, push 6: stack 4, 6. pop returns 6: stack 4. push 8: stack 4, 8. pop returns 8: stack 4. pop returns 4.")],
          "Tracing push and pop", "Application", "Write the stack after every operation."),
        Q("Evaluate the postfix expression 7 2 - 3 *.", "15", [
            ("-1", "This computes 2 * 3 - 7. The minus is applied to 7 and 2 before the multiplication."),
            ("1", "This computes 7 - (2 * 3). In postfix the minus is applied before the *."),
            ("-15", "This swaps the operands in 7 - 2, giving -5, then multiplies by 3.")], 2,
          [S("7 2 -", text="Pop 2 then 7: 7 - 2 = 5."), S("5 3 *", text="Push 3, pop 3 and 5: 5 * 3 = 15.")],
          "Postfix evaluation", "Calculation", "Apply each operator to the two items just before it."),
        Q("Which of these bracket strings is NOT correctly nested?", "([)]", [
            ("{[()]}", "Each closing bracket matches the most recent open bracket: valid."),
            ("(())", "Both pairs are properly nested: valid."),
            ("[](){}", "Three separate matched pairs: valid.")], 3,
          [S("Push and pop", text="For ([)] the stack holds ( and [ when ) arrives. The top is [, which does not match ), so the string is invalid.")],
          "Bracket checking", "Reasoning", "At each closing bracket, what is on top of the stack?"),
        NUM("Evaluate the postfix expression 9 3 / 4 +. Give the number.", 7,
            steps=[S("9 3 /", text="Pop 3 then 9: 9 / 3 = 3. Stack: 3."), S("3 4 +", text="Push 4, then add: 3 + 4 = 7.")],
            concept="Postfix evaluation", skill="Calculation", hint="Do the division first: the operator comes after its two numbers."),
    ]))

# ------------------------------------------------------------------ 2. Circular queue
SETS.append(practice_set(
    module=MODULE, topic=ADT,
    title="Queues and circular queues", lesson="csc-queue-circular",
    questions=[
        Q("Which describes a queue?", "First in, first out", [
            ("Last in, first out", "That is a stack."),
            ("Items are removed from the rear", "Items join at the rear and leave from the front."),
            ("Items are kept in sorted order", "A queue keeps arrival order, not sorted order.")], 2,
          [S("Recall", text="Items join at the rear and leave from the front: FIFO.")],
          "Queue (FIFO)", "Recall", "Think of people at a ticket window."),
        Q("A circular queue has SIZE = 6 and rear = 5. After one enqueue, what is rear?", "0", [
            ("5", "rear must move on by one place."),
            ("6", "Index 6 does not exist in an array of size 6."),
            ("1", "That would be after two enqueues.")], 0,
          [S("Apply the formula", math=r"(5 + 1) \bmod 6 = 0")],
          "Mod operator", "Calculation", "Use (rear + 1) mod SIZE."),
        NUM("A circular queue of size 8 has front = 6 and count = 4. What is the index of the rear item?", 1,
            steps=[S("Formula", math=r"\text{rear} = (6 + 4 - 1) \bmod 8"), S("Compute", math=r"9 \bmod 8 = 1"), S("Check", text="The items are at indexes 6, 7, 0 and 1.")],
            concept="Pointer arithmetic", skill="Calculation", hint="The last item is count - 1 places after the front, wrapping round."),
        Q("Which test shows that a circular queue (with a count variable) is full?", "count = SIZE", [
            ("rear = SIZE - 1", "The rear can be at the last index while there is still room at the start."),
            ("front = 0", "The front can be at index 0 without the queue being full."),
            ("front = rear", "This can occur when the queue holds exactly one item.")], 3,
          [S("Reason", text="The count records how many places are used, so the queue is full exactly when it equals the number of places.")],
          "Full and empty tests", "Concept", "How many items does a full queue hold?"),
        Q("A circular queue of size 3 is empty. Enqueue X, Y, Z, dequeue, then enqueue W. In which index is W stored?", "0", [
            ("1", "Index 1 holds Y."),
            ("2", "Index 2 holds Z, the last item before the wrap."),
            ("3", "Index 3 does not exist in an array of size 3.")], 1,
          [S("Trace", text="X, Y, Z are in 0, 1, 2 with rear = 2. Dequeue removes X (front = 1). Enqueue W: rear = (2 + 1) mod 3 = 0, so W goes in index 0.")],
          "Tracing a circular queue", "Application", "Where does rear go after index 2?"),
        Q("Why does a simple (linear) array queue waste space?", "Free places at the start are never reused once the rear reaches the end", [
            ("It can only hold one item", "It can hold as many items as the array size."),
            ("Dequeue deletes the array", "Dequeue just moves the front pointer."),
            ("It stores each item twice", "Each item is stored once.")], 2,
          [S("Example", text="After enqueues fill the array and two dequeues, the first two places are free but the rear cannot move past the end.")],
          "Circular queue", "Concept", "What happens to the places freed by dequeue?"),
        Q("A circular queue of size 4 is empty. Enqueue 1, 2, 3, 4; dequeue twice; enqueue 5. Which gives front, rear and count?", "front 2, rear 0, count 3", [
            ("front 0, rear 0, count 3", "front moved on after the two dequeues, so it is 2."),
            ("front 2, rear 4, count 3", "rear wraps: (3 + 1) mod 4 = 0, not 4."),
            ("front 2, rear 0, count 4", "Two items were removed and one added to the 4, so count is 3.")], 0,
          [S("Four enqueues", text="front 0, rear 3, count 4."), S("Two dequeues", text="front 2, count 2."), S("Enqueue 5", text="rear = (3 + 1) mod 4 = 0, count 3.")],
          "Tracing a circular queue", "Application", "Update all three variables after each operation."),
        NUM("A circular queue of size 10 has front = 8 and count = 5. At which index will the next item be stored?", 3,
            steps=[S("Rear", math=r"(8 + 5 - 1) \bmod 10 = 2"), S("Next", math=r"(2 + 1) \bmod 10 = 3")],
            concept="Pointer arithmetic", skill="Calculation", hint="Find the rear first, then move one place on."),
    ]))

# ------------------------------------------------------------------ 3. Linked lists
SETS.append(practice_set(
    module=MODULE, topic=ADT,
    title="Singly and doubly linked lists", lesson="csc-linked-lists",
    questions=[
        Q("What does a node of a singly linked list contain?", "A data value and a pointer to the next node", [
            ("Only a data value", "Without a pointer there would be no link to the next node."),
            ("Two data values", "A node holds one data item and its link."),
            ("A pointer to the previous node only", "That describes the extra pointer of a doubly linked list.")], 0,
          [S("Recall", text="Data plus next pointer.")],
          "Node and pointer", "Recall", "What links a node to the rest of the list?"),
        Q("In a singly linked list, what does a next pointer of null (or -1) mean?", "This node is the last node", [
            ("This node is the first node", "The first node is found from the start pointer."),
            ("The node has been deleted", "A deleted node is bypassed, not marked with null."),
            ("The node holds the value zero", "null is an empty pointer, not a data value.")], 1,
          [S("Reason", text="There is no node after it, so the next pointer is empty.")],
          "Null pointer", "Concept", "What comes after the last node?"),
        Q("Which is an advantage of a linked list over an array?", "Insertion needs no shifting of other items", [
            ("Direct access to the nth item", "That is an array strength; a list must be walked."),
            ("Uses less memory per item", "Each node also stores a pointer."),
            ("Items are always sorted", "A linked list keeps whatever order it was given.")], 2,
          [S("Reason", text="Inserting changes pointers only; in an array the later items must be shifted.")],
          "Linked list versus array", "Concept", "What must an array do to make room?"),
        Q("A list is stored as data = [5, 12, 20, 31], next = [1, 2, 3, -1], start = 0. Which is the third item of the list?", "20", [
            ("12", "12 is the second item."),
            ("2", "2 is a pointer value, not data."),
            ("31", "31 is the fourth item.")], 3,
          [S("Follow the pointers", text="start 0 gives 5, next[0] = 1 gives 12, next[1] = 2 gives 20.")],
          "Following pointers", "Application", "Start at index 0 and follow next twice."),
        NUM("Same arrays as in the last question. The value 15 is stored at free index 4 and inserted between 12 (index 1) and 20 (index 2). What value is given to next[4]?", 2,
            steps=[S("Link new to the rest", text="next[4] = next[1] = 2, so 15 points to 20."), S("Then", text="next[1] = 4, so 12 points to 15.")],
            concept="Insertion", skill="Application", hint="The new node must point where the previous node used to point."),
        Q("Same arrays again (5, 12, 20, 31). To delete the node holding 12 (index 1), which change is made?", "next[0] is set to 2", [
            ("next[1] is set to -1", "That would cut off 20 and 31 and does not remove 12 from the path."),
            ("next[2] is set to 0", "That makes the list loop back to 5."),
            ("data[1] is set to 0", "The node would still be on the path with a wrong value.")], 1,
          [S("Bypass", text="The predecessor of 12 is the node at index 0. Set next[0] = next[1] = 2 so 5 points straight to 20.")],
          "Deletion", "Application", "Which node must now point somewhere else?"),
        Q("What does a doubly linked list have that a singly linked list does not?", "A pointer to the previous node in each node", [
            ("A start pointer", "Both kinds need a start pointer."),
            ("Sorted items", "Order is not part of the definition."),
            ("Direct access by index", "Neither kind gives direct access.")], 2,
          [S("Reason", text="The previous pointer allows traversal backwards, at the cost of extra memory.")],
          "Doubly linked list", "Concept", "Think about moving backwards."),
        Q("To insert a new node N after node A in a singly linked list, which order is correct?", "N.next = A.next, then A.next = N", [
            ("A.next = N, then N.next = A.next", "After the first step A.next is N itself, so N would point to itself and the rest is lost."),
            ("N.next = A, then A.next = N", "N would point back to A, creating a loop."),
            ("A.next = null, then A.next = N", "This cuts off the rest of the list.")], 3,
          [S("Save the rest first", text="N.next takes the old pointer of A, then A.next is changed to N.")],
          "Order of pointer changes", "Reasoning", "Which pointer must be saved before it is overwritten?"),
    ]))

# ------------------------------------------------------------------ 4. BST insertion and search
SETS.append(practice_set(
    module=MODULE, topic=ADT,
    title="Building and searching a binary search tree", lesson="csc-bst-insert-search",
    questions=[
        Q("What is the rule of a binary search tree?", "Left subtree keys are smaller and right subtree keys are larger than the node", [
            ("Every node has exactly two children", "Nodes may have zero, one or two children."),
            ("Left subtree keys are larger than the node", "That reverses the rule."),
            ("Keys are stored in the order inserted", "Position depends on key values, not arrival order.")], 0,
          [S("Recall", text="Smaller keys go left, larger keys go right, at every node.")],
          "Binary search tree rule", "Recall", "Which side holds smaller keys?"),
        Q("Keys 8, 3, 10, 1, 6 are inserted into an empty BST in that order. What is the left child of the root?", "3", [
            ("1", "1 is smaller than 3, so it is the left child of 3."),
            ("10", "10 is larger than 8, so it goes to the right."),
            ("6", "6 is in the left subtree but sits below 3.")], 1,
          [S("Trace", text="8 is the root. 3 < 8 goes left. 10 goes right. 1 goes left of 3. 6 goes right of 3.")],
          "Insertion", "Application", "Compare each key with the root first."),
        NUM("Keys 10, 20, 30, 40, 50 are inserted in that order into an empty BST. What is the height of the tree (number of nodes on the longest path)?", 5,
            steps=[S("Each key is larger than all before it", text="Every key goes to the right of the previous one."), S("Chain", text="The tree is a chain of 5 nodes: height 5.")],
            concept="Insertion order and height", skill="Reasoning", hint="Where does each new larger key go?"),
        NUM("In the tree built from 8, 3, 10, 1, 6, how many comparisons are needed to find 6?", 3,
            steps=[S("Path", text="Compare with 8 (go left), with 3 (go right), with 6 (found)."), S("Count", text="3 comparisons.")],
            concept="Searching a BST", skill="Calculation", hint="Follow the path from the root and count the nodes visited."),
        Q("Keys 25, 15, 35, 10, 20, 30, 40 are inserted in that order. How many leaves does the tree have?", "4", [
            ("3", "The nodes 10, 20, 30 and 40 are all leaves; 3 misses one."),
            ("5", "The root and the two nodes 15 and 35 each have children."),
            ("7", "Only nodes with no children are leaves.")], 2,
          [S("Build", text="25 is the root. 15 and 35 are its children. 10 and 20 are the children of 15; 30 and 40 are the children of 35."), S("Leaves", text="10, 20, 30, 40: four leaves.")],
          "Leaves and structure", "Application", "A leaf has no children."),
        Q("Why is it a poor idea to build a BST by inserting keys that are already sorted?", "The tree becomes a chain, so searching is as slow as in a list", [
            ("The keys cannot be stored", "A BST can store any keys."),
            ("The root is lost", "The root is simply the first key."),
            ("Duplicate keys appear", "Sorting does not create duplicates.")], 3,
          [S("Reason", text="Each new key goes to the same side, so the height is n and a search can take n comparisons.")],
          "Balanced and degenerate trees", "Reasoning", "What shape results when every key goes right?"),
        NUM("A BST has root 40, left child 25, right child 60, and 50 as the left child of 60. How many comparisons are made in the unsuccessful search for 55?", 3,
            steps=[S("Path", text="55 > 40: right to 60. 55 < 60: left to 50. 55 > 50: right of 50, which is empty."), S("Count", text="Compared with 40, 60 and 50: 3 comparisons.")],
            concept="Searching a BST", skill="Calculation", hint="Count only the nodes you compare with."),
        Q("Which insertion order gives a perfectly balanced BST of height 3 from the keys 1 to 7?", "4, 2, 6, 1, 3, 5, 7", [
            ("1, 2, 3, 4, 5, 6, 7", "Sorted order gives a chain of height 7."),
            ("7, 6, 5, 4, 3, 2, 1", "Reverse order gives a chain on the left of height 7."),
            ("1, 7, 2, 6, 3, 5, 4", "This zig-zag order gives a tree of height 7 (each key goes deeper).")], 0,
          [S("Choose the middle key as root", text="4 is the root, 2 and 6 are its children, 1, 3, 5, 7 are the leaves: height 3.")],
          "Insertion order and height", "Reasoning", "Put the middle value first."),
    ]))

# ------------------------------------------------------------------ 5. BST traversals and deletion
SETS.append(practice_set(
    module=MODULE, topic=ADT,
    title="Tree traversals and deleting from a BST", lesson="csc-bst-traversal-deletion",
    questions=[
        Q("Which traversal of a binary search tree gives the keys in ascending order?", "In-order", [
            ("Pre-order", "Pre-order visits the node before its subtrees, so the root comes first."),
            ("Post-order", "Post-order visits the node last, so the root comes last."),
            ("Level by level only", "Level order is not one of the three depth-first traversals and is not sorted either.")], 0,
          [S("Reason", text="In-order does left subtree, node, right subtree, and the BST rule puts smaller keys on the left.")],
          "In-order traversal", "Recall", "Which traversal visits the node between its two subtrees?"),
        Q("A BST is built by inserting 40, 20, 60, 10, 30, 50, 70. What is its pre-order traversal?", "40, 20, 10, 30, 60, 50, 70", [
            ("10, 20, 30, 40, 50, 60, 70", "That is the in-order traversal."),
            ("10, 30, 20, 50, 70, 60, 40", "That is the post-order traversal."),
            ("40, 20, 60, 10, 30, 50, 70", "That is the insertion order (level by level), not pre-order.")], 1,
          [S("Pre-order", text="Node, left, right: 40, then the left subtree (20, 10, 30), then the right subtree (60, 50, 70).")],
          "Pre-order traversal", "Application", "Visit the node first, then everything on its left, then right."),
        Q("For the same tree (40, 20, 60, 10, 30, 50, 70) what is the post-order traversal?", "10, 30, 20, 50, 70, 60, 40", [
            ("40, 20, 10, 30, 60, 50, 70", "That is pre-order."),
            ("10, 20, 30, 40, 50, 60, 70", "That is in-order."),
            ("40, 60, 70, 50, 20, 30, 10", "That is a reversed order of visiting, not post-order.")], 2,
          [S("Post-order", text="Left, right, node: 10, 30, then 20; 50, 70, then 60; then the root 40.")],
          "Post-order traversal", "Application", "The root is the very last node visited."),
        Q("Deleting a node that has exactly one child from a BST is done by", "making the node's parent point to that child", [
            ("removing the whole subtree", "That would delete the child too."),
            ("replacing it by the root", "The root is not related to this node's place."),
            ("setting its child to null", "That removes the child and keeps the node.")], 3,
          [S("Reason", text="The child can take the removed node's place because it already fits the ordering rule.")],
          "Deleting a node with one child", "Concept", "Where should the child hang after the node is gone?"),
        Q("In the tree built from 50, 30, 70, 20, 40, 60, 80, 35, what is the in-order successor of 50?", "60", [
            ("30", "30 is smaller than 50, so it is a predecessor side key."),
            ("70", "70 is the right child, but its left subtree holds the smaller key 60."),
            ("80", "80 is the largest key in the right subtree.")], 1,
          [S("Successor", text="Go right to 70 and then left as far as possible: 60.")],
          "In-order successor", "Application", "Right once, then left as far as possible."),
        Q("In the same tree, 30 (two children) is deleted using its in-order successor. What is the pre-order traversal afterwards?", "50, 35, 20, 40, 70, 60, 80", [
            ("50, 40, 20, 35, 70, 60, 80", "40 is not the successor; 35 is the smallest key in 30's right subtree."),
            ("50, 20, 40, 35, 70, 60, 80", "This just removes 30 and moves its left child up, losing the ordering rule."),
            ("50, 35, 20, 40, 35, 70, 60, 80", "The successor must be removed from its old place; 35 would appear twice.")], 3,
          [S("Successor of 30", text="Right to 40, then left to 35. 35 has no left child."), S("Copy and delete", text="Put 35 where 30 was, remove the old leaf 35. Pre-order: 50, 35, 20, 40, 70, 60, 80.")],
          "Deleting with two children", "Application", "Find the smallest key in 30's right subtree."),
        Q("The balanced BST from 40, 20, 60, 10, 30, 50, 70 loses its root 40 (two children), using the in-order successor. What is the new pre-order traversal?", "50, 20, 10, 30, 60, 70", [
            ("60, 20, 10, 30, 50, 70", "60 is the right child, not the successor. The successor is the leftmost node of the right subtree, 50."),
            ("20, 10, 30, 60, 50, 70", "The tree must keep a single root: 50 takes the root place."),
            ("50, 20, 10, 30, 60, 50, 70", "The old node 50 must be removed; it cannot appear twice.")], 2,
          [S("Successor", text="Right to 60, then left to 50 (a leaf)."), S("Copy and delete", text="The root becomes 50 and the old leaf 50 is removed. Pre-order: 50, 20, 10, 30, 60, 70.")],
          "Deleting with two children", "Application", "Right once, then as far left as possible."),
        Q("Which traversal of an expression tree gives the postfix form of the expression?", "Post-order", [
            ("Pre-order", "Pre-order gives the prefix form."),
            ("In-order", "In-order gives the usual infix order (without brackets)."),
            ("None of them", "Post-order does give postfix: operands are listed before their operator.")], 3,
          [S("Reason", text="Post-order visits left operand, right operand, then the operator: operands first, then the operator.")],
          "Post-order traversal", "Concept", "In postfix, where does the operator go?"),
    ]))

# ------------------------------------------------------------------ 6. Linear and binary search
SETS.append(practice_set(
    module=MODULE, topic=SS,
    title="Linear and binary search", lesson="csc-linear-binary-search",
    questions=[
        Q("Which condition must be true before binary search can be used?", "The data must be sorted", [
            ("The data must be numbers", "Binary search works on any ordered data such as names."),
            ("The list must have an odd number of items", "An even length only changes how mid is rounded."),
            ("The list must contain no duplicates", "Binary search can still find one matching item.")], 0,
          [S("Reason", text="Binary search discards half the list using the order of the items.")],
          "Binary search precondition", "Recall", "What lets the algorithm throw half the list away?"),
        NUM("What is the largest number of comparisons binary search needs on a sorted list of 31 items? (Use floor(log2 n) + 1.)", 5,
            steps=[S("Formula", math=r"\lfloor \log_2 31 \rfloor + 1 = 4 + 1"), S("Check", text="31 = 2^5 - 1: the range can be halved 5 times.")],
            concept="Comparisons in binary search", skill="Calculation", hint="How many times can 31 be halved?"),
        Q("A list has 250 items. What is the worst case for linear search?", "250 comparisons", [
            ("1 comparison", "That is the best case, when the target is first."),
            ("125 comparisons", "That is about the average when the target is present."),
            ("8 comparisons", "That is the worst case of binary search, not linear search.")], 1,
          [S("Reason", text="Linear search checks every item if the target is last or absent.")],
          "Linear search cases", "Concept", "Where could the target be to make the search as long as possible?"),
        Q("In a binary search, low = 0 and high = 9. What is mid, using integer division?", "4", [
            ("5", "(0 + 9) // 2 = 4, because the .5 is dropped."),
            ("4.5", "An index must be a whole number."),
            ("9", "9 is the value of high, not the middle.")], 2,
          [S("Compute", math=r"\lfloor (0 + 9) / 2 \rfloor = 4")],
          "Binary search trace", "Calculation", "Add low and high, then divide by two, dropping the fraction."),
        NUM("Binary search for 31 in 4, 9, 15, 22, 31, 38, 45, 53, 60, 72, 81, 90, 97, 104, 120 (indexes 0 to 14). How many comparisons are made?", 4,
            steps=[S("mid = 7", text="53 > 31: high = 6. (1)"), S("mid = 3", text="22 < 31: low = 4. (2)"), S("mid = 5", text="38 > 31: high = 4. (3)"), S("mid = 4", text="31 found. (4)")],
            concept="Binary search trace", skill="Calculation", hint="Start with mid = 7 and track low and high."),
        NUM("Binary search for 100 in the same 15-item list is not found. How many comparisons are made before the range is empty?", 4,
            steps=[S("mid 7", text="53 < 100: low = 8. (1)"), S("mid 11", text="90 < 100: low = 12. (2)"), S("mid 13", text="104 > 100: high = 12. (3)"), S("mid 12", text="97 < 100: low = 13. (4)"), S("Stop", text="low > high: not found.")],
            concept="Unsuccessful search", skill="Calculation", hint="Keep going until low is greater than high."),
        Q("In which situation is linear search a better choice than binary search?", "A short unsorted list searched once", [
            ("A huge sorted list searched many times", "Binary search is much faster here."),
            ("A sorted list of one million items", "Binary search needs about 20 comparisons."),
            ("A list that is searched thousands of times", "Sorting once and using binary search wins.")], 0,
          [S("Reason", text="Binary search needs sorted data, and sorting costs time. For one search on a small list, scanning is simpler and cheaper.")],
          "Choosing a search", "Reasoning", "Binary search needs a sorted list. What does it cost to sort?"),
        NUM("Binary search needs at most 10 comparisons on 1000 items and at most 20 on 1 000 000 items. How many more comparisons does the larger list need?", 10,
            steps=[S("Subtract", math=r"20 - 10 = 10"), S("Meaning", text="A list 1000 times longer needs only 10 more comparisons.")],
            concept="Comparisons in binary search", skill="Interpretation", hint="Subtract the two maximum counts."),
    ]))

# ------------------------------------------------------------------ 7. Bubble sort
SETS.append(practice_set(
    module=MODULE, topic=SS,
    title="Bubble sort passes and counts", lesson="csc-bubble-sort",
    questions=[
        Q("What does bubble sort compare and swap?", "Adjacent items", [
            ("The smallest and largest items", "That is not how bubble sort chooses its pairs."),
            ("Items at opposite ends of the list", "Only neighbouring items are compared."),
            ("Every item with every other item", "That is not needed; passes compare neighbours only.")], 1,
          [S("Recall", text="Each step compares an item with the next one and swaps if they are out of order.")],
          "Bubble sort", "Recall", "Think of how the largest value moves."),
        Q("What is the list after the first pass of bubble sort on 4, 8, 2, 6?", "4, 2, 6, 8", [
            ("2, 4, 6, 8", "One pass does not sort the whole list."),
            ("2, 8, 4, 6", "That is the result of the first pass of selection sort."),
            ("4, 8, 2, 6", "Several neighbouring pairs are out of order, so the list changes.")], 3,
          [S("Pass 1", text="4 and 8 stay. 8 and 2 swap. 8 and 6 swap.")],
          "Tracing bubble sort", "Application", "Carry the largest item to the end by comparing neighbours."),
        Q("What does a swapped flag allow bubble sort to do?", "Stop as soon as a pass makes no swaps", [
            ("Run in less memory", "The flag does not reduce memory."),
            ("Sort in descending order", "The flag does not change the direction."),
            ("Count the passes", "The flag is true or false, not a counter.")], 2,
          [S("Reason", text="No swaps in a whole pass means every neighbouring pair is in order, so the list is sorted.")],
          "Swapped flag", "Concept", "What does a pass with no swaps prove?"),
        NUM("How many comparisons does bubble sort (with a swapped flag) make on the already sorted list 1, 2, 3, 4, 5, 6?", 5,
            steps=[S("One pass", text="5 neighbouring pairs, none out of order."), S("Stop", text="swapped is False, so the sort stops after 5 comparisons.")],
            concept="Best case of bubble sort", skill="Calculation", hint="How many passes are needed?"),
        NUM("How many comparisons does bubble sort make on the reversed list 6, 5, 4, 3, 2, 1 (the inner loop shortens each pass)?", 15,
            steps=[S("Sum", math=r"5 + 4 + 3 + 2 + 1 = 15"), S("Formula", math=r"n(n - 1)/2 = 6 \times 5 / 2 = 15")],
            concept="Worst case of bubble sort", skill="Calculation", hint="Add the comparisons of each pass."),
        Q("Bubble sort is applied to 5, 1, 4, 2, 3. What is the list after the second pass?", "1, 2, 3, 4, 5", [
            ("1, 4, 2, 3, 5", "That is the list after the first pass only."),
            ("1, 2, 4, 3, 5", "The pair 4 and 3 is swapped in pass 2."),
            ("5, 1, 4, 2, 3", "That is the starting list.")], 3,
          [S("Pass 1", text="5 moves to the end: 1, 4, 2, 3, 5."), S("Pass 2", text="1 and 4 stay; 4 and 2 swap; 4 and 3 swap: 1, 2, 3, 4, 5.")],
          "Tracing bubble sort", "Application", "Do pass 1 fully, then pass 2 on the first four items."),
        NUM("How many swaps does bubble sort make to sort 3, 2, 1?", 3,
            steps=[S("Pass 1", text="3 and 2 swap: 2, 3, 1. 3 and 1 swap: 2, 1, 3."), S("Pass 2", text="2 and 1 swap: 1, 2, 3."), S("Total", text="3 swaps.")],
            concept="Counting swaps", skill="Calculation", hint="Write the list after every swap."),
        Q("What is the best-case time complexity of bubble sort with a swapped flag?", "O(n)", [
            ("O(1)", "At least one pass over the n items is always needed."),
            ("O(log n)", "That is the cost of binary search."),
            ("O(n squared)", "That is the worst case, not the best case.")], 0,
          [S("Reason", text="Sorted data needs one pass of n - 1 comparisons.")],
          "Complexity of bubble sort", "Concept", "How many passes does sorted data need?"),
    ]))

# ------------------------------------------------------------------ 8. Insertion and selection sort
SETS.append(practice_set(
    module=MODULE, topic=SS,
    title="Insertion sort and selection sort", lesson="csc-insertion-selection-sort",
    questions=[
        Q("What is the list after the first pass of selection sort on 9, 4, 7, 2?", "2, 4, 7, 9", [
            ("4, 9, 7, 2", "This is what the first step of bubble sort or insertion sort would give."),
            ("2, 9, 4, 7", "This moves 2 to the front by shifting the other items right, which is insertion sort. Selection sort makes one swap."),
            ("9, 4, 7, 2", "The list changes: the smallest item is swapped to the front.")], 3,
          [S("Pass 1", text="The smallest is 2 (index 3). Swap it with the first item 9: 2, 4, 7, 9.")],
          "Selection sort", "Application", "Find the minimum of the whole list."),
        Q("Insertion sort is applied to 8, 3, 5, 1. What is the list after the first two insertions?", "3, 5, 8, 1", [
            ("1, 3, 5, 8", "That is the finished list; two insertions leave 1 unsorted."),
            ("3, 8, 5, 1", "That is the list after only the first insertion."),
            ("8, 3, 5, 1", "The first two items are not in order, so the list changes.")], 2,
          [S("Insert 3", text="3, 8 | 5, 1."), S("Insert 5", text="5 passes 8 and stops after 3: 3, 5, 8 | 1.")],
          "Insertion sort", "Application", "Insert 3, then 5, into the sorted part on the left."),
        NUM("How many comparisons does selection sort make on 7 items?", 21,
            steps=[S("Sum", math=r"6 + 5 + 4 + 3 + 2 + 1 = 21"), S("Formula", math=r"n(n - 1)/2 = 7 \times 6 / 2 = 21")],
            concept="Comparisons in selection sort", skill="Calculation", hint="The unsorted part shrinks by one each pass."),
        NUM("How many shifts does insertion sort make on the reversed list 5, 4, 3, 2, 1?", 10,
            steps=[S("Each insertion", text="Items 4, 3, 2, 1 move past 1, 2, 3, 4 larger items."), S("Total", math=r"1 + 2 + 3 + 4 = 10")],
            concept="Insertion sort worst case", skill="Calculation", hint="How far does each new item move?"),
        Q("Which of these sorts is stable when written in the usual way?", "Insertion sort", [
            ("Selection sort", "Its long-distance swap can pass an equal item: 2a, 2b, 1 becomes 1, 2b, 2a."),
            ("Quick sort", "Partitioning swaps items across long distances, so equal items can change order."),
            ("None of them", "Insertion sort shifts only strictly larger items, so equal items keep their order.")], 1,
          [S("Reason", text="Insertion sort moves an item left only past larger items, so equal items keep their relative order.")],
          "Stable sort", "Concept", "Does the algorithm ever jump over an equal item?"),
        NUM("What is the largest number of swaps selection sort can make on 8 items?", 7,
            steps=[S("One swap per pass at most", text="There are n - 1 = 7 passes and each makes at most one swap."), S("Result", text="At most 7 swaps.")],
            concept="Swaps in selection sort", skill="Reasoning", hint="How many passes are there and how many swaps in each?"),
        Q("Which sort is quickest on a list that is already almost in order?", "Insertion sort", [
            ("Selection sort", "It always scans the whole unsorted part, so it takes n squared / 2 comparisons whatever the order."),
            ("Merge sort", "It still needs about n log n steps; insertion sort needs about n."),
            ("Binary search", "Binary search is a search, not a sort.")], 2,
          [S("Reason", text="With few items out of place each insertion moves a short way, so the total is close to n steps.")],
          "Choosing a simple sort", "Reasoning", "Which sort stops comparing as soon as an item is in place?"),
        NUM("Selection sort is applied to 5, 3, 8, 1. How many swaps are made when the list is sorted (a swap is made only when the minimum is not already in place)?", 2,
            steps=[S("Pass 1", text="Minimum 1 swaps with 5: 1, 3, 8, 5."), S("Pass 2", text="3 is already in place: no swap."), S("Pass 3", text="Minimum 5 swaps with 8: 1, 3, 5, 8."), S("Total", text="2 swaps.")],
            concept="Tracing selection sort", skill="Application", hint="Do the passes in order and skip the swap when the minimum is already in place."),
    ]))

# ------------------------------------------------------------------ 9. Merge sort
SETS.append(practice_set(
    module=MODULE, topic=SS,
    title="Merge sort and merging", lesson="csc-merge-sort",
    questions=[
        Q("What is the base case of merge sort?", "A list of 0 or 1 item", [
            ("A list of exactly two items", "Two items are still divided and merged."),
            ("A list that is already sorted", "Merge sort does not test this; it divides regardless."),
            ("A list of even length", "Length parity does not stop the recursion.")], 0,
          [S("Reason", text="A list of 0 or 1 item is already sorted, so no more dividing is needed.")],
          "Merge sort", "Recall", "What size of list needs no sorting?"),
        Q("Merge the sorted lists 2, 6 and 4, 8. What is the result?", "2, 4, 6, 8", [
            ("2, 6, 4, 8", "Joining the lists end to end does not merge them."),
            ("4, 8, 2, 6", "The second list was placed first, but neither is sorted overall."),
            ("2, 4, 8, 6", "The items 6 and 8 are in the wrong order.")], 1,
          [S("Merge", text="2 v 4 gives 2; 6 v 4 gives 4; 6 v 8 gives 6; then copy 8.")],
          "Merging", "Application", "Compare the front items repeatedly."),
        NUM("Merge 1, 4, 7 with 2, 3, 9. How many comparisons are made before the last item is copied across?", 5,
            steps=[S("Compare", text="1 v 2, 4 v 2, 4 v 3, 4 v 9, 7 v 9."), S("Copy", text="The left list is now empty and 9 is copied: 5 comparisons.")],
            concept="Merging", skill="Calculation", hint="List each comparison of two front items."),
        NUM("Merge sort splits a list of 16 items in halves down to single items. How many levels of merging are there?", 4,
            steps=[S("Halve", text="16, 8, 4, 2, 1: four halvings."), S("Merge", text="Four levels of merging build the list back up.")],
            concept="Levels of merge sort", skill="Calculation", hint="How many times can 16 be halved to reach 1?"),
        Q("Which is the extra-space cost of merge sort?", "O(n)", [
            ("O(1)", "That is the cost of in-place sorts such as bubble sort."),
            ("O(log n)", "That is the typical stack use of quick sort."),
            ("O(n squared)", "Merge sort does not build that much extra storage.")], 2,
          [S("Reason", text="The merged lists at each level together hold about n items.")],
          "Space of merge sort", "Concept", "Merging creates a new list."),
        NUM("How many comparisons does merge sort make in total on 5, 2, 9, 1? (Count only comparisons in merges.)", 5,
            steps=[S("Pairs", text="5, 2 merges to 2, 5 (1 comparison). 9, 1 merges to 1, 9 (1)."), S("Final merge", text="2 v 1, 2 v 9, 5 v 9, then 9 is copied: 3 comparisons."), S("Total", text="1 + 1 + 3 = 5.")],
            concept="Counting comparisons", skill="Calculation", hint="Count the comparisons of each merge, from the pairs upwards."),
        Q("What is the worst-case time complexity of merge sort?", "O(n log n)", [
            ("O(n)", "Each level needs about n comparisons and there are log n levels."),
            ("O(n squared)", "That is the worst case of the simple sorts and of quick sort with bad pivots."),
            ("O(log n)", "Every item must be handled at least once, so it cannot be this low.")], 0,
          [S("Reason", text="About log2 n levels, each handling n items.")],
          "Complexity of merge sort", "Recall", "Count levels and the work per level."),
        Q("Which explains why merge sort takes about n log n steps?", "There are about log2 n levels and each level handles about n items", [
            ("It compares every pair of items", "That would be about n squared."),
            ("It sorts in place with n passes", "It builds new lists and does not use n passes."),
            ("Each merge takes one step", "A merge handles all the items of its two lists.")], 3,
          [S("Reason", text="Halving gives log2 n levels; every level merges all items once.")],
          "Complexity of merge sort", "Reasoning", "Multiply the number of levels by the work per level."),
    ]))

# ------------------------------------------------------------------ 10. Quick sort
SETS.append(practice_set(
    module=MODULE, topic=SS,
    title="Quick sort: pivot and partition", lesson="csc-quick-sort",
    questions=[
        Q("What is the job of the pivot in quick sort?", "Items not greater than it go to its left and larger items to its right", [
            ("It is always the smallest item", "A pivot is any chosen item."),
            ("It is the item sorted last", "After partitioning the pivot is already in its final place."),
            ("It is the middle position of the list", "Its final position depends on its value.")], 1,
          [S("Reason", text="Partitioning splits the items around the pivot, which ends in its final place.")],
          "Pivot and partition", "Concept", "What does the partition step do around the pivot?"),
        Q("Partition 6, 1, 8, 3 using the last item as pivot. Which list results?", "1, 3, 8, 6", [
            ("1, 3, 6, 8", "That is the fully sorted list; one partition does not sort the right side."),
            ("3, 1, 8, 6", "The pivot 3 must come after the smaller item 1."),
            ("6, 1, 3, 8", "6 is greater than the pivot 3, so it cannot stay on its left.")], 2,
          [S("Partition", text="Only 1 is not greater than 3: it goes to the front. Then the pivot is swapped in after it: 1, 3, 8, 6.")],
          "Partition", "Application", "Which items are not greater than 3?"),
        NUM("Partition 10, 15, 5, 8, 12 with the last item as pivot. At which index does the pivot finish?", 3,
            steps=[S("Items not greater than 12", text="10, 5 and 8: three items."), S("Place", text="The pivot goes after them, at index 3. List: 10, 5, 8, 12, 15.")],
            concept="Partition", skill="Calculation", hint="Count the items not greater than the pivot."),
        Q("When does quick sort with the last item as pivot behave worst?", "When the list is already sorted", [
            ("When the list is in random order", "Random order gives fairly even splits."),
            ("When the list has duplicates", "Duplicates do not force uneven splits."),
            ("When the list has only a few items", "Short lists need only a few steps.")], 3,
          [S("Reason", text="The last item is the largest, so each partition removes only the pivot.")],
          "Worst case of quick sort", "Reasoning", "What happens if the pivot is the largest item every time?"),
        NUM("How many comparisons does quick sort (last item as pivot) make on the sorted list 1, 2, 3, 4?", 6,
            steps=[S("Partitions", text="Pivot 4 needs 3 comparisons, pivot 3 needs 2, pivot 2 needs 1."), S("Total", math=r"3 + 2 + 1 = 6")],
            concept="Worst case of quick sort", skill="Calculation", hint="Each partition shrinks the part by only one item."),
        Q("Partition 4, 9, 2, 7, 5 using the last item as pivot. What is the result?", "4, 2, 5, 7, 9 with the pivot 5 at index 2", [
            ("2, 4, 5, 7, 9 with the pivot 5 at index 2", "The partition does not reorder items on the same side of the pivot: 4 stays before 2."),
            ("4, 9, 2, 5, 7 with the pivot 5 at index 3", "The pivot's final index is 2, because only 4 and 2 are not greater than 5."),
            ("5, 4, 9, 2, 7 with the pivot 5 at index 0", "The pivot goes after the smaller items, not first.")], 0,
          [S("Trace", text="4 <= 5: stays. 9 > 5. 2 <= 5: swaps with 9: 4, 2, 9, 7, 5. 7 > 5. Place the pivot: swap with 9: 4, 2, 5, 7, 9.")],
          "Partition", "Application", "Move 4 and 2 into the left group, then place the pivot."),
        Q("What is the average-case time complexity of quick sort?", "O(n log n)", [
            ("O(n squared)", "That is the worst case when pivots are poor."),
            ("O(n)", "Each level costs about n and there are about log n levels."),
            ("O(log n)", "Every item must be looked at, so the cost is at least n.")], 1,
          [S("Reason", text="A typical pivot splits the part into two parts of similar size, giving about log2 n levels.")],
          "Complexity of quick sort", "Recall", "It has the same order as merge sort."),
        Q("After a partition returns pivot index p (low to high being the part), which recursive calls follow?", "Sort low to p - 1 and p + 1 to high", [
            ("Sort low to p and p to high", "The pivot is already in place and is not sorted again."),
            ("Sort low to high again", "That would repeat the same partition forever."),
            ("Sort only low to p - 1", "The right part also needs sorting.")], 2,
          [S("Reason", text="The pivot is final. Items on its left and its right are two smaller problems.")],
          "Recursion in quick sort", "Concept", "Where is the pivot after the partition?"),
    ]))

# ------------------------------------------------------------------ 11. Time complexity and Big-O
SETS.append(practice_set(
    module=MODULE, topic=CX,
    title="Big-O and growth rates", lesson="csc-time-complexity-big-o",
    questions=[
        Q("What does the time complexity of an algorithm describe?", "How the number of steps grows as the input size grows", [
            ("The exact number of seconds it takes", "Seconds depend on the machine and the language, so they are not used."),
            ("The number of lines in the program", "Program length is not the number of steps executed."),
            ("The amount of memory it needs", "That is space complexity.")], 3,
          [S("Recall", text="Time complexity counts basic steps as a function of the input size n.")],
          "Time complexity", "Recall", "It is about growth, not a stopwatch."),
        Q("An algorithm takes 4n squared + 3n steps. What is its Big-O?", "O(n squared)", [
            ("O(n)", "n is the smaller term; the dominant term is n squared."),
            ("O(4n squared)", "The constant 4 is dropped."),
            ("O(n cubed)", "There is no cubic term.")], 1,
          [S("Simplify", text="Drop the smaller term 3n and the constant 4.")],
          "Simplifying Big-O", "Application", "Keep the fastest-growing term and drop its constant."),
        Q("Which algorithm is O(log n)?", "Binary search on a sorted array", [
            ("Linear search", "Linear search is O(n)."),
            ("Selection sort", "Selection sort is O(n squared)."),
            ("Reading every item of a list", "That is O(n).")], 2,
          [S("Reason", text="Binary search halves the range at each comparison.")],
          "Classes of Big-O", "Recall", "Which one halves the problem at each step?"),
        NUM("An algorithm makes exactly n squared steps. How many steps does it make when n = 30?", 900,
            steps=[S("Square", math=r"30^2 = 900")],
            concept="Counting steps", skill="Calculation", hint="Multiply 30 by itself."),
        NUM("An O(n squared) algorithm takes some time on n items. By what factor does the number of steps grow when n is doubled?", 4,
            steps=[S("Replace n by 2n", math=r"(2n)^2 = 4n^2"), S("Factor", text="The steps are multiplied by 4.")],
            concept="Growth when n doubles", skill="Reasoning", hint="Replace n by 2n in n squared."),
        Q("Which growth rate is the fastest (the worst for large n)?", "O(2 to the n)", [
            ("O(n squared)", "Polynomial growth is slower than exponential growth."),
            ("O(n log n)", "This grows more slowly than n squared."),
            ("O(n)", "Linear growth is much slower than exponential growth.")], 0,
          [S("Reason", text="Adding one item to the input doubles an exponential cost.")],
          "Classes of Big-O", "Concept", "Which one doubles for each extra item?"),
        Q("Reading the element at index 7 of an array has time complexity", "O(1)", [
            ("O(n)", "The array can be accessed directly; the length does not matter."),
            ("O(log n)", "No halving happens: the address is computed directly."),
            ("O(7)", "Constants are not written in Big-O: it is O(1).")], 0,
          [S("Reason", text="Direct access takes the same number of steps whatever the size of the array.")],
          "Constant time", "Concept", "Does the array length change the work?"),
        NUM("How many times can n = 256 be halved (integer division) until n reaches 1?", 8,
            steps=[S("Halve", text="256, 128, 64, 32, 16, 8, 4, 2, 1: eight halvings."), S("Link", text="This is log2 256 = 8, so the loop is O(log n).")],
            concept="Logarithmic growth", skill="Calculation", hint="Count how many times you divide by 2."),
    ]))

# ------------------------------------------------------------------ 12. Analysing algorithms
SETS.append(practice_set(
    module=MODULE, topic=CX,
    title="Analysing code, space and choosing algorithms", lesson="csc-analysing-space-comparing",
    questions=[
        Q("A program contains one loop over n items followed by a second loop over n items. What is its time complexity?", "O(n)", [
            ("O(n squared)", "Loops one after the other are added (2n), not multiplied."),
            ("O(2n squared)", "There is no multiplication, and constants are dropped."),
            ("O(log n)", "Neither loop halves anything.")], 3,
          [S("Reason", text="n + n = 2n, and Big-O drops the constant 2.")],
          "Analysing loops", "Application", "Do sequential loops add or multiply?"),
        Q("A loop over n items contains another loop over n items. What is the time complexity?", "O(n squared)", [
            ("O(n)", "The inner loop runs completely for each outer pass."),
            ("O(2n)", "Nested loops multiply: n times n."),
            ("O(n log n)", "Neither loop halves anything.")], 1,
          [S("Reason", math=r"n \times n = n^2")],
          "Analysing loops", "Application", "Count the steps of the inner loop for each outer pass."),
        NUM("A loop: for i in range(n): for j in range(i + 1, n): count = count + 1. How many times does the statement run when n = 10?", 45,
            steps=[S("Inner counts", text="9, 8, 7, ..., 1, 0 times."), S("Sum", math=r"n(n - 1)/2 = 10 \times 9 / 2 = 45")],
            concept="Analysing loops", skill="Calculation", hint="The inner loop gets shorter on each pass."),
        Q("Which of these needs only O(1) extra space?", "Bubble sort of a list in place", [
            ("Merge sort of a list", "It builds new lists totalling about n items."),
            ("Making a copy of a list", "A copy holds n more items, so O(n)."),
            ("Storing every pair of items in a new list", "That holds about n squared items.")], 2,
          [S("Reason", text="Bubble sort only needs a temporary variable for swapping.")],
          "Space complexity", "Concept", "Which one works in place with a temporary variable?"),
        Q("What is the extra-space (auxiliary) complexity of merge sort?", "O(n)", [
            ("O(1)", "That is the cost of in-place sorts."),
            ("O(log n)", "That is the typical stack depth of quick sort."),
            ("O(n squared)", "Merge sort never stores that much.")], 3,
          [S("Reason", text="Merging creates new lists holding about n items.")],
          "Space complexity", "Concept", "Merging needs somewhere to put the result."),
        Q("The recursive function factorial(n) calls factorial(n - 1) until n is 1. What is its stack space?", "O(n)", [
            ("O(1)", "Each unfinished call stays on the stack, so the depth grows with n."),
            ("O(log n)", "The call depth falls by 1 each time, not by half."),
            ("O(n squared)", "There are only n calls on the stack at a time.")], 0,
          [S("Reason", text="n calls are waiting at the deepest point, each with its own frame.")],
          "Recursion cost", "Reasoning", "How deep does the chain of waiting calls become?"),
        NUM("The recursive function fib(n) (fib(n - 1) + fib(n - 2), with fib(0) = 0 and fib(1) = 1) is called as fib(5). How many calls to fib are made in total, counting the first?", 15,
            steps=[S("Calls for small n", text="fib(0) and fib(1): 1 call each. fib(2): 3. fib(3): 5. fib(4): 9."), S("fib(5)", math=r"1 + 9 + 5 = 15")],
            concept="Recursion cost", skill="Calculation", hint="calls(n) = 1 + calls(n - 1) + calls(n - 2)."),
        Q("A school re-sorts 50 almost sorted records each day on a small computer. Which sort is the most suitable?", "Insertion sort", [
            ("Selection sort", "It always makes about n squared / 2 comparisons even on nearly sorted data."),
            ("Quick sort with the last item as pivot", "Almost sorted data gives poor pivots and the n squared case."),
            ("Binary search", "Binary search finds items; it does not sort them.")], 1,
          [S("Reason", text="Insertion sort takes close to n steps on nearly sorted data and uses no extra memory.")],
          "Choosing an algorithm", "Application", "Which sort stops quickly when little is out of place?"),
    ]))
