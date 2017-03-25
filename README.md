<h1>Used Car Price Prediction using Linear Regression</h1>
<div align="justify">
<h1><span style="color: #ffbf00;">1. DATASET</span></h1>
<p>1. <strong><span style="color: #ffbf00;">dateCrawled</span></strong> : <em>when this ad was first crawled, all field-values are taken from this date</em> <br /> 2. <strong><span style="color: #ffbf00;">name</span></strong> : <em>"name" of the car </em><br /> 3. <strong><span style="color: #ffbf00;">seller</span></strong> : <em>private or dealer </em><br /> 4. <strong><span style="color: #ffbf00;">offerType</span></strong> : <em>the selling type of the car </em><br /> 5. <strong><span style="color: #ffbf00;">price</span></strong> : <em>the price on the ad to sell the car </em><br /> 6. <strong><span style="color: #ffbf00;">abtest</span></strong> : <em>unknown </em><br /> 7. <strong><span style="color: #ffbf00;">vehicleType</span></strong> : <em>type of the car. Limousine, kleinwagen, kombi, bus etc. </em><br /> 8. <strong><span style="color: #ffbf00;">yearOfRegistration</span></strong> : <em>at which year the car was first registered</em><br /> 9. <strong><span style="color: #ffbf00;">gearbox</span></strong> : <em>manuel or otomatic</em><br /> 10. <strong><span style="color: #ffbf00;">powerPS</span></strong> : <em>power of the car in PS</em><br /> 11. <strong><span style="color: #ffbf00;">model</span></strong> : <em>model of the car</em><br /> 12. <strong><span style="color: #ffbf00;">kilometer</span></strong> : <em>how many kilometers the car has driven</em><br /> 13. <strong><span style="color: #ffbf00;">monthOfRegistration</span></strong> : <em>at which month the car was first registered</em><br /> 14. <strong><span style="color: #ffbf00;">fuelType</span></strong> : <em>benzin, diesel, lpg etc</em><br /> 15. <strong><span style="color: #ffbf00;">brand</span></strong> : <em>brand of the car. Mercedes, Porsche, audi etc&hellip;</em><br /> 16. <strong><span style="color: #ffbf00;">notRepairedDamage</span></strong> : <em>if the car has a damage which is not repaired yet. Yes or no</em><br /> 17. <strong><span style="color: #ffbf00;">dateCreated</span></strong> : <em>the date for which the ad at ebay was created</em><br /> 18. <strong><span style="color: #ffbf00;">nrOfPictures</span></strong> : <em>number of pictures in the ad </em><br /> 19. <strong><span style="color: #ffbf00;">postalCode</span></strong> : <em>code that shows the location of the car</em><br /> 20. <strong><span style="color: #ffbf00;">lastSeenOnline</span></strong> : <em>when the crawler saw this ad last online</em></p>
<h1><span style="color: #ffbf00;">2. DATA EXPLORATION</span></h1>
<p>Dataset consists of <strong><span style="color: #ffbf00;">371528 rows</span></strong> and <strong><span style="color: #ffbf00;">20 columns</span></strong> [<em>dateCrawled, name, seller, offerType, price, abtest, vehicleType, yearOfRegistration, gearbox, powerPS, model, kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage, dateCreated, nrOfPictures, postalCode, lastSeen</em>].</p>
<img src="image/missing_value.png" alt="Table 1" /><br />
<p><em>Figure 1: Missing Value</em></p>
<h3>According to Figure 1:</h3>
<ul>
<li><strong><span style="color: #ffbf00;">5 columns</span></strong> [<em>vehicleType, gearbox, model, fuelType, notRepairedDamage</em>] have missing values. Depending on the model, these columns can be removed completely. However, these columns could be important for the model. So, the records that have null values can be removed. By removing the null values column can be saved for the model. In the table, notRepairedDamage column has <strong><span style="color: #ffbf00;">72060 missing value</span></strong> which is the <strong><span style="color: #ffbf00;">19%</span></strong> of the whole dataset. In this case, removing each record is not the best option. It seems better to drop whole column.</li>
<li>In the whole dataset, <strong><span style="color: #ffbf00;">110572</span></strong> records has at least one missing value. Removing these records are not the best option because it causes <strong><span style="color: #ffbf00;">33% data loss</span></strong>. So, data loss can be decreased by dropping some non-important columns or a representing value can be assigned the missing values.</li>
</ul>
<h3>According to Table 1 and the Histogram Graph of the columns:</h3>
<ul>
<li>dateCrawled (280500), name (233531), lastSeen (182806) columns have too many unique values. Depending on the learning model, these columns can be dropped.</li>
</ul>
<p><img src="image/table_1.png" alt="Table 1" /></p>
<ul>
<li>Histogram of <strong><span style="color: #ffbf00;">nrOfPictures</span></strong> column and Table 1 says that this column has only one values and it has no meaning for model and visualization. This column can be dropped.</li>
</ul>
<p><img src="image/nrOfPictures.png" alt="" /></p>
<ul>
<li>Histogram graph of <strong><span style="color: #ffbf00;">seller</span></strong> column and Table 1 says that this column has 2 unique values and &ldquo;gewerblich&rdquo; value has only 3 records. So, this column has no distinguishing information for the model. This column can be dropped, but first the records that has &ldquo;gewerblich&rdquo; value should be removed.</li>
</ul>
<p><img src="image/seller.png" alt="" /></p>
<ul>
<li>Based on histogram graph of <strong><span style="color: #ffbf00;">offerType</span></strong>, Table 1 and column description, this column has 2 unique values. &ldquo;gesuch&rdquo; value has only 12 records. So, this column has no distinguishing information for the model. This column can be dropped, after removing the records that has &ldquo;gesuch&rdquo; value.</li>
</ul>
<p><img src="image/offerType.png" alt="" /></p>
<ul>
<li>Based on histogram graph of <strong><span style="color: #ffbf00;">abtest</span></strong> and Table 1, this column has consistent values for the model.</li>
</ul>
<p><img src="image/abtest.png" alt="" /></p>
<ul>
<li>Based on histogram graph of <strong><span style="color: #ffbf00;">monthOfRegistration</span></strong> and Table 1, this column should have 12 unique values. However, it has 13 values. Also, dataset has yearOfRegistration column. So, this column can be dropped.</li>
</ul>
<p><img src="image/monthOfRegistration.png" alt="" /></p>
<ul>
<li><strong><span style="color: #ffbf00;">postalCode</span></strong> column has <strong><span style="color: #ffbf00;">8150</span></strong> unique values. This information can be used to determine the location of the car. However, for the model, location is not a distinguishing information because all car has postal code in Germany. Car location does not affect the model. This column can be dropped.</li>
</ul>
<p><img src="image/postalCode.png" alt="" /></p>
<ul>
<li><strong><span style="color: #ffbf00;">dateCreated</span></strong> column has <strong><span style="color: #ffbf00;">114</span></strong> unique values. This column has no distinguishing information for the model. So, this column can be dropped</li>
</ul>
<p><img src="image/dateCreated.png" alt="" /></p>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">price</span></strong> column and its description, this column has <strong><span style="color: #ffbf00;">10772</span></strong> records that has <strong><span style="color: #ffbf00;">0</span></strong> value which means the car is free. Also, records have some value more than <strong><span style="color: #ffbf00;">100000 euro</span></strong>. It is not a consistent variable because cars can&rsquo;t be that much expensive. To make dataset more consistent, prices values which are <strong><span style="color: #ffbf00;">0</span></strong> and larger than <strong><span style="color: #ffbf00;">100000</span></strong> can be removed. The histogram graph of price column are below. <strong><span style="color: #ffbf00;">First</span></strong> graph shows the <strong><span style="color: #ffbf00;">original distribution</span></strong> of the prices. <strong><span style="color: #ffbf00;">Second</span></strong> graph shows the prices without <strong><span style="color: #ffbf00;">free cars</span></strong>. <strong><span style="color: #ffbf00;">Third</span></strong> graph shows the prices <strong><span style="color: #ffbf00;">between 0 and 100000 euro</span></strong>. Other records can be removed from the dataset to have consistent values.</li>
</ul>
<p><img src="image/price_100.png" alt="" /></p>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">yearsOfRegistration</span></strong> column and its description result, this column has inconsistent values. For example, it has year values larger than <strong><span style="color: #ffbf00;">2017</span></strong>. Also, there are some values smaller than <strong><span style="color: #ffbf00;">1900</span></strong> which does not make sense because in that time engine did not invented. So, yersOfRegistration records can be limited between <strong><span style="color: #ffbf00;">1900- yearsOfRegistration-2017</span></strong>.</li>
</ul>
<p><img src="image/yearsOfRegistration.png" alt="" /></p>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">powerPS</span></strong> and Table 1, this column has some inconsistent values. powerPS can&rsquo;t be less than <strong><span style="color: #ffbf00;">0</span></strong>. Also, powerPS can&rsquo;t be stronger than <strong><span style="color: #ffbf00;">1000</span></strong>. So, it can be limited between 0-powerPS-1000. Other records can be removed from the dataset to have consistent values.</li>
</ul>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">fuelType</span></strong> and Table 1, this column has 7 different value type. Apart from <strong><span style="color: #ffbf00;">&ldquo;benzin&rdquo;</span></strong> and <strong><span style="color: #ffbf00;">&ldquo;diesel&rdquo;</span></strong>, other values have very low records. So, these values do not mean much for the model. These records can be removed from the dataset.</li>
</ul>
<p><img src="image/fuelType.png" alt="" /></p>
<ul>
<li>Based on <strong><span style="color: #ffbf00;">vehicleType</span></strong> histogram and Table 1, it has 8 different values. Values are consistent and can be used for the model.</li>
</ul>
<p><img src="image/vehicleType.png" alt="" /></p>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">model</span></strong> and Table 1, this column has many different values. It can be useful for price prediction but to make the model simpler this column can be dropped.</li>
</ul>
<p><img src="image/model.png" alt="" /></p>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">kilometer</span></strong> and table 1, this column has consistent values. Also, it can be useful for the model.</li>
</ul>
<p><img src="image/kilometer.png" alt="" /></p>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">gearbox</span></strong> and Table 1, this column has 2 different values and values are consistent.</li>
</ul>
<p><img src="image/gearbox.png" alt="" /></p>
<ul>
<li>Based on histogram of <strong><span style="color: #ffbf00;">notRepairedDamage</span></strong>, this column has 2 different values. Values are consistent and can be useful for the model.</li>
</ul>
<p><img src="image/notRepairedDamage.png" alt="" /></p>
<ul>
<li>Based on histogram of the <strong><span style="color: #ffbf00;">brand</span></strong>, this column has 40 different values. It has consistent records and can be useful for the model. Also, it can be said that volkswagen is the most popular car.</li>
</ul>
<p><img src="image/brand.png" alt="" /></p>
<ul>
<li>Based on <strong><span style="color: #ffbf00;">year v.s. price graph</span></strong>, it can be said that new cars are more expensive than old ones. However, there some old cars which are also expensive.</li>
</ul>
<p><img src="image/year.png" alt="" /></p>
<ul>
<li>Based on <strong><span style="color: #ffbf00;">powerPS v.s price graph</span></strong>, low powerPS cars are cheaper than others.</li>
</ul>
<p><img src="image/power.png" alt="" /></p>
<h1><span style="color: #ffbf00;">3. PROBLEM SETTING</span></h1>
<p>The problem is predicting the actual price of the car by looking given parameters.<br /> There are <strong><span style="color: #ffbf00;">371528</span></strong> records in dataset. <strong><span style="color: #ffbf00;">243422</span></strong> of them are remaining after data cleaning process.<br /> 2 models are implemented. <br /> One of them uses the <strong><span style="color: #ffbf00;">30%</span></strong> of the dataset as a test set.<br /> Other one uses <strong><span style="color: #ffbf00;">33%</span></strong> for testing issue</p>
<h1><span style="color: #ffbf00;">4. MODELLING</span></h1>
<p>Before the implementation of the model. Dataset is cleaned using python libraries, and total number of column is decreased to 10 [<em>'vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model','kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'price'</em>].</p>
<p>After that, cleaned dataset is preprocessed using WEKA. WEKA attribute evaluator selected some attributes. It suggests the following attributes for the model [<em>'yearOfRegistration', 'gearbox', 'powerPS' ,'kilometer', 'fuelType', 'notRepairedDamage</em>].</p>
<h3><span style="color: #ffbf00;">There are 2 different implementation of linear regression model:</span></h3>
<ul>
<ul>
<li>First model is implemented using <span style="color: #ffbf00;">python sklearn library</span>.</li>
It has</ul>
</ul>
<span style="color: #ffbf00;">10</span>
<ul>
<ul>attributes.</ul>
</ul>
<br /><span style="color: #ffbf00;">30 percentage</span>
<ul>
<ul>of the dataset is used for testing.</ul>
</ul>
<br /><br />
<ul>
<ul>
<li>Second model is implemented using <span style="color: #ffbf00;">WEKA</span>.</li>
</ul>
</ul>
<span style="color: #ffbf00;">Attributeselection</span>
<ul>
<ul>filter of WEKA applied on the dataset.</ul>
</ul>
<br />
<ul>
<ul>Filter removed the</ul>
</ul>
<span style="color: #ffbf00;">3</span>
<ul>
<ul>attributes. Remaining</ul>
</ul>
<span style="color: #ffbf00;">7</span>
<ul>
<ul>attributes are used for learning.</ul>
</ul>
<br /><span style="color: #ffbf00;">33 percentage</span>
<ul>
<ul>of the dataset is used for testing.</ul>
</ul>
<br />
<h1><span style="color: #ffbf00;">5. CONCLUSION and IMPROVEMENT POINTS</span></h1>
<p>First 20 prediction of the both model is on the below table.<br /> Python Sklearn Regression model has lower error than the WEKA model.<br /> It gives pretty good result for such a simple model. <br /> In order to improve the model:<br /> - dataset cleaning could be more effienct. According to histogram graph of the attributes, they have lots of inconsistent values.<br /> - age of the car attribute can improve the model. <span style="color: #ffbf00;">Age attribute</span> could be extracted by using registrationDate and dateCreated attributes.<br /> - according to attributeselection filter of the WEKA, <span style="color: #ffbf00;">"kilometer"</span> and <span style="color: #ffbf00;">"powerPS"</span> attributes are the most important ones.</p>
<h3>Following results are taken from python sklearn model:</h3>
<p><span style="color: #ffbf00;">Root mean squared error: 555.6768635632562</span><br /> mean_absulute_error: <span style="color: #ffbf00;">397.8973442835626</span><br /> mean_squared_error: <span style="color: #ffbf00;">308776.7766994987</span></p>
<h3>Following results are taken from WEKA model:</h3>
<p><span style="color: #ffbf00;">Root mean squared error:4958.1553</span><br /> Mean absolute error: <span style="color: #ffbf00;">3103.1781</span><br /> Correlation coefficient: <span style="color: #ffbf00;">0.7864</span><br /> Relative absolute error: <span style="color: #ffbf00;">56.7852 %</span><br /> Root relative squared error: <span style="color: #ffbf00;">61.7716 %</span><br /> Total Number of Instances: <span style="color: #ffbf00;">82763</span> <br /><br /></p>
<h1>PYTHON SKLEARN LINEAR REGRESSION MODEL RESULT</h1>
<p>Root mean squared error: 555.6768635632562</p>
<table border="2">
<tbody>
<tr>
<td>inst#</td>
<td>actual</td>
<td>predicted</td>
<td>error</td>
</tr>
<tr>
<td>1</td>
<td align="right">400</td>
<td align="right">419.435</td>
<td align="right">19.435</td>
</tr>
<tr>
<td>2</td>
<td align="right">400</td>
<td align="right">602.408</td>
<td align="right">202.408</td>
</tr>
<tr>
<td>3</td>
<td align="right">624</td>
<td align="right">955.720</td>
<td align="right">331.720</td>
</tr>
<tr>
<td>4</td>
<td align="right">2579</td>
<td align="right">1690.700</td>
<td align="right">888.299</td>
</tr>
<tr>
<td>5</td>
<td align="right">2166</td>
<td align="right">1737.427</td>
<td align="right">428.572</td>
</tr>
<tr>
<td>6</td>
<td align="right">1697</td>
<td align="right">2051.277</td>
<td align="right">354.277</td>
</tr>
<tr>
<td>7</td>
<td align="right">835</td>
<td align="right">839.545</td>
<td align="right">4.545</td>
</tr>
<tr>
<td>8</td>
<td align="right">3062</td>
<td align="right">2340.980</td>
<td align="right">721.019</td>
</tr>
<tr>
<td>9</td>
<td align="right">2273</td>
<td align="right">1970.432</td>
<td align="right">302.567</td>
</tr>
<tr>
<td>10</td>
<td align="right">897</td>
<td align="right">1485.134</td>
<td align="right">588.134</td>
</tr>
<tr>
<td>11</td>
<td align="right">2006</td>
<td align="right">2126.953</td>
<td align="right">120.953</td>
</tr>
<tr>
<td>12</td>
<td align="right">1225</td>
<td align="right">1281.999</td>
<td align="right">56.999</td>
</tr>
<tr>
<td>13</td>
<td align="right">1149</td>
<td align="right">695.919</td>
<td align="right">453.080</td>
</tr>
<tr>
<td>14</td>
<td align="right">1863</td>
<td align="right">1228.076</td>
<td align="right">634.923</td>
</tr>
<tr>
<td>15</td>
<td align="right">3352</td>
<td align="right">2866.412</td>
<td align="right">485.587</td>
</tr>
<tr>
<td>16</td>
<td align="right">2056</td>
<td align="right">1947.652</td>
<td align="right">108.347</td>
</tr>
<tr>
<td>17</td>
<td align="right">0</td>
<td align="right">664.973</td>
<td align="right">664.973</td>
</tr>
<tr>
<td>18</td>
<td align="right">1975</td>
<td align="right">1852.990</td>
<td align="right">122.009</td>
</tr>
<tr>
<td>19</td>
<td align="right">932</td>
<td align="right">868.003</td>
<td align="right">63.996</td>
</tr>
<tr>
<td>20</td>
<td align="right">3435</td>
<td align="right">2710.145</td>
<td align="right">724.854</td>
</tr>
</tbody>
</table>
<h1>WEKA MODEL RESULT</h1>
<p>Root mean squared error: 4958.1553</p>
<table border="2">
<tbody>
<tr>
<td>inst#</td>
<td>actual</td>
<td>predicted</td>
<td>error</td>
</tr>
<tr>
<td>1</td>
<td align="right">9499</td>
<td align="right">5840.168</td>
<td align="right">-3658.832</td>
</tr>
<tr>
<td>2</td>
<td align="right">7990</td>
<td align="right">12515.27</td>
<td align="right">4525.27</td>
</tr>
<tr>
<td>3</td>
<td align="right">4000</td>
<td align="right">5139.611</td>
<td align="right">1139.611</td>
</tr>
<tr>
<td>4</td>
<td align="right">10700</td>
<td align="right">14125.198</td>
<td align="right">3425.198</td>
</tr>
<tr>
<td>5</td>
<td align="right">690</td>
<td align="right">-3346.537</td>
<td align="right">-4036.537</td>
</tr>
<tr>
<td>6</td>
<td align="right">1450</td>
<td align="right">3834.998</td>
<td align="right">2384.998</td>
</tr>
<tr>
<td>7</td>
<td align="right">1000</td>
<td align="right">720.987</td>
<td align="right">-279.013</td>
</tr>
<tr>
<td>8</td>
<td align="right">7800</td>
<td align="right">5329.186</td>
<td align="right">-2470.814</td>
</tr>
<tr>
<td>9</td>
<td align="right">8150</td>
<td align="right">8553.781</td>
<td align="right">403.781</td>
</tr>
<tr>
<td>10</td>
<td align="right">1111</td>
<td align="right">720.987</td>
<td align="right">-390.013</td>
</tr>
<tr>
<td>11</td>
<td align="right">9899</td>
<td align="right">16116.077</td>
<td align="right">6217.077</td>
</tr>
<tr>
<td>12</td>
<td align="right">150</td>
<td align="right">-4427.849</td>
<td align="right">-4577.849</td>
</tr>
<tr>
<td>13</td>
<td align="right">2000</td>
<td align="right">5802.808</td>
<td align="right">3802.808</td>
</tr>
<tr>
<td>14</td>
<td align="right">15000</td>
<td align="right">11530.067</td>
<td align="right">-3469.933</td>
</tr>
<tr>
<td>15</td>
<td align="right">8000</td>
<td align="right">10208.546</td>
<td align="right">2208.546</td>
</tr>
<tr>
<td>16</td>
<td align="right">4190</td>
<td align="right">4656.816</td>
<td align="right">466.816</td>
</tr>
<tr>
<td>17</td>
<td align="right">16000</td>
<td align="right">20750.782</td>
<td align="right">4750.782</td>
</tr>
<tr>
<td>18</td>
<td align="right">6000</td>
<td align="right">7567.218</td>
<td align="right">1567.218</td>
</tr>
<tr>
<td>19</td>
<td align="right">2800</td>
<td align="right">4278.547</td>
<td align="right">1478.547</td>
</tr>
<tr>
<td>20</td>
<td align="right">399</td>
<td align="right">1198.466</td>
<td align="right">799.466</td>
</tr>
</tbody>
</table>
</div>
