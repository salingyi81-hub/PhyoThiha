import json
import random

questions = []

def make_q(topic, diff, text, ans, wrongs):
    q = {
        "topic": topic,
        "difficulty": diff,
        "question": text,
        "options": [ans] + wrongs[:3],
        "answer": 0
    }
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

def add_questions(topic, diff, count, generator_func):
    for i in range(count):
        generator_func()

# ----------------- STACK GENERATORS -----------------
def stack_basic():
    types = ["theory", "simple_trace"]
    t = random.choice(types)
    if t == "theory":
        pool = [
            ("What logical principle does a Stack inherently follow?", "LIFO (Last-In, First-Out)", ["FIFO", "LILO", "Random Access"]),
            ("Which pointer primarily manages a standard Stack?", "Top", ["Front", "Rear", "Head", "Tail"]),
            ("Adding an element to the top of a stack is referred to as:", "Push", ["Pop", "Enqueue", "Insert", "Peek"]),
            ("Removing an element from a stack is known as:", "Pop", ["Push", "Dequeue", "Delete", "Shift"]),
            ("Viewing the top element without removing it is called:", "Peek / Top", ["Pop", "Look", "Front", "Search"])
        ]
        q, a, w = random.choice(pool)
        make_q("Stack", "Basic", q, a, w + ["Unknown"])
    else:
        v1, v2 = random.randint(10,50), random.randint(51,99)
        q = f"Given an empty Stack S. You perform:<br><code>S.push({v1})</code><br><code>S.push({v2})</code><br><code>S.pop()</code><br>What is now at the top of the Stack?"
        make_q("Stack", "Basic", q, str(v1), [str(v2), "Empty", "Error", "0"])

def stack_inter():
    types = ["multi_trace", "pseudo", "applications"]
    t = random.choice(types)
    if t == "multi_trace":
        ops = []
        stack = []
        for _ in range(5):
            if random.random() < 0.6 or not stack:
                v = random.randint(10, 99)
                stack.append(v)
                ops.append(f"S.push({v})")
            else:
                stack.pop()
                ops.append("S.pop()")
        code = "<br>".join([f"<code>{o}</code>" for o in ops])
        ans = str(stack[-1]) if stack else "Empty"
        wrong = [str(x) for x in random.sample(range(10,99), 3)] + ["Error"]
        make_q("Stack", "Intermediate", f"Trace the following operations on an empty Stack S:<br>{code}<br>What is the final top element?", ans, wrong)
    elif t == "applications":
        pool = [
            ("Which of the following is an algorithm heavily reliant on Stacks?", "Depth-First Search (DFS)", ["Breadth-First Search (BFS)", "Binary Search", "Selection Sort"]),
            ("In evaluating arithmetic expressions, what notation effectively uses a Stack?", "Postfix (Reverse Polish)", ["Infix", "Prefix", "Polynomial notation"]),
            ("How does a system handle recursion?", "System Call Stack", ["Process Queue", "Circular Buffer", "Heap Area"])
        ]
        q, a, w = random.choice(pool)
        make_q("Stack", "Intermediate", q, a, w + ["None"])
    else:
        make_q("Stack", "Intermediate", "Analyze the pseudocode:<br><pre><code>if top == 0:\n  return null\nelse:\n  return arr[top]</code></pre><br>What is wrong with this Peek operation if array is 0-indexed?", "Top should be checked for -1, not 0.", ["It pops the element instead of peeking.", "Array indexing is out of bounds.", "Nothing is wrong.", "It causes an overflow."])

def stack_adv():
    t = random.choice(["loop_trace", "two_stacks", "expression"])
    if t == "loop_trace":
        start = random.randint(1, 5)
        ans = start + 3
        w = [str(ans + 1), str(ans - 1), str(ans * 2), str(start)]
        q = f"Predict the top element after executing this logic on an empty Stack S:<br><pre><code>for(i={start}; i<{start+3}; i++):\n  S.push(i)\n  S.push(i * 2)\n  S.pop()\nS.push(S.pop() + 1)</code></pre>"
        make_q("Stack", "Advanced", q, str(ans), w)
    elif t == "two_stacks":
        make_q("Stack", "Advanced", "When implementing two stacks efficiently inside a single array of size N, what are the optimal starting indices for their 'top' pointers?", "top1 = -1, top2 = N", ["top1 = 0, top2 = N/2", "top1 = -1, top2 = N-1", "top1 = 0, top2 = 1", "top1 = N/2, top2 = N"])
    else:
        make_q("Stack", "Advanced", "Which data property makes a stack ideal for balancing parentheses in compiler design?", "Its ability to defer resolving the most recently opened bracket until matched.", ["Its dynamic array resizing capability.", "Its O(1) random access property.", "Its FIFO tracking logic.", "Its recursive memory allocation overhead."])


# ----------------- QUEUE GENERATORS -----------------
def q_basic():
    if random.choice([True, False]):
        pool = [
            ("What logical principle does a linear Queue follow?", "FIFO (First-In, First-Out)", ["LIFO", "FILO", "Random Access"]),
            ("Which operations are primarily associated with Queues?", "Enqueue & Dequeue", ["Push & Pop", "Insert & Read", "Add & Remove"]),
            ("In a standard Queue, where are new elements added?", "Rear (Tail)", ["Front", "Top", "Middle", "Anywhere"]),
            ("In a standard Queue, from where are elements removed?", "Front (Head)", ["Rear", "Top", "Bottom", "Anywhere"])
        ]
        q, a, w = random.choice(pool)
        make_q("Queue", "Basic", q, a, w + ["Unknown"])
    else:
        v1, v2 = random.randint(10,50), random.randint(51,99)
        q = f"Given an empty Queue Q. You perform:<br><code>Q.enqueue({v1})</code><br><code>Q.enqueue({v2})</code><br><code>Q.dequeue()</code><br>What element is currently at the front of the Queue?"
        make_q("Queue", "Basic", q, str(v2), [str(v1), "Empty", "Error", "0"])

def q_inter():
    if random.choice([True, False]):
        ops = []
        q_list = []
        for _ in range(5):
            if random.random() < 0.6 or not q_list:
                v = random.randint(10, 99)
                q_list.append(v)
                ops.append(f"Q.enqueue({v})")
            else:
                q_list.pop(0)
                ops.append("Q.dequeue()")
        code = "<br>".join([f"<code>{o}</code>" for o in ops])
        ans = str(q_list[0]) if q_list else "Empty"
        wrong = [str(x) for x in random.sample(range(10,99), 3)] + ["Error"]
        make_q("Queue", "Intermediate", f"Trace the following operations on an empty Queue Q:<br>{code}<br>What is the front element now?", ans, wrong)
    else:
        make_q("Queue", "Intermediate", "Consider a linear queue using an array. After repeatedly enqueueing and dequeueing elements until the 'rear' pointer reaches the maximum index, what problem occurs?", "False Overflow: Cannot enqueue even if there are empty spaces at the front.", ["Underflow: The queue prematurely empties.", "Memory Leak: RAM is continuously consumed.", "Segmentation Fault.", "Deadlock: Dequeue gets stuck."])

def q_adv():
    t = random.choice(["pointers", "two_stacks"])
    if t == "pointers":
        max_size = 5
        make_q("Queue", "Advanced", f"An array-based Linear Queue of size {max_size} starts with `front = -1`, `rear = -1`. We Enqueue 3 items, Dequeue 2 items, Enqueue 2 items. What are the current values of `front` and `rear`?", "front = 2, rear = 4", ["front = 1, rear = 5", "front = 2, rear = 3", "front = 0, rear = 4", "front = 3, rear = 5"])
    else:
        make_q("Queue", "Advanced", "If you implement a Queue using two Stacks (S1 and S2), what is the worst-case time complexity of the Dequeue operation?", "O(N) - when elements need to be transferred from S1 to S2.", ["O(1) - it involves just one pop.", "O(log N) - binary tree shifting is used.", "O(N^2) - due to nested loops.", "O(N log N)"])


# ------------- CIRCULAR QUEUE GENERATORS -------------
def cq_basic():
    if random.choice([True, False]):
        pool = [
            ("Why was the Circular Queue invented?", "To solve the 'False Overflow' problem in linear array queues.", ["To use LIFO efficiently.", "To perform random access faster.", "To reduce Time Complexity to O(1)."]),
            ("What is another term for a Circular Queue?", "Ring Buffer", ["Circular Stack", "Loop Queue", "Linked List", "Priority Buffer"]),
            ("What mathematical operator is critical for Circular Queues?", "Modulo (%)", ["Division (/)", "Power (^)", "Bitwise XOR", "Multiplication (*)"])
        ]
        q, a, w = random.choice(pool)
        make_q("Circular Queue", "Basic", q, a, w + ["None"])
    else:
        make_q("Circular Queue", "Basic", "In a Circular Queue of size MAX, if `rear == MAX - 1`, what will the `rear` become on the next Enqueue (assuming it's not full)?", "0", ["MAX", "MAX + 1", "-1", "1"])

def cq_inter():
    if random.choice([True, False]):
        make_q("Circular Queue", "Intermediate", "In a Circular Queue of size N, what is the standard condition to check if it is FULL?", "(rear + 1) % N == front", ["rear == N - 1", "front == (rear + 1) % N", "front == -1 && rear == N - 1", "(front + 1) % N == rear"])
    else:
        make_q("Circular Queue", "Intermediate", "In a Circular Queue, when does `front` get reset to -1?", "When the last element is dequeued, making the queue completely empty.", ["When `front` reaches the end of the array (N-1).", "When `rear` wraps around to 0.", "It never gets reset, it only increments.", "During memory garbage collection."])

def cq_adv():
    MAX = random.randint(4, 6)
    q_str = f"Given an empty Circular Queue `CQ` with MAX = {MAX}, `front = -1`, `rear = -1`.<br>Operations:<br>1. Enqueue 4 items.<br>2. Dequeue 2 items.<br>3. Enqueue 3 items.<br>What is the final state of `front` and `rear` pointers?"
    
    # simulate
    front, rear = -1, -1
    for _ in range(4):
        if front == -1: front = 0
        rear = (rear + 1) % MAX
    for _ in range(2):
        if front == rear: front, rear = -1, -1
        else: front = (front + 1) % MAX
    for _ in range(3):
        if (rear + 1) % MAX != front: # if not full
            if front == -1: front = 0
            rear = (rear + 1) % MAX
            
    ans = f"front = {front}, rear = {rear}"
    w1 = f"front = {(front+1)%MAX}, rear = {rear}"
    w2 = f"front = {front}, rear = {(rear+1)%MAX}"
    w3 = f"front = {front}, rear = {rear-1 if rear >0 else MAX-1}"
    make_q("Circular Queue", "Advanced", q_str, ans, [w1, w2, w3, "Error Condition"])


add_questions("Stack", "Basic", 18, stack_basic)
add_questions("Stack", "Intermediate", 16, stack_inter)
add_questions("Stack", "Advanced", 16, stack_adv)

add_questions("Queue", "Basic", 18, q_basic)
add_questions("Queue", "Intermediate", 16, q_inter)
add_questions("Queue", "Advanced", 16, q_adv)

add_questions("Circular Queue", "Basic", 18, cq_basic)
add_questions("Circular Queue", "Intermediate", 16, cq_inter)
add_questions("Circular Queue", "Advanced", 16, cq_adv)

with open('generated_qs_levels.json', 'w') as f:
    json.dump((questions), f, indent=4)
