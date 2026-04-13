# Empire - Australian Investment Property Analyzer

A Python-based web application to help find the best investment properties in Australia by analyzing rental yield (cashflow) and equity growth potential.

## Features
- 🔍 Search properties from realestate.com.au and domain.com.au
- 💰 Calculate rental yield (cashflow) automatically
- 📈 Estimate equity growth potential
- 🎯 Filter by suburb, price, bedrooms, bathrooms, car parks
- 💾 Save and customize search criteria
- 📊 Compare multiple properties side-by-side

## Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML/CSS/JavaScript (Bootstrap)
- **Database**: PostgreSQL
- **Data Source**: Web scraping from Australian real estate sites

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/mkilmurray19-dotcom/Empire.git
cd Empire
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python setup_db.py
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and go to: `http://localhost:5000`

## Project Structure
```
Empire/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── config.py             # Configuration settings
├── setup_db.py           # Database initialization
├── scrapers/             # Web scraping modules
│   ├── realestate.py     # realestate.com.au scraper
│   └── domain.py         # domain.com.au scraper
├── models/               # Database models
│   └── property.py       # Property data model
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── search.html       # Search page
│   └── results.html      # Results page
├── static/               # CSS, JavaScript files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── utils/                # Utility functions
    ├── calculations.py   # Cashflow/yield calculations
    └── filters.py        # Search filtering logic
```

## Usage Guide

### Searching for Properties
1. Enter your search criteria (suburb, price range, bedrooms, etc.)
2. Select data sources (realestate.com.au, domain.com.au, or both)
3. Click "Search"
4. Review results sorted by cashflow or equity growth potential

### Calculating Cashflow
The app automatically calculates:
- **Rental Yield**: (Annual Rental Income / Property Price) × 100
- **Monthly Cashflow**: Monthly Rent - Monthly Expenses
- **ROI**: Return on investment based on your deposit

### Saving Searches
Save your custom search criteria for quick access later.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.