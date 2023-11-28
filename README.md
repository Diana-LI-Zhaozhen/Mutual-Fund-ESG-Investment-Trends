# Mutual-Fund-ESG-Investment-Trends
📕HKU Mfft 21'fall-Big Data. Contributors: Diana LI @Diana-LI-Zhaozhen, Peng Pengxin. We were trying to find ESG investment trends by applying basic EDA on the prospectus of mutual funds in the States. The project and the course was instructed by Dr. Alan Kwan.


# Background

A growing number of funds claim to be making sustainable investments, while investors are concerned about the risks associated with greenwashing due to the current lack of measurable standards in this area. Although there are several ESG scoring metrics proposed by rating agencies , these data are very scarce and expensive and the sources are often not transparent or objective enough, which sets a very high barrier for investors and greatly hinders relevant investments.

We believe that NLP could be useful in ESG investment strategy analysis, as such information is often presented in textual form in prospectuses, related news reports, and speeches. NLP can enhance ESG investing in a variety of ways. For example, NLP enables the large-scale tracking of controversies. Also, NLP can be combined with graph analytics to extract key strategic ESG initiatives and learn companies’ relationships in a global market and their impact on market risk calculations (Amend, A Data-driven Approach to Environmental, Social and Governance, 2020). (Vamvourellis, Toth, Desai, Mehta, & Pasquali, 2022)


# Methodology and Findings

In this project, we attempted to classify mutual funds by utilizing the FinBERT model. Then, we explored the trend of esg investment development based on the classification results. Additionally, we tried to perform feature extracting and topic modeling from the texts to construct a new ESG investment strategy taxonomy.

## 1. Labelling and Building Database

We pulled data from the table derived_sec_fund_characteristic in database common_goods to construct our own database. This table contains raw texts extracted from 13-F files. After filtering out the Null&NaN data, we can get 1600 files submitted by 1436 funds covering reporting periods from 2015 Q4 to 2022 Q2. After removing the duplicates, we get a sample of 6519 observations. This is a relatively small sample with many highly resemble objective and strategies description (Amend, A Data-driven Approach to Environmental, Social and Governance, 2020)ns, suggesting that we should use Zero-Shot-Learning or Few-Shot-Learning techniques in the classification. Also, we contacted the cleaned text string of objective and strategy to power the analysis. 

Next, the ESG-FinBERT model  pertained by researchers at HKUST is adopted to label the contacted objectives and strategies strings. The model could classify raw text into 9 categories: Climate Change, Pollution & Waste, Corporate Governance, Natural Capital, Product Liability, Human Capital, Business Ethics &Values, Community Relations and Non-ESG. According to researchers, their pretrained ESG-FinBERT model outperforms other NLP models when doing ESG classification, especially when training on smaller text samples containing financial words that are not commonly used in general texts. (Huang, Wang, & Yang, 2022) Another study (Pasch & Ehnes, 2022) also shows preference for BERT model when doing ESG classification tasks. However, this model is not perfect since is pre-trained, which means we should bear with the inflexibility. And though both researches mentioned that the models used were trained on ESG-related corpus, mainly news and listed companies’ ESG reports, our corpus does not necessarily feature overlapping features. To get better classification results, we should have fine-tuned the pretrained model.

The labelled data was stored in our database as table fund_objectives_strategy_with_labels in database common_goods.

<table class="MsoTable15Plain2" border="1" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse;border:none">
 <tbody><tr style="height:14.65pt">
  <td width="228" style="width:170.9pt;border-top:solid black 1.5pt;border-left:
  none;border-bottom:solid black 1.5pt;border-right:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">N<b>ame</b></span></p>
  </td>
  <td width="186" style="width:139.2pt;border-top:solid black 1.5pt;border-left:
  none;border-bottom:solid black 1.5pt;border-right:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Data Type</span></b></p>
  </td>
  <td width="208" style="width:155.75pt;border-top:solid black 1.5pt;border-left:
  none;border-bottom:solid black 1.5pt;border-right:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Description</span></b></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">adsh</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(String)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Filing id, SEC Accession No.</span></p>
  </td>
 </tr>
 <tr style="height:14.65pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">cik_expanded</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(String)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">The Central Index Key (CIK)</span></p>
  </td>
 </tr>
 <tr style="height:14.65pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">name</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(String)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Fund name</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">period_end_date</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(Int32)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Reporting period end date</span></p>
  </td>
 </tr>
 <tr style="height:14.65pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">year</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Int32</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Reporting period year</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">objective</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(String)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Objective narrative</span></p>
  </td>
 </tr>
 <tr style="height:14.65pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">strategy</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(String)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Strategy narrative</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="228" style="width:170.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">cleaned_objective_strategy</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(String)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Contacted string of cleaned </span></p>
  </td>
 </tr>
 <tr style="height:14.65pt">
  <td width="228" style="width:170.9pt;border:none;border-bottom:solid black 1.5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">esg_labels</span></b></p>
  </td>
  <td width="186" style="width:139.2pt;border:none;border-bottom:solid black 1.5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Nullable(String)</span></p>
  </td>
  <td width="208" style="width:155.75pt;border:none;border-bottom:solid black 1.5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.65pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">ESG labels assigned by ESG FinBERT
  model.</span></p>
  </td>
 </tr>
</tbody></table>


## 2. Exploratory Data Analysis

After filtering out abnormal and meaningless data and only keep the last entries, we still have 1583 observations. These observations cover the reporting period from consecutive 8 years from 2015 to 2022, and are labelled as 6 categories: Corporate Governance, Community Relations, Natural Capital, Climate Change, Human Capital and Non-ESG. Labels not covered in our samples are: Pollution & Waste, Product Liability and Business Ethics & Values. 

Based on the results in the previous section, we further explored around the data. We focus on the trend of both ESG labelled strategies and funds and also the top names’ participation in ESG. Below are some of our findings. Details and illustrative figures could be found in Appendixes and codebook.

### *2.1 trend of esg-labelled strategies.*

Total Number of ESG-labelled strategies peaked in 2017. The number of strategies labelled as ESG -related does not exceed 20 in most years, but in 2017 it reached a whopping 180. Most of the ESG-labeled strategies in 2017 are labeled as Corporate Governance accounted for 96.6% of the total strategies in 2017, with the remaining divided by Climate Change (1.7%), Community Relations (1.1%) and Human Capital (0.6%). Through the trend chart analysis, it can be concluded that the proportion of ESG-related strategies is decreasing year by year from 2015 to 2022. </br> <img src="img/numberofesglabelledstrategiesbyyear.png"> </br> <img src="img/esgstrategiesin2017.png"> </br> By further checking each Corporate Governance strategy manually, we found that most these are actually not really trading with corporate governance factors but rather more general descriptions. Thus, we believe that it is an outlier caused by misclassification.

Percentage of ESG-labelled strategies in 2015 is the highest. We surprisingly found that the percentage of ESG-labelled strategies was highest in 2015. </br> <img src="img/pctofstrategiesbyyear.png"> But this is due to the denominator effect, i.e., there are too few observations in 2015. Therefore, it is fair to exclude the data of the year 2015. Then, we get an slightly upward-sloping regression line of the percentage of ESG-labelled strategies. </br> <img src="img/pctofstrategiesbyyearexcl2015.png">

Environmental and Social Factors are trending these years. Grouped by the ESG labels, we find that Corporate Governance strategies dominates till 2019.  </br> <img src="img/pctofesglabelsbyyear.png"> While the number of strategies labelled as Climate Change, Community Relations and Human Capital climb up year by year after a slight decline in 2017 and increase significantly from 2021.  </br> <img src="img/numberofesglabelsbyyear.png"> We can see that fund management has been on the radar of investors and COVID-19 epidemic has increased investors' attention to the funds’ sustainability and corporate social responsibility.


### *2.2 trend of esg-labelled funds.*

In terms of ESG-labelled funds, we see trends similar to the ESG strategy mentioned above. More and more funds are integrating ESG into their investments in the recent years. </br> <img src="img/percentageofesgfundsperyear.png"> </br> <img src="img/percentageofesgfundsperyearexcl2015.png"> </br> <img src="img/fundtradingwithineachesglabel.png"> According to the Sustainable and Socially Responsible Investment Forum (US SIF, 2023), the total ESG investment in the U.S. market in 2016 has reached 8.7 trillion US dollars, an increase of 33% over 2014, and ESG ETFs still have a large space for growth. The overall development of ESG was in good shape.


### *2.3 leaders in esg investments.*

We then look at some the top names in ESG investing. We get the first movers’ names. Corporate Governance strategies are not inspected since they are much more general strategies. We can see that most of the ESG-related strategies start from 2016.

<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="99%" style="width:99.24%;border-collapse:collapse">
 <thead>
  <tr style="height:13.85pt">
   <td width="104" nowrap="" style="width:78.0pt;border-top:solid black 1.5pt;
   border-left:none;border-bottom:solid black 1.5pt;border-right:none;
   padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
   <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">Labels</span></b></p>
   </td>
   <td width="85" nowrap="" style="width:63.8pt;border-top:solid black 1.5pt;
   border-left:none;border-bottom:solid black 1.5pt;border-right:none;
   padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
   <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">CIK</span></b></p>
   </td>
   <td width="359" nowrap="" style="width:269.3pt;border-top:solid black 1.5pt;
   border-left:none;border-bottom:solid black 1.5pt;border-right:none;
   padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
   <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">Fund Name</span></b></p>
   </td>
   <td width="49" nowrap="" style="width:36.45pt;border-top:solid black 1.5pt;
   border-left:none;border-bottom:solid black 1.5pt;border-right:none;
   padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
   <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">Year</span></b></p>
   </td>
  </tr>
 </thead>
 <tbody><tr style="height:13.85pt">
  <td width="104" nowrap="" rowspan="14" style="width:78.0pt;border:none;border-bottom:
  solid black 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">Climate Change</span></p>
  </td>
  <td width="85" nowrap="" style="width:63.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1579982</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">ARK ETF TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1738074</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">BLACKROCK FUNDS IV</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">110055</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">BLACKROCK SUSTAINABLE
  BALANCED FUND, INC.</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1324285</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">BLACKROCK UNCONSTRAINED
  EQUITY FUND</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1121624</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">CALVERT IMPACT FUND INC</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1831313</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">ENGINE NO. 1 ETF TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1467831</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">ETF MANAGERS TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">917124</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">FIRSTHAND FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">877232</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">GREEN CENTURY FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1100663</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">ISHARES TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1095726</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">NATIXIS FUNDS TRUST IV</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1506001</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">NEUBERGER BERMAN ETF TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1209466</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">POWERSHARES EXCHANGE TRADED
  FUND TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1168164</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">SPDR INDEX SHARES FUNDS
  (FORMERLY STREETTRACKS INDEX SHARES FUNDS)</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="104" nowrap="" rowspan="12" style="width:78.0pt;border:none;border-bottom:
  solid black 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">Community Relations</span></p>
  </td>
  <td width="85" nowrap="" style="width:63.8pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1811168</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2ND VOTE FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">914775</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">ADVANTAGE FUNDS, INC.</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">766285</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">AMANA MUTUAL FUNDS TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1872555</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">CATHOLIC RESPONSIBLE
  INVESTMENTS FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1026977</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">CITY NATIONAL ROCHDALE FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">707823</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">FIDELITY MT VERNON STREET
  TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1645194</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">LEGG MASON ETF INVESTMENT
  TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1489215</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">MIRAE ASSET DISCOVERY FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">795259</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">MUTUAL OF AMERICA INVESTMENT
  CORP</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1481686</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">NILE CAPITAL INVESTMENT
  TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1141819</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">TRUST FOR PROFESSIONAL
  MANAGERS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1785243</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">UNCOMMON INVESTMENT FUNDS
  TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="104" nowrap="" rowspan="6" style="width:78.0pt;border:none;border-bottom:
  solid black 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">Human Capital</span></p>
  </td>
  <td width="85" nowrap="" style="width:63.8pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1377031</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">EPIPHANY FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2017</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1748425</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">GABELLI ETFS TRUST</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2017</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1821080</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">HUMANKIND BENEFIT CORP</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2017</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1722388</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">IMPACT SHARES TRUST I</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2017</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">923184</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">MATTHEWS INTERNATIONAL FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2017</span></p>
  </td>
 </tr>
 <tr style="height:13.85pt">
  <td width="85" nowrap="" style="width:63.8pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">747546</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">PARNASSUS FUNDS</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.85pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2017</span></p>
  </td>
 </tr>
 <tr style="height:14.4pt">
  <td width="104" nowrap="" style="width:78.0pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">Natural Capital</span></p>
  </td>
  <td width="85" nowrap="" style="width:63.8pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">1121624</span></p>
  </td>
  <td width="359" nowrap="" style="width:269.3pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.4pt">
  <p class="MsoNormal" align="left" style="text-align:left"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">CALVERT IMPACT FUND INC</span></p>
  </td>
  <td width="49" nowrap="" style="width:36.45pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif;color:black">2016</span></p>
  </td>
 </tr>
</tbody></table>

BlackRock is leading in investing Climate Change both in terms of time and number of funds. But in a broader definition, we cannot see any funds is in a significantly leading position. We may need a more specific taxonomy with more dimensions to evaluate the funds’ performance.

## 3. Feature Extracting and Topic Modeling

Considering the scarcity of samples, we are not able to train the model by large amount of labeled data. So, in this section, we tried to utilize PCA and LDA models to extract features from the text and model topics.

After preliminary cleaning in section 1, the strings still need to be further lemmatized and tokenized. We only keep nouns and adjectives in our case. Also, we want to drop words that occur too frequently or too infrequently, because these word tokens are highly likely be extracted if not dropped but they are either meaningless or not significant for our classifier. So, we count the word frequency first. As indicated by the statistical data of word frequency, the distribution of count of words is extremely left-skewed and fat-tailed with most of the word appears for less than 100 times in the string.

<table class="MsoTableGrid" border="0" cellspacing="0" cellpadding="0" width="42%" style="width:42.26%;border-collapse:collapse;border:none">
 <tbody><tr>
  <td width="95" style="width:70.9pt;border-top:solid black 1.5pt;border-left:
  none;border-bottom:solid black 1.5pt;border-right:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:115%"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Metric</span></b></p>
  </td>
  <td width="160" style="width:119.7pt;border-top:solid black 1.5pt;border-left:
  none;border-bottom:solid black 1.5pt;border-right:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:115%"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Value</span></b></p>
  </td>
 </tr>
 <tr>
  <td width="95" style="width:70.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" style="text-indent:8.9pt;line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">nobs</span></p>
  </td>
  <td width="160" style="width:119.7pt;border:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="right" style="margin-right:14.4pt;text-align:right;
  line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">3064</span></p>
  </td>
 </tr>
 <tr>
  <td width="95" style="width:70.9pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" style="text-indent:8.9pt;line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">min</span></p>
  </td>
  <td width="160" style="width:119.7pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="right" style="margin-right:14.4pt;text-align:right;
  line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">1</span></p>
  </td>
 </tr>
 <tr>
  <td width="95" style="width:70.9pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" style="text-indent:8.9pt;line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">max</span></p>
  </td>
  <td width="160" style="width:119.7pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="right" style="margin-right:14.4pt;text-align:right;
  line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">12771</span></p>
  </td>
 </tr>
 <tr>
  <td width="95" style="width:70.9pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" style="text-indent:8.9pt;line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">mean</span></p>
  </td>
  <td width="160" style="width:119.7pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="right" style="margin-right:14.4pt;text-align:right;
  line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">69.09</span></p>
  </td>
 </tr>
 <tr>
  <td width="95" style="width:70.9pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" style="text-indent:8.9pt;line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">variance</span></p>
  </td>
  <td width="160" style="width:119.7pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="right" style="margin-right:14.4pt;text-align:right;
  line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">158767.35</span></p>
  </td>
 </tr>
 <tr>
  <td width="95" style="width:70.9pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" style="text-indent:8.9pt;line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">skewness</span></p>
  </td>
  <td width="160" style="width:119.7pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="right" style="margin-right:14.4pt;text-align:right;
  line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">18.33</span></p>
  </td>
 </tr>
 <tr>
  <td width="95" style="width:70.9pt;border:none;border-bottom:solid black 1.5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" style="text-indent:8.9pt;line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">kurtosis</span></p>
  </td>
  <td width="160" style="width:119.7pt;border:none;border-bottom:solid black 1.5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="right" style="margin-right:14.4pt;text-align:right;
  line-height:115%"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">450.57</span></p>
  </td>
 </tr>
</tbody></table>
</br> <img src="img/fundtradingwithineachesglabel.png"> Therefore, we dropped words with counts above 500 or below 5, 1536 words in total.

</br> <img src="img/wordcloud.png">

From the above word cloud, we can see catchy words and phrases such as: interest rate, credit default, depository receipt, swap, benchmark, environmental government agency, real estate, retirement, postretirement, yield, revenue, balance sheet, quantitative, etc. The most frequent 50 words are not all ESG-related but more of traditional fund management. </br> <img src="img/wordfrequency_tfidf.png"> 

The word counts derived in the previous setp are further vectorized and converted into term frequency–inverse document frequency (tf-idf) for PCA. And we found that it is a sparse dataset.

As the we don’t preset the raw texts and the dimensionality of raw dataset is too high, we first tried to perform PCA. Our training record shows that the accuracy score drops to below 0.95 when number of components is 299. </br> <img src="img/pca_scores.png"> Thus, we choose to keep 399 components and see the shape of clusters. </br> <img src="img/kmeanschscore.png"> 

Then, we clustered the reduced word vectors by K-means. Two criterions is recorded to evaluate the model, Calinski and Harabaz score  and SSE. Calinski and Harabaz score is also known as the Variance Ratio Criterion. The score is defined as ratio of the sum of between-cluster dispersion and of within-cluster dispersion. So, we would pick the model with the highest possible score. Our score graph is concave. The score is high when the number of clusters is small and drops dramatically before the number of clusters rises to 20. </br> <img src="img/kmeanschscore.png">  On the other hand, SSE keeps decreasing when number of clusters rises from 1 to 20, with a short plateau period at 8-9. </br> <img src="img/sse.png"> Therefore, we set the number of K-means clusters to 8 and labeled the strategies accordingly. The K-means labels are integers from 0-8. Cluster 3 is the largest, with 461 observations, accounted for more than half of the last_entry samples. Cluster 5 is the second largest, with 173 observations and Cluster 4 follows with 89 observations. 

Compared to labels assigned by ESG-FinBERT the K-means labels are more diluted while they also get many overlaps. All the observations in Cluster 0, 2 and 6 fall into Corporate Governance category under ESG-FinBERT. Most of the observations in Cluster 3, 5 are also Corporate Governance labeled, which re-confirms our previous conclusion that the Corporate Governance label is not of great significance. Look the other way around, Corporate Governance strategies are primarily grouped into categories 3 and 5, as there are a bunch of strategies labeled as Community Relations within the same clusters, which may indicate that Corporate Governance and Community Relations are corelated topics.

<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="99%" style="width:99.02%;border-collapse:collapse">
 <thead>
  <tr>
   <td width="33%" style="width:33.34%;border-top:solid black 1.5pt;border-left:
   none;border-bottom:solid black 1.5pt;border-right:none;padding:3.0pt 6.0pt 3.0pt 6.0pt">
   <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">K-means Cluster</span></b></p>
   </td>
   <td style="border-top:solid black 1.5pt;border-left:none;border-bottom:solid black 1.5pt;
   border-right:none;padding:3.0pt 6.0pt 3.0pt 6.0pt">
   <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">ESG Label</span></b></p>
   </td>
   <td width="37%" style="width:37.2%;border-top:solid black 1.5pt;border-left:
   none;border-bottom:solid black 1.5pt;border-right:none;padding:.75pt .75pt .75pt .75pt">
   <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Observations</span></b></p>
   </td>
  </tr>
 </thead>
 <tbody><tr>
  <td width="33%" style="width:33.34%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">0</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;word-break:break-all"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">40</span></p>
  </td>
 </tr>
 <tr>
  <td width="33%" rowspan="2" style="width:33.34%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">1</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">33</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Climate Change</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">11</span></p>
  </td>
 </tr>
 <tr>
  <td width="33%" style="width:33.34%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">2</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">25</span></p>
  </td>
 </tr>
 <tr>
  <td width="33%" rowspan="4" style="width:33.34%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">3</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">438</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Community Relations</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">13</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Climate Change</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">6</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Human Capital</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">4</span></p>
  </td>
 </tr>
 <tr>
  <td width="33%" rowspan="5" style="width:33.34%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">4</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">81</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Community Relations</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">1</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Climate Change</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">4</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Natural Capital</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">1</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Human Capital</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">2</span></p>
  </td>
 </tr>
 <tr>
  <td width="33%" rowspan="2" style="width:33.34%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">5</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">172</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Human Capital</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">1</span></p>
  </td>
 </tr>
 <tr>
  <td width="33%" style="width:33.34%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">6</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">33</span></p>
  </td>
 </tr>
 <tr>
  <td width="33%" rowspan="3" style="width:33.34%;border:none;border-bottom:solid black 1.5pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">7</span></p>
  </td>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Corporate Governance</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">21</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.0pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Community Relations</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.0pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">1</span></p>
  </td>
 </tr>
 <tr>
  <td style="border:none;border-bottom:solid black 1.5pt;padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">Climate Change</span></p>
  </td>
  <td width="37%" style="width:37.2%;border:none;border-bottom:solid black 1.5pt;
  padding:3.0pt 6.0pt 3.0pt 6.0pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-family:&quot;Garamond&quot;,serif">1</span></p>
  </td>
 </tr>
</tbody></table>
</br> <img src="img/jointlabelcount.png">

Lastly, we performed LDA in attempt to categorizing the feature words. There are two evaluation metrics od LDA model: perplexity and coherence score. Coherence score measures score a single topic by measuring the degree of semantic similarity between high scoring words in the topic. In the analysis, the model with the highest coherence score is selected as the optimal model. (Kapadia, 2019). As shown by the training record, the optimal model is when there are only 2 topics (Figure 16). Details will not be covered in this report as the result  is not insightful enough, i.e., we cannot see any prominent theme of the two topics.

# Conclusions and Reflections

In summary, ESG investment covers many different topics and has become increasingly popular in recent years as investors seek to align their investments with their values. The pressure from government regulations and litigations will divert capital allocation from high-pollution and high-energy-consuming projects and enterprises. Nevertheless, ESG investment is still in the early stage of development, and there is a lack of unified standards for evaluation. 

NLP can be applied to the classification of ESG investment strategies yet it’s limited. Reasons may include: (1) Our sample size is too small, while NLP requires a large amount of data to obtain relatively accurate results; (2) At present, ESG field is still in the early development stage. The ambiguous definitions messed up classification; (3) According to our discussion with Brian Liu, an alternatives portfolio manager, many of those MFs don’t do screening themselves, but rather select stocks from the ESG index pool, which makes the niche market highly homogeneous.

Given higher requirements on accuracy and granularity, we should use more labeled data. And in order to improve the interpretability of model results, which is more necessary in real-world scenarios, we should do supervised learning.

# *References*

Amend, A. (2020, July 10). A Data-driven Approach to Environmental, Social and Governance. Retrieved from databricks: https://www.databricks.com/blog/2020/07/10/a-data-driven-approach-to-environmental-social-and-governance.html <br />
Amend, A. (n.d.). ESG - reports. Retrieved from databricks: https://www.databricks.com/notebooks/esg_notebooks/01_esg_report.html
edgetrader. (n.d.). esg-nlp. Retrieved from GitHub: https://github.com/edgetrader/esg-nlp <br />
Huang, A. H., Wang, H., & Yang, Y. (2022). FinBERT: A Large Language Model for Extracting Information from Financial Text. Contemporary Accounting Research. <br />
Kapadia, S. (2019, August 19). Evaluate Topic Models: Latent Dirichlet Allocation (LDA). Retrieved from Medium: https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0 <br />
Pasch, S., & Ehnes, D. (2022). NLP for Responsible Finance: Fine-Tuning Transformer-Based Models for ESG. IEEE International Conference on Big Data (Big Data), (pp. 3532-3536). <br />
US SIF. (2023). Sustainable Investing Basics. Retrieved from https://www.ussif.org/sribasics <br />
Vamvourellis, D., Toth, A. M., Desai, D., Mehta, D., & Pasquali, S. (2022). Learning Mutual Fund Categorization using Natural Language Processing. Third ACM International Conference on AI in Finance, (pp. 87-95). <br />
yiyanghkust/finbert-esg-9-categories. (n.d.). Retrieved from Hugging Face: https://huggingface.co/yiyanghkust/finbert-esg-9-categories <br />

