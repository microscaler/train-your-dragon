# 🧠 Module 03 Practice: Fix Flawed Dataset Examples

In this self-paced activity, you'll review flawed instruction-output examples and correct them to make them suitable for model training.

---

## Instructions

For each flawed example below:

1. Identify what is incorrect or suboptimal
2. Rewrite it in a clean and usable form

Use the table to record before/after examples if desired.

---

### ❌ Example 1 (missing `output` key)

```json
{"instruction": "What is a coroutine in Python?"}
```

✅ Fix:

```json
{"instruction": "What is a coroutine in Python?", "output": "A coroutine is a special function that can pause and resume execution using the 'await' keyword..."}
```

---

### ❌ Example 2 (badly formatted output)

```json
{"instruction": "Show an async function", "output": "def fetch():\nawait fetch_data()"}
```

✅ Fix:

```json
{"instruction": "Show an async function", "output": "async def fetch():\n    await fetch_data()"}
```

---

### ❌ Example 3 (ambiguous instruction)

```json
{"instruction": "Make this better", "output": "print('Hello World')"}
```

✅ Fix:

```json
{"instruction": "Refactor this function to use async/await", "output": "async def greet():\n    print('Hello World')"}
```

---

### ❌ Example 4 (placeholder content)

```json
{"instruction": "Write a coroutine", "output": "<insert code here>"}
```

✅ Fix:

```json
{"instruction": "Write a coroutine to fetch a webpage", "output": "async def fetch_page(url):\n    response = await httpx.get(url)\n    return response.text"}
```

---

### ❌ Example 5 (missing fields)

```json
{"input": "some text"}
```

✅ Fix:

```json
{"instruction": "Explain why async code improves IO performance", "output": "Async code allows Python to handle IO-bound tasks concurrently..."}
```

---

### ❌ Example 6 (incomplete sentence)

```json
{"instruction": "Explain how to", "output": "..."}
```

✅ Fix:

```json
{"instruction": "Explain how to define a coroutine in Python", "output": "A coroutine is defined using 'async def', and is executed with 'await'."}
```

---

### ❌ Example 7 (format error – trailing comma)

```json
{"instruction": "Give an example of go! macro in Rust", "output": "go!(|| println!(\"hi\")),"}
```

✅ Fix:

```json
{"instruction": "Give an example of go! macro in Rust", "output": "go!(|| println!(\"hi\"));"}
```

---

### ❌ Example 8 (mixed fields)

```json
{"instruction": "Async Rust example", "completion": "fn main() {"}
```

✅ Fix:

```json
{"instruction": "Async Rust example", "output": "#[tokio::main]\nasync fn main() {\n    println!(\"hello\");\n}"}
```

---

### ❌ Example 9 (off-topic)

```json
{"instruction": "How to cook spaghetti?", "output": "Boil water..."}
```

✅ Fix:

```json
{"instruction": "How to handle async file IO in Python", "output": "Use aiofiles to open and read/write files asynchronously."}
```

---

### ❌ Example 10 (low signal-to-noise)

```json
{"instruction": "Tell me everything about coroutines, and maybe add something cool.", "output": "Okay, here is a lot of stuff..."}
```

✅ Fix:

```json
{"instruction": "Summarize what Python coroutines are and how they compare to threads.", "output": "Coroutines are lightweight concurrent units... They differ from threads by avoiding context switching..."}
```
