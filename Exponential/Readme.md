The exponential function can be calculated by a series expansion:

Write a function that takes a scalar input x and provides scalar output of the exponential function. A few notes/hints:

The math module has a factorial function.
Since you cannot calculate an infinite series, you have to decide when the sum has converged enough. That is accomplished by testing the result against some preset tolerance. Set that tolerance using a keyword parameter as input.
You may not use the exp function from NumPy (or a similar pre-written exponential function) :).
Note that the exponential function is not the same as the exponentiation operation.  The former is ex while the latter is ab, where a and b are each any number.

You will submit a single file.  That file will have your exponential function.  Do not put the function inside another structure, such as a class.

Make sure you include adequate, appropriate, and complete documentation. This includes a docstring for the function as well as comment lines in the code. For an example of adequate documentation, see my routine to calculate mixing ratio (Links to an external site.). (Don't worry if you don't know what mixing ratio is; just pay attention to the documentation.)

Here's an example of the sort of input/output I'd like to see. I'm assuming you have already imported your exponential function and have named it exponential:

>>> print exponential(3.4, tol=1e-8)
>>> 29.9641000474

Note that you can decide how to use tol. If you use it to specify the number of digits after the decimal point, you'll get one kind of behavior. If you use it to specify some relative error (e.g., as a percentage), you'll get another kind of behavior. I'm leaving it up to you as to what algorithm to use. Thus, your output may be slightly different than the above sample. I'll account for that in my testing/grading.

Grading
The purpose of this assignment is for you to learn through practice.  This may mean making mistakes.  The exams and project are the main time for me to evaluate the quality of your work.  As a result, this assignment is graded based on effort.

About This Document
By Johnny Lin, March 2016.
