# 🚀 NEWS FETCH AI

An intelligent news scraping and lead generation tool that extracts news articles from popular Indian newspapers and enhances them using AI-powered text regeneration.

## ✨ Features

- **Multi-Source Scraping**: Supports Dainik Bhaskar and Amar Ujala newspapers
- **Smart Duplicate Detection**: Prevents duplicate entries using headline, summary, and area combinations
- **AI Text Enhancement**: Uses Groq's DeepSeek model to paraphrase and expand content in Hindi
- **Flexible Location Support**: Scrape news by state or city
- **CSV Export**: Organized data export with regenerated content
- **Automated Browser Control**: Selenium-based web scraping with ChromeDriver management

## 🏗️ Project Structure

```
ai-news-fetcher/
├── main.py                    # Main application entry point
├── page_scrapper.py           # Web scraping logic
├── write_to_csv.py           # CSV writing and duplicate handling
├── text_regenerator.py       # AI text processing using Groq
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create this)
├── README.md                 # Project documentation
├── {city}_new_leads.csv
└── {city}_new_leads.csv_regenerated.csv
```

## 🛠️ Requirements

- Python 3.8+
- Chrome Browser
- Groq API Key

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/News-fetch-ai.git
cd news-fetch-ai
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a `.env` file in the project root:

```bash
touch .env
```

Add your Groq API key to the `.env` file:
Go to Groq website 'GroqCloud' and create a free account and get your API key

```env
GROQ_API_KEY=your_groq_api_key_here
```

## 📋 Requirements.txt

```txt
selenium==4.15.2
webdriver-manager==4.0.1
groq==0.4.1
python-dotenv==1.0.0
csv
os
time
random
re
```

## 🚀 Usage

### Run the Application

```bash
python main.py
```

### Interactive Menu Options

1. **Choose Newspaper**:
   - `1` for Dainik Bhaskar
   - `2` for Amar Ujala

2. **Select Scope**:
   - `1` for State-wise news
   - `2` for City-wise news

3. **Enter Location**: Provide state/city name as prompted

### Example Workflow

```bash
$ python main.py

Welcome to News FETCH AI
====================

Which newspaper do u want to read?
1. Bhaskar
2. Amarujala
Hit 1 for Bhaskar and 2 for Amarujala
> 1

Do you want to read news about:
1.state 
2.city
Hit 1 for state and 2 for city
> 2

Enter the city name: kanpur
Enter the state the city belongs to: uttar-pradesh
```

## 🔧 How It Works

### 1. Web Scraping
- Uses Selenium WebDriver with Chrome
- Extracts headlines, summaries, and area information
- Handles dynamic content loading

### 2. Data Processing
- **Duplicate Detection**: Uses (headline, summary, area) as unique key
- **CSV Generation**: Creates structured output files
- **Error Handling**: Graceful handling of network and parsing errors

### 3. AI Enhancement
- **Text Regeneration**: Uses Groq's DeepSeek-R1-Distill-Llama-70B model
- **Hindi Language Support**: Paraphrases content while maintaining core meaning
- **Content Expansion**: Removes timestamps and unnecessary information

### 4. Output Files
- `{city}_new_leads.csv`: Original scraped data
- `{city}_new_leads.csv_regenerated.csv`: AI-enhanced content

## 🎯 Key Components

### Main Application (`main.py`)
- User interface and flow control
- WebDriver initialization and management
- URL construction for different newspapers

### Page Scraper (`page_scrapper.py`)
- CSS selector-based data extraction
- Lead processing and structuring
- Integration with CSV writer

### CSV Handler (`write_to_csv.py`)
- Duplicate prevention logic
- File management and appending
- Integration with text regenerator

### AI Text Processor (`text_regenerator.py`)
- Groq API integration
- Response cleaning and formatting
- Batch processing of regenerated content

## 🌟 What Makes This Project Great

### 🔍 Smart Data Extraction
- **Robust Selectors**: Uses reliable CSS selectors for consistent data extraction
- **Error Recovery**: Handles missing elements and network issues gracefully
- **Dynamic Content**: Waits for content to load before scraping

### 🧠 AI-Powered Enhancement
- **Content Quality**: Improves readability and removes noise from scraped text
- **Language Preservation**: Maintains Hindi language context and meaning
- **Scalable Processing**: Processes large datasets efficiently

### 📊 Data Management
- **Duplicate Prevention**: Intelligent deduplication prevents data redundancy
- **Structured Output**: Clean CSV format for easy analysis and integration
- **Incremental Updates**: Appends new data without overwriting existing records

### 🛡️ Production Ready
- **Environment Variables**: Secure API key management
- **Error Handling**: Comprehensive exception handling and logging
- **Resource Management**: Proper cleanup of browser resources

## 🔧 Configuration

### Supported Newspapers
- **Dainik Bhaskar**: `https://www.bhaskar.com/local/{state}/{city}`
- **Amar Ujala**: `https://www.amarujala.com/{state}/{city}`

### Chrome Options
```python
options.add_argument("--window-size=1024,720")
options.add_argument("--incognito")
options.add_experimental_option("detach", True)
```

## 🐛 Troubleshooting

### Common Issues

1. **ChromeDriver Issues**:
   ```bash
   # Update webdriver-manager
   pip install --upgrade webdriver-manager
   ```

2. **Groq API Errors**:
   - Verify your API key is correct
   - Check your API quota and rate limits

3. **Selenium Errors**:
   - Ensure Chrome browser is installed
   - Update Chrome to the latest version

### Debug Mode

Add debug prints in `page_scrapper.py`:
```python
print(f"Found {len(items)} news items")
for i, item in enumerate(items):
    print(f"Processing item {i+1}")
```

## 📈 Future Enhancements

- [ ] Support for more Indian newspapers
- [ ] Real-time news monitoring
- [ ] Sentiment analysis integration
- [ ] Database storage options
- [ ] REST API interface
- [ ] Docker containerization
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes. Please respect the terms of service of the websites you scrape and ensure compliance with applicable laws and regulations.

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ai-news-fetcher/issues) page
2. Create a new issue with detailed information
3. Include error messages and system information

---

**Made with ❤️ for the Indian news ecosystem**