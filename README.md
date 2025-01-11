# Weather Dashboard

## Overview
A robust weather data collection system that fetches real-time weather data using the OpenWeather API and automatically stores it in AWS S3. This project demonstrates modern DevOps practices through cloud integration, API handling, and infrastructure as code.

## Features
- Real-time weather data fetching for multiple cities
- Automatic data storage in AWS S3
- Temperature, humidity, and weather condition tracking
- Historical data tracking with timestamps
- Secure credential management
- Error handling and logging

## Technical Stack
- **Language:** Python 3.8+
- **Cloud Provider:** AWS (S3)
- **External API:** OpenWeather API
- **Key Libraries:** 
  - boto3 (AWS SDK)
  - requests
  - python-dotenv

## Project Structure
```
weather-dashboard-demo/
├── src/
│   ├── weather_dashboard.py       # Main application script
├── tests/
│   ├── test-api-key.py            # Script to validate API key
├── .env                           # Environment variables
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation

## Installation

1. **Clone the Repository**
   ```
   git clone https://https://github.com/cloudwithoyindamola/Weather-Dashboard
   cd weather-dashboard
2. **Install Dependenc**
 pip install -r requirements.txt
3. **Configure AWS CLI**
  aws configure
4. **Configure Environment Variables Create a .env file in the root directory:**
  OPENWEATHER_API_KEY=your_openweather_api_key
  AWS_ACCESS_KEY_ID=your_aws_access_key_id
  AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
  AWS_BUCKET_NAME=your_unique_bucket_name
  AWS_DEFAULT_REGION=your_preferred_aws_region
5. **Run the weather dashboard script**
  ```
  python src/weather_dashboard.py

#### The script will:

Create the specified S3 bucket if it does not exist.
Fetch weather data for predefined cities.
Save the fetched data as JSON files to the S3 bucket.

## Key Concepts
- AWS S3 Bucket Management: Creating, configuring, and managing S3 buckets for weather data storage using boto3.
- Environment Variables: Managing API keys and AWS credentials securely through environment variables and .env files.
- Python API Integration: Implementing best practices for fetching and processing weather data from OpenWeather API.
- Git Workflow: Following version control best practices with feature branches, meaningful commits, and proper documentation.
- Error Handling: Managing API failures, network issues, and AWS service errors with proper exception handling.
- Cloud Resource Management: Efficiently handling AWS resources including bucket lifecycle, permissions, and data organization.

Contributions are welcome! Please feel free to submit a Pull Request.