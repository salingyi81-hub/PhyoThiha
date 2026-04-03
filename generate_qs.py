import json
import random

questions = []

# --- STACK TEMPLATES ---
# Trace questions
for i in range(20):
    val_pool = random.sample(range(10, 99), 5)
    stack = []
    ops_str = ""
    for _ in range(4):
        op = random.choice(["Push", "Push", "Pop"])
        if op == "Push":
            v = val_pool.pop()
            stack.append(v)
            ops_str += f"S.push({v})\n"
        else:
            if stack:
                stack.pop()
                ops_str += "S.pop()\n"
    
    if len(stack) == 0:
        ans = "Empty"
        wrong = ["10", "Error", "Undefined", "0"]
    else:
        ans = str(stack[-1])
        wrong = [str(x) for x in random.sample(range(10, 99), 4) if str(x) != ans]
    
    q = {
        "question": f"Given an empty Stack <code>S</code>, what is the top element after the following operations?\n<pre><code>{ops_str.strip()}</code></pre>",
        "options": [ans] + wrong[:3],
        "answer": 0
    }
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

stack_pseudo_codes = sorted([
    ("Push", "if top == MAX - 1:\n  print 'Overflow'\nelse:\n  top = top + 1\n  stack[top] = value"),
    ("Pop", "if top == -1:\n  print 'Underflow'\nelse:\n  value = stack[top]\n  top = top - 1\n  return value"),
    ("Peek", "if top == -1:\n  return null\nelse:\n  return stack[top]"),
    ("IsEmpty", "return top == -1"),
    ("IsFull", "return top == MAX - 1")
]*3)

for name, code in stack_pseudo_codes:
    q = {
        "question": f"Which Stack operation does the following pseudocode represent?\n<pre><code>{code}</code></pre>",
        "options": [name],
        "answer": 0
    }
    wrong = ["Push", "Pop", "Peek", "IsEmpty", "IsFull"]
    wrong.remove(name)
    q["options"] += random.sample(wrong, 3)
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

stack_theory = sorted([
    ("LIFO (Last-In, First-Out)", "What principle does a Stack data structure follow?"),
    ("Undo mechanism in text editors", "Which of the following is a common real-world application of a Stack?"),
    ("Function Call Management", "How does a compiler typically manage function calls and local variables?"),
    ("Push", "Which operation adds an element to the top of a Stack?"),
    ("Pop", "Which operation removes an element from the top of a Stack?"),
    ("Top", "What is the name of the pointer that tracks the uppermost element in a Stack?"),
    ("Overflow", "What error occurs when trying to Push to a full Stack?"),
    ("Underflow", "What error occurs when trying to Pop from an empty Stack?")
]*2)

for ans, txt in stack_theory[:15]:
    q = {
        "question": txt,
        "options": [ans],
        "answer": 0
    }
    wrong = ["FIFO (First-In, First-Out)", "Queue", "Enqueue", "Dequeue", "Underflow", "Overflow", "Front", "Rear", "Memory Leak", "CPU Scheduling"]
    if ans in wrong: wrong.remove(ans)
    q["options"] += random.sample(wrong, 3)
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

# --- QUEUE TEMPLATES ---
for i in range(20):
    val_pool = random.sample(range(10, 99), 5)
    queue = []
    ops_str = ""
    for _ in range(4):
        op = random.choice(["Enqueue", "Enqueue", "Dequeue"])
        if op == "Enqueue":
            v = val_pool.pop()
            queue.append(v)
            ops_str += f"Q.enqueue({v})\n"
        else:
            if queue:
                queue.pop(0)
                ops_str += "Q.dequeue()\n"
    
    if len(queue) == 0:
        ans = "Empty"
        wrong = ["10", "Error", "Undefined", "0"]
    else:
        ans = str(queue[0])
        wrong = [str(x) for x in random.sample(range(10, 99), 4) if str(x) != ans]
    
    q = {
        "question": f"Given an empty Queue <code>Q</code>, what is the front element after the following operations?\n<pre><code>{ops_str.strip()}</code></pre>",
        "options": [ans] + wrong[:3],
        "answer": 0
    }
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

queue_pseudo_codes = sorted([
    ("Enqueue", "if rear == MAX - 1:\n  print 'Overflow'\nelse:\n  if front == -1: front = 0\n  rear = rear + 1\n  queue[rear] = value"),
    ("Dequeue", "if front == -1 or front > rear:\n  print 'Underflow'\nelse:\n  value = queue[front]\n  front = front + 1\n  return value"),
    ("Peek", "if front == -1 or front > rear:\n  return null\nelse:\n  return queue[front]"),
    ("IsEmpty", "return front == -1 or front > rear"),
    ("IsFull", "return rear == MAX - 1")
]*3)

for name, code in queue_pseudo_codes:
    q = {
        "question": f"Which Queue operation does the following pseudocode represent?\n<pre><code>{code}</code></pre>",
        "options": [name],
        "answer": 0
    }
    wrong = ["Enqueue", "Dequeue", "Peek", "IsEmpty", "IsFull"]
    wrong.remove(name)
    q["options"] += random.sample(wrong, 3)
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

queue_theory = sorted([
    ("FIFO (First-In, First-Out)", "What principle does a Queue data structure follow?"),
    ("Task Scheduling", "Which of the following is a common real-world application of a Queue?"),
    ("Print Spooling", "Which scenario is best modeled by a Queue?"),
    ("Enqueue", "Which operation adds an element to the back of a Queue?"),
    ("Dequeue", "Which operation removes an element from the front of a Queue?"),
    ("Front", "What is the name of the pointer that tracks the first element to be removed in a Queue?"),
    ("Rear", "What is the name of the pointer that tracks where the next element will be added in a Queue?")
]*3)

for ans, txt in queue_theory[:15]:
    q = {
        "question": txt,
        "options": [ans],
        "answer": 0
    }
    wrong = ["LIFO (Last-In, First-Out)", "Stack", "Push", "Pop", "Top", "Browser History", "Undo feature"]
    if ans in wrong: wrong.remove(ans)
    q["options"] += random.sample(wrong, 3)
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

# --- CIRCULAR QUEUE TEMPLATES ---
for i in range(20):
    MAX = random.randint(3, 5)
    ops_str = f"MAX = {MAX}\n"
    q_list = []
    
    for _ in range(5):
        op = random.choice(["Enqueue", "Enqueue", "Dequeue"])
        if op == "Enqueue" and len(q_list) < MAX:
            v = random.randint(10, 99)
            q_list.append(v)
            ops_str += f"CQ.enqueue({v})\n"
        elif op == "Dequeue" and len(q_list) > 0:
            q_list.pop(0)
            ops_str += "CQ.dequeue()\n"
    
    if len(q_list) == 0:
        ans = "Empty"
        wrong = ["Error", "Undefined", "0", "10"]
    else:
        ans = str(len(q_list))
        wrong = [str(x) for x in range(10) if str(x) != ans]
    
    qq = {
        "question": f"Given an empty Circular Queue <code>CQ</code> with capacity {MAX}, how many elements are in it after these operations?\n<pre><code>{ops_str.strip()}</code></pre>",
        "options": [ans] + wrong[:3],
        "answer": 0
    }
    opts = qq["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    qq["answer"] = opts.index(correct_val)
    questions.append(qq)

cq_pseudo_codes = sorted([
    ("Enqueue", "if (rear + 1) % MAX == front:\n  print 'Overflow'\nelse:\n  if front == -1: front = 0\n  rear = (rear + 1) % MAX\n  cqueue[rear] = value"),
    ("Dequeue", "if front == -1:\n  print 'Underflow'\nelse:\n  value = cqueue[front]\n  if front == rear:\n    front = -1; rear = -1\n  else:\n    front = (front + 1) % MAX\n  return value"),
    ("IsFull", "return (rear + 1) % MAX == front"),
    ("IsEmpty", "return front == -1"),
    ("Next Position", "return (current + 1) % MAX")
]*3)

for name, code in cq_pseudo_codes:
    q = {
        "question": f"Which Circular Queue concept does the following pseudocode represent?\n<pre><code>{code}</code></pre>",
        "options": [name],
        "answer": 0
    }
    wrong = ["Enqueue", "Dequeue", "IsFull", "IsEmpty", "Next Position"]
    wrong.remove(name)
    q["options"] += random.sample(wrong, 3)
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

cq_theory = sorted([
    ("To efficiently use array space", "What is the primary advantage of a Circular Queue over a linear Queue?"),
    ("(rear + 1) % MAX == front", "What is the condition for a Circular Queue being full?"),
    ("front == -1", "What is the condition for a Circular Queue being empty?"),
    ("Ring Buffer", "What is another common name for a Circular Queue?"),
    ("Modulo division (%)", "What mathematical operator is essential for wrapping around in a Circular Queue?"),
    ("It avoids shifting elements", "Why is Dequeue more efficient in Circular Queue compared to a linear array shifting approach?")
]*3)

for ans, txt in cq_theory[:15]:
    q = {
        "question": txt,
        "options": [ans],
        "answer": 0
    }
    wrong = ["To increase maximum capacity dynamically", "rear == MAX - 1", "front == 0", "Stack Buffer", "Multiplication (*)", "It is not more efficient"]
    if ans in wrong: wrong.remove(ans)
    q["options"] += random.sample(wrong, 3)
    opts = q["options"]
    correct_val = opts[0]
    random.shuffle(opts)
    q["answer"] = opts.index(correct_val)
    questions.append(q)

all_qs = (questions + questions + questions)[:150]

out_str = "const questions = " + json.dumps(all_qs, indent=4) + ";\n"

# Rewrite quiz.js with new questions and innerHTML
with open('c:\\Users\\ASUS\\Desktop\\Stack tester\\quiz.js', 'r', encoding='utf-8') as f:
    orig = f.read()

# We extract the rest of quiz.js logic after '];'
logic_start = orig.find('let currentQuestionIndex = 0;')
if logic_start != -1:
    logic = orig[logic_start:]
    # Replace textContent with innerHTML
    logic = logic.replace('questionText.textContent', 'questionText.innerHTML')
    
    with open('c:\\Users\\ASUS\\Desktop\\Stack tester\\quiz.js', 'w', encoding='utf-8') as fw:
        fw.write(out_str + "\n" + logic)
else:
    print("Error finding logic part")

