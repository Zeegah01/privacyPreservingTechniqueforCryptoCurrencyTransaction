"""
Sample data generator for blockchain privacy simulation
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import hashlib
import json

def generate_sample_blockchain_data(num_transactions=1000):
    """Generate realistic sample blockchain data"""
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Generate addresses
    addresses = []
    for i in range(200):  # Generate 200 unique addresses
        if random.random() < 0.7:  # Bitcoin-style addresses
            addr = f"1{hashlib.sha256(str(i).encode()).hexdigest()[:25]}"
        else:  # Ethereum-style addresses
            addr = f"0x{hashlib.sha256(str(i).encode()).hexdigest()[:40]}"
        addresses.append(addr)
    
    # Generate transactions
    transactions = []
    base_time = datetime.now() - timedelta(days=30)
    
    for i in range(num_transactions):
        # Generate realistic transaction amounts
        if random.random() < 0.6:  # Small transactions (60%)
            amount = np.random.exponential(10) + 0.001
        elif random.random() < 0.9:  # Medium transactions (30%)
            amount = np.random.normal(100, 50) + 0.01
        else:  # Large transactions (10%)
            amount = np.random.exponential(1000) + 10
        
        # Generate timestamp with realistic patterns
        if random.random() < 0.1:  # Burst of transactions
            time_offset = random.randint(0, 60)
        else:
            time_offset = random.randint(0, 24*60*60)
        
        # Add daily patterns (more activity during business hours)
        hour = random.randint(9, 17) if random.random() < 0.7 else random.randint(0, 23)
        minute = random.randint(0, 59)
        
        timestamp = base_time + timedelta(
            days=i//100,
            hours=hour,
            minutes=minute,
            seconds=time_offset
        )
        
        # Select privacy technique based on amount and time
        if amount > 1000:  # Large transactions use stronger privacy
            technique = random.choice(['homomorphic_encryption', 'zero_knowledge_proofs'])
            privacy_level = 'high'
            anonymity_set = random.randint(50, 100)
        elif amount > 100:  # Medium transactions
            technique = random.choice(['ring_signatures', 'stealth_addresses'])
            privacy_level = 'medium'
            anonymity_set = random.randint(20, 50)
        else:  # Small transactions
            technique = random.choice(['mixers', 'stealth_addresses'])
            privacy_level = 'low'
            anonymity_set = random.randint(1, 20)
        
        # Calculate overhead and latency based on technique
        overhead_factors = {
            'homomorphic_encryption': 4.0,
            'zero_knowledge_proofs': 5.0,
            'ring_signatures': 2.0,
            'mixers': 1.5,
            'stealth_addresses': 1.2
        }
        
        base_overhead = overhead_factors.get(technique, 1.0)
        computational_overhead = base_overhead + np.random.normal(0, 0.5)
        computational_overhead = max(0.1, computational_overhead)
        
        # Latency based on technique and amount
        base_latency = {
            'homomorphic_encryption': 200,
            'zero_knowledge_proofs': 300,
            'ring_signatures': 100,
            'mixers': 150,
            'stealth_addresses': 50
        }
        
        latency_ms = base_latency.get(technique, 100) + np.random.exponential(50) + 10
        
        transaction = {
            'tx_id': f'tx_{i:06d}',
            'timestamp': timestamp,
            'sender': random.choice(addresses),
            'receiver': random.choice(addresses),
            'amount': max(amount, 0.001),
            'fee': np.random.uniform(0.001, 0.1),
            'block_height': random.randint(1, 10000),
            'privacy_level': privacy_level,
            'technique_used': technique,
            'anonymity_set_size': anonymity_set,
            'computational_overhead': computational_overhead,
            'latency_ms': latency_ms
        }
        
        transactions.append(transaction)
    
    return pd.DataFrame(transactions)

def generate_vulnerable_data(num_transactions=500):
    """Generate data with known vulnerabilities for testing"""
    
    df = generate_sample_blockchain_data(num_transactions)
    
    # Introduce vulnerabilities
    vulnerable_indices = random.sample(range(len(df)), len(df) // 10)  # 10% vulnerable
    
    for idx in vulnerable_indices:
        if random.random() < 0.3:  # Low anonymity
            df.loc[idx, 'anonymity_set_size'] = random.randint(1, 3)
        elif random.random() < 0.3:  # High overhead
            df.loc[idx, 'computational_overhead'] = random.uniform(4.0, 8.0)
        elif random.random() < 0.3:  # High latency
            df.loc[idx, 'latency_ms'] = random.uniform(800, 2000)
        else:  # Repeated amounts
            df.loc[idx, 'amount'] = 100.0  # Common amount
    
    return df

def save_sample_data():
    """Save sample data to files"""
    
    print("Generating sample blockchain data...")
    
    # Generate normal data
    normal_data = generate_sample_blockchain_data(2000)
    normal_data.to_csv('sample_data_normal.csv', index=False)
    print(f"✅ Saved normal data: {len(normal_data)} transactions")
    
    # Generate vulnerable data
    vulnerable_data = generate_vulnerable_data(1000)
    vulnerable_data.to_csv('sample_data_vulnerable.csv', index=False)
    print(f"✅ Saved vulnerable data: {len(vulnerable_data)} transactions")
    
    # Generate summary statistics
    summary = {
        'normal_data': {
            'total_transactions': len(normal_data),
            'avg_amount': normal_data['amount'].mean(),
            'avg_anonymity': normal_data['anonymity_set_size'].mean(),
            'technique_distribution': normal_data['technique_used'].value_counts().to_dict()
        },
        'vulnerable_data': {
            'total_transactions': len(vulnerable_data),
            'avg_amount': vulnerable_data['amount'].mean(),
            'avg_anonymity': vulnerable_data['anonymity_set_size'].mean(),
            'technique_distribution': vulnerable_data['technique_used'].value_counts().to_dict()
        }
    }
    
    with open('sample_data_summary.json', 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    
    print("✅ Saved data summary")
    print("\n📊 Sample data generated successfully!")
    print("Files created:")
    print("  - sample_data_normal.csv")
    print("  - sample_data_vulnerable.csv")
    print("  - sample_data_summary.json")

if __name__ == "__main__":
    save_sample_data() 