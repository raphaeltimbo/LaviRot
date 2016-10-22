from LAVIROT.elements import *
from LAVIROT.rotor import *
from numpy.testing import assert_almost_equal



n_ = 1
z_ = 0
le_ = 0.25
i_d_ = 0
o_d_ = 0.05
E_ = 211e9
G_ = 81.2e9
rho_ = 7810


def test_rotor_no_damping_2_shaft_elements():

    evalues = np.array([-3.8 + 68.6j, -3.8 - 68.6j, -1.8 + 30.j, -1.8 - 30.j, -0.7 + 14.4j, -0.7 - 14.4j])
    evalues2 = np.array([ 0.+68.7j,  0.-68.7j,  0.+30.1j,  0.-30.1j, -0.+14.4j, -0.-14.4j])

    Mr1 = np.array([[ 1.421,  0.   ,  0.   ,  0.049,  0.496,  0.   ,  0.   , -0.031,  0.   ,  0.   ,  0.   ,  0.   ],
                    [ 0.   ,  1.421, -0.049,  0.   ,  0.   ,  0.496,  0.031,  0.   ,  0.   ,  0.   ,  0.   ,  0.   ],
                    [ 0.   , -0.049,  0.002,  0.   ,  0.   , -0.031, -0.002,  0.   ,  0.   ,  0.   ,  0.   ,  0.   ],
                    [ 0.049,  0.   ,  0.   ,  0.002,  0.031,  0.   ,  0.   , -0.002,  0.   ,  0.   ,  0.   ,  0.   ],
                    [ 0.496,  0.   ,  0.   ,  0.031,  2.841,  0.   ,  0.   ,  0.   ,  0.496,  0.   ,  0.   , -0.031],
                    [ 0.   ,  0.496, -0.031,  0.   ,  0.   ,  2.841,  0.   ,  0.   ,  0.   ,  0.496,  0.031,  0.   ],
                    [ 0.   ,  0.031, -0.002,  0.   ,  0.   ,  0.   ,  0.005,  0.   ,  0.   , -0.031, -0.002,  0.   ],
                    [-0.031,  0.   ,  0.   , -0.002,  0.   ,  0.   ,  0.   ,  0.005,  0.031,  0.   ,  0.   , -0.002],
                    [ 0.   ,  0.   ,  0.   ,  0.   ,  0.496,  0.   ,  0.   ,  0.031,  1.421,  0.   ,  0.   , -0.049],
                    [ 0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.496, -0.031,  0.   ,  0.   ,  1.421,  0.049,  0.   ],
                    [ 0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.031, -0.002,  0.   ,  0.   ,  0.049,  0.002,  0.   ],
                    [ 0.   ,  0.   ,  0.   ,  0.   , -0.031,  0.   ,  0.   , -0.002, -0.049,  0.   ,  0.   ,  0.002]])

    tim0 = ShaftElement(0, 0.0, le_, i_d_, o_d_, E_, G_, rho_,
                        shear_effects=True,
                        rotary_inertia=True,
                        gyroscopic=True)
    tim1 = ShaftElement(1, 0.25, le_, i_d_, o_d_, E_, G_, rho_,
                        shear_effects=True,
                        rotary_inertia=True,
                        gyroscopic=True)

    shaft_elm = [tim0, tim1]
    rotor1 = Rotor(shaft_elm, [], [])
    assert_almost_equal([4, 2, 0, 5, 3, 1], rotor1.index(evalues))
    assert_almost_equal([4, 2, 0, 5, 3, 1], rotor1.index(evalues2))
    assert_almost_equal(rotor1.M(), Mr1, decimal=3)


def test_rotor_no_damping_2_shaft_elements_1_disk_2_simple_bearings():

    Mr1 = np.array([[  1.421,   0.   ,   0.   ,   0.049,   0.496,   0.   ,   0.   ,  -0.031,   0.   ,   0.   ,   0.   ,   0.   ],
                    [  0.   ,   1.421,  -0.049,   0.   ,   0.   ,   0.496,   0.031,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ],
                    [  0.   ,  -0.049,   0.002,   0.   ,   0.   ,  -0.031,  -0.002,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ],
                    [  0.049,   0.   ,   0.   ,   0.002,   0.031,   0.   ,   0.   ,  -0.002,   0.   ,   0.   ,   0.   ,   0.   ],
                    [  0.496,   0.   ,   0.   ,   0.031,  35.431,   0.   ,   0.   ,   0.   ,   0.496,   0.   ,   0.   ,  -0.031],
                    [  0.   ,   0.496,  -0.031,   0.   ,   0.   ,  35.431,   0.   ,   0.   ,   0.   ,   0.496,   0.031,   0.   ],
                    [  0.   ,   0.031,  -0.002,   0.   ,   0.   ,   0.   ,   0.183,   0.   ,   0.   ,  -0.031,  -0.002,   0.   ],
                    [ -0.031,   0.   ,   0.   ,  -0.002,   0.   ,   0.   ,   0.   ,   0.183,   0.031,   0.   ,   0.   ,  -0.002],
                    [  0.   ,   0.   ,   0.   ,   0.   ,   0.496,   0.   ,   0.   ,   0.031,   1.421,   0.   ,   0.   ,  -0.049],
                    [  0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.496,  -0.031,   0.   ,   0.   ,   1.421,   0.049,   0.   ],
                    [  0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.031,  -0.002,   0.   ,   0.   ,   0.049,   0.002,   0.   ],
                    [  0.   ,   0.   ,   0.   ,   0.   ,  -0.031,   0.   ,   0.   ,  -0.002,  -0.049,   0.   ,   0.   ,   0.002]])

    A0_0 = np.array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])

    A0_1 = np.array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.]])

    A1_0 = np.array([[  20.63 ,   -0.   ,    0.   ,    4.114,  -20.958,    0.   ,    0.   ,    1.11 ,    0.056,   -0.   ,   -0.   ,   -0.014],
                     [   0.   ,   20.63 ,   -4.114,    0.   ,   -0.   ,  -20.958,   -1.11 ,    0.   ,   -0.   ,    0.056,    0.014,    0.   ],
                     [   0.   ,  697.351, -131.328,    0.   ,   -0.   , -705.253,  -44.535,    0.   ,   -0.   ,    2.079,    0.596,    0.   ],
                     [-697.351,    0.   ,   -0.   , -131.328,  705.253,   -0.   ,   -0.   ,  -44.535,   -2.079,    0.   ,    0.   ,    0.596],
                     [   0.442,    0.   ,   -0.   ,    0.072,   -0.887,   -0.   ,   -0.   ,   -0.   ,    0.442,    0.   ,    0.   ,   -0.072],
                     [   0.   ,    0.442,   -0.072,    0.   ,   -0.   ,   -0.887,    0.   ,    0.   ,    0.   ,    0.442,    0.072,   -0.   ],
                     [   0.   ,    6.457,   -0.837,    0.   ,   -0.   ,    0.   ,   -1.561,    0.   ,   -0.   ,   -6.457,   -0.837,   -0.   ],
                     [  -6.457,   -0.   ,    0.   ,   -0.837,    0.   ,    0.   ,    0.   ,   -1.561,    6.457,    0.   ,    0.   ,   -0.837],
                     [   0.056,   -0.   ,    0.   ,    0.014,  -20.958,    0.   ,    0.   ,   -1.11 ,   20.63 ,    0.   ,    0.   ,   -4.114],
                     [   0.   ,    0.056,   -0.014,    0.   ,   -0.   ,  -20.958,    1.11 ,    0.   ,    0.   ,   20.63 ,    4.114,   -0.   ],
                     [  -0.   ,   -2.079,    0.596,   -0.   ,    0.   ,  705.253,  -44.535,   -0.   ,   -0.   , -697.351, -131.328,    0.   ],
                     [   2.079,    0.   ,   -0.   ,    0.596, -705.253,   -0.   ,    0.   ,  -44.535,  697.351,    0.   ,    0.   , -131.328]])

    A1_1 = np.array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                     [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])

    evals_sorted = np.array([-0. + 215.371j, 0. + 215.371j, -0. + 598.025j, 0. + 598.025j,
                             -0. + 3956.225j, 0. + 3956.225j, 0. + 4965.29j, -0. + 4965.29j,
                             0. + 33048.281j, -0. + 33048.281j, 0. + 33249.826j, -0. + 33249.826j,
                             -0. - 215.371j, 0. - 215.371j, -0. - 598.025j, 0. - 598.025j,
                             -0. - 3956.225j, 0. - 3956.225j, 0. - 4965.29j, -0. - 4965.29j,
                             0. - 33048.281j, -0. - 33048.281j, 0. - 33249.826j, -0. - 33249.826j])

    evects_sorted = np.array([[ -7.761e-05 +2.403e-04j,  -1.486e-17 -2.245e-03j,   1.465e-18 +2.330e-04j,   3.661e-06 -1.012e-04j],
                              [  2.608e-17 -2.444e-03j,  -5.110e-05 -9.991e-04j,  -1.072e-05 -4.068e-05j,  -1.167e-18 -2.140e-04j],
                              [  3.367e-17 +1.108e-03j,   2.317e-05 +4.530e-04j,  -4.168e-05 -1.581e-04j,  -2.554e-18 -8.320e-04j],
                              [ -3.519e-05 +1.090e-04j,   1.870e-16 -1.018e-03j,  -4.707e-18 -9.058e-04j,  -1.423e-05 +3.934e-04j],
                              [ -8.355e-05 +2.587e-04j,   3.228e-17 -2.416e-03j,   2.670e-19 +8.436e-18j,   1.282e-20 +9.436e-19j],
                              [  1.664e-17 -2.631e-03j,  -5.501e-05 -1.076e-03j,   4.022e-19 -3.432e-18j,  -4.701e-19 +1.269e-18j],
                              [  4.682e-17 +6.994e-16j,   3.601e-17 -2.012e-15j,  -4.505e-05 -1.709e-04j,  -3.328e-18 -8.992e-04j],
                              [ -2.991e-17 +2.717e-16j,   1.908e-16 -1.143e-15j,  -4.761e-18 -9.790e-04j,  -1.538e-05 +4.253e-04j],
                              [ -7.761e-05 +2.403e-04j,   7.670e-17 -2.245e-03j,  -8.824e-19 -2.330e-04j,  -3.661e-06 +1.012e-04j],
                              [  4.799e-18 -2.444e-03j,  -5.110e-05 -9.991e-04j,   1.072e-05 +4.068e-05j,   3.858e-19 +2.140e-04j],
                              [  4.814e-17 -1.108e-03j,  -2.317e-05 -4.530e-04j,  -4.168e-05 -1.581e-04j,  -3.434e-18 -8.320e-04j],
                              [  3.519e-05 -1.090e-04j,   1.698e-16 +1.018e-03j,  -4.507e-18 -9.058e-04j,  -1.423e-05 +3.934e-04j],
                              [ -5.176e-02 -1.672e-02j,   4.834e-01 -3.170e-14j,  -1.393e-01 +3.472e-16j,   6.052e-02 +2.189e-03j],
                              [  5.264e-01 -1.890e-14j,   2.152e-01 -1.100e-02j,   2.433e-02 -6.411e-03j,   1.280e-01 -1.016e-15j],
                              [ -2.387e-01 -4.557e-13j,  -9.756e-02 +4.989e-03j,   9.458e-02 -2.493e-02j,   4.975e-01 -4.494e-16j],
                              [ -2.347e-02 -7.578e-03j,   2.192e-01 -7.631e-14j,   5.417e-01 +3.186e-15j,  -2.353e-01 -8.511e-03j],
                              [ -5.572e-02 -1.799e-02j,   5.204e-01 +0.000e+00j,  -5.068e-15 +1.434e-16j,  -5.767e-16 -1.160e-16j],
                              [  5.667e-01 +0.000e+00j,   2.317e-01 -1.185e-02j,   2.058e-15 +1.798e-16j,  -7.483e-16 -1.577e-16j],
                              [ -1.523e-13 +8.313e-14j,   4.407e-13 -2.465e-14j,   1.022e-01 -2.694e-02j,   5.378e-01 +0.000e+00j],
                              [ -5.658e-14 +1.652e-14j,   2.480e-13 +1.460e-13j,   5.855e-01 +0.000e+00j,  -2.543e-01 -9.199e-03j],
                              [ -5.176e-02 -1.672e-02j,   4.834e-01 +3.039e-15j,   1.393e-01 -1.067e-16j,  -6.052e-02 -2.189e-03j],
                              [  5.264e-01 +1.730e-14j,   2.152e-01 -1.100e-02j,  -2.433e-02 +6.411e-03j,  -1.280e-01 +5.915e-16j],
                              [  2.387e-01 +3.537e-14j,   9.756e-02 -4.989e-03j,   9.458e-02 -2.493e-02j,   4.975e-01 -8.464e-15j],
                              [  2.347e-02 +7.578e-03j,  -2.192e-01 +2.158e-13j,   5.417e-01 +3.773e-15j,  -2.353e-01 -8.511e-03j]])

    evals = np.array([ 0.+33249.826j,  0.-33249.826j, -0.+33249.826j, -0.-33249.826j,
                      0.+33048.281j,  0.-33048.281j, -0.+33048.281j, -0.-33048.281j,
                      0. +4965.29j ,  0. -4965.29j , -0. +4965.29j , -0. -4965.29j ,
                      -0. +3956.225j, -0. -3956.225j,  0. +3956.225j,  0. -3956.225j,
                      -0.  +598.025j, -0.  -598.025j,  0.  +598.025j,  0.  -598.025j,
                      0.  +215.371j,  0.  -215.371j, -0.  +215.371j, -0.  -215.371j])

    evects = np.array([[  4.167e-07 +2.184e-07j,   4.167e-07 -2.184e-07j,  -4.174e-07 +2.245e-07j,  -4.174e-07 -2.245e-07j],
                       [  2.753e-18 +4.801e-07j,   2.753e-18 -4.801e-07j,  -2.779e-18 +4.765e-07j,  -2.779e-18 -4.765e-07j],
                       [  8.682e-17 +1.518e-05j,   8.682e-17 -1.518e-05j,  -8.766e-17 +1.507e-05j,  -8.766e-17 -1.507e-05j],
                       [ -1.318e-05 -6.906e-06j,  -1.318e-05 +6.906e-06j,   1.320e-05 -7.101e-06j,   1.320e-05 +7.101e-06j],
                       [  1.395e-08 +7.313e-09j,   1.395e-08 -7.313e-09j,  -1.398e-08 +7.520e-09j,  -1.398e-08 -7.520e-09j],
                       [  4.567e-20 +1.608e-08j,   4.567e-20 -1.608e-08j,  -4.599e-20 +1.596e-08j,  -4.599e-20 -1.596e-08j],
                       [  5.094e-19 -3.837e-19j,   5.094e-19 +3.837e-19j,  -5.133e-19 -3.731e-19j,  -5.133e-19 +3.731e-19j],
                       [  1.570e-19 +7.497e-19j,   1.570e-19 -7.497e-19j,  -1.529e-19 +7.470e-19j,  -1.529e-19 -7.470e-19j],
                       [  4.167e-07 +2.184e-07j,   4.167e-07 -2.184e-07j,  -4.174e-07 +2.245e-07j,  -4.174e-07 -2.245e-07j],
                       [ -1.069e-20 +4.801e-07j,  -1.069e-20 -4.801e-07j,   1.122e-20 +4.765e-07j,   1.122e-20 -4.765e-07j],
                       [  2.562e-19 -1.518e-05j,   2.562e-19 +1.518e-05j,  -2.724e-19 -1.507e-05j,  -2.724e-19 +1.507e-05j],
                       [  1.318e-05 +6.906e-06j,   1.318e-05 -6.906e-06j,  -1.320e-05 +7.101e-06j,  -1.320e-05 -7.101e-06j],
                       [ -7.260e-03 +1.385e-02j,  -7.260e-03 -1.385e-02j,  -7.466e-03 -1.388e-02j,  -7.466e-03 +1.388e-02j],
                       [ -1.596e-02 +9.178e-14j,  -1.596e-02 -9.178e-14j,  -1.584e-02 -9.268e-14j,  -1.584e-02 +9.268e-14j],
                       [ -5.048e-01 +2.895e-12j,  -5.048e-01 -2.895e-12j,  -5.011e-01 -2.924e-12j,  -5.011e-01 +2.924e-12j],
                       [  2.296e-01 -4.381e-01j,   2.296e-01 +4.381e-01j,   2.361e-01 +4.389e-01j,   2.361e-01 -4.389e-01j],
                       [ -2.432e-04 +4.640e-04j,  -2.432e-04 -4.640e-04j,  -2.500e-04 -4.648e-04j,  -2.500e-04 +4.648e-04j],
                       [ -5.346e-04 +1.526e-15j,  -5.346e-04 -1.526e-15j,  -5.307e-04 -1.541e-15j,  -5.307e-04 +1.541e-15j],
                       [  1.282e-14 +1.693e-14j,   1.282e-14 -1.693e-14j,   1.247e-14 -1.709e-14j,   1.247e-14 +1.709e-14j],
                       [ -2.488e-14 +5.148e-15j,  -2.488e-14 -5.148e-15j,  -2.479e-14 -5.040e-15j,  -2.479e-14 +5.040e-15j],
                       [ -7.260e-03 +1.385e-02j,  -7.260e-03 -1.385e-02j,  -7.466e-03 -1.388e-02j,  -7.466e-03 +1.388e-02j],
                       [ -1.596e-02 -9.137e-17j,  -1.596e-02 +9.137e-17j,  -1.584e-02 +9.410e-17j,  -1.584e-02 -9.410e-17j],
                       [  5.048e-01 +0.000e+00j,   5.048e-01 -0.000e+00j,   5.011e-01 +0.000e+00j,   5.011e-01 -0.000e+00j],
                       [ -2.296e-01 +4.381e-01j,  -2.296e-01 -4.381e-01j,  -2.361e-01 -4.389e-01j,  -2.361e-01 +4.389e-01j]])

    tim0 = ShaftElement(0, 0.0, le_, i_d_, o_d_, E_, G_, rho_,
                        shear_effects=True,
                        rotary_inertia=True,
                        gyroscopic=True)
    tim1 = ShaftElement(1, 0.25, le_, i_d_, o_d_, E_, G_, rho_,
                        shear_effects=True,
                        rotary_inertia=True,
                        gyroscopic=True)

    shaft_elm = [tim0, tim1]
    disk0 = DiskElement(1, rho_, 0.07, 0.05, 0.28)
    stf = 1e6
    bearing0 = Bearing(0, stf, stf, 0, 0)
    bearing1 = Bearing(2, stf, stf, 0, 0)

    rotor1 = Rotor(shaft_elm, [disk0], [bearing0, bearing1])
    assert_almost_equal(rotor1.M(), Mr1, decimal=3)
    assert_almost_equal(rotor1.A[:12, :12], A0_0, decimal=3)
    assert_almost_equal(rotor1.A[:12, 12:24], A0_1, decimal=3)
    assert_almost_equal(rotor1.A[12:24, :12]/1e7, A1_0, decimal=3)
    assert_almost_equal(rotor1.A[12:24, 12:24]/1e7, A1_1, decimal=3)
    #  sorted eigenvalues, eigenvectors
    rotor1_evals, rotor1_evects = rotor1.eigen()
    assert_almost_equal(rotor1_evals, evals_sorted, decimal=3)
    assert_almost_equal(rotor1_evects[:, 0:4], evects_sorted, decimal=3)
    #  not sorted
    rotor1_evals, rotor1_evects = rotor1.eigen(sorted_=False)
    assert_almost_equal(rotor1_evals, evals, decimal=3)
    assert_almost_equal(rotor1_evects[:, 0:4], evects, decimal=3)
#  TODO implement more tests using a simple rotor with 2 elements and one disk
#  TODO add test for rotor with disks and bearings

