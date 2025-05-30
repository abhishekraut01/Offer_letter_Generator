## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/offer-letter-generator.git
   cd offer-letter-generator
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your data and template**
   - Place your `candidates.csv` inside the `data/` folder.
   - Place your Word template `offer_letter_template.docx` inside the `templates/` folder.

5. **Run the script**
   ```bash
   python main.py
   ```

📂 Generated `.docx` and `.pdf` files will be saved in:

- `output/docx/` – Word offer letters  
- `output/pdf/` – PDF offer letters
