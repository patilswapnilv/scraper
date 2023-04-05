# Scraper
This project aims to scrape blog posts from a blogger website, extract their content and metadata, and rewrite the content using the OpenAI API to remove plagiarism. The project consists of a front-end React application that accepts user inputs and communicates with the back-end Python scripts using REST API. The back-end is responsible for the scraping and rewriting of blog posts.

## Tech Used
ReactJS for front-end
Python and Scrapy for back-end
Flask for building REST API
OpenAI API for text rewriting
Pytest for testing

## File Structure
```
blog-scraper-and-rewriter
├── backend
│ ├── BlogScraper.py
│ ├── ContentRewriter.py
│ ├── init.py
│ ├── items.py
│ ├── middlewares.py
│ ├── pipelines.py
│ └── settings.py
├── frontend
│ ├── public
│ │ ├── index.html
│ │ ├── manifest.json
│ │ └── robots.txt
│ ├── src
│ │ ├── App.js
│ │ ├── App.test.js
│ │ ├── index.js
│ │ ├── reportWebVitals.js
│ │ └── setupTests.js
│ ├── .gitignore
│ ├── package-lock.json
│ ├── package.json
│ └── README.md
├── tests
│ ├── backend
│ │ ├── init.py
│ │ ├── test_BlogScraper.py
│ │ └── test_ContentRewriter.py
│ └── frontend
│ ├── init.py
│ └── test_App.js
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```


## Getting the Code Working
- Clone the repository to your local machine.
- Install the dependencies for the backend by running:
<code> pip install -r requirements.txt </code>
- Install the dependencies for the frontend by running:
<code> npm install </code>inside the frontend directory. 
- Start the backend server by running:
<code> python backend/BlogScraper.py</code>
- Start the frontend by running:
<code> npm start inside the frontend directory.</code>
- Access the application at </code> http://localhost:3000 </code> in your web browser.


-----

#