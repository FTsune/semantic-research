# Semantic Research using Similarity Metrics

A comprehensive platform for evaluating and comparing different text similarity metrics on legal documents.

## Features

- **5 Similarity Metrics**: TF-IDF Cosine, BM25, Jaccard, Sentence BERT, BERTScore
- **Streamlit Web Interface**: Modern, interactive web application for similarity testing
- **Performance Monitoring**: Real-time comparison of model performance
- **Docker Deployment**: Containerized for easy deployment

## Quick Start

### Using Docker (Recommended)

1. **Clone and setup**:
   ```bash
   git clone <repository>
   cd semantic-research

2. **Run the platform**:
   ```bash
   ./scripts/run.sh

3. **Access the services**:
   - Streamlit App: http://localhost:8501

### Manual Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

2. **Run evaluation**:
   ```bash
   python main.py

3. **Start Streamlit app**:
   ```bash
   streamlit run app.py

## Project Structure

```
├── models/                # Similarity metric implementations
│   ├── tfidf_cosine.py
│   ├── okapi_bm25.py
│   ├── jaccard.py
│   ├── sbert.py
│   └── bertscore.py
├── evaluation/            # Evaluation metrics and analysis
│   ├── metrics.py
│   └── analyzer.py
├── dataset/               # Philippine legal dataset
├── notebooks/             # For documentation
├── reports/               # Generated analysis reports
├── scripts/               # Setup and run scripts
├── tests/                 # Unit testing 
├── main.py                # Main evaluation script
├── app.py                 # Streamlit web application
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Multi-service setup
└── requirements.txt       # Python dependencies
```

## Streamlit Interface Features

### 🏠 Home Page
- Project overview and statistics
- Model descriptions and capabilities
- Quick dataset insights

### 🧪 Interactive Testing
- Real-time similarity calculation
- Custom query input or example selection
- Multiple visualization options
- Performance metrics display

### 📊 Model Comparison
- Side-by-side model evaluation
- Performance metrics comparison
- Resource usage analysis
- Best model recommendations

### 📋 Batch Analysis
- Full dataset processing
- Custom query batch upload
- Model benchmarking
- Results export functionality

## Available Models

1. **TF-IDF Cosine Similarity**: Traditional term frequency approach
2. **BM25**: Probabilistic ranking function
3. **Jaccard Similarity**: Set-based similarity measure
4. **Sentence BERT**: Transformer-based embeddings
5. **BERTScore**: BERT-based semantic similarity

## Evaluation Metrics

- **Precision@1**: Accuracy of top result
- **Precision@3**: Accuracy of top 3 results
- **Recall@3**: Coverage of relevant documents in top 3
- **MRR**: Mean Reciprocal Rank
- **Runtime**: Processing time
- **Memory Usage**: Peak memory consumption

## Streamlit Features

The Streamlit interface provides:
- **Interactive widgets**: Real-time parameter adjustment
- **Rich visualizations**: Plotly charts and graphs
- **Responsive design**: Works on desktop and mobile
- **Easy deployment**: Single command startup
- **Modern UI**: Clean, professional interface
- **Export capabilities**: Download results and reports

## Docker Services

- **similarity-app**: Main application with Streamlit
- **streamlit-app**: Dedicated Streamlit service
- **Shared volumes**: For data persistence and sharing

## Usage Examples

### Command Line
```bash
# Run full evaluation
python main.py

# Start Streamlit app
streamlit run app.py

# Generate specific model report
python -c "
from models.sbert import SentenceBERTSimilarity
from evaluation.analyzer import generate_analysis_log
import json

with open('dataset/philippine-legal-dataset.json') as f:
    dataset = json.load(f)

model = SentenceBERTSimilarity()
generate_analysis_log('sbert_custom', dataset, model)
"
```

### Python API
```python
from models.sbert import SentenceBERTSimilarity

model = SentenceBERTSimilarity()
query = "What is estafa under Philippine law?"
passages = ["Estafa is fraud...", "Robbery is theft..."]
scores = model.rank(query, passages)
```

### Streamlit Components
```python
import streamlit as st
from models.sbert import SentenceBERTSimilarity

# Load model with caching
@st.cache_resource
def load_model():
    return SentenceBERTSimilarity()

model = load_model()
query = st.text_input("Enter query:")
if query:
    scores = model.rank(query, passages)
    st.plotly_chart(create_similarity_chart(scores))
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your similarity metric to `models/`
4. Update the evaluation pipeline
5. Add Streamlit interface components
6. Submit a pull request