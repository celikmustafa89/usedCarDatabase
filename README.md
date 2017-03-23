
<body>
<div align="justify">

<h1>1.	DATASET</h1>
<p>
1.	<b>dateCrawled</b> : <i>when this ad was first crawled, all field-values are taken from this date</i> <br>
2.	<b>name</b> : <i>"name" of the car </i><br>
3.	<b>seller</b> : <i>private or dealer </i><br>
4.	<b>offerType</b> : <i>the selling type of the car </i><br>
5.	<b>price</b> : <i>the price on the ad to sell the car </i><br>
6.	<b>abtest</b> : <i>unknown </i><br>
7.	<b>vehicleType</b> : <i>type of the car. Limousine, kleinwagen, kombi, bus etc. </i><br>
8.	<b>yearOfRegistration</b> : <i>at which year the car was first registered</i><br>
9.	<b>gearbox</b> : <i>manuel or otomatic</i><br>
10.	<b>powerPS</b> : <i>power of the car in PS</i><br>
11.	<b>model</b> : <i>model of the car</i><br>
12.	<b>kilometer</b> : <i>how many kilometers the car has driven</i><br>
13.	<b>monthOfRegistration</b> : <i>at which month the car was first registered</i><br>
14.	<b>fuelType</b> : <i>benzin, diesel, lpg etc</i><br>
15.	<b>brand</b> : <i>brand of the car. Mercedes, Porsche, audi etc…</i><br>
16.	<b>notRepairedDamage</b> : <i>if the car has a damage which is not repaired yet. Yes or no</i><br>
17.	<b>dateCreated</b> : <i>the date for which the ad at ebay was created</i><br>
18.	<b>nrOfPictures</b> : <i>number of pictures in the ad </i><br>
19.	<b>postalCode</b> : <i>code that shows the location of the car</i><br>
20.	<b>lastSeenOnline</b> : <i>when the crawler saw this ad last online</i><br>
</p>

<h1>2.	DATA EXPLORATION</h1>
<p>
Dataset consists of <b>371528 rows</b> and <b>20 columns</b> [<i>dateCrawled, name, seller, offerType, price, abtest, vehicleType, yearOfRegistration, gearbox, powerPS, model, kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage, dateCreated, nrOfPictures, postalCode, lastSeen</i>]. 
</p>

<img src="image/missing_value.png" alt="Table 1"><br> 

<p>
<i>Figure 1: Missing Value</i><br>
<h3>According to Figure 1:</h3>
<ul>
   <li>
   <b>5 columns</b> [<i>vehicleType, gearbox, model, fuelType, notRepairedDamage</i>] have missing values. Depending on the model, these columns can be removed completely. However, these columns could be important for the model. So, the records that have null values can be removed. By removing the null values column can be saved for the model. In the table, notRepairedDamage column has <b>72060 missing value</b> which is the <b>19%</b> of the whole dataset. In this case, removing each record is not the best option. It seems better to drop whole column.
   </li>

   <li>
   In the whole dataset, <b>110572</b> records has at least one missing value. Removing these records are not the best option because it causes  <b>33% data loss</b>. So, data loss can be decreased by dropping some non-important columns or a representing value can be assigned the missing values.
   </li>
</ul>

<h3>According to Table 1 and the Histogram Graph of the columns:</h3>
<ul>
   <li>dateCrawled (280500), name (233531), lastSeen (182806) columns have too many unique values. Depending on the learning model, these columns can be dropped.</li>
</ul>
<img src="image/table_1.png" alt="Table 1">




<ul>
   <li>Histogram of <b>nrOfPictures</b> column and Table 1 says that this column has only one values and it has no meaning for model and visualization. This column can be dropped.</li>
</ul>

<img src="image/nrOfPictures.png"> 

<ul>
   <li>Histogram graph of <b>seller</b> column and Table 1 says that this column has 2 unique values and “gewerblich” value has only 3 records. So, this column has no distinguishing information for the model. This column can be dropped, but first the records that has “gewerblich” value should be removed.</li>
</ul>

 <img src="image/seller.png"> 
 
<ul>
   <li>Based on histogram graph of <b>offerType</b>, Table 1 and column description, this column has 2 unique values. “gesuch” value has only 12 records. So, this column has no distinguishing information for the model. This column can be dropped, after removing the records that has “gesuch” value. </li>
</ul>

<img src="image/offerType.png"> 

<ul>
   <li>Based on histogram graph of <b>abtest</b> and Table 1, this column has consistent values for the model. </li>
</ul>

<img src="image/abtest.png"> 

<ul>
   <li>Based on histogram graph of <b>monthOfRegistration</b> and Table 1, this column should have 12 unique values. However, it has 13 values. Also, dataset has yearOfRegistration column. So, this column can be dropped.</li>
</ul>
 
 <img src="image/monthOfRegistration.png"> 
 
<ul>
   <li><b>postalCode</b> column has <b>8150</b> unique values. This information can be used to determine the location of the car. However, for the model, location is not a distinguishing information because all car has postal code in Germany. Car location does not affect the model. This column can be dropped.</li>
</ul>
 
<img src="image/postalCode.png"> 

<ul>
   <li><b>dateCreated</b> column has <b>114</b> unique values. This column has no distinguishing information for the model. So, this column can be dropped</li>
</ul>
 
 <img src="image/dateCreated.png"> 
 
<ul>
   <li>Based on histogram of <b>price</b> column and its description, this column has <b>10772</b> records that has <b>0</b> value which means the car is free. Also, records have some value more than <b>100000 euro</b>. It is not a consistent variable because cars can’t be that much expensive. To make dataset more consistent, prices values which are <b>0</b> and larger than <b>100000</b> can be removed. The histogram graph of price column are below. <b>First</b> graph shows the <b>original distribution</b> of the prices. <b>Second</b> graph shows the prices without <b>free cars</b>. <b>Third</b> graph shows the prices <b>between 0 and 100000 euro</b>. Other records can be removed from the dataset to have consistent values.  </li>
</ul>
 
 <img src="image/price_100.png"> 

<ul>
   <li>Based on histogram of <b>yearsOfRegistration</b> column and its description result, this column has inconsistent values. For example, it has year values larger than <b>2017</b>. Also, there are some values smaller than <b>1900</b> which does not make sense because in that time engine did not invented. So, yersOfRegistration records can be limited between <b>1900- yearsOfRegistration-2017</b>.</li>
</ul>
 
 <img src="image/yearsOfRegistration.png"> 
 
<ul>
   <li>Based on histogram of <b>powerPS</b> and Table 1, this column has some inconsistent values. powerPS can’t be less than <b>0</b>. Also, powerPS can’t be stronger than <b>1000</b>. So, it can be limited between 0-powerPS-1000. Other records can be removed from the dataset to have consistent values.</li>
</ul>

<ul>
   <li>Based on histogram of <b>fuelType</b> and Table 1, this column has 7 different value type. Apart from <b>“benzin”</b> and <b>“diesel”</b>, other values have very low records. So, these values do not mean much for the model. These records can be removed from the dataset.</li>
</ul>
 
 <img src="image/fuelType.png"> 
 
<ul>
   <li>Based on <b>vehicleType</b> histogram and Table 1, it has 8 different values. Values are consistent and can be used for the model.</li>
</ul>
 
 <img src="image/vehicleType.png"> 
 
<ul>
   <li>Based on histogram of <b>model</b> and Table 1, this column has many different values. It can be useful for price prediction but to make the model simpler this column can be dropped. </li>
</ul>
 
<img src="image/model.png"> 

<ul>
   <li>Based on histogram of <b>kilometer</b> and table 1, this column has consistent values. Also, it can be useful for the model.</li>
</ul>
 
 <img src="image/kilometer.png"> 
 
<ul>
   <li>Based on histogram of <b>gearbox</b> and Table 1, this column has 2 different values and values are consistent.</li>
</ul>
               
<img src="image/gearbox.png"> 
               
<ul>
   <li>Based on histogram of <b>notRepairedDamage</b>, this column has 2 different values. Values are consistent and can be useful for the model.</li>
</ul>
 
 <img src="image/notRepairedDamage.png"> 
 
<ul>
   <li>Based on histogram of the <b>brand</b>, this column has 40 different values. It has consistent records and can be useful for the model.</li>
</ul>
 
 <img src="image/brand.png"> 
 
<ul>
   <li>Based on <b>year v.s. price graph</b>, it can be said that new cars are more expensive than old ones. However, there some old cars which are also expensive. </li>
</ul>
 
 <img src="image/year.png"> 
 
<ul>
   <li>Based on <b>powerPS v.s price graph</b>, low powerPS cars are cheaper than others. </li>
</ul>

<img src="image/power.png"> 

<h1>3.	PROBLEM SETTING</h1>
<p>The problem is predicting the actual price of the car by looking given parameters.<br>
There are <b>371528</b> records in dataset. <b>243422</b> of them are remaining after data cleaning process.<br>
2 models are implemented. <br>
One of them uses the <b>33%</b> of the dataset as a test set.<br>
Other one uses <b>10-fold validation</b> for testing issue
</p>

<h1>4.	MODELLING</h1>
<p>Before the implementation of the model. Dataset is cleaned using python libraries, and total number of column is decreased to 10 [<i>'vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model','kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'price'</i>]. 
</p>

<p>
After that, cleaned dataset is preprocessed using WEKA. WEKA attribute evaluator selected some attributes. It suggests the following attributes for the model [<i>'yearOfRegistration', 'gearbox', 'powerPS' ,'kilometer', 'fuelType', 'notRepairedDamage</i>].
</p>

<h1>5.	CONCLUSION and IMPROVEMENT POINTS</h1>



<h3>=== Run information ===</h3>
<p>
Scheme:       weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -num-decimal-places 4
Relation:     clean_data-weka.filters.unsupervised.attribute.Remove-R1,5,8
Instances:    243422
Attributes:   7
              yearOfRegistration
              gearbox
              powerPS
              kilometer
              fuelType
              notRepairedDamage
              price
Test mode:    split 66.0% train, remainder test
</p>
<h3>=== Classifier model (full training set) ===</h3>

<p>
Linear Regression Model

price =

    163.5077 * yearOfRegistration +
    603.5232 * gearbox=automatik +
     67.2908 * powerPS +
     -0.0831 * kilometer +
   2388.1937 * fuelType=diesel +
   1939.0536 * notRepairedDamage=nein +
-321897.5597

Time taken to build model: 0.27 seconds
</p>
<h3>=== Predictions on test split ===</h3>
<h3>Predictions for dataset clean_data-weka.filters.unsupervised.attribute.Remove-R1,5,8</h3>
<table border="1">
<tr>
<td>inst#</td><td>actual</td><td>predicted</td><td>error</td></tr>
<tr><td>88467</td><td align="right">1099</td><td align="right">4534.56</td><td align="right">3435.56</td></tr>
<tr><td>88468</td><td align="right">12400</td><td align="right">15222.946</td><td align="right">2822.946</td></tr>
<tr><td>88469</td><td align="right">3900</td><td align="right">2158.239</td><td align="right">-1741.761</td></tr>
<tr><td>88470</td><td align="right">3990</td><td align="right">3694.653</td><td align="right">-295.347</td></tr>
<tr><td>88471</td><td align="right">1700</td><td align="right">4001.936</td><td align="right">2301.936</td></tr>
<tr><td>88472</td><td align="right">1700</td><td align="right">3838.052</td><td align="right">2138.052</td></tr>
<tr><td>88473</td><td align="right">11500</td><td align="right">6050.489</td><td align="right">-5449.511</td></tr>
<tr><td>88474</td><td align="right">590</td><td align="right">3080.087</td><td align="right">2490.087</td></tr>
<tr><td>88475</td><td align="right">2700</td><td align="right">4391.161</td><td align="right">1691.161</td></tr>
<tr><td>88476</td><td align="right">7300</td><td align="right">4616.502</td><td align="right">-2683.498</td></tr>
<tr><td>88477</td><td align="right">5350</td><td align="right">2424.55</td><td align="right">-2925.45</td></tr>
<tr><td>88478</td><td align="right">1100</td><td align="right">3489.798</td><td align="right">2389.798</td></tr>
<tr><td>88479</td><td align="right">3550</td><td align="right">3694.653</td><td align="right">144.653</td></tr>
<tr><td>88480</td><td align="right">650</td><td align="right">3387.37</td><td align="right">2737.37</td></tr>
<tr><td>88481</td><td align="right">2490</td><td align="right">3182.515</td><td align="right">692.515</td></tr>
<tr><td>88482</td><td align="right">16999</td><td align="right">25519.214</td><td align="right">8520.214</td></tr>
<tr><td>88483</td><td align="right">10000</td><td align="right">18113.333</td><td align="right">8113.333</td></tr>
<tr><td>88484</td><td align="right">22700</td><td align="right">22832.718</td><td align="right">132.718</td></tr>
<tr><td>88485</td><td align="right">500</td><td align="right">3694.653</td><td align="right">3194.653</td></tr>
<tr><td>88486</td><td align="right">799</td><td align="right">3346.399</td><td align="right">2547.399</td></tr>
<tr><td>88487</td><td align="right">8700</td><td align="right">5825.148</td><td align="right">-2874.852</td></tr>
<tr><td>88488</td><td align="right">14990</td><td align="right">12410.643</td><td align="right">-2579.357</td></tr>
<tr><td>88489</td><td align="right">7450</td><td align="right">6193.887</td><td align="right">-1256.113</td></tr>
<tr><td>88490</td><td align="right">12340</td><td align="right">12861.325</td><td align="right">521.325</td></tr>
<tr><td>88491</td><td align="right">1100</td><td align="right">8928.104</td><td align="right">7828.104</td></tr>
<tr><td>88492</td><td align="right">6800</td><td align="right">3797.081</td><td align="right">-3002.919</td></tr>
<tr><td>88493</td><td align="right">1490</td><td align="right">3694.653</td><td align="right">2204.653</td></tr>
<tr><td>88494</td><td align="right">6100</td><td align="right">6111.945</td><td align="right">11.945</td></tr>
<tr><td>88495</td><td align="right">500</td><td align="right">12043.832</td><td align="right">11543.832</td></tr>
<tr><td>88496</td><td align="right">1999</td><td align="right">4657.473</td><td align="right">2658.473</td></tr>
<tr><td>88497</td><td align="right">4200</td><td align="right">5231.067</td><td align="right">1031.067</td></tr>
<tr><td>88498</td><td align="right">1099</td><td align="right">5169.611</td><td align="right">4070.611</td></tr>
<tr><td>88499</td><td align="right">8499</td><td align="right">8426.81</td><td align="right">-72.19</td></tr>
<tr><td>88500</td><td align="right">1200</td><td align="right">4247.762</td><td align="right">3047.762</td></tr>
<tr><td>88501</td><td align="right">7650</td><td align="right">5231.067</td><td align="right">-2418.933</td></tr>
<tr><td>88502</td><td align="right">1600</td><td align="right">14526.438</td><td align="right">12926.438</td></tr>
<tr><td>88503</td><td align="right">2750</td><td align="right">4944.27</td><td align="right">2194.27</td></tr>
<tr><td>88504</td><td align="right">18500</td><td align="right">6746.996</td><td align="right">-11753.004</td></tr>
<tr><td>88505</td><td align="right">600</td><td align="right">4001.936</td><td align="right">3401.936</td></tr>
<tr><td>88506</td><td align="right">2950</td><td align="right">2158.239</td><td align="right">-791.761</td></tr>
<tr><td>88507</td><td align="right">1949</td><td align="right">4944.27</td><td align="right">2995.27</td></tr>
<tr><td>88508</td><td align="right">22900</td><td align="right">12410.643</td><td align="right">-10489.357</td></tr>
<tr><td>88509</td><td align="right">500</td><td align="right">3182.515</td><td align="right">2682.515</td></tr>
<tr><td>88510</td><td align="right">8200</td><td align="right">23491.147</td><td align="right">15291.147</td></tr>
<tr><td>88511</td><td align="right">5000</td><td align="right">19759.889</td><td align="right">14759.889</td></tr>
<tr><td>88512</td><td align="right">2290</td><td align="right">5231.067</td><td align="right">2941.067</td></tr>
<tr><td>88513</td><td align="right">9990</td><td align="right">22650.276</td><td align="right">12660.276</td></tr>
<tr><td>88514</td><td align="right">2400</td><td align="right">3469.312</td><td align="right">1069.312</td></tr>
<tr><td>88515</td><td align="right">6500</td><td align="right">7776.094</td><td align="right">1276.094</td></tr>
<tr><td>88516</td><td align="right">4300</td><td align="right">5538.35</td><td align="right">1238.35</td></tr>
<tr><td>88517</td><td align="right">550</td><td align="right">5026.212</td><td align="right">4476.212</td></tr>
<tr><td>88518</td><td align="right">6099</td><td align="right">5087.669</td><td align="right">-1011.331</td></tr>
<tr><td>88519</td><td align="right">2799</td><td align="right">4473.103</td><td align="right">1674.103</td></tr>
<tr><td>88520</td><td align="right">5700</td><td align="right">5026.212</td><td align="right">-673.788</td></tr>
<tr><td>88521</td><td align="right">6900</td><td align="right">5640.778</td><td align="right">-1259.222</td></tr>
<tr><td>88522</td><td align="right">2650</td><td align="right">4534.56</td><td align="right">1884.56</td></tr>
<tr><td>88523</td><td align="right">14700</td><td align="right">18666.442</td><td align="right">3966.442</td></tr>
<tr><td>88524</td><td align="right">3200</td><td align="right">4944.27</td><td align="right">1744.27</td></tr>
<tr><td>88525</td><td align="right">2190</td><td align="right">4411.646</td><td align="right">2221.646</td></tr>
<tr><td>88526</td><td align="right">2500</td><td align="right">5087.669</td><td align="right">2587.669</td></tr>
<tr><td>88527</td><td align="right">800</td><td align="right">4718.929</td><td align="right">3918.929</td></tr>
<tr><td>88528</td><td align="right">5900</td><td align="right">8713.607</td><td align="right">2813.607</td></tr>
<tr><td>88529</td><td align="right">1200</td><td align="right">4247.762</td><td align="right">3047.762</td></tr>
<tr><td>88530</td><td align="right">1200</td><td align="right">3694.653</td><td align="right">2494.653</td></tr>
<tr><td>88531</td><td align="right">8000</td><td align="right">5087.669</td><td align="right">-2912.331</td></tr>
<tr><td>88532</td><td align="right">5550</td><td align="right">6808.453</td><td align="right">1258.453</td></tr>
<tr><td>88533</td><td align="right">6200</td><td align="right">15573.128</td><td align="right">9373.128</td></tr>
<tr><td>88534</td><td align="right">4499</td><td align="right">7776.094</td><td align="right">3277.094</td></tr>
<tr><td>88535</td><td align="right">2350</td><td align="right">3571.74</td><td align="right">1221.74</td></tr>
<tr><td>88536</td><td align="right">6999</td><td align="right">19510.206</td><td align="right">12511.206</td></tr>
<tr><td>88537</td><td align="right">16900</td><td align="right">12364.852</td><td align="right">-4535.148</td></tr>
<tr><td>88538</td><td align="right">8399</td><td align="right">12043.832</td><td align="right">3644.832</td></tr>
<tr><td>88539</td><td align="right">1400</td><td align="right">10464.518</td><td align="right">9064.518</td></tr>
<tr><td>88540</td><td align="right">8999</td><td align="right">14235.784</td><td align="right">5236.784</td></tr>
<tr><td>88541</td><td align="right">5749</td><td align="right">16413.035</td><td align="right">10664.035</td></tr>
<tr><td>88542</td><td align="right">6300</td><td align="right">18506.415</td><td align="right">12206.415</td></tr>
<tr><td>88543</td><td align="right">2450</td><td align="right">3694.653</td><td align="right">1244.653</td></tr>
<tr><td>88544</td><td align="right">2750</td><td align="right">4636.987</td><td align="right">1886.987</td></tr>
<tr><td>88545</td><td align="right">1490</td><td align="right">3694.653</td><td align="right">2204.653</td></tr>
<tr><td>88546</td><td align="right">7999</td><td align="right">4309.219</td><td align="right">-3689.781</td></tr>
<tr><td>88547</td><td align="right">27000</td><td align="right">23346.784</td><td align="right">-3653.216</td></tr>
<tr><td>88548</td><td align="right">2200</td><td align="right">3694.653</td><td align="right">1494.653</td></tr>
<tr><td>88549</td><td align="right">9490</td><td align="right">23100.958</td><td align="right">13610.958</td></tr>
<tr><td>88550</td><td align="right">5400</td><td align="right">4800.871</td><td align="right">-599.129</td></tr>
<tr><td>88551</td><td align="right">850</td><td align="right">3387.37</td><td align="right">2537.37</td></tr>
<tr><td>88552</td><td align="right">6500</td><td align="right">5825.148</td><td align="right">-674.852</td></tr>
<tr><td>88553</td><td align="right">14500</td><td align="right">11796.078</td><td align="right">-2703.922</td></tr>
<tr><td>88554</td><td align="right">51500</td><td align="right">21528.631</td><td align="right">-29971.369</td></tr>
<tr><td>88555</td><td align="right">23600</td><td align="right">21273.889</td><td align="right">-2326.111</td></tr>
<tr><td>88556</td><td align="right">1300</td><td align="right">4534.56</td><td align="right">3234.56</td></tr>
<tr><td>88557</td><td align="right">550</td><td align="right">4636.987</td><td align="right">4086.987</td></tr>
<tr><td>88558</td><td align="right">10450</td><td align="right">10009.016</td><td align="right">-440.984</td></tr>
<tr><td>88559</td><td align="right">16800</td><td align="right">5640.778</td><td align="right">-11159.222</td></tr>
<tr><td>88560</td><td align="right">2799</td><td align="right">4391.161</td><td align="right">1592.161</td></tr>
<tr><td>88561</td><td align="right">3800</td><td align="right">6854.245</td><td align="right">3054.245</td></tr>
<tr><td>88562</td><td align="right">2950</td><td align="right">4001.936</td><td align="right">1051.936</td></tr>
<tr><td>88563</td><td align="right">11500</td><td align="right">15141.004</td><td align="right">3641.004</td></tr>
<tr><td>88564</td><td align="right">9850</td><td align="right">8042.405</td><td align="right">-1807.595</td></tr>
<tr><td>88565</td><td align="right">2000</td><td align="right">7894.186</td><td align="right">5894.186</td></tr>
<tr><td>88566</td><td align="right">1500</td><td align="right">3551.254</td><td align="right">2051.254</td></tr>
<tr><td>88567</td><td align="right">5750</td><td align="right">8431.63</td><td align="right">2681.63</td></tr>
<tr><td>88568</td><td align="right">1699</td><td align="right">3387.37</td><td align="right">1688.37</td></tr>
<tr><td>88569</td><td align="right">4150</td><td align="right">5026.212</td><td align="right">876.212</td></tr>
<tr><td>88570</td><td align="right">1300</td><td align="right">4309.219</td><td align="right">3009.219</td></tr>
<tr><td>88571</td><td align="right">2500</td><td align="right">11675.093</td><td align="right">9175.093</td></tr>
<tr><td>88572</td><td align="right">999</td><td align="right">4534.56</td><td align="right">3535.56</td></tr>
<tr><td>88573</td><td align="right">2750</td><td align="right">2998.145</td><td align="right">248.145</td></tr>
<tr><td>88574</td><td align="right">950</td><td align="right">5231.067</td><td align="right">4281.067</td></tr>
<tr><td>88575</td><td align="right">13999</td><td align="right">13211.507</td><td align="right">-787.493</td></tr>
<tr><td>88576</td><td align="right">18500</td><td align="right">20556.896</td><td align="right">2056.896</td></tr>
<tr><td>88577</td><td align="right">5300</td><td align="right">5825.148</td><td align="right">525.148</td></tr>
<tr><td>88578</td><td align="right">999</td><td align="right">11511.209</td><td align="right">10512.209</td></tr>
<tr><td>88579</td><td align="right">7300</td><td align="right">16804.188</td><td align="right">9504.188</td></tr>
<tr><td>88580</td><td align="right">600</td><td align="right">2158.239</td><td align="right">1558.239</td></tr>
<tr><td>88581</td><td align="right">3850</td><td align="right">7079.586</td><td align="right">3229.586</td></tr>
<tr><td>88582</td><td align="right">10990</td><td align="right">4800.871</td><td align="right">-6189.129</td></tr>
<tr><td>88583</td><td align="right">9350</td><td align="right">5231.067</td><td align="right">-4118.933</td></tr>
<tr><td>88584</td><td align="right">95</td><td align="right">3489.798</td><td align="right">3394.798</td></tr>
<tr><td>88585</td><td align="right">2000</td><td align="right">4718.929</td><td align="right">2718.929</td></tr>
<tr><td>88586</td><td align="right">700</td><td align="right">3694.653</td><td align="right">2994.653</td></tr>
<tr><td>88587</td><td align="right">6700</td><td align="right">5231.067</td><td align="right">-1468.933</td></tr>
<tr><td>88588</td><td align="right">650</td><td align="right">4001.936</td><td align="right">3351.936</td></tr>
<tr><td>88589</td><td align="right">600</td><td align="right">3387.37</td><td align="right">2787.37</td></tr>
<tr><td>88590</td><td align="right">9999</td><td align="right">5640.778</td><td align="right">-4358.222</td></tr>
<tr><td>88591</td><td align="right">3650</td><td align="right">7776.094</td><td align="right">4126.094</td></tr>
<tr><td>88592</td><td align="right">2500</td><td align="right">11427.338</td><td align="right">8927.338</td></tr>
<tr><td>88593</td><td align="right">2500</td><td align="right">4309.219</td><td align="right">1809.219</td></tr>
<tr><td>88594</td><td align="right">2100</td><td align="right">4083.878</td><td align="right">1983.878</td></tr>
<tr><td>88595</td><td align="right">15990</td><td align="right">18197.204</td><td align="right">2207.204</td></tr>
<tr><td>88596</td><td align="right">840</td><td align="right">4165.82</td><td align="right">3325.82</td></tr>
<tr><td>88597</td><td align="right">950</td><td align="right">3387.37</td><td align="right">2437.37</td></tr>
<tr><td>88598</td><td align="right">1390</td><td align="right">4247.762</td><td align="right">2857.762</td></tr>
<tr><td>88599</td><td align="right">4200</td><td align="right">4227.277</td><td align="right">27.277</td></tr>
<tr><td>88600</td><td align="right">7250</td><td align="right">13848.487</td><td align="right">6598.487</td></tr>
<tr><td>88601</td><td align="right">5000</td><td align="right">6890.395</td><td align="right">1890.395</td></tr>
<tr><td>88602</td><td align="right">9500</td><td align="right">5640.778</td><td align="right">-3859.222</td></tr>
<tr><td>88603</td><td align="right">1099</td><td align="right">4227.277</td><td align="right">3128.277</td></tr>
<tr><td>88604</td><td align="right">4000</td><td align="right">5087.669</td><td align="right">1087.669</td></tr>
<tr><td>88605</td><td align="right">900</td><td align="right">6567.448</td><td align="right">5667.448</td></tr>
<tr><td>88606</td><td align="right">8500</td><td align="right">5026.212</td><td align="right">-3473.788</td></tr>
<tr><td>88607</td><td align="right">9200</td><td align="right">6624.083</td><td align="right">-2575.917</td></tr>
<tr><td>88608</td><td align="right">1200</td><td align="right">7550.753</td><td align="right">6350.753</td></tr>
<tr><td>88609</td><td align="right">450</td><td align="right">4206.791</td><td align="right">3756.791</td></tr>
<tr><td>88610</td><td align="right">31560</td><td align="right">24471.56</td><td align="right">-7088.44</td></tr>
<tr><td>88611</td><td align="right">2500</td><td align="right">11470.238</td><td align="right">8970.238</td></tr>
<tr><td>88612</td><td align="right">4499</td><td align="right">3879.023</td><td align="right">-619.977</td></tr>
<tr><td>88613</td><td align="right">27750</td><td align="right">19094.71</td><td align="right">-8655.29</td></tr>
<tr><td>88614</td><td align="right">1450</td><td align="right">3694.653</td><td align="right">2244.653</td></tr>
<tr><td>88615</td><td align="right">12900</td><td align="right">20782.237</td><td align="right">7882.237</td></tr>
<tr><td>88616</td><td align="right">790</td><td align="right">3387.37</td><td align="right">2597.37</td></tr>
<tr><td>88617</td><td align="right">1650</td><td align="right">3694.653</td><td align="right">2044.653</td></tr>
<tr><td>88618</td><td align="right">3500</td><td align="right">4841.842</td><td align="right">1341.842</td></tr>
<tr><td>88619</td><td align="right">5299</td><td align="right">5026.212</td><td align="right">-272.788</td></tr>
<tr><td>88620</td><td align="right">3300</td><td align="right">10935.686</td><td align="right">7635.686</td></tr>
<tr><td>88621</td><td align="right">3499</td><td align="right">4473.103</td><td align="right">974.103</td></tr>
<tr><td>88622</td><td align="right">9999</td><td align="right">16329.164</td><td align="right">6330.164</td></tr>
<tr><td>88623</td><td align="right">11990</td><td align="right">20556.896</td><td align="right">8566.896</td></tr>
<tr><td>88624</td><td align="right">1499</td><td align="right">3387.37</td><td align="right">1888.37</td></tr>
<tr><td>88625</td><td align="right">4950</td><td align="right">4534.56</td><td align="right">-415.44</td></tr>
<tr><td>88626</td><td align="right">2200</td><td align="right">6649.39</td><td align="right">4449.39</td></tr>
<tr><td>88627</td><td align="right">3950</td><td align="right">4309.219</td><td align="right">359.219</td></tr>
<tr><td>88628</td><td align="right">59000</td><td align="right">22070.896</td><td align="right">-36929.104</td></tr>
<tr><td>88629</td><td align="right">449</td><td align="right">3387.37</td><td align="right">2938.37</td></tr>
<tr><td>88630</td><td align="right">24400</td><td align="right">19877.017</td><td align="right">-4522.983</td></tr>
<tr><td>88631</td><td align="right">8400</td><td align="right">6624.083</td><td align="right">-1775.917</td></tr>
<tr><td>88632</td><td align="right">15000</td><td align="right">6050.489</td><td align="right">-8949.511</td></tr>
<tr><td>88633</td><td align="right">17500</td><td align="right">11376.725</td><td align="right">-6123.275</td></tr>
<tr><td>88634</td><td align="right">600</td><td align="right">5497.379</td><td align="right">4897.379</td></tr>
<tr><td>88635</td><td align="right">4450</td><td align="right">16804.188</td><td align="right">12354.188</td></tr>
<tr><td>88636</td><td align="right">750</td><td align="right">2158.239</td><td align="right">1408.239</td></tr>
<tr><td>88637</td><td align="right">6999</td><td align="right">6624.083</td><td align="right">-374.917</td></tr>
<tr><td>88638</td><td align="right">2500</td><td align="right">6111.945</td><td align="right">3611.945</td></tr>
<tr><td>88639</td><td align="right">499</td><td align="right">3694.653</td><td align="right">3195.653</td></tr>
<tr><td>88640</td><td align="right">2600</td><td align="right">4718.929</td><td align="right">2118.929</td></tr>
<tr><td>88641</td><td align="right">2500</td><td align="right">5722.72</td><td align="right">3222.72</td></tr>
<tr><td>88642</td><td align="right">6850</td><td align="right">6337.286</td><td align="right">-512.714</td></tr>
<tr><td>88643</td><td align="right">1950</td><td align="right">4657.473</td><td align="right">2707.473</td></tr>
<tr><td>88644</td><td align="right">3900</td><td align="right">5231.067</td><td align="right">1331.067</td></tr>
<tr><td>88645</td><td align="right">490</td><td align="right">6772.303</td><td align="right">6282.303</td></tr>
<tr><td>88646</td><td align="right">3700</td><td align="right">11736.549</td><td align="right">8036.549</td></tr>
<tr><td>88647</td><td align="right">3200</td><td align="right">3571.74</td><td align="right">371.74</td></tr>
<tr><td>88648</td><td align="right">500</td><td align="right">3080.087</td><td align="right">2580.087</td></tr>
<tr><td>88649</td><td align="right">9200</td><td align="right">20454.468</td><td align="right">11254.468</td></tr>
<tr><td>88650</td><td align="right">500</td><td align="right">7038.615</td><td align="right">6538.615</td></tr>
<tr><td>88651</td><td align="right">7800</td><td align="right">18998.068</td><td align="right">11198.068</td></tr>
<tr><td>88652</td><td align="right">800</td><td align="right">7386.869</td><td align="right">6586.869</td></tr>
<tr><td>88653</td><td align="right">1650</td><td align="right">4534.56</td><td align="right">2884.56</td></tr>
<tr><td>88654</td><td align="right">18900</td><td align="right">8411.145</td><td align="right">-10488.855</td></tr>
<tr><td>88655</td><td align="right">10000</td><td align="right">12658.398</td><td align="right">2658.398</td></tr>
<tr><td>88656</td><td align="right">1500</td><td align="right">4227.277</td><td align="right">2727.277</td></tr>
<tr><td>88657</td><td align="right">6450</td><td align="right">14343.996</td><td align="right">7893.996</td></tr>
<tr><td>88658</td><td align="right">7950</td><td align="right">8616</td><td align="right">666</td></tr>
<tr><td>88659</td><td align="right">1750</td><td align="right">4227.277</td><td align="right">2477.277</td></tr>
<tr><td>88660</td><td align="right">399</td><td align="right">4227.277</td><td align="right">3828.277</td></tr>
<tr><td>88661</td><td align="right">7950</td><td align="right">5026.212</td><td align="right">-2923.788</td></tr>
<tr><td>88662</td><td align="right">1850</td><td align="right">5108.154</td><td align="right">3258.154</td></tr>
<tr><td>88663</td><td align="right">930</td><td align="right">3694.653</td><td align="right">2764.653</td></tr>
<tr><td>88664</td><td align="right">1599</td><td align="right">3715.139</td><td align="right">2116.139</td></tr>
<tr><td>88665</td><td align="right">9990</td><td align="right">5087.669</td><td align="right">-4902.331</td></tr>
<tr><td>88666</td><td align="right">1000</td><td align="right">4411.646</td><td align="right">3411.646</td></tr>
<tr><td>88667</td><td align="right">550</td><td align="right">7263.955</td><td align="right">6713.955</td></tr>
<tr><td>88668</td><td align="right">5790</td><td align="right">4391.161</td><td align="right">-1398.839</td></tr>
<tr><td>88669</td><td align="right">3290</td><td align="right">5087.669</td><td align="right">1797.669</td></tr>
<tr><td>88670</td><td align="right">3100</td><td align="right">4575.531</td><td align="right">1475.531</td></tr>
<tr><td>88671</td><td align="right">900</td><td align="right">5231.067</td><td align="right">4331.067</td></tr>
<tr><td>88672</td><td align="right">15749</td><td align="right">5825.148</td><td align="right">-9923.852</td></tr>
<tr><td>88673</td><td align="right">4390</td><td align="right">5026.212</td><td align="right">636.212</td></tr>
<tr><td>88674</td><td align="right">15999</td><td align="right">18975.654</td><td align="right">2976.654</td></tr>
<tr><td>88675</td><td align="right">2995</td><td align="right">3551.254</td><td align="right">556.254</td></tr>
<tr><td>88676</td><td align="right">5000</td><td align="right">8001.434</td><td align="right">3001.434</td></tr>
<tr><td>88677</td><td align="right">3250</td><td align="right">4391.161</td><td align="right">1141.161</td></tr>
<tr><td>88678</td><td align="right">500</td><td align="right">4718.929</td><td align="right">4218.929</td></tr>
<tr><td>88679</td><td align="right">300</td><td align="right">6746.996</td><td align="right">6446.996</td></tr>
<tr><td>88680</td><td align="right">2700</td><td align="right">10566.946</td><td align="right">7866.946</td></tr>
<tr><td>88681</td><td align="right">23900</td><td align="right">20020.416</td><td align="right">-3879.584</td></tr>
<tr><td>88682</td><td align="right">150</td><td align="right">3284.942</td><td align="right">3134.942</td></tr>
<tr><td>88683</td><td align="right">6500</td><td align="right">6337.286</td><td align="right">-162.714</td></tr>
<tr><td>88684</td><td align="right">13800</td><td align="right">5087.669</td><td align="right">-8712.331</td></tr>
<tr><td>88685</td><td align="right">3200</td><td align="right">7919.492</td><td align="right">4719.492</td></tr>
<tr><td>88686</td><td align="right">999</td><td align="right">4616.502</td><td align="right">3617.502</td></tr>
<tr><td>88687</td><td align="right">17500</td><td align="right">16062.852</td><td align="right">-1437.148</td></tr>
<tr><td>88688</td><td align="right">6199</td><td align="right">5640.778</td><td align="right">-558.222</td></tr>
<tr><td>88689</td><td align="right">4500</td><td align="right">8083.377</td><td align="right">3583.377</td></tr>
<tr><td>88690</td><td align="right">999</td><td align="right">3346.399</td><td align="right">2347.399</td></tr>
<tr><td>88691</td><td align="right">1000</td><td align="right">3694.653</td><td align="right">2694.653</td></tr>
<tr><td>88692</td><td align="right">31800</td><td align="right">23981.835</td><td align="right">-7818.165</td></tr>
<tr><td>88693</td><td align="right">1550</td><td align="right">4247.762</td><td align="right">2697.762</td></tr>
<tr><td>88694</td><td align="right">12000</td><td align="right">21521.644</td><td align="right">9521.644</td></tr>
<tr><td>88695</td><td align="right">8490</td><td align="right">11079.084</td><td align="right">2589.084</td></tr>
<tr><td>88696</td><td align="right">1290</td><td align="right">4124.849</td><td align="right">2834.849</td></tr>
<tr><td>88697</td><td align="right">1100</td><td align="right">4329.704</td><td align="right">3229.704</td></tr>
<tr><td>88698</td><td align="right">1950</td><td align="right">4800.871</td><td align="right">2850.871</td></tr>
<tr><td>88699</td><td align="right">2450</td><td align="right">5784.177</td><td align="right">3334.177</td></tr>
<tr><td>88700</td><td align="right">4999</td><td align="right">6890.395</td><td align="right">1891.395</td></tr>
<tr><td>88701</td><td align="right">2600</td><td align="right">6193.887</td><td align="right">3593.887</td></tr>
<tr><td>88702</td><td align="right">900</td><td align="right">4575.531</td><td align="right">3675.531</td></tr>
<tr><td>88703</td><td align="right">2750</td><td align="right">4227.277</td><td align="right">1477.277</td></tr>
<tr><td>88704</td><td align="right">1249</td><td align="right">4411.646</td><td align="right">3162.646</td></tr>
<tr><td>88705</td><td align="right">5990</td><td align="right">19202.923</td><td align="right">13212.923</td></tr>
<tr><td>88706</td><td align="right">7500</td><td align="right">4657.473</td><td align="right">-2842.527</td></tr>
<tr><td>88707</td><td align="right">6200</td><td align="right">4247.762</td><td align="right">-1952.238</td></tr>
<tr><td>88708</td><td align="right">14990</td><td align="right">20556.896</td><td align="right">5566.896</td></tr>
<tr><td>88709</td><td align="right">100</td><td align="right">6198.708</td><td align="right">6098.708</td></tr>
<tr><td>88710</td><td align="right">8799</td><td align="right">5231.067</td><td align="right">-3567.933</td></tr>
<tr><td>88711</td><td align="right">1999</td><td align="right">10464.518</td><td align="right">8465.518</td></tr>
<tr><td>88712</td><td align="right">1150</td><td align="right">4104.364</td><td align="right">2954.364</td></tr>
<tr><td>88713</td><td align="right">12950</td><td align="right">5026.212</td><td align="right">-7923.788</td></tr>
<tr><td>88714</td><td align="right">0</td><td align="right">8928.104</td><td align="right">8928.104</td></tr>
<tr><td>88715</td><td align="right">14999</td><td align="right">5640.778</td><td align="right">-9358.222</td></tr>
<tr><td>88716</td><td align="right">3500</td><td align="right">5231.067</td><td align="right">1731.067</td></tr>
<tr><td>88717</td><td align="right">1250</td><td align="right">12310.144</td><td align="right">11060.144</td></tr>
<tr><td>88718</td><td align="right">3700</td><td align="right">15450.215</td><td align="right">11750.215</td></tr>
<tr><td>88719</td><td align="right">399</td><td align="right">3387.37</td><td align="right">2988.37</td></tr>
<tr><td>88720</td><td align="right">1300</td><td align="right">5128.64</td><td align="right">3828.64</td></tr>
<tr><td>88721</td><td align="right">850</td><td align="right">6214.373</td><td align="right">5364.373</td></tr>
<tr><td>88722</td><td align="right">0</td><td align="right">5026.212</td><td align="right">5026.212</td></tr>
<tr><td>88723</td><td align="right">500</td><td align="right">3264.457</td><td align="right">2764.457</td></tr>
<tr><td>88724</td><td align="right">900</td><td align="right">2158.239</td><td align="right">1258.239</td></tr>
<tr><td>88725</td><td align="right">5500</td><td align="right">15839.44</td><td align="right">10339.44</td></tr>
</table>
</div>
</body>
