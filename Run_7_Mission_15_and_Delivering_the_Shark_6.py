# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":0,"y":0,"deletable":false,"next":{"block":{"type":"variables_set_motor","id":"Kio)AFDu.EK,#;4tpiVW","fields":{"VAR":{"id":"1Rb_{x}94W+Y?74tRc6U"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"4LzmZPI%+xv,T4|@Ig}9","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"6i.?cxcufL}mrs8dk$4M","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"Lk3Vz*-t][o82:a+8{yU","fields":{"VAR":{"id":"Y.3O{:6f|={+?vh!6ij+"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"1`OX[NxZgj_o[gM(JB3V","fields":{"NAME":"B"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"qiug@^-WPk/hlK1((tSu","fields":{"SELECTION":"Direction.COUNTERCLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"TmRGx^]yUn,?7sa?2gdc","fields":{"VAR":{"id":"?,ejNG]:eZ!1i|U{P![6"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"=7xPNN?@xQjRR0r=KyL}","fields":{"NAME":"E"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"m(`D_nEtfC)sxp;DdYUA","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_drive_base","id":"F9rQmu!@]3DWD35khk;4","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;"}},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":",M1yS+yPgH^?,?#Pq`%q","fields":{"VAR":{"id":"Y.3O{:6f|={+?vh!6ij+","name":"left","type":"Motor"}}}},"VAR2":{"shadow":{"type":"variables_get_motor_device","id":"]8nD]V7JZ5USns-[kLF0","fields":{"VAR":{"id":"1Rb_{x}94W+Y?74tRc6U","name":"right","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_distance","id":"q^9j,wV|7qI}cEjUv3HH","fields":{"VALUE0":81.6}}},"VALUE1":{"shadow":{"type":"unit_distance","id":"~E[|UZTuzplEv_:CLf:N","fields":{"VALUE0":114}}}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":0,"y":300,"deletable":false,"next":{"block":{"type":"blockPrint","id":"j,,T}?rBkaW$1v?olp4p","extraState":{"optionLevel":0},"inputs":{"TEXT0":{"shadow":{"type":"text","id":"!x5.0YiWya^`(y)yO5B8","fields":{"TEXT":"Hello, Pybricks!"}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"@==5)gQg2sMpYM#vg6Mg","extraState":{"optionLevel":1},"fields":{"METHOD":"DRIVEBASE_STRAIGHT_SPEED"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"w~K+hXifn:;cei(68Zj+","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_speed","id":"v9NDs*|(sEiM=~8_8G:3","fields":{"VALUE0":300}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":",xm~4z3EyeB@*wBS~Mm@","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"3KRH0/fsLK?cb0:;;[~1","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"~qM^u9rDj7o`GW3xdj.Q","fields":{"VALUE0":730}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"Vs9w(71AVdb!Xb8__JeT","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"kxAZqA1galG:X#M21Uw?","extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_DRIVE_TURN"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"%;0~LFTTU27qGF94ctG6","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angle","id":"|91Z=}X:l%E+dYYsYRzN","fields":{"VALUE0":-20}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"f`jRd/rY!x]:#m|-khy6","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"$DXJs.Df[Ts8xqL2i[Ae","extraState":{"optionLevel":1},"fields":{"METHOD":"DRIVEBASE_STRAIGHT_SPEED"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"1N8Z@H?Dd7*Qd(]T*qe*","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_speed","id":":s981DMvgtC5ca,a.e9N","fields":{"VALUE0":1000}}}},"next":{"block":{"type":"blockMotorRun","id":";kdn/4WPI*V]]gcQs)O-","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"i#$oo.Ty$:_)l-s^ycle","fields":{"VAR":{"id":"?,ejNG]:eZ!1i|U{P![6","name":"front","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"N;_H=M{8Y44SN$b=NBWQ","fields":{"VALUE0":999}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"@1NQP1[lssXfWkNI(4A,","fields":{"VALUE0":100}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"F7kS2E3JfZ^Wc%X:I:*a","fields":{"VALUE":"Stop.NONE"}}}},"next":{"block":{"type":"blockMotorRun","id":"2Z%O}E8:G(xNGXojUW9O","extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"`)ML#w~,Lwn*4PQz#i7(","fields":{"VAR":{"id":"?,ejNG]:eZ!1i|U{P![6","name":"front","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"8_[(~nrp#Spmi!_Yj+az","fields":{"VALUE0":500}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"M$)OUTI|{@Vz9e[12:Rb","fields":{"VALUE0":-80}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"j%Or}GG`^#m3!z{Puou(","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseConfigure","id":"fyS.$P7~9p@V]g:WTjwX","extraState":{"optionLevel":1},"fields":{"METHOD":"DRIVEBASE_STRAIGHT_SPEED"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"v*Yl:k]k!!#LsMWqC1F9","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_speed","id":"X=p`k*6H.?H9x-$By*w(","fields":{"VALUE0":300}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"]aPi}RQ9$MTXtz4m9y|G","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"*y4Z9F#^a`R`5`WHP}?R","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"583}TyA-[|Hp3)o453]D","fields":{"VALUE0":100}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"JfV}]wSJawa3QBN.dLZs","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"W[;yU{d=?i3Zo8@RJBsX","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"c);WO]Qco1`zAJ!3[14u","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"Z/+i#XYSGG[(d)};2z=|","fields":{"VALUE0":-100}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"G4Ym[Bg44C496nq*YrE9","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"/Pu}1KNo[i58ZzuX%*k9","extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_DRIVE_CURVE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"$jf+OsBl378G_*QYXDlN","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"zryq3S40q]!Vfi0R.})m","fields":{"VALUE0":-58}}},"ARG1":{"shadow":{"type":"unit_angle","id":"VKp}:Yog;Nf.:qyKO!f6","fields":{"VALUE0":182}}},"ARG2":{"shadow":{"type":"parameters_stop_4","id":"z1UIQWw)ww0N5Hemsrie","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"l=91wvvejh?x03}d6#0i","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"tSOCD7v*B?$8MIR1=}Dr","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"70:z;FQH/hM##Y/a:((1","fields":{"VALUE0":-400}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"qcxx;[E=3=tIWXu$2(}.","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"v~;%OGBV/fu}%A!{/q%k","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"uSUk9f3b]P6rmmPSTk%`","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"GMXA0{z1%%dEw%,t3%3V","fields":{"VALUE0":75}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"9eMf8qtTGjN6:yTo79})","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"PY.ykPc#xYk}fq=c|!v[","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"s[-E-Oxan#I@:6utz4q6","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"pC@kV.*]/Wicl%pDRH;S","fields":{"VALUE0":-80}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"r_gF.0nIqGV=.W)kCv=G","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockComment","id":";rfDN`6q%SaKi;q!7K5m","fields":{"FIELDNAME":"Code for return home after pushing the vessel to destination "},"next":{"block":{"type":"blockDriveBaseDrive","id":"XvlY6Dt-`!|$W-4,)!M*","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"Td:I2({6g;@CbWlsA?%5","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"Vb~q/:_j%(Nh)HTR5,k[","fields":{"VALUE0":140}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"]^odJ/1Iq$*Zh/QgLf-*","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"??0oeg%gOEBNY|JvHw/D","extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_DRIVE_CURVE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"W`g`db_*~pSx^N1/#qDF","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"fQ=B42aXwm0l[q^6dVVK","fields":{"VALUE0":120}}},"ARG1":{"shadow":{"type":"unit_angle","id":"0+xgLDe|+L~-AT,oXQo[","fields":{"VALUE0":183}}},"ARG2":{"shadow":{"type":"parameters_stop_4","id":"{EF}YYP:-8_zBC}N(+C#","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"}N~,oP,S,d5Mb!qFbD~+","extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":",%%lqxPZA/r|ZL^m*;U`","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"`lIN8q3o0610L8UJ+|G)","fields":{"VALUE0":700}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"|7fd`L)]Yz%lm?]`_wn[","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"fYQo*!Lg91X_],or$+8H","extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_DRIVE_CURVE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"Ik^Z:J)$qFw,sWXz;jBc","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"z,pfB;L#A*esWO|7L;3}","fields":{"VALUE0":250}}},"ARG1":{"shadow":{"type":"unit_angle","id":"GQ5]l42SLlTIGo6Z:(/=","fields":{"VALUE0":88}}},"ARG2":{"shadow":{"type":"parameters_stop_4","id":"oO7/dxya:y#3V9W;3V5)","fields":{"VALUE":"Stop.HOLD"}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}},{"type":"blockDriveBaseDrive","id":"4xE[dO$b*%Qny[^v]{N8","x":0,"y":1382,"enabled":false,"extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_DRIVE_CURVE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"EQsbxNINMRus0}G[@i-=","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"%7h5.GovnrhZ/^Jo2zf8","fields":{"VALUE0":20}}},"ARG1":{"shadow":{"type":"unit_angle","id":"?EuSPU:U94_5l5ZY;]Ef","fields":{"VALUE0":-30}}},"ARG2":{"shadow":{"type":"parameters_stop_4","id":"}4`t$|)D[SZ]!/WQ#{Yw","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"VxJ^1AL?mGYQ5^{b0=z7","enabled":false,"extraState":{"optionLevel":4},"fields":{"METHOD":"DRIVEBASE_DRIVE_CURVE"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"cPqf.uCfA9kiU1dq_i-y","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"z1cj3XyAj6oPE+?g,6*|","fields":{"VALUE0":9999}}},"ARG1":{"shadow":{"type":"unit_angle","id":"lE/T}JDWrWq4b]Ray:DE","fields":{"VALUE0":6.123456789}}},"ARG2":{"shadow":{"type":"parameters_stop_4","id":"oGKU$eDYpAVg]~+Thbpp","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"h^n`bN6;UdMAbtO:WXb!","enabled":false,"extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_DRIVE_TURN"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"d_K0Yt}-OJ~JvZ{L01]O","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angle","id":";b!rkb4}$hH6-4^4QjM4","fields":{"VALUE0":90}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"c*A$~re5d^^Q1?O1YcV@","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockDriveBaseDrive","id":"@,aXTa:=]l0U,**4Z`uj","enabled":false,"extraState":{"optionLevel":2},"fields":{"METHOD":"DRIVEBASE_DRIVE_STRAIGHT"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"7;Ucaqwex~K`#^JYc@E,","fields":{"VAR":{"id":"S}J~)lJ)`uZ@L3/Fg{a;","name":"drive base","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_distance","id":"6Ys}adp.S,KfokwD$imQ","fields":{"VALUE0":430}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"N=9`;_6fb}RlZLQJ8HfH","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockMotorRun","id":"#%`)NHS%8COLb%v-amjL","enabled":false,"extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"A,%ui*W!/*Foxy1[)k-5","fields":{"VAR":{"id":"?,ejNG]:eZ!1i|U{P![6","name":"front","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"/yZNnv;/-IICy[cbP:!~","fields":{"VALUE0":100}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"B@hn[@QLOyGYH$hO#g7Q","fields":{"VALUE0":80}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"v:y||nz9-`.I=Q]zFKfb","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockMotorRun","id":"wG?SK)^:56{3u|Id2Eqc","enabled":false,"extraState":{"optionLevel":1},"fields":{"METHOD":"MOTOR_RUN_FOR"},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"o(AG-NnVYB`P;!*Rc`?c","fields":{"VAR":{"id":"?,ejNG]:eZ!1i|U{P![6","name":"front","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_angularVelocity","id":"{@isHu6nOey]StDpIueT","fields":{"VALUE0":50}}},"ANGLE":{"shadow":{"type":"unit_angle","id":"qxPBL1:~%#NNfFxOXNeW","fields":{"VALUE0":-60}}},"THEN":{"shadow":{"type":"parameters_stop_4","id":"C)z}J`ghI$P.Cfau*OCB","fields":{"VALUE":"Stop.HOLD"}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"oQmU_=ooci5q+oD#{,Qb","type":"ColorDef"},{"name":"orange","id":"[Z?lj(=VXVon[54I[QbG","type":"ColorDef"},{"name":"yellow","id":"4~AR.P:Oj3/kc?]t`mZj","type":"ColorDef"},{"name":"green","id":"LF~UKWXr*fwWDNB2{965","type":"ColorDef"},{"name":"cyan","id":"+l2Q;DG{jb^I2{xGzS-3","type":"ColorDef"},{"name":"blue","id":"fIL.1Tz4C;:P0lKP?P8:","type":"ColorDef"},{"name":"violet","id":"F2z^YCGAyqho2pteIkYk","type":"ColorDef"},{"name":"magenta","id":"]e|dN/?~;YwQk3bj5su^","type":"ColorDef"},{"name":"white","id":"ZF$M;!;?Uadb^naVKsJK","type":"ColorDef"},{"name":"none","id":"a#iH5zu#c9Mba|m8(V56","type":"ColorDef"},{"name":"drive base","id":"S}J~)lJ)`uZ@L3/Fg{a;","type":"DriveBase"},{"name":"right","id":"1Rb_{x}94W+Y?74tRc6U","type":"Motor"},{"name":"left","id":"Y.3O{:6f|={+?vh!6ij+","type":"Motor"},{"name":"front","id":"?,ejNG]:eZ!1i|U{P![6","type":"Motor"}],"info":{"type":"pybricks","version":"1.2.3"}}
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up all devices.
right = Motor(Port.A, Direction.CLOCKWISE)
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
front = Motor(Port.E, Direction.CLOCKWISE)
drive_base = DriveBase(left, right, 81.6, 114)


# The main program starts here.
print('Hello, Pybricks!')
drive_base.settings(straight_speed=300)
drive_base.straight(730)
drive_base.turn(-20)
drive_base.settings(straight_speed=1000)
front.run_angle(999, 100, Stop.NONE)
front.run_angle(500, -80)
drive_base.settings(straight_speed=300)
drive_base.straight(100)
drive_base.straight(-100)
drive_base.curve(-58, 182)
drive_base.straight(-400)
drive_base.straight(75)
drive_base.straight(-80)
# Code for return home after pushing the vessel to destination
drive_base.straight(140)
drive_base.curve(120, 183)
drive_base.straight(700)
drive_base.curve(250, 88)