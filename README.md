# Web Scraping User Data Analysis Tool

A comprehensive Python tool for scraping HTML tables, analyzing user data, and generating detailed reports with visualizations.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/pkscripts/web_scraper_bs4
   cd web-scraper-project
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
web-scraper-project/
│
├── web_scraper_project.py    # Main script
├── index.html               # Input HTML file
├── requirements.txt         # Project dependencies
├── README.md               # Documentation
│
└── reports/                # Generated reports directory
    ├── user_data_20240312_143022.csv
    ├── report_20240312_143022.json
    └── country_distribution_20240312_143022.png
```

## Features

1. **Data Extraction**
   - User ID and basic information
   - Contact details (email)
   - Geographic data (country)
   - Account status and join dates
   - Profile URLs and avatar images

2. **Report Generation**
   - CSV exports of raw data
   - JSON formatted analysis
   - Country-wise distribution charts
   - Statistical summaries

3. **Visualizations**
   - Bar charts for user distribution
   - Country-wise analysis graphs
   - Automated chart generation

## Usage

1. **Prepare Input File**
   - Place your HTML file named `index.html` in the project directory
   - Ensure it contains user data in table format with class="user-row"

2. **Run the Script**
   ```bash
   python web_scraper_project.py
   ```

## Example Output

1. **Console Output**
   ```
   Country-wise User Report:
   +---------------+------------------+-------------------------+
   | Country       | Number of Users | Users                   |
   +---------------+------------------+-------------------------+
   | United States | 25              | John Doe, Jane Smith... |
   | Canada        | 15              | Mike Ross, Rachel Z...  |
   | UK           | 10              | James Bond, Emma W...   |
   +---------------+------------------+-------------------------+

   Detailed Statistics:
   Total number of countries: 12
   Total number of users: 150
   Active users: 142
   Average users per country: 12.50

   Top 5 countries by number of users:
   United States: 25 users
   Canada: 15 users
   UK: 10 users
   Germany: 8 users
   France: 7 users

   Reports have been generated and saved in the 'reports' directory.
   ```

2. **Generated Files**

   a. **CSV Report** (user_data_[timestamp].csv):
   ```csv
   id,name,email,country,join_date,status
   001,John Doe,john@example.com,United States,2024-01-15,active
   002,Jane Smith,jane@example.com,Canada,2024-01-16,active
   ...
   ```

   b. **JSON Report** (report_[timestamp].json):
   ```json
   {
     "country_wise": [
       {
         "Country": "United States",
         "Number of Users": 25,
         "Users": "John Doe, Jane Smith..."
       }
     ],
     "statistics": {
       "total_countries": 12,
       "total_users": 150,
       "active_users": 142,
       "average_users_per_country": 12.5
     }
   }
   ```

## Requirements

- Python 3.6+
- beautifulsoup4>=4.9.3
- tabulate>=0.8.9
- pandas>=1.3.0
- matplotlib>=3.4.3

## Error Handling

The script includes error handling for common issues:
- Missing input file
- Invalid HTML structure
- File permission errors
- Data extraction failures

## Troubleshooting

1. **File Not Found Error**
   ```
   Error: Could not find index.html
   Solution: Ensure index.html exists in the script directory
   ```

2. **Parse Error**
   ```
   Error: Unable to parse HTML content
   Solution: Verify HTML file format and encoding
   ```

3. **Permission Error**
   ```
   Error: Cannot create reports directory
   Solution: Check write permissions in the current directory
   ```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name
- GitHub: [@Pandiyaraj](https://github.com/pkscripts)
