# Background
<br />
A growing number of funds claim to be making sustainable investments, while investors are concerned about the risks associated with greenwashing due to the current lack of measurable standards in this area. Although there are several ESG scoring metrics proposed by rating agencies , these data are very scarce and expensive and the sources are often not transparent or objective enough, which sets a very high barrier for investors and greatly hinders relevant investments.
<br />
We believe that NLP could be useful in ESG investment strategy analysis, as such information is often presented in textual form in prospectuses, related news reports, and speeches. NLP can enhance ESG investing in a variety of ways. For example, NLP enables the large-scale tracking of controversies. Also, NLP can be combined with graph analytics to extract key strategic ESG initiatives and learn companies’ relationships in a global market and their impact on market risk calculations (Amend, A Data-driven Approach to Environmental, Social and Governance, 2020). (Vamvourellis, Toth, Desai, Mehta, & Pasquali, 2022)
<br />

# Methodology and Findings
<br />
In this project, we attempted to classify mutual funds by utilizing the FinBERT model. Then, we explored the trend of esg investment development based on the classification results. Additionally, we tried to perform feature extracting and topic modeling from the texts to construct a new ESG investment strategy taxonomy.
<br />

## 1. Labelling and Building Database
<br />
We pulled data from the table derived_sec_fund_characteristic in database common_goods to construct our own database. This table contains raw texts extracted from 13-F files. After filtering out the Null&NaN data, we can get 1600 files submitted by 1436 funds covering reporting periods from 2015 Q4 to 2022 Q2. After removing the duplicates, we get a sample of 6519 observations. This is a relatively small sample with many highly resemble objective and strategies description (Amend, A Data-driven Approach to Environmental, Social and Governance, 2020)ns, suggesting that we should use Zero-Shot-Learning or Few-Shot-Learning techniques in the classification. Also, we contacted the cleaned text string of objective and strategy to power the analysis. 
<br />
Next, the ESG-FinBERT model  pertained by researchers at HKUST is adopted to label the contacted objectives and strategies strings. The model could classify raw text into 9 categories: Climate Change, Pollution & Waste, Corporate Governance, Natural Capital, Product Liability, Human Capital, Business Ethics &Values, Community Relations and Non-ESG. According to researchers, their pretrained ESG-FinBERT model outperforms other NLP models when doing ESG classification, especially when training on smaller text samples containing financial words that are not commonly used in general texts. (Huang, Wang, & Yang, 2022) Another study (Pasch & Ehnes, 2022) also shows preference for BERT model when doing ESG classification tasks. However, this model is not perfect since is pre-trained, which means we should bear with the inflexibility. And though both researches mentioned that the models used were trained on ESG-related corpus, mainly news and listed companies’ ESG reports, our corpus does not necessarily feature overlapping features. To get better classification results, we should have fine-tuned the pretrained model.
<br />
The labelled data was stored in our database as table fund_objectives_strategy_with_labels in database common_goods (Table 1).
<br />

## 2. Exploratory Data Analysis
<br />
After filtering out abnormal and meaningless data and only keep the last entries, we still have 1583 observations. These observations cover the reporting period from consecutive 8 years from 2015 to 2022, and are labelled as 6 categories: Corporate Governance, Community Relations, Natural Capital, Climate Change, Human Capital and Non-ESG. Labels not covered in our samples are: Pollution & Waste, Product Liability and Business Ethics & Values. 
<br />
Based on the results in the previous section, we further explored around the data. We focus on the trend of both ESG labelled strategies and funds and also the top names’ participation in ESG. Below are some of our findings. Details and illustrative figures could be found in Appendixes and codebook.
<br />

### *2.1 trend of esg-labelled strategies.*
<br />
Total Number of ESG-labelled strategies peaked in 2017. The number of strategies labelled as ESG -related does not exceed 20 in most years, but in 2017 it reached a whopping 180. Most of the ESG-labeled strategies in 2017 are labeled as Corporate Governance accounted for 96.6% of the total strategies in 2017, with the remaining divided by Climate Change (1.7%), Community Relations (1.1%) and Human Capital (0.6%). Through the trend chart analysis, it can be concluded that the proportion of ESG-related strategies is decreasing year by year from 2015 to 2022. (Figure 1, Figure 2) By further checking each Corporate Governance strategy manually, we found that most these are actually not really trading with corporate governance factors but rather more general descriptions. Thus, we believe that it is an outlier caused by misclassification.
<br />
Percentage of ESG-labelled strategies in 2015 is the highest. We surprisingly found that the percentage of ESG-labelled strategies was highest in 2015 (Figure 3). But this is due to the denominator effect, i.e., there are too few observations in 2015. Therefore, it is fair to exclude the data of the year 2015. Then, we get an slightly upward-sloping regression line of the percentage of ESG-labelled strategies. (Figure 4). 
<br />
Environmental and Social Factors are trending these years. Grouped by the ESG labels, we find that Corporate Governance strategies dominates till 2019 (Figure 6). While the number of strategies labelled as Climate Change, Community Relations and Human Capital climb up year by year after a slight decline in 2017 and increase significantly from 2021 (Figure 5). We can see that fund management has been on the radar of investors and COVID-19 epidemic has increased investors' attention to the funds’ sustainability and corporate social responsibility.
<br />

### *2.2 trend of esg-labelled funds.*
<br />
In terms of ESG-labelled funds, we see trends similar to the ESG strategy mentioned above. More and more funds are integrating ESG into their investments in the recent years. (Figure 7, Figure 8, Figure 9) According to the Sustainable and Socially Responsible Investment Forum (US SIF, 2023), the total ESG investment in the U.S. market in 2016 has reached 8.7 trillion US dollars, an increase of 33% over 2014, and ESG ETFs still have a large space for growth. The overall development of ESG was in good shape.
<br />

### *2.3 leaders in esg investments.*
<br />
We then look at some the top names in ESG investing. We get the first movers’ names. Corporate Governance strategies are not inspected since they are much more general strategies. We can see that most of the ESG-related strategies start from 2016 (Table 3). 
<br />
BlackRock is leading in investing Climate Change both in terms of time and number of funds. But in a broader definition, we cannot see any funds is in a significantly leading position. We may need a more specific taxonomy with more dimensions to evaluate the funds’ performance.

<br />

## 3. Feature Extracting and Topic Modeling

Considering the scarcity of samples, we are not able to train the model by large amount of labeled data. So, in this section, we tried to utilize PCA and LDA models to extract features from the text and model topics.
<br />
After preliminary cleaning in section 1, the strings still need to be further lemmatized and tokenized. We only keep nouns and adjectives in our case. Also, we want to drop words that occur too frequently or too infrequently, because these word tokens are highly likely be extracted if not dropped but they are either meaningless or not significant for our classifier. So, we count the word frequency first. As indicated by the statistical data of word frequency, the distribution of count of words is extremely left-skewed and fat-tailed with most of the word appears for less than 100 times in the string (Table 4, Figure 9). Therefore, we dropped words with counts above 500 or below 5, 1536 words in total.
<br />
From the above word cloud, we can see catchy words and phrases such as: interest rate, credit default, depository receipt, swap, benchmark, environmental government agency, real estate, retirement, postretirement, yield, revenue, balance sheet, quantitative, etc. The most frequent 50 words are not all ESG-related but more of traditional fund management. (Figure 11)
<br />
The word counts derived in the previous setp are further vectorized and converted into term frequency–inverse document frequency (tf-idf) for PCA. And we found that it is a sparse dataset.
<br />
As the we don’t preset the raw texts and the dimensionality of raw dataset is too high, we first tried to perform PCA. Our training record shows that the accuracy score drops to below 0.95 when number of components is 299 (Figure 12). Thus, we choose to keep 399 components and see the shape of clusters. (Figure 13). 
<br />
Then, we clustered the reduced word vectors by K-means. Two criterions is recorded to evaluate the model, Calinski and Harabaz score  and SSE. Calinski and Harabaz score is also known as the Variance Ratio Criterion. The score is defined as ratio of the sum of between-cluster dispersion and of within-cluster dispersion. So, we would pick the model with the highest possible score. Our score graph is concave. The score is high when the number of clusters is small and drops dramatically before the number of clusters rises to 20. (Figure 13) On the other hand, SSE keeps decreasing when number of clusters rises from 1 to 20, with a short plateau period at 8-9 (Figure 14). Therefore, we set the number of K-means clusters to 8 and labeled the strategies accordingly. The K-means labels are integers from 0-8. Cluster 3 is the largest, with 461 observations, accounted for more than half of the last_entry samples. Cluster 5 is the second largest, with 173 observations and Cluster 4 follows with 89 observations. 
<br />
Compared to labels assigned by ESG-FinBERT the K-means labels are more diluted while they also get many overlaps. All the observations in Cluster 0, 2 and 6 fall into Corporate Governance category under ESG-FinBERT. Most of the observations in Cluster 3, 5 are also Corporate Governance labeled, which re-confirms our previous conclusion that the Corporate Governance label is not of great significance. Look the other way around, Corporate Governance strategies are primarily grouped into categories 3 and 5, as there are a bunch of strategies labeled as Community Relations within the same clusters, which may indicate that Corporate Governance and Community Relations are corelated topics.(Table 6, Figure 15)
<br />
Lastly, we performed LDA in attempt to categorizing the feature words. There are two evaluation metrics od LDA model: perplexity and coherence score. Coherence score measures score a single topic by measuring the degree of semantic similarity between high scoring words in the topic. In the analysis, the model with the highest coherence score is selected as the optimal model. (Kapadia, 2019). As shown by the training record, the optimal model is when there are only 2 topics (Figure 16). Details will not be covered in this report as the result  is not insightful enough, i.e., we cannot see any prominent theme of the two topics.
<br />

# Conclusions and Reflections
<br />
In summary, ESG investment covers many different topics and has become increasingly popular in recent years as investors seek to align their investments with their values. The pressure from government regulations and litigations will divert capital allocation from high-pollution and high-energy-consuming projects and enterprises. Nevertheless, ESG investment is still in the early stage of development, and there is a lack of unified standards for evaluation. 
<br />
NLP can be applied to the classification of ESG investment strategies yet it’s limited. Reasons may include: (1) Our sample size is too small, while NLP requires a large amount of data to obtain relatively accurate results; (2) At present, ESG field is still in the early development stage. The ambiguous definitions messed up classification; (3) According to our discussion with Brian Liu, an alternatives portfolio manager, many of those MFs don’t do screening themselves, but rather select stocks from the ESG index pool, which makes the niche market highly homogeneous.
<br />
Given higher requirements on accuracy and granularity, we should use more labeled data. And in order to improve the interpretability of model results, which is more necessary in real-world scenarios, we should do supervised learning.
<br />

# *References*
<br />
Amend, A. (2020, July 10). A Data-driven Approach to Environmental, Social and Governance. Retrieved from databricks: https://www.databricks.com/blog/2020/07/10/a-data-driven-approach-to-environmental-social-and-governance.html <br />
Amend, A. (n.d.). ESG - reports. Retrieved from databricks: https://www.databricks.com/notebooks/esg_notebooks/01_esg_report.html
edgetrader. (n.d.). esg-nlp. Retrieved from GitHub: https://github.com/edgetrader/esg-nlp <br />
Huang, A. H., Wang, H., & Yang, Y. (2022). FinBERT: A Large Language Model for Extracting Information from Financial Text. Contemporary Accounting Research. <br />
Kapadia, S. (2019, August 19). Evaluate Topic Models: Latent Dirichlet Allocation (LDA). Retrieved from Medium: https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0 <br />
Pasch, S., & Ehnes, D. (2022). NLP for Responsible Finance: Fine-Tuning Transformer-Based Models for ESG. IEEE International Conference on Big Data (Big Data), (pp. 3532-3536). <br />
US SIF. (2023). Sustainable Investing Basics. Retrieved from https://www.ussif.org/sribasics <br />
Vamvourellis, D., Toth, A. M., Desai, D., Mehta, D., & Pasquali, S. (2022). Learning Mutual Fund Categorization using Natural Language Processing. Third ACM International Conference on AI in Finance, (pp. 87-95). <br />
yiyanghkust/finbert-esg-9-categories. (n.d.). Retrieved from Hugging Face: https://huggingface.co/yiyanghkust/finbert-esg-9-categories <br />

