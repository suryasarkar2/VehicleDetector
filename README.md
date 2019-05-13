# VehicleDetector
Basic Version of Vehicle Detector that uses centroid estimation to detect a vehicle.
Language: Python 3.6
OS:Windows 10 64-bit
Library Used:OpenCV

Explanation:

Firstly we create a foreground mask by isolating moving cars from static background.
We then use the moments method to compute the centroid of the moving object and when it falls in given range of co-ordinates of road,the vehicle counter is raised.

This algorithm is much different and simpler than the blob detection approach of Vehicle Counter.

Application:
Can be used in traffic control systems.
Can be used to estimate the vehicle density in a given area.
