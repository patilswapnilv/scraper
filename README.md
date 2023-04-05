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
.
├── backend
│   ├── BlogScraper.py
│   ├── requirements.txt
│   ├── rewriter.py
│   └── tests
│       ├── test_blog_scraper.py
│       └── test_rewriter.py
├── frontend
│   ├── public
│   │   ├── index.html
│   │   └── ...
│   ├── src
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── components
│   │   │   ├── BlogForm.js
│   │   │   └── Result.js
│   │   ├── services
│   │   │   └── BlogService.js
│   │   └── ...
│   ├── package.json
│   └── ...
├── .gitignore
└── README.md
```


## Getting the Code Working
- Clone the repository to your local machine.
- Install the dependencies for the backend by running:
<code> pip install -r backend/requirements.txt. </code>
- Install the dependencies for the frontend by running:
<code> npm install inside the frontend directory. </code>
- Start the backend server by running:
<code> python backend/app.py.</code>
- Start the frontend by running:
<code> npm start inside the frontend directory.</code>
- Access the application at </code> http://localhost:3000 </code> in your web browser.


-----

#