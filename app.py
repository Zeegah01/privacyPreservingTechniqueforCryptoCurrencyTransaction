import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import networkx as nx
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib
import time
import random
from datetime import datetime, timedelta
import json

# Set page config
st.set_page_config(
    page_title="Blockchain Privacy Simulation",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .privacy-level {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1);
        padding: 0.5rem;
        border-radius: 0.3rem;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

class BlockchainPrivacySimulator:
    def __init__(self):
        self.transactions = []
        self.privacy_techniques = {
            'homomorphic_encryption': self.homomorphic_encryption,
            'zero_knowledge_proofs': self.zero_knowledge_proofs,
            'ring_signatures': self.ring_signatures,
            'mixers': self.mixers,
            'stealth_addresses': self.stealth_addresses
        }
        
    def generate_synthetic_blockchain_data(self, num_transactions=1000):
        """Generate synthetic blockchain transaction data"""
        np.random.seed(42)
        
        # Generate transaction data
        for i in range(num_transactions):
            transaction = {
                'tx_id': f'tx_{i:06d}',
                'timestamp': datetime.now() - timedelta(hours=random.randint(0, 24*30)),
                'sender': f'addr_{random.randint(1000, 9999)}',
                'receiver': f'addr_{random.randint(1000, 9999)}',
                'amount': np.random.exponential(100) + 0.1,
                'fee': np.random.uniform(0.001, 0.1),
                'block_height': random.randint(1, 10000),
                'privacy_level': random.choice(['low', 'medium', 'high']),
                'technique_used': random.choice(list(self.privacy_techniques.keys())),
                'anonymity_set_size': random.randint(1, 100),
                'computational_overhead': np.random.uniform(0.1, 5.0),
                'latency_ms': np.random.exponential(100) + 10
            }
            self.transactions.append(transaction)
        
        return pd.DataFrame(self.transactions)
    
    def homomorphic_encryption(self, data, key_size=2048):
        """Simulate homomorphic encryption"""
        # Simplified simulation of homomorphic encryption
        encrypted_data = {
            'original': data,
            'encrypted': hashlib.sha256(str(data).encode()).hexdigest(),
            'key_size': key_size,
            'computation_time': key_size / 1000,  # Simulated computation time
            'privacy_level': 'high',
            'overhead': key_size / 512  # Simulated overhead
        }
        return encrypted_data
    
    def zero_knowledge_proofs(self, statement, witness):
        """Simulate zero-knowledge proofs"""
        # Simplified ZKP simulation
        proof = {
            'statement': statement,
            'proof_size': len(str(statement)) * 2,
            'verification_time': len(str(statement)) / 100,
            'privacy_level': 'very_high',
            'overhead': len(str(statement)) / 50,
            'trustless': True
        }
        return proof
    
    def ring_signatures(self, message, ring_size=10):
        """Simulate ring signatures"""
        # Simplified ring signature simulation
        signature = {
            'message': message,
            'ring_size': ring_size,
            'signature_size': ring_size * 64,  # Simulated signature size
            'privacy_level': 'high',
            'overhead': ring_size / 5,
            'anonymity_set': ring_size
        }
        return signature
    
    def mixers(self, transactions, mixing_rounds=3):
        """Simulate transaction mixing"""
        mixed_txs = transactions.copy()
        for _ in range(mixing_rounds):
            random.shuffle(mixed_txs)
        
        return {
            'original_txs': transactions,
            'mixed_txs': mixed_txs,
            'mixing_rounds': mixing_rounds,
            'privacy_level': 'medium',
            'overhead': mixing_rounds * 0.5,
            'delay': mixing_rounds * 10  # minutes
        }
    
    def stealth_addresses(self, recipient_pubkey):
        """Simulate stealth addresses"""
        # Simplified stealth address simulation
        stealth_addr = {
            'original_address': recipient_pubkey,
            'stealth_address': hashlib.sha256(recipient_pubkey.encode()).hexdigest()[:40],
            'privacy_level': 'high',
            'overhead': 0.2,
            'one_time': True
        }
        return stealth_addr

def analyze_privacy_patterns(df):
    """Analyze patterns in privacy-preserving techniques"""
    analysis = {}
    
    # Privacy level distribution
    analysis['privacy_distribution'] = df['privacy_level'].value_counts()
    
    # Technique effectiveness
    technique_analysis = df.groupby('technique_used').agg({
        'anonymity_set_size': 'mean',
        'computational_overhead': 'mean',
        'latency_ms': 'mean'
    }).round(2)
    
    analysis['technique_effectiveness'] = technique_analysis
    
    # Privacy vs Performance trade-off
    analysis['privacy_performance'] = df.groupby('privacy_level').agg({
        'computational_overhead': 'mean',
        'latency_ms': 'mean'
    }).round(2)
    
    return analysis

def detect_vulnerabilities(df):
    """Detect potential vulnerabilities in privacy techniques"""
    vulnerabilities = []
    
    # Low anonymity set size
    low_anonymity = df[df['anonymity_set_size'] < 5]
    if len(low_anonymity) > 0:
        vulnerabilities.append({
            'type': 'Low Anonymity Set',
            'count': len(low_anonymity),
            'risk_level': 'High',
            'description': 'Transactions with very small anonymity sets are vulnerable to deanonymization'
        })
    
    # High computational overhead
    high_overhead = df[df['computational_overhead'] > 3.0]
    if len(high_overhead) > 0:
        vulnerabilities.append({
            'type': 'High Computational Overhead',
            'count': len(high_overhead),
            'risk_level': 'Medium',
            'description': 'High computational overhead may lead to network congestion'
        })
    
    # Pattern detection using ML
    scaler = StandardScaler()
    features = ['amount', 'fee', 'anonymity_set_size', 'computational_overhead', 'latency_ms']
    X = scaler.fit_transform(df[features])
    
    # Use isolation forest to detect anomalies
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    anomalies = iso_forest.fit_predict(X)
    
    anomaly_indices = np.where(anomalies == -1)[0]
    if len(anomaly_indices) > 0:
        vulnerabilities.append({
            'type': 'Anomalous Transactions',
            'count': len(anomaly_indices),
            'risk_level': 'Medium',
            'description': 'Detected anomalous transaction patterns that may indicate privacy leaks'
        })
    
    return vulnerabilities

def optimize_privacy_techniques(df):
    """Optimize privacy-preserving techniques using ML"""
    # Prepare features for optimization
    features = ['amount', 'fee', 'anonymity_set_size', 'computational_overhead']
    X = df[features]
    
    # Create target variable (privacy score)
    privacy_scores = []
    for _, row in df.iterrows():
        score = 0
        if row['privacy_level'] == 'low':
            score = 1
        elif row['privacy_level'] == 'medium':
            score = 2
        elif row['privacy_level'] == 'high':
            score = 3
        privacy_scores.append(score)
    
    y = np.array(privacy_scores)
    
    # Train a model to predict optimal parameters
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    return {
        'model': model,
        'feature_importance': feature_importance,
        'accuracy': model.score(X, y)
    }

def main():
    st.markdown('<h1 class="main-header">🔐 Blockchain Privacy Simulation</h1>', unsafe_allow_html=True)
    
    # Initialize simulator
    simulator = BlockchainPrivacySimulator()
    
    # Sidebar configuration
    st.sidebar.header("Simulation Configuration")
    
    num_transactions = st.sidebar.slider("Number of Transactions", 100, 5000, 1000)
    simulation_type = st.sidebar.selectbox(
        "Simulation Type",
        ["Privacy Analysis", "Vulnerability Detection", "Technique Optimization", "Real-time Monitoring"]
    )
    
    # Generate data
    if st.sidebar.button("Generate New Data"):
        st.session_state.df = simulator.generate_synthetic_blockchain_data(num_transactions)
    
    if 'df' not in st.session_state:
        st.session_state.df = simulator.generate_synthetic_blockchain_data(num_transactions)
    
    df = st.session_state.df
    
    # Main content based on simulation type
    if simulation_type == "Privacy Analysis":
        show_privacy_analysis(df, simulator)
    elif simulation_type == "Vulnerability Detection":
        show_vulnerability_detection(df)
    elif simulation_type == "Technique Optimization":
        show_technique_optimization(df)
    elif simulation_type == "Real-time Monitoring":
        show_real_time_monitoring(df, simulator)

def show_privacy_analysis(df, simulator):
    st.header("🔍 Privacy Analysis Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Transactions", len(df))
    
    with col2:
        avg_privacy = df['anonymity_set_size'].mean()
        st.metric("Avg Anonymity Set", f"{avg_privacy:.1f}")
    
    with col3:
        avg_overhead = df['computational_overhead'].mean()
        st.metric("Avg Overhead", f"{avg_overhead:.2f}x")
    
    with col4:
        avg_latency = df['latency_ms'].mean()
        st.metric("Avg Latency", f"{avg_latency:.1f}ms")
    
    # Privacy technique comparison
    st.subheader("Privacy Technique Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Technique distribution
        fig = px.pie(df, names='technique_used', title="Distribution of Privacy Techniques")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Privacy level distribution
        fig = px.bar(df['privacy_level'].value_counts(), title="Privacy Level Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance analysis
    st.subheader("Performance Analysis")
    
    analysis = analyze_privacy_patterns(df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Technique Effectiveness:**")
        st.dataframe(analysis['technique_effectiveness'])
    
    with col2:
        st.write("**Privacy vs Performance Trade-off:**")
        st.dataframe(analysis['privacy_performance'])
    
    # Interactive technique testing
    st.subheader("🔬 Interactive Technique Testing")
    
    col1, col2 = st.columns(2)
    
    with col1:
        test_data = st.text_input("Test Data", "Hello, Blockchain!")
        technique = st.selectbox("Privacy Technique", list(simulator.privacy_techniques.keys()))
    
    with col2:
        if st.button("Test Technique"):
            if technique == 'homomorphic_encryption':
                result = simulator.homomorphic_encryption(test_data)
            elif technique == 'zero_knowledge_proofs':
                result = simulator.zero_knowledge_proofs(test_data, "witness")
            elif technique == 'ring_signatures':
                result = simulator.ring_signatures(test_data)
            elif technique == 'mixers':
                result = simulator.mixers([test_data])
            elif technique == 'stealth_addresses':
                result = simulator.stealth_addresses(test_data)
            
            st.json(result)

def show_vulnerability_detection(df):
    st.header("🚨 Vulnerability Detection")
    
    vulnerabilities = detect_vulnerabilities(df)
    
    if vulnerabilities:
        st.warning(f"Found {len(vulnerabilities)} potential vulnerabilities!")
        
        for vuln in vulnerabilities:
            with st.expander(f"{vuln['type']} - {vuln['risk_level']} Risk"):
                st.write(f"**Count:** {vuln['count']}")
                st.write(f"**Description:** {vuln['description']}")
                
                if vuln['type'] == 'Low Anonymity Set':
                    low_anon_df = df[df['anonymity_set_size'] < 5]
                    st.dataframe(low_anon_df[['tx_id', 'anonymity_set_size', 'technique_used', 'privacy_level']])
    else:
        st.success("No vulnerabilities detected!")
    
    # Anomaly detection visualization
    st.subheader("Anomaly Detection")
    
    # Prepare features for anomaly detection
    features = ['amount', 'fee', 'anonymity_set_size', 'computational_overhead', 'latency_ms']
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    
    # Isolation Forest
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    anomalies = iso_forest.fit_predict(X)
    
    # Create anomaly visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    fig = px.scatter(
        x=X_pca[:, 0], 
        y=X_pca[:, 1], 
        color=anomalies,
        title="Anomaly Detection Results",
        labels={'x': 'PCA Component 1', 'y': 'PCA Component 2'},
        color_discrete_map={1: 'blue', -1: 'red'}
    )
    st.plotly_chart(fig, use_container_width=True)

def show_technique_optimization(df):
    st.header("⚡ Technique Optimization")
    
    optimization_results = optimize_privacy_techniques(df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Model Accuracy:**")
        st.metric("Accuracy", f"{optimization_results['accuracy']:.3f}")
        
        st.write("**Feature Importance:**")
        fig = px.bar(
            optimization_results['feature_importance'],
            x='importance',
            y='feature',
            orientation='h',
            title="Feature Importance for Privacy Optimization"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.write("**Optimization Recommendations:**")
        
        # Generate recommendations based on analysis
        recommendations = [
            "Increase anonymity set size for better privacy",
            "Balance computational overhead with privacy requirements",
            "Use adaptive privacy levels based on transaction amount",
            "Implement hybrid techniques for optimal performance"
        ]
        
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
    
    # Interactive optimization
    st.subheader("Interactive Optimization")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        target_amount = st.number_input("Target Amount", min_value=0.1, value=100.0)
    
    with col2:
        target_fee = st.number_input("Target Fee", min_value=0.001, value=0.01)
    
    with col3:
        target_anonymity = st.number_input("Target Anonymity Set", min_value=1, value=10)
    
    if st.button("Optimize Parameters"):
        # Use the trained model to predict optimal parameters
        model = optimization_results['model']
        prediction = model.predict([[target_amount, target_fee, target_anonymity, 1.0]])
        
        privacy_levels = {1: 'Low', 2: 'Medium', 3: 'High'}
        recommended_level = privacy_levels[prediction[0]]
        
        st.success(f"Recommended Privacy Level: **{recommended_level}**")
        
        # Show optimization metrics
        optimization_metrics = {
            'Predicted Privacy Score': prediction[0],
            'Recommended Anonymity Set Size': max(target_anonymity, 20),
            'Estimated Overhead': target_anonymity / 10,
            'Estimated Latency': target_anonymity * 5
        }
        
        st.json(optimization_metrics)

def show_real_time_monitoring(df, simulator):
    st.header("📊 Real-time Monitoring")
    
    # Simulate real-time data
    if 'monitoring_data' not in st.session_state:
        st.session_state.monitoring_data = []
    
    # Add new transaction to monitoring
    if st.button("Add New Transaction"):
        new_tx = {
            'timestamp': datetime.now(),
            'amount': np.random.exponential(100) + 0.1,
            'privacy_level': random.choice(['low', 'medium', 'high']),
            'technique': random.choice(list(simulator.privacy_techniques.keys())),
            'anonymity_set': random.randint(1, 100)
        }
        st.session_state.monitoring_data.append(new_tx)
    
    # Display real-time metrics
    if st.session_state.monitoring_data:
        monitoring_df = pd.DataFrame(st.session_state.monitoring_data)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Live Transactions", len(monitoring_df))
        
        with col2:
            avg_amount = monitoring_df['amount'].mean()
            st.metric("Avg Amount", f"${avg_amount:.2f}")
        
        with col3:
            high_privacy = len(monitoring_df[monitoring_df['privacy_level'] == 'high'])
            st.metric("High Privacy Txs", high_privacy)
        
        with col4:
            avg_anonymity = monitoring_df['anonymity_set'].mean()
            st.metric("Avg Anonymity", f"{avg_anonymity:.1f}")
        
        # Real-time charts
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.line(monitoring_df, x='timestamp', y='amount', title="Transaction Amounts Over Time")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.scatter(monitoring_df, x='amount', y='anonymity_set', color='privacy_level', 
                           title="Privacy vs Amount Relationship")
            st.plotly_chart(fig, use_container_width=True)
    
    # Network graph simulation
    st.subheader("Network Privacy Graph")
    
    # Create a simple network graph
    G = nx.Graph()
    
    # Add nodes for different privacy techniques
    techniques = list(simulator.privacy_techniques.keys())
    for technique in techniques:
        G.add_node(technique, size=20)
    
    # Add edges based on technique relationships
    edges = [
        ('homomorphic_encryption', 'zero_knowledge_proofs'),
        ('ring_signatures', 'mixers'),
        ('stealth_addresses', 'ring_signatures'),
        ('mixers', 'zero_knowledge_proofs')
    ]
    
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    
    # Create network visualization
    pos = nx.spring_layout(G)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1000, font_size=10, font_weight='bold', ax=ax)
    plt.title("Privacy Technique Network")
    st.pyplot(fig)

if __name__ == "__main__":
    main() 