<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/KfW_Bankengruppe_20xx_logo.svg/320px-KfW_Bankengruppe_20xx_logo.svg.png" alt="fff" align="left" style="width:150px;width:150px;align:left">



###  News Data Challenge

KfW is the promotional bank of the Federal Republic of Germany. The transformation of the economy and society to improve economic, ecological and social living conditions worldwide is KfW's primary objective. With a balance sheet of more than €500 billion KfW is the largest national promotional lender in the world and a reliable partner for small and midsize enterprises (SMEs), corporates and financial institutions worldwide. KfW’s ongoing regular operations span a wide array of promotional activities. They comprise lending to SMEs, energy efficiency and environmental protection, housing, infrastructure, and education, as well as project and export finance, and development cooperation. Hence, our credit analysts face the challenging task of assessing the credit risk – i.e. the possibility of a borrower defaulting on his debt – of a diverse cast of counterparties. As such they need to stay on top of current and past news developments on a global level.

Can you help them get a grip on the news?

### Data

You are provided with meta information on a set of entity articles published after 01.03.2022. Included data points are among others, a tag for the company mentioned in the original article as well as the id tag for the company’s parent industry. Furthermore, you are provided with a measure of the company’s relevance within the article, a sentiment score for the semantic polarity of company mentions and a list of key words (lemmatized) found within the article body. Lastly, it can be ascertained whether an article was read or not.


	   
|  	 Column| Data Type 			| Description 												|  
|------|--------------------|-----------------------------------------------------------| 
|     ARTICLE_ID| integer	| Article identifier 										|  
|     COMPANY_ID| integer			| Company identifier			|  
|     PUBLICATION_DATE| Datetime    | Date of article publication	|  
|     INDUSTRY_ID| integer			| Industry identifier for matched company	|  
|     SOURCE_ID| integer			| Source identifier for the article 						|  
|     KEY_WORDS_FOUND| string		| Lemmas of identified analyst key words       			| 
|     SENTIMENT| numeric			| Aggregate measure of semantic polarity for company mentions| 
|     RELEVANCE| numeric			| measure of the company’s relevance within the article		| 
|     BOOL_ARTICLE_READ| boolean	| Indicator of whether an article was read or not    		|

### Challenge Goals

*Analyze the data in order to provide useful insights*

Employ your knowledge of descriptive analysis to create visualizations and/or tables which highlight news events containing coverage peaks for certain companies/special topics or other anomalies/patterns/cluster in the news article data..

*Predict the likelihood of an article being read by a credit analyst*

Predict the likelihood of an article being read using a predictive model trained on the data points provided. Be mindful of and employ strategies accordingly when dealing with an unbalanced data set.
Your model will be evaluated against a validation sample.