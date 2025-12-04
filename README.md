# Emotion-Aware Lyric Search Engine  
### Using Multi-Pattern KMP, Emotional Graphs, and Heuristic Optimization

---

## 1. Problem Definition

Traditional lyric-analysis systems rely on simple word counting or generic embeddings that do not provide algorithmic transparency, efficient search, or emotional explainability. These approaches struggle to produce precise emotional similarity rankings or scalable performance when datasets grow.

This project implements a fully algorithmic solution for emotional similarity search in song lyrics using:

- **KMP multipattern search** for exact pattern detection  
- **A weighted emotional graph** linking emotions to associated words  
- **Heuristic optimization (Simulated Annealing)** to refine emotional weights  
- **A lightweight trie structure** to organize lyric data  
- **A dataset of 30 diverse song lyrics** for benchmarking and evaluation  

The goal is to build a fast, explainable, and reproducible emotional search engine grounded in classical algorithms.

---

## 2. Research Question

**Can a system based exclusively on multi-pattern KMP search, an emotional graph, and heuristic optimization outperform traditional frequency-based emotional classification methods in both efficiency and precision?**

---

## 3. Hypothesis

*The combination of KMP multipattern search, a structured emotion–word graph, and Simulated Annealing for weight optimization will produce a more efficient (lower search latency, higher throughput) and more accurate (higher emotional precision/recall) classification system than classical frequency-based approaches.*

---

## 4. Algorithmic Justification

### KMP Algorithm
- Linear-time pattern matching  
- Excellent for repeated scanning of large texts  
- Transparent, deterministic, and explainable  

### Simulated Annealing
- Allows optimization of emotional weights  
- Reduces emotional classification error  
- Easy to implement and benchmark  

### Emotional Graph
- Encodes semantic relationships explicitly  
- Enables weighted emotional scoring  

### Trie Structure
- Lightweight storage of lyrics  
- Efficient access to songs  

---

## 5. System Architecture



---

## 6. Data Structures Implemented

- Trie for storing lyrics  
- Directed weighted emotional graph  
- KMP prefix table for pattern matching  
- Emotional score vector per song  

---

## 7. Algorithms Implemented

- **Multi-pattern KMP**  
- **Simulated Annealing** for weight optimization  
- **Heuristic scoring and ranking**  
- **(Optional) Parallel KMP version** for benchmarking  

---

## 8. Dataset

A custom dataset of **30 diverse songs** with varied emotional content was collected manually.  
Each `.txt` file contains the full lyrics for one song and is stored in:

/data/lyrics/song1.txt
/data/lyrics/song2.txt
...
/data/lyrics/song30.txt


This dataset allows:

- realistic performance benchmarking  
- emotional diversity (joy, sadness, anger, nostalgia, love)  
- replicable experiments  

---

## 9. Performance Evaluation

We evaluate the system using:

- **Latency:** average search time per song  
- **Throughput:** number of songs processed per second  
- **Speedup:** sequential vs. parallel KMP  
- **Accuracy:** precision/recall compared to manual emotional labels  
- **Annealing Improvement:** reduction in the objective cost function  

Results are stored in:
/results/scores.txt
/results/benchmarks.txt

---

## 10. Repository Structure

/src
kmp.py
trie.py
emotional_graph.py
simulated_annealing.py
search_engine.py
main.py

/tests
test_kmp.py
test_graph.py
test_annealing.py

/benchmark
benchmark_kmp.py

/data
/lyrics/song1.txt ... song30.txt
emotions.json
labels.json (optional for optimization)

/results
scores.txt
benchmarks.txt
plots/ (optional)


---

## 11. How to Run

From the project root:

python3 src/main.py

---

## 12. Authors 

Luisa Cardona A01635458

___