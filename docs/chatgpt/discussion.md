Certainly! Here's your full **coroutine-first prompt training dataset** in **Markdown format**, ready for copy-paste into your Unsloth workflow or documentation:

````markdown
# 🧠 Coroutine-First LLM Prompt Training Dataset (Unsloth Format)

Each prompt is structured for instruction-based fine-tuning using Unsloth. Rust examples use `may`, and Python examples focus on generator-based coroutines.

---

## 🔧 Python Coroutine Primitives

### ✅ Python OS-level coroutine scheduler

**Instruction:**
> Write a Python operating system that supports cooperative multitasking using coroutines.

**Output:**
```python
<INSERT pyos8.py CODE HERE>
````

---

### ✅ Coroutine log line filter

**Instruction:**

> Write a coroutine that filters lines from a log stream for a keyword and sends them to a printer coroutine.

**Output:**

```python
@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)
```

---

### ✅ Fan-out broadcast coroutine

**Instruction:**

> Design a fan-out coroutine pipeline that broadcasts items to multiple consumers.

**Output:**

```python
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
```

---

### ✅ Fan-in pipeline with shared sink

**Instruction:**

> Design a fan-in coroutine pipeline that merges multiple filters into a single output coroutine.

**Output:**

```python
f = open("access-log")
p = printer()
follow(f,
   broadcast([grep('python', p),
              grep('ply', p),
              grep('swig', p)])
)
```

---

## 🔧 Rust Coroutine Patterns

### ✅ Async/await coroutine dispatcher (Tokio)

**Instruction:**

> Write a Rust program that uses async/await for high concurrency and only uses threads for dispatching blocking tasks.

**Output:**

```rust
use tokio::task;
use std::time::Duration;

async fn lightweight_task(id: usize) {
    println!("Coroutine {} started", id);
    tokio::time::sleep(Duration::from_millis(100)).await;
    println!("Coroutine {} finished", id);
}

#[tokio::main]
async fn main() {
    for i in 0..10 {
        tokio::spawn(lightweight_task(i));
    }
    tokio::time::sleep(Duration::from_secs(1)).await;
}
```

---

### ✅ `may` coroutine loop

**Instruction:**

> Use the `may` crate to implement a coroutine scheduler that runs multiple coroutines cooperatively in Rust.

**Output:**

```rust
use may::coroutine;
use std::time::Duration;

fn main() {
    for i in 0..5 {
        coroutine::spawn(move || {
            println!("coroutine {} running", i);
            may::go!(|| {
                may::std::thread::sleep(Duration::from_millis(100));
                println!("coroutine {} finished", i);
            });
        });
    }
    may::config().set_io_workers(1);
}
```

---

### ✅ Pipeline with `may::sync::mpsc` channels

**Instruction:**

> Write a coroutine-based log filter pipeline in Rust using may::go and channels.

**Output:**

```rust
use may::go;
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();

    go!(move || {
        let lines = vec!["python is great", "nothing here", "ply is cool"];
        for line in lines {
            tx.send(line.to_string()).unwrap();
        }
    });

    go!(move || {
        while let Ok(line) = rx.recv() {
            if line.contains("python") {
                println!("Filtered: {}", line);
            }
        }
    });
}
```

---

### ✅ Coroutine cancellation in Python

**Instruction:**

> Create a coroutine system where tasks can be cancelled cooperatively in Python.

**Output:**

```python
class Cancelled(Exception): pass

@coroutine
def cancellable():
    try:
        while True:
            line = (yield)
            print(line)
    except Cancelled:
        print("Cancelled")

t = cancellable()
t.send("hello")
t.throw(Cancelled)
```

---

### ✅ Coroutine cancellation in Rust

**Instruction:**

> Add support for coroutine cancellation to an existing Rust may-based coroutine system.

**Output:**

```rust
use may::go;
use std::sync::{Arc, atomic::{AtomicBool, Ordering}};
use std::thread;
use std::time::Duration;

fn main() {
    let cancel_flag = Arc::new(AtomicBool::new(false));

    let flag = cancel_flag.clone();
    go!(move || {
        for i in 0..10 {
            if flag.load(Ordering::Relaxed) {
                println!("Cancelled at {}", i);
                return;
            }
            println!("Running {}", i);
            thread::sleep(Duration::from_millis(50));
        }
    });

    thread::sleep(Duration::from_millis(200));
    cancel_flag.store(true, Ordering::Relaxed);
}
```

---

### ✅ Multi-producer with `may::sync::mpsc`

**Instruction:**

> Demonstrate the use of may::sync::mpsc::channel to coordinate multiple producers and a single consumer.

**Output:**

```rust
use may::go;
use may::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();

    for i in 0..3 {
        let tx = tx.clone();
        go!(move || {
            tx.send(format!("message from producer {}", i)).unwrap();
        });
    }

    go!(move || {
        for _ in 0..3 {
            if let Ok(msg) = rx.recv() {
                println!("received: {}", msg);
            }
        }
    });
}
```

---

### ✅ `select!` macro for channel coordination

**Instruction:**

> Show how to use may's select! macro to wait on multiple channel receives.

**Output:**

```rust
use may::go;
use may::sync::mpsc::{channel, TryRecvError};
use may::select;

fn main() {
    let (tx1, rx1) = channel();
    let (tx2, rx2) = channel();

    go!(move || { tx1.send("from channel 1").unwrap(); });
    go!(move || { tx2.send("from channel 2").unwrap(); });

    go!(move || {
        for _ in 0..2 {
            select! {
                recv(rx1) -> msg => println!("Got {}", msg.unwrap()),
                recv(rx2) -> msg => println!("Got {}", msg.unwrap()),
            }
        }
    });
}
```

---

### ✅ Coroutine TCP echo server (full IO)

**Instruction:**

> Build a coroutine-based TCP echo server using may's tcp and io primitives.

**Output:**

```rust
use may::net::{TcpListener, TcpStream};
use may::go;
use std::io::{Read, Write};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    println!("Listening on port 8080");

    for stream in listener.incoming() {
        match stream {
            Ok(mut stream) => {
                go!(move || {
                    let mut buf = [0u8; 512];
                    loop {
                        let n = match stream.read(&mut buf) {
                            Ok(n) if n == 0 => return,
                            Ok(n) => n,
                            Err(_) => return,
                        };
                        stream.write_all(&buf[..n]).unwrap();
                    }
                });
            },
            Err(e) => eprintln!("Connection failed: {}", e),
        }
    }
}
```

---

## 🧪 Evaluation Prompts (No Code Output)

### 🔍 Coroutines vs Threads

**Instruction:**

> Compare the performance and suitability of using threads vs coroutines for handling 1000 concurrent network requests in Rust.

**Output:**
Coroutines are generally more efficient for IO-bound tasks. They consume less memory, have lower context-switch overhead, and scale better than OS threads. For 1000 concurrent connections, coroutines avoid the resource exhaustion risks of spawning 1000 threads.

---

### 🔍 IO-bound log watcher

**Instruction:**

> Which is more appropriate for building an IO-bound file watcher in Rust: spawning threads or using coroutines?

**Output:**
Coroutines are preferred. They are lighter, scale better, and integrate well with async file and IO APIs in Rust. Threads are overkill for many-watch use cases.

---

### 🔍 Cancellation strategies

**Instruction:**

> What are the advantages of coroutine cancellation via shared flags compared to terminating threads?

**Output:**
Flag-based cancellation allows graceful exits, avoids deadlocks, and enables cooperative termination. Threads may terminate unsafely while holding shared state.

---

### 🔍 select! macro benefit

**Instruction:**

> Explain why `select!` in the `may` crate helps improve coroutine coordination.

**Output:**
The `select!` macro lets coroutines wait on multiple channels concurrently, responding to whichever message arrives first. This improves responsiveness and simplifies reactive control flow.

---

### 🔍 Log filter strategy

**Instruction:**

> Should you use threads or coroutines for log stream filtering in Python or Rust?

**Output:**
Coroutines are ideal for log stream processing—low memory use, non-blocking behavior, and simple chaining make them more efficient than threads.

---

```

Would you like a downloadable `.md` or `.jsonl` export file for this as well?
```
