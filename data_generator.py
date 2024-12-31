import random

# Lists for generating random data
first_names = ['John', 'Emma', 'Liu', 'Maria', 'Hans', 'Sophie', 'Alessandro', 'Yuki', 'Anna', 'Mohammed', 
               'James', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'George', 'Oscar', 'William']

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
              'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']

countries = ['United States', 'United Kingdom', 'Canada', 'Australia', 'Germany', 'France', 'Spain', 'Italy', 
            'Japan', 'China', 'India', 'Brazil', 'Mexico', 'Russia', 'South Korea', 'Netherlands', 'Sweden', 
            'Norway', 'Poland', 'Egypt']

# Generate 100 rows of data
for i in range(1, 101):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    country = random.choice(countries)
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    
    print(f'''                <tr class="user-row">
                    <td>{i}</td>
                    <td>{first_name} {last_name}</td>
                    <td>{email}</td>
                    <td>{country}</td>
                </tr>''')