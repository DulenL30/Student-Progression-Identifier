# Student Progression Identifier

A Python application that tracks university student progression outcomes based on credit accumulation at different performance levels (pass, defer, fail). The program collects student data, determines progression outcomes, saves results to a file, and displays statistics via a graphical histogram.

## 📌 Features

- Input validation for student credits
- Calculates student progression outcomes:
  - Progress
  - Trailer
  - Retriever
  - Exclude
- Saves outcomes to a file
- Displays stored data
- Draws a histogram using the `graphics.py` module (Tkinter-based)

## 🛠️ Technologies Used

- Python 3
- Custom `graphics.py` library (based on Tkinter)

## 🚀 How to Run

### 🧑‍💻 Prerequisites

- Python 3.8+ (with Tkinter installed)
- `graphics.py` library (included in project)

> **Note for macOS (M1/M2):**  
> If you're using Homebrew Python, you may need to install Python with Tk support:

```bash
brew install python-tk
```

### Installation

1. Clone this repository:

```bash
git clone [your-repository-url]
cd Student-Progression-Identifier
```

2. The `graphics.py` library is already included in the project directory

### Usage

Run the program:

```bash
python w2052948_part1_3.py
```

### Input Process

1. When prompted, enter 'y' to input new student data or 'q' to quit and view results
2. Enter credits for pass, defer, and fail (must total 120)
3. Valid credit values: 0, 20, 40, 60, 80, 100, 120
4. The program will display the progression outcome and save the data

### Example Input Session

```
To enter another set of data enter 'y' for quit and view results enter 'q': y
Please enter your credits at pass,defer and fail.Total (120) must be entered.
Enter your credit at pass: 120
Enter your defer credit at defer: 0
Enter your fail credit at fail: 0
Progress
```

## File Structure

```
Student-Progression-Identifier/
├── __pycache__/                      # Python cache directory
├── graphics.py                       # Graphics library (28 KB)
├── w2052948_part1_3.py              # Main program file (5 KB)
├── Inputted_progression_data.txt     # Generated data file (created at runtime)
└── README.md                         # This file
```

## Core Functions

- **`get_user_inputs()`**: Handles user interaction and input validation
- **`calculate_all_results()`**: Determines progression outcome based on credits
- **`save_inputed_data()`**: Writes student data to text file
- **`display_inputed_data()`**: Reads and displays saved data
- **`display_histogram()`**: Creates graphical histogram of results

## Data Output

The program generates two types of output:

1. **Text File**: `Inputted_progression_data.txt` containing entries like:

   ```
   Pass: 120, Defer: 0, Fail: 0, Result: Progress
   Pass: 100, Defer: 20, Fail: 0, Result: Trailer
   ```

2. **Histogram Window**: Interactive graphical display showing:
   - Color-coded bars for each progression category
   - Student count for each outcome
   - Total number of students processed

## Error Handling

- **Invalid Credit Values**: "Out of Range" message for credits not in valid list
- **Incorrect Totals**: "Total Incorrect" message when credits don't sum to 120
- **Non-Integer Input**: "Integer Required" message for invalid data types
- **Missing Data File**: Graceful handling when no previous data exists

## Color Coding

The histogram uses the following color scheme:

- 🟢 **Green**: Progress
- 🟡 **Yellow**: Trailer (Progress with module trailer)
- 🟠 **Orange**: Retriever (Do not progress - module retriever)
- 🔴 **Red**: Exclude
