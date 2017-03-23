
<body>
<div align="justify">

<h1><font color="#ffbf00">1.	DATASET</font></h1>
<p>
1.	<b><font color="#ffbf00">dateCrawled</font></b> : <i>when this ad was first crawled, all field-values are taken from this date</i> <br>
2.	<b><font color="#ffbf00">name</font></b> : <i>"name" of the car </i><br>
3.	<b><font color="#ffbf00">seller</font></b> : <i>private or dealer </i><br>
4.	<b><font color="#ffbf00">offerType</font></b> : <i>the selling type of the car </i><br>
5.	<b><font color="#ffbf00">price</font></b> : <i>the price on the ad to sell the car </i><br>
6.	<b><font color="#ffbf00">abtest</font></b> : <i>unknown </i><br>
7.	<b><font color="#ffbf00">vehicleType</font></b> : <i>type of the car. Limousine, kleinwagen, kombi, bus etc. </i><br>
8.	<b><font color="#ffbf00">yearOfRegistration</font></b> : <i>at which year the car was first registered</i><br>
9.	<b><font color="#ffbf00">gearbox</font></b> : <i>manuel or otomatic</i><br>
10.	<b><font color="#ffbf00">powerPS</font></b> : <i>power of the car in PS</i><br>
11.	<b><font color="#ffbf00">model</font></b> : <i>model of the car</i><br>
12.	<b><font color="#ffbf00">kilometer</font></b> : <i>how many kilometers the car has driven</i><br>
13.	<b><font color="#ffbf00">monthOfRegistration</font></b> : <i>at which month the car was first registered</i><br>
14.	<b><font color="#ffbf00">fuelType</font></b> : <i>benzin, diesel, lpg etc</i><br>
15.	<b><font color="#ffbf00">brand</font></b> : <i>brand of the car. Mercedes, Porsche, audi etc…</i><br>
16.	<b><font color="#ffbf00">notRepairedDamage</font></b> : <i>if the car has a damage which is not repaired yet. Yes or no</i><br>
17.	<b><font color="#ffbf00">dateCreated</font></b> : <i>the date for which the ad at ebay was created</i><br>
18.	<b><font color="#ffbf00">nrOfPictures</font></b> : <i>number of pictures in the ad </i><br>
19.	<b><font color="#ffbf00">postalCode</font></b> : <i>code that shows the location of the car</i><br>
20.	<b><font color="#ffbf00">lastSeenOnline</font></b> : <i>when the crawler saw this ad last online</i><br>
</p>

<h1><font color="#ffbf00">2.	DATA EXPLORATION</font></h1>
<p>
Dataset consists of <b><font color="#ffbf00">371528 rows</font></b> and <b><font color="#ffbf00">20 columns</font></b> [<i>dateCrawled, name, seller, offerType, price, abtest, vehicleType, yearOfRegistration, gearbox, powerPS, model, kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage, dateCreated, nrOfPictures, postalCode, lastSeen</i>]. 
</p>

<img src="image/missing_value.png" alt="Table 1"><br> 

<p>
<i>Figure 1: Missing Value</i><br>
<h3>According to Figure 1:</h3>
<ul>
   <li>
   <b><font color="#ffbf00">5 columns</font></b> [<i>vehicleType, gearbox, model, fuelType, notRepairedDamage</i>] have missing values. Depending on the model, these columns can be removed completely. However, these columns could be important for the model. So, the records that have null values can be removed. By removing the null values column can be saved for the model. In the table, notRepairedDamage column has <b><font color="#ffbf00">72060 missing value</font></b> which is the <b><font color="#ffbf00">19%</font></b> of the whole dataset. In this case, removing each record is not the best option. It seems better to drop whole column.
   </li>

   <li>
   In the whole dataset, <b><font color="#ffbf00">110572</font></b> records has at least one missing value. Removing these records are not the best option because it causes  <b><font color="#ffbf00">33% data loss</font></b>. So, data loss can be decreased by dropping some non-important columns or a representing value can be assigned the missing values.
   </li>
</ul>

<h3>According to Table 1 and the Histogram Graph of the columns:</h3>
<ul>
   <li>dateCrawled (280500), name (233531), lastSeen (182806) columns have too many unique values. Depending on the learning model, these columns can be dropped.</li>
</ul>
<img src="image/table_1.png" alt="Table 1">




<ul>
   <li>Histogram of <b><font color="#ffbf00">nrOfPictures</font></b> column and Table 1 says that this column has only one values and it has no meaning for model and visualization. This column can be dropped.</li>
</ul>

<img src="image/nrOfPictures.png"> 

<ul>
   <li>Histogram graph of <b><font color="#ffbf00">seller</font></b> column and Table 1 says that this column has 2 unique values and “gewerblich” value has only 3 records. So, this column has no distinguishing information for the model. This column can be dropped, but first the records that has “gewerblich” value should be removed.</li>
</ul>

 <img src="image/seller.png"> 
 
<ul>
   <li>Based on histogram graph of <b><font color="#ffbf00">offerType</font></b>, Table 1 and column description, this column has 2 unique values. “gesuch” value has only 12 records. So, this column has no distinguishing information for the model. This column can be dropped, after removing the records that has “gesuch” value. </li>
</ul>

<img src="image/offerType.png"> 

<ul>
   <li>Based on histogram graph of <b><font color="#ffbf00">abtest</font></b> and Table 1, this column has consistent values for the model. </li>
</ul>

<img src="image/abtest.png"> 

<ul>
   <li>Based on histogram graph of <b><font color="#ffbf00">monthOfRegistration</font></b> and Table 1, this column should have 12 unique values. However, it has 13 values. Also, dataset has yearOfRegistration column. So, this column can be dropped.</li>
</ul>
 
 <img src="image/monthOfRegistration.png"> 
 
<ul>
   <li><b><font color="#ffbf00">postalCode</font></b> column has <b><font color="#ffbf00">8150</font></b> unique values. This information can be used to determine the location of the car. However, for the model, location is not a distinguishing information because all car has postal code in Germany. Car location does not affect the model. This column can be dropped.</li>
</ul>
 
<img src="image/postalCode.png"> 

<ul>
   <li><b><font color="#ffbf00">dateCreated</font></b> column has <b><font color="#ffbf00">114</font></b> unique values. This column has no distinguishing information for the model. So, this column can be dropped</li>
</ul>
 
 <img src="image/dateCreated.png"> 
 
<ul>
   <li>Based on histogram of <b><font color="#ffbf00">price</font></b> column and its description, this column has <b><font color="#ffbf00">10772</font></b> records that has <b><font color="#ffbf00">0</font></b> value which means the car is free. Also, records have some value more than <b><font color="#ffbf00">100000 euro</font></b>. It is not a consistent variable because cars can’t be that much expensive. To make dataset more consistent, prices values which are <b><font color="#ffbf00">0</font></b> and larger than <b><font color="#ffbf00">100000</font></b> can be removed. The histogram graph of price column are below. <b><font color="#ffbf00">First</font></b> graph shows the <b><font color="#ffbf00">original distribution</font></b> of the prices. <b><font color="#ffbf00">Second</font></b> graph shows the prices without <b><font color="#ffbf00">free cars</font></b>. <b><font color="#ffbf00">Third</font></b> graph shows the prices <b><font color="#ffbf00">between 0 and 100000 euro</font></b>. Other records can be removed from the dataset to have consistent values.  </li>
</ul>
 
 <img src="image/price_100.png"> 

<ul>
   <li>Based on histogram of <b><font color="#ffbf00">yearsOfRegistration</font></b> column and its description result, this column has inconsistent values. For example, it has year values larger than <b><font color="#ffbf00">2017</font></b>. Also, there are some values smaller than <b><font color="#ffbf00">1900</font></b> which does not make sense because in that time engine did not invented. So, yersOfRegistration records can be limited between <b><font color="#ffbf00">1900- yearsOfRegistration-2017</font></b>.</li>
</ul>
 
 <img src="image/yearsOfRegistration.png"> 
 
<ul>
   <li>Based on histogram of <b><font color="#ffbf00">powerPS</font></b> and Table 1, this column has some inconsistent values. powerPS can’t be less than <b><font color="#ffbf00">0</font></b>. Also, powerPS can’t be stronger than <b><font color="#ffbf00">1000</font></b>. So, it can be limited between 0-powerPS-1000. Other records can be removed from the dataset to have consistent values.</li>
</ul>

<ul>
   <li>Based on histogram of <b><font color="#ffbf00">fuelType</font></b> and Table 1, this column has 7 different value type. Apart from <b><font color="#ffbf00">“benzin”</font></b> and <b><font color="#ffbf00">“diesel”</font></b>, other values have very low records. So, these values do not mean much for the model. These records can be removed from the dataset.</li>
</ul>
 
 <img src="image/fuelType.png"> 
 
<ul>
   <li>Based on <b><font color="#ffbf00">vehicleType</font></b> histogram and Table 1, it has 8 different values. Values are consistent and can be used for the model.</li>
</ul>
 
 <img src="image/vehicleType.png"> 
 
<ul>
   <li>Based on histogram of <b><font color="#ffbf00">model</font></b> and Table 1, this column has many different values. It can be useful for price prediction but to make the model simpler this column can be dropped. </li>
</ul>
 
<img src="image/model.png"> 

<ul>
   <li>Based on histogram of <b><font color="#ffbf00">kilometer</font></b> and table 1, this column has consistent values. Also, it can be useful for the model.</li>
</ul>
 
 <img src="image/kilometer.png"> 
 
<ul>
   <li>Based on histogram of <b><font color="#ffbf00">gearbox</font></b> and Table 1, this column has 2 different values and values are consistent.</li>
</ul>
               
<img src="image/gearbox.png"> 
               
<ul>
   <li>Based on histogram of <b><font color="#ffbf00">notRepairedDamage</font></b>, this column has 2 different values. Values are consistent and can be useful for the model.</li>
</ul>
 
 <img src="image/notRepairedDamage.png"> 
 
<ul>
   <li>Based on histogram of the <b><font color="#ffbf00">brand</font></b>, this column has 40 different values. It has consistent records and can be useful for the model.</li>
</ul>
 
 <img src="image/brand.png"> 
 
<ul>
   <li>Based on <b><font color="#ffbf00">year v.s. price graph</font></b>, it can be said that new cars are more expensive than old ones. However, there some old cars which are also expensive. </li>
</ul>
 
 <img src="image/year.png"> 
 
<ul>
   <li>Based on <b><font color="#ffbf00">powerPS v.s price graph</font></b>, low powerPS cars are cheaper than others. </li>
</ul>

<img src="image/power.png"> 

<h1><font color="#ffbf00">3.	PROBLEM SETTING</font></h1>
<p>The problem is predicting the actual price of the car by looking given parameters.<br>
There are <b><font color="#ffbf00">371528</font></b> records in dataset. <b><font color="#ffbf00">243422</font></b> of them are remaining after data cleaning process.<br>
2 models are implemented. <br>
One of them uses the <b><font color="#ffbf00">30%</font></b> of the dataset as a test set.<br>
Other one uses <b><font color="#ffbf00">33%</font></b> for testing issue
</p>

<h1><font color="#ffbf00">4.	MODELLING</font></h1>

<p>
Before the implementation of the model. Dataset is cleaned using python libraries, and total number of column is decreased to 10 [<i>'vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model','kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'price'</i>]. 
</p>

<p>
After that, cleaned dataset is preprocessed using WEKA. WEKA attribute evaluator selected some attributes. It suggests the following attributes for the model [<i>'yearOfRegistration', 'gearbox', 'powerPS' ,'kilometer', 'fuelType', 'notRepairedDamage</i>].
</p>

<h3><font color="#ffbf00">There are 2 different implementation of linear regression model:</font></h3>
<ul>
   <li>First model is implemented using <font color="#ffbf00">python sklearn library</font>.</li>
       It has <font color="#ffbf00">10</font> attributes.<br>
       <font color="#ffbf00">30 percentage</font> of the dataset is used for testing.<br>
<br>
   <li>Second model is implemented using <font color="#ffbf00">WEKA</font>.</li>
       <font color="#ffbf00">Attributeselection</font> filter of WEKA applied on the dataset.<br>
       Filter removed the <font color="#ffbf00">3</font> attributes. Remaining <font color="#ffbf00">7</font> attributes are used for learning.<br>
       <font color="#ffbf00">33 percentage</font> of the dataset is used for testing.<br>
</ul>


<h1><font color="#ffbf00">5.	CONCLUSION and IMPROVEMENT POINTS</font></h1>
<font color="#ffbf00"><h3>Following results are taken from WEKA model:</h3></font>
<font color="#ffbf00">Root mean squared error:4958.1553</font><br>
Mean absolute error:                   <font color="#ffbf00">3103.1781</font><br>
Correlation coefficient:                  <font color="#ffbf00">0.7864</font><br>
Relative absolute error:                 <font color="#ffbf00">56.7852 %</font><br>
Root relative squared error:             <font color="#ffbf00">61.7716 %</font><br>
Total Number of Instances:            <font color="#ffbf00">82763</font>   <br><br>


<font color="#ffbf00"><h3>Following results are taken from python sklearn model:</h3></font>
<font color="#ffbf00">Root mean squared error: 555.6768635632562</font><br>
mean_absulute_error: <font color="#ffbf00">397.8973442835626</font><br>
mean_squared_error: <font color="#ffbf00">308776.7766994987</font><br>

<font color="#ffbf00"><h1>WEKA MODEL RESULT</h1></font>
<p>Root mean squared error:               4958.1553<br></p>

<table border="2">
<tr>
<td>inst#</td><td>actual</td><td>predicted</td><td>error</td></tr>
<tr><td>1</td><td align="right">9499</td><td align="right">5840.168</td><td align="right">-3658.832</td></tr>
<tr><td>2</td><td align="right">7990</td><td align="right">12515.27</td><td align="right">4525.27</td></tr>
<tr><td>3</td><td align="right">4000</td><td align="right">5139.611</td><td align="right">1139.611</td></tr>
<tr><td>4</td><td align="right">10700</td><td align="right">14125.198</td><td align="right">3425.198</td></tr>
<tr><td>5</td><td align="right">690</td><td align="right">-3346.537</td><td align="right">-4036.537</td></tr>
<tr><td>6</td><td align="right">1450</td><td align="right">3834.998</td><td align="right">2384.998</td></tr>
<tr><td>7</td><td align="right">1000</td><td align="right">720.987</td><td align="right">-279.013</td></tr>
<tr><td>8</td><td align="right">7800</td><td align="right">5329.186</td><td align="right">-2470.814</td></tr>
<tr><td>9</td><td align="right">8150</td><td align="right">8553.781</td><td align="right">403.781</td></tr>
<tr><td>10</td><td align="right">1111</td><td align="right">720.987</td><td align="right">-390.013</td></tr>
<tr><td>11</td><td align="right">9899</td><td align="right">16116.077</td><td align="right">6217.077</td></tr>
<tr><td>12</td><td align="right">150</td><td align="right">-4427.849</td><td align="right">-4577.849</td></tr>
<tr><td>13</td><td align="right">2000</td><td align="right">5802.808</td><td align="right">3802.808</td></tr>
<tr><td>14</td><td align="right">15000</td><td align="right">11530.067</td><td align="right">-3469.933</td></tr>
<tr><td>15</td><td align="right">8000</td><td align="right">10208.546</td><td align="right">2208.546</td></tr>
<tr><td>16</td><td align="right">4190</td><td align="right">4656.816</td><td align="right">466.816</td></tr>
<tr><td>17</td><td align="right">16000</td><td align="right">20750.782</td><td align="right">4750.782</td></tr>
<tr><td>18</td><td align="right">6000</td><td align="right">7567.218</td><td align="right">1567.218</td></tr>
<tr><td>19</td><td align="right">2800</td><td align="right">4278.547</td><td align="right">1478.547</td></tr>
<tr><td>20</td><td align="right">399</td><td align="right">1198.466</td><td align="right">799.466</td></tr>
<tr><td>21</td><td align="right">600</td><td align="right">-683.092</td><td align="right">-1283.092</td></tr>
<tr><td>22</td><td align="right">11200</td><td align="right">13948.794</td><td align="right">2748.794</td></tr>
<tr><td>23</td><td align="right">2490</td><td align="right">4802.349</td><td align="right">2312.349</td></tr>
<tr><td>24</td><td align="right">1699</td><td align="right">1226.653</td><td align="right">-472.347</td></tr>
<tr><td>25</td><td align="right">2400</td><td align="right">1651.665</td><td align="right">-748.335</td></tr>
<tr><td>26</td><td align="right">3350</td><td align="right">1533.574</td><td align="right">-1816.426</td></tr>
<tr><td>27</td><td align="right">6900</td><td align="right">2789.065</td><td align="right">-4110.935</td></tr>
<tr><td>28</td><td align="right">1800</td><td align="right">-521.508</td><td align="right">-2321.508</td></tr>
<tr><td>29</td><td align="right">999</td><td align="right">-1024.797</td><td align="right">-2023.797</td></tr>
<tr><td>30</td><td align="right">2200</td><td align="right">2679.834</td><td align="right">479.834</td></tr>
<tr><td>31</td><td align="right">2000</td><td align="right">9352.781</td><td align="right">7352.781</td></tr>
<tr><td>32</td><td align="right">4000</td><td align="right">4870.663</td><td align="right">870.663</td></tr>
<tr><td>33</td><td align="right">450</td><td align="right">-1548.599</td><td align="right">-1998.599</td></tr>
<tr><td>34</td><td align="right">39900</td><td align="right">27378.464</td><td align="right">-12521.536</td></tr>
<tr><td>35</td><td align="right">11400</td><td align="right">7158.677</td><td align="right">-4241.323</td></tr>
<tr><td>36</td><td align="right">490</td><td align="right">2607.076</td><td align="right">2117.076</td></tr>
<tr><td>37</td><td align="right">2500</td><td align="right">4521.265</td><td align="right">2021.265</td></tr>
<tr><td>38</td><td align="right">800</td><td align="right">1934.706</td><td align="right">1134.706</td></tr>
<tr><td>39</td><td align="right">10500</td><td align="right">5678.584</td><td align="right">-4821.416</td></tr>
<tr><td>40</td><td align="right">2000</td><td align="right">4735.112</td><td align="right">2735.112</td></tr>
<tr><td>41</td><td align="right">7300</td><td align="right">6645.934</td><td align="right">-654.066</td></tr>
<tr><td>42</td><td align="right">25500</td><td align="right">16712.904</td><td align="right">-8787.096</td></tr>
<tr><td>43</td><td align="right">5800</td><td align="right">10302.763</td><td align="right">4502.763</td></tr>
<tr><td>44</td><td align="right">4378</td><td align="right">5065.356</td><td align="right">687.356</td></tr>
<tr><td>45</td><td align="right">23500</td><td align="right">12138.451</td><td align="right">-11361.549</td></tr>
<tr><td>46</td><td align="right">4500</td><td align="right">1317.769</td><td align="right">-3182.231</td></tr>
<tr><td>47</td><td align="right">13900</td><td align="right">15045.157</td><td align="right">1145.157</td></tr>
<tr><td>48</td><td align="right">19900</td><td align="right">23986.561</td><td align="right">4086.561</td></tr>
<tr><td>49</td><td align="right">1290</td><td align="right">4165.662</td><td align="right">2875.662</td></tr>
<tr><td>50</td><td align="right">1400</td><td align="right">5150.051</td><td align="right">3750.051</td></tr>
<tr><td>51</td><td align="right">6299</td><td align="right">7385.541</td><td align="right">1086.541</td></tr>
<tr><td>52</td><td align="right">5800</td><td align="right">9640.887</td><td align="right">3840.887</td></tr>
<tr><td>53</td><td align="right">2350</td><td align="right">8285.654</td><td align="right">5935.654</td></tr>
<tr><td>54</td><td align="right">6400</td><td align="right">11960.662</td><td align="right">5560.662</td></tr>
<tr><td>55</td><td align="right">7115</td><td align="right">9798.174</td><td align="right">2683.174</td></tr>
<tr><td>56</td><td align="right">650</td><td align="right">-844.676</td><td align="right">-1494.676</td></tr>
<tr><td>57</td><td align="right">2450</td><td align="right">3249.958</td><td align="right">799.958</td></tr>
<tr><td>58</td><td align="right">5599</td><td align="right">6924.336</td><td align="right">1325.336</td></tr>
<tr><td>59</td><td align="right">7950</td><td align="right">5193.831</td><td align="right">-2756.169</td></tr>
<tr><td>60</td><td align="right">950</td><td align="right">1589.949</td><td align="right">639.949</td></tr>
<tr><td>61</td><td align="right">200</td><td align="right">10427.248</td><td align="right">10227.248</td></tr>
<tr><td>62</td><td align="right">3300</td><td align="right">4278.547</td><td align="right">978.547</td></tr>
<tr><td>63</td><td align="right">4990</td><td align="right">286.413</td><td align="right">-4703.587</td></tr>
<tr><td>64</td><td align="right">550</td><td align="right">-1207.296</td><td align="right">-1757.296</td></tr>
<tr><td>65</td><td align="right">3300</td><td align="right">6552.467</td><td align="right">3252.467</td></tr>
<tr><td>66</td><td align="right">2500</td><td align="right">1549.822</td><td align="right">-950.178</td></tr>
<tr><td>67</td><td align="right">900</td><td align="right">875.494</td><td align="right">-24.506</td></tr>
<tr><td>68</td><td align="right">8700</td><td align="right">14375.406</td><td align="right">5675.406</td></tr>
<tr><td>69</td><td align="right">10800</td><td align="right">10104.972</td><td align="right">-695.028</td></tr>
<tr><td>70</td><td align="right">11500</td><td align="right">11804.133</td><td align="right">304.133</td></tr>
<tr><td>71</td><td align="right">625</td><td align="right">-1368.478</td><td align="right">-1993.478</td></tr>
<tr><td>72</td><td align="right">200</td><td align="right">1328.497</td><td align="right">1128.497</td></tr>
<tr><td>73</td><td align="right">3600</td><td align="right">7095.08</td><td align="right">3495.08</td></tr>
<tr><td>74</td><td align="right">780</td><td align="right">2648.867</td><td align="right">1868.867</td></tr>
<tr><td>75</td><td align="right">10900</td><td align="right">7708.709</td><td align="right">-3191.291</td></tr>
<tr><td>76</td><td align="right">690</td><td align="right">2650.699</td><td align="right">1960.699</td></tr>
<tr><td>77</td><td align="right">10700</td><td align="right">12285.941</td><td align="right">1585.941</td></tr>
<tr><td>78</td><td align="right">1999</td><td align="right">6793.425</td><td align="right">4794.425</td></tr>
<tr><td>79</td><td align="right">2000</td><td align="right">124.829</td><td align="right">-1875.171</td></tr>
<tr><td>80</td><td align="right">22700</td><td align="right">20377.384</td><td align="right">-2322.616</td></tr>
<tr><td>81</td><td align="right">17200</td><td align="right">19003.737</td><td align="right">1803.737</td></tr>
<tr><td>82</td><td align="right">1450</td><td align="right">882.571</td><td align="right">-567.429</td></tr>
<tr><td>83</td><td align="right">4950</td><td align="right">4346.861</td><td align="right">-603.139</td></tr>
<tr><td>84</td><td align="right">3750</td><td align="right">9377.407</td><td align="right">5627.407</td></tr>
<tr><td>85</td><td align="right">4300</td><td align="right">8057.91</td><td align="right">3757.91</td></tr>
<tr><td>86</td><td align="right">1850</td><td align="right">6648.682</td><td align="right">4798.682</td></tr>
<tr><td>87</td><td align="right">2550</td><td align="right">609.582</td><td align="right">-1940.418</td></tr>
<tr><td>88</td><td align="right">4200</td><td align="right">7425.601</td><td align="right">3225.601</td></tr>
<tr><td>89</td><td align="right">2200</td><td align="right">7506.801</td><td align="right">5306.801</td></tr>
<tr><td>90</td><td align="right">1690</td><td align="right">-36.755</td><td align="right">-1726.755</td></tr>
<tr><td>91</td><td align="right">2300</td><td align="right">1125.486</td><td align="right">-1174.514</td></tr>
<tr><td>92</td><td align="right">11000</td><td align="right">8057.91</td><td align="right">-2942.09</td></tr>
<tr><td>93</td><td align="right">11800</td><td align="right">11588.962</td><td align="right">-211.038</td></tr>
<tr><td>94</td><td align="right">3200</td><td align="right">3376.279</td><td align="right">176.279</td></tr>
<tr><td>95</td><td align="right">23800</td><td align="right">19147.564</td><td align="right">-4652.436</td></tr>
<tr><td>96</td><td align="right">3100</td><td align="right">5490.77</td><td align="right">2390.77</td></tr>
<tr><td>97</td><td align="right">3800</td><td align="right">1283.028</td><td align="right">-2516.972</td></tr>
<tr><td>98</td><td align="right">1000</td><td align="right">1729.541</td><td align="right">729.541</td></tr>
<tr><td>99</td><td align="right">1799</td><td align="right">4535.358</td><td align="right">2736.358</td></tr>
<tr><td>100</td><td align="right">7890</td><td align="right">13844.964</td><td align="right">5954.964</td></tr>
<tr><td>101</td><td align="right">4499</td><td align="right">5469.855</td><td align="right">970.855</td></tr>
<tr><td>102</td><td align="right">4999</td><td align="right">8628.578</td><td align="right">3629.578</td></tr>
<tr><td>103</td><td align="right">7390</td><td align="right">11073.305</td><td align="right">3683.305</td></tr>
<tr><td>104</td><td align="right">799</td><td align="right">-22.949</td><td align="right">-821.949</td></tr>
<tr><td>105</td><td align="right">9600</td><td align="right">10019.097</td><td align="right">419.097</td></tr>
<tr><td>106</td><td align="right">23950</td><td align="right">17710.274</td><td align="right">-6239.726</td></tr>
<tr><td>107</td><td align="right">15800</td><td align="right">10282.926</td><td align="right">-5517.074</td></tr>
<tr><td>108</td><td align="right">17990</td><td align="right">14205.547</td><td align="right">-3784.453</td></tr>
<tr><td>109</td><td align="right">3550</td><td align="right">7681.402</td><td align="right">4131.402</td></tr>
<tr><td>110</td><td align="right">12900</td><td align="right">10993.248</td><td align="right">-1906.752</td></tr>
<tr><td>111</td><td align="right">1500</td><td align="right">5448.685</td><td align="right">3948.685</td></tr>
<tr><td>112</td><td align="right">4250</td><td align="right">7223.957</td><td align="right">2973.957</td></tr>
<tr><td>113</td><td align="right">2300</td><td align="right">461.014</td><td align="right">-1838.986</td></tr>
<tr><td>114</td><td align="right">3300</td><td align="right">1251.806</td><td align="right">-2048.194</td></tr>
<tr><td>115</td><td align="right">1650</td><td align="right">1226.653</td><td align="right">-423.347</td></tr>
<tr><td>116</td><td align="right">4400</td><td align="right">4788.511</td><td align="right">388.511</td></tr>
<tr><td>117</td><td align="right">5450</td><td align="right">8466.007</td><td align="right">3016.007</td></tr>
<tr><td>118</td><td align="right">2500</td><td align="right">4124.039</td><td align="right">1624.039</td></tr>
<tr><td>119</td><td align="right">4500</td><td align="right">3861.031</td><td align="right">-638.969</td></tr>
<tr><td>120</td><td align="right">2900</td><td align="right">7958.885</td><td align="right">5058.885</td></tr>
<tr><td>121</td><td align="right">1550</td><td align="right">4334.568</td><td align="right">2784.568</td></tr>
<tr><td>122</td><td align="right">5000</td><td align="right">10763.35</td><td align="right">5763.35</td></tr>
<tr><td>123</td><td align="right">7800</td><td align="right">7931.02</td><td align="right">131.02</td></tr>
<tr><td>124</td><td align="right">3600</td><td align="right">11085.441</td><td align="right">7485.441</td></tr>
<tr><td>125</td><td align="right">3000</td><td align="right">2087.718</td><td align="right">-912.282</td></tr>
<tr><td>126</td><td align="right">3450</td><td align="right">6339.607</td><td align="right">2889.607</td></tr>
<tr><td>127</td><td align="right">3999</td><td align="right">8967.44</td><td align="right">4968.44</td></tr>
<tr><td>128</td><td align="right">7900</td><td align="right">13566.664</td><td align="right">5666.664</td></tr>
<tr><td>129</td><td align="right">19000</td><td align="right">16269.355</td><td align="right">-2730.645</td></tr>
<tr><td>130</td><td align="right">5800</td><td align="right">8088.846</td><td align="right">2288.846</td></tr>
<tr><td>131</td><td align="right">1990</td><td align="right">4359.681</td><td align="right">2369.681</td></tr>
<tr><td>132</td><td align="right">3490</td><td align="right">8917.897</td><td align="right">5427.897</td></tr>
<tr><td>133</td><td align="right">2800</td><td align="right">-479.226</td><td align="right">-3279.226</td></tr>
<tr><td>134</td><td align="right">7150</td><td align="right">11234.889</td><td align="right">4084.889</td></tr>
<tr><td>135</td><td align="right">16950</td><td align="right">9873.309</td><td align="right">-7076.691</td></tr>
<tr><td>136</td><td align="right">790</td><td align="right">-359.923</td><td align="right">-1149.923</td></tr>
<tr><td>137</td><td align="right">450</td><td align="right">1159.416</td><td align="right">709.416</td></tr>
<tr><td>138</td><td align="right">2650</td><td align="right">932.75</td><td align="right">-1717.25</td></tr>
<tr><td>139</td><td align="right">10999</td><td align="right">10323.053</td><td align="right">-675.947</td></tr>
<tr><td>140</td><td align="right">8780</td><td align="right">13555.546</td><td align="right">4775.546</td></tr>
<tr><td>141</td><td align="right">6500</td><td align="right">7845.05</td><td align="right">1345.05</td></tr>
<tr><td>142</td><td align="right">9500</td><td align="right">145.476</td><td align="right">-9354.524</td></tr>
<tr><td>143</td><td align="right">20900</td><td align="right">20002.939</td><td align="right">-897.061</td></tr>
<tr><td>144</td><td align="right">2500</td><td align="right">2712.063</td><td align="right">212.063</td></tr>
<tr><td>145</td><td align="right">2990</td><td align="right">6941.992</td><td align="right">3951.992</td></tr>
<tr><td>146</td><td align="right">4900</td><td align="right">7532.21</td><td align="right">2632.21</td></tr>
<tr><td>147</td><td align="right">11500</td><td align="right">8064.987</td><td align="right">-3435.013</td></tr>
<tr><td>148</td><td align="right">7850</td><td align="right">10196.477</td><td align="right">2346.477</td></tr>
<tr><td>149</td><td align="right">31000</td><td align="right">23201.371</td><td align="right">-7798.629</td></tr>
<tr><td>150</td><td align="right">3650</td><td align="right">4696.943</td><td align="right">1046.943</td></tr>
<tr><td>151</td><td align="right">790</td><td align="right">580.317</td><td align="right">-209.683</td></tr>
<tr><td>152</td><td align="right">10000</td><td align="right">13251.118</td><td align="right">3251.118</td></tr>
<tr><td>153</td><td align="right">4200</td><td align="right">7411.574</td><td align="right">3211.574</td></tr>
<tr><td>154</td><td align="right">1200</td><td align="right">2194.004</td><td align="right">994.004</td></tr>
<tr><td>155</td><td align="right">700</td><td align="right">-109.513</td><td align="right">-809.513</td></tr>
<tr><td>156</td><td align="right">1150</td><td align="right">1912.04</td><td align="right">762.04</td></tr>
<tr><td>157</td><td align="right">650</td><td align="right">-2861.785</td><td align="right">-3511.785</td></tr>
<tr><td>158</td><td align="right">16890</td><td align="right">15993.048</td><td align="right">-896.952</td></tr>
<tr><td>159</td><td align="right">5600</td><td align="right">8006.634</td><td align="right">2406.634</td></tr>
<tr><td>160</td><td align="right">22500</td><td align="right">19380.014</td><td align="right">-3119.986</td></tr>
<tr><td>161</td><td align="right">8499</td><td align="right">9377.407</td><td align="right">878.407</td></tr>
<tr><td>162</td><td align="right">2999</td><td align="right">4696.943</td><td align="right">1697.943</td></tr>
<tr><td>163</td><td align="right">3300</td><td align="right">5947.13</td><td align="right">2647.13</td></tr>
<tr><td>164</td><td align="right">1700</td><td align="right">1114.846</td><td align="right">-585.154</td></tr>
<tr><td>165</td><td align="right">5999</td><td align="right">7768.048</td><td align="right">1769.048</td></tr>
<tr><td>166</td><td align="right">900</td><td align="right">-2960.576</td><td align="right">-3860.576</td></tr>
<tr><td>167</td><td align="right">8000</td><td align="right">11176.022</td><td align="right">3176.022</td></tr>
<tr><td>168</td><td align="right">3200</td><td align="right">4844.433</td><td align="right">1644.433</td></tr>
<tr><td>169</td><td align="right">4050</td><td align="right">6295.656</td><td align="right">2245.656</td></tr>
<tr><td>170</td><td align="right">990</td><td align="right">1065.069</td><td align="right">75.069</td></tr>
<tr><td>171</td><td align="right">3200</td><td align="right">8368.852</td><td align="right">5168.852</td></tr>
<tr><td>172</td><td align="right">7900</td><td align="right">9959.758</td><td align="right">2059.758</td></tr>
<tr><td>173</td><td align="right">6000</td><td align="right">6680.54</td><td align="right">680.54</td></tr>
<tr><td>174</td><td align="right">1450</td><td align="right">-216.876</td><td align="right">-1666.876</td></tr>
<tr><td>175</td><td align="right">1500</td><td align="right">2396.792</td><td align="right">896.792</td></tr>
<tr><td>176</td><td align="right">3400</td><td align="right">4802.349</td><td align="right">1402.349</td></tr>
<tr><td>177</td><td align="right">1500</td><td align="right">306.926</td><td align="right">-1193.074</td></tr>
<tr><td>178</td><td align="right">7000</td><td align="right">7748.836</td><td align="right">748.836</td></tr>
<tr><td>179</td><td align="right">1150</td><td align="right">1065.069</td><td align="right">-84.931</td></tr>
<tr><td>180</td><td align="right">700</td><td align="right">6104.385</td><td align="right">5404.385</td></tr>
<tr><td>181</td><td align="right">1150</td><td align="right">4521.265</td><td align="right">3371.265</td></tr>
<tr><td>182</td><td align="right">1050</td><td align="right">-61.998</td><td align="right">-1111.998</td></tr>
<tr><td>183</td><td align="right">4300</td><td align="right">648.631</td><td align="right">-3651.369</td></tr>
<tr><td>184</td><td align="right">6300</td><td align="right">5455.762</td><td align="right">-844.238</td></tr>
<tr><td>185</td><td align="right">7950</td><td align="right">12943.903</td><td align="right">4993.903</td></tr>
<tr><td>186</td><td align="right">7990</td><td align="right">9838.3</td><td align="right">1848.3</td></tr>
<tr><td>187</td><td align="right">1199</td><td align="right">-1099.53</td><td align="right">-2298.53</td></tr>
<tr><td>188</td><td align="right">920</td><td align="right">784.972</td><td align="right">-135.028</td></tr>
<tr><td>189</td><td align="right">17299</td><td align="right">15905.588</td><td align="right">-1393.412</td></tr>
<tr><td>190</td><td align="right">11250</td><td align="right">14653.392</td><td align="right">3403.392</td></tr>
<tr><td>191</td><td align="right">4800</td><td align="right">5222.612</td><td align="right">422.612</td></tr>
<tr><td>192</td><td align="right">8250</td><td align="right">10599.962</td><td align="right">2349.962</td></tr>
<tr><td>193</td><td align="right">11200</td><td align="right">7320.262</td><td align="right">-3879.738</td></tr>
<tr><td>194</td><td align="right">2000</td><td align="right">5022.863</td><td align="right">3022.863</td></tr>
<tr><td>195</td><td align="right">6200</td><td align="right">8517.42</td><td align="right">2317.42</td></tr>
<tr><td>196</td><td align="right">860</td><td align="right">1939.15</td><td align="right">1079.15</td></tr>
<tr><td>197</td><td align="right">2350</td><td align="right">2316.539</td><td align="right">-33.461</td></tr>
<tr><td>198</td><td align="right">7150</td><td align="right">25622.999</td><td align="right">18472.999</td></tr>
<tr><td>199</td><td align="right">8600</td><td align="right">12927.949</td><td align="right">4327.949</td></tr>
<tr><td>200</td><td align="right">11900</td><td align="right">18886.887</td><td align="right">6986.887</td></tr>
</table>
</div>
</body>
