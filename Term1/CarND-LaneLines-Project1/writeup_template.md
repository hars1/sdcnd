# **Finding Lane Lines on the Road** 


---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written reportt


[//]: # (Image References)

[image1]: ./steps_reduced/solidYellowCurve.jpg "Grayscale"
[image2]: ./steps_reduced/step_1.jpg "Grayscale"
[image3]: ./steps_reduced/step_2.jpg "Grayscale"
[image4]: ./steps_reduced/step_3.jpg "Grayscale"
[image5]: ./steps_reduced/step_4.jpg "Grayscale"
[image6]: ./steps_reduced/step_5.jpg "Grayscale"
[image7]: ./steps_reduced/step_6.jpg "Grayscale"
[image8]: ./steps_reduced/step_7.jpg "Grayscale"
[image9]: ./steps_reduced/step_8.jpg "Grayscale"

---


### 1. Pipeline description.
Lane detection pipeline consists of the following steps

* Read image              
![alt text][image1]
* Find Region of Interest              
![alt text][image2]

* Blur image             
![alt text][image3]

* Enhance lane lines            
![alt text][image4]

* Grayscale image             
![alt text][image5]

* Perform Canny edge detection        
![alt text][image6]

* Find Hough lines           
![alt text][image7]

* Smoothen and extrapolate lines           
![alt text][image8]

* Merge detected lanes with original image           
![alt text][image9] 


**The *draw_lines()* function was modified to extrapolate and detect two lanes as follows**
1. Calculate the slopes of each line of the output of hough_lines function. Partition the lines and points to left and 
    right lanes. Negative slope lines are classified as belonging to left lane  and positive slope lines are classified
     as beloinging to right lane
    
2. For each of the classified left and right lanes, average slope is calculated

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Potential shortcomings 


 
One potential shortcoming would be what would happen when the curvature of the road is high. Both the left lane and right 
lane slopes would be either positive or either negative. ... 

Another shortcoming could be, if there is a divider near the edge of the road. The divider would be 
detected as an edge by canny detection resulting in a drawing of the line in between lane line and the divider


### 3. Possible improvements 

A possible improvement would be to improve robustness to curvature of the road

Another potential improvement could be to robustness to color of lane lines, low light conditions and dividers.

Another improvement could be to improve the detection of points belonging to left and right lanes. 
