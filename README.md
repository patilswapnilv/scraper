# Scraper
Here's a list of all the files and folders in the project, along with a brief description of their purpose:
<code>
scraper/
│
├── backend/
│   ├── BlogScraper.py
│   ├── ContentRewriter.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   ├── manifest.json
│   │   └── robots.txt
│   └── src/
│       ├── components/
│       │   ├── Form.js
│       │   ├── Result.js
│       │   └── Navbar.js
│       ├── pages/
│       │   └── Home.js
│       ├── services/
│       │   └── ScraperService.js
│       ├── styles/
│       │   ├── index.css
│       │   └── Navbar.css
│       ├── App.js
│       ├── index.js
│       └── package.json
│
├── README.md
├── app.py
└── requirements.txt

</code>

`frontend/`: This folder contains the React JS app for the front-end.
`frontend/public/`: This folder contains the static files for the front-end.
`frontend/src/`: This folder contains the source code for the front-end app.
`frontend/package.json`: This file lists the dependencies for the front-end app.
`frontend/README.md`: This file contains the documentation for the front-end app.
`backend/`: This folder contains the Python scripts for the back-end.
`backend/BlogScraper.py`: This file contains the scrapy spider for scraping blogger websites.
`backend/Scraper.py`: This file contains the Scraper class for converting scraped content to different formats.
`backend/OpenAIScraper.py`: This file contains the OpenAIScraper class for rewriting content using the OpenAI API.
`backend/requirements.txt`: This file lists the dependencies for the Python scripts.
`backend/README.md`: This file contains the documentation for the Python scripts.
`README.md`: This file contains the documentation for the entire project.
`LICENSE`: This file contains the license information for the project.

To install the dependencies for the project, navigate to the backend/ folder and run the following command:

<code>
pip install -r requirements.txt
</code>

To execute the project, start by running the React app in the frontend/ folder:
<code>
cd frontend/
npm start
</code>

This will start the React app on port 3000.

Then, in a separate terminal, navigate to the backend/ folder and run the following command:
<code>
python BlogScraper.py
</code>

This will start the scrapy spider and begin scraping blogger websites.

Once the scraping is complete, run the following command to rewrite the content using the OpenAI API:
<code>
python OpenAIScraper.py
</code>

This will rewrite the content and save it in the specified format.


Project Description
This project aims to scrape blog posts from a blogger website, extract their content and metadata, and rewrite the content using the OpenAI API to remove plagiarism. The project consists of a front-end React application that accepts user inputs and communicates with the back-end Python scripts using REST API. The back-end is responsible for the scraping and rewriting of blog posts.

Tech Used
ReactJS for front-end
Python and Scrapy for back-end
Flask for building REST API
OpenAI API for text rewriting
Pytest for testing
File Structure
java
Copy code
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
Getting the Code Working
Clone the repository to your local machine.
Install the dependencies for the backend by running pip install -r backend/requirements.txt.
Install the dependencies for the frontend by running npm install inside the frontend directory.
Start the backend server by running python backend/app.py.
Start the frontend by running npm start inside the frontend directory.
Access the application at http://localhost:3000 in your web browser.



# Blog Scraper and Content Rewriter

This project allows users to scrape content from Blogger websites and rewrite it to remove plagiarism using the OpenAI API. The scraped content can be saved in various formats, including XML, JSON, and separate Markdown files for each post.

## Tech Stack

- ReactJS for the front-end
- Python (Scrapy) for the back-end
- OpenAI API for content rewriting
- Testing frameworks:
  - Jest for ReactJS
  - pytest for Python

## File Structure

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



## How to Run

1. Clone the repository:

git clone https://github.com/your-username/blog-scraper-and-rewriter.git

2. Install the dependencies:
<code>
cd blog-scraper-and-rewriter
pip install -r requirements.txt
cd frontend
npm install
</code>


3. Start the back-end:

<code>
cd ../backend
scrapy crawl blog_scraper
</code>


4. Start the front-end:
<code>
cd ../frontend
npm start
</code>


5. Open your web browser and navigate to `http://localhost:3000`.






