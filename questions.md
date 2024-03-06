#### 1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

To build and run the application, I chose Docker, because it simplifies these processes, since, having the files with these configurations, a simple command is enough to build or run the app.

As a framework, I chose to use FastAPI, due to its high performance and simplicity to create APIs.

To load data from CSV files, I chose to use Python generators, because it reduces the memory usage of the application, as the data is not loaded into memory all at once, but rather, loaded as they are iterated.

Regarding the organization of the application, at the root, there are the Docker configuration files, `gitignore` and the Markdown files (`questions.md` and `README.md`). The application itself is inside the `legislative_data` module, which is separated into the following files and directories:
- **main:** Main API execution file
- **data:** CSV files that will be loaded
- **routers:** Endpoints that will return data from searches made in CSV files
- **templates:** HTML files that act as a return from endpoints
- **utils:** Properties (functions, constants, exceptions, etc.) necessary for the application working
This organization makes it easier for anyone working on the code to understand the responsibility of each file or function, since everything is also documented through docstrings.

#### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or“Co-Sponsors”?

Looking at the functions `legislator_bill_votes` and `bills_supporters_and_opposers`, that are responsible to generate list in which every element is an item represented by a dictionary, firstly, I would add these new columns in these dictionaries and then, I would create a logic (this could be a new function or even a code inside the function) to load these information came from the CSV file. If the information was missing in some item of the CSV, the value added in the dictionary would be a default value, like "Not informed", for exemplo.

#### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

I would create endpoints that, when receive a list of legislators or bills, would make the necessary transformations in the data and would export a CSV with these information.
To export this CSV, the class `DictWriter`, from `csv` library could be used, by adding all the information in a file and making it available for download in the application HTML template.

#### 4. How long did you spend working on the assignment?

Around 6 hours
