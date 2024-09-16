# model from https://www.youtube.com/watch?v=LqL5Mvq7oLc&t=1430s

# delete old model
hm_answernext yes
*deletemodel

# variables
set l 5000
set a [expr $l/2.]
set diameter 60
set meshSize [expr $l/100]
set density 0.0000000078
set pi 3.141592653589793238462643383
set volume [expr $pi*pow($diameter,2)/4.*$l]
set mass [expr $volume * $density]
set force [expr $mass * 9810]


# Basic model setup
*createentity mats cardimage=MAT1 includeid=0 name="material1"
*clearmark materials 1
*setvalue mats id=1 STATUS=1 1=210000
*setvalue mats id=1 STATUS=1 3=0.3
*setvalue mats id=1 STATUS=1 4=7.85e-09
*createentity props cardimage=PSHELL includeid=0 name="property1"
*clearmark properties 1
*setvalue props id=1 cardimage="PBEAM"
*setoption topofacecolor=11
*setoption topofacecolor=4
*setvalue props id=1 materialid={mats 1}
*setvalue props id=1 name="pbeam"
*setoption topofacecolor=4
*createentity comps includeid=0 name="myComponent"
*clearmark components 1
*setoption topofacecolor=10
*setoption topofacecolor=4
*setvalue comps id=1 propertyid={props 1}
*clearmark components 1
*clearmark components 1
*setoption topofacecolor=4
*createentity beamsectcols includeid=0 name="beamsectcol1"
*createentity beamsects includeid=0 name="beamsection1"
*clearmark beamsects 1
*setvalue beamsects id=1 name="beamSectionCircle"
*setvalue beamsects id=1 beamsect_dim1=[expr $diameter/2.]
*setoption topofacecolor=10
*setoption topofacecolor=4
*setoption topofacecolor=4
*setoption topofacecolor=10
*setoption topofacecolor=10
*setvalue props id=1 STATUS=2 3186={beamsects 1}
*createmark properties 1 "pbeam"
*syncpropertybeamsectionvalues 1
*mergehistorystate "" ""
*setvalue props id=1 STATUS=2 500=1
*setvalue props id=1 STATUS=0 36=0
*setvalue props id=1 STATUS=0 37=0
*setvalue props id=1 STATUS=0 38=0
*setvalue props id=1 STATUS=0 39=0
*mergehistorystate "" ""


#create line
*linecreatestraight 0 0 0 $l 0 0
*createmark lines 1 1
*createplane 1 1 0 0 $a 0 0
*linesplitatplane 1 1

# linemesh
*elementsizeset $meshSize
*createmark lines 1 2 3
*linemesh_preparedata1 lines 1 0 60
*linemesh_saveparameters 0 [expr int($a/$meshSize)] 0 0
*linemesh_saveparameters 1 [expr int(($l-$a)/$meshSize)] 0 0
*createvector 1 1 0 0
*linemesh_savedata_bar1 lines 1 60 0 1 0 0 0 0 0 0 1 1




# constraints
*createentity loadcols includeid=0 name="spc"
set delta 0.1
hm_createmark nodes 1 "by box" "[expr 0-$delta] [expr 0-$delta] [expr 0-$delta] [expr 0+$delta] [expr 0+$delta] [expr 0+$delta] 0 inside 0 1 0"
*loadcreateonentity_curve nodes 1 3 1 0 0 0 -999999 -999999 -999999 0 0 0 0 0
*createmark loads 0 1
*loadsupdatefixedvalue 0 0
hm_createmark nodes 1 "by box" "[expr $l-$delta] [expr 0-$delta] [expr 0-$delta] [expr $l+$delta] [expr 0+$delta] [expr 0+$delta] 0 inside 0 1 0"
*loadcreateonentity_curve nodes 1 3 1 -999999 0 0 -999999 -999999 -999999 0 0 0 0 0
*createmark loads 0 2
*loadsupdatefixedvalue 0 0

# force
*createentity loadcols includeid=0 name="Force"
hm_createmark nodes 1 "by box" "[expr $a-$delta] [expr 0-$delta] [expr 0-$delta] [expr $a+$delta] [expr 0+$delta] [expr 0+$delta] 0 inside 0 1 0"
*loadcreateonentity_curve nodes 1 1 1 -0 $force -0 0 0 $force 0 0 0 0 0

#loadstep
*createmark loadcols 1 "spc" "Force"
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "ls1" 1
*attributeupdateint loadsteps 1 4143 1 1 0 1
*attributeupdateint loadsteps 1 4709 1 1 0 1
*setvalue loadsteps id=1 STATUS=2 4059=1 4060=STATICS
*attributeupdateentity loadsteps 1 4145 1 1 0 loadcols 1
*attributeupdateentity loadsteps 1 4147 1 1 0 loadcols 2
*attributeupdateint loadsteps 1 3800 1 1 0 0
*attributeupdateint loadsteps 1 707 1 1 0 0
*attributeupdateint loadsteps 1 2396 1 1 0 0
*attributeupdateint loadsteps 1 8134 1 1 0 0
*attributeupdateint loadsteps 1 2160 1 1 0 0
*attributeupdateint loadsteps 1 10212 1 1 0 0

# control cards

*cardcreate "GLOBAL_OUTPUT_REQUEST"
*attributeupdateint cards 1 3321 1 2 0 0
*attributeupdateint cards 1 10184 1 2 0 0
*attributeupdateint cards 1 10189 1 2 0 0
*attributeupdateint cards 1 9792 1 2 0 0
*attributeupdateint cards 1 12155 1 2 0 0
*attributeupdateint cards 1 12158 1 2 0 0
*attributeupdateint cards 1 12160 1 2 0 0
*attributeupdateint cards 1 12162 1 2 0 0
*attributeupdateint cards 1 9630 1 2 0 0
*attributeupdateint cards 1 9307 1 2 0 0
*attributeupdateint cards 1 9317 1 2 0 0
*attributeupdateint cards 1 9327 1 2 0 0
*attributeupdateint cards 1 3880 1 2 0 0
*attributeupdateint cards 1 4119 1 2 0 0
*attributeupdateint cards 1 4114 1 2 0 0
*attributeupdateint cards 1 7121 1 2 0 0
*attributeupdateint cards 1 2938 1 2 0 0
*attributeupdateint cards 1 10688 1 2 0 0
*attributeupdateint cards 1 523 1 2 0 0
*attributeupdateint cards 1 2385 1 2 0 0
*attributeupdateint cards 1 4052 1 2 0 0
*attributeupdateint cards 1 3712 1 2 0 0
*attributeupdateint cards 1 3885 1 2 0 0
*attributeupdateint cards 1 274 1 2 0 0
*attributeupdateint cards 1 3057 1 2 0 0
*attributeupdateint cards 1 10833 1 2 0 0
*attributeupdateint cards 1 7113 1 2 0 0
*attributeupdateint cards 1 8500 1 2 0 0
*attributeupdateint cards 1 2419 1 2 0 0
*attributeupdateint cards 1 8493 1 2 0 0
*attributeupdateint cards 1 9709 1 2 0 0
*attributeupdateint cards 1 3809 1 2 0 0
*attributeupdateint cards 1 7125 1 2 0 0
*attributeupdateint cards 1 4877 1 2 0 0
*attributeupdateint cards 1 9337 1 2 0 0
*attributeupdateint cards 1 9347 1 2 0 0
*attributeupdateint cards 1 9357 1 2 0 0
*attributeupdateint cards 1 3325 1 2 0 0
*attributeupdateint cards 1 7093 1 2 0 0
*attributeupdateint cards 1 3333 1 2 0 0
*attributeupdateint cards 1 2423 1 2 0 0
*attributeupdateint cards 1 4047 1 2 0 0
*attributeupdateint cards 1 10701 1 2 0 0
*attributeupdateint cards 1 9275 1 2 0 0
*attributeupdateint cards 1 5463 1 2 0 0
*attributeupdateint cards 1 8949 1 2 0 0
*attributeupdateint cards 1 10504 1 2 0 0
*attributeupdateint cards 1 12336 1 2 0 0
*attributeupdateint cards 1 10440 1 2 0 0
*attributeupdateint cards 1 7329 1 2 0 0
*attributeupdateint cards 1 7333 1 2 0 0
*attributeupdateint cards 1 2427 1 2 0 1
*attributeupdateint cards 1 8153 1 2 0 0
*attributeupdateint cards 1 8150 1 2 0 0
*attributeupdateint cards 1 8144 1 2 0 0
*attributeupdateint cards 1 3642 1 2 0 0
*attributeupdateint cards 1 2431 1 2 0 0
*attributeupdateint cards 1 7337 1 2 0 0
*attributeupdateint cards 1 7117 1 2 0 0
*attributeupdateint cards 1 3891 1 2 0 0
*attributeupdateint cards 1 12346 1 2 0 0
*attributeupdateint cards 1 3329 1 2 0 0
*attributeupdateint cards 1 1921 1 0 0 1
*createstringarray 1 "        "
*attributeupdatestringarray cards 1 9609 1 2 0 1 1
*createstringarray 1 "        "
*attributeupdatestringarray cards 1 4323 1 2 0 1 1
*createstringarray 1 "        "
*attributeupdatestringarray cards 1 3342 1 2 0 1 1
*createstringarray 1 "        "
*attributeupdatestringarray cards 1 12602 1 2 0 1 1
*createstringarray 1 "        "
*attributeupdatestringarray cards 1 3343 1 2 0 1 1
*createstringarray 1 "        "
*attributeupdatestringarray cards 1 2294 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray cards 1 3437 1 0 0 analysisparameters 1 1
*createstringarray 1 "        "
*attributeupdatestringarray cards 1 11389 1 2 0 1 1
*createstringarray 1 "ALL"
*attributeupdatestringarray cards 1 2428 1 2 0 1 1