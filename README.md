# forest-cover-type-prediction
Use cartographic variables to classify forest categories

## Data Fields
Elevation - Elevation in meters
Aspect - Aspect in degrees azimuth <br>
Slope - Slope in degrees<br>
Horizontal_Distance_To_Hydrology - Horz Dist to nearest surface water features<br>
Vertical_Distance_To_Hydrology - Vert Dist to nearest surface water features<br>
Horizontal_Distance_To_Roadways - Horz Dist to nearest roadway<br>
Hillshade_9am (0 to 255 index) - Hillshade index at 9am, summer solstice<br>
Hillshade_Noon (0 to 255 index) - Hillshade index at noon, summer solstice<br>
Hillshade_3pm (0 to 255 index) - Hillshade index at 3pm, summer solstice<br>
Horizontal_Distance_To_Fire_Points - Horz Dist to nearest wildfire ignition points<br>
Wilderness_Area (4 binary columns, 0 = absence or 1 = presence) - Wilderness area designation<br>
Soil_Type (40 binary columns, 0 = absence or 1 = presence) - Soil Type designation<br>
Cover_Type (7 types, integers 1 to 7) - Forest Cover Type designation<br>
<br>

## The wilderness areas are:

1 - Rawah Wilderness Area<br>
2 - Neota Wilderness Area<br>
3 - Comanche Peak Wilderness Area<br>
4 - Cache la Poudre Wilderness Area<br>

## The soil types are:

1 Cathedral family - Rock outcrop complex, extremely stony.<br>
2 Vanet - Ratake families complex, very stony.<br>
3 Haploborolis - Rock outcrop complex, rubbly.<br>
4 Ratake family - Rock outcrop complex, rubbly.<br>
5 Vanet family - Rock outcrop complex complex, rubbly.<br>
6 Vanet - Wetmore families - Rock outcrop complex, stony.<br>
7 Gothic family.<br>
8 Supervisor - Limber families complex.<br>
9 Troutville family, very stony.<br>
10 Bullwark - Catamount families - Rock outcrop complex, rubbly.<br>
11 Bullwark - Catamount families - Rock land complex, rubbly.<br>
12 Legault family - Rock land complex, stony.<br>
13 Catamount family - Rock land - Bullwark family complex, rubbly.<br>
14 Pachic Argiborolis - Aquolis complex.<br>
15 unspecified in the USFS Soil and ELU Survey.<br>
16 Cryaquolis - Cryoborolis complex.<br>
17 Gateview family - Cryaquolis complex.<br>
18 Rogert family, very stony.<br>
19 Typic Cryaquolis - Borohemists complex.<br>
20 Typic Cryaquepts - Typic Cryaquolls complex.<br>
21 Typic Cryaquolls - Leighcan family, till substratum complex.<br>
22 Leighcan family, till substratum, extremely bouldery.<br>
23 Leighcan family, till substratum - Typic Cryaquolls complex.<br>
24 Leighcan family, extremely stony.<br>
25 Leighcan family, warm, extremely stony.<br>
26 Granile - Catamount families complex, very stony.<br>
27 Leighcan family, warm - Rock outcrop complex, extremely stony.<br>
28 Leighcan family - Rock outcrop complex, extremely stony.<br>
29 Como - Legault families complex, extremely stony.<br>
30 Como family - Rock land - Legault family complex, extremely stony.<br>
31 Leighcan - Catamount families complex, extremely stony.<br>
32 Catamount family - Rock outcrop - Leighcan family complex, extremely stony.<br>
33 Leighcan - Catamount families - Rock outcrop complex, extremely stony.<br>
34 Cryorthents - Rock land complex, extremely stony.<br>
35 Cryumbrepts - Rock outcrop - Cryaquepts complex.<br>
36 Bross family - Rock land - Cryumbrepts complex, extremely stony.<br>
37 Rock outcrop - Cryumbrepts - Cryorthents complex, extremely stony.<br>
38 Leighcan - Moran families - Cryaquolls complex, extremely stony.<br>
39 Moran family - Cryorthents - Leighcan family complex, extremely stony.<br>
40 Moran family - Cryorthents - Rock land complex, extremely stony.<br>


## Target Variable
1 - Spruce/Fir <br>
2 - Lodgepole Pine<br>
3 - Ponderosa Pine<br>
4 - Cottonwood/Willow<br>
5 - Aspen<br>
6 - Douglas-fir<br>
7 - Krummholz<br>