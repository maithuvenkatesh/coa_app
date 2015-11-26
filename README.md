Web Analytics Dashboard For Clean Ocean Action
======

##Abstruct
As non-profit organizations continue to face challenges in backing their respective initiatives to drive policy change and receive the necessary investment from both government and private sector sources, the increasing reliance on data to support their claims becomes fundamentally critical. That being said, non-profit organizations often lack the necessary resources internally to perform the required data science approaches and techniques to fully leverage the power behind the data the

#Introduction
In order to pilot this skills-based volunteer initiative, Bloomberg partnered with Clean Ocean Action (COA), an organization Bloomberg already had an extensive relationship with. Bloomberg has had a long time history of performing Beach Sweeps with COA since 2011. As of July 2015, 185 unique employees have dedicated almost 800 hours across 17 volunteer events.
- Clean Ocean Action: [http://www.cleanoceanaction.org](http://www.cleanoceanaction.org)
- Bloomberg Philanthropy: [http://www.cleanoceanaction.org](http://www.bloomberg.org)

#Schema Architecture
The first task of introducing the new data governance system was to thoroughly review the current data retrieval process in order to fully understand the data flow from beginning to end, as data could be deteriorated at any point of the process. To begin, we interviewed the COA and American Littoral Society staff as well as internal Bloomberg employees who participated in the COA beach clean-ups to identify the steps volunteers take to report the collected trash items from beaches and the procedures the COA staff follow to compile the data. Based on the observations and analysis of the 1993-2014 datasets, database schemas were developed in MySQL, for both its reputation and significant presence in the data science community.

#HIstorical Data Clenup
After designing the schemas, data munging was required. Due to the data volume and inconsistency, this process demanded a significant amount of time. Each year contained two Excel files with multiple sheets of detailed data collected by COA. Furthermore, there was little format consistency between files and the classified categories had changed overtime. Thus, there was no way to programmatically process these files and manual examination of each category and file was needed. Utilizing volunteer time at Bloomberg, the most recent years of the data were standardized and successfully transferred to the database. The remaining files will undergo a similar process during an upcoming “Bloomberg Datathon” event. After the schema design and significant data munging, a new data entry framework was needed for volunteers and COA to update collected items into the database. To solve this, we created a custom web application based solely on open source solutions so that COA could invest the resources for its core operations. For readability and future maintenance purposes, Python was our language choice and we utilized a micro web framework, Flask, as the backend. The front end was built on top of a popular open source solution, Bootstrap, so the site could be optimized for desktop computers and smartphones. This application will not only solve data entry and integrity problems but will function as a real time data analytics dashboard as well. As of September 2015, the application was successfully deployed from an internal Bloomberg web server to Amazon Web Services, more precisely, Amazon Relational Database Service and Elastic Beanstalk. WEB APPLICATION

##Web Application
After the schema design and significant data munging, a new data entry framework was needed for volunteers and COA to update collected items into the database. To solve this, we created a custom web application based solely on open source solutions so that COA could invest the resources for its core operations. For readability and future maintenance purposes, Python was our language choice and we utilized a micro web framework, Flask, as the backend. The front end was built on top of a popular open source solution, Bootstrap, so the site could be optimized for desktop computers and smartphones. This application will not only solve data entry and integrity problems but will function as a real time data analytics dashboard as well. As of September 2015, the application was successfully deployed from an internal Bloomberg web server to Amazon Web Services, more precisely, Amazon Relational Database Service and Elastic Beanstalk.