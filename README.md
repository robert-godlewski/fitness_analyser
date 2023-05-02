# Overview
This is a fitness analyser to check progress on body measurements over time.

# Setup
1. install python
2. clone repository
3. go inside the repository clone: % cd fitness_analyser
4. .....create environment......
5. activate environment: % pipenv shell
6. install dependencies: % pip install

# Running the app
1. activate environment: % pipenv shell
2. run: % python fitness_analyser.py

# References
## Coding
* https://matplotlib.org/
* https://www.geeksforgeeks.org/plot-a-horizontal-line-in-matplotlib/
* https://www.sqlite.org/datatype3.html
* https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/
* https://wellsr.com/python/adapting-and-converting-sqlite-data-types-for-python/
* https://www.tutorialspoint.com/python_data_access/python_sqlite_select_data.htm

## Research of health calculations
* https://www.cnn.com/2017/08/16/health/bmi-measure-fat-questions/index.html

# Planning
## Inputed data
All of these are float unless noted
* Height in inches and feet (add in a conversion)
* Weight in pounds (add in a conversion)
* Forearm Circumference - Men need to be around 9-11" at 5'8"
* Upper Arms Circumference (Biceps and Triceps) - Men need to be around 12-14" based off of a neck measurement of 14"
* Shoulders (pinch at the shoulder blades) - men check the Shoulder-Hip ratio
* Chest (around the niples) - Men need to the same as hips
* Waist (around Bellybutton) - check the Waist-Hip Ratio and should be 1/2 of height in inches
* Hip (Around the thickest part of Glutes) - check the Waist-Hip Ratio
* Thigh Circumference (about 2" away from butt)
* Calf Circumference (around the thickest part)
* Dates measured - Date (String)
* Notes about data - String
* Boolean if it's metric or not.

## Calculated data
* m = inch/39.37
* kg = lbs/2.205
* BMI = (weight kg)/(height x height m x m)
* Shoulder-Hip Ratio - Males = 1.6 (x<1.6 = need to do more Chest/Shoulder/Back strength and burn abs, x>1.6 = need to do more ab strength)
* Waist-Hip Ratio - Males => 0.8 <= x < 0.9 and Females => 0.6 <= x <= 0.8
* Body fat percentage based off of height-waist ratio = 50% at 34" waist and 68" height
* checking if inputed data is in metric of imperial
* checking if everything is ok / ideal / warning / too big / too small
