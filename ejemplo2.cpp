while(sdr.Read){
string dato1 = (string)sdr["dato1"];
if(dato1 == "1"){
 //accion de acuerdo a cond1
}if(dato1 == "0"){ //si este dato ya se evaluó una vez descartarlo
// accion de acuerdo a cond2
}
}
