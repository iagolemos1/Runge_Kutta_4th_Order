"""
Created on Thu Jun 18 07:59:09 2020

@author: iago
"""


class RK4(object):

    def __init__(self, *functions):

        """
        Initializing the RK4 solver.
        functions: The Function we are interested in solving.
        """
        self.f = functions   #f receiving the function
        self.t = 0           #initializing t


    def solve(self, y, dt, n):

        """
        Solving the ODEs system.
        y: A list of starting values.
        dt: Step size.
        n: Endpoint.
        """

        t = []
        res = []
        for i in y:
            res.append([])

        while self.t <= n and dt != 0:
            t.append(self.t)
            y = self._solve(y, self.t, dt)
            for c, i in enumerate(y):
                res[c].append(i)

            self.t += dt

            if self.t + dt > n:
                dt = n - self.t

        return t, res


    def _solve(self, y, t, dt):

        functions = self.f

        k1 = []
        for f in functions:
            k1.append( f(t, *y) )

        k2 = []
        for f in functions:
            k2.append( f(t + .5*dt, *[y[i] + .5*dt*k1[i] for i in range(0, len(y))]) )

        k3 = []
        for f in functions:
            k3.append( f(t + .5*dt, *[y[i] + .5*dt*k2[i] for i in range(0, len(y))]) )

        k4 = []
        for f in functions:
            k4.append( f(t + dt, *[y[i] + dt*k3[i] for i in range(0, len(y))]) )

        return [y[i] + (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) * dt / 6.0 for i in range(0, len(y))]
