# DB2
Automatic License Number Plate Recognition System 
#Team
Vijay Singh Rasaputra
Yaswanth Maruri
Rahul Ratnam Gali
Nagul Meera Vali Shaik
#Dataset
https://www.kaggle.com/datasets/elysian01/car-number-plate-detection
#Description
The License Plate detection and recognition is a 
challenging task that plays a significant role in intelligent 
transportation systems. Where it could be used as a core in 
various applications, such as security, traffic control, and 
electronic payment systems (e.g., freeway toll payment and 
parking fee payment). A variety of algorithms are 
developed for this work and each one has advantages and 
disadvantages for extracting plates in images under 
different circumstances. However, the complexity of some 
methods requires a high calculation cost and this could be 
time-consuming. In the current paper, a simple and efficient 
method is proposed to tackle the issue of license plate 
detection and character recognition. The license plate is 
detected first based on the two dimensional wavelet 
transform to extract the vertical edges of the input image. 
The high density of vertical edges is computed first to 
detect the potential areas of the license plate. Then these 
potential areas are verified by using a plate/non-plate CNN 
classifier. After the license plate is detected, the characters 
are segmented by using a simple method that is based on 
the empty distance between the characters. Finally, these 
character candidates are classified by training another CNN 
classifier. 
