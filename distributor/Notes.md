# Notes

* y_max can be anything equal to or more than maximum value of P', but if it is more, then more values of x' aren't used so it becomes less efficient in terms of accuracy per random number produced
* Might want to compare the time efficiency of the Python native library and numpy ways of doing the techniques - numpy is *insanely* faster!
* Think about whether I want to create a fixed number of random sinusoidally distributed numbers (which has some difficulties with my implementation in the reject-accept method) or whether I want to throw a fixed number of initial random evenly distributed numbers, meaning analytic formula produces different number to reject-accept method.
* Reject-accept is less efficient in terms of processor time taken and also in terms of the number of random sinusoidally distributed numbers produced.