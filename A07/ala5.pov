#version 3.7;

// 1. Setup the environment
global_settings { 
    assumed_gamma 1.0 
    ambient_light rgb <0.2, 0.2, 0.2> // Add some ambient light to fill shadows
}

// Position camera back along Z-axis
camera {
  location <0, 0, -18>  
  look_at  <0, 0, 0>    
  right x*image_width/image_height
}

// Main Light (Sunlight)
light_source { 
    <20, 20, -20> 
    color rgb <1, 1, 1> 
    shadowless // Optional: removes harsh shadows that might hide atoms
}

// 2. DARK BACKGROUND (Crucial for seeing White Hydrogens/Bonds)
background { color rgb <0.2, 0.2, 0.3> } // Dark Blue-Grey

// 3. Include the molecule
#include "ala.pov"

// 4. Place 5 molecules in a Pentagon
#declare Radius = 5; 
#declare Count = 5;
#declare Index = 0;

union {
    #while (Index < Count)
        object {
            Alanine_Mol
            
            // Center the molecule locally so it rotates nicely
            // (These numbers are approximate centers for Alanine)
            translate -<2.5, 0.5, 0> 
            
            // Rotate the molecule itself so it faces 'outward' or looks interesting
            rotate <0, 90, 0> 
            
            // Move out to the pentagon ring
            translate <0, Radius, 0>
            
            // Rotate around the center (Z-axis) to form the pentagon
            rotate <0, 0, Index * (360/Count)>
        }
        #declare Index = Index + 1;
    #end
    
    // Rotate the entire pentagon slightly to see 3D depth
    rotate <20, 10, 0>
}