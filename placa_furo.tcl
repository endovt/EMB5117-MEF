hm_answernext yes
*deletemodel 

# default for testing (no input needed)
*createentity comps includeid=0 name="component1"
*createentity comps includeid=0 name="component2"
*createentity comps includeid=0 name="component3"
*clearmark components 1
# set input_Yng 210000
# set input_nu 0.3
# set input_t 2.0
# set input_rho 7.8e-9

# user input 
set input_Yng [hm_getfloat "Please enter a vlaue for Young's Module in MPa"]
set input_nu [hm_getfloat "Please enter a vlaue for poisson's ratio"]
set input_rho [hm_getfloat "Please enter a vlaue for the material density in mm"]
set input_t [hm_getfloat "Please enter a vlaue for thickness in mm"]

# esta seria uma solução mais elegante...
# hwtk::inputdialog -title "Input Dialog"


# Main Script Part
set prop_name "Property_for_all_Components"
set mat_name "Material_for_all_Components"
*createentity mats cardimage=MAT1 includeid=0 name=$mat_name
*createmark materials 1 "by name" $mat_name
*setvalue mats id=[hm_getmark materials 1] STATUS=1 1=$input_Yng
*setvalue mats id=[hm_getmark materials 1] STATUS=1 3=$input_nu
*setvalue mats id=[hm_getmark materials 1] STATUS=1 4=$input_rho
*clearmark materials 1
*createentity props cardimage=PSHELL includeid=0 name=$prop_name
*createmark prop 1 "by name" $prop_name
*setvalue props id=[hm_getmark prop 1] STATUS=1 95=$input_t
*clearmark prop 1
*setoption topofacecolor=11
*setoption topofacecolor=11
*setoption topofacecolor=4
*setoption topofacecolor=4
*createmark materials 1 "by name" $mat_name
*createmark prop 2 "by name" $prop_name
*setvalue props id=[hm_getmark prop 2] materialid=[hm_getmark materials 1]
*clearmark materials 1
*createmark comps 1 "all"
*setvalue comps mark=1 propertyid=[hm_getmark prop 2]
*clearmark prop 2
*clearmark comps 1