% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 1298.797001897711200 ; 1289.844444097714800 ];

%-- Principal point:
cc = [ 454.765965894902880 ; 786.556404993593450 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ 0.177898314953551 ; -0.397779628862520 ; -0.003900899253780 ; 0.000899304007875 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 3.966354600100879 ; 4.115505926896454 ];

%-- Principal point uncertainty:
cc_error = [ 4.745871738004235 ; 5.603074747464790 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.016163539623272 ; 0.086171334579728 ; 0.002105545662616 ; 0.001652522308594 ; 0.000000000000000 ];

%-- Image size:
nx = 899;
ny = 1599;


%-- Various other variables (may be ignored if you do not use the Matlab Calibration Toolbox):
%-- Those variables are used to control which intrinsic parameters should be optimized

n_ima = 16;						% Number of calibration images
est_fc = [ 1 ; 1 ];					% Estimation indicator of the two focal variables
est_aspect_ratio = 1;				% Estimation indicator of the aspect ratio fc(2)/fc(1)
center_optim = 1;					% Estimation indicator of the principal point
est_alpha = 0;						% Estimation indicator of the skew coefficient
est_dist = [ 1 ; 1 ; 1 ; 1 ; 0 ];	% Estimation indicator of the distortion coefficients


%-- Extrinsic parameters:
%-- The rotation (omc_kk) and the translation (Tc_kk) vectors for every calibration image and their uncertainties

%-- Image #1:
omc_1 = [ 2.195936e+00 ; 2.176317e+00 ; 1.319162e-02 ];
Tc_1  = [ -1.011182e+02 ; -1.316452e+02 ; 3.614629e+02 ];
omc_error_1 = [ 3.181516e-03 ; 3.154686e-03 ; 6.752904e-03 ];
Tc_error_1  = [ 1.350809e+00 ; 1.596476e+00 ; 1.362530e+00 ];

%-- Image #2:
omc_2 = [ 2.157167e+00 ; 2.166527e+00 ; 6.173261e-01 ];
Tc_2  = [ -6.302319e+01 ; -1.011283e+02 ; 3.211588e+02 ];
omc_error_2 = [ 3.974513e-03 ; 3.147348e-03 ; 7.524128e-03 ];
Tc_error_2  = [ 1.207784e+00 ; 1.427992e+00 ; 1.246372e+00 ];

%-- Image #3:
omc_3 = [ -1.956833e+00 ; -2.132077e+00 ; -1.089721e+00 ];
Tc_3  = [ -4.943875e+01 ; -8.522172e+01 ; 3.051770e+02 ];
omc_error_3 = [ 2.588256e-03 ; 4.779853e-03 ; 6.376052e-03 ];
Tc_error_3  = [ 1.136655e+00 ; 1.354396e+00 ; 1.239987e+00 ];

%-- Image #4:
omc_4 = [ -2.030556e+00 ; -1.960675e+00 ; -8.389922e-01 ];
Tc_4  = [ -6.971710e+01 ; -8.374785e+01 ; 3.294602e+02 ];
omc_error_4 = [ 3.165679e-03 ; 4.255049e-03 ; 6.496775e-03 ];
Tc_error_4  = [ 1.224037e+00 ; 1.466127e+00 ; 1.274326e+00 ];

%-- Image #5:
omc_5 = [ -1.857303e+00 ; -1.909679e+00 ; -1.032297e+00 ];
Tc_5  = [ -6.714965e+01 ; -5.284578e+01 ; 3.141076e+02 ];
omc_error_5 = [ 3.025261e-03 ; 4.446368e-03 ; 5.804425e-03 ];
Tc_error_5  = [ 1.155704e+00 ; 1.389334e+00 ; 1.234472e+00 ];

%-- Image #6:
omc_6 = [ 1.966797e+00 ; 1.991795e+00 ; 4.001563e-01 ];
Tc_6  = [ -5.284822e+01 ; -1.090676e+02 ; 3.406101e+02 ];
omc_error_6 = [ 3.908696e-03 ; 3.020172e-03 ; 6.584025e-03 ];
Tc_error_6  = [ 1.275998e+00 ; 1.491399e+00 ; 1.291199e+00 ];

%-- Image #7:
omc_7 = [ 1.859268e+00 ; 1.836565e+00 ; 6.640377e-01 ];
Tc_7  = [ -5.016913e+01 ; -1.185268e+02 ; 3.324423e+02 ];
omc_error_7 = [ 3.939399e-03 ; 2.800582e-03 ; 5.890202e-03 ];
Tc_error_7  = [ 1.252541e+00 ; 1.455372e+00 ; 1.321218e+00 ];

%-- Image #8:
omc_8 = [ 1.805138e+00 ; 1.762511e+00 ; 7.455645e-01 ];
Tc_8  = [ -3.070837e+01 ; -1.086997e+02 ; 2.909898e+02 ];
omc_error_8 = [ 4.037932e-03 ; 2.661121e-03 ; 5.472775e-03 ];
Tc_error_8  = [ 1.092168e+00 ; 1.268578e+00 ; 1.170660e+00 ];

%-- Image #9:
omc_9 = [ 1.742820e+00 ; 1.717086e+00 ; 7.864386e-01 ];
Tc_9  = [ -2.689185e+01 ; -1.024833e+02 ; 2.780513e+02 ];
omc_error_9 = [ 4.072559e-03 ; 2.654711e-03 ; 5.250205e-03 ];
Tc_error_9  = [ 1.040299e+00 ; 1.212433e+00 ; 1.111197e+00 ];

%-- Image #10:
omc_10 = [ 1.928244e+00 ; 1.769421e+00 ; 7.194713e-02 ];
Tc_10  = [ -7.379219e+01 ; -1.048881e+02 ; 4.326342e+02 ];
omc_error_10 = [ 4.047311e-03 ; 3.263586e-03 ; 6.156499e-03 ];
Tc_error_10  = [ 1.602323e+00 ; 1.884637e+00 ; 1.466020e+00 ];

%-- Image #11:
omc_11 = [ 1.912423e+00 ; 1.612643e+00 ; -9.074264e-02 ];
Tc_11  = [ -8.581371e+01 ; -1.079926e+02 ; 3.994037e+02 ];
omc_error_11 = [ 3.823854e-03 ; 3.234726e-03 ; 5.318125e-03 ];
Tc_error_11  = [ 1.479428e+00 ; 1.745509e+00 ; 1.301344e+00 ];

%-- Image #12:
omc_12 = [ 2.011778e+00 ; 1.996364e+00 ; -1.828147e-01 ];
Tc_12  = [ -7.127840e+01 ; -1.202531e+02 ; 4.124724e+02 ];
omc_error_12 = [ 3.728504e-03 ; 3.860088e-03 ; 7.045776e-03 ];
Tc_error_12  = [ 1.524607e+00 ; 1.799605e+00 ; 1.385265e+00 ];

%-- Image #13:
omc_13 = [ 1.916793e+00 ; 1.889048e+00 ; -4.516499e-01 ];
Tc_13  = [ -7.263802e+01 ; -1.090785e+02 ; 4.518875e+02 ];
omc_error_13 = [ 3.426673e-03 ; 3.965983e-03 ; 6.045283e-03 ];
Tc_error_13  = [ 1.658661e+00 ; 1.970771e+00 ; 1.350669e+00 ];

%-- Image #14:
omc_14 = [ 1.845021e+00 ; 1.775397e+00 ; -6.488351e-01 ];
Tc_14  = [ -7.831458e+01 ; -9.492930e+01 ; 4.710884e+02 ];
omc_error_14 = [ 3.267473e-03 ; 4.060422e-03 ; 5.458966e-03 ];
Tc_error_14  = [ 1.724010e+00 ; 2.056763e+00 ; 1.312177e+00 ];

%-- Image #15:
omc_15 = [ 2.064063e+00 ; 2.021704e+00 ; -1.010471e+00 ];
Tc_15  = [ -7.099707e+01 ; -7.411598e+01 ; 4.652227e+02 ];
omc_error_15 = [ 2.587095e-03 ; 4.780955e-03 ; 6.302391e-03 ];
Tc_error_15  = [ 1.693129e+00 ; 2.034454e+00 ; 1.222975e+00 ];

%-- Image #16:
omc_16 = [ -2.044796e+00 ; -1.936119e+00 ; 9.599340e-01 ];
Tc_16  = [ -7.752910e+01 ; -8.309087e+01 ; 4.571404e+02 ];
omc_error_16 = [ 4.334546e-03 ; 2.627714e-03 ; 6.428033e-03 ];
Tc_error_16  = [ 1.668916e+00 ; 2.002614e+00 ; 1.242982e+00 ];

