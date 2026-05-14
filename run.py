#!/usr/bin/env python3
"""
Launcher script for the Blockchain Privacy Simulation
"""

import subprocess
import sys
import os

def main():
    """Launch the Streamlit application"""
    try:
        # Check if streamlit is installed
        import streamlit
        print("🚀 Starting Blockchain Privacy Simulation...")
        print("📊 Opening in your default web browser...")
        
        # Launch the app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
        
    except ImportError:
        print("❌ Streamlit is not installed!")
        print("📦 Please install requirements first:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Simulation stopped by user")
    except Exception as e:
        print(f"❌ Error starting simulation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 