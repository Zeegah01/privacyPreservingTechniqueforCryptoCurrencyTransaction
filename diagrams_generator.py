"""
Diagram Generator for Blockchain Privacy Simulation
This script generates all the diagrams and visualizations referenced in Chapter 3 and Chapter 4
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import networkx as nx
from datetime import datetime, timedelta
import random

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_system_architecture_diagram():
    """Figure 3.1: System Architecture Diagram"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define components
    components = {
        'Data Generation Module': (2, 6),
        'Privacy Technique Simulator': (6, 6),
        'Machine Learning Engine': (10, 6),
        'Vulnerability Detection System': (6, 4),
        'Real-time Monitoring Interface': (6, 2),
        'Data Layer': (2, 4),
        'Analysis Layer': (6, 4),
        'Presentation Layer': (10, 4)
    }
    
    # Draw components
    for name, pos in components.items():
        if 'Layer' in name:
            # Draw layers as rectangles
            rect = plt.Rectangle((pos[0]-1, pos[1]-0.5), 2, 1, 
                               facecolor='lightblue', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
        else:
            # Draw modules as circles
            circle = plt.Circle(pos, 0.8, facecolor='lightgreen', edgecolor='black', linewidth=2)
            ax.add_patch(circle)
        
        ax.text(pos[0], pos[1], name, ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Draw connections
    connections = [
        ((2, 6), (6, 6)),  # Data Gen to Privacy Sim
        ((6, 6), (10, 6)),  # Privacy Sim to ML Engine
        ((6, 6), (6, 4)),   # Privacy Sim to Vulnerability
        ((6, 4), (6, 2)),   # Vulnerability to Monitoring
        ((10, 6), (10, 4)), # ML Engine to Analysis Layer
        ((6, 4), (2, 4)),   # Analysis to Data Layer
        ((6, 4), (10, 4)),  # Analysis to Presentation Layer
    ]
    
    for start, end in connections:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('Figure 3.1: System Architecture', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figures/system_architecture.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_privacy_technique_comparison():
    """Figure 3.2: Privacy Technique Comparison"""
    techniques = ['Homomorphic\nEncryption', 'Zero-Knowledge\nProofs', 'Ring\nSignatures', 
                 'Transaction\nMixers', 'Stealth\nAddresses']
    
    privacy_scores = [85, 95, 78, 65, 82]
    performance_scores = [60, 40, 80, 85, 95]
    overhead = [4.2, 5.1, 2.3, 1.8, 1.4]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Privacy vs Performance scatter plot
    scatter = ax1.scatter(performance_scores, privacy_scores, s=[o*100 for o in overhead], 
                         c=range(len(techniques)), cmap='viridis', alpha=0.7)
    ax1.set_xlabel('Performance Score')
    ax1.set_ylabel('Privacy Score')
    ax1.set_title('Privacy vs Performance Trade-off')
    ax1.grid(True, alpha=0.3)
    
    # Add technique labels
    for i, technique in enumerate(techniques):
        ax1.annotate(technique, (performance_scores[i], privacy_scores[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    # Overhead comparison bar chart
    bars = ax2.bar(techniques, overhead, color=sns.color_palette("husl", 5))
    ax2.set_ylabel('Computational Overhead (x baseline)')
    ax2.set_title('Computational Overhead by Technique')
    ax2.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, value in zip(bars, overhead):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{value:.1f}x', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('figures/privacy_technique_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_ml_workflow_diagram():
    """Figure 3.3: Machine Learning Workflow"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Define workflow steps
    steps = [
        ('Data\nGeneration', 1, 6),
        ('Feature\nEngineering', 3, 6),
        ('Model\nTraining', 5, 6),
        ('Pattern\nRecognition', 7, 6),
        ('Anomaly\nDetection', 9, 6),
        ('Optimization', 11, 6),
        ('Validation', 13, 6)
    ]
    
    # Draw workflow boxes
    for step, x, y in steps:
        rect = plt.Rectangle((x-0.8, y-0.5), 1.6, 1, 
                           facecolor='lightcoral', edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, step, ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Draw arrows
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1][1], steps[i+1][2]), 
                   xytext=(steps[i][1]+0.8, steps[i][2]),
                   arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    
    # Add feedback loops
    ax.annotate('', xy=(11, 5), xytext=(13, 5.5),
               arrowprops=dict(arrowstyle='->', lw=2, color='red', linestyle='--'))
    ax.text(12, 4.8, 'Feedback\nLoop', ha='center', va='center', fontsize=8, color='red')
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    plt.title('Figure 3.3: Machine Learning Workflow', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figures/ml_workflow.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_vulnerability_assessment_framework():
    """Figure 3.4: Vulnerability Assessment Framework"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define vulnerability categories
    categories = {
        'Low Anonymity\nSet': (2, 6, 'red'),
        'High Computational\nOverhead': (6, 6, 'orange'),
        'Temporal Pattern\nVulnerabilities': (10, 6, 'yellow'),
        'Amount Pattern\nVulnerabilities': (2, 4, 'lightgreen'),
        'Network Topology\nVulnerabilities': (6, 4, 'lightblue'),
        'Implementation\nVulnerabilities': (10, 4, 'purple')
    }
    
    # Draw vulnerability categories
    for name, (x, y, color) in categories.items():
        circle = plt.Circle((x, y), 1, facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Central assessment node
    center_circle = plt.Circle((6, 2), 1.5, facecolor='gold', edgecolor='black', linewidth=3)
    ax.add_patch(center_circle)
    ax.text(6, 2, 'Risk\nAssessment\nFramework', ha='center', va='center', 
            fontsize=10, fontweight='bold')
    
    # Draw connections to assessment
    for name, (x, y, color) in categories.items():
        ax.annotate('', xy=(6, 3.5), xytext=(x, y-1),
                   arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('Figure 3.4: Vulnerability Assessment Framework', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figures/vulnerability_framework.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_performance_metrics_dashboard():
    """Figure 4.1: Performance Metrics Dashboard"""
    # Generate sample data
    np.random.seed(42)
    techniques = ['Homomorphic\nEncryption', 'Zero-Knowledge\nProofs', 'Ring\nSignatures', 
                 'Transaction\nMixers', 'Stealth\nAddresses']
    
    privacy_scores = [85, 95, 78, 65, 82]
    performance_scores = [60, 40, 80, 85, 95]
    adoption_rates = [18, 15, 22, 25, 20]
    avg_latency = [245, 312, 127, 189, 67]
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Privacy vs Performance scatter
    scatter = ax1.scatter(performance_scores, privacy_scores, s=[r*20 for r in adoption_rates], 
                         c=avg_latency, cmap='viridis', alpha=0.7)
    ax1.set_xlabel('Performance Score')
    ax1.set_ylabel('Privacy Score')
    ax1.set_title('Privacy vs Performance Trade-off')
    ax1.grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=ax1, label='Average Latency (ms)')
    
    # Adoption rates
    bars1 = ax2.bar(techniques, adoption_rates, color=sns.color_palette("husl", 5))
    ax2.set_ylabel('Adoption Rate (%)')
    ax2.set_title('Technique Adoption Rates')
    ax2.tick_params(axis='x', rotation=45)
    
    # Average latency
    bars2 = ax3.bar(techniques, avg_latency, color=sns.color_palette("Set2", 5))
    ax3.set_ylabel('Average Latency (ms)')
    ax3.set_title('Average Transaction Latency')
    ax3.tick_params(axis='x', rotation=45)
    
    # Privacy scores
    bars3 = ax4.bar(techniques, privacy_scores, color=sns.color_palette("Paired", 5))
    ax4.set_ylabel('Privacy Score (%)')
    ax4.set_title('Privacy Protection Scores')
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('figures/performance_dashboard.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_vulnerability_analysis():
    """Figure 4.2: Vulnerability Analysis Results"""
    # Generate sample vulnerability data
    vulnerability_types = ['Low Anonymity\nSet', 'High Computational\nOverhead', 
                          'Temporal Pattern\nVulnerabilities', 'Amount Pattern\nVulnerabilities',
                          'Network Topology\nVulnerabilities']
    
    critical_count = [15, 25, 8, 12, 5]
    high_count = [40, 30, 20, 15, 10]
    medium_count = [60, 45, 35, 25, 20]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Stacked bar chart
    x = np.arange(len(vulnerability_types))
    ax1.bar(x, critical_count, label='Critical', color='red', alpha=0.8)
    ax1.bar(x, high_count, bottom=critical_count, label='High', color='orange', alpha=0.8)
    ax1.bar(x, medium_count, bottom=np.array(critical_count) + np.array(high_count), 
            label='Medium', color='yellow', alpha=0.8)
    
    ax1.set_xlabel('Vulnerability Type')
    ax1.set_ylabel('Number of Vulnerabilities')
    ax1.set_title('Vulnerability Distribution by Type and Severity')
    ax1.set_xticks(x)
    ax1.set_xticklabels(vulnerability_types, rotation=45)
    ax1.legend()
    
    # Pie chart of overall vulnerability distribution
    total_vulnerabilities = sum(critical_count) + sum(high_count) + sum(medium_count)
    sizes = [sum(critical_count), sum(high_count), sum(medium_count)]
    labels = ['Critical', 'High', 'Medium']
    colors = ['red', 'orange', 'yellow']
    
    ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax2.set_title('Overall Vulnerability Distribution')
    
    plt.tight_layout()
    plt.savefig('figures/vulnerability_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_optimization_results():
    """Figure 4.3: Optimization Results"""
    # Generate sample optimization data
    metrics = ['Privacy\nEnhancement', 'Performance\nOptimization', 'Efficiency\nGains', 'Cost\nReduction']
    before_optimization = [65, 70, 60, 75]
    after_optimization = [88, 88, 91, 97]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Before vs After comparison
    x = np.arange(len(metrics))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, before_optimization, width, label='Before Optimization', 
                    color='lightcoral', alpha=0.8)
    bars2 = ax1.bar(x + width/2, after_optimization, width, label='After Optimization', 
                    color='lightgreen', alpha=0.8)
    
    ax1.set_xlabel('Performance Metrics')
    ax1.set_ylabel('Score (%)')
    ax1.set_title('Performance Metrics: Before vs After Optimization')
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Improvement percentages
    improvements = [(a - b) for a, b in zip(after_optimization, before_optimization)]
    bars3 = ax2.bar(metrics, improvements, color=sns.color_palette("viridis", 4))
    ax2.set_ylabel('Improvement (%)')
    ax2.set_title('Optimization Improvements')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    
    # Add value labels
    for bar, value in zip(bars3, improvements):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                f'+{value:.1f}%', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('figures/optimization_results.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_real_time_monitoring():
    """Figure 4.4: Real-time Monitoring Dashboard"""
    # Generate time series data
    np.random.seed(42)
    time_points = pd.date_range(start='2024-01-01', periods=100, freq='H')
    
    # Generate realistic transaction data
    base_transactions = 50
    transactions = [base_transactions + np.random.normal(0, 10) + 
                   np.sin(i/24 * 2 * np.pi) * 20 for i in range(100)]
    
    privacy_scores = [75 + np.random.normal(0, 5) + 
                     np.cos(i/12 * 2 * np.pi) * 10 for i in range(100)]
    
    latency = [150 + np.random.normal(0, 20) + 
              np.sin(i/8 * 2 * np.pi) * 30 for i in range(100)]
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Transaction volume over time
    ax1.plot(time_points, transactions, color='blue', linewidth=2)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Transaction Volume')
    ax1.set_title('Real-time Transaction Volume')
    ax1.grid(True, alpha=0.3)
    
    # Privacy scores over time
    ax2.plot(time_points, privacy_scores, color='green', linewidth=2)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Privacy Score')
    ax2.set_title('Real-time Privacy Scores')
    ax2.grid(True, alpha=0.3)
    
    # Latency over time
    ax3.plot(time_points, latency, color='red', linewidth=2)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Latency (ms)')
    ax3.set_title('Real-time Transaction Latency')
    ax3.grid(True, alpha=0.3)
    
    # Current metrics summary
    current_metrics = {
        'Active Transactions': int(transactions[-1]),
        'Avg Privacy Score': f"{privacy_scores[-1]:.1f}%",
        'Avg Latency': f"{latency[-1]:.1f}ms",
        'System Status': 'Healthy'
    }
    
    y_pos = np.arange(len(current_metrics))
    ax4.barh(y_pos, [1, 1, 1, 1], color=['blue', 'green', 'red', 'orange'])
    ax4.set_yticks(y_pos)
    ax4.set_yticklabels(current_metrics.keys())
    ax4.set_xlabel('Status')
    ax4.set_title('Current System Metrics')
    
    # Add metric values
    for i, (key, value) in enumerate(current_metrics.items()):
        ax4.text(0.5, i, value, ha='center', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figures/real_time_monitoring.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_network_topology():
    """Figure 4.5: Network Topology Visualization"""
    # Create a sample network graph
    G = nx.Graph()
    
    # Add nodes for different privacy techniques
    techniques = ['Homomorphic\nEncryption', 'Zero-Knowledge\nProofs', 'Ring\nSignatures', 
                 'Transaction\nMixers', 'Stealth\nAddresses', 'Data\nGeneration', 
                 'ML\nEngine', 'Vulnerability\nDetection']
    
    for technique in techniques:
        G.add_node(technique)
    
    # Add edges based on relationships
    edges = [
        ('Data\nGeneration', 'Homomorphic\nEncryption'),
        ('Data\nGeneration', 'Zero-Knowledge\nProofs'),
        ('Data\nGeneration', 'Ring\nSignatures'),
        ('Data\nGeneration', 'Transaction\nMixers'),
        ('Data\nGeneration', 'Stealth\nAddresses'),
        ('Homomorphic\nEncryption', 'ML\nEngine'),
        ('Zero-Knowledge\nProofs', 'ML\nEngine'),
        ('Ring\nSignatures', 'ML\nEngine'),
        ('Transaction\nMixers', 'ML\nEngine'),
        ('Stealth\nAddresses', 'ML\nEngine'),
        ('ML\nEngine', 'Vulnerability\nDetection'),
        ('Homomorphic\nEncryption', 'Zero-Knowledge\nProofs'),
        ('Ring\nSignatures', 'Transaction\nMixers'),
        ('Stealth\nAddresses', 'Ring\nSignatures')
    ]
    
    G.add_edges_from(edges)
    
    # Create the visualization
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Use spring layout for better visualization
    pos = nx.spring_layout(G, k=3, iterations=50)
    
    # Draw the network
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=8, font_weight='bold',
            edge_color='gray', width=2, alpha=0.7, ax=ax)
    
    plt.title('Figure 4.5: Network Topology of Privacy Techniques', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figures/network_topology.png', dpi=300, bbox_inches='tight')
    plt.show()

def generate_all_diagrams():
    """Generate all diagrams for the thesis"""
    print("Generating all diagrams for Chapter 3 and Chapter 4...")
    
    # Create figures directory
    import os
    os.makedirs('figures', exist_ok=True)
    
    # Chapter 3 diagrams
    print("Generating Chapter 3 diagrams...")
    create_system_architecture_diagram()
    create_privacy_technique_comparison()
    create_ml_workflow_diagram()
    create_vulnerability_assessment_framework()
    
    # Chapter 4 diagrams
    print("Generating Chapter 4 diagrams...")
    create_performance_metrics_dashboard()
    create_vulnerability_analysis()
    create_optimization_results()
    create_real_time_monitoring()
    create_network_topology()
    
    print("All diagrams generated successfully!")
    print("Diagrams saved in the 'figures' directory.")

if __name__ == "__main__":
    generate_all_diagrams() 