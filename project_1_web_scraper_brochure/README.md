# Web Scraper and Brochure Generator

## 📖 Project Overview
This project aims to scrape website content, analyze links, and generate a professional company brochure using OpenAI's API. It demonstrates how Python can be used for automation, natural language processing, and web scraping.

## 🗂️ File Structure
Planned files:
project_1_web_scraper_brochure/ ├── main.py # Entry point for running the project ├── website.py # Handles web scraping and link extraction ├── prompts.py # Contains OpenAI prompts ├── requirements.txt # Project dependencies └── README.md # Project documentation

## 🧩 Website Module
The `website.py` file defines a `Website` class that:
- Scrapes webpage content, titles, and links using BeautifulSoup.
- Removes unnecessary elements like scripts and images.

## 🧩 Prompts Module
The `prompts.py` file contains predefined templates for OpenAI's API to:
- Classify webpage links (e.g., "About Us", "Careers").
- Generate company brochures in Markdown format.

## 🧩 OpenAI Utilities Module
The `openai_utils.py` file provides utility functions to:
- Interact with OpenAI's GPT model for content generation.
- Analyze and categorize webpage links based on user-defined prompts.


## 🧩 Stream Module
The `stream.py` file implements streaming functionality to:
- Generate Markdown content in real time.
- Dynamically display updates during brochure generation.


## ⚙️ Installation
Coming soon...

## 📋 Example Output
Coming soon...

