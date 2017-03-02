% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 4324.772876631287500 ; 4341.639922913979700 ];

%-- Principal point:
cc = [ 2614.638576820419100 ; 1439.800349203793800 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ 0.184115753717683 ; -0.457285683244851 ; -0.004018058329371 ; -0.002917604092806 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 7.418078555605079 ; 7.465461204202621 ];

%-- Principal point uncertainty:
cc_error = [ 10.358047533081400 ; 10.115473435218689 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.008458664030403 ; 0.028408086488884 ; 0.000954990335448 ; 0.000931444232992 ; 0.000000000000000 ];

%-- Image size:
nx = 5312;
ny = 2988;


%-- Various other variables (may be ignored if you do not use the Matlab Calibration Toolbox):
%-- Those variables are used to control which intrinsic parameters should be optimized

n_ima = 12;						% Number of calibration images
est_fc = [ 1 ; 1 ];					% Estimation indicator of the two focal variables
est_aspect_ratio = 1;				% Estimation indicator of the aspect ratio fc(2)/fc(1)
center_optim = 1;					% Estimation indicator of the principal point
est_alpha = 0;						% Estimation indicator of the skew coefficient
est_dist = [ 1 ; 1 ; 1 ; 1 ; 0 ];	% Estimation indicator of the distortion coefficients


%-- Extrinsic parameters:
%-- The rotation (omc_kk) and the translation (Tc_kk) vectors for every calibration image and their uncertainties

%-- Image #1:
omc_1 = [ -2.210068e+00 ; -2.197058e+00 ; 1.365703e-01 ];
Tc_1  = [ -1.183194e+02 ; -9.027070e+01 ; 3.611604e+02 ];
omc_error_1 = [ 2.215930e-03 ; 2.204148e-03 ; 4.801129e-03 ];
Tc_error_1  = [ 8.688622e-01 ; 8.482780e-01 ; 7.807740e-01 ];

%-- Image #2:
omc_2 = [ 1.832771e+00 ; 1.924790e+00 ; -4.750934e-02 ];
Tc_2  = [ -1.398936e+02 ; -9.973963e+01 ; 3.469729e+02 ];
omc_error_2 = [ 1.868015e-03 ; 2.221570e-03 ; 3.716973e-03 ];
Tc_error_2  = [ 8.431347e-01 ; 8.260451e-01 ; 8.114633e-01 ];

%-- Image #3:
omc_3 = [ -2.069225e+00 ; -2.054477e+00 ; -6.483665e-01 ];
Tc_3  = [ -1.480318e+02 ; -7.857276e+01 ; 3.339776e+02 ];
omc_error_3 = [ 2.126722e-03 ; 2.416482e-03 ; 4.491006e-03 ];
Tc_error_3  = [ 8.221140e-01 ; 8.196713e-01 ; 8.987221e-01 ];

%-- Image #4:
omc_4 = [ 1.271894e+00 ; 1.586413e+00 ; 1.104882e-01 ];
Tc_4  = [ -6.515883e+01 ; -1.227243e+02 ; 3.901211e+02 ];
omc_error_4 = [ 2.067368e-03 ; 2.219580e-03 ; 2.618185e-03 ];
Tc_error_4  = [ 9.360637e-01 ; 9.043264e-01 ; 8.378959e-01 ];

%-- Image #5:
omc_5 = [ -1.794659e+00 ; -1.782669e+00 ; -4.031693e-01 ];
Tc_5  = [ -1.537644e+02 ; -8.861926e+01 ; 3.890430e+02 ];
omc_error_5 = [ 2.021723e-03 ; 2.287687e-03 ; 3.655974e-03 ];
Tc_error_5  = [ 9.351516e-01 ; 9.308514e-01 ; 9.112277e-01 ];

%-- Image #6:
omc_6 = [ 1.776942e+00 ; 1.910037e+00 ; 9.989877e-02 ];
Tc_6  = [ -1.206306e+02 ; -9.959204e+01 ; 3.487662e+02 ];
omc_error_6 = [ 1.999416e-03 ; 2.137641e-03 ; 3.644666e-03 ];
Tc_error_6  = [ 8.482253e-01 ; 8.237121e-01 ; 7.963485e-01 ];

%-- Image #7:
omc_7 = [ -2.076735e+00 ; -1.948024e+00 ; 1.117345e+00 ];
Tc_7  = [ -8.225307e+01 ; -5.260930e+01 ; 4.678293e+02 ];
omc_error_7 = [ 2.558802e-03 ; 1.564750e-03 ; 3.778106e-03 ];
Tc_error_7  = [ 1.109897e+00 ; 1.078634e+00 ; 6.903104e-01 ];

%-- Image #8:
omc_8 = [ 1.696370e+00 ; 1.763612e+00 ; -8.032732e-01 ];
Tc_8  = [ -1.201277e+02 ; -8.439467e+01 ; 4.122263e+02 ];
omc_error_8 = [ 1.714247e-03 ; 2.299201e-03 ; 3.110466e-03 ];
Tc_error_8  = [ 9.796009e-01 ; 9.644784e-01 ; 7.085917e-01 ];

%-- Image #9:
omc_9 = [ 1.587767e+00 ; 1.677251e+00 ; -8.693489e-01 ];
Tc_9  = [ -1.177320e+02 ; -7.186948e+01 ; 3.987783e+02 ];
omc_error_9 = [ 1.748123e-03 ; 2.286965e-03 ; 2.890129e-03 ];
Tc_error_9  = [ 9.475310e-01 ; 9.332334e-01 ; 6.584983e-01 ];

%-- Image #10:
omc_10 = [ -1.918438e+00 ; -2.087796e+00 ; 1.299172e+00 ];
Tc_10  = [ -6.080454e+01 ; -7.246463e+01 ; 4.852217e+02 ];
omc_error_10 = [ 2.743291e-03 ; 1.562245e-03 ; 3.750176e-03 ];
Tc_error_10  = [ 1.159372e+00 ; 1.122658e+00 ; 6.964303e-01 ];

%-- Image #11:
omc_11 = [ -1.720517e+00 ; -1.833723e+00 ; 7.438748e-02 ];
Tc_11  = [ -1.091722e+02 ; -1.033855e+02 ; 3.962230e+02 ];
omc_error_11 = [ 1.915530e-03 ; 2.190365e-03 ; 3.436002e-03 ];
Tc_error_11  = [ 9.450431e-01 ; 9.237853e-01 ; 7.962388e-01 ];

%-- Image #12:
omc_12 = [ -1.957667e+00 ; -1.998509e+00 ; 6.199987e-01 ];
Tc_12  = [ -1.150012e+02 ; -9.385622e+01 ; 4.457018e+02 ];
omc_error_12 = [ 2.247693e-03 ; 1.876982e-03 ; 3.867638e-03 ];
Tc_error_12  = [ 1.054238e+00 ; 1.033528e+00 ; 7.899173e-01 ];

