# Table of Contents
- [CalPal - Calorie Calculator](#calpal---calorie-calculator)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

# CalPal - Calorie Calculator
A Python-based command-line application for calculating daily calorie intake and visualizing trends over time. Leverages user input or CSV data to compute totals and outputs visual charts using Matplotlib.

![GitHub](https://img.shields.io/github/license/code-by-sahib/CalPal-Calorie-Calculator)

## Features
- Calculate total calories from user-entered meals or from a CSV file  
- Compute Basal Metabolic Rate (BMR) and maintenance calories  
- Generate line and bar charts of calorie intake over days  
- Save visualizations as PNG images  
- Interactive menu-driven CLI  

## Requirements
- Python 3.6 or higher  
- matplotlib  
- pandas  
- numpy  

## Installation
1. Clone the repository  
   ```bash
   git clone https://github.com/code-by-sahib/CalPal-Calorie-Calculator.git
   ```
2. Navigate to the Code directory  
   ```bash
   cd CalPal-Calorie-Calculator/Code
   ```
3. Install dependencies  
   ```bash
   pip install matplotlib pandas numpy
   ```

## Usage
- **Interactive mode**  
  ```bash
  python main.py
  ```
  Follow on-screen prompts to enter meals and calories.
- **CSV mode**  
  ```bash
  python main.py --input path/to/calories.csv
  ```
  Ensure CSV has columns `date,food,calories`.  
- Output charts are saved in the `output/` folder.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/XYZ`)  
3. Commit changes (`git commit -m "Add XYZ feature"`)  
4. Push branch (`git push origin feature/XYZ`)  
5. Open a pull request  

---

## License
```
MIT License

Copyright (c) 2025 Sahib Ahluwalia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall 
be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE.
```

---

## Acknowledgements
- Developed as part of personal Python projects to practice data analysis and visualization.

---

## Contact
For questions or feedback, please reach out via e-mail: sahib.ahluwalia@torontomu.ca

