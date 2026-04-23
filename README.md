# 🧠 AI Knowledge Graph Builder
---

## 📌 Overview

**AI Knowledge Graph Builder** is an intelligent system that transforms unstructured text into structured knowledge by extracting entities and relationships to build a graph-based representation of information.

The application uses Natural Language Processing (NLP) to identify key entities such as people, organizations, and locations, and constructs relationships between them to form a **knowledge graph**. This allows users to better understand complex data and explore connections between concepts.

---

## ✨ Features

* 📄 Input text or document content
* 🔍 Entity extraction using NLP (spaCy)
* 🔗 Automatic relationship creation
* 📊 Graph-based data representation
* ⚡ Interactive UI using Streamlit

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **spaCy (NLP for entity extraction)**
* **NetworkX (graph construction)**

---

## 🏗️ Architecture

```id="archkg1"
Document Input
      ↓
Text Processing
      ↓
Entity Extraction (spaCy)
      ↓
Relationship Mapping
      ↓
Graph Construction (NetworkX)
      ↓
Streamlit UI Display
```

---

## 📂 Project Structure

```id="archkg2"
ai-knowledge-graph/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── extractor.py
│   ├── graph_builder.py
│   └── query.py
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash id="run1kg"
git clone https://github.com/your-username/ai-knowledge-graph.git
cd ai-knowledge-graph
```

---

### 2️⃣ Install Dependencies

```bash id="run2kg"
pip install -r requirements.txt
```

---

### 3️⃣ Install spaCy Model

```bash id="run3kg"
python -m spacy download en_core_web_sm
```

---

### 4️⃣ Run Application

```bash id="run4kg"
streamlit run app.py
```

---

## 💡 Example Input

```text id="examplekg"
Elon Musk is the CEO of Tesla. Tesla is based in California. SpaceX was also founded by Elon Musk.
```

---

## 📊 Example Output

* Entities:

  * Elon Musk (Person)
  * Tesla (Organization)
  * California (Location)
  * SpaceX (Organization)

* Relationships:

  * Elon Musk → Tesla
  * Tesla → California
  * Elon Musk → SpaceX

---

## 🎯 Use Cases

* Knowledge extraction from documents
* Research and data analysis
* Semantic search systems
* Recommendation engines
* AI-powered search and reasoning

---

## 📬 Author

**Joncy Keda - AI Developer**

