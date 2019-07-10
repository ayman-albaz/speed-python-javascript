# Exploring the computational speed between python, cython and javascript
## Method
Finding all prime numbers between 2 and 1000. Repeat for 100 times while finding the time of each run. Cythonize is bascially cythonizing a regular .py script without editing any of the codes to C or 'Cython notation'.

## Results
| Language | Mean speed | Standard deviation |
| --- | --- | --- |
| Python   | 46.93 ms   | 3.21 ms            |
| Cythonize| 19.22 ms   | 1.68 ms            |
| Cython   | 1.73 ms    | 0.44 ms            |
| Javascript | 5.4 ms     | 0.94 ms            |

We can see that while regular python is much slower than regular Javascript, we can achieve speeds faster than javascript by using Cython.
