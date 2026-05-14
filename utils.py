"""
Utility functions for blockchain privacy simulation
"""

import numpy as np
import pandas as pd
import hashlib
import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any
import json

class PrivacyMetrics:
    """Calculate various privacy metrics for blockchain transactions"""
    
    @staticmethod
    def calculate_entropy(transactions: List[Dict]) -> float:
        """Calculate Shannon entropy of transaction patterns"""
        if not transactions:
            return 0.0
        
        # Extract transaction amounts
        amounts = [tx.get('amount', 0) for tx in transactions]
        
        # Create histogram
        hist, _ = np.histogram(amounts, bins=20)
        hist = hist[hist > 0]  # Remove zero bins
        
        # Calculate entropy
        p = hist / hist.sum()
        entropy = -np.sum(p * np.log2(p))
        
        return entropy
    
    @staticmethod
    def calculate_anonymity_score(anonymity_set_size: int, technique_used: str) -> float:
        """Calculate anonymity score based on set size and technique"""
        base_score = min(anonymity_set_size / 100.0, 1.0)
        
        # Technique multipliers
        technique_multipliers = {
            'homomorphic_encryption': 1.2,
            'zero_knowledge_proofs': 1.5,
            'ring_signatures': 1.3,
            'mixers': 1.1,
            'stealth_addresses': 1.0
        }
        
        multiplier = technique_multipliers.get(technique_used, 1.0)
        return min(base_score * multiplier, 1.0)
    
    @staticmethod
    def calculate_privacy_level(anonymity_score: float, entropy: float) -> str:
        """Determine privacy level based on anonymity score and entropy"""
        combined_score = (anonymity_score + entropy / 10.0) / 2.0
        
        if combined_score >= 0.8:
            return 'very_high'
        elif combined_score >= 0.6:
            return 'high'
        elif combined_score >= 0.4:
            return 'medium'
        else:
            return 'low'

class BlockchainAnalyzer:
    """Analyze blockchain data for patterns and vulnerabilities"""
    
    def __init__(self):
        self.patterns = {}
        self.vulnerabilities = []
    
    def detect_temporal_patterns(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Detect temporal patterns in transactions"""
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
        
        patterns = {
            'hourly_distribution': df['hour'].value_counts().sort_index().to_dict(),
            'daily_distribution': df['day_of_week'].value_counts().sort_index().to_dict(),
            'peak_hours': df.groupby('hour')['amount'].mean().nlargest(3).to_dict(),
            'quiet_hours': df.groupby('hour')['amount'].mean().nsmallest(3).to_dict()
        }
        
        return patterns
    
    def detect_amount_patterns(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Detect patterns in transaction amounts"""
        patterns = {
            'amount_distribution': {
                'mean': df['amount'].mean(),
                'median': df['amount'].median(),
                'std': df['amount'].std(),
                'skewness': df['amount'].skew(),
                'kurtosis': df['amount'].kurtosis()
            },
            'amount_ranges': {
                'small': len(df[df['amount'] < 10]),
                'medium': len(df[(df['amount'] >= 10) & (df['amount'] < 100)]),
                'large': len(df[df['amount'] >= 100])
            },
            'suspicious_amounts': df[df['amount'] > df['amount'].quantile(0.99)]['tx_id'].tolist()
        }
        
        return patterns
    
    def detect_network_patterns(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Detect network-level patterns"""
        # Sender frequency
        sender_freq = df['sender'].value_counts()
        receiver_freq = df['receiver'].value_counts()
        
        patterns = {
            'active_senders': sender_freq.head(10).to_dict(),
            'active_receivers': receiver_freq.head(10).to_dict(),
            'unique_addresses': len(set(df['sender'].tolist() + df['receiver'].tolist())),
            'high_frequency_addresses': sender_freq[sender_freq > 10].index.tolist()
        }
        
        return patterns

class VulnerabilityScanner:
    """Scan for various types of vulnerabilities"""
    
    @staticmethod
    def scan_low_anonymity(df: pd.DataFrame, threshold: int = 5) -> List[Dict]:
        """Scan for transactions with low anonymity sets"""
        low_anon = df[df['anonymity_set_size'] < threshold]
        
        vulnerabilities = []
        for _, row in low_anon.iterrows():
            vulnerabilities.append({
                'tx_id': row['tx_id'],
                'type': 'low_anonymity',
                'severity': 'high',
                'description': f'Anonymity set size {row["anonymity_set_size"]} is below threshold {threshold}',
                'recommendation': 'Increase anonymity set size or use stronger privacy technique'
            })
        
        return vulnerabilities
    
    @staticmethod
    def scan_high_overhead(df: pd.DataFrame, threshold: float = 3.0) -> List[Dict]:
        """Scan for transactions with high computational overhead"""
        high_overhead = df[df['computational_overhead'] > threshold]
        
        vulnerabilities = []
        for _, row in high_overhead.iterrows():
            vulnerabilities.append({
                'tx_id': row['tx_id'],
                'type': 'high_overhead',
                'severity': 'medium',
                'description': f'Computational overhead {row["computational_overhead"]:.2f}x is above threshold {threshold}x',
                'recommendation': 'Consider using lighter privacy technique or optimize implementation'
            })
        
        return vulnerabilities
    
    @staticmethod
    def scan_pattern_vulnerabilities(df: pd.DataFrame) -> List[Dict]:
        """Scan for pattern-based vulnerabilities"""
        vulnerabilities = []
        
        # Check for repeated amounts
        amount_counts = df['amount'].value_counts()
        repeated_amounts = amount_counts[amount_counts > 5]
        
        for amount, count in repeated_amounts.items():
            vulnerabilities.append({
                'type': 'repeated_amount',
                'severity': 'medium',
                'description': f'Amount {amount:.2f} appears {count} times',
                'recommendation': 'Use amount mixing or randomize transaction amounts'
            })
        
        # Check for time-based patterns
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        
        hourly_counts = df['hour'].value_counts()
        peak_hours = hourly_counts[hourly_counts > hourly_counts.mean() + hourly_counts.std()]
        
        if len(peak_hours) > 0:
            vulnerabilities.append({
                'type': 'temporal_pattern',
                'severity': 'low',
                'description': f'Peak activity detected in hours: {peak_hours.index.tolist()}',
                'recommendation': 'Consider temporal mixing to obscure activity patterns'
            })
        
        return vulnerabilities

class PerformanceAnalyzer:
    """Analyze performance characteristics of privacy techniques"""
    
    @staticmethod
    def calculate_performance_metrics(df: pd.DataFrame) -> Dict[str, Any]:
        """Calculate comprehensive performance metrics"""
        metrics = {
            'overall_performance': {
                'avg_latency': df['latency_ms'].mean(),
                'avg_overhead': df['computational_overhead'].mean(),
                'throughput': len(df) / (df['latency_ms'].sum() / 1000),  # txs per second
                'efficiency_score': 1 / (df['computational_overhead'].mean() * df['latency_ms'].mean() / 1000)
            },
            'technique_performance': df.groupby('technique_used').agg({
                'latency_ms': ['mean', 'std'],
                'computational_overhead': ['mean', 'std'],
                'anonymity_set_size': 'mean'
            }).round(2),
            'privacy_performance_tradeoff': df.groupby('privacy_level').agg({
                'latency_ms': 'mean',
                'computational_overhead': 'mean',
                'anonymity_set_size': 'mean'
            }).round(2)
        }
        
        return metrics
    
    @staticmethod
    def identify_bottlenecks(df: pd.DataFrame) -> List[Dict]:
        """Identify performance bottlenecks"""
        bottlenecks = []
        
        # High latency transactions
        high_latency = df[df['latency_ms'] > df['latency_ms'].quantile(0.95)]
        if len(high_latency) > 0:
            bottlenecks.append({
                'type': 'high_latency',
                'count': len(high_latency),
                'avg_latency': high_latency['latency_ms'].mean(),
                'techniques': high_latency['technique_used'].value_counts().to_dict()
            })
        
        # High overhead transactions
        high_overhead = df[df['computational_overhead'] > df['computational_overhead'].quantile(0.95)]
        if len(high_overhead) > 0:
            bottlenecks.append({
                'type': 'high_overhead',
                'count': len(high_overhead),
                'avg_overhead': high_overhead['computational_overhead'].mean(),
                'techniques': high_overhead['technique_used'].value_counts().to_dict()
            })
        
        return bottlenecks

class DataGenerator:
    """Generate realistic blockchain data for simulation"""
    
    @staticmethod
    def generate_addresses(num_addresses: int) -> List[str]:
        """Generate realistic blockchain addresses"""
        addresses = []
        for i in range(num_addresses):
            # Simulate different address formats
            if random.random() < 0.7:  # Bitcoin-style
                addr = f"1{hashlib.sha256(str(i).encode()).hexdigest()[:25]}"
            else:  # Ethereum-style
                addr = f"0x{hashlib.sha256(str(i).encode()).hexdigest()[:40]}"
            addresses.append(addr)
        
        return addresses
    
    @staticmethod
    def generate_transaction_amounts(num_transactions: int) -> List[float]:
        """Generate realistic transaction amounts"""
        amounts = []
        
        # Mix of different amount distributions
        for _ in range(num_transactions):
            if random.random() < 0.6:  # Small transactions
                amount = np.random.exponential(10) + 0.001
            elif random.random() < 0.9:  # Medium transactions
                amount = np.random.normal(100, 50) + 0.01
            else:  # Large transactions
                amount = np.random.exponential(1000) + 10
            
            amounts.append(max(amount, 0.001))  # Minimum amount
        
        return amounts
    
    @staticmethod
    def generate_temporal_patterns(num_transactions: int) -> List[datetime]:
        """Generate realistic temporal patterns"""
        timestamps = []
        base_time = datetime.now() - timedelta(days=30)
        
        for i in range(num_transactions):
            # Add some randomness and patterns
            if random.random() < 0.1:  # Burst of transactions
                time_offset = random.randint(0, 60)  # Within 1 hour
            else:
                time_offset = random.randint(0, 24*60*60)  # Within 30 days
            
            # Add some daily patterns (more activity during certain hours)
            hour = random.randint(9, 17) if random.random() < 0.7 else random.randint(0, 23)
            minute = random.randint(0, 59)
            
            timestamp = base_time + timedelta(
                days=i//100,
                hours=hour,
                minutes=minute,
                seconds=time_offset
            )
            
            timestamps.append(timestamp)
        
        return sorted(timestamps)

class ReportGenerator:
    """Generate comprehensive analysis reports"""
    
    @staticmethod
    def generate_privacy_report(df: pd.DataFrame, analysis_results: Dict) -> str:
        """Generate a comprehensive privacy analysis report"""
        report = []
        report.append("# Blockchain Privacy Analysis Report")
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Transactions: {len(df)}")
        report.append("")
        
        # Executive Summary
        report.append("## Executive Summary")
        avg_privacy = df['anonymity_set_size'].mean()
        high_privacy_txs = len(df[df['privacy_level'] == 'high'])
        report.append(f"- Average anonymity set size: {avg_privacy:.1f}")
        report.append(f"- High privacy transactions: {high_privacy_txs} ({high_privacy_txs/len(df)*100:.1f}%)")
        report.append("")
        
        # Technique Analysis
        report.append("## Privacy Technique Analysis")
        technique_stats = df.groupby('technique_used').agg({
            'anonymity_set_size': 'mean',
            'computational_overhead': 'mean',
            'latency_ms': 'mean'
        }).round(2)
        
        for technique, stats in technique_stats.iterrows():
            report.append(f"### {technique.replace('_', ' ').title()}")
            report.append(f"- Average anonymity set: {stats['anonymity_set_size']:.1f}")
            report.append(f"- Average overhead: {stats['computational_overhead']:.2f}x")
            report.append(f"- Average latency: {stats['latency_ms']:.1f}ms")
            report.append("")
        
        # Recommendations
        report.append("## Recommendations")
        if avg_privacy < 20:
            report.append("- Consider increasing anonymity set sizes for better privacy")
        if len(df[df['computational_overhead'] > 2]) > len(df) * 0.1:
            report.append("- High computational overhead detected; consider optimization")
        
        return "\n".join(report)
    
    @staticmethod
    def generate_vulnerability_report(vulnerabilities: List[Dict]) -> str:
        """Generate a vulnerability assessment report"""
        report = []
        report.append("# Vulnerability Assessment Report")
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        if not vulnerabilities:
            report.append("## Summary")
            report.append("✅ No vulnerabilities detected!")
            return "\n".join(report)
        
        # Categorize vulnerabilities
        high_severity = [v for v in vulnerabilities if v.get('severity') == 'high']
        medium_severity = [v for v in vulnerabilities if v.get('severity') == 'medium']
        low_severity = [v for v in vulnerabilities if v.get('severity') == 'low']
        
        report.append("## Summary")
        report.append(f"- High severity: {len(high_severity)}")
        report.append(f"- Medium severity: {len(medium_severity)}")
        report.append(f"- Low severity: {len(low_severity)}")
        report.append("")
        
        # Detailed findings
        for severity, vulns in [('High', high_severity), ('Medium', medium_severity), ('Low', low_severity)]:
            if vulns:
                report.append(f"## {severity} Severity Vulnerabilities")
                for i, vuln in enumerate(vulns, 1):
                    report.append(f"### {i}. {vuln.get('type', 'Unknown')}")
                    report.append(f"**Description:** {vuln.get('description', 'No description')}")
                    if 'recommendation' in vuln:
                        report.append(f"**Recommendation:** {vuln['recommendation']}")
                    report.append("")
        
        return "\n".join(report)

def export_data(df: pd.DataFrame, filename: str, format: str = 'csv'):
    """Export data to various formats"""
    if format.lower() == 'csv':
        df.to_csv(filename, index=False)
    elif format.lower() == 'json':
        df.to_json(filename, orient='records', indent=2)
    elif format.lower() == 'excel':
        df.to_excel(filename, index=False)
    else:
        raise ValueError(f"Unsupported format: {format}")

def load_data(filename: str, format: str = 'csv') -> pd.DataFrame:
    """Load data from various formats"""
    if format.lower() == 'csv':
        return pd.read_csv(filename)
    elif format.lower() == 'json':
        return pd.read_json(filename)
    elif format.lower() == 'excel':
        return pd.read_excel(filename)
    else:
        raise ValueError(f"Unsupported format: {format}") 