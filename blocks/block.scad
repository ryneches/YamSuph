$fn     = 20;
thick   = 20;
fiddle  = 0.01;
spacing = 9.0;

difference() {
    // chassis
    translate( [ -fiddle, 0, -fiddle ] ) cube([ spacing*2 + fiddle*2, 
                                                thick, 
                                                spacing*2 + fiddle*2]);
    // wells
    translate( [ spacing, -7.5, spacing ] ){
        hull() {
            sphere( 4.8 );
            translate( [0,10+d,0] ) sphere( 2 );
        }
    }
}