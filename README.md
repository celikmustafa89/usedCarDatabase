
<body>
<div align="center">

<h1>1.	DATASET</h1>
<p align="left">
1.	<b>dateCrawled</b> : when this ad was first crawled, all field-values are taken from this date <br>
2.	<b>name</b> : "name" of the car <br>
3.	<b>seller</b> : private or dealer <br>
4.	<b>offerType</b> : the selling type of the car <br>
5.	<b>price</b> : the price on the ad to sell the car <br>
6.	<b>abtest</b> : unknown <br>
7.	<b>vehicleType</b> : type of the car. Limousine, kleinwagen, kombi, bus etc. <br>
8.	<b>yearOfRegistration</b> : at which year the car was first registered<br>
9.	<b>gearbox</b> : manuel or otomatic<br>
10.	<b>powerPS</b> : power of the car in PS<br>
11.	<b>model</b> : model of the car<br>
12.	<b>kilometer</b> : how many kilometers the car has driven<br>
13.	<b>monthOfRegistration</b> : at which month the car was first registered<br>
14.	<b>fuelType</b> : benzin, diesel, lpg etc<br>
15.	<b>brand</b> : brand of the car. Mercedes, Porsche, audi etc…<br>
16.	<b>notRepairedDamage</b> : if the car has a damage which is not repaired yet. Yes or no<br>
17.	<b>dateCreated</b> : the date for which the ad at ebay was created<br>
18.	<b>nrOfPictures</b> : number of pictures in the ad <br>
19.	<b>postalCode</b> : code that shows the location of the car<br>
20.	<b>lastSeenOnline</b> : when the crawler saw this ad last online<br>
</p>

<h1>2.	DATA EXPLORATION</h1>
<p align="left">
Dataset consists of 371528 rows and 20 columns [dateCrawled, name, seller, offerType, price, abtest, vehicleType, yearOfRegistration, gearbox, powerPS, model, kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage, dateCreated, nrOfPictures, postalCode, lastSeen]. 
</p>

<img src="image/missing_value.png" alt="Table 1"><br> 

<p align="left">
Figure 1: Missing Value<br>
According to Figure 1:<br>
</p>
<ul align="left">
   <li>
   5 columns [vehicleType, gearbox, model, fuelType, notRepairedDamage] have missing values. Depending on the model, these columns can be removed completely. However, these columns could be important for the model. So, the records that have null values can be removed. By removing the null values column can be saved for the model. In the table, notRepairedDamage column has 72060 missing value which is the 19% of the whole dataset. In this case, removing each record is not the best option. It seems better to drop whole column.
   </li>

   <li>
   In the whole dataset, 110572 records has at least one missing value. Removing these records are not the best option because it causes  33% data loss. So, data loss can be decreased by dropping some non-important columns or a representing value can be assigned the missing values.
   </li>
</ul>

<p align="left">According to Table 1 and the Histogram Graph of the columns:</p>
<ul>
   <li>dateCrawled (280500), name (233531), lastSeen (182806) columns have too many unique values. Depending on the learning model, these columns can be dropped.</li>
</ul>
<img src="image/table_1.png" alt="Table 1">




<ul>
   <li>Histogram of nrOfPictures column and Table 1 says that this column has only one values and it has no meaning for model and visualization. This column can be dropped.</li>
</ul>
 
<ul>
   <li>Histogram graph of seller column and Table 1 says that this column has 2 unique values and “gewerblich” value has only 3 records. So, this column has no distinguishing information for the model. This column can be dropped, but first the records that has “gewerblich” value should be removed.</li>
</ul>
 
<ul>
   <li>Based on histogram graph of offerType, Table 1 and column description, this column has 2 unique values. “gesuch” value has only 12 records. So, this column has no distinguishing information for the model. This column can be dropped, after removing the records that has “gesuch” value. </li>
</ul>











<ul>
   <li>Based on histogram graph of abtest and Table 1, this column has consistent values for the model. </li>
</ul>
 

<ul>
   <li>Based on histogram graph of monthOfRegistration and Table 1, this column should have 12 unique values. However, it has 13 values. Also, dataset has yearOfRegistration column. So, this column can be dropped.</li>
</ul>
 
<ul>
   <li>postalCode column has 8150 unique values. This information can be used to determine the location of the car. However, for the model, location is not a distinguishing information because all car has postal code in Germany. Car location does not affect the model. This column can be dropped.</li>
</ul>
 

<ul>
   <li>dateCreated column has 114 unique values. This column has no distinguishing information for the model. So, this column can be dropped</li>
</ul>
 
<ul>
   <li>Based on histogram of price column and its description, this column has 10772 records that has 0 value which means the car is free. Also, records have some value more than 100000 euro. It is not a consistent variable because cars can’t be that much expensive. To make dataset more consistent, prices values which are 0 and larger than 100000 can be removed. The histogram graph of price column are below. First graph shows the original distribution of the prices. Second graph shows the prices without free cars. Third graph shows the prices between 0 and 100000 euro. Other records can be removed from the dataset to have consistent values.  </li>
</ul>
 

<ul>
   <li>Based on histogram of yearsOfRegistration column and its description result, this column has inconsistent values. For example, it has year values larger than 2017. Also, there are some values smaller than 1900 which does not make sense because in that time engine did not invented. So, yersOfRegistration records can be limited between 1900- yearsOfRegistration-2017.</li>
</ul>
 
<ul>
   <li>Based on histogram of powerPS and Table 1, this column has some inconsistent values. powerPS can’t be less than 0. Also, powerPS can’t be stronger than 1000. So, it can be limited between 0-powerPS-1000. Other records can be removed from the dataset to have consistent values.</li>
</ul>

<ul>
   <li>Based on histogram of fuelType and Table 1, this column has 7 different value type. Apart from “benzin” and “diesel”, other values have very low records. So, these values do not mean much for the model. These records can be removed from the dataset.</li>
</ul>
 
<ul>
   <li>Based on vehicleType histogram and Table 1, it has 8 different values. Values are consistent and can be used for the model.</li>
</ul>
 
<ul>
   <li>Based on histogram of model and Table 1, this column has many different values. It can be useful for price prediction but to make the model simpler this column can be dropped. </li>
</ul>
 



<ul>
   <li>Based on histogram of kilometer and table 1, this column has consistent values. Also, it can be useful for the model.</li>
</ul>
 
<ul>
   <li>Based on histogram of gearbox and Table 1, this column has 2 different values and values are consistent.</li>
</ul>
                  
<ul>
   <li>Based on histogram of notRepairedDamage, this column has 2 different values. Values are consistent and can be useful for the model.</li>
</ul>
 
<ul>
   <li>Based on histogram of the brand, this column has 40 different values. It has consistent records and can be useful for the model.</li>
</ul>
 
<ul>
   <li>Based on year v.s. price graph, it can be said that new cars are more expensive than old ones. However, there some old cars which are also expensive. </li>
</ul>
 
<ul>
   <li>Based on powerPS v.s price graph, low powerPS cars are cheaper than others. </li>
</ul>




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
<tr><td>201</td><td align="right">900</td><td align="right">-1853.23</td><td align="right">-2753.23</td></tr>
<tr><td>202</td><td align="right">900</td><td align="right">-1432.77</td><td align="right">-2332.77</td></tr>
<tr><td>203</td><td align="right">14000</td><td align="right">6994.058</td><td align="right">-7005.942</td></tr>
<tr><td>204</td><td align="right">2900</td><td align="right">3790.231</td><td align="right">890.231</td></tr>
<tr><td>205</td><td align="right">1450</td><td align="right">4116.963</td><td align="right">2666.963</td></tr>
<tr><td>206</td><td align="right">15000</td><td align="right">13816.124</td><td align="right">-1183.876</td></tr>
<tr><td>207</td><td align="right">1800</td><td align="right">6513.328</td><td align="right">4713.328</td></tr>
<tr><td>208</td><td align="right">22499</td><td align="right">16801.731</td><td align="right">-5697.269</td></tr>
<tr><td>209</td><td align="right">170</td><td align="right">-1853.23</td><td align="right">-2023.23</td></tr>
<tr><td>210</td><td align="right">3300</td><td align="right">4278.547</td><td align="right">978.547</td></tr>
<tr><td>211</td><td align="right">700</td><td align="right">8377.425</td><td align="right">7677.425</td></tr>
<tr><td>212</td><td align="right">4760</td><td align="right">2611.716</td><td align="right">-2148.284</td></tr>
<tr><td>213</td><td align="right">700</td><td align="right">-2499.567</td><td align="right">-3199.567</td></tr>
<tr><td>214</td><td align="right">750</td><td align="right">-540.045</td><td align="right">-1290.045</td></tr>
<tr><td>215</td><td align="right">11000</td><td align="right">11073.305</td><td align="right">73.305</td></tr>
<tr><td>216</td><td align="right">750</td><td align="right">1287.489</td><td align="right">537.489</td></tr>
<tr><td>217</td><td align="right">1980</td><td align="right">1847.747</td><td align="right">-132.253</td></tr>
<tr><td>218</td><td align="right">5900</td><td align="right">2768.787</td><td align="right">-3131.213</td></tr>
<tr><td>219</td><td align="right">99990</td><td align="right">42935.124</td><td align="right">-57054.876</td></tr>
<tr><td>220</td><td align="right">3200</td><td align="right">5262.079</td><td align="right">2062.079</td></tr>
<tr><td>221</td><td align="right">1350</td><td align="right">4591.218</td><td align="right">3241.218</td></tr>
<tr><td>222</td><td align="right">2200</td><td align="right">4376.719</td><td align="right">2176.719</td></tr>
<tr><td>223</td><td align="right">13999</td><td align="right">8072.004</td><td align="right">-5926.996</td></tr>
<tr><td>224</td><td align="right">2450</td><td align="right">7062.373</td><td align="right">4612.373</td></tr>
<tr><td>225</td><td align="right">12490</td><td align="right">10676.551</td><td align="right">-1813.449</td></tr>
<tr><td>226</td><td align="right">55990</td><td align="right">27578.85</td><td align="right">-28411.15</td></tr>
<tr><td>227</td><td align="right">10999</td><td align="right">12740.332</td><td align="right">1741.332</td></tr>
<tr><td>228</td><td align="right">16000</td><td align="right">13846.993</td><td align="right">-2153.007</td></tr>
<tr><td>229</td><td align="right">13900</td><td align="right">14286.782</td><td align="right">386.782</td></tr>
<tr><td>230</td><td align="right">2100</td><td align="right">6132.994</td><td align="right">4032.994</td></tr>
<tr><td>231</td><td align="right">1999</td><td align="right">3793.794</td><td align="right">1794.794</td></tr>
<tr><td>232</td><td align="right">4500</td><td align="right">16145.904</td><td align="right">11645.904</td></tr>
<tr><td>233</td><td align="right">25999</td><td align="right">15196.099</td><td align="right">-10802.901</td></tr>
<tr><td>234</td><td align="right">12499</td><td align="right">9636.59</td><td align="right">-2862.41</td></tr>
<tr><td>235</td><td align="right">500</td><td align="right">-2511.506</td><td align="right">-3011.506</td></tr>
<tr><td>236</td><td align="right">4350</td><td align="right">7116.593</td><td align="right">2766.593</td></tr>
<tr><td>237</td><td align="right">10900</td><td align="right">13100.683</td><td align="right">2200.683</td></tr>
<tr><td>238</td><td align="right">3200</td><td align="right">7534.702</td><td align="right">4334.702</td></tr>
<tr><td>239</td><td align="right">525</td><td align="right">-3226.157</td><td align="right">-3751.157</td></tr>
<tr><td>240</td><td align="right">2750</td><td align="right">5462.712</td><td align="right">2712.712</td></tr>
<tr><td>241</td><td align="right">1999</td><td align="right">286.413</td><td align="right">-1712.587</td></tr>
<tr><td>242</td><td align="right">250</td><td align="right">1198.466</td><td align="right">948.466</td></tr>
<tr><td>243</td><td align="right">23000</td><td align="right">10491.588</td><td align="right">-12508.412</td></tr>
<tr><td>244</td><td align="right">970</td><td align="right">1132.306</td><td align="right">162.306</td></tr>
<tr><td>245</td><td align="right">21499</td><td align="right">15500.842</td><td align="right">-5998.158</td></tr>
<tr><td>246</td><td align="right">20000</td><td align="right">19612.66</td><td align="right">-387.34</td></tr>
<tr><td>247</td><td align="right">1000</td><td align="right">630.094</td><td align="right">-369.906</td></tr>
<tr><td>248</td><td align="right">299</td><td align="right">-1530.464</td><td align="right">-1829.464</td></tr>
<tr><td>249</td><td align="right">13750</td><td align="right">16273.015</td><td align="right">2523.015</td></tr>
<tr><td>250</td><td align="right">7000</td><td align="right">7942.649</td><td align="right">942.649</td></tr>
<tr><td>251</td><td align="right">350</td><td align="right">802.737</td><td align="right">452.737</td></tr>
<tr><td>252</td><td align="right">4999</td><td align="right">5652.354</td><td align="right">653.354</td></tr>
<tr><td>253</td><td align="right">1700</td><td align="right">4440.131</td><td align="right">2740.131</td></tr>
<tr><td>254</td><td align="right">12499</td><td align="right">15369.997</td><td align="right">2870.997</td></tr>
<tr><td>255</td><td align="right">17800</td><td align="right">16305.849</td><td align="right">-1494.151</td></tr>
<tr><td>256</td><td align="right">4800</td><td align="right">4508.445</td><td align="right">-291.555</td></tr>
<tr><td>257</td><td align="right">300</td><td align="right">809.138</td><td align="right">509.138</td></tr>
<tr><td>258</td><td align="right">6350</td><td align="right">8763.932</td><td align="right">2413.932</td></tr>
<tr><td>259</td><td align="right">1500</td><td align="right">-695.031</td><td align="right">-2195.031</td></tr>
<tr><td>260</td><td align="right">700</td><td align="right">-2772.958</td><td align="right">-3472.958</td></tr>
<tr><td>261</td><td align="right">1400</td><td align="right">-359.923</td><td align="right">-1759.923</td></tr>
<tr><td>262</td><td align="right">7590</td><td align="right">14192.435</td><td align="right">6602.435</td></tr>
<tr><td>263</td><td align="right">26975</td><td align="right">22514.998</td><td align="right">-4460.002</td></tr>
<tr><td>264</td><td align="right">1690</td><td align="right">6941.992</td><td align="right">5251.992</td></tr>
<tr><td>265</td><td align="right">3000</td><td align="right">3155.611</td><td align="right">155.611</td></tr>
<tr><td>266</td><td align="right">6550</td><td align="right">7158.677</td><td align="right">608.677</td></tr>
<tr><td>267</td><td align="right">3550</td><td align="right">5193.831</td><td align="right">1643.831</td></tr>
<tr><td>268</td><td align="right">3650</td><td align="right">5287.101</td><td align="right">1637.101</td></tr>
<tr><td>269</td><td align="right">2000</td><td align="right">1482.585</td><td align="right">-517.415</td></tr>
<tr><td>270</td><td align="right">6999</td><td align="right">8314.722</td><td align="right">1315.722</td></tr>
<tr><td>271</td><td align="right">5150</td><td align="right">6120.233</td><td align="right">970.233</td></tr>
<tr><td>272</td><td align="right">999</td><td align="right">487.047</td><td align="right">-511.953</td></tr>
<tr><td>273</td><td align="right">10000</td><td align="right">9215.033</td><td align="right">-784.967</td></tr>
<tr><td>274</td><td align="right">4550</td><td align="right">6457.24</td><td align="right">1907.24</td></tr>
<tr><td>275</td><td align="right">6500</td><td align="right">11568.13</td><td align="right">5068.13</td></tr>
<tr><td>276</td><td align="right">31200</td><td align="right">22181.632</td><td align="right">-9018.368</td></tr>
<tr><td>277</td><td align="right">5999</td><td align="right">10806.284</td><td align="right">4807.284</td></tr>
<tr><td>278</td><td align="right">490</td><td align="right">-2202.432</td><td align="right">-2692.432</td></tr>
<tr><td>279</td><td align="right">5850</td><td align="right">4831.613</td><td align="right">-1018.387</td></tr>
<tr><td>280</td><td align="right">990</td><td align="right">-1530.062</td><td align="right">-2520.062</td></tr>
<tr><td>281</td><td align="right">4950</td><td align="right">4103.124</td><td align="right">-846.876</td></tr>
<tr><td>282</td><td align="right">2250</td><td align="right">3579.947</td><td align="right">1329.947</td></tr>
<tr><td>283</td><td align="right">4850</td><td align="right">7223.957</td><td align="right">2373.957</td></tr>
<tr><td>284</td><td align="right">850</td><td align="right">-1167.844</td><td align="right">-2017.844</td></tr>
<tr><td>285</td><td align="right">10499</td><td align="right">6343.936</td><td align="right">-4155.064</td></tr>
<tr><td>286</td><td align="right">13900</td><td align="right">13160.529</td><td align="right">-739.471</td></tr>
<tr><td>287</td><td align="right">3200</td><td align="right">3313.944</td><td align="right">113.944</td></tr>
<tr><td>288</td><td align="right">1300</td><td align="right">3161.484</td><td align="right">1861.484</td></tr>
<tr><td>289</td><td align="right">1750</td><td align="right">-320.874</td><td align="right">-2070.874</td></tr>
<tr><td>290</td><td align="right">4000</td><td align="right">5127.475</td><td align="right">1127.475</td></tr>
<tr><td>291</td><td align="right">50</td><td align="right">-1095.891</td><td align="right">-1145.891</td></tr>
<tr><td>292</td><td align="right">200</td><td align="right">371.383</td><td align="right">171.383</td></tr>
<tr><td>293</td><td align="right">650</td><td align="right">-844.676</td><td align="right">-1494.676</td></tr>
<tr><td>294</td><td align="right">1500</td><td align="right">6339.607</td><td align="right">4839.607</td></tr>
<tr><td>295</td><td align="right">6850</td><td align="right">8931.991</td><td align="right">2081.991</td></tr>
<tr><td>296</td><td align="right">2900</td><td align="right">4521.265</td><td align="right">1621.265</td></tr>
<tr><td>297</td><td align="right">5500</td><td align="right">11607.179</td><td align="right">6107.179</td></tr>
<tr><td>298</td><td align="right">900</td><td align="right">7287.54</td><td align="right">6387.54</td></tr>
<tr><td>299</td><td align="right">2200</td><td align="right">3955.378</td><td align="right">1755.378</td></tr>
<tr><td>300</td><td align="right">5890</td><td align="right">9725.818</td><td align="right">3835.818</td></tr>
<tr><td>301</td><td align="right">250</td><td align="right">-2222.046</td><td align="right">-2472.046</td></tr>
<tr><td>302</td><td align="right">8790</td><td align="right">11516.948</td><td align="right">2726.948</td></tr>
<tr><td>303</td><td align="right">9800</td><td align="right">9134.295</td><td align="right">-665.705</td></tr>
<tr><td>304</td><td align="right">950</td><td align="right">1275.55</td><td align="right">325.55</td></tr>
<tr><td>305</td><td align="right">19980</td><td align="right">21341.07</td><td align="right">1361.07</td></tr>
<tr><td>306</td><td align="right">2400</td><td align="right">2228.387</td><td align="right">-171.613</td></tr>
<tr><td>307</td><td align="right">6150</td><td align="right">8770.407</td><td align="right">2620.407</td></tr>
<tr><td>308</td><td align="right">1950</td><td align="right">6780.408</td><td align="right">4830.408</td></tr>
<tr><td>309</td><td align="right">11490</td><td align="right">10905.408</td><td align="right">-584.592</td></tr>
<tr><td>310</td><td align="right">1290</td><td align="right">3955.378</td><td align="right">2665.378</td></tr>
<tr><td>311</td><td align="right">3400</td><td align="right">4373.904</td><td align="right">973.904</td></tr>
<tr><td>312</td><td align="right">1290</td><td align="right">2504.156</td><td align="right">1214.156</td></tr>
<tr><td>313</td><td align="right">1699</td><td align="right">1065.069</td><td align="right">-633.931</td></tr>
<tr><td>314</td><td align="right">17900</td><td align="right">15360.77</td><td align="right">-2539.23</td></tr>
<tr><td>315</td><td align="right">4500</td><td align="right">3914.174</td><td align="right">-585.826</td></tr>
<tr><td>316</td><td align="right">4600</td><td align="right">8906.748</td><td align="right">4306.748</td></tr>
<tr><td>317</td><td align="right">1200</td><td align="right">-3184.953</td><td align="right">-4384.953</td></tr>
<tr><td>318</td><td align="right">7500</td><td align="right">5776.775</td><td align="right">-1723.225</td></tr>
<tr><td>319</td><td align="right">2700</td><td align="right">3043.129</td><td align="right">343.129</td></tr>
<tr><td>320</td><td align="right">1299</td><td align="right">5172.905</td><td align="right">3873.905</td></tr>
<tr><td>321</td><td align="right">890</td><td align="right">-1006.26</td><td align="right">-1896.26</td></tr>
<tr><td>322</td><td align="right">599</td><td align="right">-2364.016</td><td align="right">-2963.016</td></tr>
<tr><td>323</td><td align="right">7500</td><td align="right">5585.117</td><td align="right">-1914.883</td></tr>
<tr><td>324</td><td align="right">800</td><td align="right">-3380.246</td><td align="right">-4180.246</td></tr>
<tr><td>325</td><td align="right">4490</td><td align="right">3836.075</td><td align="right">-653.925</td></tr>
<tr><td>326</td><td align="right">680</td><td align="right">-2946.482</td><td align="right">-3626.482</td></tr>
<tr><td>327</td><td align="right">2799</td><td align="right">6889.639</td><td align="right">4090.639</td></tr>
<tr><td>328</td><td align="right">20700</td><td align="right">15471.015</td><td align="right">-5228.985</td></tr>
<tr><td>329</td><td align="right">28500</td><td align="right">23201.371</td><td align="right">-5298.629</td></tr>
<tr><td>330</td><td align="right">550</td><td align="right">-1716.889</td><td align="right">-2266.889</td></tr>
<tr><td>331</td><td align="right">1000</td><td align="right">9102.938</td><td align="right">8102.938</td></tr>
<tr><td>332</td><td align="right">14950</td><td align="right">15804.318</td><td align="right">854.318</td></tr>
<tr><td>333</td><td align="right">3800</td><td align="right">1294.968</td><td align="right">-2505.032</td></tr>
<tr><td>334</td><td align="right">2999</td><td align="right">9536.046</td><td align="right">6537.046</td></tr>
<tr><td>335</td><td align="right">3000</td><td align="right">7412.454</td><td align="right">4412.454</td></tr>
<tr><td>336</td><td align="right">33900</td><td align="right">36992.026</td><td align="right">3092.026</td></tr>
<tr><td>337</td><td align="right">3500</td><td align="right">7695.496</td><td align="right">4195.496</td></tr>
<tr><td>338</td><td align="right">1499</td><td align="right">5490.577</td><td align="right">3991.577</td></tr>
<tr><td>339</td><td align="right">14700</td><td align="right">15534.36</td><td align="right">834.36</td></tr>
<tr><td>340</td><td align="right">30999</td><td align="right">29327.829</td><td align="right">-1671.171</td></tr>
<tr><td>341</td><td align="right">10900</td><td align="right">8079.081</td><td align="right">-2820.919</td></tr>
<tr><td>342</td><td align="right">18500</td><td align="right">13395.794</td><td align="right">-5104.206</td></tr>
<tr><td>343</td><td align="right">16800</td><td align="right">9833.182</td><td align="right">-6966.818</td></tr>
<tr><td>344</td><td align="right">10000</td><td align="right">12186.539</td><td align="right">2186.539</td></tr>
<tr><td>345</td><td align="right">3100</td><td align="right">945.364</td><td align="right">-2154.636</td></tr>
<tr><td>346</td><td align="right">6900</td><td align="right">12197.723</td><td align="right">5297.723</td></tr>
<tr><td>347</td><td align="right">2600</td><td align="right">2866.57</td><td align="right">266.57</td></tr>
<tr><td>348</td><td align="right">9500</td><td align="right">9632.481</td><td align="right">132.481</td></tr>
<tr><td>349</td><td align="right">6150</td><td align="right">6947.991</td><td align="right">797.991</td></tr>
<tr><td>350</td><td align="right">4300</td><td align="right">10965.061</td><td align="right">6665.061</td></tr>
<tr><td>351</td><td align="right">7990</td><td align="right">9014.202</td><td align="right">1024.202</td></tr>
<tr><td>352</td><td align="right">1790</td><td align="right">2800.214</td><td align="right">1010.214</td></tr>
<tr><td>353</td><td align="right">4850</td><td align="right">5329.186</td><td align="right">479.186</td></tr>
<tr><td>354</td><td align="right">700</td><td align="right">418.733</td><td align="right">-281.267</td></tr>
<tr><td>355</td><td align="right">7000</td><td align="right">10196.477</td><td align="right">3196.477</td></tr>
<tr><td>356</td><td align="right">600</td><td align="right">-322.923</td><td align="right">-922.923</td></tr>
<tr><td>357</td><td align="right">5000</td><td align="right">7385.541</td><td align="right">2385.541</td></tr>
<tr><td>358</td><td align="right">6200</td><td align="right">3661.475</td><td align="right">-2538.525</td></tr>
<tr><td>359</td><td align="right">5950</td><td align="right">7278.177</td><td align="right">1328.177</td></tr>
<tr><td>360</td><td align="right">9500</td><td align="right">26095.34</td><td align="right">16595.34</td></tr>
<tr><td>361</td><td align="right">8500</td><td align="right">5517</td><td align="right">-2983</td></tr>
<tr><td>362</td><td align="right">2380</td><td align="right">5448.685</td><td align="right">3068.685</td></tr>
<tr><td>363</td><td align="right">16999</td><td align="right">16389.736</td><td align="right">-609.264</td></tr>
<tr><td>364</td><td align="right">4500</td><td align="right">7547.125</td><td align="right">3047.125</td></tr>
<tr><td>365</td><td align="right">4550</td><td align="right">9068.332</td><td align="right">4518.332</td></tr>
<tr><td>366</td><td align="right">650</td><td align="right">-1764.404</td><td align="right">-2414.404</td></tr>
<tr><td>367</td><td align="right">3800</td><td align="right">10695.036</td><td align="right">6895.036</td></tr>
<tr><td>368</td><td align="right">1800</td><td align="right">5125.517</td><td align="right">3325.517</td></tr>
<tr><td>369</td><td align="right">4999</td><td align="right">4709.079</td><td align="right">-289.921</td></tr>
<tr><td>370</td><td align="right">450</td><td align="right">-805.626</td><td align="right">-1255.626</td></tr>
<tr><td>371</td><td align="right">18000</td><td align="right">15458.781</td><td align="right">-2541.219</td></tr>
<tr><td>372</td><td align="right">7000</td><td align="right">6605.807</td><td align="right">-394.193</td></tr>
<tr><td>373</td><td align="right">989</td><td align="right">1683.218</td><td align="right">694.218</td></tr>
<tr><td>374</td><td align="right">6250</td><td align="right">7601.279</td><td align="right">1351.279</td></tr>
<tr><td>375</td><td align="right">11850</td><td align="right">11987.607</td><td align="right">137.607</td></tr>
<tr><td>376</td><td align="right">24999</td><td align="right">20162.561</td><td align="right">-4836.439</td></tr>
<tr><td>377</td><td align="right">1199</td><td align="right">1630.075</td><td align="right">431.075</td></tr>
<tr><td>378</td><td align="right">6480</td><td align="right">10009.65</td><td align="right">3529.65</td></tr>
<tr><td>379</td><td align="right">3300</td><td align="right">3163.509</td><td align="right">-136.491</td></tr>
<tr><td>380</td><td align="right">3250</td><td align="right">286.413</td><td align="right">-2963.587</td></tr>
<tr><td>381</td><td align="right">4950</td><td align="right">7695.661</td><td align="right">2745.661</td></tr>
<tr><td>382</td><td align="right">1590</td><td align="right">2731.019</td><td align="right">1141.019</td></tr>
<tr><td>383</td><td align="right">11500</td><td align="right">11116.88</td><td align="right">-383.12</td></tr>
<tr><td>384</td><td align="right">1900</td><td align="right">3594.041</td><td align="right">1694.041</td></tr>
<tr><td>385</td><td align="right">25000</td><td align="right">16373.09</td><td align="right">-8626.91</td></tr>
<tr><td>386</td><td align="right">2200</td><td align="right">2752.189</td><td align="right">552.189</td></tr>
<tr><td>387</td><td align="right">850</td><td align="right">-3781.513</td><td align="right">-4631.513</td></tr>
<tr><td>388</td><td align="right">5999</td><td align="right">7829.97</td><td align="right">1830.97</td></tr>
<tr><td>389</td><td align="right">15950</td><td align="right">15271.986</td><td align="right">-678.014</td></tr>
<tr><td>390</td><td align="right">46900</td><td align="right">23687.956</td><td align="right">-23212.044</td></tr>
<tr><td>391</td><td align="right">4200</td><td align="right">6477.333</td><td align="right">2277.333</td></tr>
<tr><td>392</td><td align="right">2000</td><td align="right">210.201</td><td align="right">-1789.799</td></tr>
<tr><td>393</td><td align="right">11200</td><td align="right">16400.476</td><td align="right">5200.476</td></tr>
<tr><td>394</td><td align="right">1450</td><td align="right">-521.508</td><td align="right">-1971.508</td></tr>
<tr><td>395</td><td align="right">6700</td><td align="right">5678.584</td><td align="right">-1021.416</td></tr>
<tr><td>396</td><td align="right">49500</td><td align="right">42562.834</td><td align="right">-6937.166</td></tr>
<tr><td>397</td><td align="right">12000</td><td align="right">14125.198</td><td align="right">2125.198</td></tr>
<tr><td>398</td><td align="right">2500</td><td align="right">2235.208</td><td align="right">-264.792</td></tr>
<tr><td>399</td><td align="right">1800</td><td align="right">10869.637</td><td align="right">9069.637</td></tr>
<tr><td>400</td><td align="right">3500</td><td align="right">7896.326</td><td align="right">4396.326</td></tr>
<tr><td>401</td><td align="right">7600</td><td align="right">7964.574</td><td align="right">364.574</td></tr>
<tr><td>402</td><td align="right">1300</td><td align="right">-1018.199</td><td align="right">-2318.199</td></tr>
<tr><td>403</td><td align="right">2500</td><td align="right">4696.943</td><td align="right">2196.943</td></tr>
<tr><td>404</td><td align="right">820</td><td align="right">-385.956</td><td align="right">-1205.956</td></tr>
<tr><td>405</td><td align="right">3000</td><td align="right">5880.098</td><td align="right">2880.098</td></tr>
<tr><td>406</td><td align="right">1100</td><td align="right">-3053.845</td><td align="right">-4153.845</td></tr>
<tr><td>407</td><td align="right">3955</td><td align="right">9564.234</td><td align="right">5609.234</td></tr>
<tr><td>408</td><td align="right">250</td><td align="right">-1530.062</td><td align="right">-1780.062</td></tr>
<tr><td>409</td><td align="right">1999</td><td align="right">5989.329</td><td align="right">3990.329</td></tr>
<tr><td>410</td><td align="right">21900</td><td align="right">11428.899</td><td align="right">-10471.101</td></tr>
<tr><td>411</td><td align="right">12500</td><td align="right">14717.315</td><td align="right">2217.315</td></tr>
<tr><td>412</td><td align="right">5299</td><td align="right">4031.756</td><td align="right">-1267.244</td></tr>
<tr><td>413</td><td align="right">9000</td><td align="right">15792.909</td><td align="right">6792.909</td></tr>
<tr><td>414</td><td align="right">593</td><td align="right">28808.163</td><td align="right">28215.163</td></tr>
<tr><td>415</td><td align="right">2700</td><td align="right">2066.803</td><td align="right">-633.197</td></tr>
<tr><td>416</td><td align="right">1900</td><td align="right">8738.146</td><td align="right">6838.146</td></tr>
<tr><td>417</td><td align="right">3150</td><td align="right">1255.918</td><td align="right">-1894.082</td></tr>
<tr><td>418</td><td align="right">650</td><td align="right">2700.346</td><td align="right">2050.346</td></tr>
<tr><td>419</td><td align="right">4250</td><td align="right">2572.47</td><td align="right">-1677.53</td></tr>
<tr><td>420</td><td align="right">6299</td><td align="right">6041.682</td><td align="right">-257.318</td></tr>
<tr><td>421</td><td align="right">10200</td><td align="right">14192.463</td><td align="right">3992.463</td></tr>
<tr><td>422</td><td align="right">5100</td><td align="right">1286.412</td><td align="right">-3813.588</td></tr>
<tr><td>423</td><td align="right">2200</td><td align="right">1360.05</td><td align="right">-839.95</td></tr>
<tr><td>424</td><td align="right">1990</td><td align="right">4404.926</td><td align="right">2414.926</td></tr>
<tr><td>425</td><td align="right">15500</td><td align="right">10332.818</td><td align="right">-5167.182</td></tr>
<tr><td>426</td><td align="right">5999</td><td align="right">1941.304</td><td align="right">-4057.696</td></tr>
<tr><td>427</td><td align="right">9700</td><td align="right">11824.191</td><td align="right">2124.191</td></tr>
<tr><td>428</td><td align="right">14222</td><td align="right">15920.562</td><td align="right">1698.562</td></tr>
<tr><td>429</td><td align="right">5500</td><td align="right">4870.663</td><td align="right">-629.337</td></tr>
<tr><td>430</td><td align="right">11900</td><td align="right">11183.04</td><td align="right">-716.96</td></tr>
<tr><td>431</td><td align="right">1850</td><td align="right">6631.84</td><td align="right">4781.84</td></tr>
<tr><td>432</td><td align="right">5200</td><td align="right">3923.405</td><td align="right">-1276.595</td></tr>
<tr><td>433</td><td align="right">25990</td><td align="right">21433.113</td><td align="right">-4556.887</td></tr>
<tr><td>434</td><td align="right">1440</td><td align="right">931.385</td><td align="right">-508.615</td></tr>
<tr><td>435</td><td align="right">1250</td><td align="right">3566.931</td><td align="right">2316.931</td></tr>
<tr><td>436</td><td align="right">1200</td><td align="right">2147.476</td><td align="right">947.476</td></tr>
<tr><td>437</td><td align="right">8800</td><td align="right">7870.293</td><td align="right">-929.707</td></tr>
<tr><td>438</td><td align="right">500</td><td align="right">3054.188</td><td align="right">2554.188</td></tr>
<tr><td>439</td><td align="right">8890</td><td align="right">13047.603</td><td align="right">4157.603</td></tr>
<tr><td>440</td><td align="right">5500</td><td align="right">10332.818</td><td align="right">4832.818</td></tr>
<tr><td>441</td><td align="right">8000</td><td align="right">11203.954</td><td align="right">3203.954</td></tr>
<tr><td>442</td><td align="right">12150</td><td align="right">10091.956</td><td align="right">-2058.044</td></tr>
<tr><td>443</td><td align="right">11200</td><td align="right">15271.986</td><td align="right">4071.986</td></tr>
<tr><td>444</td><td align="right">1500</td><td align="right">124.829</td><td align="right">-1375.171</td></tr>
<tr><td>445</td><td align="right">1490</td><td align="right">3001.044</td><td align="right">1511.044</td></tr>
<tr><td>446</td><td align="right">2000</td><td align="right">602.984</td><td align="right">-1397.016</td></tr>
<tr><td>447</td><td align="right">1200</td><td align="right">-36.755</td><td align="right">-1236.755</td></tr>
<tr><td>448</td><td align="right">650</td><td align="right">-1771.9</td><td align="right">-2421.9</td></tr>
<tr><td>449</td><td align="right">1999</td><td align="right">586.513</td><td align="right">-1412.487</td></tr>
<tr><td>450</td><td align="right">3600</td><td align="right">11247.025</td><td align="right">7647.025</td></tr>
<tr><td>451</td><td align="right">800</td><td align="right">1684.296</td><td align="right">884.296</td></tr>
<tr><td>452</td><td align="right">21500</td><td align="right">18838.489</td><td align="right">-2661.511</td></tr>
<tr><td>453</td><td align="right">2000</td><td align="right">1631.152</td><td align="right">-368.848</td></tr>
<tr><td>454</td><td align="right">20490</td><td align="right">14938.238</td><td align="right">-5551.762</td></tr>
<tr><td>455</td><td align="right">5900</td><td align="right">8219.495</td><td align="right">2319.495</td></tr>
<tr><td>456</td><td align="right">2000</td><td align="right">7386.331</td><td align="right">5386.331</td></tr>
<tr><td>457</td><td align="right">5990</td><td align="right">8092.604</td><td align="right">2102.604</td></tr>
<tr><td>458</td><td align="right">600</td><td align="right">622.986</td><td align="right">22.986</td></tr>
<tr><td>459</td><td align="right">2900</td><td align="right">2369.682</td><td align="right">-530.318</td></tr>
<tr><td>460</td><td align="right">800</td><td align="right">970.722</td><td align="right">170.722</td></tr>
<tr><td>461</td><td align="right">2200</td><td align="right">2835.387</td><td align="right">635.387</td></tr>
<tr><td>462</td><td align="right">6999</td><td align="right">5652.354</td><td align="right">-1346.646</td></tr>
<tr><td>463</td><td align="right">1999</td><td align="right">2032.42</td><td align="right">33.42</td></tr>
<tr><td>464</td><td align="right">7250</td><td align="right">6013.691</td><td align="right">-1236.309</td></tr>
<tr><td>465</td><td align="right">1250</td><td align="right">4654.791</td><td align="right">3404.791</td></tr>
<tr><td>466</td><td align="right">1750</td><td align="right">268.207</td><td align="right">-1481.793</td></tr>
<tr><td>467</td><td align="right">2500</td><td align="right">1684.968</td><td align="right">-815.032</td></tr>
<tr><td>468</td><td align="right">950</td><td align="right">2678.756</td><td align="right">1728.756</td></tr>
<tr><td>469</td><td align="right">3999</td><td align="right">5652.354</td><td align="right">1653.354</td></tr>
<tr><td>470</td><td align="right">1200</td><td align="right">-1067.959</td><td align="right">-2267.959</td></tr>
<tr><td>471</td><td align="right">750</td><td align="right">-2014.815</td><td align="right">-2764.815</td></tr>
<tr><td>472</td><td align="right">14500</td><td align="right">14347.474</td><td align="right">-152.526</td></tr>
<tr><td>473</td><td align="right">12999</td><td align="right">12883.176</td><td align="right">-115.824</td></tr>
<tr><td>474</td><td align="right">9950</td><td align="right">12689.871</td><td align="right">2739.871</td></tr>
<tr><td>475</td><td align="right">17899</td><td align="right">14790.142</td><td align="right">-3108.858</td></tr>
<tr><td>476</td><td align="right">32999</td><td align="right">17946.651</td><td align="right">-15052.349</td></tr>
<tr><td>477</td><td align="right">2100</td><td align="right">3996.516</td><td align="right">1896.516</td></tr>
<tr><td>478</td><td align="right">13000</td><td align="right">11815.283</td><td align="right">-1184.717</td></tr>
<tr><td>479</td><td align="right">9950</td><td align="right">16249.474</td><td align="right">6299.474</td></tr>
<tr><td>480</td><td align="right">10550</td><td align="right">13523.824</td><td align="right">2973.824</td></tr>
<tr><td>481</td><td align="right">72500</td><td align="right">7784.587</td><td align="right">-64715.413</td></tr>
<tr><td>482</td><td align="right">4150</td><td align="right">3057.223</td><td align="right">-1092.777</td></tr>
<tr><td>483</td><td align="right">1000</td><td align="right">5827.745</td><td align="right">4827.745</td></tr>
<tr><td>484</td><td align="right">16900</td><td align="right">10131.107</td><td align="right">-6768.893</td></tr>
<tr><td>485</td><td align="right">500</td><td align="right">-1368.478</td><td align="right">-1868.478</td></tr>
<tr><td>486</td><td align="right">4500</td><td align="right">7547.125</td><td align="right">3047.125</td></tr>
<tr><td>487</td><td align="right">2200</td><td align="right">4759.246</td><td align="right">2559.246</td></tr>
<tr><td>488</td><td align="right">2700</td><td align="right">4399.937</td><td align="right">1699.937</td></tr>
<tr><td>489</td><td align="right">6400</td><td align="right">7249.99</td><td align="right">849.99</td></tr>
<tr><td>490</td><td align="right">2200</td><td align="right">2141.938</td><td align="right">-58.062</td></tr>
<tr><td>491</td><td align="right">1450</td><td align="right">542.254</td><td align="right">-907.746</td></tr>
<tr><td>492</td><td align="right">8850</td><td align="right">12927.949</td><td align="right">4077.949</td></tr>
<tr><td>493</td><td align="right">2900</td><td align="right">4858.436</td><td align="right">1958.436</td></tr>
<tr><td>494</td><td align="right">6990</td><td align="right">9658.55</td><td align="right">2668.55</td></tr>
<tr><td>495</td><td align="right">1850</td><td align="right">5125.517</td><td align="right">3275.517</td></tr>
<tr><td>496</td><td align="right">10700</td><td align="right">15191.288</td><td align="right">4491.288</td></tr>
<tr><td>497</td><td align="right">1390</td><td align="right">8759.061</td><td align="right">7369.061</td></tr>
<tr><td>498</td><td align="right">17999</td><td align="right">14536.169</td><td align="right">-3462.831</td></tr>
<tr><td>499</td><td align="right">199</td><td align="right">5177.583</td><td align="right">4978.583</td></tr>
<tr><td>500</td><td align="right">2650</td><td align="right">8556.564</td><td align="right">5906.564</td></tr>
<tr><td>501</td><td align="right">13100</td><td align="right">13492.955</td><td align="right">392.955</td></tr>
<tr><td>502</td><td align="right">5000</td><td align="right">8770.407</td><td align="right">3770.407</td></tr>
<tr><td>503</td><td align="right">10400</td><td align="right">10428.14</td><td align="right">28.14</td></tr>
<tr><td>504</td><td align="right">1750</td><td align="right">-1853.23</td><td align="right">-3603.23</td></tr>
<tr><td>505</td><td align="right">1000</td><td align="right">2493.007</td><td align="right">1493.007</td></tr>
<tr><td>506</td><td align="right">1100</td><td align="right">964.321</td><td align="right">-135.679</td></tr>
<tr><td>507</td><td align="right">2750</td><td align="right">138.923</td><td align="right">-2611.077</td></tr>
<tr><td>508</td><td align="right">12999</td><td align="right">9358.45</td><td align="right">-3640.55</td></tr>
<tr><td>509</td><td align="right">8200</td><td align="right">8007.61</td><td align="right">-192.39</td></tr>
<tr><td>510</td><td align="right">7490</td><td align="right">9338.357</td><td align="right">1848.357</td></tr>
<tr><td>511</td><td align="right">2499</td><td align="right">10333.698</td><td align="right">7834.698</td></tr>
<tr><td>512</td><td align="right">800</td><td align="right">-521.508</td><td align="right">-1321.508</td></tr>
<tr><td>513</td><td align="right">4999</td><td align="right">4554.571</td><td align="right">-444.429</td></tr>
<tr><td>514</td><td align="right">2300</td><td align="right">9766.735</td><td align="right">7466.735</td></tr>
<tr><td>515</td><td align="right">4800</td><td align="right">6339.607</td><td align="right">1539.607</td></tr>
<tr><td>516</td><td align="right">2100</td><td align="right">9728.566</td><td align="right">7628.566</td></tr>
<tr><td>517</td><td align="right">1270</td><td align="right">-1006.26</td><td align="right">-2276.26</td></tr>
<tr><td>518</td><td align="right">2950</td><td align="right">7250.87</td><td align="right">4300.87</td></tr>
<tr><td>519</td><td align="right">12190</td><td align="right">12935.498</td><td align="right">745.498</td></tr>
<tr><td>520</td><td align="right">100</td><td align="right">-1651.52</td><td align="right">-1751.52</td></tr>
<tr><td>521</td><td align="right">5600</td><td align="right">4979.984</td><td align="right">-620.016</td></tr>
<tr><td>522</td><td align="right">600</td><td align="right">-1853.23</td><td align="right">-2453.23</td></tr>
<tr><td>523</td><td align="right">1000</td><td align="right">-1771.9</td><td align="right">-2771.9</td></tr>
<tr><td>524</td><td align="right">1300</td><td align="right">12387.102</td><td align="right">11087.102</td></tr>
<tr><td>525</td><td align="right">1800</td><td align="right">13.022</td><td align="right">-1786.978</td></tr>
<tr><td>526</td><td align="right">1200</td><td align="right">-1119.144</td><td align="right">-2319.144</td></tr>
<tr><td>527</td><td align="right">39000</td><td align="right">21373.904</td><td align="right">-17626.096</td></tr>
<tr><td>528</td><td align="right">2299</td><td align="right">1657.185</td><td align="right">-641.815</td></tr>
<tr><td>529</td><td align="right">1300</td><td align="right">-1789.36</td><td align="right">-3089.36</td></tr>
<tr><td>530</td><td align="right">24800</td><td align="right">15260.801</td><td align="right">-9539.199</td></tr>
<tr><td>531</td><td align="right">2600</td><td align="right">4802.349</td><td align="right">2202.349</td></tr>
<tr><td>532</td><td align="right">2850</td><td align="right">2731.019</td><td align="right">-118.981</td></tr>
<tr><td>533</td><td align="right">750</td><td align="right">-844.676</td><td align="right">-1594.676</td></tr>
<tr><td>534</td><td align="right">2700</td><td align="right">4316.775</td><td align="right">1616.775</td></tr>
<tr><td>535</td><td align="right">2800</td><td align="right">5289.944</td><td align="right">2489.944</td></tr>
<tr><td>536</td><td align="right">4100</td><td align="right">4979.984</td><td align="right">879.984</td></tr>
<tr><td>537</td><td align="right">10990</td><td align="right">13809.614</td><td align="right">2819.614</td></tr>
<tr><td>538</td><td align="right">33500</td><td align="right">11414.041</td><td align="right">-22085.959</td></tr>
<tr><td>539</td><td align="right">9990</td><td align="right">8931.991</td><td align="right">-1058.009</td></tr>
<tr><td>540</td><td align="right">1000</td><td align="right">-844.676</td><td align="right">-1844.676</td></tr>
<tr><td>541</td><td align="right">1750</td><td align="right">5346.243</td><td align="right">3596.243</td></tr>
<tr><td>542</td><td align="right">1450</td><td align="right">3060.187</td><td align="right">1610.187</td></tr>
<tr><td>543</td><td align="right">13100</td><td align="right">2933.611</td><td align="right">-10166.389</td></tr>
<tr><td>544</td><td align="right">4750</td><td align="right">5032.247</td><td align="right">282.247</td></tr>
<tr><td>545</td><td align="right">6900</td><td align="right">12927.949</td><td align="right">6027.949</td></tr>
<tr><td>546</td><td align="right">5900</td><td align="right">8787.248</td><td align="right">2887.248</td></tr>
<tr><td>547</td><td align="right">999</td><td align="right">-1274.131</td><td align="right">-2273.131</td></tr>
<tr><td>548</td><td align="right">16850</td><td align="right">12940.239</td><td align="right">-3909.761</td></tr>
<tr><td>82755</td><td align="right">1650</td><td align="right">-359.923</td><td align="right">-2009.923</td></tr>
<tr><td>82756</td><td align="right">1900</td><td align="right">1172.433</td><td align="right">-727.567</td></tr>
<tr><td>82757</td><td align="right">7000</td><td align="right">12767.47</td><td align="right">5767.47</td></tr>
<tr><td>82758</td><td align="right">3350</td><td align="right">3962.455</td><td align="right">612.455</td></tr>
<tr><td>82759</td><td align="right">8000</td><td align="right">11712.216</td><td align="right">3712.216</td></tr>
<tr><td>82760</td><td align="right">1380</td><td align="right">1226.653</td><td align="right">-153.347</td></tr>
<tr><td>82761</td><td align="right">249</td><td align="right">-3122.16</td><td align="right">-3371.16</td></tr>
<tr><td>82762</td><td align="right">23445</td><td align="right">22191.83</td><td align="right">-1253.17</td></tr>
<tr><td>82763</td><td align="right">10800</td><td align="right">15497.831</td><td align="right">4697.831</td></tr>
</table>
</div>
</body>
