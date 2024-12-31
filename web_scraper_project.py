"""
##########################################
# Web Scraping User Data Analysis Tool
##########################################

A Python-based web scraping tool that extracts user data from HTML tables 
and generates comprehensive reports and visualizations.

Author: PandiyarajK
GitHub: @pkscripts
License: MIT

Requirements:
- beautifulsoup4>=4.9.3
- tabulate>=0.8.9
- pandas>=1.3.0
- matplotlib>=3.4.3

Usage:
1. Install dependencies: pip install -r requirements.txt
2. Place index.html in the same directory
3. Run: python web_scraper_project.py
"""

from bs4 import BeautifulSoup
from collections import defaultdict
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os

class WebScraper:
    """Main scraper class that handles all scraping and reporting functionality"""
    
    def __init__(self, input_file='index.html'):
        self.input_file = input_file
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
    def read_and_parse_html(self):
        """Read and parse HTML file using BeautifulSoup"""
        with open(self.input_file, 'r', encoding='utf-8') as file:
            return BeautifulSoup(file.read(), 'html.parser')

    def extract_user_data(self, soup):
        """Extract user data from HTML soup"""
        user_data = []
        user_rows = soup.find_all('tr', class_='user-row')
        
        for row in user_rows:
            columns = row.find_all('td')
            # Extract text and strip whitespace
            user = {
                'id': columns[0].text.strip(),
                'name': columns[1].text.strip(),
                'email': columns[2].text.strip(),
                'country': columns[3].text.strip(),
                'join_date': columns[4].text.strip() if len(columns) > 4 else 'N/A',
                'status': columns[5].get('class', [''])[0] if len(columns) > 5 else 'unknown'
            }
            
            # Extract any links associated with the user
            links = row.find_all('a')
            user['profile_url'] = links[0].get('href') if links else None
            
            # Extract any images (e.g., user avatars)
            images = row.find_all('img')
            user['avatar_url'] = images[0].get('src') if images else None
            
            user_data.append(user)
        
        return user_data

    def generate_reports(self, user_data):
        """Generate various reports from user data"""
        # Convert to DataFrame for easier analysis
        df = pd.DataFrame(user_data)
        
        # Create reports directory if it doesn't exist
        os.makedirs('reports', exist_ok=True)

        # 1. Country-wise Summary
        country_summary = df.groupby('country').agg({
            'id': 'count',
            'name': lambda x: ', '.join(x)
        }).reset_index()
        country_summary.columns = ['Country', 'Number of Users', 'Users']

        # 2. Generate Various Reports
        reports = {
            'country_wise': country_summary.to_dict('records'),
            'statistics': {
                'total_countries': len(df['country'].unique()),
                'total_users': len(df),
                'active_users': len(df[df['status'] == 'active']),
                'average_users_per_country': len(df) / len(df['country'].unique())
            },
            'top_countries': df['country'].value_counts().head(5).to_dict()
        }

        # 3. Save reports to files
        self._save_reports(df, reports)
        
        # 4. Generate Visualizations
        self._generate_visualizations(df)

        return reports, country_summary

    def _save_reports(self, df, reports):
        """Save reports to files"""
        # CSV Export
        df.to_csv(f'reports/user_data_{self.timestamp}.csv', index=False)
        
        # JSON Export
        with open(f'reports/report_{self.timestamp}.json', 'w') as f:
            json.dump(reports, f, indent=4)

    def _generate_visualizations(self, df):
        """Generate visualizations from the data"""
        plt.figure(figsize=(12, 6))
        df['country'].value_counts().plot(kind='bar')
        plt.title('Users by Country')
        plt.xlabel('Country')
        plt.ylabel('Number of Users')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'reports/country_distribution_{self.timestamp}.png')
        plt.close()

    def print_reports(self, reports, country_summary):
        """Print formatted reports to console"""
        # Print the summary table
        print("\nCountry-wise User Report:")
        print(tabulate(country_summary, 
                      headers='keys',
                      tablefmt='grid'))

        # Print detailed statistics
        print("\nDetailed Statistics:")
        stats = reports['statistics']
        print(f"Total number of countries: {stats['total_countries']}")
        print(f"Total number of users: {stats['total_users']}")
        print(f"Active users: {stats['active_users']}")
        print(f"Average users per country: {stats['average_users_per_country']:.2f}")

        # Print top countries
        print("\nTop 5 countries by number of users:")
        for country, count in reports['top_countries'].items():
            print(f"{country}: {count} users")

    def run(self):
        """Main execution method"""
        try:
            # Parse HTML
            soup = self.read_and_parse_html()
            
            # Extract data
            user_data = self.extract_user_data(soup)
            
            # Generate reports
            reports, country_summary = self.generate_reports(user_data)
            
            # Print reports
            self.print_reports(reports, country_summary)
            
            print("\nReports have been generated and saved in the 'reports' directory.")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def create_requirements_file():
    """Create requirements.txt file"""
    requirements = """beautifulsoup4>=4.9.3
tabulate>=0.8.9
pandas>=1.3.0
matplotlib>=3.4.3"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)

def create_readme():
    """Create README.md file"""
    readme = """# Web Scraping User Data Analysis Tool

A Python-based web scraping tool that extracts user data from HTML tables and generates comprehensive reports and visualizations.

## Features

- Extracts user data (ID, Name, Email, Country, etc.)
- Generates detailed reports and visualizations
- Creates CSV, JSON, and PNG outputs
- Interactive console output

## Installation & Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Place your HTML file (named `index.html`) in the same directory
3. Run the script:
   ```bash
   python web_scraper_project.py
   ```

## Output

Check the `reports` directory for generated files:
- user_data_[timestamp].csv
- report_[timestamp].json
- country_distribution_[timestamp].png

## License

MIT License
"""
    with open('README.md', 'w') as f:
        f.write(readme)

if __name__ == "__main__":
    # Create supporting files
    create_requirements_file()
    create_readme()
    
    # Run the scraper
    scraper = WebScraper()
    scraper.run() 
