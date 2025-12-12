# Kangaroo - Bitcoin Puzzle Analysis Tool

A Windows-based tool for analyzing and solving Bitcoin puzzles, combining a high-performance C/C++ core with a Python dashboard interface.

## ✨ Features

- **High-Performance Core**: Optimized C/C++ executable for maximum speed
- **Python Dashboard**: User-friendly Plotly-based monitoring interface
- **Progress Tracking**: Real-time execution monitoring and statistics
- **Checkpoint System**: Save and resume execution
- **Dynamic Configuration**: Easy puzzle list management
- **Error Tracking**: Comprehensive error logging and reporting
- **24/7 Operation**: Designed for continuous operation

## 🛠️ Technologies

- **C/C++**: Core solver (Kangaroo.exe)
- **Python 3.8+**: Dashboard and management
- **Plotly**: Data visualization
- **Flask**: Web server
- **JSON**: Configuration and state management

## 📦 Installation

### Prerequisites
- Windows 7 or later
- Python 3.8 or higher (for dashboard)
- ~1.2 GB disk space

### Setup

1. Clone the repository:
```bash
git clone https://github.com/lucasandre16112000-png/09-kangaroo.git
cd 09-kangaroo
```

2. (Optional) Create Python virtual environment for dashboard:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running Kangaroo

### Quick Start
Double-click `INICIAR.bat` to start with default settings.

### Manual Start
```bash
Kangaroo.exe
```

### Start Dashboard
```bash
python painel_kangaroo_FINAL.py
```

Access dashboard at `http://localhost:5000`

## ⚙️ Configuration

### Edit Puzzle List
Modify `all_puzzles.txt` to add or remove puzzles:
```
puzzle_address_1
puzzle_address_2
puzzle_address_3
```

### Advanced Settings
Edit `GUIA_COMPLETO.txt` for detailed configuration options.

## 📊 Dashboard Features

- **Real-Time Stats**: Processing speed, puzzles tested, elapsed time
- **Progress Tracking**: Percentage complete and estimated time remaining
- **Error Log**: Recent errors for troubleshooting
- **Control Panel**: Pause, resume, and stop execution
- **History**: Previous execution records

## 🔄 How It Works

1. **Initialization**: Loads puzzle list and configuration
2. **Processing**: C/C++ core tests combinations at high speed
3. **Monitoring**: Python dashboard tracks progress
4. **Checkpointing**: Saves state every 5 minutes
5. **Reporting**: Generates statistics and logs

## 📁 Project Structure

```
.
├── Kangaroo.exe                    # Core solver
├── painel_kangaroo_FINAL.py       # Dashboard
├── TESTAR_SALVAMENTO.py           # Checkpoint validator
├── all_puzzles.txt                # Puzzle list
├── INICIAR.bat                    # Quick start script
├── GUIA_COMPLETO.txt              # Full guide
└── README.md                      # This file
```

## 🔒 Security

- Private keys stored locally only
- Secure checkpoint system
- No external network communication
- Comprehensive logging

## 📈 Performance

- **Speed**: Depends on CPU and puzzle complexity
- **Memory**: Efficient memory usage
- **Stability**: Designed for long-running operations
- **Reliability**: Automatic checkpoint recovery

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Lucas André - [GitHub](https://github.com/lucasandre16112000-png)

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Use at your own risk.
