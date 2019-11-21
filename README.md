<h2>PROJECT DESCRIPTION.</h2>
<h2>DATA VISUALIZATION AND MACHINE LEARNING</h2>

This project project uses two data sets. All the data sets have been visualized and presented in either plots, charts or graphs whereas one data set has been used for machine learning purpose.

<h2>DATA SETS USED.</h2>

<h2>VISUALIZATION</h2>

<h3>Data sets used:</h3>

<h4>1.online_retail.csv</h4>
This data set has information for online retail transactions for various countries for a store in the United Kingdom. It shows the number of transactions made by individuals from specified countries.

The data has the following columns:

1. Invoice
2. Stock Code: A unique number that identifies with the product
3. Description: Description of the product
4. Quantity: Number of products ordered
5.Invoice Date: The date of the invoice
6. Price: The price for the commodity ordered
7. Customer ID: Unique Identification of the customer
8. Country: The country from which the transaction was made

<h5>The data has been visualized as follows:</h5>

- Pi chart to show volume  in percentage of transactions per country.
- Two graphs that show quantity of distribution of transactions in 2011, and in July of 2011
- Bar chart to show quantity of online transactions by country
- Scatter plot showing distribution of quantity vs price
- A heat map that shows correlation in StockCode, Quantity, Price, Customer ID, Country
- A histogram showing distribution of price vs Quantity

<h4>2. african_crises.csv</h4>

The data shows the state of economy of thirteen African countries between the year 1870 to 2013.
The data has the following columns:

1. case: The order of countries in number i.e  case 1 is Angola
2. cc3: Code of the country
3. country: Names of the countries
4. year: respective year
5. systemic_crisis: 0 indicates crisis while 1 indicates no crisis
6. exch_usd: Shows the exchange rate in US dollars
7. domestic_debt_in_default: The domestic debt for particular countries
8. sovereign_external_debt_default: External debt for particular countries
9. gdp_weighted_default: gross domestic product
10. inflation_annual_cpi: Inflation based on consumer price index
11. independence: 0 indicates not inependent, 1 indicates independence
12. currency_crises: 0 indicates crisis, 1 indicates no crisis
13. inflation_crises: 0 indicates inflation crises, 1 indicates no crisis
14. banking_crisis: 0 indicates banking crises, 1 indicates no crises



<h5>The data has been visualized as follows:</h5>

- Two Pi charts  showing state of banking crisis and state of independence
- A heat map showing correlation in sovereign external debt, gross domestic product weighted default  and inflation annual consumer price index
- A histogram showing distribution of sovereign debt vs domestic debt
- Scatter plot showing year vs exchange rate in US dollars


<h2>MACHINE LEARNING</h2>

<h5> Data set used:</h5>
african_crises.csv

- Two subsets used – exch_usd, inflation_annual_cpi
- Method applied: Clustering
- Imported Kmeans from sklearn.cluster for clustering
- Centronoids for calculating the mean for clusters
- Generated an excel file to show the two columns.




