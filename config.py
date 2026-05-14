"""
Configuration settings for the blockchain privacy simulation
"""

import os
from typing import Dict, Any

class SimulationConfig:
    """Configuration class for simulation parameters"""
    
    # Data generation settings
    DEFAULT_NUM_TRANSACTIONS = 1000
    MIN_TRANSACTIONS = 100
    MAX_TRANSACTIONS = 10000
    
    # Privacy technique parameters
    PRIVACY_TECHNIQUES = {
        'homomorphic_encryption': {
            'key_sizes': [1024, 2048, 4096],
            'default_key_size': 2048,
            'computation_factor': 0.001,
            'privacy_level': 'high'
        },
        'zero_knowledge_proofs': {
            'proof_sizes': [256, 512, 1024],
            'default_proof_size': 512,
            'verification_factor': 0.0005,
            'privacy_level': 'very_high'
        },
        'ring_signatures': {
            'ring_sizes': [5, 10, 20, 50],
            'default_ring_size': 10,
            'signature_factor': 0.064,
            'privacy_level': 'high'
        },
        'mixers': {
            'mixing_rounds': [1, 3, 5, 10],
            'default_rounds': 3,
            'delay_factor': 10,  # minutes per round
            'privacy_level': 'medium'
        },
        'stealth_addresses': {
            'address_length': 40,
            'overhead_factor': 0.2,
            'privacy_level': 'high'
        }
    }
    
    # Vulnerability detection thresholds
    VULNERABILITY_THRESHOLDS = {
        'low_anonymity': 5,
        'high_overhead': 3.0,
        'high_latency': 500,  # ms
        'repeated_amounts': 5,
        'temporal_pattern_threshold': 1.0  # standard deviations above mean
    }
    
    # Performance thresholds
    PERFORMANCE_THRESHOLDS = {
        'acceptable_latency': 200,  # ms
        'acceptable_overhead': 2.0,
        'minimum_anonymity': 10,
        'optimal_throughput': 1000  # transactions per second
    }
    
    # Machine learning parameters
    ML_PARAMETERS = {
        'random_forest': {
            'n_estimators': 100,
            'max_depth': 10,
            'random_state': 42
        },
        'isolation_forest': {
            'contamination': 0.1,
            'random_state': 42
        },
        'kmeans': {
            'n_clusters': 5,
            'random_state': 42
        },
        'pca': {
            'n_components': 2
        }
    }
    
    # Visualization settings
    VISUALIZATION_CONFIG = {
        'default_figsize': (10, 6),
        'color_palette': 'viridis',
        'max_points': 1000,  # for performance
        'animation_duration': 1000  # ms
    }
    
    # Real-time monitoring settings
    MONITORING_CONFIG = {
        'update_interval': 5,  # seconds
        'max_history': 1000,  # data points
        'alert_thresholds': {
            'privacy_drop': 0.2,
            'performance_degradation': 0.3,
            'vulnerability_increase': 0.5
        }
    }

class PrivacyLevels:
    """Privacy level definitions and scoring"""
    
    LEVELS = {
        'very_low': {
            'score': 0.0,
            'anonymity_set': 1,
            'description': 'No privacy protection'
        },
        'low': {
            'score': 0.25,
            'anonymity_set': 5,
            'description': 'Basic privacy protection'
        },
        'medium': {
            'score': 0.5,
            'anonymity_set': 20,
            'description': 'Moderate privacy protection'
        },
        'high': {
            'score': 0.75,
            'anonymity_set': 50,
            'description': 'Strong privacy protection'
        },
        'very_high': {
            'score': 1.0,
            'anonymity_set': 100,
            'description': 'Maximum privacy protection'
        }
    }
    
    @classmethod
    def get_level_by_score(cls, score: float) -> str:
        """Get privacy level based on score"""
        for level, config in cls.LEVELS.items():
            if score <= config['score']:
                return level
        return 'very_high'
    
    @classmethod
    def get_score_by_level(cls, level: str) -> float:
        """Get score based on privacy level"""
        return cls.LEVELS.get(level, {}).get('score', 0.0)

class SecurityLevels:
    """Security level definitions"""
    
    LEVELS = {
        'low': {
            'description': 'Basic security measures',
            'vulnerability_tolerance': 0.3,
            'recommended_techniques': ['mixers', 'stealth_addresses']
        },
        'medium': {
            'description': 'Standard security measures',
            'vulnerability_tolerance': 0.1,
            'recommended_techniques': ['ring_signatures', 'homomorphic_encryption']
        },
        'high': {
            'description': 'Advanced security measures',
            'vulnerability_tolerance': 0.05,
            'recommended_techniques': ['zero_knowledge_proofs', 'homomorphic_encryption']
        },
        'very_high': {
            'description': 'Maximum security measures',
            'vulnerability_tolerance': 0.01,
            'recommended_techniques': ['zero_knowledge_proofs']
        }
    }

class NetworkConfig:
    """Network topology and configuration"""
    
    # Network types
    NETWORK_TYPES = {
        'bitcoin': {
            'block_time': 600,  # seconds
            'max_block_size': 1000000,  # bytes
            'fee_structure': 'satoshi_per_byte'
        },
        'ethereum': {
            'block_time': 12,  # seconds
            'gas_limit': 15000000,
            'fee_structure': 'gas_price'
        },
        'monero': {
            'block_time': 120,  # seconds
            'ring_size': 11,
            'fee_structure': 'per_byte'
        },
        'zcash': {
            'block_time': 150,  # seconds
            'shielded_transactions': True,
            'fee_structure': 'per_byte'
        }
    }
    
    # Default network parameters
    DEFAULT_NETWORK = 'bitcoin'
    DEFAULT_BLOCK_TIME = 600
    DEFAULT_MAX_BLOCK_SIZE = 1000000

class OptimizationConfig:
    """Optimization algorithm parameters"""
    
    # Genetic algorithm parameters
    GENETIC_ALGORITHM = {
        'population_size': 50,
        'generations': 100,
        'mutation_rate': 0.1,
        'crossover_rate': 0.8,
        'elite_size': 5
    }
    
    # Particle swarm optimization parameters
    PARTICLE_SWARM = {
        'particles': 30,
        'iterations': 100,
        'cognitive_weight': 2.0,
        'social_weight': 2.0,
        'inertia_weight': 0.7
    }
    
    # Objective function weights
    OBJECTIVE_WEIGHTS = {
        'privacy': 0.4,
        'performance': 0.3,
        'security': 0.3
    }

class ExportConfig:
    """Export and reporting configuration"""
    
    # Supported export formats
    EXPORT_FORMATS = ['csv', 'json', 'excel', 'pdf']
    
    # Report templates
    REPORT_TEMPLATES = {
        'executive_summary': {
            'sections': ['overview', 'key_findings', 'recommendations'],
            'max_pages': 2
        },
        'technical_report': {
            'sections': ['methodology', 'results', 'analysis', 'conclusions'],
            'max_pages': 10
        },
        'vulnerability_report': {
            'sections': ['summary', 'findings', 'risk_assessment', 'remediation'],
            'max_pages': 5
        }
    }
    
    # Chart export settings
    CHART_EXPORT = {
        'formats': ['png', 'svg', 'pdf'],
        'dpi': 300,
        'transparent': False
    }

def get_config() -> Dict[str, Any]:
    """Get complete configuration dictionary"""
    return {
        'simulation': SimulationConfig,
        'privacy_levels': PrivacyLevels,
        'security_levels': SecurityLevels,
        'network': NetworkConfig,
        'optimization': OptimizationConfig,
        'export': ExportConfig
    }

def validate_config(config: Dict[str, Any]) -> bool:
    """Validate configuration parameters"""
    try:
        # Validate simulation config
        assert config['simulation'].DEFAULT_NUM_TRANSACTIONS > 0
        assert config['simulation'].MIN_TRANSACTIONS <= config['simulation'].MAX_TRANSACTIONS
        
        # Validate privacy techniques
        for technique, params in config['simulation'].PRIVACY_TECHNIQUES.items():
            assert 'privacy_level' in params
            assert params['privacy_level'] in config['privacy_levels'].LEVELS
        
        # Validate thresholds
        for threshold_name, value in config['simulation'].VULNERABILITY_THRESHOLDS.items():
            assert value >= 0
        
        return True
    except (AssertionError, KeyError) as e:
        print(f"Configuration validation failed: {e}")
        return False

# Environment-specific configurations
class DevelopmentConfig(SimulationConfig):
    """Development environment configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    CACHE_ENABLED = False

class ProductionConfig(SimulationConfig):
    """Production environment configuration"""
    DEBUG = False
    LOG_LEVEL = 'INFO'
    CACHE_ENABLED = True
    
    # Override some settings for production
    DEFAULT_NUM_TRANSACTIONS = 5000
    MAX_TRANSACTIONS = 50000

def get_environment_config(environment: str = None) -> SimulationConfig:
    """Get configuration based on environment"""
    if environment is None:
        environment = os.getenv('ENVIRONMENT', 'development')
    
    if environment.lower() == 'production':
        return ProductionConfig
    else:
        return DevelopmentConfig 