Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

#### History About DBT:



Data Maturity Model:

	Data Collection
	Data Wrangling
		The process of transforming raw data into a usable format for analysis, like cleaning, structuring, merging.
	Data Integration
	BI and Analytics
	Artificial Intelligence

ETL vs ELT:

  Tradition approach was ETL where transformation was done before loading the data into the database because the storage and compute resources was very costly.

  Today ELT is preferred because of cloud computing is available and the resources has become very cheap.

  EL part is done by Fivetran and Stich and for transformation we can make use of DBT.


Data Warehouse:

	Organized sets of structured data that are typically more performant than data lakes, but can be more expensive and limited in their ability to scale
	1. On-Premise:
		Oracle
		IBM
		teradata
	
	2. Cloud:
		Snowflake
		Redshift
		BigQuery

Data Lake:

	It's a centralized repository that stores, processes, and secures large amount of data in it's original format.
	Data lakes can store data from any source, in any type or volume, and in any structure. They can be used to power big data analytics, machine learning, predictive analytics, and other forms of intelligent action.

Data Lakehouse:

	A data lakehouse is a data management platform that combines the best features of data lakes and data warehouses:
	A data lakehouse offers a unified platform for storing and analyzing structured and unstructured data. It can help organizations: establish a single source of truth, eliminate redundant costs, ensure data freshness, and avoid isolated systems for processing different workloads.
	
	Scalable storage and processing
	Direct querying
	Separation of storage and compute resources

Evolution of Modern Data Stack

	1. SMP Data warehouses:
			Symmetric Multiprocessing:
				A symmetric multiprocessing system contains multiple processors that share the same memory and operate under a single OS. This architecture enables each processor to work on any task by accessing all I/O devices and data paths, regardless of the location of the data for that task in the centralized memory bank.

	2. Rise of MPP Cloud data warehouses:
			Massively Parallel Processing
			Azure Synapse Analytics SQL Pool
			Amazon Redshift Manged storage
			Google BigQuery storage
			Snowflake computing storage
	The main difference between SMP and MPP is the system design. In an SMP system, each processor shares the same resources. In an MPP system, each processor has its own dedicated resources and shares nothing. In other words, an SMP system has tightly coupled processors, and an MPP system has more loosely coupled processors.
	
	The other key distinction between the two systems lies in the "M" of MPP: massively. Because each processor uses its own OS and memory, you can set up hundreds of processors in an MPP setup, which enables you to crunch massive amounts of data in parallel.


ETL to ELT:

  The modern Data Stack in the AI era:
  Data source(Google Analytics, LinkedIn, Shopify, etc)  --> Extract/Load(Fivetran, stich, airbyte) --> Transform(dbt)  --> BI Tools(Power BI, Tableau)


SCD (Slowly Changing Dimensions):

  Slowly Changing Dimensions (SCD) are a critical concept in data warehousing and business intelligence. They refer to the methods used to manage and track changes in dimension data over time. This is essential for maintaining historical accuracy and ensuring data integrity in a data warehouse.

  Slowly Changing Dimensions are those parts of the data warehousing structures that change on an irregular basis and not on fixed time intervals. They record and preserve past alterations in data including alterations in the client’s residence or phone contacts. SCDs play a significant role in keeping up-to-date records for analysis, reporting, and decision-making for current and future use. 

Types of Slowly changing dimensions and implementation:

	Type 0: Fixed Dimensions
	Type 1: Overwrite
	Type 2: Add new row
	Type 3: Add new attribute
	Type 4: History table

DBT:

Models:

CTEs:

Materializations:

  1. View (Default): Lightweight model, use it when you don't reuse data too often.
  2. Table: Use it when you read from this model repeatedly
  3. Incremental: (Table Appends) Use it with fact tables where data is coming incrementally and we are not dealing with updating historical data.
  FULL-REFRESH
  4. Ephermal (CTEs): you merely want to alias your date



Sources and Seeds:

	Seeds are local files that you upload to data warehouse from dbt. (dbt seed)
	
	Sources is an abstraction layer on the top of your input tables. (define a sources.yml file in models folder and configure table name and their identifier and then later refer them in models using source macro) 
	
	Source freshness can be checked automatically. (dbt source freshness)

Snapshots:

	It lives in snapshots folder. (dbt snapshot)
	Strategies:
		Timestamp:
			A unique key and an update_at field is defined on the source model. These columns are used for determining changes.
		Check:
			Any change in a set of columns (or all coloumns) will be picked up as an update.


Tests:

	1. Singular:
		Singular tests are sql queries stored in tests which are expected to return an empty resultset
	2. Generic:
		unique
		non-null
		accepted_values
		relationship

	We can also define our own custom generic test or import tests from dbt packages.

Macros:

	understand how macros are created:
	use macros to implement your own generic tests:
	find and install third-party dbt packages:

Documentation:

	It can be defined in two ways:
		1. yaml files (like schema.yml)
		2. In standalone markdown files

	Dbt ships with a lightweight Documentation web server
	For customizing the landing page, a special file, overview.md is used.
	You can add your own assets(like images) to a special project folder.