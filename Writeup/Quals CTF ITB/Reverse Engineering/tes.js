const function_list = [
  "prototype",
  "console",
  "1426432jlZlon",
  "24NcLsad",
  "search",
  "1437704cGeqiZ",
  "9MGLQiz",
  "__proto__",
  "1488Eulffi",
  "warn",
  "trace",
  "toString",
  "33wuVVmu",
  "log",
  "185482euNCIu",
  "8006889AWsaHN",
  "436163oydeiG",
  "bind",
  "10xVPXyQ",
  "floor",
  "length",
  "table",
  "15220632zgoPdm",
  "exception",
  "constructor",
  "39KSIZml",
  "(((.+)+)+)+$",
  "20755eGwtzy",
];
for(const func of function_list){
  if(!isNaN(parseInt(func))){
    console.log(`${func} , ${parseInt(func)}, ${function_list.indexOf(func)}`)
  }
}