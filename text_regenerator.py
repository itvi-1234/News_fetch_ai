import os 
import groq
from dotenv import load_dotenv 
from groq import Groq
import re
import csv

class Replygenerator:

    """Class to regenerate data for the leads"""

    def __init__(self):
        load_dotenv()
        groq_api_key = os.getenv("GROQ_API_KEY")

        if not groq_api_key:
            raise ValueError("groq_api_key not found")
        
        self.provider = "groq"
        
        self.api_key = groq_api_key

        self.llm_client = Groq(api_key = groq_api_key)

        self.model_name = "deepseek-r1-distill-llama-70b" 

        self.system_prompt = """ 
                paraphase and slightely expand the given text in Hindi language , by keeping the core meaning same,
                Remove timestamps and other unnecessary information
                return **ONLY** the regenerated text without thinking process
        """

    def generate_response(self, query : str) -> str:

        messages = [
            {"role": "system" , "content" : self.system_prompt},
            {"role" : "user" , "content" : query}
        ]

        response = self.llm_client.chat.completions.create(
            messages=messages,
            model=self.model_name,
            temperature=0.3,
            max_tokens=6000, # Use max_tokens for Groq
        )

        reply = response.choices[0].message.content.strip()
    
        return self.clean_response(reply)
    
    def clean_response(self, text: str) -> str:
        text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', '', text)
        return text.strip()
    
def write_regenerated_csv(filename , keys : list):

    """
    Writes the regenerated data to the csv file

    Args:
        filename (str): Name of the csv file to write to
        keys (list): List of keys to write to the csv file

    Returns:
        None

    functionality: Reads the existing csv file, checks for duplicates, and writes the new regernerated leads to the csv file
    """

    bot = Replygenerator()

    output_filename = f"{filename}_regenerated.csv"

    if os.path.exists(filename):
        with open(filename , 'r' , encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i , row in enumerate (reader , start = 1):
                print(f"processing {i}th record")
                headline = row['headline']
                summary = row['summary']
                Area = row['Area']

                if (headline == 'N/A' or summary == 'N/A'):
                    continue
                
                new_headline = bot.generate_response(headline)
                new_summary = bot.generate_response(summary)

                new_row = {'Area' : Area ,'headline' : new_headline , 'summary' : new_summary}

                #make a new file to save the regenerated data
                file_exists = os.path.exists(output_filename)
                with open(output_filename , 'a' , newline = '' , encoding = 'utf-8') as f:
                    writer = csv.DictWriter(f , fieldnames = keys)

                    if not file_exists:
                        writer.writeheader()

                    writer.writerow(new_row)
