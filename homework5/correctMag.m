figure
scatter(magx,magy)
xlabel('MagX')
ylabel('MagY')
title('Unadjusted MagX vs MagY')

fit_ellipse(magx,magy)

magxm = magx - ans.X0_in
magym = magy - ans.Y0_in

cosphi = cos(ans.phi)
sinphi = sin(ans.phi)

mxr = ((magxm*cosphi)-(magym*sinphi))
myr = ((magym*coshi)+(magxm*sinphi))

mxr = mxr / (ans.long_axis/ans.short_axis)

figure
scatter(mxr,myr)
xlabel('MagX')
ylabel('MagY')
title('Adjusted MagX vs. MagY')
