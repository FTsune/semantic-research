import streamlit as st
import json
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
from datetime import datetime

# Import models
from models.tfidf_cosine import TFIDFCosineSimilarity
from models.okapi_bm25 import BM25Similarity
from models.jaccard import JaccardSimilarity
from models.sbert import SentenceBERTSimilarity
from models.bertscore import BERTScoreSimilarity
from evaluation.metrics import evaluate_model
from evaluation.analyzer import generate_analysis_log

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch")

# Page configuration
st.set_page_config(
    page_title="Text Similarity Evaluation Platform",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_models():
    """Load and cache all similarity models"""
    return {
        'TF-IDF': TFIDFCosineSimilarity(use_dimensionality_reduction=True, n_components=50),
        'BM25': BM25Similarity(),
        'Jaccard': JaccardSimilarity(),
        'Sentence BERT': SentenceBERTSimilarity(model_name='all-mpnet-base-v2'),
        'BERTScore': BERTScoreSimilarity(model_type='distilbert-base-uncased')
    }

@st.cache_data
def load_dataset():
    """Load and cache the dataset"""
    try:
        with open('dataset/philippine-legal-dataset.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure the dataset is in the correct location.")
        return []

def main():
    # Header
    st.markdown('<h1 class="main-header">🔍 Text Similarity Evaluation</h1>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Home", "🧪 Interactive Testing", "📊 Model Comparison", "📋 Batch Analysis"]
    )
    
    # Load data
    models = load_models()
    dataset = load_dataset()
    
    if page == "🏠 Home":
        show_home_page()
    elif page == "🧪 Interactive Testing":
        show_interactive_testing(models, dataset)
    elif page == "📊 Model Comparison":
        show_model_comparison(models, dataset)
    elif page == "📋 Batch Analysis":
        show_batch_analysis(models, dataset)

def show_home_page():
    """Display the home page with project overview"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Welcome to the Text Similarity Evaluation Platform
        
        This platform provides comprehensive tools for evaluating and comparing different text similarity metrics 
        specifically designed for Philippine legal document retrieval and analysis.
        
        ### 🚀 Features
        
        - **5 Similarity Metrics**: TF-IDF, BM25, Jaccard, Sentence BERT, BERTScore
        - **Interactive Testing**: Real-time similarity calculation with custom queries
        - **Performance Comparison**: Side-by-side model evaluation
        - **Batch Analysis**: Process multiple queries efficiently
        - **Visualization**: Rich charts and graphs for result analysis
        
        ### 📊 Available Models
        """)
        
        model_info = {
            "TF-IDF": "Traditional term frequency-inverse document frequency with cosine similarity",
            "BM25": "Probabilistic ranking function used by search engines",
            "Jaccard": "Set-based similarity measure using token overlap",
            "Sentence BERT": "Transformer-based semantic embeddings",
            "BERTScore": "BERT-based semantic similarity scoring"
        }
        
        for model, description in model_info.items():
            st.markdown(f"**{model}**: {description}")
    
    with col2:
        st.markdown("### 📈 Quick Stats")
        
        dataset = load_dataset()
        if dataset:
            st.metric("Total Queries", len(dataset))
            total_passages = sum(len(item['passages']) for item in dataset)
            st.metric("Total Passages", total_passages)
            relevant_passages = sum(sum(p['relevant'] for p in item['passages']) for item in dataset)
            st.metric("Relevant Passages", relevant_passages)
            
            # Relevance ratio
            relevance_ratio = relevant_passages / total_passages if total_passages > 0 else 0
            st.metric("Relevance Ratio", f"{relevance_ratio:.2%}")

def show_interactive_testing(models, dataset):
    """Display the interactive testing interface"""
    
    st.header("🧪 Interactive Similarity Testing")
    
    # Example selector
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if dataset:
            example_options = ["Custom Query"] + [f"Example {i+1}: {item['query'][:50]}..." 
                                                 for i, item in enumerate(dataset[:10])]
            selected_example = st.selectbox("Choose an example or enter custom query:", example_options)
        else:
            selected_example = "Custom Query"
    
    with col2:
        selected_model = st.selectbox("Select Model:", list(models.keys()), index=3)  # Default to Sentence BERT
    
    # Query input
    if selected_example == "Custom Query":
        query = st.text_area("Enter your query:", 
                           placeholder="What is the function of the Presidential Electoral Tribunal?",
                           height=100)
        
        # Custom passages
        st.subheader("Passages to Compare")
        st.markdown("Enter passages and mark their relevance:")

        # Initialize session state for passages if not exists
        if 'custom_passages' not in st.session_state:
            st.session_state.custom_passages = []

        # Add passage section
        with st.expander("➕ Add New Passage", expanded=len(st.session_state.custom_passages) == 0):
            new_passage = st.text_area("Enter passage text:", 
                                      placeholder="Enter a passage to compare against the query...",
                                      height=100,
                                      key="new_passage_input")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                is_relevant = st.checkbox("Mark as relevant", key="new_passage_relevant")
            with col2:
                passage_label = st.selectbox("Label type:", 
                                           ["exact", "paraphrase", "conceptual", "irrelevant"],
                                           index=3 if not is_relevant else 0,
                                           key="new_passage_label")
            
            if st.button("Add Passage"):
                if new_passage.strip():
                    st.session_state.custom_passages.append({
                        'text': new_passage.strip(),
                        'relevant': is_relevant,
                        'label': passage_label
                    })
                    st.success("✅ Passage added!")
                    st.rerun()
                else:
                    st.warning("Please enter passage text.")

        # Display current passages
        if st.session_state.custom_passages:
            st.subheader(f"Current Passages ({len(st.session_state.custom_passages)})")
            
            for i, passage_data in enumerate(st.session_state.custom_passages):
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                    
                    with col1:
                        # Show passage text (truncated)
                        display_text = passage_data['text'][:100] + "..." if len(passage_data['text']) > 100 else passage_data['text']
                        st.write(f"**Passage {i+1}:** {display_text}")
                    
                    with col2:
                        # Relevance indicator
                        relevance_color = "🟢" if passage_data['relevant'] else "🔴"
                        st.write(f"{relevance_color} {'Relevant' if passage_data['relevant'] else 'Irrelevant'}")
                    
                    with col3:
                        # Label
                        st.write(f"**{passage_data['label']}**")
                    
                    with col4:
                        # Remove button
                        if st.button("🗑️", key=f"remove_{i}", help="Remove passage"):
                            st.session_state.custom_passages.pop(i)
                            st.rerun()
                    
                    # Show full text in expander
                    with st.expander(f"View full text - Passage {i+1}"):
                        st.write(passage_data['text'])
                        
                        # Edit options
                        edit_col1, edit_col2 = st.columns(2)
                        with edit_col1:
                            new_relevant = st.checkbox("Relevant", 
                                                     value=passage_data['relevant'],
                                                     key=f"edit_relevant_{i}")
                        with edit_col2:
                            new_label = st.selectbox("Label:", 
                                                   ["exact", "paraphrase", "conceptual", "irrelevant"],
                                                   index=["exact", "paraphrase", "conceptual", "irrelevant"].index(passage_data['label']),
                                                   key=f"edit_label_{i}")
                        
                        if st.button("Update", key=f"update_{i}"):
                            st.session_state.custom_passages[i]['relevant'] = new_relevant
                            st.session_state.custom_passages[i]['label'] = new_label
                            st.success("✅ Passage updated!")
                            st.rerun()

        # Clear all passages button
        if st.session_state.custom_passages:
            if st.button("🗑️ Clear All Passages", type="secondary"):
                st.session_state.custom_passages = []
                st.rerun()

        # Extract data for analysis
        if st.session_state.custom_passages:
            passages = [p['text'] for p in st.session_state.custom_passages]
            labels = [p['relevant'] for p in st.session_state.custom_passages]
            tags = [p['label'] for p in st.session_state.custom_passages]
        else:
            passages, labels, tags = [], [], []
    else:
        # Load selected example
        example_idx = int(selected_example.split()[1].rstrip(':')) - 1
        example = dataset[example_idx]
        query = st.text_area("Query:", value=example['query'], height=100)
        
        passages = [p['text'] for p in example['passages']]
        labels = [p['relevant'] for p in example['passages']]
        tags = [p['label'] for p in example['passages']]
        
        # Display passages
        st.subheader("Available Passages")
        for i, (passage, label, tag) in enumerate(zip(passages, labels, tags)):
            status = "✅ Relevant" if label else "❌ Irrelevant"
            with st.expander(f"Passage {i+1}: {tag} - {status}"):
                st.write(passage)
    
    # Run analysis
    if st.button("🔍 Analyze Similarity", type="primary"):
        if query and passages:
            with st.spinner("Calculating similarities..."):
                model = models[selected_model]
                scores = model.rank(query, passages)
                
                # Sort results
                sorted_indices = np.argsort(scores)[::-1]
                
                # Create results dataframe
                results_df = pd.DataFrame({
                    'Rank': range(1, len(passages) + 1),
                    'Passage': [passages[i] for i in sorted_indices],
                    'Score': [scores[i] for i in sorted_indices],
                    'Relevant': [labels[i] for i in sorted_indices],
                    'Label': [tags[i] for i in sorted_indices],
                    'Original_Index': sorted_indices
                })
                
                # Display results
                st.success("✅ Analysis Complete!")
                
                # Top results
                st.subheader("🏆 Top Results")
                
                for i in range(min(3, len(results_df))):
                    row = results_df.iloc[i]
                    
                    with st.container():
                        col1, col2, col3 = st.columns([1, 2, 1])
                        
                        with col1:
                            st.metric(f"Rank {row['Rank']}", f"{row['Score']:.4f}")
                        
                        with col2:
                            status = "✅ Relevant" if row['Relevant'] else "❌ Irrelevant"
                            st.write(f"**{status}** ({row['Label']})")
                            st.write(row['Passage'][:200] + "..." if len(row['Passage']) > 200 else row['Passage'])
                        
                        with col3:
                            if row['Relevant']:
                                st.success("Correct")
                            else:
                                st.error("Incorrect")
                
                # Visualizations
                st.subheader("📊 Visualizations")
                
                # Create tabs for different visualizations
                tab1, tab2, tab3 = st.tabs(["Similarity Scores", "Performance Analysis", "Detailed Results"])
                
                with tab1:
                    # Bar chart of similarity scores
                    fig = go.Figure()
                    colors = ['green' if rel else 'red' for rel in results_df['Relevant']]
                    
                    fig.add_trace(go.Bar(
                        x=[f"Passage {i}" for i in results_df['Rank']],
                        y=results_df['Score'],
                        marker_color=colors,
                        text=results_df['Score'].round(4),
                        textposition='auto',
                        hovertemplate='<b>Rank %{x}</b><br>Score: %{y:.4f}<br>Relevant: %{customdata}<extra></extra>',
                        customdata=results_df['Relevant']
                    ))
                    
                    fig.update_layout(
                        title=f"Similarity Scores - {selected_model}",
                        xaxis_title="Passages (Ranked)",
                        yaxis_title="Similarity Score",
                        height=400
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                with tab2:
                    # Performance metrics
                    col1, col2, col3, col4 = st.columns(4)
                    
                    # Calculate metrics
                    top1_correct = results_df.iloc[0]['Relevant']
                    top3_correct = sum(results_df.iloc[:3]['Relevant'])
                    total_relevant = sum(results_df['Relevant'])
                    
                    precision_at_1 = 1.0 if top1_correct else 0.0
                    precision_at_3 = top3_correct / 3
                    recall_at_3 = top3_correct / total_relevant if total_relevant > 0 else 0.0
                    
                    # Find MRR
                    mrr_rank = None
                    for i, relevant in enumerate(results_df['Relevant'], 1):
                        if relevant:
                            mrr_rank = i
                            break
                    mrr = 1.0 / mrr_rank if mrr_rank else 0.0
                    
                    with col1:
                        st.metric("Precision@1", f"{precision_at_1:.3f}")
                    with col2:
                        st.metric("Precision@3", f"{precision_at_3:.3f}")
                    with col3:
                        st.metric("Recall@3", f"{recall_at_3:.3f}")
                    with col4:
                        st.metric("MRR", f"{mrr:.3f}")
                    
                    # Relevance distribution
                    relevance_counts = results_df['Relevant'].value_counts()
                    fig_pie = go.Figure(data=[go.Pie(
                        labels=['Irrelevant', 'Relevant'],
                        values=[relevance_counts.get(False, 0), relevance_counts.get(True, 0)],
                        hole=0.3
                    )])
                    fig_pie.update_layout(title="Relevance Distribution", height=300)
                    st.plotly_chart(fig_pie, use_container_width=True)
                
                with tab3:
                    # Detailed results table
                    st.dataframe(
                        results_df[['Rank', 'Score', 'Relevant', 'Label', 'Passage']],
                        use_container_width=True,
                        height=400
                    )
        else:
            st.warning("Please enter both a query and passages to analyze.")

def show_model_comparison(models, dataset):
    """Display model comparison interface"""
    
    st.header("📊 Model Comparison")
    
    if not dataset:
        st.error("No dataset available for comparison.")
        return
    
    # Model selection
    selected_models = st.multiselect(
        "Select models to compare:",
        list(models.keys()),
        default=list(models.keys())[:3]
    )
    
    if not selected_models:
        st.warning("Please select at least one model.")
        return
    
    # Run comparison
    if st.button("🚀 Run Comparison", type="primary"):
        results = {}
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, model_name in enumerate(selected_models):
            status_text.text(f"Evaluating {model_name}...")
            model = models[model_name]
            
            # Evaluate model
            metrics = evaluate_model(model, dataset)
            results[model_name] = metrics
            
            progress_bar.progress((i + 1) / len(selected_models))
        
        status_text.text("Comparison complete!")
        
        # Display results
        st.success("✅ Comparison Complete!")
        
        # Create comparison dataframe
        comparison_df = pd.DataFrame(results).T
        
        # Metrics overview
        st.subheader("📈 Performance Metrics")
        st.dataframe(comparison_df.round(4), use_container_width=True)
        
        # Visualizations
        st.subheader("📊 Performance Comparison")
        
        # Create subplots for different metrics
        metrics_to_plot = ['Precision@1', 'Precision@3', 'Recall@3', 'MRR']
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=metrics_to_plot,
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        positions = [(1,1), (1,2), (2,1), (2,2)]
        colors = px.colors.qualitative.Set1[:len(selected_models)]
        
        for metric, (row, col) in zip(metrics_to_plot, positions):
            fig.add_trace(
                go.Bar(
                    x=comparison_df.index,
                    y=comparison_df[metric],
                    name=metric,
                    marker_color=colors,
                    showlegend=False
                ),
                row=row, col=col
            )
        
        fig.update_layout(height=600, title_text="Model Performance Comparison")
        st.plotly_chart(fig, use_container_width=True)
        
        # Resource usage comparison
        st.subheader("⚡ Resource Usage")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_runtime = go.Figure()
            fig_runtime.add_trace(go.Bar(
                x=comparison_df.index,
                y=comparison_df['Runtime (in seconds)'],
                marker_color='lightblue',
                text=comparison_df['Runtime (in seconds)'].round(2),
                textposition='auto'
            ))
            fig_runtime.update_layout(title="Runtime Comparison (seconds)", height=400)
            st.plotly_chart(fig_runtime, use_container_width=True)
        
        with col2:
            fig_memory = go.Figure()
            fig_memory.add_trace(go.Bar(
                x=comparison_df.index,
                y=comparison_df['Peak Memory (in KB)'],
                marker_color='lightcoral',
                text=comparison_df['Peak Memory (in KB)'].round(0),
                textposition='auto'
            ))
            fig_memory.update_layout(title="Memory Usage (KB)", height=400)
            st.plotly_chart(fig_memory, use_container_width=True)
        
        # Best model recommendation
        st.subheader("🏆 Recommendations")
        
        # Find best models for different metrics
        best_precision1 = comparison_df['Precision@1'].idxmax()
        best_precision3 = comparison_df['Precision@3'].idxmax()
        best_recall3 = comparison_df['Recall@3'].idxmax()
        best_mrr = comparison_df['MRR'].idxmax()
        best_speed = comparison_df['Runtime (in seconds)'].idxmin()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**🎯 Best Accuracy**")
            st.write(f"Precision@1: **{best_precision1}**")
            st.write(f"MRR: **{best_mrr}**")
        
        with col2:
            st.markdown("**🔍 Best Coverage**")
            st.write(f"Precision@3: **{best_precision3}**")
            st.write(f"Recall@3: **{best_recall3}**")
        
        with col3:
            st.markdown("**⚡ Best Performance**")
            st.write(f"Fastest: **{best_speed}**")

def show_batch_analysis(models, dataset):
    """Display batch analysis interface"""
    
    st.header("📋 Batch Analysis")
    
    # Analysis options
    col1, col2 = st.columns([1, 1])
    
    with col1:
        analysis_type = st.selectbox(
            "Analysis Type:",
            ["Full Dataset Analysis", "Custom Query Batch", "Model Benchmarking"]
        )
    
    with col2:
        selected_model = st.selectbox("Select Model:", list(models.keys()))
    
    if analysis_type == "Full Dataset Analysis":
        st.subheader("📊 Complete Dataset Analysis")
        
        if st.button("🚀 Run Full Analysis"):
            model = models[selected_model]
            
            with st.spinner("Running full dataset analysis..."):
                # Generate detailed analysis
                metrics = evaluate_model(model, dataset)
                generate_analysis_log(selected_model.lower().replace(' ', '_'), dataset, model, metrics)
                
                st.success("✅ Analysis Complete!")
                
                # Display summary metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Precision@1", f"{metrics['Precision@1']:.4f}")
                with col2:
                    st.metric("Precision@3", f"{metrics['Precision@3']:.4f}")
                with col3:
                    st.metric("Recall@3", f"{metrics['Recall@3']:.4f}")
                with col4:
                    st.metric("MRR", f"{metrics['MRR']:.4f}")
                
                # Show analysis report
                report_path = f"reports/{selected_model.lower().replace(' ', '_')}_performance.md"
                if os.path.exists(report_path):
                    with open(report_path, 'r', encoding='utf-8') as f:
                        report_content = f.read()
                    
                    with st.expander("📄 View Detailed Report"):
                        st.markdown(report_content)
    
    elif analysis_type == "Custom Query Batch":
        st.subheader("📝 Custom Query Batch Processing")
        
        # File upload for batch queries
        uploaded_file = st.file_uploader(
            "Upload queries file (JSON format):",
            type=['json'],
            help="Upload a JSON file with queries and passages"
        )
        
        if uploaded_file:
            try:
                batch_data = json.load(uploaded_file)
                st.success(f"✅ Loaded {len(batch_data)} queries")
                
                if st.button("🔄 Process Batch"):
                    model = models[selected_model]
                    results = []
                    
                    progress_bar = st.progress(0)
                    
                    for i, item in enumerate(batch_data):
                        query = item['query']
                        passages = [p['text'] for p in item['passages']]
                        labels = [p['relevant'] for p in item['passages']]
                        
                        scores = model.rank(query, passages)
                        sorted_indices = np.argsort(scores)[::-1]
                        
                        # Calculate metrics for this query
                        top1_correct = labels[sorted_indices[0]]
                        
                        results.append({
                            'Query': query[:50] + "...",
                            'Top1_Correct': top1_correct,
                            'Top1_Score': scores[sorted_indices[0]],
                            'Avg_Score': np.mean(scores)
                        })
                        
                        progress_bar.progress((i + 1) / len(batch_data))
                    
                    # Display batch results
                    results_df = pd.DataFrame(results)
                    
                    st.subheader("📊 Batch Results Summary")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        accuracy = results_df['Top1_Correct'].mean()
                        st.metric("Batch Accuracy", f"{accuracy:.2%}")
                    with col2:
                        avg_score = results_df['Top1_Score'].mean()
                        st.metric("Avg Top1 Score", f"{avg_score:.4f}")
                    with col3:
                        total_queries = len(results_df)
                        st.metric("Processed Queries", total_queries)
                    
                    # Results table
                    st.dataframe(results_df, use_container_width=True)
                    
                    # Download results
                    csv = results_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results CSV",
                        data=csv,
                        file_name=f"batch_results_{selected_model}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
            
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
    
    elif analysis_type == "Model Benchmarking":
        st.subheader("🏁 Model Benchmarking")
        
        benchmark_models = st.multiselect(
            "Select models for benchmarking:",
            list(models.keys()),
            default=list(models.keys())
        )
        
        if benchmark_models and st.button("🏃‍♂️ Run Benchmark"):
            benchmark_results = {}
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, model_name in enumerate(benchmark_models):
                status_text.text(f"Benchmarking {model_name}...")
                model = models[model_name]
                
                start_time = time.time()
                metrics = evaluate_model(model, dataset)
                end_time = time.time()
                
                metrics['Total_Runtime'] = end_time - start_time
                benchmark_results[model_name] = metrics
                
                progress_bar.progress((i + 1) / len(benchmark_models))
            
            status_text.text("Benchmarking complete!")
            
            # Display benchmark results
            benchmark_df = pd.DataFrame(benchmark_results).T
            
            st.subheader("🏆 Benchmark Results")
            st.dataframe(benchmark_df.round(4), use_container_width=True)
            
            # Performance ranking
            st.subheader("📊 Performance Ranking")
            
            ranking_metrics = ['Precision@1', 'Precision@3', 'Recall@3', 'MRR']
            
            for metric in ranking_metrics:
                ranked = benchmark_df[metric].sort_values(ascending=False)
                
                with st.expander(f"🏅 {metric} Ranking"):
                    for i, (model, score) in enumerate(ranked.items(), 1):
                        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
                        st.write(f"{medal} **{model}**: {score:.4f}")

if __name__ == "__main__":
    main()